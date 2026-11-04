# Cycle 6 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle 6 Records, Cycle 5 Stage 5 Remediated Records, and Actionable Community Records

- Review: 20261104T180000Z-c6s4-record-deep-audit
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-04T17:52:00Z
- Finished UTC: 2026-11-04T18:00:00Z
- Reviewer: antigravity-c6s4-record-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Deep per-record scientific and structural audit of 21 records (all 9 data/isolates/*.yaml records, both kb/taxa/*.yaml reusable taxon records, all 4 newly curated Cycle 6 community records [000501, 000502, 000503, 000504], all 3 community records remediated in Cycle 5 Stage 5 [000084, 000085, 000385], and 3 kb/communities/*.yaml records with newly identified actionable completeness gaps [000374, 000402, 000404]) at frozen Git revision 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.

## Scope And Provenance

Focused per-record deep audit of all isolate baselines (9), all reusable taxon records (2), all newly curated Cycle 6 community records (4), all Cycle 5 Stage 5 remediated community records (3), and all community records with new actionable Stage 5 remediation findings (3).

Selection: All 9 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 4 new Cycle 6 kb/communities/*.yaml records (000501-000504), 3 Cycle 5 Stage 5 remediated records (000084, 000085, 000385), and 3 kb/communities/*.yaml records (000374, 000402, 000404) surfaced by completeness audits.
Coverage: full; 21 reviewed / 21 in the declared population.
Source: git_commit at Git base 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000084 | kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml | maintained | CommunityMech:000084 (Streptococcus mutans - Selenomonas sputigena ECC Pathobiont Model) |
| CommunityMech:000085 | kb/communities/SMutans_VParvula_ASC_Biofilm.yaml | maintained | CommunityMech:000085 (Streptococcus mutans - Veillonella parvula Adult Severe Caries Model) |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | CommunityMech:000322 (Methylobacterium REE E-waste Platform) |
| CommunityMech:000374 | kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml | maintained | CommunityMech:000374 (Achromobacter-Enterobacter SL8-SL12 Cadmium Immobilization Coculture) |
| CommunityMech:000385 | kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml | maintained | CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium) |
| CommunityMech:000402 | kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml | maintained | CommunityMech:000402 (Delta nrfA Shewanella-Anammox Nitrite Coupled Consortium) |
| CommunityMech:000404 | kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml | maintained | CommunityMech:000404 (Wollastonite Ramichloridium-Talaromyces Fungal Consortium) |
| CommunityMech:000488 | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml | maintained | CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate) |
| CommunityMech:000489 | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml | maintained | CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate) |
| CommunityMech:000490 | data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml | maintained | CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate) |
| CommunityMech:000492 | data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml | maintained | CommunityMech:000492 (Intrasporangium chromatireducens Q5-1 Chromate Reduction Isolate) |
| CommunityMech:000495 | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml | maintained | CommunityMech:000495 (Ferroplasma acidiphilum ZJ Acid Mine Drainage Isolate) |
| CommunityMech:000501 | kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml | maintained | CommunityMech:000501 (Burkholderia-Bacillus C2 Masson Pine SynCom) |
| CommunityMech:000502 | kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml | maintained | CommunityMech:000502 (Bacillus B8-1 and A1 PAH Biofilm Consortium 1) |
| CommunityMech:000503 | kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml | maintained | CommunityMech:000503 (Bacillus B8-1 and A3 Naphthalene Biofilm Consortium 2) |
| CommunityMech:000504 | kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml | maintained | CommunityMech:000504 (Bacillus B8-1, A1, and A3 Three-Strain PAH Biofilm Consortium 4) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (Geobacter_sulfurreducens) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on 21 deep-audit records | passed | True | CommunityMech:000084, CommunityMech:000085, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000374, CommunityMech:000385, CommunityMech:000402, CommunityMech:000404, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000501, CommunityMech:000502, CommunityMech:000503, CommunityMech:000504, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 19 MicrobialCommunity records and 2 TaxonRecord files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| NetworkIntegrityAuditor check on 21 deep-audit records | passed | True | CommunityMech:000084, CommunityMech:000085, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000374, CommunityMech:000385, CommunityMech:000402, CommunityMech:000404, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000501, CommunityMech:000502, CommunityMech:000503, CommunityMech:000504, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 19/19 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor with 0 warnings. |

## Scientific And Domain Assessments

### Deep per-record audit of CommunityMech:000084 (Streptococcus mutans - Selenomonas sputigena ECC Pathobiont Model)

completeness: supported. Targets: CommunityMech:000084.

Record CommunityMech:000084 (kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml) in cohort ORAL has Completeness Score 98/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000085 (Streptococcus mutans - Veillonella parvula Adult Severe Caries Model)

completeness: supported. Targets: CommunityMech:000085.

Record CommunityMech:000085 (kb/communities/SMutans_VParvula_ASC_Biofilm.yaml) in cohort ORAL has Completeness Score 97/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

### Deep per-record audit of CommunityMech:000402 (Delta nrfA Shewanella-Anammox Nitrite Coupled Consortium)

completeness: concern. Targets: CommunityMech:000402.

Record CommunityMech:000402 (kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml) in cohort BIOTECHNOLOGY has Completeness Score 90/100, 3 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000404 (Wollastonite Ramichloridium-Talaromyces Fungal Consortium)

completeness: concern. Targets: CommunityMech:000404.

Record CommunityMech:000404 (kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml) in cohort BIOMINING has Completeness Score 90/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

### Deep per-record audit of CommunityMech:000501 (Burkholderia-Bacillus C2 Masson Pine SynCom)

completeness: supported. Targets: CommunityMech:000501.

Record CommunityMech:000501 (kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml) in cohort RHIZOSPHERE has Completeness Score 83/100, 5 taxa, 3 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000502 (Bacillus B8-1 and A1 PAH Biofilm Consortium 1)

completeness: supported. Targets: CommunityMech:000502.

Record CommunityMech:000502 (kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml) in cohort BIOREMEDIATION has Completeness Score 95/100, 2 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000503 (Bacillus B8-1 and A3 Naphthalene Biofilm Consortium 2)

completeness: supported. Targets: CommunityMech:000503.

Record CommunityMech:000503 (kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml) in cohort BIOREMEDIATION has Completeness Score 95/100, 2 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000504 (Bacillus B8-1, A1, and A3 Three-Strain PAH Biofilm Consortium 4)

completeness: supported. Targets: CommunityMech:000504.

Record CommunityMech:000504 (kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml) in cohort BIOREMEDIATION has Completeness Score 95/100, 3 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1)

completeness: supported. Targets: CommunityMech:taxon:000001.

Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 5 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000002 (Geobacter_sulfurreducens)

completeness: supported. Targets: CommunityMech:taxon:000002.

Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 4 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

## Category Boundaries


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
- Full-text PDFs behind publisher paywalls were not fetched; source verification used cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T180000Z-c6s4-record-deep-audit
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 6 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle
  6 Records, Cycle 5 Stage 5 Remediated Records, and Actionable Community Records
started_at: '2026-11-04T17:52:00Z'
finished_at: '2026-11-04T18:00:00Z'
reviewer:
  identity: antigravity-c6s4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 6 Stage 4 read-only review pass over frozen
    commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1 without record mutation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (3 P2 major findings across CommunityMech:000374, 000402,
  and 000404; 18 isolate/taxon/new-community/C5S5-remediated records pass with 0 defects)
scientific_review: true
summary: Deep per-record scientific and structural audit of 21 records (all 9 data/isolates/*.yaml
  records, both kb/taxa/*.yaml reusable taxon records, all 4 newly curated Cycle 6
  community records [000501, 000502, 000503, 000504], all 3 community records remediated
  in Cycle 5 Stage 5 [000084, 000085, 000385], and 3 kb/communities/*.yaml records
  with newly identified actionable completeness gaps [000374, 000402, 000404]) at
  frozen Git revision 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.
source:
  git_revision: 634cae02f33fd755d0c2dd38a6c03fd7d10041c1
  state: git_commit
  inputs:
  - path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    sha256: eeef4a3c72f6660c2263fe91ec7858610797c19fa513bf641e2a6234ff4414d4
    role: target
  - path: kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml
    sha256: 49c084f295ba077f383e193820af2dd4a1620e0af6310110f2da9eb71a4d77a8
    role: target
  - path: kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml
    sha256: 715ea160d2968d36d0d7d0fab42cfec1c66cd5cbbce39b3381861a036e9d6ff4
    role: target
  - path: kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml
    sha256: de9b2f80f9c505f9404ccc9f107d1bdfdf5849291e944cb5be6ce8063c8507f5
    role: target
  - path: kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml
    sha256: 4c540d55438895202d84cb0b25957c0637780be4e031b5029211b747ad07a18d
    role: target
  - path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
    sha256: 04ab8c93316524a7316f27651a9cf1b29cd83f6495e558c9a4c190c216301516
    role: target
  - path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
    sha256: 05bdd8b0222ec8e14e7b5b63b6be37e9f73bd8de356023cf52c0b6c47bb182d6
    role: target
  - path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    sha256: bc1fb667da9be21480d7f27961b01fc547c45dc3cef1ca63b58fe01584104076
    role: target
  - path: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
    sha256: f300a08a92756ce174019800b7a50cec74b8d9a6be17a56accd8e2daa8aa6cf3
    role: target
  - path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    sha256: 06d15492c6e358b75deffe722b5299d7b5f86bf15090276db87fda690c6e639e
    role: target
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
  - path: data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml
    sha256: cc05785add2613ee69f29971820f913e038de75e44d584a3d8ec22015377c0f1
    role: target
  - path: data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml
    sha256: 3be922d81b044ad742cd52ae866f3007d2f17141fc7355c4a34ad9f96ca304c4
    role: target
  - path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    sha256: 70d9761a556a3e744eb81c26f1906bb0ce697b3d64be526ecaafddea7404f978
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: e18219ed636fb72eba06642469cdcca904a0c2f21697a1893447f80dab179556
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
  description: Focused per-record deep audit of all isolate baselines (9), all reusable
    taxon records (2), all newly curated Cycle 6 community records (4), all Cycle
    5 Stage 5 remediated community records (3), and all community records with new
    actionable Stage 5 remediation findings (3).
  selection: All 9 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 4 new Cycle 6 kb/communities/*.yaml
    records (000501-000504), 3 Cycle 5 Stage 5 remediated records (000084, 000085,
    000385), and 3 kb/communities/*.yaml records (000374, 000402, 000404) surfaced
    by completeness audits.
  coverage: full
  population_size: 21
  reviewed_target_ids:
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000374
  - CommunityMech:000385
  - CommunityMech:000402
  - CommunityMech:000404
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000501
  - CommunityMech:000502
  - CommunityMech:000503
  - CommunityMech:000504
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
targets:
- target_id: CommunityMech:000084
  path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
  label: CommunityMech:000084 (Streptococcus mutans - Selenomonas sputigena ECC Pathobiont
    Model)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000085
  path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
  label: CommunityMech:000085 (Streptococcus mutans - Veillonella parvula Adult Severe
    Caries Model)
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
- target_id: CommunityMech:000501
  path: kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml
  label: CommunityMech:000501 (Burkholderia-Bacillus C2 Masson Pine SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000502
  path: kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml
  label: CommunityMech:000502 (Bacillus B8-1 and A1 PAH Biofilm Consortium 1)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000503
  path: kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml
  label: CommunityMech:000503 (Bacillus B8-1 and A3 Naphthalene Biofilm Consortium
    2)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000504
  path: kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml
  label: CommunityMech:000504 (Bacillus B8-1, A1, and A3 Three-Strain PAH Biofilm
    Consortium 4)
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
- check_id: chk-linkml-schema-deep-c6s4
  name: LinkML schema validation on 21 deep-audit records
  status: passed
  required: true
  summary: All 19 MicrobialCommunity records and 2 TaxonRecord files validate against
    src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000374
  - CommunityMech:000385
  - CommunityMech:000402
  - CommunityMech:000404
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000501
  - CommunityMech:000502
  - CommunityMech:000503
  - CommunityMech:000504
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -c 'validate 21 deep-audit records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-deep-c6s4
  name: NetworkIntegrityAuditor check on 21 deep-audit records
  status: passed
  required: true
  summary: All 19/19 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor
    with 0 warnings.
  target_ids:
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000374
  - CommunityMech:000385
  - CommunityMech:000402
  - CommunityMech:000404
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000501
  - CommunityMech:000502
  - CommunityMech:000503
  - CommunityMech:000504
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
- assessment_id: assess-communitymech-000084
  area: completeness
  topic: Deep per-record audit of CommunityMech:000084 (Streptococcus mutans - Selenomonas
    sputigena ECC Pathobiont Model)
  outcome: supported
  summary: Record CommunityMech:000084 (kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml)
    in cohort ORAL has Completeness Score 98/100, 2 taxa, 3 interactions, 2 causal
    edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000084
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
- assessment_id: assess-communitymech-000085
  area: completeness
  topic: Deep per-record audit of CommunityMech:000085 (Streptococcus mutans - Veillonella
    parvula Adult Severe Caries Model)
  outcome: supported
  summary: Record CommunityMech:000085 (kb/communities/SMutans_VParvula_ASC_Biofilm.yaml)
    in cohort ORAL has Completeness Score 97/100, 2 taxa, 3 interactions, 2 causal
    edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000085
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
- assessment_id: assess-communitymech-000402
  area: completeness
  topic: Deep per-record audit of CommunityMech:000402 (Delta nrfA Shewanella-Anammox
    Nitrite Coupled Consortium)
  outcome: concern
  summary: Record CommunityMech:000402 (kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 90/100, 3 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000402
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
- assessment_id: assess-communitymech-000404
  area: completeness
  topic: Deep per-record audit of CommunityMech:000404 (Wollastonite Ramichloridium-Talaromyces
    Fungal Consortium)
  outcome: concern
  summary: Record CommunityMech:000404 (kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml)
    in cohort BIOMINING has Completeness Score 90/100, 2 taxa, 3 interactions, 2 causal
    edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000404
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
- assessment_id: assess-communitymech-000501
  area: completeness
  topic: Deep per-record audit of CommunityMech:000501 (Burkholderia-Bacillus C2 Masson
    Pine SynCom)
  outcome: supported
  summary: Record CommunityMech:000501 (kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml)
    in cohort RHIZOSPHERE has Completeness Score 83/100, 5 taxa, 3 interactions, 0
    causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000501
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 83.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000502
  area: completeness
  topic: Deep per-record audit of CommunityMech:000502 (Bacillus B8-1 and A1 PAH Biofilm
    Consortium 1)
  outcome: supported
  summary: Record CommunityMech:000502 (kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml)
    in cohort BIOREMEDIATION has Completeness Score 95/100, 2 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000502
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
- assessment_id: assess-communitymech-000503
  area: completeness
  topic: Deep per-record audit of CommunityMech:000503 (Bacillus B8-1 and A3 Naphthalene
    Biofilm Consortium 2)
  outcome: supported
  summary: Record CommunityMech:000503 (kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml)
    in cohort BIOREMEDIATION has Completeness Score 95/100, 2 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000503
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
- assessment_id: assess-communitymech-000504
  area: completeness
  topic: Deep per-record audit of CommunityMech:000504 (Bacillus B8-1, A1, and A3
    Three-Strain PAH Biofilm Consortium 4)
  outcome: supported
  summary: Record CommunityMech:000504 (kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml)
    in cohort BIOREMEDIATION has Completeness Score 95/100, 3 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000504
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
  topic: Deep per-record audit of CommunityMech:taxon:000002 (Geobacter_sulfurreducens)
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
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used
  cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.
tags:
- cycle6
- stage4
- record-review
- deep-audit
```
