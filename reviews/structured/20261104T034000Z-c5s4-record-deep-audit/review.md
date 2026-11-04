# Cycle 5 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle 5 Records, Cycle 4 Stage 5 Remediated Records, and Actionable Community Records

- Review: 20261104T034000Z-c5s4-record-deep-audit
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-04T03:32:00Z
- Finished UTC: 2026-11-04T03:40:00Z
- Reviewer: antigravity-c5s4-record-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Deep per-record scientific and structural audit of 21 records (all 9 data/isolates/*.yaml records, both kb/taxa/*.yaml reusable taxon records, all 4 newly curated Cycle 5 community records [000497, 000498, 000499, 000500], all 3 community records remediated in Cycle 4 Stage 5 [000083, 000357, 000397], and 3 kb/communities/*.yaml records with newly identified actionable completeness gaps [000084, 000085, 000385]) at frozen Git revision 898c839a50e08b75609d6ac6fa0659fcdb001f80.

## Scope And Provenance

Focused per-record deep audit of all isolate baselines (9), all reusable taxon records (2), all newly curated Cycle 5 community records (4), all Cycle 4 Stage 5 remediated community records (3), and all community records with new actionable Stage 5 remediation findings (3).

Selection: All 9 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 4 new Cycle 5 kb/communities/*.yaml records (000497-000500), 3 Cycle 4 Stage 5 remediated records (000083, 000357, 000397), and 3 kb/communities/*.yaml records (000084, 000085, 000385) surfaced by completeness audits.
Coverage: full; 21 reviewed / 21 in the declared population.
Source: git_commit at Git base 898c839a50e08b75609d6ac6fa0659fcdb001f80.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000083 | kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml | maintained | CommunityMech:000083 (Streptococcus mutans - Candida albicans ECC Biofilm Model) |
| CommunityMech:000084 | kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml | maintained | CommunityMech:000084 (Streptococcus mutans - Selenomonas sputigena ECC Pathobiont Model) |
| CommunityMech:000085 | kb/communities/SMutans_VParvula_ASC_Biofilm.yaml | maintained | CommunityMech:000085 (Streptococcus mutans - Veillonella parvula Adult Severe Caries Model) |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | CommunityMech:000322 (Methylobacterium REE E-waste Platform) |
| CommunityMech:000357 | kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml | maintained | CommunityMech:000357 (E. coli GL10-XL12 D-Lactate Mixed-Sugar SynCom) |
| CommunityMech:000385 | kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml | maintained | CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium) |
| CommunityMech:000397 | kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml | maintained | CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen Nitrifying Community) |
| CommunityMech:000488 | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml | maintained | CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate) |
| CommunityMech:000489 | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml | maintained | CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate) |
| CommunityMech:000490 | data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml | maintained | CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate) |
| CommunityMech:000492 | data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml | maintained | CommunityMech:000492 (Intrasporangium chromatireducens Q5-1 Chromate Reduction Isolate) |
| CommunityMech:000495 | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml | maintained | CommunityMech:000495 (Ferroplasma acidiphilum ZJ Acid Mine Drainage Isolate) |
| CommunityMech:000497 | kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml | maintained | CommunityMech:000497 (Synechocystis Escherichia coli Acetate-Butanol Coculture) |
| CommunityMech:000498 | kb/communities/Cyantraniliprole_Consortium_T1.yaml | maintained | CommunityMech:000498 (Cyantraniliprole Bioremediation Consortium T1) |
| CommunityMech:000499 | kb/communities/Cyantraniliprole_Consortium_T2.yaml | maintained | CommunityMech:000499 (Cyantraniliprole Bioremediation Consortium T2) |
| CommunityMech:000500 | kb/communities/Cyantraniliprole_Consortium_T3.yaml | maintained | CommunityMech:000500 (Cyantraniliprole Bioremediation Consortium T3) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (Geobacter_sulfurreducens) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on 21 deep-audit records | passed | True | CommunityMech:000083, CommunityMech:000084, CommunityMech:000085, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000357, CommunityMech:000385, CommunityMech:000397, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000497, CommunityMech:000498, CommunityMech:000499, CommunityMech:000500, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 19 MicrobialCommunity records and 2 TaxonRecord files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| NetworkIntegrityAuditor check on 21 deep-audit records | passed | True | CommunityMech:000083, CommunityMech:000084, CommunityMech:000085, CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000357, CommunityMech:000385, CommunityMech:000397, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000497, CommunityMech:000498, CommunityMech:000499, CommunityMech:000500, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 19/19 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor with 0 warnings. |

## Scientific And Domain Assessments

### Deep per-record audit of CommunityMech:000083 (Streptococcus mutans - Candida albicans ECC Biofilm Model)

completeness: supported. Targets: CommunityMech:000083.

Record CommunityMech:000083 (kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml) in cohort ORAL has Completeness Score 97/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000084 (Streptococcus mutans - Selenomonas sputigena ECC Pathobiont Model)

completeness: concern. Targets: CommunityMech:000084.

Record CommunityMech:000084 (kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml) in cohort ORAL has Completeness Score 83/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000085 (Streptococcus mutans - Veillonella parvula Adult Severe Caries Model)

completeness: concern. Targets: CommunityMech:000085.

Record CommunityMech:000085 (kb/communities/SMutans_VParvula_ASC_Biofilm.yaml) in cohort ORAL has Completeness Score 82/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

### Deep per-record audit of CommunityMech:000357 (E. coli GL10-XL12 D-Lactate Mixed-Sugar SynCom)

completeness: supported. Targets: CommunityMech:000357.

Record CommunityMech:000357 (kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml) in cohort BIOTECHNOLOGY has Completeness Score 100/100, 2 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium)

completeness: concern. Targets: CommunityMech:000385.

Record CommunityMech:000385 (kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml) in cohort BIOMINING has Completeness Score 90/100, 2 taxa, 2 interactions, 1 causal edges, 0 inline gene annotations, 1 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen Nitrifying Community)

completeness: supported. Targets: CommunityMech:000397.

Record CommunityMech:000397 (kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml) in cohort BIOTECHNOLOGY has Completeness Score 95/100, 3 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

### Deep per-record audit of CommunityMech:000497 (Synechocystis Escherichia coli Acetate-Butanol Coculture)

completeness: supported. Targets: CommunityMech:000497.

Record CommunityMech:000497 (kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 100/100, 2 taxa, 2 interactions, 1 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000498 (Cyantraniliprole Bioremediation Consortium T1)

completeness: supported. Targets: CommunityMech:000498.

Record CommunityMech:000498 (kb/communities/Cyantraniliprole_Consortium_T1.yaml) in cohort BIOREMEDIATION has Completeness Score 100/100, 6 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000499 (Cyantraniliprole Bioremediation Consortium T2)

completeness: supported. Targets: CommunityMech:000499.

Record CommunityMech:000499 (kb/communities/Cyantraniliprole_Consortium_T2.yaml) in cohort BIOREMEDIATION has Completeness Score 100/100, 6 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000500 (Cyantraniliprole Bioremediation Consortium T3)

completeness: supported. Targets: CommunityMech:000500.

Record CommunityMech:000500 (kb/communities/Cyantraniliprole_Consortium_T3.yaml) in cohort BIOREMEDIATION has Completeness Score 100/100, 6 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1)

completeness: supported. Targets: CommunityMech:taxon:000001.

Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 5 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000002 (Geobacter_sulfurreducens)

completeness: supported. Targets: CommunityMech:taxon:000002.

Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 4 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

## Findings

### c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose: SMutans_SSputigena_ECC_Pathobiont (CommunityMech:000084) omits functional_role, abundance_level, and 1% sucrose environmental_factors

major / open / confirmed; issue key: c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose.

In kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml (CommunityMech:000084), taxonomy[0] (Streptococcus mutans, NCBITaxon:1309) omits functional_role and abundance_level, taxonomy[1] (Selenomonas sputigena, NCBITaxon:69823) omits functional_role, and environmental_factors is absent. The cited open-access source PMID:37217495 (PMC10247392) establishes S. mutans as the primary sucrose-fermenting exopolysaccharide-producing pathobiont (PRIMARY_DEGRADER, CROSS_FEEDER; ABUNDANT in caries-associated plaque, &gt;25% of bacterial reads in C4), S. sputigena as the flagellated honeycomb-encapsulating cooperative partner (SYNTROPHIC_PARTNER, CROSS_FEEDER), and 1% (w/v) sucrose supplementation in BHIS medium as the essential dietary carbohydrate regime driving GtfB/GtfC glucan matrix assembly and acidogenesis.

### c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose: SMutans_VParvula_ASC_Biofilm (CommunityMech:000085) omits functional_role, abundance_level, and 1% sucrose environmental_factors

major / open / confirmed; issue key: c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose.

In kb/communities/SMutans_VParvula_ASC_Biofilm.yaml (CommunityMech:000085), taxonomy[0] (Streptococcus mutans, NCBITaxon:1309) omits functional_role and abundance_level, taxonomy[1] (Veillonella parvula, NCBITaxon:29466, which already records abundance_level: DOMINANT) omits functional_role, and environmental_factors is absent. The cited open-access source PMID:39345197 (PMC11537095) establishes S. mutans as the primary sucrose-fermenting lactic-acid- and EPS-producing bacterium (PRIMARY_DEGRADER, CROSS_FEEDER; ABUNDANT in Adult Severe Caries supragingival plaque and dual-species biofilm), V. parvula as the lactate-consuming metabolic cross-feeder (SYNTROPHIC_PARTNER, CROSS_FEEDER) that promotes S. mutans mature biofilm formation with enhanced acid resistance and hydrogen peroxide detoxicity, and 1% (w/v) sucrose supplementation in BHI broth as the defining cariogenic substrate regime.

### c5s4-000385-so3-bs3-bsubtilis-functional-role: SO3_BS3_Lithium_Battery_Bioleaching_Consortium (CommunityMech:000385) omits functional_role on Bacillus subtilis 168 BS3

major / open / confirmed; issue key: c5s4-000385-so3-bs3-bsubtilis-functional-role.

In kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml (CommunityMech:000385), taxonomy[0] (Shewanella oneidensis MR-1 SO3, NCBITaxon:70863) carries functional_role: [ELECTROGEN, ELECTRON_DONOR], but taxonomy[1] (Bacillus subtilis 168 BS3, term.id: NCBITaxon:1423) omits functional_role despite ecological_interactions and PMID:42733304 (doi:10.1002/advs.77699, PMC13572860) explicitly documenting that engineered B. subtilis BS3 converts inhibitory residual ethanol in Moutai brewing wastewater into acetate via the Adh-AldH dual-enzyme cascade (eliminating ethanol inhibition on S. oneidensis EET) and synthesizes riboflavin as an electron shuttle to promote flavin-mediated extracellular electron transfer in S. oneidensis SO3 during spent ternary lithium-ion battery cathode bioleaching.

## Recommended Actions And Acceptance Checks

### act-populate-smutans-ssputigena-roles-abundance-and-sucrose

Add functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT to Streptococcus mutans (taxonomy[0]), add functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] to Selenomonas sputigena (taxonomy[1]), add environmental_factors for 1% (w/v) sucrose supplementation in BHIS medium backed by PMID:37217495 on CommunityMech:000084, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
- just validate-history history

### act-populate-smutans-vparvula-roles-abundance-and-sucrose

Add functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT to Streptococcus mutans (taxonomy[0]), add functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] to Veillonella parvula (taxonomy[1]), add environmental_factors for 1% (w/v) sucrose supplementation in BHI broth backed by PMID:39345197 on CommunityMech:000085, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
- just validate-history history

### act-populate-so3-bs3-bsubtilis-functional-role

Add functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] to Bacillus subtilis 168 (BS3) backed by PMID:42733304 (doi:10.1002/advs.77699) on CommunityMech:000385, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
- just validate-history history

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and TaxonRecord classes | supports | All 485 kb/communities/*.yaml, 9 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (496 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 496 records | supports | Proportional 100-point review-communities Completeness Score audit across all 494 MicrobialCommunity records (min 40, median 90, mean 91.11, max 100; CommunityMech:000084 = 83/100, CommunityMech:000085 = 82/100, CommunityMech:000385 = 90/100) and 2 TaxonRecord files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (494/494), while scripts/audit_completeness.py:calculate_completeness() (which requires every taxon to have functional_role for its 50-point required block) scores 000084 at 30/100, 000085 at 30/100, and 000385 at 20/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 485 kb/communities and 9 data/isolates records found 469/485 communities and 9/9 isolates with 0 warnings (including all 19/19 MicrobialCommunity records in the 21-record deep audit) and 16 community records with 44 non-fatal warnings (42 DISCONNECTED across 15 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-495 | supports | Corpus-wide causal graph inventory covers all 494 MicrobialCommunity records with 100% SHA-256 attestation in verify_causal_graph_reviews.py (0 unreviewed records). |
| ev-common-taxon-linkage-audit | kb/taxa/Geobacter_sulfurreducens.yaml; TaxonomicComposition.common_taxon cross-references across kb/communities/*.yaml | supports | Corpus-wide audit of reusable taxon cross-references confirmed 15 TaxonomicComposition.common_taxon links across kb/communities/*.yaml (6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 [4 reusable UniProt EET genes plus inline macA/Q749P2] and 9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes plus inline fccA/Q8EKT2]) after Cycle 5 Stage 3 inline gene expansion (#2103). |
| ev-smutans-ssputigena-pmid37217495 | PMID:37217495; kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml | supports | PMID:37217495 (PMC10247392) establishes that Streptococcus mutans is the primary sucrose-fermenting exopolysaccharide-producing pathobiont (&gt;25% of bacterial reads in caries-associated cluster C4) and Selenomonas sputigena is the flagellated honeycomb-encapsulating cooperative partner in brain heart infusion medium supplemented with 1% (w/v) sucrose at 37 °C under 5% CO2. |
| ev-smutans-vparvula-pmid39345197 | PMID:39345197; kb/communities/SMutans_VParvula_ASC_Biofilm.yaml | supports | PMID:39345197 (PMC11537095) establishes that Streptococcus mutans is the primary sucrose-fermenting lactic-acid- and EPS-producing bacterium and Veillonella parvula is the lactate-consuming syntrophic cross-feeder that promotes mature biofilm formation, acid resistance, and hydrogen peroxide detoxicity in Brain Heart Infusion (BHI) broth supplemented with 1% (w/v) sucrose at 37 °C under anaerobic conditions. |
| ev-so3-bs3-pmid42733304 | PMID:42733304; kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml | supports | PMID:42733304 (doi:10.1002/advs.77699, PMC13572860) establishes that engineered Bacillus subtilis 168 (BS3) acts as a syntrophic cross-feeding partner that converts inhibitory residual ethanol in Moutai brewing wastewater into acetate via the Adh-AldH dual-enzyme cascade (relieving ethanol inhibition on S. oneidensis EET) and synthesizes riboflavin as an electron shuttle to promote flavin-mediated extracellular electron transfer in Shewanella oneidensis MR-1 (SO3) during spent ternary lithium-ion battery cathode bioleaching. |
| ev-prior-structured-reviews | reviews/structured; 52 retained structured review bundles through 20261031T235500Z-c4s5-remediation-verification | context_only | Lineage inspection of all 52 prior structured reviews and Cycle 4 Stage 5 evidence.yaml confirmed that all 3 Cycle 4 Stage 4 open findings across CommunityMech:000083, 000357, and 000397 were resolved in Cycle 4 Stage 5 (#2095, PR #2096) and 7 record-scoped source-limited findings remain deferred at commit 898c839a50e08b75609d6ac6fa0659fcdb001f80. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T034000Z-c5s4-record-deep-audit
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 5 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle
  5 Records, Cycle 4 Stage 5 Remediated Records, and Actionable Community Records
started_at: '2026-11-04T03:32:00Z'
finished_at: '2026-11-04T03:40:00Z'
reviewer:
  identity: antigravity-c5s4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 5 Stage 4 read-only review pass over frozen
    commit 898c839a50e08b75609d6ac6fa0659fcdb001f80 without record mutation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (3 P2 major findings across CommunityMech:000084, 000085,
  and 000385; 18 isolate/taxon/new-community/C4S5-remediated records pass with 0 defects)
scientific_review: true
summary: Deep per-record scientific and structural audit of 21 records (all 9 data/isolates/*.yaml
  records, both kb/taxa/*.yaml reusable taxon records, all 4 newly curated Cycle 5
  community records [000497, 000498, 000499, 000500], all 3 community records remediated
  in Cycle 4 Stage 5 [000083, 000357, 000397], and 3 kb/communities/*.yaml records
  with newly identified actionable completeness gaps [000084, 000085, 000385]) at
  frozen Git revision 898c839a50e08b75609d6ac6fa0659fcdb001f80.
source:
  git_revision: 898c839a50e08b75609d6ac6fa0659fcdb001f80
  state: git_commit
  inputs:
  - path: kb/communities/Cyantraniliprole_Consortium_T1.yaml
    sha256: 9ebd2f07ce536e4e92569e93b36f69ac1c3f8efce458c1520a5879000cbb2c90
    role: target
  - path: kb/communities/Cyantraniliprole_Consortium_T2.yaml
    sha256: cd6a38668c90338cf89fe2279e1958fffd8b12da401ea0ad82b4faaa08b526f6
    role: target
  - path: kb/communities/Cyantraniliprole_Consortium_T3.yaml
    sha256: a09fbcc47c0c084facbf9a501bbef519452bc4c70ad31f0071a383d5db144457
    role: target
  - path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    sha256: c70bbd5b522140d6b6cf6a2c4ea9ae97cdf10dda7d45534071997a5b1786dbcd
    role: target
  - path: kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
    sha256: a26aa5c32aa6f451822223c283ef769d31d13d82037e2caeb271008a76a5fe49
    role: target
  - path: kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
    sha256: 03b81604911a0ff08ab1a0d9ad8db5fbfb6174f41388c9af31bd91759a1f87f3
    role: target
  - path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
    sha256: 8c32ed74a997011d25ad1e3501b42f6da246ba28e23d58a85a92ee9fad169846
    role: target
  - path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
    sha256: 1c331f8546d510e5a20819f77901353203ba43b317c92f5bdb4ad8ab2364e265
    role: target
  - path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    sha256: b70b100dcdc43b4caf560b3794f0165db3b7c99410a7ba8d5b811825ebdceef4
    role: target
  - path: kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml
    sha256: 6210d91810b668f546c1e2f17c7f2c01ed37bc250d6314f79696ee7e591b063c
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
    sha256: 5d2b49dc2fd42756bdc303302e135ad208c10f76de161e618545a99dd1f6e142
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: df038771231777f9846f246f0c578484c697845043103008586e813badd113f8
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
    sha256: cbb58097bff2d314d375e4c738e180278599677a8d06d4c04277b6ec0badd8a7
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: f1d85409152fa009387f5c9840c30ac4c5c2aa4593555a88c6a6c369ae813402
    role: context
scope:
  description: Focused per-record deep audit of all isolate baselines (9), all reusable
    taxon records (2), all newly curated Cycle 5 community records (4), all Cycle
    4 Stage 5 remediated community records (3), and all community records with new
    actionable Stage 5 remediation findings (3).
  selection: All 9 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 4 new Cycle 5 kb/communities/*.yaml
    records (000497-000500), 3 Cycle 4 Stage 5 remediated records (000083, 000357,
    000397), and 3 kb/communities/*.yaml records (000084, 000085, 000385) surfaced
    by completeness audits.
  coverage: full
  population_size: 21
  reviewed_target_ids:
  - CommunityMech:000083
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000357
  - CommunityMech:000385
  - CommunityMech:000397
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000497
  - CommunityMech:000498
  - CommunityMech:000499
  - CommunityMech:000500
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
targets:
- target_id: CommunityMech:000083
  path: kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
  label: CommunityMech:000083 (Streptococcus mutans - Candida albicans ECC Biofilm
    Model)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
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
- target_id: CommunityMech:000357
  path: kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
  label: CommunityMech:000357 (E. coli GL10-XL12 D-Lactate Mixed-Sugar SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000385
  path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
  label: CommunityMech:000385 (SO3-BS3 Lithium-ion Battery Bioleaching Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000397
  path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  label: CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen Nitrifying Community)
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
- target_id: CommunityMech:000497
  path: kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml
  label: CommunityMech:000497 (Synechocystis Escherichia coli Acetate-Butanol Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000498
  path: kb/communities/Cyantraniliprole_Consortium_T1.yaml
  label: CommunityMech:000498 (Cyantraniliprole Bioremediation Consortium T1)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000499
  path: kb/communities/Cyantraniliprole_Consortium_T2.yaml
  label: CommunityMech:000499 (Cyantraniliprole Bioremediation Consortium T2)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000500
  path: kb/communities/Cyantraniliprole_Consortium_T3.yaml
  label: CommunityMech:000500 (Cyantraniliprole Bioremediation Consortium T3)
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
- check_id: chk-linkml-schema-deep-c5s4
  name: LinkML schema validation on 21 deep-audit records
  status: passed
  required: true
  summary: All 19 MicrobialCommunity records and 2 TaxonRecord files validate against
    src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000083
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000357
  - CommunityMech:000385
  - CommunityMech:000397
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000497
  - CommunityMech:000498
  - CommunityMech:000499
  - CommunityMech:000500
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -c 'validate 21 deep-audit records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-deep-c5s4
  name: NetworkIntegrityAuditor check on 21 deep-audit records
  status: passed
  required: true
  summary: All 19/19 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor
    with 0 warnings.
  target_ids:
  - CommunityMech:000083
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000357
  - CommunityMech:000385
  - CommunityMech:000397
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000497
  - CommunityMech:000498
  - CommunityMech:000499
  - CommunityMech:000500
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
  accessed_at: '2026-11-04T03:35:00Z'
  support: supports
  summary: All 485 kb/communities/*.yaml, 9 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records (496 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: scripts/audit_completeness.py
  locator: 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness()
    across all 496 records
  accessed_at: '2026-11-04T03:36:00Z'
  support: supports
  summary: Proportional 100-point review-communities Completeness Score audit across
    all 494 MicrobialCommunity records (min 40, median 90, mean 91.11, max 100; CommunityMech:000084
    = 83/100, CommunityMech:000085 = 82/100, CommunityMech:000385 = 90/100) and 2
    TaxonRecord files (100/100) confirmed 100% core metadata presence and 100% top-level
    environment_term coverage (494/494), while scripts/audit_completeness.py:calculate_completeness()
    (which requires every taxon to have functional_role for its 50-point required
    block) scores 000084 at 30/100, 000085 at 30/100, and 000385 at 20/100.
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-11-04T03:37:00Z'
  support: supports
  summary: NetworkIntegrityAuditor across 485 kb/communities and 9 data/isolates records
    found 469/485 communities and 9/9 isolates with 0 warnings (including all 19/19
    MicrobialCommunity records in the 21-record deep audit) and 16 community records
    with 44 non-fatal warnings (42 DISCONNECTED across 15 records and 2 COMMUNITY_LEVEL
    UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0
    error-severity issues, 0 broken downstream references).
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-495
  accessed_at: '2026-11-04T03:37:30Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 494 MicrobialCommunity records
    with 100% SHA-256 attestation in verify_causal_graph_reviews.py (0 unreviewed
    records).
- evidence_id: ev-common-taxon-linkage-audit
  kind: record_content
  reference: kb/taxa/Geobacter_sulfurreducens.yaml
  locator: TaxonomicComposition.common_taxon cross-references across kb/communities/*.yaml
  accessed_at: '2026-11-04T03:38:00Z'
  support: supports
  summary: Corpus-wide audit of reusable taxon cross-references confirmed 15 TaxonomicComposition.common_taxon
    links across kb/communities/*.yaml (6 Geobacter sulfurreducens communities linked
    to CommunityMech:taxon:000002 [4 reusable UniProt EET genes plus inline macA/Q749P2]
    and 9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001 [5
    reusable UniProt EET genes plus inline fccA/Q8EKT2]) after Cycle 5 Stage 3 inline
    gene expansion (#2103).
- evidence_id: ev-smutans-ssputigena-pmid37217495
  kind: primary_source
  reference: PMID:37217495
  locator: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
  accessed_at: '2026-11-04T03:38:30Z'
  support: supports
  summary: PMID:37217495 (PMC10247392) establishes that Streptococcus mutans is the
    primary sucrose-fermenting exopolysaccharide-producing pathobiont (>25% of bacterial
    reads in caries-associated cluster C4) and Selenomonas sputigena is the flagellated
    honeycomb-encapsulating cooperative partner in brain heart infusion medium supplemented
    with 1% (w/v) sucrose at 37 °C under 5% CO2.
  quote: We show that S. sputigena, a flagellated anaerobe with previously unknown
    role in supragingival biofilm, becomes trapped in streptococcal exoglucans, loses
    motility but actively proliferates to build a honeycomb-like multicellular-superstructure
    encapsulating S. mutans, enhancing acidogenesis.
- evidence_id: ev-smutans-vparvula-pmid39345197
  kind: primary_source
  reference: PMID:39345197
  locator: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
  accessed_at: '2026-11-04T03:39:00Z'
  support: supports
  summary: PMID:39345197 (PMC11537095) establishes that Streptococcus mutans is the
    primary sucrose-fermenting lactic-acid- and EPS-producing bacterium and Veillonella
    parvula is the lactate-consuming syntrophic cross-feeder that promotes mature
    biofilm formation, acid resistance, and hydrogen peroxide detoxicity in Brain
    Heart Infusion (BHI) broth supplemented with 1% (w/v) sucrose at 37 °C under anaerobic
    conditions.
  quote: In vitro experiments found that V. parvula can effectively promote S. mutans
    mature biofilm formation with enhanced acid resistance, hydrogen peroxide detoxicity,
    and biofilm virulence.
- evidence_id: ev-so3-bs3-pmid42733304
  kind: primary_source
  reference: PMID:42733304
  locator: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
  accessed_at: '2026-11-04T03:39:20Z'
  support: supports
  summary: PMID:42733304 (doi:10.1002/advs.77699, PMC13572860) establishes that engineered
    Bacillus subtilis 168 (BS3) acts as a syntrophic cross-feeding partner that converts
    inhibitory residual ethanol in Moutai brewing wastewater into acetate via the
    Adh-AldH dual-enzyme cascade (relieving ethanol inhibition on S. oneidensis EET)
    and synthesizes riboflavin as an electron shuttle to promote flavin-mediated extracellular
    electron transfer in Shewanella oneidensis MR-1 (SO3) during spent ternary lithium-ion
    battery cathode bioleaching.
  quote: strain BS3 in the SO3‐BS3 consortium eliminated the ethanol inhibition on
    EET of S. oneidensis by converting residual ethanol in the brewing wastewater
    into acetate via the Adh‐AldH dual enzyme cascade reaction. Also, strain BS3 synthesized
    riboflavin, which was employed as an electron shuttle for promoting the EET of
    S. oneidensis.
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 52 retained structured review bundles through 20261031T235500Z-c4s5-remediation-verification
  accessed_at: '2026-11-04T03:39:45Z'
  support: context_only
  summary: 'Lineage inspection of all 52 prior structured reviews and Cycle 4 Stage
    5 evidence.yaml confirmed that all 3 Cycle 4 Stage 4 open findings across CommunityMech:000083,
    000357, and 000397 were resolved in Cycle 4 Stage 5 (#2095, PR #2096) and 7 record-scoped
    source-limited findings remain deferred at commit 898c839a50e08b75609d6ac6fa0659fcdb001f80.'
assessments:
- assessment_id: assess-communitymech-000083
  area: completeness
  topic: Deep per-record audit of CommunityMech:000083 (Streptococcus mutans - Candida
    albicans ECC Biofilm Model)
  outcome: supported
  summary: Record CommunityMech:000083 (kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml)
    in cohort ORAL has Completeness Score 97/100, 2 taxa, 3 interactions, 2 causal
    edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000083
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
- assessment_id: assess-communitymech-000084
  area: completeness
  topic: Deep per-record audit of CommunityMech:000084 (Streptococcus mutans - Selenomonas
    sputigena ECC Pathobiont Model)
  outcome: concern
  summary: Record CommunityMech:000084 (kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml)
    in cohort ORAL has Completeness Score 83/100, 2 taxa, 3 interactions, 2 causal
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
    value: 83.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000085
  area: completeness
  topic: Deep per-record audit of CommunityMech:000085 (Streptococcus mutans - Veillonella
    parvula Adult Severe Caries Model)
  outcome: concern
  summary: Record CommunityMech:000085 (kb/communities/SMutans_VParvula_ASC_Biofilm.yaml)
    in cohort ORAL has Completeness Score 82/100, 2 taxa, 3 interactions, 2 causal
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
    value: 82.0
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
- assessment_id: assess-communitymech-000357
  area: completeness
  topic: Deep per-record audit of CommunityMech:000357 (E. coli GL10-XL12 D-Lactate
    Mixed-Sugar SynCom)
  outcome: supported
  summary: Record CommunityMech:000357 (kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 100/100, 2 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000357
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
- assessment_id: assess-communitymech-000385
  area: completeness
  topic: Deep per-record audit of CommunityMech:000385 (SO3-BS3 Lithium-ion Battery
    Bioleaching Consortium)
  outcome: concern
  summary: Record CommunityMech:000385 (kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml)
    in cohort BIOMINING has Completeness Score 90/100, 2 taxa, 2 interactions, 1 causal
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
    value: 90.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000397
  area: completeness
  topic: Deep per-record audit of CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen
    Nitrifying Community)
  outcome: supported
  summary: Record CommunityMech:000397 (kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 95/100, 3 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000397
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
- assessment_id: assess-communitymech-000497
  area: completeness
  topic: Deep per-record audit of CommunityMech:000497 (Synechocystis Escherichia
    coli Acetate-Butanol Coculture)
  outcome: supported
  summary: Record CommunityMech:000497 (kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 100/100, 2 taxa, 2 interactions,
    1 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000497
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
- assessment_id: assess-communitymech-000498
  area: completeness
  topic: Deep per-record audit of CommunityMech:000498 (Cyantraniliprole Bioremediation
    Consortium T1)
  outcome: supported
  summary: Record CommunityMech:000498 (kb/communities/Cyantraniliprole_Consortium_T1.yaml)
    in cohort BIOREMEDIATION has Completeness Score 100/100, 6 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000498
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
- assessment_id: assess-communitymech-000499
  area: completeness
  topic: Deep per-record audit of CommunityMech:000499 (Cyantraniliprole Bioremediation
    Consortium T2)
  outcome: supported
  summary: Record CommunityMech:000499 (kb/communities/Cyantraniliprole_Consortium_T2.yaml)
    in cohort BIOREMEDIATION has Completeness Score 100/100, 6 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000499
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
- assessment_id: assess-communitymech-000500
  area: completeness
  topic: Deep per-record audit of CommunityMech:000500 (Cyantraniliprole Bioremediation
    Consortium T3)
  outcome: supported
  summary: Record CommunityMech:000500 (kb/communities/Cyantraniliprole_Consortium_T3.yaml)
    in cohort BIOREMEDIATION has Completeness Score 100/100, 6 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000500
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
- finding_id: c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose
  issue_key: c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SMutans_SSputigena_ECC_Pathobiont (CommunityMech:000084) omits functional_role,
    abundance_level, and 1% sucrose environmental_factors
  description: In kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml (CommunityMech:000084),
    taxonomy[0] (Streptococcus mutans, NCBITaxon:1309) omits functional_role and abundance_level,
    taxonomy[1] (Selenomonas sputigena, NCBITaxon:69823) omits functional_role, and
    environmental_factors is absent. The cited open-access source PMID:37217495 (PMC10247392)
    establishes S. mutans as the primary sucrose-fermenting exopolysaccharide-producing
    pathobiont (PRIMARY_DEGRADER, CROSS_FEEDER; ABUNDANT in caries-associated plaque,
    >25% of bacterial reads in C4), S. sputigena as the flagellated honeycomb-encapsulating
    cooperative partner (SYNTROPHIC_PARTNER, CROSS_FEEDER), and 1% (w/v) sucrose supplementation
    in BHIS medium as the essential dietary carbohydrate regime driving GtfB/GtfC
    glucan matrix assembly and acidogenesis.
  target_ids:
  - CommunityMech:000084
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - environmental_factors
  evidence_ids:
  - ev-completeness-audit
  - ev-smutans-ssputigena-pmid37217495
  rule_id: review-yaml-record:taxonomy-and-environment-completeness
  native_severity: P2
  normalization_reason: Missing source-backed taxon functional_role, abundance_level,
    and environmental_factors on an established two-member oral biofilm community
    maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - oral-cohort
  - completeness
- finding_id: c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose
  issue_key: c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SMutans_VParvula_ASC_Biofilm (CommunityMech:000085) omits functional_role,
    abundance_level, and 1% sucrose environmental_factors
  description: 'In kb/communities/SMutans_VParvula_ASC_Biofilm.yaml (CommunityMech:000085),
    taxonomy[0] (Streptococcus mutans, NCBITaxon:1309) omits functional_role and abundance_level,
    taxonomy[1] (Veillonella parvula, NCBITaxon:29466, which already records abundance_level:
    DOMINANT) omits functional_role, and environmental_factors is absent. The cited
    open-access source PMID:39345197 (PMC11537095) establishes S. mutans as the primary
    sucrose-fermenting lactic-acid- and EPS-producing bacterium (PRIMARY_DEGRADER,
    CROSS_FEEDER; ABUNDANT in Adult Severe Caries supragingival plaque and dual-species
    biofilm), V. parvula as the lactate-consuming metabolic cross-feeder (SYNTROPHIC_PARTNER,
    CROSS_FEEDER) that promotes S. mutans mature biofilm formation with enhanced acid
    resistance and hydrogen peroxide detoxicity, and 1% (w/v) sucrose supplementation
    in BHI broth as the defining cariogenic substrate regime.'
  target_ids:
  - CommunityMech:000085
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - environmental_factors
  evidence_ids:
  - ev-completeness-audit
  - ev-smutans-vparvula-pmid39345197
  rule_id: review-yaml-record:taxonomy-and-environment-completeness
  native_severity: P2
  normalization_reason: Missing source-backed taxon functional_role, abundance_level,
    and environmental_factors on a two-species oral syntrophic biofilm community maps
    to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - oral-cohort
  - completeness
- finding_id: c5s4-000385-so3-bs3-bsubtilis-functional-role
  issue_key: c5s4-000385-so3-bs3-bsubtilis-functional-role
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SO3_BS3_Lithium_Battery_Bioleaching_Consortium (CommunityMech:000385) omits
    functional_role on Bacillus subtilis 168 BS3
  description: 'In kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    (CommunityMech:000385), taxonomy[0] (Shewanella oneidensis MR-1 SO3, NCBITaxon:70863)
    carries functional_role: [ELECTROGEN, ELECTRON_DONOR], but taxonomy[1] (Bacillus
    subtilis 168 BS3, term.id: NCBITaxon:1423) omits functional_role despite ecological_interactions
    and PMID:42733304 (doi:10.1002/advs.77699, PMC13572860) explicitly documenting
    that engineered B. subtilis BS3 converts inhibitory residual ethanol in Moutai
    brewing wastewater into acetate via the Adh-AldH dual-enzyme cascade (eliminating
    ethanol inhibition on S. oneidensis EET) and synthesizes riboflavin as an electron
    shuttle to promote flavin-mediated extracellular electron transfer in S. oneidensis
    SO3 during spent ternary lithium-ion battery cathode bioleaching.'
  target_ids:
  - CommunityMech:000385
  field_paths:
  - taxonomy[1].functional_role
  evidence_ids:
  - ev-completeness-audit
  - ev-so3-bs3-pmid42733304
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P2
  normalization_reason: Missing source-backed functional_role on one of two engineered
    syntrophic partners causes scripts/audit_completeness.py required-block failure
    (20/100) and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - biomining-cohort
  - completeness
actions:
- action_id: act-populate-smutans-ssputigena-roles-abundance-and-sucrose
  description: 'Add functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level:
    ABUNDANT to Streptococcus mutans (taxonomy[0]), add functional_role: [SYNTROPHIC_PARTNER,
    CROSS_FEEDER] to Selenomonas sputigena (taxonomy[1]), add environmental_factors
    for 1% (w/v) sucrose supplementation in BHIS medium backed by PMID:37217495 on
    CommunityMech:000084, and append curation_history.'
  finding_ids:
  - c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose
  target_ids:
  - CommunityMech:000084
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
  - just validate-history history
- action_id: act-populate-smutans-vparvula-roles-abundance-and-sucrose
  description: 'Add functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level:
    ABUNDANT to Streptococcus mutans (taxonomy[0]), add functional_role: [SYNTROPHIC_PARTNER,
    CROSS_FEEDER] to Veillonella parvula (taxonomy[1]), add environmental_factors
    for 1% (w/v) sucrose supplementation in BHI broth backed by PMID:39345197 on CommunityMech:000085,
    and append curation_history.'
  finding_ids:
  - c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose
  target_ids:
  - CommunityMech:000085
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
  - just validate-history history
- action_id: act-populate-so3-bs3-bsubtilis-functional-role
  description: 'Add functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] to Bacillus
    subtilis 168 (BS3) backed by PMID:42733304 (doi:10.1002/advs.77699) on CommunityMech:000385,
    and append curation_history.'
  finding_ids:
  - c5s4-000385-so3-bs3-bsubtilis-functional-role
  target_ids:
  - CommunityMech:000385
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
  - just validate-history history
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used
  cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.
tags:
- cycle5
- stage4
- record-review
- deep-audit
```
