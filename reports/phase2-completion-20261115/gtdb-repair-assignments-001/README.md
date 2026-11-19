# Whole-record GTDB repair assignments

Assignment only, from the retained historical classifier partition. No record is split across lanes. Other branches' ongoing repairs are not silently counted complete. Each record requires current source inspection, guarded application, native checks and immutable saved successor assessment. A new route requires one verified real canary before a batch. Full scientific review remains distinct.

Source plan SHA-256: `eaf78e16c342e36a0aa82c52c45888e8efb667fc2b70aa8d77ead956024f5f7c`.
Current-record byte check at `301f35b8d9db679f3067297317356081fa305959`.
Selected: 126 records / 418 affected taxonomy occurrences.

| Lane | Whole records |
|---|---:|
| ambiguity | 30 |
| genus | 40 |
| species | 56 |

Start with each lane's already selected canary. Complete pure groups before
mixed groups; inspect all affected occurrences together. The genus lane owns
every mixed record containing a higher-rank occurrence. The species lane
owns the two mixed groups containing both renamed and same-name species.
The ambiguity lane owns the other mixed groups and the pure unsupported case.

| Record | Lane | Affected occurrences | Source group |
|---|---|---:|---|
| CommunityMech:000003 · `kb/communities/At_RSPHERE_SynCom.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000105 · `kb/communities/Pepper_Phytophthora_SynCom5.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000275 · `kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml` | ambiguity | 1 | unsupported_or_scope_status |
| CommunityMech:000344 · `kb/communities/Klebsiella_Arthrobacter_KZ_Phenanthrene_Cadmium_SynCom.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000346 · `kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml` | ambiguity | 4 | ambiguous+same_name_species_or_strain |
| CommunityMech:000363 · `kb/communities/Synechocystis_Pseudomonas_Acetate_Butanol_Coculture.yaml` | ambiguity | 2 | ambiguous+renamed_mapping |
| CommunityMech:000365 · `kb/communities/Baijiu_Pit_Mud_Hexanoic_Acid_SynCom_G4.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000373 · `kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml` | ambiguity | 2 | ambiguous |
| CommunityMech:000376 · `kb/communities/Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom.yaml` | ambiguity | 2 | ambiguous+renamed_mapping |
| CommunityMech:000382 · `kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml` | ambiguity | 9 | ambiguous+same_name_species_or_strain |
| CommunityMech:000393 · `kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000400 · `kb/communities/Carbon_Substrate_PMSX_Biofilm_SynCom.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000401 · `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000409 · `kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` | ambiguity | 2 | ambiguous+same_name_species_or_strain |
| CommunityMech:000412 · `kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000419 · `kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` | ambiguity | 3 | ambiguous+same_name_species_or_strain |
| CommunityMech:000425 · `kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000446 · `kb/communities/Phaeodactylum_Aliivibrio_Diel_Coculture.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000460 · `kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000466 · `kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | ambiguity | 3 | ambiguous+same_name_species_or_strain |
| CommunityMech:000467 · `kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml` | ambiguity | 4 | ambiguous+same_name_species_or_strain |
| CommunityMech:000499 · `kb/communities/Cyantraniliprole_Consortium_T2.yaml` | ambiguity | 2 | ambiguous |
| CommunityMech:000500 · `kb/communities/Cyantraniliprole_Consortium_T3.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000501 · `kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml` | ambiguity | 3 | ambiguous+same_name_species_or_strain |
| CommunityMech:000505 · `kb/communities/Hexamine_Formaldehyde_Consortium_C1.yaml` | ambiguity | 2 | ambiguous+renamed_mapping |
| CommunityMech:000506 · `kb/communities/Hexamine_Formaldehyde_Consortium_C2.yaml` | ambiguity | 3 | ambiguous+renamed_mapping |
| CommunityMech:000507 · `kb/communities/Hexamine_Formaldehyde_Consortium_C3.yaml` | ambiguity | 3 | ambiguous+renamed_mapping |
| CommunityMech:000508 · `kb/communities/Hexamine_Formaldehyde_Consortium_C4.yaml` | ambiguity | 3 | ambiguous+renamed_mapping |
| CommunityMech:000509 · `kb/communities/Hexamine_Formaldehyde_Consortium_C5.yaml` | ambiguity | 5 | ambiguous+renamed_mapping |
| CommunityMech:000546 · `data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml` | ambiguity | 1 | ambiguous |
| CommunityMech:000340 · `kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000342 · `kb/communities/Nitratireductor_Gordonia_Z123_LDPE_Degradation_SynCom.yaml` | genus | 3 | same_name_higher_rank |
| CommunityMech:000348 · `kb/communities/Sorghum_SRC2v4_Root_Colonization_SynCom.yaml` | genus | 5 | renamed_mapping+same_name_higher_rank+same_name_species_or_strain |
| CommunityMech:000349 · `kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml` | genus | 3 | same_name_higher_rank |
| CommunityMech:000350 · `kb/communities/High_Ammonia_Biogas_0B_Butyrate_Oxidizing_Enrichment.yaml` | genus | 3 | same_name_higher_rank+same_name_species_or_strain |
| CommunityMech:000353 · `kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000364 · `kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml` | genus | 5 | same_name_higher_rank+same_name_species_or_strain |
| CommunityMech:000372 · `kb/communities/Pseudomonas_Klebsiella_Alcaligenes_FeII_Nitrogen_Removal_SynCom.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000379 · `kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml` | genus | 3 | ambiguous+same_name_higher_rank |
| CommunityMech:000381 · `kb/communities/Prymnesium_Parvum_B12_Limited_SynCom.yaml` | genus | 15 | ambiguous+renamed_mapping+same_name_higher_rank+same_name_species_or_strain |
| CommunityMech:000384 · `kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml` | genus | 2 | same_name_higher_rank+same_name_species_or_strain |
| CommunityMech:000389 · `kb/communities/Rumen_Substrate_Adapted_Lignocellulose_Enrichment_Consortia.yaml` | genus | 15 | ambiguous+renamed_mapping+same_name_higher_rank |
| CommunityMech:000390 · `kb/communities/Microalgae_Cyanobacteria_Bioactive_Peptide_Consortia.yaml` | genus | 1 | same_name_higher_rank |
| CommunityMech:000403 · `kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | genus | 5 | same_name_higher_rank |
| CommunityMech:000406 · `kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000410 · `kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000415 · `kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml` | genus | 4 | same_name_higher_rank |
| CommunityMech:000416 · `kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` | genus | 6 | renamed_mapping+same_name_higher_rank |
| CommunityMech:000420 · `kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml` | genus | 3 | ambiguous+same_name_higher_rank+unsupported_or_scope_status |
| CommunityMech:000424 · `kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml` | genus | 1 | same_name_higher_rank |
| CommunityMech:000427 · `kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | genus | 12 | renamed_mapping+same_name_higher_rank |
| CommunityMech:000429 · `kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | genus | 15 | ambiguous+same_name_higher_rank |
| CommunityMech:000433 · `kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml` | genus | 3 | same_name_higher_rank |
| CommunityMech:000436 · `kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml` | genus | 8 | renamed_mapping+same_name_higher_rank |
| CommunityMech:000437 · `kb/communities/TCP_NonDehalogenimonas_Groundwater_Consortium.yaml` | genus | 4 | ambiguous+same_name_higher_rank |
| CommunityMech:000440 · `kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000441 · `kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml` | genus | 3 | ambiguous+renamed_mapping+same_name_higher_rank |
| CommunityMech:000442 · `kb/communities/Mangrove_Benzene_MFC_Bioanode_Consortium.yaml` | genus | 4 | renamed_mapping+same_name_higher_rank |
| CommunityMech:000447 · `kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000456 · `kb/communities/Caragana_Wheat_Drought_SynCom15.yaml` | genus | 5 | same_name_higher_rank |
| CommunityMech:000458 · `kb/communities/Alfalfa_Stress_Adapted_Bacterial_SynCom.yaml` | genus | 3 | same_name_higher_rank |
| CommunityMech:000463 · `kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` | genus | 6 | renamed_mapping+same_name_higher_rank |
| CommunityMech:000468 · `kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml` | genus | 5 | same_name_higher_rank |
| CommunityMech:000474 · `kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000475 · `kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml` | genus | 1 | same_name_higher_rank |
| CommunityMech:000477 · `kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml` | genus | 2 | same_name_higher_rank |
| CommunityMech:000482 · `kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml` | genus | 1 | same_name_higher_rank |
| CommunityMech:000494 · `kb/communities/Tunisian_Sahara_Saline_Spore_Forming_Halophile_Community.yaml` | genus | 6 | renamed_mapping+same_name_higher_rank |
| CommunityMech:000552 · `data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml` | genus | 1 | same_name_higher_rank |
| CommunityMech:000553 · `data/isolates/Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline.yaml` | genus | 1 | same_name_higher_rank |
| CommunityMech:000053 · `kb/communities/Phenol_Carboxylation_Consortium.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000091 · `kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml` | species | 5 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000313 · `kb/communities/Chlorella_Keystone_Taxa_Antifungal_SynCom.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000338 · `kb/communities/Caragana_Korshinskii_CrossKingdom_Forage_SynCom.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000339 · `kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml` | species | 5 | same_name_species_or_strain |
| CommunityMech:000341 · `kb/communities/Priestia_Pseudomonas_Rice_Arsenic_Stress_SynCom.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000347 · `kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000352 · `kb/communities/GENIA_NineMember_MultiPollutant_Bioremediation_SynCom.yaml` | species | 9 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000358 · `kb/communities/Bacillus_A1_A3_Naphthalene_Biofilm_Consortium.yaml` | species | 2 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000359 · `kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml` | species | 1 | renamed_mapping |
| CommunityMech:000361 · `kb/communities/RH1_Glyphosate_Streptomyces_Consortium.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000362 · `kb/communities/Sphingobium_Nitrososphaera_Phenanthrene_Carbon_SynCom.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000369 · `kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml` | species | 6 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000377 · `kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml` | species | 9 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000378 · `kb/communities/Soy_Sauce_Temporal_SevenSpecies_SynCom.yaml` | species | 4 | same_name_species_or_strain |
| CommunityMech:000383 · `kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml` | species | 11 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000387 · `kb/communities/Community_G_GenX_Biodegradation_Consortium.yaml` | species | 6 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000388 · `kb/communities/Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000391 · `kb/communities/Wheat_CrownRot_TB_CrossKingdom_SynCom.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000392 · `kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000395 · `kb/communities/Nasal_SynCom_C_Bioreactor.yaml` | species | 9 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000396 · `kb/communities/Clostridial_isoDCA_Mini_Consortium.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000397 · `kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000398 · `kb/communities/Optimized_Rumen_Fiber_Degrading_SynCom3.yaml` | species | 4 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000405 · `kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml` | species | 6 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000408 · `kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000411 · `kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000414 · `kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` | species | 4 | same_name_species_or_strain |
| CommunityMech:000423 · `kb/communities/HAMBI_Carbon_Gradient_SynCom16.yaml` | species | 15 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000426 · `kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000428 · `kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | species | 12 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000431 · `kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000432 · `kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml` | species | 3 | same_name_species_or_strain |
| CommunityMech:000435 · `kb/communities/Mulberry_Distillers_Grains_Feed_Consortium.yaml` | species | 3 | same_name_species_or_strain |
| CommunityMech:000443 · `kb/communities/MWF001_FourSpecies_CrossFeeding_Consortium.yaml` | species | 4 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000448 · `kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000449 · `kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | species | 5 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000454 · `kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml` | species | 1 | renamed_mapping |
| CommunityMech:000459 · `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` | species | 4 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000471 · `kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml` | species | 4 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000472 · `kb/communities/Halobacillus_Black_Gram_Halophilic_PGPR_Consortium.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000476 · `kb/communities/Endophytic_SynCom_NS_Brassica_Cadmium_Phytoextraction_Consortium.yaml` | species | 3 | renamed_mapping+same_name_species_or_strain |
| CommunityMech:000481 · `kb/communities/Delftia_Klebsiella_Light_Driven_Hydrogen_Denitrifying_Coculture.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000491 · `kb/communities/TwoStep_PCB_Copper_Gold_Bioleaching_Consortium.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000492 · `data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml` | species | 1 | renamed_mapping |
| CommunityMech:000497 · `kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml` | species | 1 | renamed_mapping |
| CommunityMech:000498 · `kb/communities/Cyantraniliprole_Consortium_T1.yaml` | species | 5 | ambiguous+renamed_mapping+same_name_species_or_strain |
| CommunityMech:000502 · `kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml` | species | 2 | renamed_mapping |
| CommunityMech:000503 · `kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml` | species | 1 | renamed_mapping |
| CommunityMech:000504 · `kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml` | species | 2 | renamed_mapping |
| CommunityMech:000517 · `kb/communities/Parmigiano_NWS_Set1_LAB_Triculture.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000522 · `kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml` | species | 2 | same_name_species_or_strain |
| CommunityMech:000549 · `data/isolates/Bacillus_Paramycoides_B81_PAH_Biodegradation_Isolate_Baseline.yaml` | species | 1 | renamed_mapping |
| CommunityMech:000550 · `data/isolates/Bacillus_Paranthracis_A1_PAH_Biofilm_Isolate_Baseline.yaml` | species | 1 | renamed_mapping |
| CommunityMech:000554 · `data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml` | species | 1 | same_name_species_or_strain |
| CommunityMech:000555 · `data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml` | species | 1 | same_name_species_or_strain |
