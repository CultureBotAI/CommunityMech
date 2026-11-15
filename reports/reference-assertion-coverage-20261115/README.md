# Measured native reference coverage on M5

These are cache-only native CLI measurements. No acquisition, enrichment or input writes were allowed. Actual comparisons are distinct from retained issues, skipped prefixes and unannotated snippets. Lexical comparison does not establish scientific truth.

| Attempt / case | Records completed / selected | Snippet surfaces | Occurrences compared | Native issues | Measurement valid | Native exit |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| reference-coverage-m5-canary-001 / control | 1/1 | 11 | 11 | 0 | True | 0 |
| reference-coverage-m5-canary-001 / mutation | 1/1 | 11 | 11 | 1 | True | 1 |
| reference-coverage-m5-canary-001 / restoration | 1/1 | 11 | 11 | 0 | True | 0 |
| reference-coverage-m5-corpus-001 / measurement | 156/549 | 2812 | 2713 | 27 | False | 1 |
| reference-coverage-m5-canary-002 / control | 1/1 | 11 | 11 | 0 | True | 0 |
| reference-coverage-m5-canary-002 / mutation | 1/1 | 11 | 11 | 1 | True | 1 |
| reference-coverage-m5-canary-002 / restoration | 1/1 | 11 | 11 | 0 | True | 0 |
| reference-coverage-m5-ratio-canary-001 / measurement | 1/1 | 19 | 19 | 0 | True | 0 |
| reference-coverage-m5-corpus-002 / measurement | 549/549 | 10695 | 10172 | 103 | True | 1 |

## reference-coverage-m5-canary-001

Exact code and declared-record revision: `1e5052c96c00f0e85fc66b191579e71ffed60533`. Input hashes unchanged: **True**. Wrapper exit: **0**.

control: assertion coverage complete = **True**; native validation passed = **True**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 11 |

mutation: assertion coverage complete = **True**; native validation passed = **False**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 10 |
| mismatched | 1 |

restoration: assertion coverage complete = **True**; native validation passed = **True**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 11 |


## reference-coverage-m5-corpus-001

Exact code and declared-record revision: `1e5052c96c00f0e85fc66b191579e71ffed60533`. Input hashes unchanged: **True**. Wrapper exit: **2**.

measurement: assertion coverage complete = **False**; native validation passed = **False**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 2687 |
| mismatched | 26 |
| no_content | 1 |
| unannotated_excerpt | 98 |


## reference-coverage-m5-canary-002

Exact code and declared-record revision: `9ba3eefc1be7a9f8bb9f0b9399f69429c16e44fc`. Input hashes unchanged: **True**. Wrapper exit: **0**.

control: assertion coverage complete = **True**; native validation passed = **True**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 11 |

mutation: assertion coverage complete = **True**; native validation passed = **False**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 10 |
| mismatched | 1 |

restoration: assertion coverage complete = **True**; native validation passed = **True**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 11 |


## reference-coverage-m5-ratio-canary-001

Exact code and declared-record revision: `9ba3eefc1be7a9f8bb9f0b9399f69429c16e44fc`. Input hashes unchanged: **True**. Wrapper exit: **0**.

measurement: assertion coverage complete = **True**; native validation passed = **True**.

| Occurrence outcome | Count |
| --- | ---: |
| matched | 19 |


## reference-coverage-m5-corpus-002

Exact code and declared-record revision: `9ba3eefc1be7a9f8bb9f0b9399f69429c16e44fc`. Input hashes unchanged: **True**. Wrapper exit: **1**.

measurement: assertion coverage complete = **False**; native validation passed = **False**.

| Record with native findings | Issues | Prior tracking owner |
| --- | ---: | --- |
| Caragana_Wheat_Drought_SynCom15 | 15 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Prymnesium_Parvum_B12_Limited_SynCom | 15 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Fucoidan_Seven_Degrader_Combinatorial_SynCom | 14 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom | 12 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Nasal_SynCom_C_Bioreactor | 11 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| SynCom_ARC_Peanut_Aflatoxin_Nodulation | 9 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Choysum_SynLAV_DEHP_Rhizobacterial_SynCom | 8 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium | 5 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom | 4 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism | 3 | [#703](https://github.com/CultureBotAI/CommunityMech/issues/703) |
| Coscinodiscus_Synthetic_Community | 3 | [#596](https://github.com/CultureBotAI/CommunityMech/issues/596) |
| Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium | 2 | [#2793](https://github.com/CultureBotAI/CommunityMech/issues/2793) |
| Bayan_Obo_REE_Tailings_Consortium | 1 | [#1261](https://github.com/CultureBotAI/CommunityMech/issues/1261) |
| Mixed_Gallium_LED_Recovery_Consortium | 1 | [#1618](https://github.com/CultureBotAI/CommunityMech/issues/1618) |

| Occurrence outcome | Count |
| --- | ---: |
| matched | 10070 |
| mismatched | 102 |
| no_content | 1 |
| unannotated_excerpt | 522 |

## Boundaries and unresolved owners

SupportingReference's unannotated snippets remain owned by [#476](https://github.com/CultureBotAI/CommunityMech/issues/476). BIOPROJECT skips are configured exclusions, not successful text comparisons. Missing content and substring mismatches remain native findings, not proof that a scientific claim is false. Supplement-specific routing remains owned by [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996). No supplement or alternative source was substituted.

The first corpus attempt is retained as incomplete/invalid: YAML1.1 inventory loading disagreed with the native YAML1.2 parser ([#2799](https://github.com/CultureBotAI/CommunityMech/issues/2799)). Its partial counters must not be combined with a later full attempt. The native parser correction retained record/cache bytes and matching rules. Reference-identity binding is guarded by [#2795](https://github.com/CultureBotAI/CommunityMech/issues/2795).

The adjacent JSON contains per-record status counts and SHA256 hashes of the private raw receipts/logs. Raw source excerpts, reference values and local invocation paths are deliberately omitted here.
Tracking owners are carried from the retained earlier triage only where the record and finding count agree; this is routing metadata, not a new scientific disposition or a live issue-state claim.
The JSON also hashes the retained Python-version receipt, exact Git-bound launch plan and same-path nohup/just output for each attempt.

Verified runtime: Python 3.13.2 on M5.
Complete corpus native prefix skips: 0; title-only validations: 0; uncompared SupportingReference surfaces: 522.

