# Cycle 14 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward Findings

- Review: 20261110T185500Z-c14s5-remediation-verification
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-10T18:52:00Z
- Finished UTC: 2026-11-10T18:55:00Z
- Reviewer: antigravity-c14s5-remediation-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Post-remediation scientific and structural verification review of all 12 finding-bearing community and isolate records from Cycle 14 Stage 4 (2 community records resolved in GitHub issue #2755, 3 cadmium-immobilization coculture and isolate baseline records deduplicated under open vocabulary-gap issue #2194, and 7 source-limited deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). CommunityMech:000106 (Tobacco_Chemotactic_Biocontrol_SynCom.yaml) now populates abundance_level: DOMINANT, abundance_value: '5% (v/w) equal-ratio strain inoculation into composite organic fertilizer', and verbatim equal-ratio inoculation evidence from PMID:40670700 (doi:10.1007/s00253-025-13547-6) across Pseudomonas sp. (taxonomy[0], NCBITaxon:306) and Bacillus sp. (taxonomy[1], NCBITaxon:1386) while preserving discussions[0], raising its review-communities s_ab rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level; Completeness Score 87/100 -&gt; 92/100; scripts/audit_completeness.py score 80/100). CommunityMech:000110 (Rice_P_Uptake_Intercropping_SynCom4.yaml) now populates abundance_level: DOMINANT, abundance_value: '1 x 10^8 CFU/g equal-density four-strain SynCom suspension (15 mL injected into sterilized soil)', and verbatim isolate selection and equal-density inoculation evidence from PMID:39684532 (doi:10.3390/ijms252312819) across Variovorax paradoxus (taxonomy[0], NCBITaxon:34073), Novosphingobium subterraneum (taxonomy[1], NCBITaxon:48936), Hydrogenophaga pseudoflava (taxonomy[2], NCBITaxon:47421), and Acidovorax sp. (taxonomy[3], NCBITaxon:12916) while preserving discussions[0], raising review-communities s_ab from 0/5 to 5/5 (0/4 -&gt; 4/4 taxa with abundance_level; Completeness Score 92/100 -&gt; 97/100; scripts/audit_completeness.py score 80/100). Both modified records are re-attested in reports/causal_graph_review/decisions/20261110-c14s5-review-remediation.yaml.

## Scope And Provenance

Full post-remediation verification of all 12 community and isolate records referenced by Cycle 14 Stage 4 findings (2 remediated community records + 3 vocabulary-blocked cadmium-immobilization records + 7 carried-forward source-limited targets).

Selection: All 12 records referenced by carry_forward_ids and owner_paths in Cycle 14 Stage 4 evidence.yaml.
Coverage: full; 12 reviewed / 12 in the declared population.
Source: working_tree at Git base 7e7fc7e05b5979b283b76ecca384a58665efabe9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000106 | kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml | maintained | CommunityMech:000106 (Tobacco Chemotactic Biocontrol SynCom) |
| CommunityMech:000110 | kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml | maintained | CommunityMech:000110 (Rice P-Uptake Intercropping SynCom) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:000374 | kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml | maintained | CommunityMech:000374 (Achromobacter SL8 and Enterobacter SL12 Cadmium-Immobilizing Coculture) |
| CommunityMech:000533 | data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml | maintained | CommunityMech:000533 (Achromobacter sp. SL8 Single-Strain Cadmium-Immobilization Baseline) |
| CommunityMech:000534 | data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml | maintained | CommunityMech:000534 (Enterobacter sp. SL12 Single-Strain Cadmium-Immobilization Baseline) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema and strict corpus validation on all 12 Cycle 14 Stage 5 target records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000106, CommunityMech:000110, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000533, CommunityMech:000534 | All 12 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| Causal review inventory, participating_taxa integrity, and HTML docs regression tests | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000106, CommunityMech:000110, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000533, CommunityMech:000534 | All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py, and test_docs_do_not_contradict_the_kb.py pass with 0 failures. |

## Scientific And Domain Assessments

### Post-remediation verification of abundance_level and direct equal-ratio / equal-density SynCom inoculation evidence on CommunityMech:000106 and 000110 (Issue #2755)

completeness: supported. Targets: CommunityMech:000106, CommunityMech:000110.

CommunityMech:000106 (review-communities s_ab 0/5 -&gt; 5/5, Completeness Score 87/100 -&gt; 92/100; scripts/audit_completeness.py score 80/100) and CommunityMech:000110 (review-communities s_ab 0/5 -&gt; 5/5, Completeness Score 92/100 -&gt; 97/100; scripts/audit_completeness.py score 80/100) now populate source-backed functional_role, abundance_level, abundance_value, and verbatim abundance evidence across all 6/6 TaxonomicComposition entries while preserving all record-level discussions.

### Verification of schema-policy and abstract-grounded integrity on 3 vocabulary-blocked (#2194) and 7 source-limited (#765, #1467, #1657, #1681, #1699, #1841, #1847) records

evidence: supported. Targets: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000533, CommunityMech:000534.

CommunityMech:000374, 000533, and 000534 preserve accurate inorganic Cd2+ immobilization representations without forcing FunctionalRoleEnum.PRIMARY_DEGRADER ('Degrades complex substrates', #2194 / #301), and all 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain grounded strictly to verbatim abstract claims without fabrication.

## Findings

### c14s4-000106-tobacco-chemotactic-syncom-abundance-levels: Both chemotactic SynCom member rows in Tobacco_Chemotactic_Biocontrol_SynCom (CommunityMech:000106) omit abundance_level despite explicit equal 5% (v/w) strain inoculation in PMID:40670700

major / resolved / confirmed; issue key: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels.

In kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml (CommunityMech:000106), Pseudomonas sp. (taxonomy[0], NCBITaxon:306, functional_role: [CROSS_FEEDER]) and Bacillus sp. (taxonomy[1], NCBITaxon:1386, functional_role: [CROSS_FEEDER]) both omit controlled abundance_level and direct equal-inoculation evidence in taxonomy[].evidence. The cited open-access study (PMID:40670700, doi:10.1007/s00253-025-13547-6) explicitly establishes in Materials and Methods ('Creation of bacterial fertilizer for chemotactic SynCom') that 'Each strain used in the chemotactic SynCom was inoculated into the composite nutrient at a 5% (v/w) ratio, along with the corresponding prebiotics screened in the previous experiment.' Setting abundance_level: DOMINANT and attaching this verbatim PMID:40670700 equal-inoculation snippet on taxonomy[0] and taxonomy[1] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level; proportional Completeness Score 87/100 -&gt; 92/100; scripts/audit_completeness.py score 80/100 -&gt; 95/100).

Disposition: Resolved in Issue #2755: populated abundance_level: DOMINANT, abundance_value: '5% (v/w) equal-ratio strain inoculation into composite organic fertilizer', and verbatim equal-ratio inoculation evidence from PMID:40670700 (doi:10.1007/s00253-025-13547-6) on Pseudomonas sp. (NCBITaxon:306) and Bacillus sp. (NCBITaxon:1386).

### c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels: All four defined rice rhizosphere SynCom4 members in Rice_P_Uptake_Intercropping_SynCom4 (CommunityMech:000110) omit abundance_level despite explicit 1 x 10^8 CFU/g equal-density SynCom assembly in PMID:39684532

major / resolved / confirmed; issue key: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels.

In kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml (CommunityMech:000110), Variovorax paradoxus (taxonomy[0], NCBITaxon:34073, functional_role: [CROSS_FEEDER]), Novosphingobium subterraneum (taxonomy[1], NCBITaxon:48936, functional_role: [CROSS_FEEDER]), Hydrogenophaga pseudoflava (taxonomy[2], NCBITaxon:47421, functional_role: [CROSS_FEEDER]), and Acidovorax sp. (taxonomy[3], NCBITaxon:12916, functional_role: [CROSS_FEEDER]) all omit controlled abundance_level and direct equal-density inoculation evidence in taxonomy[].evidence. The cited open-access study (PMID:39684532, doi:10.3390/ijms252312819) explicitly establishes in Section 2.1 ('Four isolates were selected from enriched genera that closely matched their corresponding ASV sequences; i.e., Novosphingobium subterraneum (ASV995, 98.02%), Hydrogenophaga pseudoflava ( ASV44940 , 99.07%), Acidovorax sp. ( ASV57550 , 100%), and Variovorax paradoxus (ASV7847, 97.22%).') and in Section 4.4 ('Glasshouse Pot Experiments') that 'The concentration of the cultured bacterial strain was adjusted to 1 × 108 CFU/g with sterilized water. A 15 mL suspension of this SynCom was injected into the sterilized soil; sterilized water served as a control.' Setting abundance_level: DOMINANT and attaching this verbatim PMID:39684532 equal-density SynCom inoculation snippet on taxonomy[0..3] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/4 -&gt; 4/4 taxa with abundance_level; proportional Completeness Score 92/100 -&gt; 97/100; scripts/audit_completeness.py score 80/100 -&gt; 95/100).

Disposition: Resolved in Issue #2755: populated abundance_level: DOMINANT, abundance_value: '1 x 10^8 CFU/g equal-density four-strain SynCom suspension (15 mL injected into sterilized soil)', and verbatim isolate selection and equal-density inoculation evidence from PMID:39684532 (doi:10.3390/ijms252312819) on Variovorax paradoxus (NCBITaxon:34073), Novosphingobium subterraneum (NCBITaxon:48936), Hydrogenophaga pseudoflava (NCBITaxon:47421), and Acidovorax sp. (NCBITaxon:12916).

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

### act-defer-functional-role-vocab-and-source-limited-findings-c14s5

Retain the 3 cadmium-immobilization functional_role findings under open vocabulary-gap issue #2194 until FunctionalRoleEnum adds a non-degradative metal-immobilizer value, and retain the 7 source-limited full-text findings under open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or supplementary tables become available.

- Do not force FunctionalRoleEnum.PRIMARY_DEGRADER onto inorganic Cd2+ immobilization records (#2194, #301).
- Verify full-text or supplementary table availability before expanding abstract-grounded claims on source-limited records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c14s5-schema-validation | src/communitymech/schema/communitymech.yaml; MicrobialCommunity | supports | All 12 Cycle 14 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology term label errors. |
| ev-c14s5-causal-inventory | reports/causal_graph_review/decisions/20261110-c14s5-review-remediation.yaml; records[0..1] | supports | Successor causal review ledger 20261110-c14s5-review-remediation.yaml re-attests both modified community records (CommunityMech:000106 and CommunityMech:000110); reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks. |
| ev-c14s5-primary-sources | references_cache/; PMID:40670700, PMID:39684532, PMID:42307251 | supports | Primary source caches in references_cache/ support abundance_level: DOMINANT and verbatim 5% (v/w) equal-ratio inoculation evidence on CommunityMech:000106 (PMID:40670700, doi:10.1007/s00253-025-13547-6) and abundance_level: DOMINANT plus verbatim isolate selection and 1 x 10^8 CFU/g equal-density inoculation evidence on CommunityMech:000110 (PMID:39684532, doi:10.3390/ijms252312819) (#2755), while confirming that inorganic Cd2+ immobilization in PMID:42307251 (CommunityMech:000374, 000533, 000534) is blocked on FunctionalRoleEnum vocabulary expansion (#2194, #301) and the 7 source-limited records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims. |

## Limits And Additional Notes

- 3 carried-forward cadmium-immobilization functional_role findings across CommunityMech:000374, 000533, and 000534 remain deferred under open GitHub issue #2194 (#301) until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier value.
- 7 carried-forward source-limited findings across CommunityMech:000048 (#1657), 000054 (#1699), 000091 (#1467), 000153 (#765), 000222 (#1841), 000295 (#1681), and 000302 (#1847) remain deferred pending full-text table or supplement ingestion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T185500Z-c14s5-remediation-verification
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 14 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward
  Findings
started_at: '2026-11-10T18:52:00Z'
finished_at: '2026-11-10T18:55:00Z'
reviewer:
  identity: antigravity-c14s5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated post-remediation verification review pass over the
    12 Cycle 14 Stage 4 finding-bearing community and isolate records in the working
    tree.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
native_verdict: 'PASS_WITH_LIMITATIONS (2 actionable Cycle 14 Stage 4 findings resolved
  across 2 updated community records in #2755; 3 FunctionalRoleEnum vocabulary-gap
  findings deferred under #2194; 7 source-limited findings deferred under open GitHub
  issues)'
scientific_review: true
summary: 'Post-remediation scientific and structural verification review of all 12
  finding-bearing community and isolate records from Cycle 14 Stage 4 (2 community
  records resolved in GitHub issue #2755, 3 cadmium-immobilization coculture and isolate
  baseline records deduplicated under open vocabulary-gap issue #2194, and 7 source-limited
  deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699,
  #1841, and #1847). CommunityMech:000106 (Tobacco_Chemotactic_Biocontrol_SynCom.yaml)
  now populates abundance_level: DOMINANT, abundance_value: ''5% (v/w) equal-ratio
  strain inoculation into composite organic fertilizer'', and verbatim equal-ratio
  inoculation evidence from PMID:40670700 (doi:10.1007/s00253-025-13547-6) across
  Pseudomonas sp. (taxonomy[0], NCBITaxon:306) and Bacillus sp. (taxonomy[1], NCBITaxon:1386)
  while preserving discussions[0], raising its review-communities s_ab rubric component
  from 0/5 to 5/5 (0/2 -> 2/2 taxa with abundance_level; Completeness Score 87/100
  -> 92/100; scripts/audit_completeness.py score 80/100). CommunityMech:000110 (Rice_P_Uptake_Intercropping_SynCom4.yaml)
  now populates abundance_level: DOMINANT, abundance_value: ''1 x 10^8 CFU/g equal-density
  four-strain SynCom suspension (15 mL injected into sterilized soil)'', and verbatim
  isolate selection and equal-density inoculation evidence from PMID:39684532 (doi:10.3390/ijms252312819)
  across Variovorax paradoxus (taxonomy[0], NCBITaxon:34073), Novosphingobium subterraneum
  (taxonomy[1], NCBITaxon:48936), Hydrogenophaga pseudoflava (taxonomy[2], NCBITaxon:47421),
  and Acidovorax sp. (taxonomy[3], NCBITaxon:12916) while preserving discussions[0],
  raising review-communities s_ab from 0/5 to 5/5 (0/4 -> 4/4 taxa with abundance_level;
  Completeness Score 92/100 -> 97/100; scripts/audit_completeness.py score 80/100).
  Both modified records are re-attested in reports/causal_graph_review/decisions/20261110-c14s5-review-remediation.yaml.'
source:
  git_revision: 7e7fc7e05b5979b283b76ecca384a58665efabe9
  state: working_tree
  inputs:
  - path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
    sha256: 0680fbc0c1ee94f3a79ce13d9c6b3d8b91317022addca4c095195a37974b6d0e
    role: target
  - path: data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
    sha256: 68a2f6ea9b523e7db0eacf6ef1a87af5227cd3f6c7e93be14facffc265232796
    role: target
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    sha256: eeef4a3c72f6660c2263fe91ec7858610797c19fa513bf641e2a6234ff4414d4
    role: target
  - path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    sha256: e4ccd373cf107383615b6f207ceb0521c83b4c97daf57c6700a441b2392ddda3
    role: target
  - path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    sha256: 51bf55d56342aa28864c0dd458a172209f9ef1e14e51a0cd210bb46521a17f47
    role: target
  - path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    sha256: 49138a663308a7331c64b2be0a72a6127ad800063b78a7648c27712fc9dd87ef
    role: target
  - path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    sha256: 1e5ee2a939774f3954bdb42b6c4124c1de1f0b36a3dc7b3e93e74ad52baa199b
    role: target
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 0f03389e79ddcf2e97ebb0f32bd51a776b6bcbaea3ddad52c21ada8feca2939b
    role: target
  - path: kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
    sha256: 2f705e42f3bb09abc227b96b636a133d3c82f612203782eb31412be6bea54a0e
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
    sha256: 05fbd542d92c9fc17a9538e9ab69804f5a0a4771488110aaee7c70e1d8c4539f
    role: target
  - path: reports/causal_graph_review/decisions/20261110-c14s5-review-remediation.yaml
    sha256: d3ed8d624a3aa4f33e2c3dcbb4323c7031544fd4d5ab81eb80c932411ffc0c29
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 301fe04f778a729c1b0ac07e38d6f7950ccf4add6a7cee7da8824200b65d42a3
    role: context
  - path: reviews/structured/20261110T164500Z-c14s4-record-deep-audit/review.yaml
    sha256: 9eb75fdf55ddcedced5cd2bd3c32430a5a33f24fd9d568062048a4a09628a1d6
    role: context
  - path: reviews/structured/20261110T164600Z-c14s4-frozen-cohort-review/review.yaml
    sha256: 2308b28f6f9bb5828b6d56ec14b17a45ff19da3bf71a640a9c20f0c8bfa48240
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Full post-remediation verification of all 12 community and isolate
    records referenced by Cycle 14 Stage 4 findings (2 remediated community records
    + 3 vocabulary-blocked cadmium-immobilization records + 7 carried-forward source-limited
    targets).
  selection: All 12 records referenced by carry_forward_ids and owner_paths in Cycle
    14 Stage 4 evidence.yaml.
  coverage: full
  population_size: 12
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000106
  - CommunityMech:000110
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000533
  - CommunityMech:000534
targets:
- target_id: CommunityMech:000048
  path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
  label: CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000054
  path: kb/communities/Phormidium_Alkaline_Consortium.yaml
  label: CommunityMech:000054 (Phormidium Alkaline Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000091
  path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
  label: CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000106
  path: kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml
  label: CommunityMech:000106 (Tobacco Chemotactic Biocontrol SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000110
  path: kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml
  label: CommunityMech:000110 (Rice P-Uptake Intercropping SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000153
  path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
  label: CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000222
  path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  label: CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000295
  path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  label: CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic
    Co-culture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000302
  path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  label: CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000374
  path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  label: CommunityMech:000374 (Achromobacter SL8 and Enterobacter SL12 Cadmium-Immobilizing
    Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000533
  path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
  label: CommunityMech:000533 (Achromobacter sp. SL8 Single-Strain Cadmium-Immobilization
    Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000534
  path: data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
  label: CommunityMech:000534 (Enterobacter sp. SL12 Single-Strain Cadmium-Immobilization
    Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-c14s5
  name: LinkML schema and strict corpus validation on all 12 Cycle 14 Stage 5 target
    records
  status: passed
  required: true
  summary: All 12 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml
    with 0 errors.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000106
  - CommunityMech:000110
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000533
  - CommunityMech:000534
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c14s5-schema-validation
- check_id: chk-causal-and-participants-tests-c14s5
  name: Causal review inventory, participating_taxa integrity, and HTML docs regression
    tests
  status: passed
  required: true
  summary: All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py,
    and test_docs_do_not_contradict_the_kb.py pass with 0 failures.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000106
  - CommunityMech:000110
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000533
  - CommunityMech:000534
  command: .venv/bin/pytest tests/test_participating_taxa.py tests/test_causal_review_inventory.py
    tests/test_docs_do_not_contradict_the_kb.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c14s5-causal-inventory
evidence:
- evidence_id: ev-c14s5-schema-validation
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity
  accessed_at: '2026-11-10T18:53:00Z'
  support: supports
  summary: All 12 Cycle 14 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml
    with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology
    term label errors.
- evidence_id: ev-c14s5-causal-inventory
  kind: validation
  reference: reports/causal_graph_review/decisions/20261110-c14s5-review-remediation.yaml
  locator: records[0..1]
  accessed_at: '2026-11-10T18:53:30Z'
  support: supports
  summary: Successor causal review ledger 20261110-c14s5-review-remediation.yaml re-attests
    both modified community records (CommunityMech:000106 and CommunityMech:000110);
    reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks.
- evidence_id: ev-c14s5-primary-sources
  kind: primary_source
  reference: references_cache/
  locator: PMID:40670700, PMID:39684532, PMID:42307251
  accessed_at: '2026-11-10T18:54:00Z'
  support: supports
  summary: 'Primary source caches in references_cache/ support abundance_level: DOMINANT
    and verbatim 5% (v/w) equal-ratio inoculation evidence on CommunityMech:000106
    (PMID:40670700, doi:10.1007/s00253-025-13547-6) and abundance_level: DOMINANT
    plus verbatim isolate selection and 1 x 10^8 CFU/g equal-density inoculation evidence
    on CommunityMech:000110 (PMID:39684532, doi:10.3390/ijms252312819) (#2755), while
    confirming that inorganic Cd2+ immobilization in PMID:42307251 (CommunityMech:000374,
    000533, 000534) is blocked on FunctionalRoleEnum vocabulary expansion (#2194,
    #301) and the 7 source-limited records (#765, #1467, #1657, #1681, #1699, #1841,
    #1847) remain bounded to abstract-verified claims.'
assessments:
- assessment_id: assess-c14s5-taxonomic-abundance-levels
  area: completeness
  topic: 'Post-remediation verification of abundance_level and direct equal-ratio
    / equal-density SynCom inoculation evidence on CommunityMech:000106 and 000110
    (Issue #2755)'
  outcome: supported
  summary: CommunityMech:000106 (review-communities s_ab 0/5 -> 5/5, Completeness
    Score 87/100 -> 92/100; scripts/audit_completeness.py score 80/100) and CommunityMech:000110
    (review-communities s_ab 0/5 -> 5/5, Completeness Score 92/100 -> 97/100; scripts/audit_completeness.py
    score 80/100) now populate source-backed functional_role, abundance_level, abundance_value,
    and verbatim abundance evidence across all 6/6 TaxonomicComposition entries while
    preserving all record-level discussions.
  target_ids:
  - CommunityMech:000106
  - CommunityMech:000110
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-causal-inventory
  - ev-c14s5-primary-sources
  metrics:
  - name: remediated_taxon_abundance_level_pct
    value: 100.0
    unit: percent
    definition: Percentage of TaxonomicComposition entries across the 2 remediated
      MicrobialCommunity records carrying both populated functional_role and abundance_level
      (6/6).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c14s5-deferred-vocabulary-and-source-limited-records
  area: evidence
  topic: 'Verification of schema-policy and abstract-grounded integrity on 3 vocabulary-blocked
    (#2194) and 7 source-limited (#765, #1467, #1657, #1681, #1699, #1841, #1847)
    records'
  outcome: supported
  summary: 'CommunityMech:000374, 000533, and 000534 preserve accurate inorganic Cd2+
    immobilization representations without forcing FunctionalRoleEnum.PRIMARY_DEGRADER
    (''Degrades complex substrates'', #2194 / #301), and all 7 source-limited records
    (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain
    grounded strictly to verbatim abstract claims without fabrication.'
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000533
  - CommunityMech:000534
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
findings:
- finding_id: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels
  issue_key: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Both chemotactic SynCom member rows in Tobacco_Chemotactic_Biocontrol_SynCom
    (CommunityMech:000106) omit abundance_level despite explicit equal 5% (v/w) strain
    inoculation in PMID:40670700
  description: 'In kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml (CommunityMech:000106),
    Pseudomonas sp. (taxonomy[0], NCBITaxon:306, functional_role: [CROSS_FEEDER])
    and Bacillus sp. (taxonomy[1], NCBITaxon:1386, functional_role: [CROSS_FEEDER])
    both omit controlled abundance_level and direct equal-inoculation evidence in
    taxonomy[].evidence. The cited open-access study (PMID:40670700, doi:10.1007/s00253-025-13547-6)
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
  - ev-c14s5-schema-validation
  - ev-c14s5-causal-inventory
  - ev-c14s5-primary-sources
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
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164500Z-c14s4-record-deep-audit
    finding_id: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: c14s4-000106-tobacco-chemotactic-syncom-abundance-levels
  disposition_reason: 'Resolved in Issue #2755: populated abundance_level: DOMINANT,
    abundance_value: ''5% (v/w) equal-ratio strain inoculation into composite organic
    fertilizer'', and verbatim equal-ratio inoculation evidence from PMID:40670700
    (doi:10.1007/s00253-025-13547-6) on Pseudomonas sp. (NCBITaxon:306) and Bacillus
    sp. (NCBITaxon:1386).'
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2755
- finding_id: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels
  issue_key: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels
  category: completeness
  severity: major
  status: resolved
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
  - ev-c14s5-schema-validation
  - ev-c14s5-causal-inventory
  - ev-c14s5-primary-sources
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
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164500Z-c14s4-record-deep-audit
    finding_id: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels
  disposition_reason: 'Resolved in Issue #2755: populated abundance_level: DOMINANT,
    abundance_value: ''1 x 10^8 CFU/g equal-density four-strain SynCom suspension
    (15 mL injected into sterilized soil)'', and verbatim isolate selection and equal-density
    inoculation evidence from PMID:39684532 (doi:10.3390/ijms252312819) on Variovorax
    paradoxus (NCBITaxon:34073), Novosphingobium subterraneum (NCBITaxon:48936), Hydrogenophaga
    pseudoflava (NCBITaxon:47421), and Acidovorax sp. (NCBITaxon:12916).'
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2755
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
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164500Z-c14s4-record-deep-audit
    finding_id: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
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
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164500Z-c14s4-record-deep-audit
    finding_id: c12s4-000533-achromobacter-sl8-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
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
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164500Z-c14s4-record-deep-audit
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
- finding_id: cheese-assay-evidence-gap
  issue_key: cheese-assay-evidence-gap
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Pairwise cheese-rind competition and cross-feeding assay details require
    full-text tables beyond cached PMID:25043025 abstract
  description: Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153)
    is grounded to the cached PMID:25043025 abstract; strain-pair competition and
    cross-feeding assay specifics remain deferred until full-text supplementary tables
    are available (#765).
  target_ids:
  - CommunityMech:000153
  field_paths:
  - ecological_interactions
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text evidence gap preserved as minor.
  disposition_reason: 'Deferred: source-limited until full-text assay tables for PMID:25043025
    are ingested (#765).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T071900Z-cheese-rind-audit
    finding_id: assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/765
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1467-source-discrepancy-and-extension
  issue_key: communitymech-1467-source-discrepancy-and-extension
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: GLBRC Transwell exometabolite SynCom (CommunityMech:000091) full 18-species
    campaign details require full-text tables
  description: GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures
    the cached abstract-supported five-member model; broader 18-species campaign details
    and strain-table reconciliation require full-text tables (#1467).
  target_ids:
  - CommunityMech:000091
  field_paths:
  - taxonomy
  - ecological_interactions
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text extension gap preserved as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1467 pending full-text table
    reconciliation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T223718Z-glbrc-before
    finding_id: source-discrepancy
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T231926Z-glbrc-after
    finding_id: source-discrepancy
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1467
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1699-coverage
  issue_key: communitymech-1699-coverage
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Full heterotrophic isolate inventory for Phormidium alkaline consortium (CommunityMech:000054)
    requires full-text tables
  description: Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) records
    the abstract-supported cyanobacterial host and glyoxylate-consuming heterotrophic
    partner; additional co-isolated heterotrophs require full-text table verification
    (#1699).
  target_ids:
  - CommunityMech:000054
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text taxonomic coverage gap preserved
    as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1699 pending full-text isolate
    table verification.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T052328Z-phormidium-before
    finding_id: coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T052748Z-phormidium-after
    finding_id: coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1699
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1841
  issue_key: communitymech-1841
  category: grounding
  severity: minor
  status: deferred
  certainty: confirmed
  title: Lower-rank isolate resolution for Sulfide_Spring_Autotrophic_CPR_Biofilm
    (CommunityMech:000222) requires full-text strain tables
  description: Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222)
    grounds parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments
    requires full-text supplementary tables (#1841).
  target_ids:
  - CommunityMech:000222
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited lower-rank taxonomic grounding gap preserved
    as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1841 pending full-text supplementary
    strain table inspection.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T200439Z-spring-parent-rank
    finding_id: lower-rank
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: communitymech-1841
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1841
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1847-metg2-membership
  issue_key: communitymech-1847-metg2-membership
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Complete MetG2 rhizobacteria membership and host-assay specifics in CommunityMech:000302
    require full-text tables
  description: SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml (CommunityMech:000302)
    models the abstract-enumerated rhizobacterial taxa; full isolate membership and
    assay specifics require full-text tables (#1847).
  target_ids:
  - CommunityMech:000302
  field_paths:
  - taxonomy
  - growth_media
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text membership/cultivation gap preserved
    as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1847 pending full-text membership
    and media table inspection.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T043154Z-metg2-host-before
    finding_id: membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T044333Z-metg2-host-after
    finding_id: membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1847
  tags:
  - carried-forward
  - source-limited
- finding_id: okeke-fulltext-assay-gap
  issue_key: okeke-fulltext-assay-gap
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Paywalled full-text assay parameters for Okeke-Lu cellulolytic consortium
    (CommunityMech:000048) remain deferred
  description: Okeke_Lu_Cellulolytic_Consortium.yaml (CommunityMech:000048) is grounded
    to abstract-verified cellulolytic-xylanolytic claims; full-text monoculture vs
    co-culture enzyme assay parameters remain paywalled.
  target_ids:
  - CommunityMech:000048
  field_paths:
  - ecological_interactions
  - growth_media
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Paywalled full-text assay detail gap preserved as minor.
  disposition_reason: 'Deferred: source-limited because primary full text is paywalled
    (#1657).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T105803Z-okeke-before
    finding_id: source-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T110432Z-okeke-after
    finding_id: source-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1657
  tags:
  - carried-forward
  - source-limited
- finding_id: parachlorella-remaining-research
  issue_key: parachlorella-remaining-research
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Secondary metabolite exchange specifics in Parachlorella-Saccharomyces co-culture
    (CommunityMech:000295) require full-text data
  description: Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml (CommunityMech:000295)
    captures the primary abstract-supported algal-yeast mutualism; secondary metabolite
    exchange kinetics require full-text tables.
  target_ids:
  - CommunityMech:000295
  field_paths:
  - ecological_interactions
  evidence_ids:
  - ev-c14s5-schema-validation
  - ev-c14s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text interaction detail gap preserved
    as minor.
  disposition_reason: 'Deferred: source-limited pending full-text interaction data
    (#1681).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T133733Z-parachlorella-before
    finding_id: remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T134821Z-parachlorella-after
    finding_id: remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005600Z-c13s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T032500Z-c13s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T164600Z-c14s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-defer-functional-role-vocab-and-source-limited-findings-c14s5
  description: 'Retain the 3 cadmium-immobilization functional_role findings under
    open vocabulary-gap issue #2194 until FunctionalRoleEnum adds a non-degradative
    metal-immobilizer value, and retain the 7 source-limited full-text findings under
    open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access
    full text or supplementary tables become available.'
  finding_ids:
  - c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - c12s4-000533-achromobacter-sl8-isolate-functional-role
  - c12s4-000534-enterobacter-sl12-isolate-functional-role
  - cheese-assay-evidence-gap
  - communitymech-1467-source-discrepancy-and-extension
  - communitymech-1699-coverage
  - communitymech-1841
  - communitymech-1847-metg2-membership
  - okeke-fulltext-assay-gap
  - parachlorella-remaining-research
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000533
  - CommunityMech:000534
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical_record
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
  - 'Do not force FunctionalRoleEnum.PRIMARY_DEGRADER onto inorganic Cd2+ immobilization
    records (#2194, #301).'
  - Verify full-text or supplementary table availability before expanding abstract-grounded
    claims on source-limited records.
limitations:
- '3 carried-forward cadmium-immobilization functional_role findings across CommunityMech:000374,
  000533, and 000534 remain deferred under open GitHub issue #2194 (#301) until FunctionalRoleEnum
  adds a heavy-metal-immobilizer / metal-detoxifier value.'
- 7 carried-forward source-limited findings across CommunityMech:000048 (#1657), 000054
  (#1699), 000091 (#1467), 000153 (#765), 000222 (#1841), 000295 (#1681), and 000302
  (#1847) remain deferred pending full-text table or supplement ingestion.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261110T164500Z-c14s4-record-deep-audit
  relationship: supersedes_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261110T164600Z-c14s4-frozen-cohort-review
  relationship: supersedes_stage4_cohort_review
tags:
- cycle14
- stage5
- remediation-verification
- record-review
```
