# Shrimp enrichment SynCom panel: genus reference correspondence with isolate and assay limits retained

- Review: 20261116T000401Z-shrimp-436-genus-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-16T00:04:01.198096Z
- Finished UTC: 2026-11-16T00:04:01.673692Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Eight existing genus descriptors now have native reference blocks and statuses, with two appended native events. The modest Exiguobacterium_A and Bacillus majorities remain reference-population results, not experimental stock placements. Source genera, absent strain/species identifiers, four SynCom variants, memberships, historical notes and scientific content remain unchanged. Eight actual native checks and one append-only sidecar bind the applied bytes.

## Scope And Provenance

Only the eight taxonomy GTDB blocks/statuses, actual guarded application and appended history, source-population interpretation and eight scoped native checks. This does not identify the experimental genomes, infer individual protection mechanisms or resolve the missing assay protocol.

Selection: CommunityMech:000436 is the first whole-record canary in the prepared Shrimp/Thermophilic/Sahara lane. Records 416 and 494 remain unapplied by this workflow. This diagnostic covers only record 436; complete input checkpoints and strict historical admission precede its publication and any later applications.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 261941db9aa5c359dc7599f28e4648a6c9723396.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000436 | kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml # taxonomy[0:8].taxon_term.gtdb_classification; taxonomy[0:8].taxon_term.gtdb_grounding_status; appended native curation_history | maintained | Eight genus reference correspondences; shrimp SynCom panel and unresolved isolate identities retained |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000436 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Source genera and four SynCom variants remain distinct from reference genome placement

grounding: supported. Targets: CommunityMech:000436.

The primary abstract supports eight genus-level isolates and four variants with the retained memberships. Generic reference correspondences preserve source genera and absent strain/species identifiers; neither suffixes nor same-name blocks independently identify the study genomes.

### Eight filtered genus populations retain majority and nomenclature limits

grounding: supported. Targets: CommunityMech:000436.

The eight native populations are 30/44, 591/591, 264/270, 88/88, 49/83, 4981/8737, 486/486 and 134/134 in taxonomy order. The non-type Exiguobacterium_A majority and split Bacillus population remain explicit; Tritonibacter-to-Epibacterium is reference nomenclature. No counts are interpreted as isolates, abundance, protective effect or stock-genome assignments.

### Actual application and eight native checks preserve source and historical boundaries

provenance: supported. Targets: CommunityMech:000436.

Actual f23b-to-4152 persistence, two native inline events, one new sidecar and eight completed native commands bind frozen 261941 execution. Closed historical repairs and the current OPEN stock/protocol discussion remain distinct. Exact original ledger, current biology and old history are protected; strict admission, measured references, products and full QC remain separate.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000436-schema | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-strict | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-gtdb | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-domain | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-scalars | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-history | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-new-history | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-terms | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000436-primary | references_cache/doi_10.1016_j.aquaculture.2025.743350.md; Complete retained abstract: three gut enrichment media, genus rosters, eight corresponding isolates, four SynCom variants and shrimp survival statements. | supports | The abstract supports the source genus roster and construction of a four-variant panel. It does not provide exact strain identities or complete culture/challenge conditions. The enriched-consortium survival statement remains distinct from the SynCom results. |
| 000436-database | reports/gtdb-shrimp-thermophilic-sahara-20261115/436-source-evidence-001.json; All eight selected occurrences: full native rank-level results, filtered numerators/denominators, original descriptors, NCBI genus identity, warning and primary locators. | supports | The native ncbi_rank_g routes support eight reference blocks. Exiguobacterium_A 49/83 is explicitly non-type; Bacillus 4981/8737 spans 44 clades. No result assigns an experimental stock genome or proves individual protection. |
| 000436-application | .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-applied-001/receipt.json; Actual applied flag, frozen 261941 revision, stage 598128e4, before f23b26c7, after 4152f796 and captured native inputs. | supports | The guarded application persists exactly eight reference blocks/statuses and two native events. Original stock/source content, biological assertions, historical notes and old history are preserved. |
| 000436-scientific-boundary | kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml; OPEN shrimp_vibrio_syncom_strains_and_challenge_protocol discussion; four SynCom memberships; single community-level protection node. | context_only | Reference correspondence does not resolve species/stock names, assemblies, ratios, medium recipes or challenge timing, and does not create genus-to-pathogen causal edges. |
| 000436-historical-boundary | reports/causal_graph_review/decisions/20261007-four-records-batch101.yaml; Original record 436 unchanged/zero-event row and full captured batch 101 caller. | context_only | The original ledger remains immutable. Strict admission must protect all current biological predicates and other records' successor chains while admitting only the exact reference-only transition. |
| 000436-closed-crosswalk-repair | .temp/phase2-schema-20261115/shrimp436-issue1105-snapshot-001.log; Captured issue identity, CLOSED state and historical missing-crosswalk note repair. | context_only | Historical notes remain preserved as the original pass's limits; this closed repair is not a species/strain identification or current scientific clearance. |
| 000436-closed-timing-repair | .temp/phase2-schema-20261115/source-issue1106-snapshot-001.log; Captured issue identity, CLOSED state and unsupported challenge-timing repair. | context_only | Do not restore unsupported timing. The current OPEN protocol discussion remains unresolved despite this historical issue closure. |

## Limits And Additional Notes

- Partial technical diagnostic with scientific_review:false. Native checks do not establish full scientific review, measured snippet validation, current generated products, aggregate QC or campaign completion.
- Coverage is the complete retained primary abstract, whole canonical record, authored source assessment and batch 101 context. No new full article, supplementary material, original challenge data or study assembly was acquired or audited. Retained source-access limitations are not a fresh exhaustive claim of absence.
- The abstract describes eight corresponding isolates and four SynCom variants but does not expose exact species, strain codes, assemblies, mixing ratios, kanamycin concentration or challenge timing. The current OPEN stock/protocol discussion remains unresolved.
- Filtered reference populations are Ruegeria 30/44, Microbacterium 591/591, Tenacibaculum 264/270, Demequina 88/88, Exiguobacterium_A 49/83, Bacillus 4981/8737, Paracoccus 486/486 and Epibacterium 134/134. These denominators are not shrimp abundances, experimental isolate counts, replicates or protective-effect estimates. Fractions 0.682, 0.978, 0.59 and 0.57 are native rounded values.
- Exiguobacterium_A is a non-type majority: 49 references versus 34 in the type-bearing alternative. Bacillus spans 44 native clades with a 0.57 majority. These results do not establish which clade contains either unnamed study isolate. Preserve the preferred source genera and the native warning in source evidence.
- Tritonibacter-to-Epibacterium is reference nomenclature correspondence. It neither formally renames the source isolate nor independently links a reference assembly to the experimental strain. All source names, NCBI descriptors and historical missing-crosswalk notes remain unchanged.
- The abstract's greater-than-68-percent survival statement concerns enriched consortia, not a newly generalized effect estimate for every SynCom. Preserve the existing community-level protection node, no genus-to-pathogen edges, four variant memberships, three enrichment media and all source quotations without adding individual causal claims.
- Captured issues 1105 and 1106 are CLOSED historical repairs of missing-crosswalk wording and unsupported timing. Their closure does not resolve the current OPEN stock/protocol discussion or constitute approval of this new mapping. Both exact snapshots are additional captured review inputs through the unchanged provenance wrapper.
- Actual staging, guarded application and all eight native commands ran at frozen M5 revision 261941db9aa5c359dc7599f28e4648a6c9723396 with Python 3.13.2. Eight free plans preceded eight serial actual gates. The two native events report eight changed descriptors and one new sidecar records the actual application receipt.
- Crosswalk 761d5537 identifies exact bytes with an unestablished release. NCBI authority provenance is file identity/stat rather than a full database digest. Preserve batch 101's immutable historical unchanged/zero-event row, all current biological predicates, caches and other three records' successor chains. The complete input checkpoint precedes caller changes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261116T000401Z-shrimp-436-genus-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Shrimp enrichment SynCom panel: genus reference correspondence with isolate
  and assay limits retained'
started_at: '2026-11-16T00:04:01.198096Z'
finished_at: '2026-11-16T00:04:01.673692Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The source preparation and local preview received independent
    review. The executing agent reread the complete retained abstract, whole canonical
    record, native populations and batch 101. Root independently read the actual M5
    candidate, complete diff, native log and all 29 stage inputs. Inventory independently
    read the actual application and gate/history configuration before execution. This
    is a partial technical self-review, not a complete new scientific assessment.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Eight existing genus descriptors now have native reference blocks and statuses,
  with two appended native events. The modest Exiguobacterium_A and Bacillus majorities
  remain reference-population results, not experimental stock placements. Source genera,
  absent strain/species identifiers, four SynCom variants, memberships, historical
  notes and scientific content remain unchanged. Eight actual native checks and one
  append-only sidecar bind the applied bytes.
source:
  git_revision: 261941db9aa5c359dc7599f28e4648a6c9723396
  state: working_tree
  inputs:
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-applied-001/before.yaml
    sha256: f23b26c7b39205a716e77e5149c06e2c4e4c618dec523a3e5245c65370ec7c0e
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-applied-001/receipt.json
    sha256: 7ace8f2a47468e00800ee6d0478f3551b78b16f63d0717630a4ff7b597ae3b7b
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-domain-001/native.log
    sha256: 1f51fcb4e625843cfd36b3a4c7c96f9fef78405a32685d2703ddb3653c9be25f
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-domain-001/receipt.json
    sha256: f3f7dd1dacbee37d0297513f70b99d2aecccfce64a0f737337d2caa60b0a5414
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-domain-001/start.json
    sha256: 6b13314c4387a99462dd2200a85096e33feab449bbb6013b6ddc8494a26840f6
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-gtdb-001/native.log
    sha256: 593695620503b617fad2db4c85c094a0115b89b5cd054920d85f661ab19eefbf
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-gtdb-001/receipt.json
    sha256: b63d3f9f250576ff4ffef55be0b0532112992b117dd3063f4051d60ece1a8995
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-gtdb-001/start.json
    sha256: 50497e3d53ee1a96413d079e12a16f24e7094bbda5749ecaba7546df090bbd49
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-history-001/receipt.json
    sha256: 53b4378ac3ee937910686649f94156b6fdbcae3480540f02c552e37dedc6c2a6
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-history-001/start.json
    sha256: 4c7d223a7734777ff56a67c28827926b1aad43f1704dfa36f990f0d81faf8d7a
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-m5-candidate-001/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
    sha256: 4152f796b81669cb2ebb9a2229ce35e8364e5f49c67f2ba454f1aafa0f1a9301
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-m5-candidate-001/receipt.json
    sha256: 598128e4353f750d0a539258289709c5a9988548c4d15cb0d7e9238bf26a807f
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-new-history-001/native.log
    sha256: df1cf2851404b0f08e6ef100144a4bc058ef4dbdcf2c26b86001eae5b87e8650
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-new-history-001/receipt.json
    sha256: b3c256dcc7930bf0a700c65a11ec0f202a122b4a8c4c6b1215cb6882ba0ddbe3
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-new-history-001/start.json
    sha256: 9a2a3c257108d112c035c9c47f3b10c82e670d1e77893d53e31b9429f599b340
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-review-draft-001/base-draft/inspection.json
    sha256: 0ed88d427a6fdb3f0d6d6e79c4bc43c29d8b80b2a39db2486509d27c84870809
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-review-draft-001/base-draft/review.json
    sha256: 2fe48f6d3a9133e4d29e5cc833a057f0a73bd6561ba27d00820bedf8826a6d2e
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-scalars-001/native.log
    sha256: d3ee378820096ce6c5c23b504753883b79112602252b22d8f21acd966be95b44
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-scalars-001/receipt.json
    sha256: b3f586383dddad195e190723b526cea53c069c5d2d471bd78b1f5bfa101fbfd0
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-scalars-001/start.json
    sha256: 4b9250bfca3a144a20c2af409db15e721546e8875e1822ded2100fad11b7f8c2
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-schema-001/native.log
    sha256: 7fd90922289544985541f83b5ecbeb8d64d2e4b949e5eaaabe0f2dd859b5581f
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-schema-001/receipt.json
    sha256: efe8cca76d3f62e882d4bd454481e230081fb6dfa82fa498f8a8af883419ce62
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-schema-001/start.json
    sha256: f7b8503c900ff4d23eb912a9ac7c031498aa0f206e74b897ec3fbf19361c6318
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/native.log
    sha256: a7398469a3e59baac2667794bdd08251241f1f67560202486c0cef479f36656e
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/receipt.json
    sha256: 640509beb5878aa5f715f8090466b67b8f83eb9a44235b476e931d1b2d5353d4
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/start.json
    sha256: 80b1cdbfc5bf1ce495b42c2931ef1aa867f860890a3182bc476fd3a075db9bfd
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-terms-001/native.log
    sha256: 49fcb0004a07663331a0be79370b88ba45ec37608d8c5394a5eb28d716033b70
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-terms-001/receipt.json
    sha256: 7ce18d89e4ce51f0887210772e9a56732c5ff5523746c4ad928d37caeeff1e01
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-terms-001/start.json
    sha256: ea3f449b3ae51cacce49090a4989e1f3fd033e851c649e25e7a48d3b9d346b23
    role: context
  - path: .temp/gtdb-shrimp-thermophilic-sahara-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/phase2-schema-20261115/shrimp-thermophilic-sahara-native-routes-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/shrimp-thermophilic-sahara-native-routes-001.json
    sha256: 58ec18e188ba06b5eb0a6aca16cb2bbae9cad1dbd1cc0f25eb044fe214e53480
    role: context
  - path: .temp/phase2-schema-20261115/shrimp-thermophilic-sahara-native-routes-001.log
    sha256: 0ded5f54dacbbb462b75677374d973f7a41914f1ebc1df5b9551c3afdda4528d
    role: context
  - path: .temp/phase2-schema-20261115/shrimp436-issue1105-snapshot-001.log
    sha256: 39176919ca270a8de596a3937c94af1e7b37f09ca3b02c4ff805b0e822084804
    role: context
  - path: .temp/phase2-schema-20261115/shrimp436-source-binding-canary-001.log
    sha256: ad5c42d353b6cfea8bd65b18e397a3f0bcbe3f310c4b817631a7f89c10e1de31
    role: context
  - path: .temp/phase2-schema-20261115/source-issue1106-snapshot-001.log
    sha256: c4811ab4adffcc7152a951ca9fd6156bb8625d56bf902b8f5db6c0ddf3d2d7e0
    role: context
  - path: history/records/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel/2026-09-26T122531Z-codex-436.yaml
    sha256: b83542b6b766334389408bb16031c5153c5a4c1ccdbe3853a2c36dae2882739a
    role: context
  - path: history/records/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel/2026-11-15T235733Z-codex-a950e3.yaml
    sha256: fbdc5c19d40c8c9be43ba16e1a79f6ecb0b9d6278500366e13c4846679c020d2
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
    sha256: 4152f796b81669cb2ebb9a2229ce35e8364e5f49c67f2ba454f1aafa0f1a9301
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/doi_10.1016_j.aquaculture.2025.743350.md
    sha256: 08d126af9e096b7fbbb277971f6b23d74deaeaa597a9f20fe3f9a25bc7c2d674
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch101.yaml
    sha256: fbb7b9763fedd9775f30a3a2aee832e1b2c61d5b2fb2d09f79fe4d991d6ea12c
    role: context
  - path: reports/gtdb-shrimp-thermophilic-sahara-20261115/436-check-config-001.json
    sha256: 35d64b67bb50efb33ae0bfd149b48a20256e1a6d73ddc5be8ce557e8889fc185
    role: context
  - path: reports/gtdb-shrimp-thermophilic-sahara-20261115/436-review-config-001.json
    sha256: ee6433c6da4d8b31cb602859400870384999babb78738c1ff76dd7125f9068d6
    role: context
  - path: reports/gtdb-shrimp-thermophilic-sahara-20261115/436-source-evidence-001.json
    sha256: 62a210df425e32a0e7a7cce2a5ec5a2847ba223333d7208b5eeb1ae9db7629a8
    role: context
  - path: reports/gtdb-shrimp-thermophilic-sahara-20261115/shrimp436-authored-source-context-001.json
    sha256: 2c7d11d4e0dad3518943290753f38a45bf0e0448d745fcd238e3915ae4e47a4c
    role: context
  - path: reports/gtdb-shrimp-thermophilic-sahara-20261115/shrimp436-source-config-001.json
    sha256: 65a41016f6343df8db872edc17e99a1f3790c30cb636c4ff12195725df69f0f3
    role: context
  - path: reports/gtdb-shrimp-thermophilic-sahara-20261115/three-route-plan-001.json
    sha256: ae0a3dc1d088996a7b8d4edf4d5f08d2acaf139370323de40d0ca8cd21dbc00a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/bind_gtdb_batch_source_context_20261115.py
    sha256: 6cdeb82122c130cd5b2e7e73bbe66bc5123fc951892f9f87edb589fb4929aac3
    role: context
  - path: scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py
    sha256: c6bf0d09dc3d01797ab5d956a4f7458a9a153a8704508f50e656729e4ee1b860
    role: context
  - path: scripts/adhoc/check_gtdb_batch_unit_20261115.py
    sha256: 723047d1ec66fa752d6cedddbb6d399b18fa7f5b7a0e27fc435c76abfeb10493
    role: context
  - path: scripts/adhoc/compose_gtdb_source_config_20261115.jq
    sha256: 45f228d7cbd89ac7b39ff0f470d6a7602e822b866133d2f9a1b462ce38f9d5a5
    role: context
  - path: scripts/adhoc/export_m5_technical_evidence_20261114.py
    sha256: a0f43f617e8921443e660d262d28713f40b4c23770b684203c37b65330cc4a5d
    role: context
  - path: scripts/adhoc/extend_gtdb_review_provenance_20261115.py
    sha256: 9be067c65585b97e0d79d76cb0865dafd8cb3e9ac268a3bcb793293c81f28315
    role: context
  - path: scripts/adhoc/gtdb_batch_curation_20261115.py
    sha256: bc488158440416db558133cfc0609111d96f46123b66c22efbafcfef1934d144
    role: context
  - path: scripts/adhoc/report_gtdb_batch_routes_20261115.py
    sha256: 2d4732edafccba24741b728b9e672ca7fada5e50d8220162a9ccf3c5d8d875ef
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/__init__.py
    sha256: c003d906fef500e765c59c8f15ee821054e26c43e59a1be70dbc23c33f8aae66
    role: context
  - path: src/communitymech/curate/__init__.py
    sha256: a591b57cbf73ef2ddb0da6d0b7be0dd784258115ae20cf4883f6f379bcad9324
    role: context
  - path: src/communitymech/curate/curation_event.py
    sha256: 58ebdb58ac39d7a319156ec735db9ef2e9afb4c7350613039ad9dc49d65a5afc
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: 7e0a621831b28ac0f718a29c22af8052f93e006012fff77e11d92849e4852c45
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c6f6e4a5cf42e450cf55d8fcb12817591c736198e24bcd217142b4f86712b4c3
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11
    role: context
  - path: src/communitymech/validation/write_validated.py
    sha256: d19dd3b1e46856b4de67ecc17fc856aaa1034a9a97259cab3bbd54c3891fb019
    role: context
  - path: src/communitymech/validators/__init__.py
    sha256: 975d33a39c8e7173d25aa0de711f25a19158228ecfd837908c829b3f9f14cf93
    role: context
  - path: src/communitymech/validators/ncbi_domain.py
    sha256: b1e7ffc3c35c237e36c2c19fab42f1d42a14161397de9c5e726ed85897f1e262
    role: context
  - path: tests/test_causal_review_batch101.py
    sha256: 22375a34b732f5a1123e1322bffef050202b31b34d9b1f21fa444ab87975c0f4
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000436
  path: kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
  selector: taxonomy[0:8].taxon_term.gtdb_classification; taxonomy[0:8].taxon_term.gtdb_grounding_status;
    appended native curation_history
  label: Eight genus reference correspondences; shrimp SynCom panel and unresolved
    isolate identities retained
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: Only the eight taxonomy GTDB blocks/statuses, actual guarded application
    and appended history, source-population interpretation and eight scoped native
    checks. This does not identify the experimental genomes, infer individual protection
    mechanisms or resolve the missing assay protocol.
  selection: CommunityMech:000436 is the first whole-record canary in the prepared
    Shrimp/Thermophilic/Sahara lane. Records 416 and 494 remain unapplied by this
    workflow. This diagnostic covers only record 436; complete input checkpoints and
    strict historical admission precede its publication and any later applications.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000436
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000436-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never validate kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000436-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
    --out .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000436-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000436-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000436-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000436-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never validate-history history/records/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000436-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Ground eight genus reference descriptors while preserving the shrimp
    SynCom panel and unresolved stock identities.' --details 'The native rank-level
    crosswalk supplies eight genus reference blocks and statuses, with two appended
    native events. Filtered reference counts are Ruegeria 30/44, Microbacterium 591/591,
    Tenacibaculum 264/270, Demequina 88/88, Exiguobacterium_A 49/83, Bacillus 4981/8737,
    Paracoccus 486/486 and Epibacterium 134/134 from the source Tritonibacter descriptor.
    Exiguobacterium_A is a non-type majority, with 34 references in the type-bearing
    alternative; its suffix does not identify the unnamed study isolate. These populations
    are not shrimp abundances, experimental isolate counts, protective-effect estimates
    or independent stock-genome assignments. Preserve all eight source genera and
    absent species/strain identifiers, four SynCom variants and their memberships,
    historical missing-crosswalk notes, three enrichment media, source quotations,
    old history and the single community-level protection node without genus-to-pathogen
    edges. The retained abstract'"'"'s greater-than-68-percent survival statement
    concerns enriched consortia, not a newly generalized SynCom estimate. Exact strain
    names, assemblies, medium recipes, member ratios and challenge timing remain unresolved.
    Captured closed issues 1105 and 1106 document historical missing-crosswalk and
    unsupported-timing repairs; their closure does not resolve the current OPEN stock/protocol
    discussion. The crosswalk release is unestablished; NCBI authority uses file identity/stat,
    not a database content digest. Preserve batch 101'"'"'s immutable unchanged/zero-event
    ledger and all current biological predicates. This partial technical correction
    does not complete scientific review, measured references, generated products or
    corpus QC. Actual apply receipt .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-applied-001/receipt.json
    sha256:7ace8f2a47468e00800ee6d0478f3551b78b16f63d0717630a4ff7b597ae3b7b.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000436-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000436
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000436-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000436-schema
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-schema-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-strict
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-strict-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-gtdb
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-gtdb-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-domain
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-domain-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-scalars
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-scalars-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-history
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-history-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-new-history
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-new-history-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-terms
  kind: validation
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-terms-001/native.log
  accessed_at: '2026-11-16T00:04:01.198096Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000436-primary
  kind: primary_source
  reference: references_cache/doi_10.1016_j.aquaculture.2025.743350.md
  locator: 'Complete retained abstract: three gut enrichment media, genus rosters,
    eight corresponding isolates, four SynCom variants and shrimp survival statements.'
  support: supports
  summary: The abstract supports the source genus roster and construction of a four-variant
    panel. It does not provide exact strain identities or complete culture/challenge
    conditions. The enriched-consortium survival statement remains distinct from the
    SynCom results.
  accessed_at: '2026-11-16T00:04:01.198096Z'
- evidence_id: 000436-database
  kind: database
  reference: reports/gtdb-shrimp-thermophilic-sahara-20261115/436-source-evidence-001.json
  locator: 'All eight selected occurrences: full native rank-level results, filtered
    numerators/denominators, original descriptors, NCBI genus identity, warning and
    primary locators.'
  support: supports
  summary: The native ncbi_rank_g routes support eight reference blocks. Exiguobacterium_A
    49/83 is explicitly non-type; Bacillus 4981/8737 spans 44 clades. No result assigns
    an experimental stock genome or proves individual protection.
  accessed_at: '2026-11-16T00:04:01.198096Z'
- evidence_id: 000436-application
  kind: record_content
  reference: .temp/gtdb-shrimp-thermophilic-sahara-20261115/436-applied-001/receipt.json
  locator: Actual applied flag, frozen 261941 revision, stage 598128e4, before f23b26c7,
    after 4152f796 and captured native inputs.
  support: supports
  summary: The guarded application persists exactly eight reference blocks/statuses
    and two native events. Original stock/source content, biological assertions, historical
    notes and old history are preserved.
  accessed_at: '2026-11-16T00:04:01.198096Z'
- evidence_id: 000436-scientific-boundary
  kind: record_content
  reference: kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml
  locator: OPEN shrimp_vibrio_syncom_strains_and_challenge_protocol discussion; four
    SynCom memberships; single community-level protection node.
  support: context_only
  summary: Reference correspondence does not resolve species/stock names, assemblies,
    ratios, medium recipes or challenge timing, and does not create genus-to-pathogen
    causal edges.
  accessed_at: '2026-11-16T00:04:01.198096Z'
- evidence_id: 000436-historical-boundary
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261007-four-records-batch101.yaml
  locator: Original record 436 unchanged/zero-event row and full captured batch 101
    caller.
  support: context_only
  summary: The original ledger remains immutable. Strict admission must protect all
    current biological predicates and other records' successor chains while admitting
    only the exact reference-only transition.
  accessed_at: '2026-11-16T00:04:01.198096Z'
- evidence_id: 000436-closed-crosswalk-repair
  kind: prior_review
  reference: .temp/phase2-schema-20261115/shrimp436-issue1105-snapshot-001.log
  locator: Captured issue identity, CLOSED state and historical missing-crosswalk
    note repair.
  support: context_only
  summary: Historical notes remain preserved as the original pass's limits; this closed
    repair is not a species/strain identification or current scientific clearance.
  accessed_at: '2026-11-16T00:04:01.198096Z'
- evidence_id: 000436-closed-timing-repair
  kind: prior_review
  reference: .temp/phase2-schema-20261115/source-issue1106-snapshot-001.log
  locator: Captured issue identity, CLOSED state and unsupported challenge-timing
    repair.
  support: context_only
  summary: Do not restore unsupported timing. The current OPEN protocol discussion
    remains unresolved despite this historical issue closure.
  accessed_at: '2026-11-16T00:04:01.198096Z'
assessments:
- assessment_id: 000436-source
  area: grounding
  topic: Source genera and four SynCom variants remain distinct from reference genome
    placement
  outcome: supported
  target_ids:
  - CommunityMech:000436
  evidence_ids:
  - 000436-primary
  - 000436-database
  - 000436-terms
  - 000436-scientific-boundary
  summary: The primary abstract supports eight genus-level isolates and four variants
    with the retained memberships. Generic reference correspondences preserve source
    genera and absent strain/species identifiers; neither suffixes nor same-name blocks
    independently identify the study genomes.
- assessment_id: 000436-population
  area: grounding
  topic: Eight filtered genus populations retain majority and nomenclature limits
  outcome: supported
  target_ids:
  - CommunityMech:000436
  evidence_ids:
  - 000436-database
  - 000436-gtdb
  - 000436-domain
  - 000436-primary
  summary: The eight native populations are 30/44, 591/591, 264/270, 88/88, 49/83,
    4981/8737, 486/486 and 134/134 in taxonomy order. The non-type Exiguobacterium_A
    majority and split Bacillus population remain explicit; Tritonibacter-to-Epibacterium
    is reference nomenclature. No counts are interpreted as isolates, abundance, protective
    effect or stock-genome assignments.
- assessment_id: 000436-provenance
  area: provenance
  topic: Actual application and eight native checks preserve source and historical
    boundaries
  outcome: supported
  target_ids:
  - CommunityMech:000436
  evidence_ids:
  - 000436-application
  - 000436-schema
  - 000436-strict
  - 000436-scalars
  - 000436-new-history
  - 000436-history
  - 000436-terms
  - 000436-historical-boundary
  - 000436-closed-crosswalk-repair
  - 000436-closed-timing-repair
  - 000436-scientific-boundary
  summary: Actual f23b-to-4152 persistence, two native inline events, one new sidecar
    and eight completed native commands bind frozen 261941 execution. Closed historical
    repairs and the current OPEN stock/protocol discussion remain distinct. Exact
    original ledger, current biology and old history are protected; strict admission,
    measured references, products and full QC remain separate.
findings: []
actions: []
limitations:
- Partial technical diagnostic with scientific_review:false. Native checks do not
  establish full scientific review, measured snippet validation, current generated
  products, aggregate QC or campaign completion.
- Coverage is the complete retained primary abstract, whole canonical record, authored
  source assessment and batch 101 context. No new full article, supplementary material,
  original challenge data or study assembly was acquired or audited. Retained source-access
  limitations are not a fresh exhaustive claim of absence.
- The abstract describes eight corresponding isolates and four SynCom variants but
  does not expose exact species, strain codes, assemblies, mixing ratios, kanamycin
  concentration or challenge timing. The current OPEN stock/protocol discussion remains
  unresolved.
- Filtered reference populations are Ruegeria 30/44, Microbacterium 591/591, Tenacibaculum
  264/270, Demequina 88/88, Exiguobacterium_A 49/83, Bacillus 4981/8737, Paracoccus
  486/486 and Epibacterium 134/134. These denominators are not shrimp abundances,
  experimental isolate counts, replicates or protective-effect estimates. Fractions
  0.682, 0.978, 0.59 and 0.57 are native rounded values.
- 'Exiguobacterium_A is a non-type majority: 49 references versus 34 in the type-bearing
  alternative. Bacillus spans 44 native clades with a 0.57 majority. These results
  do not establish which clade contains either unnamed study isolate. Preserve the
  preferred source genera and the native warning in source evidence.'
- Tritonibacter-to-Epibacterium is reference nomenclature correspondence. It neither
  formally renames the source isolate nor independently links a reference assembly
  to the experimental strain. All source names, NCBI descriptors and historical missing-crosswalk
  notes remain unchanged.
- The abstract's greater-than-68-percent survival statement concerns enriched consortia,
  not a newly generalized effect estimate for every SynCom. Preserve the existing
  community-level protection node, no genus-to-pathogen edges, four variant memberships,
  three enrichment media and all source quotations without adding individual causal
  claims.
- Captured issues 1105 and 1106 are CLOSED historical repairs of missing-crosswalk
  wording and unsupported timing. Their closure does not resolve the current OPEN
  stock/protocol discussion or constitute approval of this new mapping. Both exact
  snapshots are additional captured review inputs through the unchanged provenance
  wrapper.
- Actual staging, guarded application and all eight native commands ran at frozen
  M5 revision 261941db9aa5c359dc7599f28e4648a6c9723396 with Python 3.13.2. Eight free
  plans preceded eight serial actual gates. The two native events report eight changed
  descriptors and one new sidecar records the actual application receipt.
- Crosswalk 761d5537 identifies exact bytes with an unestablished release. NCBI authority
  provenance is file identity/stat rather than a full database digest. Preserve batch
  101's immutable historical unchanged/zero-event row, all current biological predicates,
  caches and other three records' successor chains. The complete input checkpoint
  precedes caller changes.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/pull/2925
- https://github.com/CultureBotAI/CommunityMech/issues/1105
- https://github.com/CultureBotAI/CommunityMech/issues/1106
```
