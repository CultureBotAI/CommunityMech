# Cycle 4 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle 4 Record, Cycle 3 Stage 5 Remediated Records, and Actionable Community Records

- Review: 20261031T200000Z-c4s4-record-deep-audit
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-31T19:52:00Z
- Finished UTC: 2026-10-31T20:00:00Z
- Reviewer: antigravity-c4s4-record-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Deep per-record scientific and structural audit of 18 records (all 9 data/isolates/*.yaml records, both kb/taxa/*.yaml reusable taxon records, the newly curated Cycle 4 community record 000496, all 3 community records remediated in Cycle 3 Stage 5 [000280, 000434, 000448], and 3 kb/communities/*.yaml records with newly identified actionable completeness gaps [000083, 000357, 000397]) at frozen Git revision 0b03bdf7f9250e686bb9d0be5d3b99b71d1a0795.

## Scope And Provenance

Focused per-record deep audit of all isolate baselines (9), all reusable taxon records (2), the newly curated Cycle 4 community record (1), all Cycle 3 Stage 5 remediated community records (3), and all community records with new actionable Stage 5 remediation findings (3).

Selection: All 9 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 1 new Cycle 4 kb/communities/*.yaml record (000496), 3 Cycle 3 Stage 5 remediated records (000280, 000434, 000448), and 3 kb/communities/*.yaml records (000083, 000357, 000397) surfaced by completeness audits.
Coverage: full; 18 reviewed / 18 in the declared population.
Source: git_commit at Git base 0b03bdf7f9250e686bb9d0be5d3b99b71d1a0795.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000083 | kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml | maintained | CommunityMech:000083 (Streptococcus mutans - Candida albicans ECC Biofilm Model) |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000280 | kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml | maintained | CommunityMech:000280 (Pinus armandii Endophytic Biocontrol SynCom) |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | CommunityMech:000322 (Methylobacterium REE E-waste Platform) |
| CommunityMech:000357 | kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml | maintained | CommunityMech:000357 (E. coli GL10-XL12 D-Lactate Mixed-Sugar SynCom) |
| CommunityMech:000397 | kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml | maintained | CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen Nitrifying Community) |
| CommunityMech:000434 | kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml | maintained | CommunityMech:000434 (Acidic Nitrification Minimal Consortium) |
| CommunityMech:000448 | kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml | maintained | CommunityMech:000448 (Soymilk Mixed-Starter Metabolic Division SynCom) |
| CommunityMech:000488 | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml | maintained | CommunityMech:000488 (Bacillus licheniformis Tannery Effluent Chromate Biosorption Isolate) |
| CommunityMech:000489 | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml | maintained | CommunityMech:000489 (Adapted Acidithiobacillus ferrooxidans Waste LED Metal Bioleaching Isolate) |
| CommunityMech:000490 | data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml | maintained | CommunityMech:000490 (Ferrimicrobium acidiphilum Acidophilic Extracellular Iron Respiration Isolate) |
| CommunityMech:000492 | data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml | maintained | CommunityMech:000492 (Intrasporangium chromatireducens Q5-1 Chromate Reduction Isolate) |
| CommunityMech:000495 | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml | maintained | CommunityMech:000495 (Ferroplasma acidiphilum ZJ Acid Mine Drainage Isolate) |
| CommunityMech:000496 | kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml | maintained | CommunityMech:000496 (Methylomicrobium-Arthrospira Biogas Conversion Coculture) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (Geobacter_sulfurreducens) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on 18 deep-audit records | passed | True | CommunityMech:000083, CommunityMech:000273, CommunityMech:000280, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000357, CommunityMech:000397, CommunityMech:000434, CommunityMech:000448, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000496, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 16 MicrobialCommunity records and 2 TaxonRecord files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| NetworkIntegrityAuditor check on 18 deep-audit records | passed | True | CommunityMech:000083, CommunityMech:000273, CommunityMech:000280, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000357, CommunityMech:000397, CommunityMech:000434, CommunityMech:000448, CommunityMech:000488, CommunityMech:000489, CommunityMech:000490, CommunityMech:000492, CommunityMech:000495, CommunityMech:000496, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 16/16 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor with 0 warnings. |

## Scientific And Domain Assessments

### Deep per-record audit of CommunityMech:000083 (Streptococcus mutans - Candida albicans ECC Biofilm Model)

completeness: concern. Targets: CommunityMech:000083.

Record CommunityMech:000083 (kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml) in cohort ORAL has Completeness Score 80/100, 2 taxa, 3 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)

completeness: supported. Targets: CommunityMech:000273.

Record CommunityMech:000273 (data/isolates/Chromobacterium_Gold_Biocyanidation.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 91/100, 1 taxa, 4 interactions, 2 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000280 (Pinus armandii Endophytic Biocontrol SynCom)

completeness: supported. Targets: CommunityMech:000280.

Record CommunityMech:000280 (kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml) in cohort RHIZOSPHERE has Completeness Score 77/100, 5 taxa, 4 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

completeness: concern. Targets: CommunityMech:000357.

Record CommunityMech:000357 (kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml) in cohort BIOTECHNOLOGY has Completeness Score 90/100, 2 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen Nitrifying Community)

completeness: concern. Targets: CommunityMech:000397.

Record CommunityMech:000397 (kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml) in cohort BIOTECHNOLOGY has Completeness Score 85/100, 3 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000434 (Acidic Nitrification Minimal Consortium)

completeness: supported. Targets: CommunityMech:000434.

Record CommunityMech:000434 (kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml) in cohort BIOTECHNOLOGY has Completeness Score 80/100, 2 taxa, 1 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:000448 (Soymilk Mixed-Starter Metabolic Division SynCom)

completeness: supported. Targets: CommunityMech:000448.

Record CommunityMech:000448 (kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml) in cohort BIOTECHNOLOGY has Completeness Score 83/100, 3 taxa, 2 interactions, 0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

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

### Deep per-record audit of CommunityMech:000496 (Methylomicrobium-Arthrospira Biogas Conversion Coculture)

completeness: supported. Targets: CommunityMech:000496.

Record CommunityMech:000496 (kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 100/100, 2 taxa, 4 interactions, 3 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1)

completeness: supported. Targets: CommunityMech:taxon:000001.

Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 5 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000002 (Geobacter_sulfurreducens)

completeness: supported. Targets: CommunityMech:taxon:000002.

Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, 4 inline gene annotations, 0 reusable CommonTaxon links, and 0 network warnings.

## Findings

### c4s4-000083-smutans-calbicans-roles-metabolites-and-sucrose: Streptococcus mutans-Candida albicans ECC Biofilm (CommunityMech:000083) omits source-backed functional_role and DOMINANT/ABUNDANT abundance_level on both co-species biofilm members, exopolysaccharide (CHEBI:72813) on ecological_interactions[1], and environmental_factors for 1% sucrose availability

major / open / confirmed; issue key: communitymech-c4s4-000083-smutans-calbicans-roles-metabolites-and-sucrose.

CommunityMech:000083 (kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml, proportional Completeness Score 80/100; scripts/audit_completeness.py score 25/100) models the cariogenic plaque biofilm co-infection of Streptococcus mutans UA159 (NCBITaxon:1309) and Candida albicans SC5314 (NCBITaxon:5476) in early childhood caries (PMID:24566629). In taxonomy, Streptococcus mutans omits functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: DOMINANT, and Candida albicans omits functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: ABUNDANT, despite verbatim support in the already-curated PMID:24566629 snippets (S. mutans GtfB synthesizes glucan exopolysaccharides from 1% sucrose and binds fungal mannan and beta-1,3-glucan sites, while C. albicans augments EPS production and viable S. mutans carriage in cospecies biofilms inoculated at ~2 x 10^6 CFU/mL S. mutans and ~2 x 10^4 CFU/mL C. albicans). In addition, ecological_interactions[1] ('Candida-Driven EPS Amplification of Streptococcus mutans') omits metabolites exopolysaccharide (CHEBI:72813, which is already curated in related_ingredients[0] backed by the identical PMID:24566629 snippet), and environmental_factors is absent despite growth_media[0].evidence[0] (PMID:24566629) establishing 1% (30 mM) sucrose availability in UFYTE broth at 37 °C under 5% CO2.

### c4s4-000357-ecoli-gl10-xl12-roles-and-abundance: E. coli GL10-XL12 D-Lactate Mixed-Sugar SynCom (CommunityMech:000357) omits PRIMARY_DEGRADER functional_role and DOMINANT abundance_level on both engineered specialist strains

major / open / confirmed; issue key: communitymech-c4s4-000357-ecoli-gl10-xl12-roles-and-abundance.

CommunityMech:000357 (kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml, proportional Completeness Score 90/100; scripts/audit_completeness.py score 35/100) models the two-strain division-of-labor consortium of glucose-specialized Escherichia coli GL10 and xylose-utilizing Escherichia coli XL12 (NCBITaxon:562) for mixed glucose/xylose co-fermentation to optically pure D-lactate in M9 medium containing 5 g/L glucose and 5 g/L xylose (PMID:42038008, doi:10.1016/j.bidere.2026.100072). Both taxonomy entries omit functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT despite verbatim support in the already-curated PMID:42038008 snippets ('Two division-of-labor engineered E. coli strains, XL12 and GL10, were constructed and characterized in terms of sugar utilization and D-lactate synthesis capabilities.' and 'The initial OD600 was adjust to 0.2, with the inoculation ratio of GL10 and XL12 was 1:1.').

### c4s4-000397-nitrifying-syncom-roles-and-abundance: Defined Three-Strain Organic-Nitrogen Nitrifying Community (CommunityMech:000397) omits functional_role and ABUNDANT abundance_level across all three synthetic consortium members

major / open / confirmed; issue key: communitymech-c4s4-000397-nitrifying-syncom-roles-and-abundance.

CommunityMech:000397 (kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml, proportional Completeness Score 85/100; scripts/audit_completeness.py score 15/100) models the defined three-species nitrifying consortium of Bacillus badius NBRC 15713 (NCBITaxon:1455, Pseudobacillus badius), Nitrosomonas europaea NBRC 14298 (NCBITaxon:915), and Nitrobacter winogradskyi NBRC 14297 (NCBITaxon:913) under selected organic nitrogen conditions (PMID:42668143, doi:10.1093/bbb/zbag131). In taxonomy, ammonifying heterotroph Bacillus badius NBRC 15713 omits functional_role: [PRIMARY_DEGRADER] and abundance_level: ABUNDANT, chemolithoautotrophic ammonia oxidizer Nitrosomonas europaea NBRC 14298 omits functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER] and abundance_level: ABUNDANT, and chemolithoautotrophic nitrite oxidizer Nitrobacter winogradskyi NBRC 14297 omits functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER] and abundance_level: ABUNDANT despite verbatim support in the already-curated PMID:42668143 snippets for sequential ammonification and nitrification by the three defined strains.

## Recommended Actions And Acceptance Checks

### act-populate-smutans-calbicans-roles-metabolites-and-sucrose

Add functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: DOMINANT to Streptococcus mutans, add functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: ABUNDANT to Candida albicans, add metabolites exopolysaccharide (CHEBI:72813) to ecological_interactions[1] ('Candida-Driven EPS Amplification of Streptococcus mutans'), add environmental_factors for 1% (30 mM) sucrose availability backed by PMID:24566629 on CommunityMech:000083, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-populate-ecoli-gl10-xl12-roles-and-abundance

Add functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT to Escherichia coli GL10 and Escherichia coli XL12 backed by PMID:42038008 (doi:10.1016/j.bidere.2026.100072) on CommunityMech:000357, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-populate-nitrifying-syncom-roles-and-abundance

Add functional_role: [PRIMARY_DEGRADER] and abundance_level: ABUNDANT to Bacillus badius NBRC 15713 (NCBITaxon:1455, Pseudobacillus badius), add functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER] and abundance_level: ABUNDANT to Nitrosomonas europaea NBRC 14298 and Nitrobacter winogradskyi NBRC 14297 backed by PMID:42668143 (doi:10.1093/bbb/zbag131) on CommunityMech:000397, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
- uv run python scripts/verify_history_Changed_records.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and TaxonRecord classes | supports | All 481 kb/communities/*.yaml, 9 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (492 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 492 records | supports | Proportional 100-point review-communities Completeness Score audit across all 490 MicrobialCommunity records (min 40, median 90, mean 90.97, max 100; CommunityMech:000083 = 80/100, CommunityMech:000357 = 90/100, CommunityMech:000397 = 85/100) and 2 TaxonRecord files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (490/490), while scripts/audit_completeness.py:calculate_completeness() (which requires every taxon to have functional_role for its 50-point required block) scores 000083 at 25/100, 000357 at 35/100, and 000397 at 15/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 481 kb/communities and 9 data/isolates records found 465/481 communities and 9/9 isolates with 0 warnings (including all 16/16 MicrobialCommunity records in the 18-record deep audit) and 16 community records with 44 non-fatal warnings (42 DISCONNECTED across 15 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-491 | supports | Corpus-wide causal graph inventory covers all 490 MicrobialCommunity records with 100% SHA-256 attestation in verify_causal_graph_reviews.py (0 unreviewed records). |
| ev-common-taxon-linkage-audit | kb/taxa/Geobacter_sulfurreducens.yaml; TaxonomicComposition.common_taxon cross-references across kb/communities/*.yaml | supports | Corpus-wide audit of reusable taxon cross-references confirmed 6/6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 (4 UniProt EET genes) and 9/9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001 (5 UniProt EET genes) with Cycle 4 Stage 3 inline gene expansion (#2091). |
| ev-smutans-calbicans-pmid24566629 | PMID:24566629; kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml | supports | PMID:24566629 establishes that Streptococcus mutans and Candida albicans are the two co-species cariogenic biofilm members under 1% (30 mM) sucrose availability in UFYTE broth at 37 °C under 5% CO2, with C. albicans augmenting exopolysaccharide (EPS, CHEBI:72813) accumulation and viable S. mutans carriage while fungal mannan and beta-1,3-glucan provide sites for S. mutans GtfB binding and activity. |
| ev-ecoli-gl10-xl12-pmid42038008 | PMID:42038008; kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml | supports | PMID:42038008 (doi:10.1016/j.bidere.2026.100072) establishes that glucose-specialized E. coli GL10 and xylose-utilizing E. coli XL12 act as the two division-of-labor sugar-degrading consortium members co-fermenting 5 g/L glucose and 5 g/L xylose in M9 medium at 37 °C to optically pure D-lactate (3.76 g/L at a 1:1 GL10:XL12 inoculation ratio and 4.53 g/L at a 1:5 ratio). |
| ev-nitrifying-syncom-pmid42668143 | PMID:42668143; kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml | supports | PMID:42668143 (doi:10.1093/bbb/zbag131) establishes that Bacillus badius NBRC 15713 (NCBITaxon:1455, Pseudobacillus badius), Nitrosomonas europaea NBRC 14298 (NCBITaxon:915), and Nitrobacter winogradskyi NBRC 14297 (NCBITaxon:913) form a defined three-strain nitrifying microbial community performing sequential ammonification and nitrification under selected organic nitrogen conditions. |
| ev-prior-structured-reviews | reviews/structured; 49 retained structured review bundles through 20261031T081500Z-c3s5-remediation-verification | context_only | Lineage inspection of all 49 prior structured reviews and Cycle 3 Stage 5 evidence.yaml confirmed that all 3 Cycle 3 Stage 4 open findings across CommunityMech:000280, 000434, and 000448 were resolved in Cycle 3 Stage 5 (#2084, PR #2085) and 7 record-scoped source-limited findings remain deferred at commit 0b03bdf7f9250e686bb9d0be5d3b99b71d1a0795. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T200000Z-c4s4-record-deep-audit
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 4 Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, New Cycle
  4 Record, Cycle 3 Stage 5 Remediated Records, and Actionable Community Records
started_at: '2026-10-31T19:52:00Z'
finished_at: '2026-10-31T20:00:00Z'
reviewer:
  identity: antigravity-c4s4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 4 Stage 4 read-only review pass over frozen
    commit 0b03bdf7f9250e686bb9d0be5d3b99b71d1a0795 without record mutation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (3 P2 major findings across CommunityMech:000083, 000357,
  and 000397; 15 isolate/taxon/new-community/C3S5-remediated records pass with 0 defects)
scientific_review: true
summary: Deep per-record scientific and structural audit of 18 records (all 9 data/isolates/*.yaml
  records, both kb/taxa/*.yaml reusable taxon records, the newly curated Cycle 4 community
  record 000496, all 3 community records remediated in Cycle 3 Stage 5 [000280, 000434,
  000448], and 3 kb/communities/*.yaml records with newly identified actionable completeness
  gaps [000083, 000357, 000397]) at frozen Git revision 0b03bdf7f9250e686bb9d0be5d3b99b71d1a0795.
source:
  git_revision: 0b03bdf7f9250e686bb9d0be5d3b99b71d1a0795
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
  - path: data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml
    sha256: cc05785add2613ee69f29971820f913e038de75e44d584a3d8ec22015377c0f1
    role: target
  - path: data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml
    sha256: 3be922d81b044ad742cd52ae866f3007d2f17141fc7355c4a34ad9f96ca304c4
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
  - path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    sha256: 13b8ee224941b8e8a9767f0543b9eea1768c6499e311d0cde2cca07ade2e708d
    role: target
  - path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    sha256: b3843b5e2f64d179b4bc11a1558b7f977c025252fa6fe16d8ab82e0dfb292ec1
    role: target
  - path: kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
    sha256: 5d5c7c4e2d853489be775ef1cc44ec611af78b2dff902287c1bf2f18bfa9ad4d
    role: target
  - path: kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml
    sha256: 3cbfb0fc0d3b7cd9911a140d3380317c3ab0b97817fd9323b93826d5764ba2bf
    role: target
  - path: kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml
    sha256: b2a5b083856cdb822daec58cd6da7b794f8e03bb575f20fcfbdc9d9c81769202
    role: target
  - path: kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
    sha256: fb7d747151fb52f52127e035683a77dcb1596d6f1fc97ac1e8635298ce24fd34
    role: target
  - path: kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml
    sha256: f8b17ce636bfb8c48470f7664fc1497566777d760886bb9c557c7e5c16fa8cf3
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: b081a3672463ea1a9b240583e63d3273bfdf27d600be6e2df99c85b4394f0a27
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: 8d3910162407ca61bcb5bc1ebbec2c7f1f57e32bea34149d4f873a86bc257061
    role: target
  - path: reports/causal_graph_review/inventory.tsv
    sha256: c25700a2a7279bcb0dd7aa15c074a3227882170f0d86016298488f0ae7e4d69a
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: 004ddf43435ad8e3bb1a905a6ee71011f66ad4d8aaaa9da5613142c7f1132205
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Focused per-record deep audit of all isolate baselines (9), all reusable
    taxon records (2), the newly curated Cycle 4 community record (1), all Cycle 3
    Stage 5 remediated community records (3), and all community records with new actionable
    Stage 5 remediation findings (3).
  selection: All 9 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, 1 new Cycle 4 kb/communities/*.yaml
    record (000496), 3 Cycle 3 Stage 5 remediated records (000280, 000434, 000448),
    and 3 kb/communities/*.yaml records (000083, 000357, 000397) surfaced by completeness
    audits.
  coverage: full
  population_size: 18
  reviewed_target_ids:
  - CommunityMech:000083
  - CommunityMech:000273
  - CommunityMech:000280
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000357
  - CommunityMech:000397
  - CommunityMech:000434
  - CommunityMech:000448
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000496
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
- target_id: CommunityMech:000273
  path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  label: CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000280
  path: kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml
  label: CommunityMech:000280 (Pinus armandii Endophytic Biocontrol SynCom)
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
- target_id: CommunityMech:000397
  path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  label: CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen Nitrifying Community)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000434
  path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
  label: CommunityMech:000434 (Acidic Nitrification Minimal Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000448
  path: kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml
  label: CommunityMech:000448 (Soymilk Mixed-Starter Metabolic Division SynCom)
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
- target_id: CommunityMech:000496
  path: kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml
  label: CommunityMech:000496 (Methylomicrobium-Arthrospira Biogas Conversion Coculture)
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
- check_id: chk-linkml-schema-deep-c4s4
  name: LinkML schema validation on 18 deep-audit records
  status: passed
  required: true
  summary: All 16 MicrobialCommunity records and 2 TaxonRecord files validate against
    src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000083
  - CommunityMech:000273
  - CommunityMech:000280
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000357
  - CommunityMech:000397
  - CommunityMech:000434
  - CommunityMech:000448
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000496
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -c 'validate 18 deep-audit records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-deep-c4s4
  name: NetworkIntegrityAuditor check on 18 deep-audit records
  status: passed
  required: true
  summary: All 16/16 MicrobialCommunity deep-audit records pass NetworkIntegrityAuditor
    with 0 warnings.
  target_ids:
  - CommunityMech:000083
  - CommunityMech:000273
  - CommunityMech:000280
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000357
  - CommunityMech:000397
  - CommunityMech:000434
  - CommunityMech:000448
  - CommunityMech:000488
  - CommunityMech:000489
  - CommunityMech:000490
  - CommunityMech:000492
  - CommunityMech:000495
  - CommunityMech:000496
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
  accessed_at: '2026-10-31T19:55:00Z'
  support: supports
  summary: All 481 kb/communities/*.yaml, 9 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records (492 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: scripts/audit_completeness.py
  locator: 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness()
    across all 492 records
  accessed_at: '2026-10-31T19:56:00Z'
  support: supports
  summary: Proportional 100-point review-communities Completeness Score audit across
    all 490 MicrobialCommunity records (min 40, median 90, mean 90.97, max 100; CommunityMech:000083
    = 80/100, CommunityMech:000357 = 90/100, CommunityMech:000397 = 85/100) and 2
    TaxonRecord files (100/100) confirmed 100% core metadata presence and 100% top-level
    environment_term coverage (490/490), while scripts/audit_completeness.py:calculate_completeness()
    (which requires every taxon to have functional_role for its 50-point required
    block) scores 000083 at 25/100, 000357 at 35/100, and 000397 at 15/100.
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-10-31T19:57:00Z'
  support: supports
  summary: NetworkIntegrityAuditor across 481 kb/communities and 9 data/isolates records
    found 465/481 communities and 9/9 isolates with 0 warnings (including all 16/16
    MicrobialCommunity records in the 18-record deep audit) and 16 community records
    with 44 non-fatal warnings (42 DISCONNECTED across 15 records and 2 COMMUNITY_LEVEL
    UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0
    error-severity issues, 0 broken downstream references).
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-491
  accessed_at: '2026-10-31T19:57:30Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 490 MicrobialCommunity records
    with 100% SHA-256 attestation in verify_causal_graph_reviews.py (0 unreviewed
    records).
- evidence_id: ev-common-taxon-linkage-audit
  kind: record_content
  reference: kb/taxa/Geobacter_sulfurreducens.yaml
  locator: TaxonomicComposition.common_taxon cross-references across kb/communities/*.yaml
  accessed_at: '2026-10-31T19:58:00Z'
  support: supports
  summary: Corpus-wide audit of reusable taxon cross-references confirmed 6/6 Geobacter
    sulfurreducens communities linked to CommunityMech:taxon:000002 (4 UniProt EET
    genes) and 9/9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001
    (5 UniProt EET genes) with Cycle 4 Stage 3 inline gene expansion (#2091).
- evidence_id: ev-smutans-calbicans-pmid24566629
  kind: primary_source
  reference: PMID:24566629
  locator: kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
  accessed_at: '2026-10-31T19:58:30Z'
  support: supports
  summary: PMID:24566629 establishes that Streptococcus mutans and Candida albicans
    are the two co-species cariogenic biofilm members under 1% (30 mM) sucrose availability
    in UFYTE broth at 37 °C under 5% CO2, with C. albicans augmenting exopolysaccharide
    (EPS, CHEBI:72813) accumulation and viable S. mutans carriage while fungal mannan
    and beta-1,3-glucan provide sites for S. mutans GtfB binding and activity.
  quote: The presence of C. albicans augments the production of exopolysaccharides
    (EPS), such that cospecies biofilms accrue more biomass and harbor more viable
    S. mutans cells than single-species biofilms.
- evidence_id: ev-ecoli-gl10-xl12-pmid42038008
  kind: primary_source
  reference: PMID:42038008
  locator: kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
  accessed_at: '2026-10-31T19:59:00Z'
  support: supports
  summary: PMID:42038008 (doi:10.1016/j.bidere.2026.100072) establishes that glucose-specialized
    E. coli GL10 and xylose-utilizing E. coli XL12 act as the two division-of-labor
    sugar-degrading consortium members co-fermenting 5 g/L glucose and 5 g/L xylose
    in M9 medium at 37 °C to optically pure D-lactate (3.76 g/L at a 1:1 GL10:XL12
    inoculation ratio and 4.53 g/L at a 1:5 ratio).
  quote: Two division-of-labor engineered E. coli strains, XL12 and GL10, were constructed
    and characterized in terms of sugar utilization and D-lactate synthesis capabilities.
- evidence_id: ev-nitrifying-syncom-pmid42668143
  kind: primary_source
  reference: PMID:42668143
  locator: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  accessed_at: '2026-10-31T19:59:20Z'
  support: supports
  summary: PMID:42668143 (doi:10.1093/bbb/zbag131) establishes that Bacillus badius
    NBRC 15713 (NCBITaxon:1455, Pseudobacillus badius), Nitrosomonas europaea NBRC
    14298 (NCBITaxon:915), and Nitrobacter winogradskyi NBRC 14297 (NCBITaxon:913)
    form a defined three-strain nitrifying microbial community performing sequential
    ammonification and nitrification under selected organic nitrogen conditions.
  quote: 'A simplified synthetic nitrifying microbial community capable of sequential
    ammonification and nitrification under organic conditions was constructed using
    three defined strains: Bacillus badius NBRC 15713, Nitrosomonas europaea NBRC
    14298, and Nitrobacter winogradskyi NBRC 14297.'
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 49 retained structured review bundles through 20261031T081500Z-c3s5-remediation-verification
  accessed_at: '2026-10-31T19:59:45Z'
  support: context_only
  summary: 'Lineage inspection of all 49 prior structured reviews and Cycle 3 Stage
    5 evidence.yaml confirmed that all 3 Cycle 3 Stage 4 open findings across CommunityMech:000280,
    000434, and 000448 were resolved in Cycle 3 Stage 5 (#2084, PR #2085) and 7 record-scoped
    source-limited findings remain deferred at commit 0b03bdf7f9250e686bb9d0be5d3b99b71d1a0795.'
assessments:
- assessment_id: assess-communitymech-000083
  area: completeness
  topic: Deep per-record audit of CommunityMech:000083 (Streptococcus mutans - Candida
    albicans ECC Biofilm Model)
  outcome: concern
  summary: Record CommunityMech:000083 (kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml)
    in cohort ORAL has Completeness Score 80/100, 2 taxa, 3 interactions, 2 causal
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
    value: 80.0
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
- assessment_id: assess-communitymech-000280
  area: completeness
  topic: Deep per-record audit of CommunityMech:000280 (Pinus armandii Endophytic
    Biocontrol SynCom)
  outcome: supported
  summary: Record CommunityMech:000280 (kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml)
    in cohort RHIZOSPHERE has Completeness Score 77/100, 5 taxa, 4 interactions, 0
    causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0 network
    warnings.
  target_ids:
  - CommunityMech:000280
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 77.0
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
  outcome: concern
  summary: Record CommunityMech:000357 (kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 90/100, 2 taxa, 1 interactions,
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
    value: 90.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000397
  area: completeness
  topic: Deep per-record audit of CommunityMech:000397 (Defined Three-Strain Organic-Nitrogen
    Nitrifying Community)
  outcome: concern
  summary: Record CommunityMech:000397 (kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 85/100, 3 taxa, 1 interactions,
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
    value: 85.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000434
  area: completeness
  topic: Deep per-record audit of CommunityMech:000434 (Acidic Nitrification Minimal
    Consortium)
  outcome: supported
  summary: Record CommunityMech:000434 (kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 80/100, 2 taxa, 1 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000434
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-common-taxon-linkage-audit
  metrics:
  - name: completeness_score
    value: 80.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000448
  area: completeness
  topic: Deep per-record audit of CommunityMech:000448 (Soymilk Mixed-Starter Metabolic
    Division SynCom)
  outcome: supported
  summary: Record CommunityMech:000448 (kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 83/100, 3 taxa, 2 interactions,
    0 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000448
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
- assessment_id: assess-communitymech-000496
  area: completeness
  topic: Deep per-record audit of CommunityMech:000496 (Methylomicrobium-Arthrospira
    Biogas Conversion Coculture)
  outcome: supported
  summary: Record CommunityMech:000496 (kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 100/100, 2 taxa, 4 interactions,
    3 causal edges, 0 inline gene annotations, 0 reusable CommonTaxon links, and 0
    network warnings.
  target_ids:
  - CommunityMech:000496
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
- finding_id: c4s4-000083-smutans-calbicans-roles-metabolites-and-sucrose
  issue_key: communitymech-c4s4-000083-smutans-calbicans-roles-metabolites-and-sucrose
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Streptococcus mutans-Candida albicans ECC Biofilm (CommunityMech:000083)
    omits source-backed functional_role and DOMINANT/ABUNDANT abundance_level on both
    co-species biofilm members, exopolysaccharide (CHEBI:72813) on ecological_interactions[1],
    and environmental_factors for 1% sucrose availability
  description: 'CommunityMech:000083 (kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml,
    proportional Completeness Score 80/100; scripts/audit_completeness.py score 25/100)
    models the cariogenic plaque biofilm co-infection of Streptococcus mutans UA159
    (NCBITaxon:1309) and Candida albicans SC5314 (NCBITaxon:5476) in early childhood
    caries (PMID:24566629). In taxonomy, Streptococcus mutans omits functional_role:
    [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: DOMINANT, and Candida albicans
    omits functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level:
    ABUNDANT, despite verbatim support in the already-curated PMID:24566629 snippets
    (S. mutans GtfB synthesizes glucan exopolysaccharides from 1% sucrose and binds
    fungal mannan and beta-1,3-glucan sites, while C. albicans augments EPS production
    and viable S. mutans carriage in cospecies biofilms inoculated at ~2 x 10^6 CFU/mL
    S. mutans and ~2 x 10^4 CFU/mL C. albicans). In addition, ecological_interactions[1]
    (''Candida-Driven EPS Amplification of Streptococcus mutans'') omits metabolites
    exopolysaccharide (CHEBI:72813, which is already curated in related_ingredients[0]
    backed by the identical PMID:24566629 snippet), and environmental_factors is absent
    despite growth_media[0].evidence[0] (PMID:24566629) establishing 1% (30 mM) sucrose
    availability in UFYTE broth at 37 °C under 5% CO2.'
  target_ids:
  - CommunityMech:000083
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - taxonomy[1].abundance_level
  - ecological_interactions[1].metabolites
  - environmental_factors
  evidence_ids:
  - ev-completeness-audit
  - ev-smutans-calbicans-pmid24566629
  rule_id: review-communities:completeness-functional-roles-and-metabolites
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing source-backed functional_role, abundance_level,
    interaction metabolites, and environmental_factors on an active two-species biofilm
    record) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
- finding_id: c4s4-000357-ecoli-gl10-xl12-roles-and-abundance
  issue_key: communitymech-c4s4-000357-ecoli-gl10-xl12-roles-and-abundance
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: E. coli GL10-XL12 D-Lactate Mixed-Sugar SynCom (CommunityMech:000357) omits
    PRIMARY_DEGRADER functional_role and DOMINANT abundance_level on both engineered
    specialist strains
  description: 'CommunityMech:000357 (kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml,
    proportional Completeness Score 90/100; scripts/audit_completeness.py score 35/100)
    models the two-strain division-of-labor consortium of glucose-specialized Escherichia
    coli GL10 and xylose-utilizing Escherichia coli XL12 (NCBITaxon:562) for mixed
    glucose/xylose co-fermentation to optically pure D-lactate in M9 medium containing
    5 g/L glucose and 5 g/L xylose (PMID:42038008, doi:10.1016/j.bidere.2026.100072).
    Both taxonomy entries omit functional_role: [PRIMARY_DEGRADER] and abundance_level:
    DOMINANT despite verbatim support in the already-curated PMID:42038008 snippets
    (''Two division-of-labor engineered E. coli strains, XL12 and GL10, were constructed
    and characterized in terms of sugar utilization and D-lactate synthesis capabilities.''
    and ''The initial OD600 was adjust to 0.2, with the inoculation ratio of GL10
    and XL12 was 1:1.'').'
  target_ids:
  - CommunityMech:000357
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-ecoli-gl10-xl12-pmid42038008
  rule_id: review-communities:completeness-functional-roles-and-abundance
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing PRIMARY_DEGRADER functional_role
    and DOMINANT abundance_level on both engineered specialist strains in a two-member
    fermentation consortium) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
- finding_id: c4s4-000397-nitrifying-syncom-roles-and-abundance
  issue_key: communitymech-c4s4-000397-nitrifying-syncom-roles-and-abundance
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Defined Three-Strain Organic-Nitrogen Nitrifying Community (CommunityMech:000397)
    omits functional_role and ABUNDANT abundance_level across all three synthetic
    consortium members
  description: 'CommunityMech:000397 (kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml,
    proportional Completeness Score 85/100; scripts/audit_completeness.py score 15/100)
    models the defined three-species nitrifying consortium of Bacillus badius NBRC
    15713 (NCBITaxon:1455, Pseudobacillus badius), Nitrosomonas europaea NBRC 14298
    (NCBITaxon:915), and Nitrobacter winogradskyi NBRC 14297 (NCBITaxon:913) under
    selected organic nitrogen conditions (PMID:42668143, doi:10.1093/bbb/zbag131).
    In taxonomy, ammonifying heterotroph Bacillus badius NBRC 15713 omits functional_role:
    [PRIMARY_DEGRADER] and abundance_level: ABUNDANT, chemolithoautotrophic ammonia
    oxidizer Nitrosomonas europaea NBRC 14298 omits functional_role: [PRIMARY_PRODUCER,
    CROSS_FEEDER] and abundance_level: ABUNDANT, and chemolithoautotrophic nitrite
    oxidizer Nitrobacter winogradskyi NBRC 14297 omits functional_role: [PRIMARY_PRODUCER,
    CROSS_FEEDER] and abundance_level: ABUNDANT despite verbatim support in the already-curated
    PMID:42668143 snippets for sequential ammonification and nitrification by the
    three defined strains.'
  target_ids:
  - CommunityMech:000397
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - taxonomy[1].abundance_level
  - taxonomy[2].functional_role
  - taxonomy[2].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-nitrifying-syncom-pmid42668143
  rule_id: review-communities:completeness-functional-roles-and-abundance
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing source-backed functional_role and
    abundance_level across all three defined nitrifying consortium strains) maps to
    major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
actions:
- action_id: act-populate-smutans-calbicans-roles-metabolites-and-sucrose
  description: 'Add functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level:
    DOMINANT to Streptococcus mutans, add functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]
    and abundance_level: ABUNDANT to Candida albicans, add metabolites exopolysaccharide
    (CHEBI:72813) to ecological_interactions[1] (''Candida-Driven EPS Amplification
    of Streptococcus mutans''), add environmental_factors for 1% (30 mM) sucrose availability
    backed by PMID:24566629 on CommunityMech:000083, and append curation_history.'
  finding_ids:
  - c4s4-000083-smutans-calbicans-roles-metabolites-and-sucrose
  target_ids:
  - CommunityMech:000083
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-populate-ecoli-gl10-xl12-roles-and-abundance
  description: 'Add functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT
    to Escherichia coli GL10 and Escherichia coli XL12 backed by PMID:42038008 (doi:10.1016/j.bidere.2026.100072)
    on CommunityMech:000357, and append curation_history.'
  finding_ids:
  - c4s4-000357-ecoli-gl10-xl12-roles-and-abundance
  target_ids:
  - CommunityMech:000357
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-populate-nitrifying-syncom-roles-and-abundance
  description: 'Add functional_role: [PRIMARY_DEGRADER] and abundance_level: ABUNDANT
    to Bacillus badius NBRC 15713 (NCBITaxon:1455, Pseudobacillus badius), add functional_role:
    [PRIMARY_PRODUCER, CROSS_FEEDER] and abundance_level: ABUNDANT to Nitrosomonas
    europaea NBRC 14298 and Nitrobacter winogradskyi NBRC 14297 backed by PMID:42668143
    (doi:10.1093/bbb/zbag131) on CommunityMech:000397, and append curation_history.'
  finding_ids:
  - c4s4-000397-nitrifying-syncom-roles-and-abundance
  target_ids:
  - CommunityMech:000397
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  - uv run python scripts/verify_history_Changed_records.py
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used
  cached PubMed/DOI abstracts and open-access PMC full texts in references_cache/.
tags:
- cycle4
- stage4
- record-review
- deep-audit
```
