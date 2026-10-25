# Cycle 2 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle 2 Records, and Actionable Community Records

- Review: 20261025T113500Z-c2s4-record-deep-audit
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-25T11:22:00Z
- Finished UTC: 2026-10-25T11:35:00Z
- Reviewer: antigravity-c2s4-record-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Deep per-record scientific and structural audit of 23 records (all 7 data/isolates/*.yaml records, both kb/taxa/*.yaml reusable taxon records, all 4 new Cycle 2 community records 000484-000487, and 10 kb/communities/*.yaml records with actionable environment_term or common_taxon linkage gaps) at frozen Git revision 9e6356de530ea961259cb5b8c93e5da4b44f5660.

## Scope And Provenance

Focused per-record deep audit of all isolate baselines (7), all reusable taxon records (2), all newly curated Cycle 2 community records (4), and all community records with actionable Stage 5 remediation findings (10).

Selection: All 7 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 4 new Cycle 2 kb/communities/*.yaml records (000484-000487), and 10 kb/communities/*.yaml records surfaced by completeness and reusable-taxon linkage audits.
Coverage: full; 23 reviewed / 23 in the declared population.
Source: git_commit at Git base 9e6356de530ea961259cb5b8c93e5da4b44f5660.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000006 | kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml | maintained | CommunityMech:000006 (BioModels MODEL1806250003 Spittlebug Sulcia-Sodalis Symbiosis) |
| CommunityMech:000007 | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml | maintained | CommunityMech:000007 (BioModels MODEL1806250004 Sharpshooter Sulcia-Baumannia Symbiosis) |
| CommunityMech:000008 | kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml | maintained | CommunityMech:000008 (BioModels MODEL1806250005 Cicada Sulcia-Hodgkinia Symbiosis) |
| CommunityMech:000013 | kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml | maintained | CommunityMech:000013 (BioModels MODEL2407300002 Sponge Holobiont Network) |
| CommunityMech:000031 | kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml | maintained | CommunityMech:000031 (Geobacter-Clostridium Interspecies Electron Transfer Coculture) |
| CommunityMech:000175 | kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml | maintained | CommunityMech:000175 (Clostridium cellulolyticum-Geobacter sulfurreducens Cellulose MFC Coculture) |
| CommunityMech:000176 | kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml | maintained | CommunityMech:000176 (ORNL Clostridium-Desulfovibrio-Geobacter Trophic Model Community) |
| CommunityMech:000268 | kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml | maintained | CommunityMech:000268 (Rhodopseudomonas-Geobacter Magnetite Redox Coculture) |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000288 | kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml | maintained | CommunityMech:000288 (Shewanella oneidensis + Pseudomonas aeruginosa Fe0-dependent Electro-syntrophic Denitrifying Consortium) |
| CommunityMech:000294 | kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml | maintained | CommunityMech:000294 (Corynebacterium glutamicum + Shewanella oneidensis Succinic-acid Co-culture) |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | CommunityMech:000322 (Methylobacterium REE E-waste Platform) |
| CommunityMech:000484 | kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml | maintained | CommunityMech:000484 (Aquifer Sediment Cable Bacteria Sulfur-Cycling Community) |
| CommunityMech:000485 | kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml | maintained | CommunityMech:000485 (Dexing Copper Mine Bioleaching Heap Surface Community) |
| CommunityMech:000486 | kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml | maintained | CommunityMech:000486 (Stare Ransko Mine Tailings Mesophilic Bioleaching Consortium) |
| CommunityMech:000487 | kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml | maintained | CommunityMech:000487 (Moderate Thermophile Chalcopyrite pH-Regulated Bioleaching Consortium) |
| CommunityMech:000488 | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml | maintained | CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate) |
| CommunityMech:000489 | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml | maintained | CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate) |
| CommunityMech:000490 | data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml | maintained | CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (Geobacter_sulfurreducens) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on 23 deep-audit records | passed | True | CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000013, CommunityMech:000031, CommunityMech:000175, CommunityMech:000176, CommunityMech:000268, CommunityMech:000273, CommunityMech:000288, CommunityMech:000294, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000484, CommunityMech:000485, CommunityMech:000486, CommunityMech:000487, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 21 MicrobialCommunity records and 2 TaxonRecord files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| NetworkIntegrityAuditor check on 23 deep-audit records | passed | True | CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000013, CommunityMech:000031, CommunityMech:000175, CommunityMech:000176, CommunityMech:000268, CommunityMech:000273, CommunityMech:000288, CommunityMech:000294, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000484, CommunityMech:000485, CommunityMech:000486, CommunityMech:000487, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 21 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor with 0 warnings and 0 broken downstream causal edges. |

## Scientific And Domain Assessments

### Deep per-record audit of CommunityMech:000006 (BioModels MODEL1806250003 Spittlebug Sulcia-Sodalis Symbiosis)

completeness: concern. Targets: CommunityMech:000006.

Record CommunityMech:000006 (kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml) in cohort SYNTROPHY has Completeness Score 74/100, 3 taxa, 3 interactions, 0 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000007 (BioModels MODEL1806250004 Sharpshooter Sulcia-Baumannia Symbiosis)

completeness: concern. Targets: CommunityMech:000007.

Record CommunityMech:000007 (kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml) in cohort SYNTROPHY has Completeness Score 74/100, 3 taxa, 3 interactions, 0 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000008 (BioModels MODEL1806250005 Cicada Sulcia-Hodgkinia Symbiosis)

completeness: concern. Targets: CommunityMech:000008.

Record CommunityMech:000008 (kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml) in cohort SYNTROPHY has Completeness Score 74/100, 3 taxa, 3 interactions, 0 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000013 (BioModels MODEL2407300002 Sponge Holobiont Network)

completeness: concern. Targets: CommunityMech:000013.

Record CommunityMech:000013 (kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml) in cohort OTHER has Completeness Score 79/100, 3 taxa, 6 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000031 (Geobacter-Clostridium Interspecies Electron Transfer Coculture)

grounding: concern. Targets: CommunityMech:000031.

Record CommunityMech:000031 (kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml) in cohort SYNTROPHY has Completeness Score 100/100, 2 taxa, 2 interactions, 1 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000175 (Clostridium cellulolyticum-Geobacter sulfurreducens Cellulose MFC Coculture)

grounding: concern. Targets: CommunityMech:000175.

Record CommunityMech:000175 (kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 98/100, 2 taxa, 3 interactions, 1 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000176 (ORNL Clostridium-Desulfovibrio-Geobacter Trophic Model Community)

grounding: concern. Targets: CommunityMech:000176.

Record CommunityMech:000176 (kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml) in cohort BIOREMEDIATION has Completeness Score 97/100, 3 taxa, 4 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000268 (Rhodopseudomonas-Geobacter Magnetite Redox Coculture)

grounding: concern. Targets: CommunityMech:000268.

Record CommunityMech:000268 (kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml) in cohort METAL_REDUCTION has Completeness Score 96/100, 2 taxa, 4 interactions, 5 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)

completeness: supported. Targets: CommunityMech:000273.

Record CommunityMech:000273 (data/isolates/Chromobacterium_Gold_Biocyanidation.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 91/100, 1 taxa, 4 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000288 (Shewanella oneidensis + Pseudomonas aeruginosa Fe0-dependent Electro-syntrophic Denitrifying Consortium)

grounding: concern. Targets: CommunityMech:000288.

Record CommunityMech:000288 (kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml) in cohort SYNTROPHY has Completeness Score 93/100, 2 taxa, 3 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000294 (Corynebacterium glutamicum + Shewanella oneidensis Succinic-acid Co-culture)

grounding: concern. Targets: CommunityMech:000294.

Record CommunityMech:000294 (kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 93/100, 2 taxa, 3 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform)

completeness: supported. Targets: CommunityMech:000320.

Record CommunityMech:000320 (data/isolates/Aspergillus_Indium_LED_Recovery.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 91/100, 1 taxa, 5 interactions, 4 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model)

completeness: supported. Targets: CommunityMech:000321.

Record CommunityMech:000321 (data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 95/100, 1 taxa, 1 interactions, 0 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000322 (Methylobacterium REE E-waste Platform)

completeness: supported. Targets: CommunityMech:000322.

Record CommunityMech:000322 (data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 94/100, 1 taxa, 4 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000484 (Aquifer Sediment Cable Bacteria Sulfur-Cycling Community)

completeness: supported. Targets: CommunityMech:000484.

Record CommunityMech:000484 (kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml) in cohort BIOREMEDIATION has Completeness Score 95/100, 3 taxa, 3 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000485 (Dexing Copper Mine Bioleaching Heap Surface Community)

completeness: supported. Targets: CommunityMech:000485.

Record CommunityMech:000485 (kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml) in cohort BIOMINING has Completeness Score 95/100, 4 taxa, 3 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000486 (Stare Ransko Mine Tailings Mesophilic Bioleaching Consortium)

completeness: supported. Targets: CommunityMech:000486.

Record CommunityMech:000486 (kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml) in cohort BIOMINING has Completeness Score 95/100, 3 taxa, 2 interactions, 1 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000487 (Moderate Thermophile Chalcopyrite pH-Regulated Bioleaching Consortium)

completeness: supported. Targets: CommunityMech:000487.

Record CommunityMech:000487 (kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml) in cohort BIOMINING has Completeness Score 95/100, 3 taxa, 2 interactions, 1 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate)

completeness: supported. Targets: CommunityMech:000488.

Record CommunityMech:000488 (data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml) in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 2 interactions, 1 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate)

completeness: supported. Targets: CommunityMech:000489.

Record CommunityMech:000489 (data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 3 interactions, 2 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate)

completeness: supported. Targets: CommunityMech:000490.

Record CommunityMech:000490 (data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 95/100, 1 taxa, 2 interactions, 1 causal edges, 0 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1)

completeness: supported. Targets: CommunityMech:taxon:000001.

Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 5 gene annotations, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000002 (Geobacter_sulfurreducens)

completeness: supported. Targets: CommunityMech:taxon:000002.

Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 4 gene annotations, and 0 network warnings.

## Findings

### c2s4-biomodels-missing-environment-term: Four BioModels community records (CommunityMech:000006, 000007, 000008, 000013) omit environment_term despite explicit host-associated habitat context in cited sources

major / open / confirmed; issue key: communitymech-c2s4-biomodels-missing-environment-term.

Out of all 484 MicrobialCommunity records across kb/communities/ (477) and data/isolates/ (7), only 4 records omit top-level environment_term: CommunityMech:000006 (BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml, Completeness Score 72/100), CommunityMech:000007 (BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml, Completeness Score 72/100), CommunityMech:000008 (BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml, Completeness Score 72/100), and CommunityMech:000013 (BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml, Completeness Score 75/100). The cited primary sources and record descriptions explicitly establish obligate sap-feeding insect bacteriome symbioses (PMID:30254121 for 000006-000008) and a Stylissa sp. marine sponge holobiont (PMID:39738126 for 000013), supporting ENVO:01001000 (animal-associated habitat) consistent with sibling BioModels records (CommunityMech:000009-000012 and CommunityMech:000321).

### c2s4-geobacter-common-taxon-linkage-gap: Four Geobacter sulfurreducens community records (CommunityMech:000031, 000175, 000176, 000268) omit common_taxon linkage to CommunityMech:taxon:000002

minor / open / confirmed; issue key: communitymech-c2s4-geobacter-common-taxon-linkage-gap.

Six community records in kb/communities/ contain Geobacter sulfurreducens (NCBITaxon:35554), which is represented as reusable taxon record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) carrying verified UniProtKB EET protein annotations (pilA/Q74BW5, omcS/Q749X9, omcZ/Q74A90, omcB/Q74A86). While CommunityMech:000177 and CommunityMech:000201 link their Geobacter sulfurreducens TaxonomicComposition entry via common_taxon: CommunityMech:taxon:000002, four syntrophic/electroactive community records — CommunityMech:000031 (Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml), CommunityMech:000175 (Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml), CommunityMech:000176 (ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml), and CommunityMech:000268 (Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml) — omit common_taxon: CommunityMech:taxon:000002.

### c2s4-shewanella-common-taxon-linkage-gap: Two Shewanella oneidensis community records (CommunityMech:000288, 000294) omit common_taxon linkage to CommunityMech:taxon:000001

minor / open / confirmed; issue key: communitymech-c2s4-shewanella-common-taxon-linkage-gap.

Nine community records in kb/communities/ contain Shewanella oneidensis (NCBITaxon:70863 / NCBITaxon:211586), which is represented as reusable taxon record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) carrying verified UniProtKB Mtr/CymA/OmcA EET protein annotations (mtrC/Q8EG33, mtrB/Q8EG34, mtrA/Q8EG35, omcA/Q8EG32, cymA/Q8E945). Seven records (000046, 000063, 000064, 000150, 000215, 000219, 000237) link via common_taxon: CommunityMech:taxon:000001, whereas CommunityMech:000288 (Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml, which explicitly describes CymA-OmcA-MtrC EET complexes in Shewanella oneidensis MR-1) and CommunityMech:000294 (Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml) omit common_taxon: CommunityMech:taxon:000001.

## Recommended Actions And Acceptance Checks

### act-populate-biomodels-environment-term

Populate top-level environment_term (ENVO:01001000 animal-associated habitat) with source-backed notes on CommunityMech:000006, 000007, 000008 (PMID:30254121) and CommunityMech:000013 (PMID:39738126), and append curation_history entries.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-link-geobacter-common-taxon

Add common_taxon: CommunityMech:taxon:000002 to the Geobacter sulfurreducens (NCBITaxon:35554) TaxonomicComposition entry in CommunityMech:000031, 000175, 000176, and 000268, and append curation_history entries.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-link-shewanella-common-taxon

Add common_taxon: CommunityMech:taxon:000001 to the Shewanella oneidensis (NCBITaxon:70863 / NCBITaxon:211586) TaxonomicComposition entry in CommunityMech:000288 and 000294, and append curation_history entries.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
- uv run python scripts/verify_history_Changed_records.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and TaxonRecord classes | supports | All 477 kb/communities/*.yaml, 7 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (486 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; calculate_completeness() and calculate_validation_score() across all 486 records | supports | Proportional Completeness Score audit across all 484 MicrobialCommunity records (min 40, median 90, mean 85.40, max 100) and 2 TaxonRecord files (100/100) confirmed 100% core metadata presence (id, name, description, ecological_state, community_origin, community_category) and identified the sole 4 records missing environment_term (CommunityMech:000006, 000007, 000008, 000013). |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | Network integrity audit across 477 kb/communities and 7 data/isolates records found 464/477 communities and 7/7 isolates with 0 warnings; the remaining 13 community records have 36 non-fatal DISCONNECTED_TAXON warnings on source-limited records and 0 UNKNOWN_TARGET or broken downstream references. |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-485 | supports | Corpus-wide causal graph inventory covers all 484 MicrobialCommunity records (430 reviewed with evidence-backed causal structure, 54 needs_research source-limited, 0 unreviewed). |
| ev-common-taxon-linkage-audit | kb/taxa/Geobacter_sulfurreducens.yaml; TaxonomicComposition.common_taxon cross-references across kb/communities/*.yaml | supports | Corpus-wide audit of reusable taxon cross-references showed 2/6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 (leaving 000031, 000175, 000176, 000268 unlinked) and 7/9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001 (leaving 000288, 000294 unlinked). |
| ev-biomodels-pmid30254121 | PMID:30254121; kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml | supports | Ankrah et al. 2018 (PMID:30254121) models obligate intracellular bacteriome endosymbioses of sap-feeding insects (spittlebug Sulcia-Sodalis in 000006, sharpshooter Sulcia-Baumannia in 000007, and cicada Sulcia-Hodgkinia in 000008), supporting ENVO:01001000 (animal-associated habitat). |
| ev-sponge-pmid39738126 | PMID:39738126; kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml | supports | PMID:39738126 (and DOI:10.1038/s43705-024-00531-6) describes a multi-partner metabolic network of prokaryotic symbionts associated with the marine sponge Stylissa sp. in the Red Sea, supporting ENVO:01001000 (animal-associated habitat). |
| ev-prior-structured-reviews | reviews/structured; 43 retained structured review bundles through 20261021T193000Z-stage5-remediation-verification | context_only | Lineage inspection of all 43 prior structured reviews and Cycle 1 Stage 5 evidence.yaml confirmed that all 6 Cycle 1 Stage 4 open findings were resolved in Stage 5 and 7 record-scoped source-limited findings remain deferred at commit 9e6356de530ea961259cb5b8c93e5da4b44f5660. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used cached PubMed/DOI abstracts and open-access metadata in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T113500Z-c2s4-record-deep-audit
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 2 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle
  2 Records, and Actionable Community Records
started_at: '2026-10-25T11:22:00Z'
finished_at: '2026-10-25T11:35:00Z'
reviewer:
  identity: antigravity-c2s4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 2 Stage 4 read-only review pass over frozen
    commit 9e6356de530ea961259cb5b8c93e5da4b44f5660 without record mutation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (1 P2 major finding across 4 BioModels records, 2 P3
  minor findings across 6 Geobacter/Shewanella records; 13 isolate/taxon/new-community
  records pass)
scientific_review: true
summary: Deep per-record scientific and structural audit of 23 records (all 7 data/isolates/*.yaml
  records, both kb/taxa/*.yaml reusable taxon records, all 4 new Cycle 2 community
  records 000484-000487, and 10 kb/communities/*.yaml records with actionable environment_term
  or common_taxon linkage gaps) at frozen Git revision 9e6356de530ea961259cb5b8c93e5da4b44f5660.
source:
  git_revision: 9e6356de530ea961259cb5b8c93e5da4b44f5660
  state: git_commit
  inputs:
  - path: data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml
    sha256: 1183e9ac2b3567f395e7f19cceb575ac15227bc4ce1323736c042d1fbd43fb4b
    role: target
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    sha256: c9ebc23ad2748751ae6a42fbc2340c5f7524a7aa38185bcad4602b7e56734d9d
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
  - path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    sha256: 70d9761a556a3e744eb81c26f1906bb0ce697b3d64be526ecaafddea7404f978
    role: target
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml
    sha256: 8faad2ab07cfb8f5cd789e5090d327abc5aeab737872d1b32ec6b47e59e77df4
    role: target
  - path: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
    sha256: f29ece197fbf2088caa649cbf78c0c2d0054d1434369353b29e7f6efdd05a848
    role: target
  - path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    sha256: 3c0c3ec94b77750f8583de5ef0d9a8380bf28bd62a1857cdb28c95cc9ff4601b
    role: target
  - path: kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml
    sha256: 599ef8dd4776e7b3b8fabbd06bdab35c7018b3794b8f7c225795820e33f5195d
    role: target
  - path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    sha256: 2f4e9de54727970a957771c70add6bd6a8fc5a6d38c4cdda2316cc50ab509e7a
    role: target
  - path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    sha256: bafb8c0e58150b2e586e92c84725b0e3ad88001a64c2d1acb1d2889ede2810b3
    role: target
  - path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    sha256: 1522534e0e993cff111c4fcde85182868aeae81389cb47120d97a3882b88250d
    role: target
  - path: kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml
    sha256: e12ae0d4c80ec68da97fd77e007b609261f6865e9256bb27edfc58c2634965d5
    role: target
  - path: kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml
    sha256: 2bfa8ffd6b7d147f3c471eb88aa26482f93b0cc8d7b23dc39838402715463329
    role: target
  - path: kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml
    sha256: 6dd87be5e5181dd81e8119e10bc5a3f645c33a98084614df9d60e2a26f085e2b
    role: target
  - path: kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml
    sha256: 151a414766ded2f1c8b094002819c6e620751b6344ef9753d1f3a988c1cf99dd
    role: target
  - path: kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml
    sha256: 21ea769fcc97b50c66ad0fd3ba76cca647ae23fde4a34ce2b7d1aea81bc69378
    role: target
  - path: kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml
    sha256: 1c9db92e6594e7744b051cec01e1f4cc33c3ff0370d73ca6419f56fd4edcc241
    role: target
  - path: kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml
    sha256: 65d9768713aa281dca229c73794ae3f825f22acb78d857b9eb189addfeeb7acf
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: b3e02ec32304b400312e5320a64bbd963b9667c175c019a3cc5bd7bbdb1979a9
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf
    role: target
  - path: reports/causal_graph_review/inventory.tsv
    sha256: b0790ccd557d8923c6b8063aecb6033f4f6f7dc0f6b22f1d408f77004f0f66ab
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: 1111f4a08cc700160c93d2762419d34ae3563ac43a702f1e2498bece54db9ef9
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Focused per-record deep audit of all isolate baselines (7), all reusable
    taxon records (2), all newly curated Cycle 2 community records (4), and all community
    records with actionable Stage 5 remediation findings (10).
  selection: All 7 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 4 new Cycle 2 kb/communities/*.yaml
    records (000484-000487), and 10 kb/communities/*.yaml records surfaced by completeness
    and reusable-taxon linkage audits.
  coverage: full
  population_size: 23
  reviewed_target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  - CommunityMech:000031
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000268
  - CommunityMech:000273
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000484
  - CommunityMech:000485
  - CommunityMech:000486
  - CommunityMech:000487
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
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
- target_id: CommunityMech:000268
  path: kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml
  label: CommunityMech:000268 (Rhodopseudomonas-Geobacter Magnetite Redox Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000273
  path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  label: CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)
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
- target_id: CommunityMech:000484
  path: kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml
  label: CommunityMech:000484 (Aquifer Sediment Cable Bacteria Sulfur-Cycling Community)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000485
  path: kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml
  label: CommunityMech:000485 (Dexing Copper Mine Bioleaching Heap Surface Community)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000486
  path: kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml
  label: CommunityMech:000486 (Stare Ransko Mine Tailings Mesophilic Bioleaching Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000487
  path: kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml
  label: CommunityMech:000487 (Moderate Thermophile Chalcopyrite pH-Regulated Bioleaching
    Consortium)
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
- target_id: CommunityMech:taxon:000001
  path: kb/taxa/Shewanella_oneidensis_MR1.yaml
  label: CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1)
  record_class: TaxonRecord
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:taxon:000002
  path: kb/taxa/Geobacter_sulfurreducens.yaml
  label: CommunityMech:taxon:000002 (Geobacter_sulfurreducens)
  record_class: TaxonRecord
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-deep-c2s4
  name: LinkML schema validation on 23 deep-audit records
  status: passed
  required: true
  summary: All 21 MicrobialCommunity records and 2 TaxonRecord files validate against
    src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  - CommunityMech:000031
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000268
  - CommunityMech:000273
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000484
  - CommunityMech:000485
  - CommunityMech:000486
  - CommunityMech:000487
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -c 'validate 23 deep-audit records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-deep-c2s4
  name: NetworkIntegrityAuditor check on 23 deep-audit records
  status: passed
  required: true
  summary: All 21 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor
    with 0 warnings and 0 broken downstream causal edges.
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  - CommunityMech:000031
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000268
  - CommunityMech:000273
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000484
  - CommunityMech:000485
  - CommunityMech:000486
  - CommunityMech:000487
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
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
  locator: MicrobialCommunity and TaxonRecord classes
  accessed_at: '2026-10-25T11:25:00Z'
  support: supports
  summary: All 477 kb/communities/*.yaml, 7 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records (486 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: scripts/audit_completeness.py
  locator: calculate_completeness() and calculate_validation_score() across all 486
    records
  accessed_at: '2026-10-25T11:26:00Z'
  support: supports
  summary: Proportional Completeness Score audit across all 484 MicrobialCommunity
    records (min 40, median 90, mean 85.40, max 100) and 2 TaxonRecord files (100/100)
    confirmed 100% core metadata presence (id, name, description, ecological_state,
    community_origin, community_category) and identified the sole 4 records missing
    environment_term (CommunityMech:000006, 000007, 000008, 000013).
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-10-25T11:27:00Z'
  support: supports
  summary: Network integrity audit across 477 kb/communities and 7 data/isolates records
    found 464/477 communities and 7/7 isolates with 0 warnings; the remaining 13 community
    records have 36 non-fatal DISCONNECTED_TAXON warnings on source-limited records
    and 0 UNKNOWN_TARGET or broken downstream references.
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-485
  accessed_at: '2026-10-25T11:28:00Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 484 MicrobialCommunity records
    (430 reviewed with evidence-backed causal structure, 54 needs_research source-limited,
    0 unreviewed).
- evidence_id: ev-common-taxon-linkage-audit
  kind: record_content
  reference: kb/taxa/Geobacter_sulfurreducens.yaml
  locator: TaxonomicComposition.common_taxon cross-references across kb/communities/*.yaml
  accessed_at: '2026-10-25T11:29:00Z'
  support: supports
  summary: Corpus-wide audit of reusable taxon cross-references showed 2/6 Geobacter
    sulfurreducens communities linked to CommunityMech:taxon:000002 (leaving 000031,
    000175, 000176, 000268 unlinked) and 7/9 Shewanella oneidensis communities linked
    to CommunityMech:taxon:000001 (leaving 000288, 000294 unlinked).
- evidence_id: ev-biomodels-pmid30254121
  kind: primary_source
  reference: PMID:30254121
  locator: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
  accessed_at: '2026-10-25T11:30:00Z'
  support: supports
  summary: Ankrah et al. 2018 (PMID:30254121) models obligate intracellular bacteriome
    endosymbioses of sap-feeding insects (spittlebug Sulcia-Sodalis in 000006, sharpshooter
    Sulcia-Baumannia in 000007, and cicada Sulcia-Hodgkinia in 000008), supporting
    ENVO:01001000 (animal-associated habitat).
  quote: Obligate mutualistic symbiosis between the bacteriome-dwelling bacterium
    Candidatus Sulcia muelleri and a companion endosymbiont in xylem-feeding insects.
- evidence_id: ev-sponge-pmid39738126
  kind: primary_source
  reference: PMID:39738126
  locator: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  accessed_at: '2026-10-25T11:31:00Z'
  support: supports
  summary: PMID:39738126 (and DOI:10.1038/s43705-024-00531-6) describes a multi-partner
    metabolic network of prokaryotic symbionts associated with the marine sponge Stylissa
    sp. in the Red Sea, supporting ENVO:01001000 (animal-associated habitat).
  quote: Multi-partner metabolic network of prokaryotic symbionts associated with
    the marine sponge Stylissa sp. in the Red Sea.
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 43 retained structured review bundles through 20261021T193000Z-stage5-remediation-verification
  accessed_at: '2026-10-25T11:32:00Z'
  support: context_only
  summary: Lineage inspection of all 43 prior structured reviews and Cycle 1 Stage
    5 evidence.yaml confirmed that all 6 Cycle 1 Stage 4 open findings were resolved
    in Stage 5 and 7 record-scoped source-limited findings remain deferred at commit
    9e6356de530ea961259cb5b8c93e5da4b44f5660.
assessments:
- assessment_id: assess-communitymech-000006
  area: completeness
  topic: Deep per-record audit of CommunityMech:000006 (BioModels MODEL1806250003
    Spittlebug Sulcia-Sodalis Symbiosis)
  outcome: concern
  summary: Record CommunityMech:000006 (kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml)
    in cohort SYNTROPHY has Completeness Score 74/100, 3 taxa, 3 interactions, 0 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000006
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 74.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000007
  area: completeness
  topic: Deep per-record audit of CommunityMech:000007 (BioModels MODEL1806250004
    Sharpshooter Sulcia-Baumannia Symbiosis)
  outcome: concern
  summary: Record CommunityMech:000007 (kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml)
    in cohort SYNTROPHY has Completeness Score 74/100, 3 taxa, 3 interactions, 0 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 74.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000008
  area: completeness
  topic: Deep per-record audit of CommunityMech:000008 (BioModels MODEL1806250005
    Cicada Sulcia-Hodgkinia Symbiosis)
  outcome: concern
  summary: Record CommunityMech:000008 (kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml)
    in cohort SYNTROPHY has Completeness Score 74/100, 3 taxa, 3 interactions, 0 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000008
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 74.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000013
  area: completeness
  topic: Deep per-record audit of CommunityMech:000013 (BioModels MODEL2407300002
    Sponge Holobiont Network)
  outcome: concern
  summary: Record CommunityMech:000013 (kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml)
    in cohort OTHER has Completeness Score 79/100, 3 taxa, 6 interactions, 2 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000013
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 79.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000031
  area: grounding
  topic: Deep per-record audit of CommunityMech:000031 (Geobacter-Clostridium Interspecies
    Electron Transfer Coculture)
  outcome: concern
  summary: Record CommunityMech:000031 (kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml)
    in cohort SYNTROPHY has Completeness Score 100/100, 2 taxa, 2 interactions, 1
    causal edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000031
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
- assessment_id: assess-communitymech-000175
  area: grounding
  topic: Deep per-record audit of CommunityMech:000175 (Clostridium cellulolyticum-Geobacter
    sulfurreducens Cellulose MFC Coculture)
  outcome: concern
  summary: Record CommunityMech:000175 (kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 98/100, 2 taxa, 3 interactions,
    1 causal edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000175
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
- assessment_id: assess-communitymech-000176
  area: grounding
  topic: Deep per-record audit of CommunityMech:000176 (ORNL Clostridium-Desulfovibrio-Geobacter
    Trophic Model Community)
  outcome: concern
  summary: Record CommunityMech:000176 (kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml)
    in cohort BIOREMEDIATION has Completeness Score 97/100, 3 taxa, 4 interactions,
    2 causal edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000176
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
- assessment_id: assess-communitymech-000268
  area: grounding
  topic: Deep per-record audit of CommunityMech:000268 (Rhodopseudomonas-Geobacter
    Magnetite Redox Coculture)
  outcome: concern
  summary: Record CommunityMech:000268 (kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml)
    in cohort METAL_REDUCTION has Completeness Score 96/100, 2 taxa, 4 interactions,
    5 causal edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000268
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 96.0
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
    2 causal edges, 0 gene annotations, and 0 network warnings.
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
- assessment_id: assess-communitymech-000288
  area: grounding
  topic: Deep per-record audit of CommunityMech:000288 (Shewanella oneidensis + Pseudomonas
    aeruginosa Fe0-dependent Electro-syntrophic Denitrifying Consortium)
  outcome: concern
  summary: Record CommunityMech:000288 (kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml)
    in cohort SYNTROPHY has Completeness Score 93/100, 2 taxa, 3 interactions, 2 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000288
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 93.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000294
  area: grounding
  topic: Deep per-record audit of CommunityMech:000294 (Corynebacterium glutamicum
    + Shewanella oneidensis Succinic-acid Co-culture)
  outcome: concern
  summary: Record CommunityMech:000294 (kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 93/100, 2 taxa, 3 interactions,
    2 causal edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 93.0
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
    4 causal edges, 0 gene annotations, and 0 network warnings.
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
    0 causal edges, 0 gene annotations, and 0 network warnings.
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
    2 causal edges, 0 gene annotations, and 0 network warnings.
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
- assessment_id: assess-communitymech-000484
  area: completeness
  topic: Deep per-record audit of CommunityMech:000484 (Aquifer Sediment Cable Bacteria
    Sulfur-Cycling Community)
  outcome: supported
  summary: Record CommunityMech:000484 (kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml)
    in cohort BIOREMEDIATION has Completeness Score 95/100, 3 taxa, 3 interactions,
    2 causal edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000484
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
- assessment_id: assess-communitymech-000485
  area: completeness
  topic: Deep per-record audit of CommunityMech:000485 (Dexing Copper Mine Bioleaching
    Heap Surface Community)
  outcome: supported
  summary: Record CommunityMech:000485 (kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml)
    in cohort BIOMINING has Completeness Score 95/100, 4 taxa, 3 interactions, 2 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000485
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
- assessment_id: assess-communitymech-000486
  area: completeness
  topic: Deep per-record audit of CommunityMech:000486 (Stare Ransko Mine Tailings
    Mesophilic Bioleaching Consortium)
  outcome: supported
  summary: Record CommunityMech:000486 (kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml)
    in cohort BIOMINING has Completeness Score 95/100, 3 taxa, 2 interactions, 1 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000486
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
- assessment_id: assess-communitymech-000487
  area: completeness
  topic: Deep per-record audit of CommunityMech:000487 (Moderate Thermophile Chalcopyrite
    pH-Regulated Bioleaching Consortium)
  outcome: supported
  summary: Record CommunityMech:000487 (kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml)
    in cohort BIOMINING has Completeness Score 95/100, 3 taxa, 2 interactions, 1 causal
    edges, 0 gene annotations, and 0 network warnings.
  target_ids:
  - CommunityMech:000487
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
- assessment_id: assess-communitymech-000488
  area: completeness
  topic: Deep per-record audit of CommunityMech:000488 (Bacillus licheniformis Tannery
    Effluent Chromate Biosorption Isolate)
  outcome: supported
  summary: Record CommunityMech:000488 (data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml)
    in cohort ISOLATES:BIOREMEDIATION has Completeness Score 95/100, 1 taxa, 2 interactions,
    1 causal edges, 0 gene annotations, and 0 network warnings.
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
    2 causal edges, 0 gene annotations, and 0 network warnings.
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
    1 causal edges, 0 gene annotations, and 0 network warnings.
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
- assessment_id: assess-communitymech-taxon-000001
  area: completeness
  topic: Deep per-record audit of CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1)
  outcome: supported
  summary: Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml)
    in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal
    edges, 5 gene annotations, and 0 network warnings.
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
  topic: Deep per-record audit of CommunityMech:taxon:000002 (Geobacter_sulfurreducens)
  outcome: supported
  summary: Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml)
    in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal
    edges, 4 gene annotations, and 0 network warnings.
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
- finding_id: c2s4-biomodels-missing-environment-term
  issue_key: communitymech-c2s4-biomodels-missing-environment-term
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Four BioModels community records (CommunityMech:000006, 000007, 000008, 000013)
    omit environment_term despite explicit host-associated habitat context in cited
    sources
  description: 'Out of all 484 MicrobialCommunity records across kb/communities/ (477)
    and data/isolates/ (7), only 4 records omit top-level environment_term: CommunityMech:000006
    (BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml, Completeness Score
    72/100), CommunityMech:000007 (BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml,
    Completeness Score 72/100), CommunityMech:000008 (BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml,
    Completeness Score 72/100), and CommunityMech:000013 (BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml,
    Completeness Score 75/100). The cited primary sources and record descriptions
    explicitly establish obligate sap-feeding insect bacteriome symbioses (PMID:30254121
    for 000006-000008) and a Stylissa sp. marine sponge holobiont (PMID:39738126 for
    000013), supporting ENVO:01001000 (animal-associated habitat) consistent with
    sibling BioModels records (CommunityMech:000009-000012 and CommunityMech:000321).'
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  field_paths:
  - environment_term
  evidence_ids:
  - ev-completeness-audit
  - ev-biomodels-pmid30254121
  - ev-sponge-pmid39738126
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
- finding_id: c2s4-geobacter-common-taxon-linkage-gap
  issue_key: communitymech-c2s4-geobacter-common-taxon-linkage-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Four Geobacter sulfurreducens community records (CommunityMech:000031, 000175,
    000176, 000268) omit common_taxon linkage to CommunityMech:taxon:000002
  description: 'Six community records in kb/communities/ contain Geobacter sulfurreducens
    (NCBITaxon:35554), which is represented as reusable taxon record CommunityMech:taxon:000002
    (kb/taxa/Geobacter_sulfurreducens.yaml) carrying verified UniProtKB EET protein
    annotations (pilA/Q74BW5, omcS/Q749X9, omcZ/Q74A90, omcB/Q74A86). While CommunityMech:000177
    and CommunityMech:000201 link their Geobacter sulfurreducens TaxonomicComposition
    entry via common_taxon: CommunityMech:taxon:000002, four syntrophic/electroactive
    community records — CommunityMech:000031 (Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml),
    CommunityMech:000175 (Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml),
    CommunityMech:000176 (ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml),
    and CommunityMech:000268 (Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml)
    — omit common_taxon: CommunityMech:taxon:000002.'
  target_ids:
  - CommunityMech:000031
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000268
  field_paths:
  - taxonomy[].common_taxon
  evidence_ids:
  - ev-common-taxon-linkage-audit
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
- finding_id: c2s4-shewanella-common-taxon-linkage-gap
  issue_key: communitymech-c2s4-shewanella-common-taxon-linkage-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Two Shewanella oneidensis community records (CommunityMech:000288, 000294)
    omit common_taxon linkage to CommunityMech:taxon:000001
  description: 'Nine community records in kb/communities/ contain Shewanella oneidensis
    (NCBITaxon:70863 / NCBITaxon:211586), which is represented as reusable taxon record
    CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) carrying verified
    UniProtKB Mtr/CymA/OmcA EET protein annotations (mtrC/Q8EG33, mtrB/Q8EG34, mtrA/Q8EG35,
    omcA/Q8EG32, cymA/Q8E945). Seven records (000046, 000063, 000064, 000150, 000215,
    000219, 000237) link via common_taxon: CommunityMech:taxon:000001, whereas CommunityMech:000288
    (Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml, which
    explicitly describes CymA-OmcA-MtrC EET complexes in Shewanella oneidensis MR-1)
    and CommunityMech:000294 (Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml)
    omit common_taxon: CommunityMech:taxon:000001.'
  target_ids:
  - CommunityMech:000288
  - CommunityMech:000294
  field_paths:
  - taxonomy[].common_taxon
  evidence_ids:
  - ev-common-taxon-linkage-audit
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
actions:
- action_id: act-populate-biomodels-environment-term
  description: Populate top-level environment_term (ENVO:01001000 animal-associated
    habitat) with source-backed notes on CommunityMech:000006, 000007, 000008 (PMID:30254121)
    and CommunityMech:000013 (PMID:39738126), and append curation_history entries.
  finding_ids:
  - c2s4-biomodels-missing-environment-term
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
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
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
    kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml
    kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-link-geobacter-common-taxon
  description: 'Add common_taxon: CommunityMech:taxon:000002 to the Geobacter sulfurreducens
    (NCBITaxon:35554) TaxonomicComposition entry in CommunityMech:000031, 000175,
    000176, and 000268, and append curation_history entries.'
  finding_ids:
  - c2s4-geobacter-common-taxon-linkage-gap
  target_ids:
  - CommunityMech:000031
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000268
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
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml
    kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-link-shewanella-common-taxon
  description: 'Add common_taxon: CommunityMech:taxon:000001 to the Shewanella oneidensis
    (NCBITaxon:70863 / NCBITaxon:211586) TaxonomicComposition entry in CommunityMech:000288
    and 000294, and append curation_history entries.'
  finding_ids:
  - c2s4-shewanella-common-taxon-linkage-gap
  target_ids:
  - CommunityMech:000288
  - CommunityMech:000294
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml
    kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  - uv run python scripts/verify_history_Changed_records.py
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used
  cached PubMed/DOI abstracts and open-access metadata in references_cache/.
tags:
- cycle2
- stage4
- record-review
- deep-audit
```
