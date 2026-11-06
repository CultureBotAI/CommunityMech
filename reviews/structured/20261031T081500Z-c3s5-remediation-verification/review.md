# Cycle 3 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward Findings

- Review: 20261031T081500Z-c3s5-remediation-verification
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-31T08:00:00Z
- Finished UTC: 2026-10-31T08:15:00Z
- Reviewer: antigravity-c3s5-remediation-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Post-remediation scientific and structural verification review of all 10 finding-bearing community records from Cycle 3 Stage 4 (3 community records across 3 actionable open findings grouped into GitHub issue #2084, plus 7 source-limited deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). CommunityMech:000280 (Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml) now populates functional_role: [PATHOGEN_ANTAGONIST] on its 3 verified antagonist isolates (Paenibacillus terrae RE7, Bacillus velezensis NA3, Bacillus subtilis NA11) and abundance_level: ABUNDANT across all 5 equal-part SynCom members while preserving ecological_interactions[2] without biological_processes per test_causal_review_batch85.py (#1705), raising proportional Completeness Score from 71 to 83/100. CommunityMech:000434 (Acidic_Nitrification_Minimal_Consortium.yaml) now populates functional_role: [PRIMARY_PRODUCER] and abundance_level: DOMINANT on Candidatus Nitrosoglobus kelleri and abundance_level: DOMINANT on Mycobacterium species per PMID:42762737, raising proportional Completeness Score from 75 to 85/100. CommunityMech:000448 (Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml) now populates functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT on Streptococcus salivarius subsp. thermophilus, abundance_level: ABUNDANT on Lactobacillus delbrueckii subsp. bulgaricus, abundance_level: DOMINANT on Lactiplantibacillus plantarum, and explicit 3-member participating_taxa plus biological_processes GO:0006113 (fermentation) on ecological_interactions[1] ('Inferred Soymilk Nutrient Cross-Feeding') per PMID:42637460, raising proportional Completeness Score from 77 to 84/100. All 3 modified records are re-attested in reports/causal_graph_review/decisions/20261031-c3s5-review-remediation.yaml.

## Scope And Provenance

Full post-remediation verification of all 10 community records referenced by Cycle 3 Stage 4 findings (3 actionable finding targets + 7 carried-forward source-limited targets).

Selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle 3 Stage 4 evidence.yaml.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base a0631777d79ffe10235c6022408c58084a9e3283.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000280 | kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml | maintained | CommunityMech:000280 (Pinus armandii Endophytic Biocontrol SynCom) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:000434 | kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml | maintained | CommunityMech:000434 (Acidic Nitrification Minimal Consortium) |
| CommunityMech:000448 | kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml | maintained | CommunityMech:000448 (Soymilk Mixed-Starter Metabolic Division SynCom) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema and strict corpus validation on all 10 Cycle 3 Stage 5 target records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000280, CommunityMech:000295, CommunityMech:000302, CommunityMech:000434, CommunityMech:000448 | All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| Causal review inventory, participating_taxa integrity, and batch regression tests | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000280, CommunityMech:000295, CommunityMech:000302, CommunityMech:000434, CommunityMech:000448 | All 71 pytest checks across test_participating_taxa.py, test_causal_review_inventory.py, test_causal_review_batch85.py, and test_causal_review_batch104.py pass with 0 failures. |

## Scientific And Domain Assessments

### Post-remediation verification of functional_role, abundance_level, participating_taxa, and biological_processes on CommunityMech:000280, 000434, and 000448 (Issue #2084)

completeness: supported. Targets: CommunityMech:000280, CommunityMech:000434, CommunityMech:000448.

CommunityMech:000280 (proportional Completeness Score 71 -&gt; 83/100), CommunityMech:000434 (proportional Completeness Score 75 -&gt; 85/100), and CommunityMech:000448 (proportional Completeness Score 77 -&gt; 84/100) now populate source-backed functional_role and abundance_level on TaxonomicComposition entries and explicit participating_taxa plus GO:0006113 (fermentation) on CommunityMech:000448 ecological_interactions[1], bringing record-level functional_role coverage across all 489 MicrobialCommunity records to 489/489 (100.0%).

### Verification of abstract-grounded integrity on 7 source-limited deferred community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)

evidence: supported. Targets: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302.

All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim abstract claims without fabrication while their full-text/supplementary data gaps remain tracked in open GitHub issues.

## Findings

### c3s4-000280-pinus-syncom-antagonist-roles-and-growth-process: Pinus armandii Endophytic Biocontrol SynCom (CommunityMech:000280) omits PATHOGEN_ANTAGONIST functional roles, ABUNDANT ordinal ranks, and GO:0040007 growth biological process

major / resolved / confirmed; issue key: communitymech-c3s4-000280-pinus-syncom-antagonist-roles-and-growth-process.

CommunityMech:000280 (kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml) omitted functional_role: [PATHOGEN_ANTAGONIST] on the three verified antagonistic SynCom isolates (Paenibacillus terrae RE7, Bacillus velezensis NA3, Bacillus subtilis NA11) and omitted abundance_level: ABUNDANT across all five equal-part SynCom members despite explicit support in PMID:42322490.

Disposition: Resolved in Issue #2084: populated functional_role: [PATHOGEN_ANTAGONIST] on Paenibacillus terrae RE7, Bacillus velezensis NA3, and Bacillus subtilis NA11 and abundance_level: ABUNDANT across all 5 equal-part SynCom members per PMID:42322490, while preserving ecological_interactions[2] without biological_processes per test_causal_review_batch85.py (#1705).

### c3s4-000434-acidic-nitrification-functional-roles-and-processes: Acidic Nitrification Minimal Consortium (CommunityMech:000434) omits PRIMARY_PRODUCER functional_role on Candidatus Nitrosoglobus kelleri and DOMINANT abundance_level on both dominant consortium taxa despite verbatim support in PMID:42762737

major / resolved / confirmed; issue key: communitymech-c3s4-000434-acidic-nitrification-functional-roles-and-processes.

CommunityMech:000434 (kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml) omitted functional_role: [PRIMARY_PRODUCER] and abundance_level: DOMINANT on "Candidatus Nitrosoglobus kelleri" and omitted abundance_level: DOMINANT on Mycobacterium species despite verbatim support in PMID:42762737.

Disposition: Resolved in Issue #2084: populated functional_role: [PRIMARY_PRODUCER] and abundance_level: DOMINANT on Candidatus Nitrosoglobus kelleri and abundance_level: DOMINANT on Mycobacterium species per PMID:42762737 while preserving ecological_interactions[0] and Mycobacterium functional_role bounded per #1086/#1087/#1088.

### c3s4-000448-soymilk-starter-roles-and-crossfeeding-participants: Soymilk Mixed-Starter Metabolic Division SynCom (CommunityMech:000448) omits PRIMARY_DEGRADER functional_role on Streptococcus thermophilus, starter abundance levels, and explicit participating_taxa on Inferred Soymilk Nutrient Cross-Feeding

major / resolved / confirmed; issue key: communitymech-c3s4-000448-soymilk-starter-roles-and-crossfeeding-participants.

CommunityMech:000448 (kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml) omitted functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT on Streptococcus salivarius subsp. thermophilus, abundance_level: ABUNDANT on Lactobacillus delbrueckii subsp. bulgaricus, abundance_level: DOMINANT on Lactiplantibacillus plantarum, and explicit participating_taxa plus GO:0006113 (fermentation) on ecological_interactions[1] ('Inferred Soymilk Nutrient Cross-Feeding') despite verbatim support in PMID:42637460.

Disposition: Resolved in Issue #2084: populated functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT on Streptococcus salivarius subsp. thermophilus, abundance_level: ABUNDANT on Lactobacillus delbrueckii subsp. bulgaricus, abundance_level: DOMINANT on Lactiplantibacillus plantarum, and explicit 3-member participating_taxa plus biological_processes GO:0006113 (fermentation) on ecological_interactions[1] ('Inferred Soymilk Nutrient Cross-Feeding') per PMID:42637460.

### cheese-assay-evidence-gap: Full-text-dependent cheese rind assay specifics remain deferred in CommunityMech:000153

minor / deferred / confirmed; issue key: cheese-assay-evidence-gap.

Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153) remains capped at abstract-verified taxa and interactions because strain-specific pairwise assay details in PMID:25043025 require full-text table inspection.

Disposition: Deferred: source-limited until full-text assay tables for PMID:25043025 are ingested (#765).

### communitymech-1467-source-discrepancy-and-extension: Broader 18-species Transwell campaign and strain/table discrepancies in CommunityMech:000091 require full-text audit

minor / deferred / confirmed; issue key: communitymech-1467-source-discrepancy-and-extension.

GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures the abstract-supported exometabolite Transwell SynCom, while full-text table reconciliation for the broader 18-species campaign remains open under issue #1467.

Disposition: Deferred: tracked in GitHub issue #1467 pending full-text table reconciliation.

### communitymech-1699-coverage: Additional Phormidium alkaline-lake co-isolates in CommunityMech:000054 require full-text table verification

minor / deferred / confirmed; issue key: communitymech-1699-coverage.

Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) models the primary cyanobacterial host and abstract-backed heterotrophic guild; additional heterotrophic co-isolates require full-text table verification (#1699).

Disposition: Deferred: tracked in GitHub issue #1699 pending full-text isolate table verification.

### communitymech-1841: Lower-rank taxon resolution for Sulfide Spring Autotrophic CPR Biofilm (CommunityMech:000222) requires full-text MAG table

minor / deferred / confirmed; issue key: communitymech-1841.

Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222) retains parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments requires full-text supplementary tables (#1841).

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

### act-defer-source-limited-fulltext-findings-c3s5

Retain source-limited full-text findings under open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text or supplementary table availability before expanding abstract-grounded claims on source-limited records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c3s5-schema-validation | src/communitymech/schema/communitymech.yaml; MicrobialCommunity | supports | All 10 Cycle 3 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml with 0 LinkML errors and 489/489 MicrobialCommunity records now carrying at least one taxon functional_role (100%). |
| ev-c3s5-causal-inventory | reports/causal_graph_review/decisions/20261031-c3s5-review-remediation.yaml; records[0..2] | supports | Successor causal review ledger 20261031-c3s5-review-remediation.yaml re-attests all 3 modified community records (CommunityMech:000280, 000434, 000448); reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks (435 reviewed, 54 needs_research, 0 stale hashes, 0 structural defects). |
| ev-c3s5-primary-sources | references_cache/; PMID:42322490, PMID:42762737, PMID:42637460 | supports | Primary source abstracts and public supplement notes support PATHOGEN_ANTAGONIST and ABUNDANT on CommunityMech:000280 (PMID:42322490), PRIMARY_PRODUCER and DOMINANT on CommunityMech:000434 (PMID:42762737), and PRIMARY_DEGRADER, DOMINANT/ABUNDANT, 3-member participating_taxa, and GO:0006113 (fermentation) on CommunityMech:000448 (PMID:42637460) (#2084), while confirming that the 7 deferred records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims. |

## Limits And Additional Notes

- Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699, 000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred because primary full text or supplementary tables are paywalled or unavailable in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T081500Z-c3s5-remediation-verification
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 3 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward
  Findings
started_at: '2026-10-31T08:00:00Z'
finished_at: '2026-10-31T08:15:00Z'
reviewer:
  identity: antigravity-c3s5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated post-remediation verification review pass over the
    10 Cycle 3 Stage 4 finding-bearing community records in the working tree.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
native_verdict: 'PASS_WITH_LIMITATIONS (3 actionable Cycle 3 Stage 4 findings resolved
  across 3 updated community records in #2084; 7 source-limited findings deferred
  under open GitHub issues)'
scientific_review: true
summary: 'Post-remediation scientific and structural verification review of all 10
  finding-bearing community records from Cycle 3 Stage 4 (3 community records across
  3 actionable open findings grouped into GitHub issue #2084, plus 7 source-limited
  deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699,
  #1841, and #1847). CommunityMech:000280 (Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml)
  now populates functional_role: [PATHOGEN_ANTAGONIST] on its 3 verified antagonist
  isolates (Paenibacillus terrae RE7, Bacillus velezensis NA3, Bacillus subtilis NA11)
  and abundance_level: ABUNDANT across all 5 equal-part SynCom members while preserving
  ecological_interactions[2] without biological_processes per test_causal_review_batch85.py
  (#1705), raising proportional Completeness Score from 71 to 83/100. CommunityMech:000434
  (Acidic_Nitrification_Minimal_Consortium.yaml) now populates functional_role: [PRIMARY_PRODUCER]
  and abundance_level: DOMINANT on Candidatus Nitrosoglobus kelleri and abundance_level:
  DOMINANT on Mycobacterium species per PMID:42762737, raising proportional Completeness
  Score from 75 to 85/100. CommunityMech:000448 (Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml)
  now populates functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT
  on Streptococcus salivarius subsp. thermophilus, abundance_level: ABUNDANT on Lactobacillus
  delbrueckii subsp. bulgaricus, abundance_level: DOMINANT on Lactiplantibacillus
  plantarum, and explicit 3-member participating_taxa plus biological_processes GO:0006113
  (fermentation) on ecological_interactions[1] (''Inferred Soymilk Nutrient Cross-Feeding'')
  per PMID:42637460, raising proportional Completeness Score from 77 to 84/100. All
  3 modified records are re-attested in reports/causal_graph_review/decisions/20261031-c3s5-review-remediation.yaml.'
source:
  git_revision: a0631777d79ffe10235c6022408c58084a9e3283
  state: working_tree
  inputs:
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    sha256: 13b8ee224941b8e8a9767f0543b9eea1768c6499e311d0cde2cca07ade2e708d
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
  - path: kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml
    sha256: b2a5b083856cdb822daec58cd6da7b794f8e03bb575f20fcfbdc9d9c81769202
    role: target
  - path: kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml
    sha256: f8b17ce636bfb8c48470f7664fc1497566777d760886bb9c557c7e5c16fa8cf3
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: reports/causal_graph_review/decisions/20261031-c3s5-review-remediation.yaml
    sha256: 94fce730acc4a1465ed5395d0e510586dadb90cb9eff77af0370a0cb758a34ce
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: f9de398fc3ab2d63cb24e77bd38ac0704bd895f7edf94ffca2360fc94fe69f75
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Full post-remediation verification of all 10 community records referenced
    by Cycle 3 Stage 4 findings (3 actionable finding targets + 7 carried-forward
    source-limited targets).
  selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle
    3 Stage 4 evidence.yaml.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000280
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000434
  - CommunityMech:000448
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
- target_id: CommunityMech:000280
  path: kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml
  label: CommunityMech:000280 (Pinus armandii Endophytic Biocontrol SynCom)
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
checks:
- check_id: chk-linkml-schema-c3s5
  name: LinkML schema and strict corpus validation on all 10 Cycle 3 Stage 5 target
    records
  status: passed
  required: true
  summary: All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml
    with 0 errors.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000280
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000434
  - CommunityMech:000448
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c3s5-schema-validation
- check_id: chk-causal-and-participants-tests-c3s5
  name: Causal review inventory, participating_taxa integrity, and batch regression
    tests
  status: passed
  required: true
  summary: All 71 pytest checks across test_participating_taxa.py, test_causal_review_inventory.py,
    test_causal_review_batch85.py, and test_causal_review_batch104.py pass with 0
    failures.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000280
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000434
  - CommunityMech:000448
  command: .venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_participating_taxa.py
    tests/test_causal_review_inventory.py tests/test_causal_review_batch85.py tests/test_causal_review_batch104.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c3s5-causal-inventory
evidence:
- evidence_id: ev-c3s5-schema-validation
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity
  accessed_at: '2026-10-31T08:05:00Z'
  support: supports
  summary: All 10 Cycle 3 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml
    with 0 LinkML errors and 489/489 MicrobialCommunity records now carrying at least
    one taxon functional_role (100%).
- evidence_id: ev-c3s5-causal-inventory
  kind: validation
  reference: reports/causal_graph_review/decisions/20261031-c3s5-review-remediation.yaml
  locator: records[0..2]
  accessed_at: '2026-10-31T08:07:00Z'
  support: supports
  summary: Successor causal review ledger 20261031-c3s5-review-remediation.yaml re-attests
    all 3 modified community records (CommunityMech:000280, 000434, 000448); reports/causal_graph_review/inventory.tsv
    passes all 32 inventory integrity checks (435 reviewed, 54 needs_research, 0 stale
    hashes, 0 structural defects).
- evidence_id: ev-c3s5-primary-sources
  kind: primary_source
  reference: references_cache/
  locator: PMID:42322490, PMID:42762737, PMID:42637460
  accessed_at: '2026-10-31T08:08:00Z'
  support: supports
  summary: 'Primary source abstracts and public supplement notes support PATHOGEN_ANTAGONIST
    and ABUNDANT on CommunityMech:000280 (PMID:42322490), PRIMARY_PRODUCER and DOMINANT
    on CommunityMech:000434 (PMID:42762737), and PRIMARY_DEGRADER, DOMINANT/ABUNDANT,
    3-member participating_taxa, and GO:0006113 (fermentation) on CommunityMech:000448
    (PMID:42637460) (#2084), while confirming that the 7 deferred records (#765, #1467,
    #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims.'
assessments:
- assessment_id: assess-c3s5-functional-roles-and-participants
  area: completeness
  topic: 'Post-remediation verification of functional_role, abundance_level, participating_taxa,
    and biological_processes on CommunityMech:000280, 000434, and 000448 (Issue #2084)'
  outcome: supported
  summary: CommunityMech:000280 (proportional Completeness Score 71 -> 83/100), CommunityMech:000434
    (proportional Completeness Score 75 -> 85/100), and CommunityMech:000448 (proportional
    Completeness Score 77 -> 84/100) now populate source-backed functional_role and
    abundance_level on TaxonomicComposition entries and explicit participating_taxa
    plus GO:0006113 (fermentation) on CommunityMech:000448 ecological_interactions[1],
    bringing record-level functional_role coverage across all 489 MicrobialCommunity
    records to 489/489 (100.0%).
  target_ids:
  - CommunityMech:000280
  - CommunityMech:000434
  - CommunityMech:000448
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-causal-inventory
  - ev-c3s5-primary-sources
  metrics:
  - name: record_functional_role_coverage_pct
    value: 100.0
    unit: percent
    definition: Percentage of MicrobialCommunity records in CommunityMech with at
      least one TaxonomicComposition entry carrying a populated functional_role (489/489).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c3s5-deferred-source-limited-records
  area: evidence
  topic: 'Verification of abstract-grounded integrity on 7 source-limited deferred
    community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)'
  outcome: supported
  summary: All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153,
    000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim
    abstract claims without fabrication while their full-text/supplementary data gaps
    remain tracked in open GitHub issues.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
findings:
- finding_id: c3s4-000280-pinus-syncom-antagonist-roles-and-growth-process
  issue_key: communitymech-c3s4-000280-pinus-syncom-antagonist-roles-and-growth-process
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Pinus armandii Endophytic Biocontrol SynCom (CommunityMech:000280) omits
    PATHOGEN_ANTAGONIST functional roles, ABUNDANT ordinal ranks, and GO:0040007 growth
    biological process
  description: 'CommunityMech:000280 (kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml)
    omitted functional_role: [PATHOGEN_ANTAGONIST] on the three verified antagonistic
    SynCom isolates (Paenibacillus terrae RE7, Bacillus velezensis NA3, Bacillus subtilis
    NA11) and omitted abundance_level: ABUNDANT across all five equal-part SynCom
    members despite explicit support in PMID:42322490.'
  target_ids:
  - CommunityMech:000280
  field_paths:
  - taxonomy[].functional_role
  - taxonomy[].abundance_level
  - ecological_interactions[2].biological_processes
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-causal-inventory
  - ev-c3s5-primary-sources
  rule_id: review-communities:completeness-functional-roles-and-processes
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing source-backed functional_role and
    abundance_level on an active biocontrol SynCom record) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2084: populated functional_role: [PATHOGEN_ANTAGONIST]
    on Paenibacillus terrae RE7, Bacillus velezensis NA3, and Bacillus subtilis NA11
    and abundance_level: ABUNDANT across all 5 equal-part SynCom members per PMID:42322490,
    while preserving ecological_interactions[2] without biological_processes per test_causal_review_batch85.py
    (#1705).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063000Z-c3s4-record-deep-audit
    finding_id: c3s4-000280-pinus-syncom-antagonist-roles-and-growth-process
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: c3s4-000280-pinus-syncom-antagonist-roles-and-growth-process
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2084
- finding_id: c3s4-000434-acidic-nitrification-functional-roles-and-processes
  issue_key: communitymech-c3s4-000434-acidic-nitrification-functional-roles-and-processes
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Acidic Nitrification Minimal Consortium (CommunityMech:000434) omits PRIMARY_PRODUCER
    functional_role on Candidatus Nitrosoglobus kelleri and DOMINANT abundance_level
    on both dominant consortium taxa despite verbatim support in PMID:42762737
  description: 'CommunityMech:000434 (kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml)
    omitted functional_role: [PRIMARY_PRODUCER] and abundance_level: DOMINANT on "Candidatus
    Nitrosoglobus kelleri" and omitted abundance_level: DOMINANT on Mycobacterium
    species despite verbatim support in PMID:42762737.'
  target_ids:
  - CommunityMech:000434
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-causal-inventory
  - ev-c3s5-primary-sources
  rule_id: review-communities:completeness-functional-roles-and-abundance
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing PRIMARY_PRODUCER functional_role
    and DOMINANT abundance_level on the dominant consortium members despite verbatim
    abstract evidence in PMID:42762737) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2084: populated functional_role: [PRIMARY_PRODUCER]
    and abundance_level: DOMINANT on Candidatus Nitrosoglobus kelleri and abundance_level:
    DOMINANT on Mycobacterium species per PMID:42762737 while preserving ecological_interactions[0]
    and Mycobacterium functional_role bounded per #1086/#1087/#1088.'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063000Z-c3s4-record-deep-audit
    finding_id: c3s4-000434-acidic-nitrification-functional-roles-and-processes
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: c3s4-000434-acidic-nitrification-functional-roles-and-processes
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2084
- finding_id: c3s4-000448-soymilk-starter-roles-and-crossfeeding-participants
  issue_key: communitymech-c3s4-000448-soymilk-starter-roles-and-crossfeeding-participants
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Soymilk Mixed-Starter Metabolic Division SynCom (CommunityMech:000448) omits
    PRIMARY_DEGRADER functional_role on Streptococcus thermophilus, starter abundance
    levels, and explicit participating_taxa on Inferred Soymilk Nutrient Cross-Feeding
  description: 'CommunityMech:000448 (kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml)
    omitted functional_role: [PRIMARY_DEGRADER] and abundance_level: DOMINANT on Streptococcus
    salivarius subsp. thermophilus, abundance_level: ABUNDANT on Lactobacillus delbrueckii
    subsp. bulgaricus, abundance_level: DOMINANT on Lactiplantibacillus plantarum,
    and explicit participating_taxa plus GO:0006113 (fermentation) on ecological_interactions[1]
    (''Inferred Soymilk Nutrient Cross-Feeding'') despite verbatim support in PMID:42637460.'
  target_ids:
  - CommunityMech:000448
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[].abundance_level
  - ecological_interactions[1].participating_taxa
  - ecological_interactions[1].biological_processes
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-causal-inventory
  - ev-c3s5-primary-sources
  rule_id: review-communities:completeness-functional-roles-and-participants
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing PRIMARY_DEGRADER functional_role
    on S. thermophilus, missing abundance_level across all 3 starter taxa, and missing
    explicit participating_taxa and GO:0006113 fermentation on ecological_interactions[1])
    maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2084: populated functional_role: [PRIMARY_DEGRADER]
    and abundance_level: DOMINANT on Streptococcus salivarius subsp. thermophilus,
    abundance_level: ABUNDANT on Lactobacillus delbrueckii subsp. bulgaricus, abundance_level:
    DOMINANT on Lactiplantibacillus plantarum, and explicit 3-member participating_taxa
    plus biological_processes GO:0006113 (fermentation) on ecological_interactions[1]
    (''Inferred Soymilk Nutrient Cross-Feeding'') per PMID:42637460.'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063000Z-c3s4-record-deep-audit
    finding_id: c3s4-000448-soymilk-starter-roles-and-crossfeeding-participants
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: c3s4-000448-soymilk-starter-roles-and-crossfeeding-participants
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2084
- finding_id: cheese-assay-evidence-gap
  issue_key: cheese-assay-evidence-gap
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Full-text-dependent cheese rind assay specifics remain deferred in CommunityMech:000153
  description: Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153)
    remains capped at abstract-verified taxa and interactions because strain-specific
    pairwise assay details in PMID:25043025 require full-text table inspection.
  target_ids:
  - CommunityMech:000153
  field_paths:
  - ecological_interactions
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text assay detail gap preserved as minor.
  disposition_reason: 'Deferred: source-limited until full-text assay tables for PMID:25043025
    are ingested (#765).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T091351Z-cheese-before
    finding_id: evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T092604Z-cheese-after
    finding_id: evidence-gap
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
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/765
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1467-source-discrepancy-and-extension
  issue_key: communitymech-1467-source-discrepancy-and-extension
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Broader 18-species Transwell campaign and strain/table discrepancies in CommunityMech:000091
    require full-text audit
  description: 'GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures
    the abstract-supported exometabolite Transwell SynCom, while full-text table reconciliation
    for the broader 18-species campaign remains open under issue #1467.'
  target_ids:
  - CommunityMech:000091
  field_paths:
  - taxonomy
  - ecological_interactions
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text extension preserved as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1467 pending full-text table
    reconciliation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T062338Z-transwell-before
    finding_id: remaining
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T063739Z-transwell-after
    finding_id: remaining
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
  title: Additional Phormidium alkaline-lake co-isolates in CommunityMech:000054 require
    full-text table verification
  description: Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) models the
    primary cyanobacterial host and abstract-backed heterotrophic guild; additional
    heterotrophic co-isolates require full-text table verification (#1699).
  target_ids:
  - CommunityMech:000054
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text membership extension preserved as
    minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1699 pending full-text isolate
    table verification.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T235318Z-causal-prompt-phormidium-after
    finding_id: phormidium-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T014050Z-phormidium-identity-after
    finding_id: phormidium-coverage
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
  title: Lower-rank taxon resolution for Sulfide Spring Autotrophic CPR Biofilm (CommunityMech:000222)
    requires full-text MAG table
  description: Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222)
    retains parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments
    requires full-text supplementary tables (#1841).
  target_ids:
  - CommunityMech:000222
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
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
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
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
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
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
  - ev-c3s5-schema-validation
  - ev-c3s5-primary-sources
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
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-defer-source-limited-fulltext-findings-c3s5
  description: 'Retain source-limited full-text findings under open GitHub issues
    (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or
    supplementary strain/assay tables become available for CommunityMech:000048, 000054,
    000091, 000153, 000222, 000295, and 000302.'
  finding_ids:
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
  acceptance_checks:
  - Verify full-text or supplementary table availability before expanding abstract-grounded
    claims on source-limited records.
limitations:
- 'Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699,
  000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred
  because primary full text or supplementary tables are paywalled or unavailable in
  references_cache/.'
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261026T063000Z-c3s4-record-deep-audit
  relationship: supersedes_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  relationship: supersedes_stage4_cohort_review
tags:
- cycle3
- stage5
- remediation-verification
- record-review
```
