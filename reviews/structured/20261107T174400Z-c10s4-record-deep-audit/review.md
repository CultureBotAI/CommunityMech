# Cycle 10 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle 10 Records, Cycle 9 Stage 5 Remediated Records, and Actionable Community Records

- Review: 20261107T174400Z-c10s4-record-deep-audit
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-07T17:38:00Z
- Finished UTC: 2026-11-07T17:44:00Z
- Reviewer: antigravity-c10s4-record-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Deep per-record scientific and structural audit of 23 records (all 12 data/isolates/*.yaml records including newly curated 000524 and 000525, both kb/taxa/*.yaml reusable taxon records updated in Cycle 10 Stage 3, both newly curated and causal-graph-reviewed community records in Cycle 10 Stage 1/2 [000522, 000523], all 3 community records remediated in Cycle 9 Stage 5 [000331, 000455, 000461], representative CommonTaxon-linked community 000385, and 3 kb/communities/*.yaml records with newly identified actionable completeness gaps [000052, 000092, 000162]) at frozen Git revision c253d3d0ca073e3ed71447d0e184439b7fd9485c.

## Scope And Provenance

Focused per-record deep audit of all isolate baselines (12), all reusable taxon records (2), all newly curated and causal-graph-reviewed community records in Cycle 10 (2), all Cycle 9 Stage 5 remediated community records (3), representative CommonTaxon-linked community (1), and all community records with new actionable Stage 5 remediation findings (3).

Selection: All 12 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 2 new/causal-graph-reviewed kb/communities/*.yaml records (000522, 000523), 3 Cycle 9 Stage 5 remediated records (000331, 000455, 000461), representative CommonTaxon-linked record (000385), and 3 kb/communities/*.yaml records (000052, 000092, 000162) surfaced by completeness audits.
Coverage: full; 23 reviewed / 23 in the declared population.
Source: git_commit at Git base c253d3d0ca073e3ed71447d0e184439b7fd9485c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000052 | kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml | maintained | CommunityMech:000052 (Pelotomaculum-Methanothermobacter Syntrophic Consortium) |
| CommunityMech:000092 | kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml | maintained | CommunityMech:000092 (Rhodopseudomonas-E. coli Cross-Feeding Coculture) |
| CommunityMech:000162 | kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml | maintained | CommunityMech:000162 (Thalassiosira-Ruegeria Phycosphere Coculture) |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | CommunityMech:000322 (Methylobacterium REE E-waste Platform) |
| CommunityMech:000331 | kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml | maintained | CommunityMech:000331 (Pseudomonas-Paracoccus Bifenthrin-Degrading Consortium) |
| CommunityMech:000385 | kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml | maintained | CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium) |
| CommunityMech:000455 | kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml | maintained | CommunityMech:000455 (E. coli K-12 MG1655 Arg-Met Cross-Feeding Coculture) |
| CommunityMech:000461 | kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml | maintained | CommunityMech:000461 (Pseudomonas-Acidovorax Aniline-Degradation SynCom) |
| CommunityMech:000488 | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml | maintained | CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate) |
| CommunityMech:000489 | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml | maintained | CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate) |
| CommunityMech:000490 | data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml | maintained | CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate) |
| CommunityMech:000492 | data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml | maintained | CommunityMech:000492 (Intrasporangium chromatireducens Q5-1 Chromate Reduction Isolate) |
| CommunityMech:000495 | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml | maintained | CommunityMech:000495 (Ferroplasma acidiphilum ZJ Acid Mine Drainage Isolate) |
| CommunityMech:000521 | data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml | maintained | CommunityMech:000521 (Pseudomonas protegens E1BL2 Jala Maize Seed-Endophyte Isolate Baseline) |
| CommunityMech:000522 | kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml | maintained | CommunityMech:000522 (Parmigiano NWS Set 3 LAB Triculture) |
| CommunityMech:000523 | kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml | maintained | CommunityMech:000523 (SO2-BS1 Lithium-ion Battery Bioleaching Consortium) |
| CommunityMech:000524 | data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml | maintained | CommunityMech:000524 (Shewanella oneidensis MR-1 SO1 Brewing-Wastewater NCM Bioleaching Isolate Baseline) |
| CommunityMech:000525 | data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml | maintained | CommunityMech:000525 (Bacillus subtilis 168 BS1 Brewing-Wastewater Ethanol-Detoxifying Isolate Baseline) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (Shewanella oneidensis MR-1) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (Geobacter sulfurreducens) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on 23 deep-audit records | passed | True | CommunityMech:000052, CommunityMech:000092, CommunityMech:000162, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000331, CommunityMech:000385, CommunityMech:000455, CommunityMech:000461, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000521, CommunityMech:000522, CommunityMech:000523, CommunityMech:000524, CommunityMech:000525, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 21 MicrobialCommunity records and 2 CommonTaxon files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| NetworkIntegrityAuditor check on 23 deep-audit records | passed | True | CommunityMech:000052, CommunityMech:000092, CommunityMech:000162, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000331, CommunityMech:000385, CommunityMech:000455, CommunityMech:000461, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000521, CommunityMech:000522, CommunityMech:000523, CommunityMech:000524, CommunityMech:000525, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 21/21 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor with 0 warnings. |

## Scientific And Domain Assessments

### Deep per-record audit of CommunityMech:000052 (Pelotomaculum-Methanothermobacter Syntrophic Consortium)

completeness: concern. Targets: CommunityMech:000052.

Record CommunityMech:000052 (kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml) in cohort SYNTROPHY has Completeness Score 100/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000092 (Rhodopseudomonas-E. coli Cross-Feeding Coculture)

completeness: concern. Targets: CommunityMech:000092.

Record CommunityMech:000092 (kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 98/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000162 (Thalassiosira-Ruegeria Phycosphere Coculture)

completeness: concern. Targets: CommunityMech:000162.

Record CommunityMech:000162 (kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml) in cohort PHYTOPLANKTON has Completeness Score 97/100, 2 taxa, 3 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

### Deep per-record audit of CommunityMech:000331 (Pseudomonas-Paracoccus Bifenthrin-Degrading Consortium)

completeness: supported. Targets: CommunityMech:000331.

Record CommunityMech:000331 (kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml) in cohort BIOREMEDIATION has Completeness Score 95/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium)

completeness: supported. Targets: CommunityMech:000385.

Record CommunityMech:000385 (kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml) in cohort BIOMINING has Completeness Score 95/100, 2 taxa, 2 interactions, 1 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000455 (E. coli K-12 MG1655 Arg-Met Cross-Feeding Coculture)

completeness: supported. Targets: CommunityMech:000455.

Record CommunityMech:000455 (kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 98/100, 2 taxa, 3 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000461 (Pseudomonas-Acidovorax Aniline-Degradation SynCom)

completeness: supported. Targets: CommunityMech:000461.

Record CommunityMech:000461 (kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml) in cohort BIOREMEDIATION has Completeness Score 90/100, 2 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

### Deep per-record audit of CommunityMech:000522 (Parmigiano NWS Set 3 LAB Triculture)

completeness: supported. Targets: CommunityMech:000522.

Record CommunityMech:000522 (kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 85/100, 3 taxa, 4 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000523 (SO2-BS1 Lithium-ion Battery Bioleaching Consortium)

completeness: supported. Targets: CommunityMech:000523.

Record CommunityMech:000523 (kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml) in cohort BIOMINING has Completeness Score 97/100, 2 taxa, 2 interactions, 1 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000524 (Shewanella oneidensis MR-1 SO1 Brewing-Wastewater NCM Bioleaching Isolate Baseline)

completeness: supported. Targets: CommunityMech:000524.

Record CommunityMech:000524 (data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000525 (Bacillus subtilis 168 BS1 Brewing-Wastewater Ethanol-Detoxifying Isolate Baseline)

completeness: supported. Targets: CommunityMech:000525.

Record CommunityMech:000525 (data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000001 (Shewanella oneidensis MR-1)

completeness: supported. Targets: CommunityMech:taxon:000001.

Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 5 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000002 (Geobacter sulfurreducens)

completeness: supported. Targets: CommunityMech:taxon:000002.

Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 4 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

## Findings

### c10s4-000052-pelotomaculum-methanothermobacter-abundance-levels: Both obligate syntrophic coculture partners in Pelotomaculum_Methanothermobacter_Syntrophy (CommunityMech:000052) omit abundance_level despite defined two-member coculture support in PMID:12361280

major / open / confirmed; issue key: c10s4-000052-pelotomaculum-methanothermobacter-abundance-levels.

In kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml (CommunityMech:000052), both Pelotomaculum thermopropionicum (taxonomy[0], NCBITaxon:110500, functional_role: [PRIMARY_DEGRADER, SYNTROPHIC_PARTNER]) and Methanothermobacter thermautotrophicus (taxonomy[1], NCBITaxon:145262, functional_role: [SYNTROPHIC_PARTNER]) omit abundance_level. The cited species description (PMID:12361280, doi:10.1099/00207713-52-5-1729) explicitly establishes that 'The strain grew on propionate, ethanol, lactate, 1-butanol, 1-pentanol, 1,3-propanediol, 1-propanol and ethylene glycol in co-culture with the hydrogenotrophic methanogen Methanothermobacter thermautotrophicus strain deltaH(T).' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] while preserving discussions[0] (si-deltah-fulltext-and-feedback) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

### c10s4-000092-rhodopseudomonas-ecoli-abundance-levels: Both reciprocal cross-feeding coculture members in Rhodopseudomonas_Ecoli_CrossFeeding_Coculture (CommunityMech:000092) omit abundance_level despite defined two-member coculture support in PMID:32788711

major / open / confirmed; issue key: c10s4-000092-rhodopseudomonas-ecoli-abundance-levels.

In kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml (CommunityMech:000092), both Rhodopseudomonas palustris (taxonomy[0], NCBITaxon:1076, functional_role: [PRIMARY_PRODUCER]) and Escherichia coli (taxonomy[1], NCBITaxon:562, functional_role: [CROSS_FEEDER]) omit abundance_level. The cited open-access study (PMID:32788711, PMC7784955, doi:10.1038/s41396-020-00737-5) explicitly establishes that 'Previously we engineered a cross-feeding coculture between N2-fixing Rhodopseudomonas palustris and fermentative Escherichia coli. Engineered R. palustris excretes essential nitrogen as NH4+ to E. coli, while E. coli excretes essential carbon as fermentation products to R. palustris.' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] while preserving discussions[0] (reciprocal_exchange_strain_context) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

### c10s4-000162-thalassiosira-ruegeria-abundance-levels: Both marine phycosphere model coculture partners in Thalassiosira_Ruegeria_Phycosphere_Coculture (CommunityMech:000162) omit abundance_level despite defined two-member coculture support in PMID:28631440

major / open / confirmed; issue key: c10s4-000162-thalassiosira-ruegeria-abundance-levels.

In kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml (CommunityMech:000162), both Thalassiosira pseudonana CCMP1335 (taxonomy[0], NCBITaxon:296543, functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER], abundance_value: 'One of two members in the defined coculture.') and Ruegeria pomeroyi DSS-3 (taxonomy[1], NCBITaxon:246200, functional_role: [CROSS_FEEDER], abundance_value: 'One of two members in the defined coculture.') omit abundance_level. The cited primary model-system study (PMID:28631440, doi:10.1111/1462-2920.13834) explicitly establishes that 'Here, we analysed transcript and intracellular metabolite patterns in a two-member model system and found that the presence of a heterotrophic bacterium induced a potential recognition cascade in a marine phytoplankton species that parallels better-understood vascular plant response systems. Bacterium Ruegeria pomeroyi DSS-3 triggered differential expression of &gt;80 genes in diatom Thalassiosira pseudonana CCMP1335'. Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] while preserving discussions[0] (ruegeria-recognition-mediation-and-b12-extension) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

## Recommended Actions And Acceptance Checks

### act-populate-pelotomaculum-methanothermobacter-abundance-levels

Add abundance_level: DOMINANT to both Pelotomaculum thermopropionicum (taxonomy[0], NCBITaxon:110500) and Methanothermobacter thermautotrophicus (taxonomy[1], NCBITaxon:145262) backed by PMID:12361280 (doi:10.1099/00207713-52-5-1729) on CommunityMech:000052 while preserving discussions[0] (si-deltah-fulltext-and-feedback), and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
- just validate-history history

### act-populate-rhodopseudomonas-ecoli-abundance-levels

Add abundance_level: DOMINANT to both Rhodopseudomonas palustris (taxonomy[0], NCBITaxon:1076) and Escherichia coli (taxonomy[1], NCBITaxon:562) backed by PMID:32788711 (PMC7784955, doi:10.1038/s41396-020-00737-5) on CommunityMech:000092 while preserving discussions[0] (reciprocal_exchange_strain_context), and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
- just validate-history history

### act-populate-thalassiosira-ruegeria-abundance-levels

Add abundance_level: DOMINANT to both Thalassiosira pseudonana CCMP1335 (taxonomy[0], NCBITaxon:296543) and Ruegeria pomeroyi DSS-3 (taxonomy[1], NCBITaxon:246200) backed by PMID:28631440 (doi:10.1111/1462-2920.13834) on CommunityMech:000162 while preserving discussions[0] (ruegeria-recognition-mediation-and-b12-extension), and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
- just validate-history history

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and CommonTaxon classes | supports | All 507 kb/communities/*.yaml, 12 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (521 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 521 records | supports | Proportional 100-point review-communities Completeness Score audit across all 519 MicrobialCommunity records (min 40, median 90, mean 91.25, max 100; CommunityMech:000052 = 100/100, CommunityMech:000092 = 98/100, CommunityMech:000162 = 97/100) and 2 CommonTaxon files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (519/519), while scripts/audit_completeness.py:calculate_completeness() scores 000052 at 90/100, 000092 at 80/100, and 000162 at 95/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 507 kb/communities and 12 data/isolates records found 490/507 communities and 12/12 isolates with 0 warnings (including all 21/21 MicrobialCommunity records in the 23-record deep audit) and 17 community records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-520 | supports | Corpus-wide causal graph inventory covers all 519 MicrobialCommunity records (507 kb/communities/*.yaml and 12 data/isolates/*.yaml) through CommunityMech:000525 with 100% SHA-256 attestation in verify_causal_graph_reviews.py after Cycle 10 Stage 2 (#2719). |
| ev-common-taxon-linkage-audit | kb/taxa/Shewanella_oneidensis_MR1.yaml; TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem entries | supports | Corpus-wide audit of reusable taxon cross-references confirmed 19 TaxonomicComposition.common_taxon links across 18 MicrobialCommunity records (17 kb/communities/*.yaml records and 1 data/isolates/*.yaml record: 6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 23 verified EvidenceItems] and 12 Shewanella oneidensis communities plus isolate baseline CommunityMech:000524 linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 30 verified EvidenceItems], with CommunityMech:000177 linking to both) after Cycle 10 Stage 3 (#2720). |
| ev-pelotomaculum-methanothermobacter-pmid12361280 | PMID:12361280; kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml | supports | PMID:12361280 (doi:10.1099/00207713-52-5-1729) establishes that Pelotomaculum thermopropionicum strain SI(T) (NCBITaxon:110500) grew on propionate, ethanol, lactate, and alcohols in a defined two-member syntrophic coculture with the hydrogenotrophic methanogen Methanothermobacter thermautotrophicus strain deltaH(T) (NCBITaxon:145262). |
| ev-rhodopseudomonas-ecoli-pmid32788711 | PMID:32788711; kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml | supports | PMID:32788711 (PMC7784955, doi:10.1038/s41396-020-00737-5) establishes that N2-fixing Rhodopseudomonas palustris (NCBITaxon:1076) and fermentative Escherichia coli (NCBITaxon:562) form a defined two-member reciprocal nitrogen-and-carbon cross-feeding coculture. |
| ev-thalassiosira-ruegeria-pmid28631440 | PMID:28631440; kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml | supports | PMID:28631440 (doi:10.1111/1462-2920.13834) establishes that the marine diatom Thalassiosira pseudonana CCMP1335 (NCBITaxon:296543) and the heterotrophic roseobacter Ruegeria pomeroyi DSS-3 (NCBITaxon:246200) form a defined two-member marine phytoplankton-bacterium model coculture. |
| ev-prior-structured-reviews | reviews/structured; 261 retained structured review bundles through 20261107T062000Z-c9s5-remediation-verification-r2 | context_only | Lineage inspection of all 261 prior structured reviews and Cycle 9 Stage 5 evidence.yaml confirmed that all 3 Cycle 9 Stage 4 open findings across CommunityMech:000331, 000455, and 000461 were resolved in Cycle 9 Stage 5 (#2713, PR #2714) and 7 record-scoped source-limited findings remain deferred at commit c253d3d0ca073e3ed71447d0e184439b7fd9485c. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T174400Z-c10s4-record-deep-audit
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 10 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle
  10 Records, Cycle 9 Stage 5 Remediated Records, and Actionable Community Records
started_at: '2026-11-07T17:38:00Z'
finished_at: '2026-11-07T17:44:00Z'
reviewer:
  identity: antigravity-c10s4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 10 Stage 4 read-only review pass over frozen
    commit c253d3d0ca073e3ed71447d0e184439b7fd9485c without record mutation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (3 P2 major findings across CommunityMech:000052, 000092,
  and 000162; 20 isolate/taxon/new-community/C9S5-remediated/CommonTaxon-linked records
  pass with 0 defects)
scientific_review: true
summary: Deep per-record scientific and structural audit of 23 records (all 12 data/isolates/*.yaml
  records including newly curated 000524 and 000525, both kb/taxa/*.yaml reusable
  taxon records updated in Cycle 10 Stage 3, both newly curated and causal-graph-reviewed
  community records in Cycle 10 Stage 1/2 [000522, 000523], all 3 community records
  remediated in Cycle 9 Stage 5 [000331, 000455, 000461], representative CommonTaxon-linked
  community 000385, and 3 kb/communities/*.yaml records with newly identified actionable
  completeness gaps [000052, 000092, 000162]) at frozen Git revision c253d3d0ca073e3ed71447d0e184439b7fd9485c.
source:
  git_revision: c253d3d0ca073e3ed71447d0e184439b7fd9485c
  state: git_commit
  inputs:
  - path: kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml
    sha256: 3097670257aa374e7bf38197c0c1528cfd4f2e0f7c6b1acbb8c33abf431500a4
    role: target
  - path: kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml
    sha256: 178f803afb7a8bef72f1f34a3eabefc751cc4095c11b6b28d1bf736ee7af6749
    role: target
  - path: kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
    sha256: 360878e4212242ce0caf07938081bf46502f977747343a560d00684f3b725609
    role: target
  - path: kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml
    sha256: 1b43d889efac75c21e02af27ab2f1c94979448a7cc4c2e15cbff1ad1f6f71b68
    role: target
  - path: kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml
    sha256: f3ac3ff51d02bb342a6f48d80fa4549b22ef17b3ee7052d4694a44e84dd159f5
    role: target
  - path: kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
    sha256: 4c797dbaa4c2fe4d6627839b90da2a1b4adb5e0185bec3606120860268913ad3
    role: target
  - path: kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml
    sha256: 6e09328a97a58487fe879282ebc174db8c5990a6db79a35e2f96dafffc5d1c93
    role: target
  - path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    sha256: bc1fb667da9be21480d7f27961b01fc547c45dc3cef1ca63b58fe01584104076
    role: target
  - path: kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
    sha256: f1e51614a8c4a7856a2669afe12574d1c982f12dcebf9f53f49c65d470f747d6
    role: target
  - path: data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml
    sha256: 1183e9ac2b3567f395e7f19cceb575ac15227bc4ce1323736c042d1fbd43fb4b
    role: target
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    sha256: c9ebc23ad2748751ae6a42fbc2340c5f7524a7aa38185bcad4602b7e56734d9d
    role: target
  - path: data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml
    sha256: 165451ae89b467384dae87f9e5ef00d4b68fc7823037b3b96226e632bf186947
    role: target
  - path: data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml
    sha256: 7ad94b96c56469311346da8af429fb922eaa122a96464121697282771c45120e
    role: target
  - path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    sha256: 3f3fe69bc250a439ff851305a95d485ad1deee50602335de11b36601542e04d4
    role: target
  - path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    sha256: 4eb42a867f2b2b1489c4ef4fa95e408d241a54d0e2bfb1cf9474dd407d036b86
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
  - path: data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml
    sha256: 64b3114cddeee0140d34709e04dd0510dbc62710da0a73810629133c72147f71
    role: target
  - path: data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml
    sha256: 671bdcdf702788c7280e49be29c0e95455be1ca1ded72119ede0b0da864154f1
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: 5acba5205a69a57fb7270a7e92e156ca3f26affd7035aaa8216bb29307b57aaf
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: c841f96e490b0406dbccd7bca516dd0aacb42c34cf5f6042e99740ebfe86d49e
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
    sha256: ea93f2c4a12c8c5442ec903613548c884cd340aeced78c1202749bc3ae1553d9
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: e25436bd9af7759065b2dcc2ef6d767be0e3c48d798f16013fc267ded70b2422
    role: context
scope:
  description: Focused per-record deep audit of all isolate baselines (12), all reusable
    taxon records (2), all newly curated and causal-graph-reviewed community records
    in Cycle 10 (2), all Cycle 9 Stage 5 remediated community records (3), representative
    CommonTaxon-linked community (1), and all community records with new actionable
    Stage 5 remediation findings (3).
  selection: All 12 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 2 new/causal-graph-reviewed
    kb/communities/*.yaml records (000522, 000523), 3 Cycle 9 Stage 5 remediated records
    (000331, 000455, 000461), representative CommonTaxon-linked record (000385), and
    3 kb/communities/*.yaml records (000052, 000092, 000162) surfaced by completeness
    audits.
  coverage: full
  population_size: 23
  reviewed_target_ids:
  - CommunityMech:000052
  - CommunityMech:000092
  - CommunityMech:000162
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000331
  - CommunityMech:000385
  - CommunityMech:000455
  - CommunityMech:000461
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000521
  - CommunityMech:000522
  - CommunityMech:000523
  - CommunityMech:000524
  - CommunityMech:000525
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
targets:
- target_id: CommunityMech:000052
  path: kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
  label: CommunityMech:000052 (Pelotomaculum-Methanothermobacter Syntrophic Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000092
  path: kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
  label: CommunityMech:000092 (Rhodopseudomonas-E. coli Cross-Feeding Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000162
  path: kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
  label: CommunityMech:000162 (Thalassiosira-Ruegeria Phycosphere Coculture)
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
- target_id: CommunityMech:000331
  path: kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml
  label: CommunityMech:000331 (Pseudomonas-Paracoccus Bifenthrin-Degrading Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000385
  path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
  label: CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium)
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
- target_id: CommunityMech:000522
  path: kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml
  label: CommunityMech:000522 (Parmigiano NWS Set 3 LAB Triculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000523
  path: kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml
  label: CommunityMech:000523 (SO2-BS1 Lithium-ion Battery Bioleaching Consortium)
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
- check_id: chk-linkml-schema-deep-c10s4
  name: LinkML schema validation on 23 deep-audit records
  status: passed
  required: true
  summary: All 21 MicrobialCommunity records and 2 CommonTaxon files validate against
    src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000052
  - CommunityMech:000092
  - CommunityMech:000162
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000331
  - CommunityMech:000385
  - CommunityMech:000455
  - CommunityMech:000461
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000521
  - CommunityMech:000522
  - CommunityMech:000523
  - CommunityMech:000524
  - CommunityMech:000525
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -c 'validate 23 deep-audit records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-deep-c10s4
  name: NetworkIntegrityAuditor check on 23 deep-audit records
  status: passed
  required: true
  summary: All 21/21 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor
    with 0 warnings.
  target_ids:
  - CommunityMech:000052
  - CommunityMech:000092
  - CommunityMech:000162
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000331
  - CommunityMech:000385
  - CommunityMech:000455
  - CommunityMech:000461
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000521
  - CommunityMech:000522
  - CommunityMech:000523
  - CommunityMech:000524
  - CommunityMech:000525
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
  accessed_at: '2026-11-07T17:40:00Z'
  support: supports
  summary: All 507 kb/communities/*.yaml, 12 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records (521 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: scripts/audit_completeness.py
  locator: 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness()
    across all 521 records
  accessed_at: '2026-11-07T17:41:00Z'
  support: supports
  summary: Proportional 100-point review-communities Completeness Score audit across
    all 519 MicrobialCommunity records (min 40, median 90, mean 91.25, max 100; CommunityMech:000052
    = 100/100, CommunityMech:000092 = 98/100, CommunityMech:000162 = 97/100) and 2
    CommonTaxon files (100/100) confirmed 100% core metadata presence and 100% top-level
    environment_term coverage (519/519), while scripts/audit_completeness.py:calculate_completeness()
    scores 000052 at 90/100, 000092 at 80/100, and 000162 at 95/100.
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-11-07T17:41:30Z'
  support: supports
  summary: NetworkIntegrityAuditor across 507 kb/communities and 12 data/isolates
    records found 490/507 communities and 12/12 isolates with 0 warnings (including
    all 21/21 MicrobialCommunity records in the 23-record deep audit) and 17 community
    records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL
    UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0
    error-severity issues, 0 broken downstream references).
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-520
  accessed_at: '2026-11-07T17:42:00Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 519 MicrobialCommunity records
    (507 kb/communities/*.yaml and 12 data/isolates/*.yaml) through CommunityMech:000525
    with 100% SHA-256 attestation in verify_causal_graph_reviews.py after Cycle 10
    Stage 2 (#2719).
- evidence_id: ev-common-taxon-linkage-audit
  kind: record_content
  reference: kb/taxa/Shewanella_oneidensis_MR1.yaml
  locator: TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem
    entries
  accessed_at: '2026-11-07T17:42:30Z'
  support: supports
  summary: 'Corpus-wide audit of reusable taxon cross-references confirmed 19 TaxonomicComposition.common_taxon
    links across 18 MicrobialCommunity records (17 kb/communities/*.yaml records and
    1 data/isolates/*.yaml record: 6 Geobacter sulfurreducens communities linked to
    CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 23 verified EvidenceItems]
    and 12 Shewanella oneidensis communities plus isolate baseline CommunityMech:000524
    linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 30 verified
    EvidenceItems], with CommunityMech:000177 linking to both) after Cycle 10 Stage
    3 (#2720).'
- evidence_id: ev-pelotomaculum-methanothermobacter-pmid12361280
  kind: primary_source
  reference: PMID:12361280
  locator: kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
  accessed_at: '2026-11-07T17:43:00Z'
  support: supports
  summary: PMID:12361280 (doi:10.1099/00207713-52-5-1729) establishes that Pelotomaculum
    thermopropionicum strain SI(T) (NCBITaxon:110500) grew on propionate, ethanol,
    lactate, and alcohols in a defined two-member syntrophic coculture with the hydrogenotrophic
    methanogen Methanothermobacter thermautotrophicus strain deltaH(T) (NCBITaxon:145262).
  quote: The strain grew on propionate, ethanol, lactate, 1-butanol, 1-pentanol, 1,3-propanediol,
    1-propanol and ethylene glycol in co-culture with the hydrogenotrophic methanogen
    Methanothermobacter thermautotrophicus strain deltaH(T).
- evidence_id: ev-rhodopseudomonas-ecoli-pmid32788711
  kind: primary_source
  reference: PMID:32788711
  locator: kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
  accessed_at: '2026-11-07T17:43:15Z'
  support: supports
  summary: PMID:32788711 (PMC7784955, doi:10.1038/s41396-020-00737-5) establishes
    that N2-fixing Rhodopseudomonas palustris (NCBITaxon:1076) and fermentative Escherichia
    coli (NCBITaxon:562) form a defined two-member reciprocal nitrogen-and-carbon
    cross-feeding coculture.
  quote: Previously we engineered a cross-feeding coculture between N2-fixing Rhodopseudomonas
    palustris and fermentative Escherichia coli. Engineered R. palustris excretes
    essential nitrogen as NH4+ to E. coli, while E. coli excretes essential carbon
    as fermentation products to R. palustris.
- evidence_id: ev-thalassiosira-ruegeria-pmid28631440
  kind: primary_source
  reference: PMID:28631440
  locator: kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
  accessed_at: '2026-11-07T17:43:30Z'
  support: supports
  summary: PMID:28631440 (doi:10.1111/1462-2920.13834) establishes that the marine
    diatom Thalassiosira pseudonana CCMP1335 (NCBITaxon:296543) and the heterotrophic
    roseobacter Ruegeria pomeroyi DSS-3 (NCBITaxon:246200) form a defined two-member
    marine phytoplankton-bacterium model coculture.
  quote: Here, we analysed transcript and intracellular metabolite patterns in a two-member
    model system and found that the presence of a heterotrophic bacterium induced
    a potential recognition cascade in a marine phytoplankton species that parallels
    better-understood vascular plant response systems. Bacterium Ruegeria pomeroyi
    DSS-3 triggered differential expression of >80 genes in diatom Thalassiosira pseudonana
    CCMP1335
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 261 retained structured review bundles through 20261107T062000Z-c9s5-remediation-verification-r2
  accessed_at: '2026-11-07T17:43:45Z'
  support: context_only
  summary: 'Lineage inspection of all 261 prior structured reviews and Cycle 9 Stage
    5 evidence.yaml confirmed that all 3 Cycle 9 Stage 4 open findings across CommunityMech:000331,
    000455, and 000461 were resolved in Cycle 9 Stage 5 (#2713, PR #2714) and 7 record-scoped
    source-limited findings remain deferred at commit c253d3d0ca073e3ed71447d0e184439b7fd9485c.'
assessments:
- assessment_id: assess-communitymech-000052
  area: completeness
  topic: Deep per-record audit of CommunityMech:000052 (Pelotomaculum-Methanothermobacter
    Syntrophic Consortium)
  outcome: concern
  summary: Record CommunityMech:000052 (kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml)
    in cohort SYNTROPHY has Completeness Score 100/100, 2 taxa, 3 interactions, 2
    causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000052
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
- assessment_id: assess-communitymech-000092
  area: completeness
  topic: Deep per-record audit of CommunityMech:000092 (Rhodopseudomonas-E. coli Cross-Feeding
    Coculture)
  outcome: concern
  summary: Record CommunityMech:000092 (kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 98/100, 2 taxa, 3 interactions,
    2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000092
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 98.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000162
  area: completeness
  topic: Deep per-record audit of CommunityMech:000162 (Thalassiosira-Ruegeria Phycosphere
    Coculture)
  outcome: concern
  summary: Record CommunityMech:000162 (kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml)
    in cohort PHYTOPLANKTON has Completeness Score 97/100, 2 taxa, 3 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000162
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 97.0
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
- assessment_id: assess-communitymech-000331
  area: completeness
  topic: Deep per-record audit of CommunityMech:000331 (Pseudomonas-Paracoccus Bifenthrin-Degrading
    Consortium)
  outcome: supported
  summary: Record CommunityMech:000331 (kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml)
    in cohort BIOREMEDIATION has Completeness Score 95/100, 2 taxa, 3 interactions,
    2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000331
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
- assessment_id: assess-communitymech-000455
  area: completeness
  topic: Deep per-record audit of CommunityMech:000455 (E. coli K-12 MG1655 Arg-Met
    Cross-Feeding Coculture)
  outcome: supported
  summary: Record CommunityMech:000455 (kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 98/100, 2 taxa, 3 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000455
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 98.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000461
  area: completeness
  topic: Deep per-record audit of CommunityMech:000461 (Pseudomonas-Acidovorax Aniline-Degradation
    SynCom)
  outcome: supported
  summary: Record CommunityMech:000461 (kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml)
    in cohort BIOREMEDIATION has Completeness Score 90/100, 2 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000461
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
- assessment_id: assess-communitymech-000522
  area: completeness
  topic: Deep per-record audit of CommunityMech:000522 (Parmigiano NWS Set 3 LAB Triculture)
  outcome: supported
  summary: Record CommunityMech:000522 (kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 85/100, 3 taxa, 4 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000522
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
- assessment_id: assess-communitymech-000523
  area: completeness
  topic: Deep per-record audit of CommunityMech:000523 (SO2-BS1 Lithium-ion Battery
    Bioleaching Consortium)
  outcome: supported
  summary: Record CommunityMech:000523 (kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml)
    in cohort BIOMINING has Completeness Score 97/100, 2 taxa, 2 interactions, 1 causal
    edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000523
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 97.0
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
- finding_id: c10s4-000052-pelotomaculum-methanothermobacter-abundance-levels
  issue_key: c10s4-000052-pelotomaculum-methanothermobacter-abundance-levels
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Both obligate syntrophic coculture partners in Pelotomaculum_Methanothermobacter_Syntrophy
    (CommunityMech:000052) omit abundance_level despite defined two-member coculture
    support in PMID:12361280
  description: 'In kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
    (CommunityMech:000052), both Pelotomaculum thermopropionicum (taxonomy[0], NCBITaxon:110500,
    functional_role: [PRIMARY_DEGRADER, SYNTROPHIC_PARTNER]) and Methanothermobacter
    thermautotrophicus (taxonomy[1], NCBITaxon:145262, functional_role: [SYNTROPHIC_PARTNER])
    omit abundance_level. The cited species description (PMID:12361280, doi:10.1099/00207713-52-5-1729)
    explicitly establishes that ''The strain grew on propionate, ethanol, lactate,
    1-butanol, 1-pentanol, 1,3-propanediol, 1-propanol and ethylene glycol in co-culture
    with the hydrogenotrophic methanogen Methanothermobacter thermautotrophicus strain
    deltaH(T).'' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1]
    while preserving discussions[0] (si-deltah-fulltext-and-feedback) raises the review-communities
    s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000052
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-pelotomaculum-methanothermobacter-pmid12361280
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both defined two-member
    syntrophic coculture partners leaves the review-communities s_ab rubric component
    at 0/5 (Completeness Score 100/100; scripts/audit_completeness.py score 90/100)
    and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
- finding_id: c10s4-000092-rhodopseudomonas-ecoli-abundance-levels
  issue_key: c10s4-000092-rhodopseudomonas-ecoli-abundance-levels
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Both reciprocal cross-feeding coculture members in Rhodopseudomonas_Ecoli_CrossFeeding_Coculture
    (CommunityMech:000092) omit abundance_level despite defined two-member coculture
    support in PMID:32788711
  description: 'In kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
    (CommunityMech:000092), both Rhodopseudomonas palustris (taxonomy[0], NCBITaxon:1076,
    functional_role: [PRIMARY_PRODUCER]) and Escherichia coli (taxonomy[1], NCBITaxon:562,
    functional_role: [CROSS_FEEDER]) omit abundance_level. The cited open-access study
    (PMID:32788711, PMC7784955, doi:10.1038/s41396-020-00737-5) explicitly establishes
    that ''Previously we engineered a cross-feeding coculture between N2-fixing Rhodopseudomonas
    palustris and fermentative Escherichia coli. Engineered R. palustris excretes
    essential nitrogen as NH4+ to E. coli, while E. coli excretes essential carbon
    as fermentation products to R. palustris.'' Setting abundance_level: DOMINANT
    on both taxonomy[0] and taxonomy[1] while preserving discussions[0] (reciprocal_exchange_strain_context)
    raises the review-communities s_ab abundance_level rubric component from 0/5 to
    5/5 (0/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000092
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-rhodopseudomonas-ecoli-pmid32788711
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both defined two-member
    reciprocal cross-feeding coculture members leaves the review-communities s_ab
    rubric component at 0/5 (Completeness Score 98/100; scripts/audit_completeness.py
    score 80/100) and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
- finding_id: c10s4-000162-thalassiosira-ruegeria-abundance-levels
  issue_key: c10s4-000162-thalassiosira-ruegeria-abundance-levels
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Both marine phycosphere model coculture partners in Thalassiosira_Ruegeria_Phycosphere_Coculture
    (CommunityMech:000162) omit abundance_level despite defined two-member coculture
    support in PMID:28631440
  description: 'In kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
    (CommunityMech:000162), both Thalassiosira pseudonana CCMP1335 (taxonomy[0], NCBITaxon:296543,
    functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER], abundance_value: ''One of two
    members in the defined coculture.'') and Ruegeria pomeroyi DSS-3 (taxonomy[1],
    NCBITaxon:246200, functional_role: [CROSS_FEEDER], abundance_value: ''One of two
    members in the defined coculture.'') omit abundance_level. The cited primary model-system
    study (PMID:28631440, doi:10.1111/1462-2920.13834) explicitly establishes that
    ''Here, we analysed transcript and intracellular metabolite patterns in a two-member
    model system and found that the presence of a heterotrophic bacterium induced
    a potential recognition cascade in a marine phytoplankton species that parallels
    better-understood vascular plant response systems. Bacterium Ruegeria pomeroyi
    DSS-3 triggered differential expression of >80 genes in diatom Thalassiosira pseudonana
    CCMP1335''. Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1]
    while preserving discussions[0] (ruegeria-recognition-mediation-and-b12-extension)
    raises the review-communities s_ab abundance_level rubric component from 0/5 to
    5/5 (0/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000162
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-thalassiosira-ruegeria-pmid28631440
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both defined two-member
    phycosphere coculture members leaves the review-communities s_ab rubric component
    at 0/5 (Completeness Score 97/100; scripts/audit_completeness.py score 95/100)
    and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
actions:
- action_id: act-populate-pelotomaculum-methanothermobacter-abundance-levels
  description: 'Add abundance_level: DOMINANT to both Pelotomaculum thermopropionicum
    (taxonomy[0], NCBITaxon:110500) and Methanothermobacter thermautotrophicus (taxonomy[1],
    NCBITaxon:145262) backed by PMID:12361280 (doi:10.1099/00207713-52-5-1729) on
    CommunityMech:000052 while preserving discussions[0] (si-deltah-fulltext-and-feedback),
    and append curation_history.'
  finding_ids:
  - c10s4-000052-pelotomaculum-methanothermobacter-abundance-levels
  target_ids:
  - CommunityMech:000052
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml
  - just validate-history history
- action_id: act-populate-rhodopseudomonas-ecoli-abundance-levels
  description: 'Add abundance_level: DOMINANT to both Rhodopseudomonas palustris (taxonomy[0],
    NCBITaxon:1076) and Escherichia coli (taxonomy[1], NCBITaxon:562) backed by PMID:32788711
    (PMC7784955, doi:10.1038/s41396-020-00737-5) on CommunityMech:000092 while preserving
    discussions[0] (reciprocal_exchange_strain_context), and append curation_history.'
  finding_ids:
  - c10s4-000092-rhodopseudomonas-ecoli-abundance-levels
  target_ids:
  - CommunityMech:000092
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml
  - just validate-history history
- action_id: act-populate-thalassiosira-ruegeria-abundance-levels
  description: 'Add abundance_level: DOMINANT to both Thalassiosira pseudonana CCMP1335
    (taxonomy[0], NCBITaxon:296543) and Ruegeria pomeroyi DSS-3 (taxonomy[1], NCBITaxon:246200)
    backed by PMID:28631440 (doi:10.1111/1462-2920.13834) on CommunityMech:000162
    while preserving discussions[0] (ruegeria-recognition-mediation-and-b12-extension),
    and append curation_history.'
  finding_ids:
  - c10s4-000162-thalassiosira-ruegeria-abundance-levels
  target_ids:
  - CommunityMech:000162
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml
  - just validate-history history
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used
  cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.
tags:
- cycle10
- stage4
- record-review
- deep-audit
```
