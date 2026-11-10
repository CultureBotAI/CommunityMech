# Cycle 14 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle 14 Isolate Baselines, Cycle 13 Stage 5 Remediated Records, and Actionable Community Records

- Review: 20261110T164500Z-c14s4-record-deep-audit
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-10T16:40:00Z
- Finished UTC: 2026-11-10T16:45:00Z
- Reviewer: antigravity-c14s4-record-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Deep per-record scientific and structural audit of 38 records (all 30 data/isolates/*.yaml records including newly curated and causal-graph-enriched Cycle 14 Stage 1/2 isolate baselines 000542, 000543, 000544, 000545, 000546, 000547, and 000548, both kb/taxa/*.yaml reusable taxon records updated with expanded UniProtKB EET evidence in Cycle 14 Stage 3, both community records remediated in Cycle 13 Stage 5 [000424, 000438], representative CommonTaxon-linked community 000385, vocabulary-blocked cadmium-immobilization coculture 000374, and 2 kb/communities/*.yaml records [000106, 000110] with newly identified actionable abundance_level gaps) at frozen Git revision c44f4b14c7bd2723af5c3c86bba43a446eaf3efc.

## Scope And Provenance

Focused per-record deep audit of all isolate baselines (30, including 7 new Cycle 14 Stage 1/2 isolates and 2 vocabulary-blocked deferred isolates: 000533 and 000534), all reusable taxon records (2), both Cycle 13 Stage 5 remediated community records (2: 000424, 000438), representative CommonTaxon-linked community (1: 000385), vocabulary-blocked cadmium-immobilization coculture (1: 000374), and 2 community records with new actionable Stage 5 remediation findings (000106, 000110).

Selection: All 30 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 2 Cycle 13 Stage 5 remediated kb/communities/*.yaml records (000424, 000438), representative CommonTaxon-linked record (000385), vocabulary-blocked coculture record (000374), and 2 kb/communities/*.yaml records (000106, 000110) surfaced by completeness audits.
Coverage: full; 38 reviewed / 38 in the declared population.
Source: git_commit at Git base c44f4b14c7bd2723af5c3c86bba43a446eaf3efc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000106 | kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml | maintained | CommunityMech:000106 (Tobacco Chemotactic Biocontrol SynCom) |
| CommunityMech:000110 | kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml | maintained | CommunityMech:000110 (Rice Phosphorus Uptake Intercropping SynCom4) |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | CommunityMech:000322 (Methylobacterium REE E-waste Platform) |
| CommunityMech:000374 | kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml | maintained | CommunityMech:000374 (Achromobacter-Enterobacter SL8-SL12 Cadmium Immobilization Coculture) |
| CommunityMech:000385 | kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml | maintained | CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium) |
| CommunityMech:000424 | kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml | maintained | CommunityMech:000424 (QY2-S1 Dehalogenimonas-Rich Brominated-Flame-Retardant Consortium) |
| CommunityMech:000438 | kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml | maintained | CommunityMech:000438 (Wine Yeast Three-Species Contact Consortium) |
| CommunityMech:000488 | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml | maintained | CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate) |
| CommunityMech:000489 | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml | maintained | CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate) |
| CommunityMech:000490 | data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml | maintained | CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate) |
| CommunityMech:000492 | data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml | maintained | CommunityMech:000492 (Intrasporangium chromatireducens Q5-1 Chromate Reduction Isolate) |
| CommunityMech:000495 | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml | maintained | CommunityMech:000495 (Ferroplasma acidiphilum ZJ Acid Mine Drainage Isolate) |
| CommunityMech:000521 | data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml | maintained | CommunityMech:000521 (Pseudomonas protegens E1BL2 Jala Maize Seed-Endophyte Isolate Baseline) |
| CommunityMech:000524 | data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml | maintained | CommunityMech:000524 (Shewanella oneidensis MR-1 SO1 Brewing-Wastewater NCM Bioleaching Isolate Baseline) |
| CommunityMech:000525 | data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml | maintained | CommunityMech:000525 (Bacillus subtilis 168 BS1 Brewing-Wastewater Ethanol-Detoxifying Isolate Baseline) |
| CommunityMech:000529 | data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml | maintained | CommunityMech:000529 (Bacillus subtilis 168 BS3 Brewing-Wastewater Metal-Resistant Isolate Baseline) |
| CommunityMech:000530 | data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml | maintained | CommunityMech:000530 (Bacillus subtilis 168 BS0 Brewing-Wastewater Wild-Type Isolate Baseline) |
| CommunityMech:000531 | data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml | maintained | CommunityMech:000531 (Microbacterium sp. BR1 Sulfadiazine-Cleaving Isolate Baseline) |
| CommunityMech:000532 | data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml | maintained | CommunityMech:000532 (Terrabacter sp. 2APm3 Sulfadiazine Axenic Isolate Baseline) |
| CommunityMech:000533 | data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml | maintained | CommunityMech:000533 (Achromobacter sp. SL8 Cadmium Immobilization Isolate Baseline) |
| CommunityMech:000534 | data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml | maintained | CommunityMech:000534 (Enterobacter sp. SL12 Cadmium Immobilization Isolate Baseline) |
| CommunityMech:000536 | data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml | maintained | CommunityMech:000536 (Pseudomonas sp. ZM-1 Prometryn-Degrading Isolate Baseline) |
| CommunityMech:000537 | data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml | maintained | CommunityMech:000537 (Achromobacter sp. ZM-2 Prometryn-Degrading Isolate Baseline) |
| CommunityMech:000538 | data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml | maintained | CommunityMech:000538 (Stenotrophomonas sp. ZM-3 Prometryn-Degrading Isolate Baseline) |
| CommunityMech:000539 | data/isolates/Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml | maintained | CommunityMech:000539 (Rhodopseudomonas palustris CGA676 Anaerobic Monoculture Baseline) |
| CommunityMech:000540 | data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml | maintained | CommunityMech:000540 (Escherichia coli PFM2 Anaerobic Monoculture Baseline) |
| CommunityMech:000542 | data/isolates/Escherichia_Coli_GL10_Glucose_D_Lactate_Isolate_Baseline.yaml | maintained | CommunityMech:000542 (Escherichia coli GL10 Glucose-Specialized D-Lactate Isolate Baseline) |
| CommunityMech:000543 | data/isolates/Escherichia_Coli_XL12_Xylose_D_Lactate_Isolate_Baseline.yaml | maintained | CommunityMech:000543 (Escherichia coli XL12 Xylose-Specialized D-Lactate Isolate Baseline) |
| CommunityMech:000544 | data/isolates/Escherichia_Coli_XL5_PTS_Deficient_D_Lactate_Isolate_Baseline.yaml | maintained | CommunityMech:000544 (Escherichia coli XL5 PTS/Glucokinase-Deficient Intermediate Isolate Baseline) |
| CommunityMech:000545 | data/isolates/Bifidobacterium_Bifidum_JCM1254_2FL_FOS_Monoculture_Baseline.yaml | maintained | CommunityMech:000545 (Bifidobacterium bifidum JCM1254 2'-FL/FOS Anaerobic Monoculture Baseline) |
| CommunityMech:000546 | data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml | maintained | CommunityMech:000546 (Faecalibacterium prausnitzii A2-165 2'-FL/FOS Anaerobic Monoculture Baseline) |
| CommunityMech:000547 | data/isolates/Ramichloridium_Apiculatum_CMS1_Wollastonite_Bioleaching_Isolate_Baseline.yaml | maintained | CommunityMech:000547 (Ramichloridium apiculatum CMS-1 Wollastonite Bioleaching Isolate Baseline) |
| CommunityMech:000548 | data/isolates/Talaromyces_Pseudofuniculosus_Hzt3_Wollastonite_Bioleaching_Isolate_Baseline.yaml | maintained | CommunityMech:000548 (Talaromyces pseudofuniculosus hzt-3' Wollastonite Bioleaching Isolate Baseline) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (Shewanella oneidensis MR-1) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (Geobacter sulfurreducens) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on 38 deep-audit records | passed | True | CommunityMech:000106, CommunityMech:000110, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000374, CommunityMech:000385, CommunityMech:000424, CommunityMech:000438, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000521, CommunityMech:000524, CommunityMech:000525, CommunityMech:000529, CommunityMech:000530, CommunityMech:000531, CommunityMech:000532, CommunityMech:000533, CommunityMech:000534, CommunityMech:000536, CommunityMech:000537, CommunityMech:000538, CommunityMech:000539, CommunityMech:000540, CommunityMech:000542, CommunityMech:000543, CommunityMech:000544, CommunityMech:000545, CommunityMech:000546, CommunityMech:000547, CommunityMech:000548, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 36 MicrobialCommunity records and 2 CommonTaxon files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| NetworkIntegrityAuditor check on 38 deep-audit records | passed | True | CommunityMech:000106, CommunityMech:000110, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000374, CommunityMech:000385, CommunityMech:000424, CommunityMech:000438, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000521, CommunityMech:000524, CommunityMech:000525, CommunityMech:000529, CommunityMech:000530, CommunityMech:000531, CommunityMech:000532, CommunityMech:000533, CommunityMech:000534, CommunityMech:000536, CommunityMech:000537, CommunityMech:000538, CommunityMech:000539, CommunityMech:000540, CommunityMech:000542, CommunityMech:000543, CommunityMech:000544, CommunityMech:000545, CommunityMech:000546, CommunityMech:000547, CommunityMech:000548, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 36/36 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor with 0 warnings. |

## Scientific And Domain Assessments

### Deep per-record audit of CommunityMech:000106 (Tobacco Chemotactic Biocontrol SynCom)

completeness: concern. Targets: CommunityMech:000106.

Record CommunityMech:000106 (kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml) in cohort RHIZOSPHERE has Completeness Score 87/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000110 (Rice Phosphorus Uptake Intercropping SynCom4)

completeness: concern. Targets: CommunityMech:000110.

Record CommunityMech:000110 (kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml) in cohort RHIZOSPHERE has Completeness Score 92/100, 4 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)

completeness: supported. Targets: CommunityMech:000273.

Record CommunityMech:000273 (data/isolates/Chromobacterium_Gold_Biocyanidation.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 91/100, 1 taxa, 4 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform)

completeness: supported. Targets: CommunityMech:000320.

Record CommunityMech:000320 (data/isolates/Aspergillus_Indium_LED_Recovery.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 91/100, 1 taxa, 5 interactions, 4 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model)

completeness: supported. Targets: CommunityMech:000321.

Record CommunityMech:000321 (data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000322 (Methylobacterium REE E-waste Platform)

completeness: supported. Targets: CommunityMech:000322.

Record CommunityMech:000322 (data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 94/100, 1 taxa, 4 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000374 (Achromobacter-Enterobacter SL8-SL12 Cadmium Immobilization Coculture)

completeness: concern. Targets: CommunityMech:000374.

Record CommunityMech:000374 (kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml) in cohort BIOREMEDIATION has Completeness Score 90/100, 2 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium)

completeness: supported. Targets: CommunityMech:000385.

Record CommunityMech:000385 (kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml) in cohort BIOMINING has Completeness Score 95/100, 2 taxa, 2 interactions, 1 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000424 (QY2-S1 Dehalogenimonas-Rich Brominated-Flame-Retardant Consortium)

completeness: supported. Targets: CommunityMech:000424.

Record CommunityMech:000424 (kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml) in cohort BIOREMEDIATION has Completeness Score 100/100, 4 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000438 (Wine Yeast Three-Species Contact Consortium)

completeness: supported. Targets: CommunityMech:000438.

Record CommunityMech:000438 (kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml) in cohort BIOTECHNOLOGY has Completeness Score 88/100, 3 taxa, 3 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate)

completeness: supported. Targets: CommunityMech:000488.

Record CommunityMech:000488 (data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 2 interactions, 1 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate)

completeness: supported. Targets: CommunityMech:000489.

Record CommunityMech:000489 (data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate)

completeness: supported. Targets: CommunityMech:000490.

Record CommunityMech:000490 (data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions, 1 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000492 (Intrasporangium chromatireducens Q5-1 Chromate Reduction Isolate)

completeness: supported. Targets: CommunityMech:000492.

Record CommunityMech:000492 (data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000495 (Ferroplasma acidiphilum ZJ Acid Mine Drainage Isolate)

completeness: supported. Targets: CommunityMech:000495.

Record CommunityMech:000495 (data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml) in cohort ISOLATES:EXTREME_ENVIRONMENT has Completeness Score 92/100, 1 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000521 (Pseudomonas protegens E1BL2 Jala Maize Seed-Endophyte Isolate Baseline)

completeness: supported. Targets: CommunityMech:000521.

Record CommunityMech:000521 (data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml) in cohort ISOLATES:RHIZOSPHERE has Completeness Score 94/100, 1 taxa, 3 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000524 (Shewanella oneidensis MR-1 SO1 Brewing-Wastewater NCM Bioleaching Isolate Baseline)

completeness: supported. Targets: CommunityMech:000524.

Record CommunityMech:000524 (data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000525 (Bacillus subtilis 168 BS1 Brewing-Wastewater Ethanol-Detoxifying Isolate Baseline)

completeness: supported. Targets: CommunityMech:000525.

Record CommunityMech:000525 (data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000529 (Bacillus subtilis 168 BS3 Brewing-Wastewater Metal-Resistant Isolate Baseline)

completeness: supported. Targets: CommunityMech:000529.

Record CommunityMech:000529 (data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000530 (Bacillus subtilis 168 BS0 Brewing-Wastewater Wild-Type Isolate Baseline)

completeness: supported. Targets: CommunityMech:000530.

Record CommunityMech:000530 (data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000531 (Microbacterium sp. BR1 Sulfadiazine-Cleaving Isolate Baseline)

completeness: supported. Targets: CommunityMech:000531.

Record CommunityMech:000531 (data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000532 (Terrabacter sp. 2APm3 Sulfadiazine Axenic Isolate Baseline)

completeness: supported. Targets: CommunityMech:000532.

Record CommunityMech:000532 (data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000533 (Achromobacter sp. SL8 Cadmium Immobilization Isolate Baseline)

completeness: concern. Targets: CommunityMech:000533.

Record CommunityMech:000533 (data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 85/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000534 (Enterobacter sp. SL12 Cadmium Immobilization Isolate Baseline)

completeness: concern. Targets: CommunityMech:000534.

Record CommunityMech:000534 (data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 85/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000536 (Pseudomonas sp. ZM-1 Prometryn-Degrading Isolate Baseline)

completeness: supported. Targets: CommunityMech:000536.

Record CommunityMech:000536 (data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000537 (Achromobacter sp. ZM-2 Prometryn-Degrading Isolate Baseline)

completeness: supported. Targets: CommunityMech:000537.

Record CommunityMech:000537 (data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000538 (Stenotrophomonas sp. ZM-3 Prometryn-Degrading Isolate Baseline)

completeness: supported. Targets: CommunityMech:000538.

Record CommunityMech:000538 (data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000539 (Rhodopseudomonas palustris CGA676 Anaerobic Monoculture Baseline)

completeness: supported. Targets: CommunityMech:000539.

Record CommunityMech:000539 (data/isolates/Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml) in cohort ISOLATES:SYNTROPHY has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000540 (Escherichia coli PFM2 Anaerobic Monoculture Baseline)

completeness: supported. Targets: CommunityMech:000540.

Record CommunityMech:000540 (data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml) in cohort ISOLATES:SYNTROPHY has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000542 (Escherichia coli GL10 Glucose-Specialized D-Lactate Isolate Baseline)

completeness: supported. Targets: CommunityMech:000542.

Record CommunityMech:000542 (data/isolates/Escherichia_Coli_GL10_Glucose_D_Lactate_Isolate_Baseline.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000543 (Escherichia coli XL12 Xylose-Specialized D-Lactate Isolate Baseline)

completeness: supported. Targets: CommunityMech:000543.

Record CommunityMech:000543 (data/isolates/Escherichia_Coli_XL12_Xylose_D_Lactate_Isolate_Baseline.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000544 (Escherichia coli XL5 PTS/Glucokinase-Deficient Intermediate Isolate Baseline)

completeness: supported. Targets: CommunityMech:000544.

Record CommunityMech:000544 (data/isolates/Escherichia_Coli_XL5_PTS_Deficient_D_Lactate_Isolate_Baseline.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000545 (Bifidobacterium bifidum JCM1254 2'-FL/FOS Anaerobic Monoculture Baseline)

completeness: supported. Targets: CommunityMech:000545.

Record CommunityMech:000545 (data/isolates/Bifidobacterium_Bifidum_JCM1254_2FL_FOS_Monoculture_Baseline.yaml) in cohort ISOLATES:DIET has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000546 (Faecalibacterium prausnitzii A2-165 2'-FL/FOS Anaerobic Monoculture Baseline)

completeness: supported. Targets: CommunityMech:000546.

Record CommunityMech:000546 (data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml) in cohort ISOLATES:DIET has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000547 (Ramichloridium apiculatum CMS-1 Wollastonite Bioleaching Isolate Baseline)

completeness: supported. Targets: CommunityMech:000547.

Record CommunityMech:000547 (data/isolates/Ramichloridium_Apiculatum_CMS1_Wollastonite_Bioleaching_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000548 (Talaromyces pseudofuniculosus hzt-3' Wollastonite Bioleaching Isolate Baseline)

completeness: supported. Targets: CommunityMech:000548.

Record CommunityMech:000548 (data/isolates/Talaromyces_Pseudofuniculosus_Hzt3_Wollastonite_Bioleaching_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000001 (Shewanella oneidensis MR-1)

completeness: supported. Targets: CommunityMech:taxon:000001.

Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 5 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000002 (Geobacter sulfurreducens)

completeness: supported. Targets: CommunityMech:taxon:000002.

Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 4 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

## Findings

### c14s4-000106-tobacco-chemotactic-syncom-abundance-levels: Both chemotactic SynCom member rows in Tobacco_Chemotactic_Biocontrol_SynCom (CommunityMech:000106) omit abundance_level despite explicit equal 5% (v/w) strain inoculation in PMID:40670700

major / open / confirmed; issue key: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels.

In kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml (CommunityMech:000106), Pseudomonas sp. (taxonomy[0], NCBITaxon:306, functional_role: [CROSS_FEEDER]) and Bacillus sp. (taxonomy[1], NCBITaxon:1386, functional_role: [CROSS_FEEDER]) both omit controlled abundance_level and direct equal-inoculation evidence in taxonomy[].evidence. The cited open-access study (PMID:40670700, doi:10.1007/s00253-025-13561-8) explicitly establishes in Materials and Methods ('Creation of bacterial fertilizer for chemotactic SynCom') that 'Each strain used in the chemotactic SynCom was inoculated into the composite nutrient at a 5% (v/w) ratio, along with the corresponding prebiotics screened in the previous experiment.' Setting abundance_level: DOMINANT and attaching this verbatim PMID:40670700 equal-inoculation snippet on taxonomy[0] and taxonomy[1] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level; proportional Completeness Score 87/100 -&gt; 92/100; scripts/audit_completeness.py score 80/100 -&gt; 95/100).

### c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels: All four defined rice rhizosphere SynCom4 members in Rice_P_Uptake_Intercropping_SynCom4 (CommunityMech:000110) omit abundance_level despite explicit 1 x 10^8 CFU/g equal-density SynCom assembly in PMID:39684532

major / open / confirmed; issue key: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels.

In kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml (CommunityMech:000110), Variovorax paradoxus (taxonomy[0], NCBITaxon:34073, functional_role: [CROSS_FEEDER]), Novosphingobium subterraneum (taxonomy[1], NCBITaxon:48936, functional_role: [CROSS_FEEDER]), Hydrogenophaga pseudoflava (taxonomy[2], NCBITaxon:47421, functional_role: [CROSS_FEEDER]), and Acidovorax sp. (taxonomy[3], NCBITaxon:12916, functional_role: [CROSS_FEEDER]) all omit controlled abundance_level and direct equal-density inoculation evidence in taxonomy[].evidence. The cited open-access study (PMID:39684532, doi:10.3390/ijms252312819) explicitly establishes in Section 2.1 ('Four isolates were selected from enriched genera that closely matched their corresponding ASV sequences; i.e., Novosphingobium subterraneum (ASV995, 98.02%), Hydrogenophaga pseudoflava ( ASV44940 , 99.07%), Acidovorax sp. ( ASV57550 , 100%), and Variovorax paradoxus (ASV7847, 97.22%).') and in Section 4.4 ('Glasshouse Pot Experiments') that 'The concentration of the cultured bacterial strain was adjusted to 1 × 108 CFU/g with sterilized water. A 15 mL suspension of this SynCom was injected into the sterilized soil; sterilized water served as a control.' Setting abundance_level: DOMINANT and attaching this verbatim PMID:39684532 equal-density SynCom inoculation snippet on taxonomy[0..3] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/4 -&gt; 4/4 taxa with abundance_level; proportional Completeness Score 92/100 -&gt; 97/100; scripts/audit_completeness.py score 80/100 -&gt; 95/100).

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

## Recommended Actions And Acceptance Checks

### act-populate-tobacco-chemotactic-syncom-abundance-levels

Add abundance_level: DOMINANT and verbatim equal-ratio (5% v/w) inoculation evidence from PMID:40670700 (doi:10.1007/s00253-025-13561-8) to Pseudomonas sp. (taxonomy[0], NCBITaxon:306) and Bacillus sp. (taxonomy[1], NCBITaxon:1386) on CommunityMech:000106, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
- just validate-history history

### act-populate-rice-p-uptake-intercropping-syncom4-abundance-levels

Add abundance_level: DOMINANT and verbatim equal-density (1 x 10^8 CFU/g) SynCom inoculation evidence from PMID:39684532 (doi:10.3390/ijms252312819) to Variovorax paradoxus (taxonomy[0], NCBITaxon:34073), Novosphingobium subterraneum (taxonomy[1], NCBITaxon:48936), Hydrogenophaga pseudoflava (taxonomy[2], NCBITaxon:47421), and Acidovorax sp. (taxonomy[3], NCBITaxon:12916) on CommunityMech:000110, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
- just validate-history history

### act-defer-vocabulary-blocked-cadmium-findings-c14s4-batch

Retain deferred FunctionalRoleEnum vocabulary-gap findings on CommunityMech:000374, CommunityMech:000533, and CommunityMech:000534 under open GitHub issue #2194 (#301) until a heavy-metal-immobilizer / metal-detoxifier value is added to FunctionalRoleEnum.

- Verify FunctionalRoleEnum expansion in src/communitymech/schema/communitymech.yaml (#2194) before assigning functional_role on inorganic Cd2+ immobilization records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and CommonTaxon classes | supports | All 512 kb/communities/*.yaml, 30 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (544 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 544 records | supports | Proportional 100-point review-communities Completeness Score audit across all 542 MicrobialCommunity records (min 50, median 94, mean 91.37, max 100; CommunityMech:000106 = 87/100 [s_ab = 0/5], CommunityMech:000110 = 92/100 [s_ab = 0/5], CommunityMech:000374 = 90/100 [s_fr = 0/10], CommunityMech:000533 = 85/100 [s_fr = 0/10, external_resources = 0/5], CommunityMech:000534 = 85/100 [s_fr = 0/10, external_resources = 0/5]) and 2 CommonTaxon files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (542/542), while scripts/audit_completeness.py:calculate_completeness() scores 000106 at 80/100, 000110 at 80/100, 000374 at 40/100, 000533 at 25/100, and 000534 at 25/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 512 kb/communities and 30 data/isolates records found 495/512 communities and 30/30 isolates with 0 warnings (including all 36/36 MicrobialCommunity records in the 38-record deep audit) and 17 community records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-543 | supports | Corpus-wide causal graph inventory covers all 542 MicrobialCommunity records (512 kb/communities/*.yaml and 30 data/isolates/*.yaml) through CommunityMech:000548 with 100% SHA-256 attestation in verify_causal_graph_reviews.py after Cycle 14 Stage 2 (#2752). |
| ev-common-taxon-linkage-audit | kb/taxa/Shewanella_oneidensis_MR1.yaml; TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem entries | supports | Corpus-wide audit of reusable taxon cross-references confirmed 22 TaxonomicComposition.common_taxon links across 21 MicrobialCommunity records (20 kb/communities/*.yaml records and 1 data/isolates/*.yaml record: 6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 33 verified EvidenceItems] and 15 Shewanella oneidensis communities plus isolate baseline CommunityMech:000524 linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 41 verified EvidenceItems; 74 total EvidenceItems], with CommunityMech:000177 linking to both) after Cycle 14 Stage 3 (#2753). |
| ev-tobacco-chemotactic-syncom-pmid40670700 | PMID:40670700; kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml | supports | PMID:40670700 (doi:10.1007/s00253-025-13561-8) establishes that the chemotactic tobacco rhizosphere SynCom comprises two Pseudomonas strains (Y364, Y832; NCBITaxon:306) and one Bacillus strain (Y878; NCBITaxon:1386), and that each SynCom strain was inoculated at an equal 5% (v/w) ratio into the composite organic fertilizer. |
| ev-rice-p-uptake-intercropping-syncom4-pmid39684532 | PMID:39684532; kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml | supports | PMID:39684532 (doi:10.3390/ijms252312819) establishes that Variovorax paradoxus (ASV7847, NCBITaxon:34073), Novosphingobium subterraneum (ASV995, NCBITaxon:48936), Hydrogenophaga pseudoflava (ASV44940, NCBITaxon:47421), and Acidovorax sp. (ASV57550, NCBITaxon:12916) were selected from enriched intercropped-rice genera, cultured in their respective liquid media, adjusted to 1 × 10^8 CFU/g with sterilized water, and injected as a 15 mL four-strain SynCom suspension into sterilized soil. |
| ev-achromobacter-enterobacter-sl8-sl12-pmid42307251 | PMID:42307251; kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml, data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml, data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml | supports | PMID:42307251 (doi:10.1128/spectrum.01081-26) establishes that Achromobacter sp. SL8 (NCBITaxon:222) and Enterobacter sp. SL12 (NCBITaxon:547) are primary cadmium-detoxifying and cadmium-immobilizing bacteria in both the defined SL8-SL12 coculture (CommunityMech:000374) and the single-strain monoculture isolate baselines (CommunityMech:000533 and CommunityMech:000534); inorganic Cd2+ immobilization remains deferred under open issue #2194 (#301) until FunctionalRoleEnum adds a metal-immobilizer / metal-detoxifier value. |
| ev-prior-structured-reviews | reviews/structured; 274 retained structured review bundles through 20261110T032500Z-c13s5-remediation-verification | context_only | Lineage inspection of all 274 prior structured reviews and Cycle 13 Stage 5 evidence.yaml confirmed that both Cycle 13 Stage 4 abundance_level findings across CommunityMech:000424 and 000438 were resolved in Cycle 13 Stage 5 (#2747, PR #2748), 3 FunctionalRoleEnum vocabulary-gap findings across CommunityMech:000374, 000533, and 000534 remain deferred under #2194, and 7 record-scoped source-limited findings remain deferred at commit c44f4b14c7bd2723af5c3c86bba43a446eaf3efc. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Three cadmium-immobilization records (CommunityMech:000374, 000533, 000534) remain deferred under open GitHub issue #2194 (#301) until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier value.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T164500Z-c14s4-record-deep-audit
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 14 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle
  14 Isolate Baselines, Cycle 13 Stage 5 Remediated Records, and Actionable Community
  Records
started_at: '2026-11-10T16:40:00Z'
finished_at: '2026-11-10T16:45:00Z'
reviewer:
  identity: antigravity-c14s4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 14 Stage 4 read-only review pass over frozen
    commit c44f4b14c7bd2723af5c3c86bba43a446eaf3efc without record mutation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
native_verdict: 'NEEDS_CURATION (2 P2 major open findings across CommunityMech:000106
  and 000110; 3 P3 minor vocabulary-blocked findings deferred under #2194 across CommunityMech:000374,
  000533, and 000534; 33 isolate/taxon/C13S5-remediated/CommonTaxon-linked records
  pass with 0 defects)'
scientific_review: true
summary: Deep per-record scientific and structural audit of 38 records (all 30 data/isolates/*.yaml
  records including newly curated and causal-graph-enriched Cycle 14 Stage 1/2 isolate
  baselines 000542, 000543, 000544, 000545, 000546, 000547, and 000548, both kb/taxa/*.yaml
  reusable taxon records updated with expanded UniProtKB EET evidence in Cycle 14
  Stage 3, both community records remediated in Cycle 13 Stage 5 [000424, 000438],
  representative CommonTaxon-linked community 000385, vocabulary-blocked cadmium-immobilization
  coculture 000374, and 2 kb/communities/*.yaml records [000106, 000110] with newly
  identified actionable abundance_level gaps) at frozen Git revision c44f4b14c7bd2723af5c3c86bba43a446eaf3efc.
source:
  git_revision: c44f4b14c7bd2723af5c3c86bba43a446eaf3efc
  state: git_commit
  inputs:
  - path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
    sha256: 0680fbc0c1ee94f3a79ce13d9c6b3d8b91317022addca4c095195a37974b6d0e
    role: target
  - path: data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml
    sha256: 54d10773f390acfaf392996a1ce4bb25978fb6f0d3cc1d10657c4626fef56819
    role: target
  - path: data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml
    sha256: 1183e9ac2b3567f395e7f19cceb575ac15227bc4ce1323736c042d1fbd43fb4b
    role: target
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    sha256: c9ebc23ad2748751ae6a42fbc2340c5f7524a7aa38185bcad4602b7e56734d9d
    role: target
  - path: data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml
    sha256: 452de842b34bb5c9073f31331ddef8f120323f5a934257e9a9db1e5e8f043f43
    role: target
  - path: data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml
    sha256: 165451ae89b467384dae87f9e5ef00d4b68fc7823037b3b96226e632bf186947
    role: target
  - path: data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml
    sha256: 42834ab5f80c67edd88527a323dfa94514b440d63891e4fd88790b50a230cf28
    role: target
  - path: data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml
    sha256: 7ad94b96c56469311346da8af429fb922eaa122a96464121697282771c45120e
    role: target
  - path: data/isolates/Bifidobacterium_Bifidum_JCM1254_2FL_FOS_Monoculture_Baseline.yaml
    sha256: 8190e352c3a803e85e2ab6b64a1791a6f14b2ea93dab2173c1ef653ea9e0a216
    role: target
  - path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    sha256: 3f3fe69bc250a439ff851305a95d485ad1deee50602335de11b36601542e04d4
    role: target
  - path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    sha256: 4eb42a867f2b2b1489c4ef4fa95e408d241a54d0e2bfb1cf9474dd407d036b86
    role: target
  - path: data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
    sha256: 68a2f6ea9b523e7db0eacf6ef1a87af5227cd3f6c7e93be14facffc265232796
    role: target
  - path: data/isolates/Escherichia_Coli_GL10_Glucose_D_Lactate_Isolate_Baseline.yaml
    sha256: a747c09cf287a252aa4e8fc66485fd6aa337d320cb7903c8a92d101a44855dc0
    role: target
  - path: data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml
    sha256: 991e85326303854835a6a7481d1599e068f4d67411856fbb8092620953919b18
    role: target
  - path: data/isolates/Escherichia_Coli_XL12_Xylose_D_Lactate_Isolate_Baseline.yaml
    sha256: c19c097c6068fa07ecdd2e9533d2d6a2225637a5a594ff14b21ef3a86f6d2e9f
    role: target
  - path: data/isolates/Escherichia_Coli_XL5_PTS_Deficient_D_Lactate_Isolate_Baseline.yaml
    sha256: 4105ae978347925a7541a5bd66f6ceadc35bd4bda35683f70bffca35b36ab79f
    role: target
  - path: data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
    sha256: b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790
    role: target
  - path: data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml
    sha256: 58f2d2fd0be0be26c7519de2e31f5cc80a9dbb2a43932a242dc27fc832e1a492
    role: target
  - path: data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml
    sha256: cc05785add2613ee69f29971820f913e038de75e44d584a3d8ec22015377c0f1
    role: target
  - path: data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml
    sha256: 3be922d81b044ad742cd52ae866f3007d2f17141fc7355c4a34ad9f96ca304c4
    role: target
  - path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    sha256: 70d9761a556a3e744eb81c26f1906bb0ce697b3d64be526ecaafddea7404f978
    role: target
  - path: data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml
    sha256: c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5
    role: target
  - path: data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml
    sha256: 64b3114cddeee0140d34709e04dd0510dbc62710da0a73810629133c72147f71
    role: target
  - path: data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml
    sha256: 61b09aef22790ae6960d309edc1a1a51fffca8c659ed04be36fa08fecdd2ccf9
    role: target
  - path: data/isolates/Ramichloridium_Apiculatum_CMS1_Wollastonite_Bioleaching_Isolate_Baseline.yaml
    sha256: d772c9002f1af1474616567beadbdd148c9724daf6e910b5a242621d04cc1f30
    role: target
  - path: data/isolates/Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml
    sha256: ad02b70b47aa8cd86d7949e08c3ce23366c1caec6c5463c74cd45a9396aac666
    role: target
  - path: data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml
    sha256: 671bdcdf702788c7280e49be29c0e95455be1ca1ded72119ede0b0da864154f1
    role: target
  - path: data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml
    sha256: c41cdba4bbbd54b987db9e8f901658ae1e76c79524a8cf9b2ac8ae271044bc4f
    role: target
  - path: data/isolates/Talaromyces_Pseudofuniculosus_Hzt3_Wollastonite_Bioleaching_Isolate_Baseline.yaml
    sha256: 5963957669bdfef206891e57c3b354d0ef934edb13e840651edd73f113d3d900
    role: target
  - path: data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml
    sha256: 81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e
    role: target
  - path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    sha256: eeef4a3c72f6660c2263fe91ec7858610797c19fa513bf641e2a6234ff4414d4
    role: target
  - path: kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
    sha256: 2eede18215821618a8acacbe5d47754774d268e044e47b80368100e8e4927fc0
    role: target
  - path: kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
    sha256: 9a5de564abd6e776d8f8eb5717c5d11d60cdf85a27414c0b58df620fae74dd9e
    role: target
  - path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    sha256: bc1fb667da9be21480d7f27961b01fc547c45dc3cef1ca63b58fe01584104076
    role: target
  - path: kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
    sha256: 2d1851c88c385f813706b923eeb0754bf70bbac4dd94fb15369bf5e45317e371
    role: target
  - path: kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
    sha256: 16e610d3f506c025d952d08666dceb99d94b774deef5578d5fb6f3e9d5f22d5a
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: cdde2dcc8804f32aea582cd32f6e0933923bf70a2909aaa0aa0cccf008502730
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: e7c38a51a1769c01b7f930f1bd67b8910d0db1fedae0093256435bf438e3eaf5
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
    sha256: 301fe04f778a729c1b0ac07e38d6f7950ccf4add6a7cee7da8824200b65d42a3
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: 378ef45aed3a6b1a96d4a807600f45ea0ad3a036a63375233f640d0efee56567
    role: context
scope:
  description: 'Focused per-record deep audit of all isolate baselines (30, including
    7 new Cycle 14 Stage 1/2 isolates and 2 vocabulary-blocked deferred isolates:
    000533 and 000534), all reusable taxon records (2), both Cycle 13 Stage 5 remediated
    community records (2: 000424, 000438), representative CommonTaxon-linked community
    (1: 000385), vocabulary-blocked cadmium-immobilization coculture (1: 000374),
    and 2 community records with new actionable Stage 5 remediation findings (000106,
    000110).'
  selection: All 30 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 2 Cycle 13 Stage 5
    remediated kb/communities/*.yaml records (000424, 000438), representative CommonTaxon-linked
    record (000385), vocabulary-blocked coculture record (000374), and 2 kb/communities/*.yaml
    records (000106, 000110) surfaced by completeness audits.
  coverage: full
  population_size: 38
  reviewed_target_ids:
  - CommunityMech:000106
  - CommunityMech:000110
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000374
  - CommunityMech:000385
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000521
  - CommunityMech:000524
  - CommunityMech:000525
  - CommunityMech:000529
  - CommunityMech:000530
  - CommunityMech:000531
  - CommunityMech:000532
  - CommunityMech:000533
  - CommunityMech:000534
  - CommunityMech:000536
  - CommunityMech:000537
  - CommunityMech:000538
  - CommunityMech:000539
  - CommunityMech:000540
  - CommunityMech:000542
  - CommunityMech:000543
  - CommunityMech:000544
  - CommunityMech:000545
  - CommunityMech:000546
  - CommunityMech:000547
  - CommunityMech:000548
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
targets:
- target_id: CommunityMech:000106
  path: kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
  label: CommunityMech:000106 (Tobacco Chemotactic Biocontrol SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000110
  path: kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
  label: CommunityMech:000110 (Rice Phosphorus Uptake Intercropping SynCom4)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000273
  path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  label: CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000320
  path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  label: CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000321
  path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  label: CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000322
  path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  label: CommunityMech:000322 (Methylobacterium REE E-waste Platform)
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
- target_id: CommunityMech:000385
  path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
  label: CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium)
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
- target_id: CommunityMech:000488
  path: data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml
  label: CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption
    Isolate)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000489
  path: data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml
  label: CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal
    Bioleaching Isolate)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000490
  path: data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml
  label: CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular
    Iron Respiration Isolate)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000492
  path: data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml
  label: CommunityMech:000492 (Intrasporangium chromatireducens Q5-1 Chromate Reduction
    Isolate)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000495
  path: data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml
  label: CommunityMech:000495 (Ferroplasma acidiphilum ZJ Acid Mine Drainage Isolate)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000521
  path: data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml
  label: CommunityMech:000521 (Pseudomonas protegens E1BL2 Jala Maize Seed-Endophyte
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000524
  path: data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml
  label: CommunityMech:000524 (Shewanella oneidensis MR-1 SO1 Brewing-Wastewater NCM
    Bioleaching Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000525
  path: data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml
  label: CommunityMech:000525 (Bacillus subtilis 168 BS1 Brewing-Wastewater Ethanol-Detoxifying
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000529
  path: data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml
  label: CommunityMech:000529 (Bacillus subtilis 168 BS3 Brewing-Wastewater Metal-Resistant
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000530
  path: data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml
  label: CommunityMech:000530 (Bacillus subtilis 168 BS0 Brewing-Wastewater Wild-Type
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000531
  path: data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml
  label: CommunityMech:000531 (Microbacterium sp. BR1 Sulfadiazine-Cleaving Isolate
    Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000532
  path: data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml
  label: CommunityMech:000532 (Terrabacter sp. 2APm3 Sulfadiazine Axenic Isolate Baseline)
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
- target_id: CommunityMech:000536
  path: data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml
  label: CommunityMech:000536 (Pseudomonas sp. ZM-1 Prometryn-Degrading Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000537
  path: data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml
  label: CommunityMech:000537 (Achromobacter sp. ZM-2 Prometryn-Degrading Isolate
    Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000538
  path: data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml
  label: CommunityMech:000538 (Stenotrophomonas sp. ZM-3 Prometryn-Degrading Isolate
    Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000539
  path: data/isolates/Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml
  label: CommunityMech:000539 (Rhodopseudomonas palustris CGA676 Anaerobic Monoculture
    Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000540
  path: data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml
  label: CommunityMech:000540 (Escherichia coli PFM2 Anaerobic Monoculture Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000542
  path: data/isolates/Escherichia_Coli_GL10_Glucose_D_Lactate_Isolate_Baseline.yaml
  label: CommunityMech:000542 (Escherichia coli GL10 Glucose-Specialized D-Lactate
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000543
  path: data/isolates/Escherichia_Coli_XL12_Xylose_D_Lactate_Isolate_Baseline.yaml
  label: CommunityMech:000543 (Escherichia coli XL12 Xylose-Specialized D-Lactate
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000544
  path: data/isolates/Escherichia_Coli_XL5_PTS_Deficient_D_Lactate_Isolate_Baseline.yaml
  label: CommunityMech:000544 (Escherichia coli XL5 PTS/Glucokinase-Deficient Intermediate
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000545
  path: data/isolates/Bifidobacterium_Bifidum_JCM1254_2FL_FOS_Monoculture_Baseline.yaml
  label: CommunityMech:000545 (Bifidobacterium bifidum JCM1254 2'-FL/FOS Anaerobic
    Monoculture Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000546
  path: data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
  label: CommunityMech:000546 (Faecalibacterium prausnitzii A2-165 2'-FL/FOS Anaerobic
    Monoculture Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000547
  path: data/isolates/Ramichloridium_Apiculatum_CMS1_Wollastonite_Bioleaching_Isolate_Baseline.yaml
  label: CommunityMech:000547 (Ramichloridium apiculatum CMS-1 Wollastonite Bioleaching
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000548
  path: data/isolates/Talaromyces_Pseudofuniculosus_Hzt3_Wollastonite_Bioleaching_Isolate_Baseline.yaml
  label: CommunityMech:000548 (Talaromyces pseudofuniculosus hzt-3' Wollastonite Bioleaching
    Isolate Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:taxon:000001
  path: kb/taxa/Shewanella_oneidensis_MR1.yaml
  label: CommunityMech:taxon:000001 (Shewanella oneidensis MR-1)
  record_class: CommonTaxon
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:taxon:000002
  path: kb/taxa/Geobacter_sulfurreducens.yaml
  label: CommunityMech:taxon:000002 (Geobacter sulfurreducens)
  record_class: CommonTaxon
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-deep-c14s4
  name: LinkML schema validation on 38 deep-audit records
  status: passed
  required: true
  summary: All 36 MicrobialCommunity records and 2 CommonTaxon files validate against
    src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000106
  - CommunityMech:000110
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000374
  - CommunityMech:000385
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000521
  - CommunityMech:000524
  - CommunityMech:000525
  - CommunityMech:000529
  - CommunityMech:000530
  - CommunityMech:000531
  - CommunityMech:000532
  - CommunityMech:000533
  - CommunityMech:000534
  - CommunityMech:000536
  - CommunityMech:000537
  - CommunityMech:000538
  - CommunityMech:000539
  - CommunityMech:000540
  - CommunityMech:000542
  - CommunityMech:000543
  - CommunityMech:000544
  - CommunityMech:000545
  - CommunityMech:000546
  - CommunityMech:000547
  - CommunityMech:000548
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -c 'validate 38 deep-audit records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-deep-c14s4
  name: NetworkIntegrityAuditor check on 38 deep-audit records
  status: passed
  required: true
  summary: All 36/36 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor
    with 0 warnings.
  target_ids:
  - CommunityMech:000106
  - CommunityMech:000110
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000374
  - CommunityMech:000385
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000521
  - CommunityMech:000524
  - CommunityMech:000525
  - CommunityMech:000529
  - CommunityMech:000530
  - CommunityMech:000531
  - CommunityMech:000532
  - CommunityMech:000533
  - CommunityMech:000534
  - CommunityMech:000536
  - CommunityMech:000537
  - CommunityMech:000538
  - CommunityMech:000539
  - CommunityMech:000540
  - CommunityMech:000542
  - CommunityMech:000543
  - CommunityMech:000544
  - CommunityMech:000545
  - CommunityMech:000546
  - CommunityMech:000547
  - CommunityMech:000548
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -m communitymech.cli audit-network
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-network-integrity-audit
evidence:
- evidence_id: ev-schema-validation-gate
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity and CommonTaxon classes
  accessed_at: '2026-11-10T16:41:00Z'
  support: supports
  summary: All 512 kb/communities/*.yaml, 30 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records (544 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: scripts/audit_completeness.py
  locator: 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness()
    across all 544 records
  accessed_at: '2026-11-10T16:42:00Z'
  support: supports
  summary: Proportional 100-point review-communities Completeness Score audit across
    all 542 MicrobialCommunity records (min 50, median 94, mean 91.37, max 100; CommunityMech:000106
    = 87/100 [s_ab = 0/5], CommunityMech:000110 = 92/100 [s_ab = 0/5], CommunityMech:000374
    = 90/100 [s_fr = 0/10], CommunityMech:000533 = 85/100 [s_fr = 0/10, external_resources
    = 0/5], CommunityMech:000534 = 85/100 [s_fr = 0/10, external_resources = 0/5])
    and 2 CommonTaxon files (100/100) confirmed 100% core metadata presence and 100%
    top-level environment_term coverage (542/542), while scripts/audit_completeness.py:calculate_completeness()
    scores 000106 at 80/100, 000110 at 80/100, 000374 at 40/100, 000533 at 25/100,
    and 000534 at 25/100.
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-11-10T16:42:30Z'
  support: supports
  summary: NetworkIntegrityAuditor across 512 kb/communities and 30 data/isolates
    records found 495/512 communities and 30/30 isolates with 0 warnings (including
    all 36/36 MicrobialCommunity records in the 38-record deep audit) and 17 community
    records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL
    UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0
    error-severity issues, 0 broken downstream references).
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-543
  accessed_at: '2026-11-10T16:43:00Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 542 MicrobialCommunity records
    (512 kb/communities/*.yaml and 30 data/isolates/*.yaml) through CommunityMech:000548
    with 100% SHA-256 attestation in verify_causal_graph_reviews.py after Cycle 14
    Stage 2 (#2752).
- evidence_id: ev-common-taxon-linkage-audit
  kind: record_content
  reference: kb/taxa/Shewanella_oneidensis_MR1.yaml
  locator: TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem
    entries
  accessed_at: '2026-11-10T16:43:30Z'
  support: supports
  summary: 'Corpus-wide audit of reusable taxon cross-references confirmed 22 TaxonomicComposition.common_taxon
    links across 21 MicrobialCommunity records (20 kb/communities/*.yaml records and
    1 data/isolates/*.yaml record: 6 Geobacter sulfurreducens communities linked to
    CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 33 verified EvidenceItems]
    and 15 Shewanella oneidensis communities plus isolate baseline CommunityMech:000524
    linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 41 verified
    EvidenceItems; 74 total EvidenceItems], with CommunityMech:000177 linking to both)
    after Cycle 14 Stage 3 (#2753).'
- evidence_id: ev-tobacco-chemotactic-syncom-pmid40670700
  kind: primary_source
  reference: PMID:40670700
  locator: kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
  accessed_at: '2026-11-10T16:44:00Z'
  support: supports
  summary: PMID:40670700 (doi:10.1007/s00253-025-13561-8) establishes that the chemotactic
    tobacco rhizosphere SynCom comprises two Pseudomonas strains (Y364, Y832; NCBITaxon:306)
    and one Bacillus strain (Y878; NCBITaxon:1386), and that each SynCom strain was
    inoculated at an equal 5% (v/w) ratio into the composite organic fertilizer.
  quote: Each strain used in the chemotactic SynCom was inoculated into the composite
    nutrient at a 5% (v/w) ratio, along with the corresponding prebiotics screened
    in the previous experiment.
- evidence_id: ev-rice-p-uptake-intercropping-syncom4-pmid39684532
  kind: primary_source
  reference: PMID:39684532
  locator: kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
  accessed_at: '2026-11-10T16:44:15Z'
  support: supports
  summary: PMID:39684532 (doi:10.3390/ijms252312819) establishes that Variovorax paradoxus
    (ASV7847, NCBITaxon:34073), Novosphingobium subterraneum (ASV995, NCBITaxon:48936),
    Hydrogenophaga pseudoflava (ASV44940, NCBITaxon:47421), and Acidovorax sp. (ASV57550,
    NCBITaxon:12916) were selected from enriched intercropped-rice genera, cultured
    in their respective liquid media, adjusted to 1 × 10^8 CFU/g with sterilized water,
    and injected as a 15 mL four-strain SynCom suspension into sterilized soil.
  quote: The concentration of the cultured bacterial strain was adjusted to 1 × 108
    CFU/g with sterilized water. A 15 mL suspension of this SynCom was injected into
    the sterilized soil; sterilized water served as a control.
- evidence_id: ev-achromobacter-enterobacter-sl8-sl12-pmid42307251
  kind: primary_source
  reference: PMID:42307251
  locator: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml,
    data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml,
    data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
  accessed_at: '2026-11-10T16:44:30Z'
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
  locator: 274 retained structured review bundles through 20261110T032500Z-c13s5-remediation-verification
  accessed_at: '2026-11-10T16:44:45Z'
  support: context_only
  summary: 'Lineage inspection of all 274 prior structured reviews and Cycle 13 Stage
    5 evidence.yaml confirmed that both Cycle 13 Stage 4 abundance_level findings
    across CommunityMech:000424 and 000438 were resolved in Cycle 13 Stage 5 (#2747,
    PR #2748), 3 FunctionalRoleEnum vocabulary-gap findings across CommunityMech:000374,
    000533, and 000534 remain deferred under #2194, and 7 record-scoped source-limited
    findings remain deferred at commit c44f4b14c7bd2723af5c3c86bba43a446eaf3efc.'
assessments:
- assessment_id: assess-communitymech-000106
  area: completeness
  topic: Deep per-record audit of CommunityMech:000106 (Tobacco Chemotactic Biocontrol
    SynCom)
  outcome: concern
  summary: Record CommunityMech:000106 (kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml)
    in cohort RHIZOSPHERE has Completeness Score 87/100, 2 taxa, 3 interactions, 2
    causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000106
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 87.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000110
  area: completeness
  topic: Deep per-record audit of CommunityMech:000110 (Rice Phosphorus Uptake Intercropping
    SynCom4)
  outcome: concern
  summary: Record CommunityMech:000110 (kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml)
    in cohort RHIZOSPHERE has Completeness Score 92/100, 4 taxa, 3 interactions, 2
    causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000110
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 92.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000273
  area: completeness
  topic: Deep per-record audit of CommunityMech:000273 (Chromobacterium Gold Biocyanidation
    Platform)
  outcome: supported
  summary: Record CommunityMech:000273 (data/isolates/Chromobacterium_Gold_Biocyanidation.yaml)
    in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 91/100, 1 taxa, 4 interactions,
    2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000273
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 91.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000320
  area: completeness
  topic: Deep per-record audit of CommunityMech:000320 (Aspergillus Indium LCD Recovery
    Platform)
  outcome: supported
  summary: Record CommunityMech:000320 (data/isolates/Aspergillus_Indium_LED_Recovery.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 91/100, 1 taxa, 5 interactions,
    4 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 91.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000321
  area: completeness
  topic: Deep per-record audit of CommunityMech:000321 (BioModels MODEL2204300002
    Kefir Rothia Model)
  outcome: supported
  summary: Record CommunityMech:000321 (data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml)
    in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000322
  area: completeness
  topic: Deep per-record audit of CommunityMech:000322 (Methylobacterium REE E-waste
    Platform)
  outcome: supported
  summary: Record CommunityMech:000322 (data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 94/100, 1 taxa, 4 interactions,
    2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 94.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000374
  area: completeness
  topic: Deep per-record audit of CommunityMech:000374 (Achromobacter-Enterobacter
    SL8-SL12 Cadmium Immobilization Coculture)
  outcome: concern
  summary: Record CommunityMech:000374 (kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml)
    in cohort BIOREMEDIATION has Completeness Score 90/100, 2 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 90.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000385
  area: completeness
  topic: Deep per-record audit of CommunityMech:000385 (SO3-BS3 Lithium-ion Battery
    Bioleaching Consortium)
  outcome: supported
  summary: Record CommunityMech:000385 (kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml)
    in cohort BIOMINING has Completeness Score 95/100, 2 taxa, 2 interactions, 1 causal
    edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000385
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000424
  area: completeness
  topic: Deep per-record audit of CommunityMech:000424 (QY2-S1 Dehalogenimonas-Rich
    Brominated-Flame-Retardant Consortium)
  outcome: supported
  summary: Record CommunityMech:000424 (kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml)
    in cohort BIOREMEDIATION has Completeness Score 100/100, 4 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000424
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 100.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000438
  area: completeness
  topic: Deep per-record audit of CommunityMech:000438 (Wine Yeast Three-Species Contact
    Consortium)
  outcome: supported
  summary: Record CommunityMech:000438 (kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 88/100, 3 taxa, 3 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000438
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 88.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000488
  area: completeness
  topic: Deep per-record audit of CommunityMech:000488 (Bacillus licheniformis Tannery
    Effluent Chromate Biosorption Isolate)
  outcome: supported
  summary: Record CommunityMech:000488 (data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 2 interactions,
    1 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000488
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000489
  area: completeness
  topic: Deep per-record audit of CommunityMech:000489 (Adapted Acidithiobacillus
    ferrooxidans Waste LED Metal Bioleaching Isolate)
  outcome: supported
  summary: Record CommunityMech:000489 (data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 3 interactions,
    2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000489
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000490
  area: completeness
  topic: Deep per-record audit of CommunityMech:000490 (Ferrimicrobium acidiphilum
    Acidophilic Extracellular Iron Respiration Isolate)
  outcome: supported
  summary: Record CommunityMech:000490 (data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions,
    1 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000490
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000492
  area: completeness
  topic: Deep per-record audit of CommunityMech:000492 (Intrasporangium chromatireducens
    Q5-1 Chromate Reduction Isolate)
  outcome: supported
  summary: Record CommunityMech:000492 (data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 3 interactions,
    2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000492
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000495
  area: completeness
  topic: Deep per-record audit of CommunityMech:000495 (Ferroplasma acidiphilum ZJ
    Acid Mine Drainage Isolate)
  outcome: supported
  summary: Record CommunityMech:000495 (data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml)
    in cohort ISOLATES:EXTREME_ENVIRONMENT has Completeness Score 92/100, 1 taxa,
    3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon
    links, and 0 network warnings.
  target_ids:
  - CommunityMech:000495
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 92.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000521
  area: completeness
  topic: Deep per-record audit of CommunityMech:000521 (Pseudomonas protegens E1BL2
    Jala Maize Seed-Endophyte Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000521 (data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml)
    in cohort ISOLATES:RHIZOSPHERE has Completeness Score 94/100, 1 taxa, 3 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000521
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 94.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000524
  area: completeness
  topic: Deep per-record audit of CommunityMech:000524 (Shewanella oneidensis MR-1
    SO1 Brewing-Wastewater NCM Bioleaching Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000524 (data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000524
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000525
  area: completeness
  topic: Deep per-record audit of CommunityMech:000525 (Bacillus subtilis 168 BS1
    Brewing-Wastewater Ethanol-Detoxifying Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000525 (data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000525
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000529
  area: completeness
  topic: Deep per-record audit of CommunityMech:000529 (Bacillus subtilis 168 BS3
    Brewing-Wastewater Metal-Resistant Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000529 (data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000529
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000530
  area: completeness
  topic: Deep per-record audit of CommunityMech:000530 (Bacillus subtilis 168 BS0
    Brewing-Wastewater Wild-Type Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000530 (data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000530
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000531
  area: completeness
  topic: Deep per-record audit of CommunityMech:000531 (Microbacterium sp. BR1 Sulfadiazine-Cleaving
    Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000531 (data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000531
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000532
  area: completeness
  topic: Deep per-record audit of CommunityMech:000532 (Terrabacter sp. 2APm3 Sulfadiazine
    Axenic Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000532 (data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000532
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000533
  area: completeness
  topic: Deep per-record audit of CommunityMech:000533 (Achromobacter sp. SL8 Cadmium
    Immobilization Isolate Baseline)
  outcome: concern
  summary: Record CommunityMech:000533 (data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 85/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000533
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 85.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000534
  area: completeness
  topic: Deep per-record audit of CommunityMech:000534 (Enterobacter sp. SL12 Cadmium
    Immobilization Isolate Baseline)
  outcome: concern
  summary: Record CommunityMech:000534 (data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 85/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000534
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 85.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000536
  area: completeness
  topic: Deep per-record audit of CommunityMech:000536 (Pseudomonas sp. ZM-1 Prometryn-Degrading
    Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000536 (data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000536
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000537
  area: completeness
  topic: Deep per-record audit of CommunityMech:000537 (Achromobacter sp. ZM-2 Prometryn-Degrading
    Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000537 (data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000537
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000538
  area: completeness
  topic: Deep per-record audit of CommunityMech:000538 (Stenotrophomonas sp. ZM-3
    Prometryn-Degrading Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000538 (data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000538
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000539
  area: completeness
  topic: Deep per-record audit of CommunityMech:000539 (Rhodopseudomonas palustris
    CGA676 Anaerobic Monoculture Baseline)
  outcome: supported
  summary: Record CommunityMech:000539 (data/isolates/Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml)
    in cohort ISOLATES:SYNTROPHY has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000539
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000540
  area: completeness
  topic: Deep per-record audit of CommunityMech:000540 (Escherichia coli PFM2 Anaerobic
    Monoculture Baseline)
  outcome: supported
  summary: Record CommunityMech:000540 (data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml)
    in cohort ISOLATES:SYNTROPHY has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000540
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000542
  area: completeness
  topic: Deep per-record audit of CommunityMech:000542 (Escherichia coli GL10 Glucose-Specialized
    D-Lactate Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000542 (data/isolates/Escherichia_Coli_GL10_Glucose_D_Lactate_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000542
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000543
  area: completeness
  topic: Deep per-record audit of CommunityMech:000543 (Escherichia coli XL12 Xylose-Specialized
    D-Lactate Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000543 (data/isolates/Escherichia_Coli_XL12_Xylose_D_Lactate_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000543
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000544
  area: completeness
  topic: Deep per-record audit of CommunityMech:000544 (Escherichia coli XL5 PTS/Glucokinase-Deficient
    Intermediate Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000544 (data/isolates/Escherichia_Coli_XL5_PTS_Deficient_D_Lactate_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000544
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000545
  area: completeness
  topic: Deep per-record audit of CommunityMech:000545 (Bifidobacterium bifidum JCM1254
    2'-FL/FOS Anaerobic Monoculture Baseline)
  outcome: supported
  summary: Record CommunityMech:000545 (data/isolates/Bifidobacterium_Bifidum_JCM1254_2FL_FOS_Monoculture_Baseline.yaml)
    in cohort ISOLATES:DIET has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000545
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000546
  area: completeness
  topic: Deep per-record audit of CommunityMech:000546 (Faecalibacterium prausnitzii
    A2-165 2'-FL/FOS Anaerobic Monoculture Baseline)
  outcome: supported
  summary: Record CommunityMech:000546 (data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml)
    in cohort ISOLATES:DIET has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000546
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000547
  area: completeness
  topic: Deep per-record audit of CommunityMech:000547 (Ramichloridium apiculatum
    CMS-1 Wollastonite Bioleaching Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000547 (data/isolates/Ramichloridium_Apiculatum_CMS1_Wollastonite_Bioleaching_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000547
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000548
  area: completeness
  topic: Deep per-record audit of CommunityMech:000548 (Talaromyces pseudofuniculosus
    hzt-3' Wollastonite Bioleaching Isolate Baseline)
  outcome: supported
  summary: Record CommunityMech:000548 (data/isolates/Talaromyces_Pseudofuniculosus_Hzt3_Wollastonite_Bioleaching_Isolate_Baseline.yaml)
    in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000548
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 95.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-taxon-000001
  area: completeness
  topic: Deep per-record audit of CommunityMech:taxon:000001 (Shewanella oneidensis
    MR-1)
  outcome: supported
  summary: Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml)
    in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal
    edges, 5 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:taxon:000001
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 100.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-taxon-000002
  area: completeness
  topic: Deep per-record audit of CommunityMech:taxon:000002 (Geobacter sulfurreducens)
  outcome: supported
  summary: Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml)
    in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal
    edges, 4 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:taxon:000002
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 100.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
findings:
- finding_id: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels
  issue_key: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Both chemotactic SynCom member rows in Tobacco_Chemotactic_Biocontrol_SynCom
    (CommunityMech:000106) omit abundance_level despite explicit equal 5% (v/w) strain
    inoculation in PMID:40670700
  description: 'In kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml (CommunityMech:000106),
    Pseudomonas sp. (taxonomy[0], NCBITaxon:306, functional_role: [CROSS_FEEDER])
    and Bacillus sp. (taxonomy[1], NCBITaxon:1386, functional_role: [CROSS_FEEDER])
    both omit controlled abundance_level and direct equal-inoculation evidence in
    taxonomy[].evidence. The cited open-access study (PMID:40670700, doi:10.1007/s00253-025-13561-8)
    explicitly establishes in Materials and Methods (''Creation of bacterial fertilizer
    for chemotactic SynCom'') that ''Each strain used in the chemotactic SynCom was
    inoculated into the composite nutrient at a 5% (v/w) ratio, along with the corresponding
    prebiotics screened in the previous experiment.'' Setting abundance_level: DOMINANT
    and attaching this verbatim PMID:40670700 equal-inoculation snippet on taxonomy[0]
    and taxonomy[1] raises the review-communities s_ab abundance_level rubric component
    from 0/5 to 5/5 (0/2 -> 2/2 taxa with abundance_level; proportional Completeness
    Score 87/100 -> 92/100; scripts/audit_completeness.py score 80/100 -> 95/100).'
  target_ids:
  - CommunityMech:000106
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-tobacco-chemotactic-syncom-pmid40670700
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing controlled abundance_level on both chemotactic SynCom
    member rows leaves the review-communities s_ab rubric component at 0/5 (Completeness
    Score 87/100; scripts/audit_completeness.py score 80/100) and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
- finding_id: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels
  issue_key: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: All four defined rice rhizosphere SynCom4 members in Rice_P_Uptake_Intercropping_SynCom4
    (CommunityMech:000110) omit abundance_level despite explicit 1 x 10^8 CFU/g equal-density
    SynCom assembly in PMID:39684532
  description: 'In kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml (CommunityMech:000110),
    Variovorax paradoxus (taxonomy[0], NCBITaxon:34073, functional_role: [CROSS_FEEDER]),
    Novosphingobium subterraneum (taxonomy[1], NCBITaxon:48936, functional_role: [CROSS_FEEDER]),
    Hydrogenophaga pseudoflava (taxonomy[2], NCBITaxon:47421, functional_role: [CROSS_FEEDER]),
    and Acidovorax sp. (taxonomy[3], NCBITaxon:12916, functional_role: [CROSS_FEEDER])
    all omit controlled abundance_level and direct equal-density inoculation evidence
    in taxonomy[].evidence. The cited open-access study (PMID:39684532, doi:10.3390/ijms252312819)
    explicitly establishes in Section 2.1 (''Four isolates were selected from enriched
    genera that closely matched their corresponding ASV sequences; i.e., Novosphingobium
    subterraneum (ASV995, 98.02%), Hydrogenophaga pseudoflava ( ASV44940 , 99.07%),
    Acidovorax sp. ( ASV57550 , 100%), and Variovorax paradoxus (ASV7847, 97.22%).'')
    and in Section 4.4 (''Glasshouse Pot Experiments'') that ''The concentration of
    the cultured bacterial strain was adjusted to 1 × 108 CFU/g with sterilized water.
    A 15 mL suspension of this SynCom was injected into the sterilized soil; sterilized
    water served as a control.'' Setting abundance_level: DOMINANT and attaching this
    verbatim PMID:39684532 equal-density SynCom inoculation snippet on taxonomy[0..3]
    raises the review-communities s_ab abundance_level rubric component from 0/5 to
    5/5 (0/4 -> 4/4 taxa with abundance_level; proportional Completeness Score 92/100
    -> 97/100; scripts/audit_completeness.py score 80/100 -> 95/100).'
  target_ids:
  - CommunityMech:000110
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  - taxonomy[2].abundance_level
  - taxonomy[3].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-rice-p-uptake-intercropping-syncom4-pmid39684532
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on all four defined
    rice rhizosphere SynCom4 members leaves the review-communities s_ab rubric component
    at 0/5 (Completeness Score 92/100; scripts/audit_completeness.py score 80/100)
    and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: c12s4-000533-achromobacter-sl8-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
actions:
- action_id: act-populate-tobacco-chemotactic-syncom-abundance-levels
  description: 'Add abundance_level: DOMINANT and verbatim equal-ratio (5% v/w) inoculation
    evidence from PMID:40670700 (doi:10.1007/s00253-025-13561-8) to Pseudomonas sp.
    (taxonomy[0], NCBITaxon:306) and Bacillus sp. (taxonomy[1], NCBITaxon:1386) on
    CommunityMech:000106, and append curation_history.'
  finding_ids:
  - c14s4-000106-tobacco-chemotactic-syncom-abundance-levels
  target_ids:
  - CommunityMech:000106
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
  - just validate-history history
- action_id: act-populate-rice-p-uptake-intercropping-syncom4-abundance-levels
  description: 'Add abundance_level: DOMINANT and verbatim equal-density (1 x 10^8
    CFU/g) SynCom inoculation evidence from PMID:39684532 (doi:10.3390/ijms252312819)
    to Variovorax paradoxus (taxonomy[0], NCBITaxon:34073), Novosphingobium subterraneum
    (taxonomy[1], NCBITaxon:48936), Hydrogenophaga pseudoflava (taxonomy[2], NCBITaxon:47421),
    and Acidovorax sp. (taxonomy[3], NCBITaxon:12916) on CommunityMech:000110, and
    append curation_history.'
  finding_ids:
  - c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels
  target_ids:
  - CommunityMech:000110
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
  - just validate-history history
- action_id: act-defer-vocabulary-blocked-cadmium-findings-c14s4-batch
  description: 'Retain deferred FunctionalRoleEnum vocabulary-gap findings on CommunityMech:000374,
    CommunityMech:000533, and CommunityMech:000534 under open GitHub issue #2194 (#301)
    until a heavy-metal-immobilizer / metal-detoxifier value is added to FunctionalRoleEnum.'
  finding_ids:
  - c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - c12s4-000533-achromobacter-sl8-isolate-functional-role
  - c12s4-000534-enterobacter-sl12-isolate-functional-role
  target_ids:
  - CommunityMech:000374
  - CommunityMech:000533
  - CommunityMech:000534
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
  acceptance_checks:
  - Verify FunctionalRoleEnum expansion in src/communitymech/schema/communitymech.yaml
    (#2194) before assigning functional_role on inorganic Cd2+ immobilization records.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261110T005500Z-c13s4-record-deep-audit
  relationship: prior_cycle_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261110T032500Z-c13s5-remediation-verification
  relationship: prior_cycle_stage5_remediation_review
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- 'Three cadmium-immobilization records (CommunityMech:000374, 000533, 000534) remain
  deferred under open GitHub issue #2194 (#301) until FunctionalRoleEnum adds a heavy-metal-immobilizer
  / metal-detoxifier value.'
tags:
- cycle14
- stage4
- record-review
- deep-audit
```
