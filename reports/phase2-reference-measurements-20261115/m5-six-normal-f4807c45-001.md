# Six Phase 2 records: measured native references on M5

On 2026-11-16 at 00:59:17–00:59:19 UTC, the six Phase 2 records below completed
the native reference measurement at commit
`f4807c459e0986ff9d2aa41365f393b1e9ba4d2d`. All 270 snippet occurrences were
actually compared and matched. There were no native issues, measurement
errors, omitted occurrences or input drift. This is a scoped quotation-matching
result; it does not certify scientific interpretation or complete corpus QC.

| Record | Snippet surfaces | Actual comparisons | Matched | Native issues |
| --- | ---: | ---: | ---: | ---: |
| 000025 · EcoFAB Ring Trial | 72 | 72 | 72 | 0 |
| 000087 · LBNL Switchgrass | 37 | 37 | 37 | 0 |
| 000088 · LBNL Brachypodium Drought | 63 | 63 | 63 | 0 |
| 000122 · LBNL Human Gut | 44 | 44 | 44 | 0 |
| 000515 · Yolo Soil Dopamine | 14 | 14 | 14 | 0 |
| 000516 · Brachypodium Dopamine SynCom | 40 | 40 | 40 | 0 |
| Total | 270 | 270 | 270 | 0 |

The [one-record normal Switchgrass canary](../supplement-normal-coverage-f4807c45-20261116.md)
preceded this batch on the same M5 checkout, native recorder, environment,
`just reference-assertion-coverage` recipe, normal configuration and private
output root. Its actual 37/37 result and persisted source identities were
verified before the six-record free plan and actual invocation. The plan
selected the exact six paths below. This does not establish behavior under
concurrent load or coverage of other records.

The recipe invokes the native reference CLI with existing caches and
`--no-full-text`, without acquisition, source writes or canonical changes.
The actual invocation uses M5's `/opt/homebrew/bin/just` and retains
`UV_NO_SYNC=true`, `UV_OFFLINE=true`, `JUST_NO_DOTENV=true`,
`PYTHONDONTWRITEBYTECODE=1` and the existing local source-data root. It runs on
the named M5 branch `fix/supplement-adoption-m5-1996-20261115`; the adjacent
original config backup is the only untracked file recorded by the inner
launcher. The lock hash is
`1e1374a77207de170502a89ea7eebcb018d65daac8b0faecc39988d955f3df62`.

The native measurement records 270 excerpt-validator invocations, matcher
calls, substring calls and compared substring parts; it records zero
title-only validations. Its 549 declared record paths describe the repository
inventory. Only the six selected records were processed. All 1,502 captured
input hashes were independently rechecked after the evidence was mirrored to
the local checkout. The three selected supplement identities are unchanged
from the verified Switchgrass canary; all other matching uses the retained
article sources.

| Artifact under `.temp/supplement-adoption-1996-20261115/phase2-six-normal-coverage-m5-001/` | SHA256 |
| --- | --- |
| `started.json` | `c8f6029e7a415a8e921c0be6938e99757566c56e0611750aa0f57d09ad78bfc0` |
| `receipt.json` | `4daa4adfa9c34f1084246a894e7140d02dc435d3aa20ba94aa05f3365311a8b1` |
| `measurement.json` | `7cdacb71b4d176cdab89d9cbf0d9be8d296f5d5e30dc82279c61bb4f901ba052` |
| `measurement.log` | `c71744d7c149ebcbed59236948d941177d9e1a8dfd896e490948106fe48eef50` |

The native plan and actual recorder artifacts are retained under
`.temp/phase2-schema-20261115/`, separately from the outer SSH launch records:

| Native M5 recorder | Exit | Receipt SHA256 | Raw log SHA256 |
| --- | ---: | --- | --- |
| `supplement-phase2-six-coverage-plan-m5-001` | 0 | `7c25e2b4781138a183572826adfc4f36d07f225dd5ab791b9f8641097da81854` | `8838d1eaa29ebbf3563afb24a790a8ea65ab4ca197406c399a7ef82becd6d7fa` |
| `supplement-phase2-six-coverage-actual-m5-001` | 0 | `c7b4e6790f7c4cdb4bf401ca165ccfd178415285f5bf1f54dd3e7d522b3702b7` | `eed39671be5892f5e13784ab40618e76911c56e698412c844223689c756c4109` |

Exact selected canonical inputs under `kb/communities/`:

| File | SHA256 |
| --- | --- |
| `EcoFAB_Ring_Trial_SynCom17.yaml` | `7f5b0122647382d048e0b750d1c5f324b32f74868685d111db39d588c735b339` |
| `LBNL_Switchgrass_Soil_SynCom16.yaml` | `bcc2759c9da7c4059330726a1b154df600ec394d1106be2dcc1f4d247eed5eb9` |
| `LBNL_Brachypodium_Drought_SynCom15.yaml` | `ee609781b7adaa7305ad9cc16c61aa8f7eb8ac3887f92a15ead26d25f4b3592e` |
| `LBNL_Human_Gut_Interaction_SynCom.yaml` | `c8c508709645f7a90090f0e3e69a5bcd5757f89b624343abcef8ad9e412be34e` |
| `Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml` | `669893f1ffdefda67d443f528520c3c43fab1619c09e5a6b09cdf1621172a368` |
| `Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml` | `304702c684faedb244d678e628ec174851dbdcafe46128eab86d824798e0482a` |

Previous failed or partial measurements remain immutable. This run does not
erase the unresolved Switchgrass Methods/Table S1 scientific discrepancy
under issue1548, certify any unsaved review draft, or establish a full-QC or
549-record reference pass. It does not change any review or curation status.
