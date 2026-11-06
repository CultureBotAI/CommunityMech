# Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, and Actionable Community Records

- Review: 20261021T101000Z-stage4-record-deep-audit
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T09:50:00Z
- Finished UTC: 2026-10-21T10:10:00Z
- Reviewer: antigravity-stage4-record-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Deep per-record scientific and structural audit of 16 records (all 4 data/isolates/*.yaml records, both kb/taxa/*.yaml reusable taxon records, and 10 kb/communities/*.yaml records with actionable completeness, participant-connectivity, or host/pathogen boundary defects) at frozen Git revision 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.

## Scope And Provenance

Focused per-record deep audit of all isolate baselines (4), all reusable taxon records (2), and all community records with actionable Stage 5 remediation findings (10).

Selection: All 4 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, and 10 kb/communities/*.yaml records surfaced by completeness and network-integrity gates.
Coverage: full; 16 reviewed / 16 in the declared population.
Source: git_commit at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | CommunityMech:000322 (Methylobacterium REE E-waste Platform) |
| CommunityMech:000339 | kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml | maintained | CommunityMech:000339 (Space Habitat Seven-Member Stress-Tolerance SynCom) |
| CommunityMech:000347 | kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml | maintained | CommunityMech:000347 (Bacillus siamensis-vallismortis HT Masson Pine SynCom) |
| CommunityMech:000360 | kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml | maintained | CommunityMech:000360 (Wolffia Mankai Endosphere Cobamide Guild) |
| CommunityMech:000364 | kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml | maintained | CommunityMech:000364 (Sclerotinia Sclerotia 12-Strain Biocontrol SynCom) |
| CommunityMech:000373 | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml | maintained | CommunityMech:000373 (Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom) |
| CommunityMech:000399 | kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml | maintained | CommunityMech:000399 (Pseudomonas aeruginosa Eight-Strain Full-Factorial SynCom) |
| CommunityMech:000415 | kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml | maintained | CommunityMech:000415 (Algal-Methanotroph Biogas Valorization Coculture) |
| CommunityMech:000433 | kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml | maintained | CommunityMech:000433 (Nitrifying Wastewater Ammonia-Oxidizing Consortium) |
| CommunityMech:000434 | kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml | maintained | CommunityMech:000434 (Acidic Nitrification Minimal Consortium) |
| CommunityMech:000447 | kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml | maintained | CommunityMech:000447 (Brocadia Low-Nitrogen Anammox Consortium) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (Geobacter_sulfurreducens) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on deep-audit records | passed | True | CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000339, CommunityMech:000347, CommunityMech:000360, CommunityMech:000364, CommunityMech:000373, CommunityMech:000399, CommunityMech:000415, CommunityMech:000433, CommunityMech:000434, CommunityMech:000447, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 14 MicrobialCommunity records and 2 TaxonRecord files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| NetworkIntegrityAuditor check on deep-audit records | passed | True | CommunityMech:000273, CommunityMech:000320, CommunityMech:000321, CommunityMech:000322, CommunityMech:000339, CommunityMech:000347, CommunityMech:000360, CommunityMech:000364, CommunityMech:000373, CommunityMech:000399, CommunityMech:000415, CommunityMech:000433, CommunityMech:000434, CommunityMech:000447, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | Identified 14 DISCONNECTED_TAXON warnings across 5 SynCom/guild records and 7 UNKNOWN_TARGET warnings across 3 biocontrol records; 0 broken causal edges. |

## Scientific And Domain Assessments

### Deep per-record audit of CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)

evidence: concern. Targets: CommunityMech:000273.

Record CommunityMech:000273 (data/isolates/Chromobacterium_Gold_Biocyanidation.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 87/100, 1 taxa, 4 interactions, 2 causal edges, and 0 network warnings.

### Deep per-record audit of CommunityMech:000320 (Aspergillus Indium LCD Recovery Platform)

completeness: supported. Targets: CommunityMech:000320.

Record CommunityMech:000320 (data/isolates/Aspergillus_Indium_LED_Recovery.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 86/100, 1 taxa, 5 interactions, 4 causal edges, and 0 network warnings.

### Deep per-record audit of CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model)

completeness: concern. Targets: CommunityMech:000321.

Record CommunityMech:000321 (data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml) in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 80/100, 1 taxa, 1 interactions, 0 causal edges, and 0 network warnings.

### Deep per-record audit of CommunityMech:000322 (Methylobacterium REE E-waste Platform)

completeness: supported. Targets: CommunityMech:000322.

Record CommunityMech:000322 (data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml) in cohort ISOLATES:BIOMINING has Completeness Score 89/100, 1 taxa, 4 interactions, 2 causal edges, and 0 network warnings.

### Deep per-record audit of CommunityMech:000339 (Space Habitat Seven-Member Stress-Tolerance SynCom)

completeness: concern. Targets: CommunityMech:000339.

Record CommunityMech:000339 (kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml) in cohort EXTREME_ENVIRONMENT has Completeness Score 75/100, 7 taxa, 1 interactions, 0 causal edges, and 6 network warnings.

### Deep per-record audit of CommunityMech:000347 (Bacillus siamensis-vallismortis HT Masson Pine SynCom)

completeness: concern. Targets: CommunityMech:000347.

Record CommunityMech:000347 (kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml) in cohort RHIZOSPHERE has Completeness Score 83/100, 2 taxa, 3 interactions, 0 causal edges, and 3 network warnings.

### Deep per-record audit of CommunityMech:000360 (Wolffia Mankai Endosphere Cobamide Guild)

completeness: concern. Targets: CommunityMech:000360.

Record CommunityMech:000360 (kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml) in cohort OTHER has Completeness Score 75/100, 7 taxa, 2 interactions, 0 causal edges, and 0 network warnings.

### Deep per-record audit of CommunityMech:000364 (Sclerotinia Sclerotia 12-Strain Biocontrol SynCom)

completeness: concern. Targets: CommunityMech:000364.

Record CommunityMech:000364 (kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml) in cohort OTHER has Completeness Score 85/100, 12 taxa, 3 interactions, 1 causal edges, and 2 network warnings.

### Deep per-record audit of CommunityMech:000373 (Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom)

completeness: concern. Targets: CommunityMech:000373.

Record CommunityMech:000373 (kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml) in cohort RHIZOSPHERE has Completeness Score 89/100, 3 taxa, 5 interactions, 0 causal edges, and 2 network warnings.

### Deep per-record audit of CommunityMech:000399 (Pseudomonas aeruginosa Eight-Strain Full-Factorial SynCom)

completeness: concern. Targets: CommunityMech:000399.

Record CommunityMech:000399 (kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml) in cohort BIOTECHNOLOGY has Completeness Score 75/100, 8 taxa, 1 interactions, 0 causal edges, and 5 network warnings.

### Deep per-record audit of CommunityMech:000415 (Algal-Methanotroph Biogas Valorization Coculture)

completeness: concern. Targets: CommunityMech:000415.

Record CommunityMech:000415 (kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml) in cohort BIOTECHNOLOGY has Completeness Score 90/100, 6 taxa, 2 interactions, 0 causal edges, and 1 network warnings.

### Deep per-record audit of CommunityMech:000433 (Nitrifying Wastewater Ammonia-Oxidizing Consortium)

completeness: concern. Targets: CommunityMech:000433.

Record CommunityMech:000433 (kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml) in cohort BIOTECHNOLOGY has Completeness Score 75/100, 3 taxa, 1 interactions, 0 causal edges, and 1 network warnings.

### Deep per-record audit of CommunityMech:000434 (Acidic Nitrification Minimal Consortium)

completeness: concern. Targets: CommunityMech:000434.

Record CommunityMech:000434 (kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml) in cohort BIOTECHNOLOGY has Completeness Score 70/100, 2 taxa, 1 interactions, 0 causal edges, and 0 network warnings.

### Deep per-record audit of CommunityMech:000447 (Brocadia Low-Nitrogen Anammox Consortium)

completeness: concern. Targets: CommunityMech:000447.

Record CommunityMech:000447 (kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml) in cohort BIOTECHNOLOGY has Completeness Score 85/100, 2 taxa, 1 interactions, 0 causal edges, and 1 network warnings.

### Deep per-record audit of CommunityMech:taxon:000001 (Shewanella_oneidensis_MR1)

completeness: supported. Targets: CommunityMech:taxon:000001.

Record CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, and 0 network warnings.

### Deep per-record audit of CommunityMech:taxon:000002 (Geobacter_sulfurreducens)

completeness: supported. Targets: CommunityMech:taxon:000002.

Record CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) in cohort TAXA has Completeness Score 100/100, 1 taxa, 0 interactions, 0 causal edges, and 0 network warnings.

## Findings

### stage4-missing-community-origin-000434: CommunityMech:000434 omits community_origin despite acidic nitrification bioreactor operation in PMID:42762737

major / open / confirmed; issue key: communitymech-stage4-000434-missing-origin.

Acidic_Nitrification_Minimal_Consortium.yaml (CommunityMech:000434) is the only MicrobialCommunity record in the 477-community corpus missing community_origin. The cited abstract (PMID:42762737) describes three acidic nitrification bioreactors operated between pH 2.0 and 5.0 where the pH 2.0 bioreactor hosts a simplified consortium dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species, supporting community_origin: ENGINEERED.

### stage4-missing-ecological-state-000360: CommunityMech:000360 omits ecological_state despite persistent host-filtered endosphere guild maintenance in PMID:42304541

major / open / confirmed; issue key: communitymech-stage4-000360-missing-state.

Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml (CommunityMech:000360) is the only MicrobialCommunity record in the 477-community corpus missing ecological_state. The cited source (PMID:42304541) describes a persistent host-filtered endosphere cobamide-producing guild assembled and maintained in a stable host-mediated niche, supporting ecological_state: STABLE.

### stage4-disconnected-syncom-participants: Five SynCom/consortium records omit co-tested member taxa from COMMUNITY_LEVEL participating_taxa

minor / open / confirmed; issue key: communitymech-stage4-disconnected-syncom-participants.

NetworkIntegrityAuditor flags 14 DISCONNECTED_TAXON warnings across five records (CommunityMech:000339 Space_Habitat_SevenMember_Stress_Tolerance_SynCom [6 disconnected taxa: Sphingomonas paucimobilis, Cupriavidus metallidurans, Ralstonia pickettii, Acinetobacter radioresistens, Burkholderia cepacia, Chryseobacterium gleum], CommunityMech:000399 Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom [5 disconnected strains: H27, F2, F3, W6, M15], CommunityMech:000415 Algal_Methanotroph_Biogas_Valorization_Coculture [1 disconnected cyanobacterial primary producer: Leptolyngbya, NCBITaxon:47251], CommunityMech:000433 Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium [1 disconnected taxon: Legionella MAGs, NCBITaxon:445], and CommunityMech:000447 Brocadia_Low_Nitrogen_Anammox_Consortium [1 disconnected taxon: Candidatus Kuenenia early-acclimation lineage, NCBITaxon:174636]) where COMMUNITY_LEVEL ecological_interactions list only a subset of participating_taxa.

### stage4-external-host-pathogen-targets: Three biocontrol/rhizosphere SynCom records place external non-member hosts or pathogens in target_taxon

minor / open / confirmed; issue key: communitymech-stage4-external-host-pathogen-targets.

NetworkIntegrityAuditor flags all 7 UNKNOWN_TARGET warnings in the corpus across three records (CommunityMech:000347 Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom [3 warnings: Fusarium oxysporum on 1 interaction and Pinus massoniana on 2 interactions], CommunityMech:000364 Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom [2 warnings: Sclerotinia sclerotiorum on 2 interactions], and CommunityMech:000373 Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom [2 warnings: Nicotiana tabacum (tobacco, NCBITaxon:4097) on 2 interactions]) because external host plants and target phytopathogens outside taxonomy[] are modeled in target_taxon on COMMUNITY_LEVEL interactions.

### stage4-isolate-000273-unverified-ore-prose: CommunityMech:000273 retains unverified arsenopyrite ore recovery claims and un-evidenced environmental_factors

major / open / confirmed; issue key: communitymech-stage4-000273-unverified-ore-prose.

Although Stage 2 repaired ecological_interactions on data/isolates/Chromobacterium_Gold_Biocyanidation.yaml (CommunityMech:000273), its top-level description, environment_term.notes, taxonomy[0].taxon_term.notes, and 8 un-evidenced environmental_factors entries (7 ore/cyanide/pulp-density parameters and 1 temperature entry) still assert refractory gold-bearing sulfide ore (arsenopyrite/pyrite) bioleaching, 70-85% gold recovery, 50-200 ppm CN-, and 7-14 day leaching time that do not come from the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4: Acidithiobacillus ferrooxidans pretreatment removing &gt;80% Cu followed by Chromobacterium violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct bioleaching).

### stage4-isolate-000321-missing-functional-role: CommunityMech:000321 omits functional_role and abundance_level on its sole taxon entry

minor / open / confirmed; issue key: communitymech-stage4-000321-missing-role.

data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml (CommunityMech:000321) is the only record in data/isolates/ missing functional_role and abundance_level on taxonomy[0] (Rothia, NCBITaxon:32207, supported by PMID:33398099 and PMID:28963201), reducing its proportional Completeness Score to 80/100.

## Recommended Actions And Acceptance Checks

### act-set-community-origin-000434

Set community_origin: ENGINEERED on CommunityMech:000434 (Acidic_Nitrification_Minimal_Consortium.yaml) and append a curation_history entry.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-set-ecological-state-000360

Set ecological_state: STABLE on CommunityMech:000360 (Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml) and append a curation_history entry.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-connect-syncom-participants

Populate full abstract-backed participating_taxa on COMMUNITY_LEVEL ecological_interactions in CommunityMech:000339, 000399, 000415, 000433, and 000447.

- just audit-network
- uv run python scripts/verify_history_Changed_records.py

### act-remove-external-host-pathogen-targets

Replace external non-member host/pathogen target_taxon entries on COMMUNITY_LEVEL interactions in CommunityMech:000347, 000364, and 000373 with member participating_taxa while preserving host/pathogen context in interaction name/description.

- just audit-network
- uv run python scripts/verify_history_Changed_records.py

### act-reconcile-isolate-000273-prose

Align description, environment_term.notes, taxonomy[0].taxon_term.notes, and environmental_factors in data/isolates/Chromobacterium_Gold_Biocyanidation.yaml (CommunityMech:000273) strictly to the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4).

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-populate-isolate-000321-role

Populate functional_role and abundance_level on taxonomy[0] in data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml (CommunityMech:000321) supported by PMID:33398099 and PMID:28963201.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
- uv run python scripts/verify_history_Changed_records.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and TaxonRecord classes | supports | All 473 kb/communities/*.yaml, 4 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | .claude/skills/review-communities/SKILL.md; Section 5: Completeness Score (0-100) and Validation Quality Score (0-100) | supports | Proportional Completeness Score audit across all 477 MicrobialCommunity records (min 40, median 90, mean 85.06, max 100) identified 2 core metadata omissions (CommunityMech:000434 missing community_origin; CommunityMech:000360 missing ecological_state) and 1 isolate missing functional_role (CommunityMech:000321, Completeness Score 80/100). |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | Network integrity audit across 473 kb/communities records found 452 records with 0 warnings and 21 records with 57 warnings (50 DISCONNECTED_TAXON, 7 UNKNOWN_TARGET across 44 issue categories), of which 5 SynCom/guild records have 14 remediable disconnected member taxa and 3 biocontrol records place external hosts/pathogens in target_taxon across 7 interaction entries. |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-478 | supports | Corpus-wide causal graph inventory covers all 477 MicrobialCommunity records (423 reviewed with evidence-backed causal structure, 54 needs_research source-limited, 0 unreviewed). |
| ev-000434-pmid42762737 | PMID:42762737; references_cache/PMID_42762737.txt | supports | Cached PubMed abstract PMID:42762737 describes operating acidic nitrification bioreactors between pH 2.0 and 5.0, with the pH 2.0 bioreactor hosting a strongly simplified community dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species. |
| ev-000360-pmid42304541 | PMID:42304541; references_cache/PMID_42304541.txt | supports | Cached PubMed abstract PMID:42304541 describes a persistent host-filtered endosphere cobamide-producing bacterial guild assembled and maintained in a stable host-mediated niche within Wolffia globosa Mankai. |
| ev-isolate-000273-audit | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml; description, environment_term.notes, taxonomy[0].taxon_term.notes, environmental_factors | refutes | Non-graph prose and 8 un-evidenced environmental_factors (7 ore/cyanide/pulp-density parameters and 1 temperature entry) in CommunityMech:000273 still claim refractory arsenopyrite ore bioleaching (70-85% Au recovery, 50-200 ppm CN-, 7-14 days) rather than the two-step waste-PCB bioleaching reported by doi:10.1007/s10163-014-0276-4 (Acidithiobacillus ferrooxidans pretreatment removing &gt;80% Cu followed by Chromobacterium violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct bioleaching). |
| ev-isolate-000321-audit | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; taxonomy[0] | supports | CommunityMech:000321 is a valid single-species GSMM baseline record for Rothia (PMID:33398099, PMID:28963201; Completeness Score 80/100) but omits functional_role and abundance_level on taxonomy[0]. |
| ev-prior-structured-reviews | reviews/structured; 40 retained structured review bundles through 20261016T091936Z | context_only | Lineage inspection of all 40 prior structured reviews identified 7 record-scoped source-limited findings that remain unresolved at commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b and are carried forward as deferred. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used cached PubMed/DOI abstracts and open-access metadata in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101000Z-stage4-record-deep-audit
kind: batch
repository: CultureBotAI/CommunityMech
title: Stage 4 Per-Record Deep Audit of Isolates, Reusable Taxa, and Actionable Community
  Records
started_at: '2026-10-21T09:50:00Z'
finished_at: '2026-10-21T10:10:00Z'
reviewer:
  identity: antigravity-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Stage 4 read-only review pass over frozen commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
    without record mutation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (3 P2 major findings, 3 P3 minor findings across 12
  records; 4 isolate/taxon records pass)
scientific_review: true
summary: Deep per-record scientific and structural audit of 16 records (all 4 data/isolates/*.yaml
  records, both kb/taxa/*.yaml reusable taxon records, and 10 kb/communities/*.yaml
  records with actionable completeness, participant-connectivity, or host/pathogen
  boundary defects) at frozen Git revision 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
source:
  git_revision: 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
  state: git_commit
  inputs:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    sha256: c9ebc23ad2748751ae6a42fbc2340c5f7524a7aa38185bcad4602b7e56734d9d
    role: target
  - path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    sha256: b73ac6cd532c8fb20c7d1fa70979b2a220238069f0ce78c7b6c9d66af2524ab8
    role: target
  - path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    sha256: 6f859fe8ba028743e55e8b77565c2ee747df5b436e7d3741728af6e037850fa2
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
    sha256: 376423d5910b761cc88aa6d9afe44204a7c275ed3e8873fef1a56c4def1e19c9
    role: target
  - path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    sha256: 3e009885b98b2aa6b6763fb5386ab60f764367d5436db204e0aede39dc6e3331
    role: target
  - path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    sha256: e0126b602878c9abada427f906334f6a059784e07b29c33b709c9a9549f0689f
    role: target
  - path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    sha256: c0cb1ddb17e22f1fba3db44ecdb5cf8cc8a3412d23be6910a043851f23ce51d6
    role: target
  - path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    sha256: 227362963f3008129281c29d08829d1bf49aa57230b126cc7986e592c6cd9a96
    role: target
  - path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    sha256: 61a0b16fc00db138fa35884e8f9f170bda3b2cc9092008a9d5098b3600ad920a
    role: target
  - path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
    sha256: 5771a8a97beb8ccb19b6cccad32062d896b09747ce0670788686060481cf68b9
    role: target
  - path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
    sha256: b76f915e08d08faf1516698a67c53bb6e25f912bd8d4803dfe55412f1a100a3e
    role: target
  - path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
    sha256: 0304999156eeec1556a337ff0138a6bfce205c38b9d5a8010051d864949a2a7f
    role: target
  - path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
    sha256: 829d29dcebcb9ba30483df9d1ec71eafb945a6a3bf966539ee6a16d9abd9077d
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: 2a17e614d13876fbb4b2e3bed44c3bd8c339eb8602d53f091cabf6beb5d7e6bd
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf
    role: target
  - path: reports/causal_graph_review/inventory.tsv
    sha256: cc95d8ac0dbf12aa50a3afd2a59fae72fbe5df1b89a636296f5b0e97cfe19fd0
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: d38c4ddc359b6987209ce5d12d5af119e6b64da51ee40d568fe4f8d382bcd56c
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Focused per-record deep audit of all isolate baselines (4), all reusable
    taxon records (2), and all community records with actionable Stage 5 remediation
    findings (10).
  selection: All 4 data/isolates/*.yaml, all 2 kb/taxa/*.yaml, and 10 kb/communities/*.yaml
    records surfaced by completeness and network-integrity gates.
  coverage: full
  population_size: 16
  reviewed_target_ids:
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
targets:
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
- target_id: CommunityMech:000339
  path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
  label: CommunityMech:000339 (Space Habitat Seven-Member Stress-Tolerance SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000347
  path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  label: CommunityMech:000347 (Bacillus siamensis-vallismortis HT Masson Pine SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000360
  path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
  label: CommunityMech:000360 (Wolffia Mankai Endosphere Cobamide Guild)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000364
  path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
  label: CommunityMech:000364 (Sclerotinia Sclerotia 12-Strain Biocontrol SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000373
  path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  label: CommunityMech:000373 (Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000399
  path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
  label: CommunityMech:000399 (Pseudomonas aeruginosa Eight-Strain Full-Factorial
    SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000415
  path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  label: CommunityMech:000415 (Algal-Methanotroph Biogas Valorization Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000433
  path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  label: CommunityMech:000433 (Nitrifying Wastewater Ammonia-Oxidizing Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000434
  path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
  label: CommunityMech:000434 (Acidic Nitrification Minimal Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000447
  path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  label: CommunityMech:000447 (Brocadia Low-Nitrogen Anammox Consortium)
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
- check_id: chk-linkml-schema-deep
  name: LinkML schema validation on deep-audit records
  status: passed
  required: true
  summary: All 14 MicrobialCommunity records and 2 TaxonRecord files validate against
    src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/python -c 'validate 16 deep-audit records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-deep
  name: NetworkIntegrityAuditor check on deep-audit records
  status: passed
  required: true
  summary: Identified 14 DISCONNECTED_TAXON warnings across 5 SynCom/guild records
    and 7 UNKNOWN_TARGET warnings across 3 biocontrol records; 0 broken causal edges.
  target_ids:
  - CommunityMech:000273
  - CommunityMech:000320
  - CommunityMech:000321
  - CommunityMech:000322
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
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
  accessed_at: '2026-10-21T10:05:00Z'
  support: supports
  summary: All 473 kb/communities/*.yaml, 4 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: .claude/skills/review-communities/SKILL.md
  locator: 'Section 5: Completeness Score (0-100) and Validation Quality Score (0-100)'
  accessed_at: '2026-10-21T10:06:00Z'
  support: supports
  summary: Proportional Completeness Score audit across all 477 MicrobialCommunity
    records (min 40, median 90, mean 85.06, max 100) identified 2 core metadata omissions
    (CommunityMech:000434 missing community_origin; CommunityMech:000360 missing ecological_state)
    and 1 isolate missing functional_role (CommunityMech:000321, Completeness Score
    80/100).
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-10-21T10:06:30Z'
  support: supports
  summary: Network integrity audit across 473 kb/communities records found 452 records
    with 0 warnings and 21 records with 57 warnings (50 DISCONNECTED_TAXON, 7 UNKNOWN_TARGET
    across 44 issue categories), of which 5 SynCom/guild records have 14 remediable
    disconnected member taxa and 3 biocontrol records place external hosts/pathogens
    in target_taxon across 7 interaction entries.
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-478
  accessed_at: '2026-10-21T10:07:00Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 477 MicrobialCommunity records
    (423 reviewed with evidence-backed causal structure, 54 needs_research source-limited,
    0 unreviewed).
- evidence_id: ev-000434-pmid42762737
  kind: primary_source
  reference: PMID:42762737
  locator: references_cache/PMID_42762737.txt
  accessed_at: '2026-10-21T10:07:30Z'
  support: supports
  summary: Cached PubMed abstract PMID:42762737 describes operating acidic nitrification
    bioreactors between pH 2.0 and 5.0, with the pH 2.0 bioreactor hosting a strongly
    simplified community dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium
    species.
  quote: To address this gap, three acidic nitrification bioreactors were operated
    between pH 2.0 and 5.0. All systems achieved stable ammonia oxidation (34.4-51.8
    mg N L-1 d-1), despite pH 2.0 bioreactor hosting a strongly simplified community
    dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species.
- evidence_id: ev-000360-pmid42304541
  kind: primary_source
  reference: PMID:42304541
  locator: references_cache/PMID_42304541.txt
  accessed_at: '2026-10-21T10:07:45Z'
  support: supports
  summary: Cached PubMed abstract PMID:42304541 describes a persistent host-filtered
    endosphere cobamide-producing bacterial guild assembled and maintained in a stable
    host-mediated niche within Wolffia globosa Mankai.
- evidence_id: ev-isolate-000273-audit
  kind: record_content
  reference: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  locator: description, environment_term.notes, taxonomy[0].taxon_term.notes, environmental_factors
  accessed_at: '2026-10-21T10:08:00Z'
  support: refutes
  summary: Non-graph prose and 8 un-evidenced environmental_factors (7 ore/cyanide/pulp-density
    parameters and 1 temperature entry) in CommunityMech:000273 still claim refractory
    arsenopyrite ore bioleaching (70-85% Au recovery, 50-200 ppm CN-, 7-14 days) rather
    than the two-step waste-PCB bioleaching reported by doi:10.1007/s10163-014-0276-4
    (Acidithiobacillus ferrooxidans pretreatment removing >80% Cu followed by Chromobacterium
    violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct
    bioleaching).
- evidence_id: ev-isolate-000321-audit
  kind: record_content
  reference: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  locator: taxonomy[0]
  accessed_at: '2026-10-21T10:08:15Z'
  support: supports
  summary: CommunityMech:000321 is a valid single-species GSMM baseline record for
    Rothia (PMID:33398099, PMID:28963201; Completeness Score 80/100) but omits functional_role
    and abundance_level on taxonomy[0].
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 40 retained structured review bundles through 20261016T091936Z
  accessed_at: '2026-10-21T10:08:30Z'
  support: context_only
  summary: Lineage inspection of all 40 prior structured reviews identified 7 record-scoped
    source-limited findings that remain unresolved at commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
    and are carried forward as deferred.
assessments:
- assessment_id: assess-communitymech-000273
  area: evidence
  topic: Deep per-record audit of CommunityMech:000273 (Chromobacterium Gold Biocyanidation
    Platform)
  outcome: concern
  summary: Record CommunityMech:000273 (data/isolates/Chromobacterium_Gold_Biocyanidation.yaml)
    in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 87/100, 1 taxa, 4 interactions,
    2 causal edges, and 0 network warnings.
  target_ids:
  - CommunityMech:000273
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 87.0
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
    in cohort ISOLATES:BIOMINING has Completeness Score 86/100, 1 taxa, 5 interactions,
    4 causal edges, and 0 network warnings.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 86.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000321
  area: completeness
  topic: Deep per-record audit of CommunityMech:000321 (BioModels MODEL2204300002
    Kefir Rothia Model)
  outcome: concern
  summary: Record CommunityMech:000321 (data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml)
    in cohort ISOLATES:BIOTECHNOLOGY has Completeness Score 80/100, 1 taxa, 1 interactions,
    0 causal edges, and 0 network warnings.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 80.0
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
    in cohort ISOLATES:BIOMINING has Completeness Score 89/100, 1 taxa, 4 interactions,
    2 causal edges, and 0 network warnings.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 89.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000339
  area: completeness
  topic: Deep per-record audit of CommunityMech:000339 (Space Habitat Seven-Member
    Stress-Tolerance SynCom)
  outcome: concern
  summary: Record CommunityMech:000339 (kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml)
    in cohort EXTREME_ENVIRONMENT has Completeness Score 75/100, 7 taxa, 1 interactions,
    0 causal edges, and 6 network warnings.
  target_ids:
  - CommunityMech:000339
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 75.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000347
  area: completeness
  topic: Deep per-record audit of CommunityMech:000347 (Bacillus siamensis-vallismortis
    HT Masson Pine SynCom)
  outcome: concern
  summary: Record CommunityMech:000347 (kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml)
    in cohort RHIZOSPHERE has Completeness Score 83/100, 2 taxa, 3 interactions, 0
    causal edges, and 3 network warnings.
  target_ids:
  - CommunityMech:000347
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 83.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000360
  area: completeness
  topic: Deep per-record audit of CommunityMech:000360 (Wolffia Mankai Endosphere
    Cobamide Guild)
  outcome: concern
  summary: Record CommunityMech:000360 (kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml)
    in cohort OTHER has Completeness Score 75/100, 7 taxa, 2 interactions, 0 causal
    edges, and 0 network warnings.
  target_ids:
  - CommunityMech:000360
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 75.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000364
  area: completeness
  topic: Deep per-record audit of CommunityMech:000364 (Sclerotinia Sclerotia 12-Strain
    Biocontrol SynCom)
  outcome: concern
  summary: Record CommunityMech:000364 (kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml)
    in cohort OTHER has Completeness Score 85/100, 12 taxa, 3 interactions, 1 causal
    edges, and 2 network warnings.
  target_ids:
  - CommunityMech:000364
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 85.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000373
  area: completeness
  topic: Deep per-record audit of CommunityMech:000373 (Bacillus G12-Y4-X25 Tobacco
    Biocontrol SynCom)
  outcome: concern
  summary: Record CommunityMech:000373 (kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml)
    in cohort RHIZOSPHERE has Completeness Score 89/100, 3 taxa, 5 interactions, 0
    causal edges, and 2 network warnings.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 89.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000399
  area: completeness
  topic: Deep per-record audit of CommunityMech:000399 (Pseudomonas aeruginosa Eight-Strain
    Full-Factorial SynCom)
  outcome: concern
  summary: Record CommunityMech:000399 (kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 75/100, 8 taxa, 1 interactions,
    0 causal edges, and 5 network warnings.
  target_ids:
  - CommunityMech:000399
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 75.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000415
  area: completeness
  topic: Deep per-record audit of CommunityMech:000415 (Algal-Methanotroph Biogas
    Valorization Coculture)
  outcome: concern
  summary: Record CommunityMech:000415 (kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 90/100, 6 taxa, 2 interactions,
    0 causal edges, and 1 network warnings.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 90.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000433
  area: completeness
  topic: Deep per-record audit of CommunityMech:000433 (Nitrifying Wastewater Ammonia-Oxidizing
    Consortium)
  outcome: concern
  summary: Record CommunityMech:000433 (kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 75/100, 3 taxa, 1 interactions,
    0 causal edges, and 1 network warnings.
  target_ids:
  - CommunityMech:000433
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 75.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000434
  area: completeness
  topic: Deep per-record audit of CommunityMech:000434 (Acidic Nitrification Minimal
    Consortium)
  outcome: concern
  summary: Record CommunityMech:000434 (kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 70/100, 2 taxa, 1 interactions,
    0 causal edges, and 0 network warnings.
  target_ids:
  - CommunityMech:000434
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 70.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-communitymech-000447
  area: completeness
  topic: Deep per-record audit of CommunityMech:000447 (Brocadia Low-Nitrogen Anammox
    Consortium)
  outcome: concern
  summary: Record CommunityMech:000447 (kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml)
    in cohort BIOTECHNOLOGY has Completeness Score 85/100, 2 taxa, 1 interactions,
    0 causal edges, and 1 network warnings.
  target_ids:
  - CommunityMech:000447
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 85.0
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
    edges, and 0 network warnings.
  target_ids:
  - CommunityMech:taxon:000001
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
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
    edges, and 0 network warnings.
  target_ids:
  - CommunityMech:taxon:000002
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  metrics:
  - name: completeness_score
    value: 100.0
    unit: points
    definition: Proportional review-communities Completeness Score (0-100).
    minimum: 0.0
    maximum: 100.0
findings:
- finding_id: stage4-missing-community-origin-000434
  issue_key: communitymech-stage4-000434-missing-origin
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: CommunityMech:000434 omits community_origin despite acidic nitrification
    bioreactor operation in PMID:42762737
  description: 'Acidic_Nitrification_Minimal_Consortium.yaml (CommunityMech:000434)
    is the only MicrobialCommunity record in the 477-community corpus missing community_origin.
    The cited abstract (PMID:42762737) describes three acidic nitrification bioreactors
    operated between pH 2.0 and 5.0 where the pH 2.0 bioreactor hosts a simplified
    consortium dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species,
    supporting community_origin: ENGINEERED.'
  target_ids:
  - CommunityMech:000434
  field_paths:
  - community_origin
  evidence_ids:
  - ev-completeness-audit
  - ev-000434-pmid42762737
  rule_id: review-communities:completeness-core-metadata
  native_severity: P2
  normalization_reason: CommunityMech P2 (record-completeness metadata omission with
    direct primary-source resolution) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    role: canonical_record
  tags:
  - completeness
  - metadata
  - stage5-remediation
- finding_id: stage4-missing-ecological-state-000360
  issue_key: communitymech-stage4-000360-missing-state
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: CommunityMech:000360 omits ecological_state despite persistent host-filtered
    endosphere guild maintenance in PMID:42304541
  description: 'Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml (CommunityMech:000360)
    is the only MicrobialCommunity record in the 477-community corpus missing ecological_state.
    The cited source (PMID:42304541) describes a persistent host-filtered endosphere
    cobamide-producing guild assembled and maintained in a stable host-mediated niche,
    supporting ecological_state: STABLE.'
  target_ids:
  - CommunityMech:000360
  field_paths:
  - ecological_state
  evidence_ids:
  - ev-completeness-audit
  - ev-000360-pmid42304541
  rule_id: review-communities:completeness-core-metadata
  native_severity: P2
  normalization_reason: CommunityMech P2 (record-completeness metadata omission with
    direct primary-source resolution) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
    role: canonical_record
  tags:
  - completeness
  - metadata
  - stage5-remediation
- finding_id: stage4-disconnected-syncom-participants
  issue_key: communitymech-stage4-disconnected-syncom-participants
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Five SynCom/consortium records omit co-tested member taxa from COMMUNITY_LEVEL
    participating_taxa
  description: 'NetworkIntegrityAuditor flags 14 DISCONNECTED_TAXON warnings across
    five records (CommunityMech:000339 Space_Habitat_SevenMember_Stress_Tolerance_SynCom
    [6 disconnected taxa: Sphingomonas paucimobilis, Cupriavidus metallidurans, Ralstonia
    pickettii, Acinetobacter radioresistens, Burkholderia cepacia, Chryseobacterium
    gleum], CommunityMech:000399 Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom
    [5 disconnected strains: H27, F2, F3, W6, M15], CommunityMech:000415 Algal_Methanotroph_Biogas_Valorization_Coculture
    [1 disconnected cyanobacterial primary producer: Leptolyngbya, NCBITaxon:47251],
    CommunityMech:000433 Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium [1 disconnected
    taxon: Legionella MAGs, NCBITaxon:445], and CommunityMech:000447 Brocadia_Low_Nitrogen_Anammox_Consortium
    [1 disconnected taxon: Candidatus Kuenenia early-acclimation lineage, NCBITaxon:174636])
    where COMMUNITY_LEVEL ecological_interactions list only a subset of participating_taxa.'
  target_ids:
  - CommunityMech:000339
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000447
  field_paths:
  - ecological_interactions[].participating_taxa
  evidence_ids:
  - ev-network-integrity-audit
  rule_id: review-communities:network-integrity-disconnected-taxon
  native_severity: P3
  normalization_reason: CommunityMech P3 (network-integrity participant list completeness
    on COMMUNITY_LEVEL nodes) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    role: canonical_record
  tags:
  - graph
  - participating_taxa
  - stage5-remediation
- finding_id: stage4-external-host-pathogen-targets
  issue_key: communitymech-stage4-external-host-pathogen-targets
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Three biocontrol/rhizosphere SynCom records place external non-member hosts
    or pathogens in target_taxon
  description: 'NetworkIntegrityAuditor flags all 7 UNKNOWN_TARGET warnings in the
    corpus across three records (CommunityMech:000347 Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom
    [3 warnings: Fusarium oxysporum on 1 interaction and Pinus massoniana on 2 interactions],
    CommunityMech:000364 Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom [2 warnings:
    Sclerotinia sclerotiorum on 2 interactions], and CommunityMech:000373 Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom
    [2 warnings: Nicotiana tabacum (tobacco, NCBITaxon:4097) on 2 interactions]) because
    external host plants and target phytopathogens outside taxonomy[] are modeled
    in target_taxon on COMMUNITY_LEVEL interactions.'
  target_ids:
  - CommunityMech:000347
  - CommunityMech:000364
  - CommunityMech:000373
  field_paths:
  - ecological_interactions[].target_taxon
  - ecological_interactions[].participating_taxa
  evidence_ids:
  - ev-network-integrity-audit
  rule_id: review-communities:network-integrity-unknown-target
  native_severity: P3
  normalization_reason: CommunityMech P3 (host/pathogen boundary modeling in COMMUNITY_LEVEL
    interactions) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  tags:
  - scope
  - boundary
  - network-integrity
  - stage5-remediation
- finding_id: stage4-isolate-000273-unverified-ore-prose
  issue_key: communitymech-stage4-000273-unverified-ore-prose
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: CommunityMech:000273 retains unverified arsenopyrite ore recovery claims
    and un-evidenced environmental_factors
  description: 'Although Stage 2 repaired ecological_interactions on data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    (CommunityMech:000273), its top-level description, environment_term.notes, taxonomy[0].taxon_term.notes,
    and 8 un-evidenced environmental_factors entries (7 ore/cyanide/pulp-density parameters
    and 1 temperature entry) still assert refractory gold-bearing sulfide ore (arsenopyrite/pyrite)
    bioleaching, 70-85% gold recovery, 50-200 ppm CN-, and 7-14 day leaching time
    that do not come from the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4:
    Acidithiobacillus ferrooxidans pretreatment removing >80% Cu followed by Chromobacterium
    violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct
    bioleaching).'
  target_ids:
  - CommunityMech:000273
  field_paths:
  - description
  - environment_term.notes
  - taxonomy[0].taxon_term.notes
  - environmental_factors
  evidence_ids:
  - ev-isolate-000273-audit
  rule_id: review-yaml-record:evidence-claim-alignment
  native_severity: P2
  normalization_reason: CommunityMech P2 (unverified numeric/substrate prose not supported
    by cited primary source) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    role: canonical_record
  tags:
  - evidence
  - isolates
  - stage5-remediation
- finding_id: stage4-isolate-000321-missing-functional-role
  issue_key: communitymech-stage4-000321-missing-role
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: CommunityMech:000321 omits functional_role and abundance_level on its sole
    taxon entry
  description: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml (CommunityMech:000321)
    is the only record in data/isolates/ missing functional_role and abundance_level
    on taxonomy[0] (Rothia, NCBITaxon:32207, supported by PMID:33398099 and PMID:28963201),
    reducing its proportional Completeness Score to 80/100.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-isolate-000321-audit
  rule_id: review-communities:completeness-functional-roles
  native_severity: P3
  normalization_reason: CommunityMech P3 (missing optional functional_role annotation
    on isolate taxon) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  tags:
  - completeness
  - isolates
  - stage5-remediation
actions:
- action_id: act-set-community-origin-000434
  description: 'Set community_origin: ENGINEERED on CommunityMech:000434 (Acidic_Nitrification_Minimal_Consortium.yaml)
    and append a curation_history entry.'
  finding_ids:
  - stage4-missing-community-origin-000434
  target_ids:
  - CommunityMech:000434
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-set-ecological-state-000360
  description: 'Set ecological_state: STABLE on CommunityMech:000360 (Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml)
    and append a curation_history entry.'
  finding_ids:
  - stage4-missing-ecological-state-000360
  target_ids:
  - CommunityMech:000360
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-connect-syncom-participants
  description: Populate full abstract-backed participating_taxa on COMMUNITY_LEVEL
    ecological_interactions in CommunityMech:000339, 000399, 000415, 000433, and 000447.
  finding_ids:
  - stage4-disconnected-syncom-participants
  target_ids:
  - CommunityMech:000339
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000447
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - just audit-network
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-remove-external-host-pathogen-targets
  description: Replace external non-member host/pathogen target_taxon entries on COMMUNITY_LEVEL
    interactions in CommunityMech:000347, 000364, and 000373 with member participating_taxa
    while preserving host/pathogen context in interaction name/description.
  finding_ids:
  - stage4-external-host-pathogen-targets
  target_ids:
  - CommunityMech:000347
  - CommunityMech:000364
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - just audit-network
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-reconcile-isolate-000273-prose
  description: Align description, environment_term.notes, taxonomy[0].taxon_term.notes,
    and environmental_factors in data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    (CommunityMech:000273) strictly to the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4).
  finding_ids:
  - stage4-isolate-000273-unverified-ore-prose
  target_ids:
  - CommunityMech:000273
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-populate-isolate-000321-role
  description: Populate functional_role and abundance_level on taxonomy[0] in data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    (CommunityMech:000321) supported by PMID:33398099 and PMID:28963201.
  finding_ids:
  - stage4-isolate-000321-missing-functional-role
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  - uv run python scripts/verify_history_Changed_records.py
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Full-text PDFs behind publisher paywalls were not fetched; source verification used
  cached PubMed/DOI abstracts and open-access metadata in references_cache/.
tags:
- stage4
- record-review
- deep-audit
```
