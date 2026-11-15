# Current M5 reference comparison and issue ownership

The fresh M5 comparison at `c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a`
processed **549/549 records** on `2026-11-15T05:06:30Z–05:07:08Z`.
It inspected **10,837 snippet surfaces** and made **10,836 actual native
substring comparisons**: 10,728 matched and 108 mismatched. One occurrence
had no source content and could not be compared. Native and process exits were
**1**, with **109 issues across 17 records**. Measurement validity passed;
record traversal completed; assertion coverage and validation did not pass.
All measured input hashes remained unchanged.

The [verified JSON](code006-reference-measurement.json) and
[549-record table](code006-reference-measurement.md) retain the exact counters,
native dependency hashes and failed result. The misleading native label
`Total checks: 109` counts retained issues, not the 10,836 actual comparisons.
Lexical matching is not a scientific verdict or a substitute for full QC.

The same persisted launcher first ran a plan selecting all 549 Git-declared
records and observed `.venv/bin/python --version` as **3.13.2**. Its real Asgard
canary compared 11/11 snippets in each of the control, mutation and restoration
cases, with native exits **0/1/0**. The changed `[NiFe]` token was detected;
control and restoration input files were byte-identical. The canary receipt
SHA-256 is `ae3a4ab683e8b511d84622771b9190461fdbde3c6f8fb4c6a2a7340e6a790da1`.
No acquisition, enrichment, source rewriting or cache saving was allowed.

The independent process-exit artifact is the actual launcher file
`.temp/phase2-schema-20261115/code006-reference-corpus-001.exit`, containing
`1` followed by a newline, SHA-256
`4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`.
The exporter's `process.exit` key is a logical artifact label for that file.
Raw measurement, launcher, plan and canary artifacts are retained on M5 and
hash-verified in the local mirror; no new `corpus-001/process.exit` path is implied.

The [current ownership reconciliation](code006-reference-owners.json) verifies
every failing occurrence against the immutable
[historical ledger](../phase2-reference-blockers-20261115/reference-blockers-20185647.json).
All 109 match in record bytes, field path, reference, native class, status,
comparison flag, cache path, cache bytes and content type. Therefore existing
owners apply to these exact occurrences. Their issue-state snapshots remain
historical; this reconciliation does not claim a fresh GitHub state audit.

| Record | Native issues | Existing owner |
|---|---:|---|
| Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism | 4 | [#703](https://github.com/CultureBotAI/CommunityMech/issues/703) |
| Bayan_Obo_REE_Tailings_Consortium | 1 | [#1261](https://github.com/CultureBotAI/CommunityMech/issues/1261), [#1093](https://github.com/CultureBotAI/CommunityMech/issues/1093) |
| Caragana_Wheat_Drought_SynCom15 | 15 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Choysum_SynLAV_DEHP_Rhizobacterial_SynCom | 8 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Coscinodiscus_Synthetic_Community | 3 | [#596](https://github.com/CultureBotAI/CommunityMech/issues/596) |
| Fucoidan_Seven_Degrader_Combinatorial_SynCom | 15 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom | 12 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| LBNL_Switchgrass_Soil_SynCom16 | 2 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Mixed_Gallium_LED_Recovery_Consortium | 1 | [#1618](https://github.com/CultureBotAI/CommunityMech/issues/1618) |
| Nasal_SynCom_C_Bioreactor | 11 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Panzhihua_Vanadium_Titanium_Tailings | 1 | [#2841](https://github.com/CultureBotAI/CommunityMech/issues/2841), [#1683](https://github.com/CultureBotAI/CommunityMech/issues/1683), [#1680](https://github.com/CultureBotAI/CommunityMech/issues/1680) |
| Prymnesium_Parvum_B12_Limited_SynCom | 15 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium | 5 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom | 4 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| SynCom_ARC_Peanut_Aflatoxin_Nodulation | 9 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| Synechococcus_Pseudomonas_PhotoPHA_DNT_Coculture | 1 | [#1863](https://github.com/CultureBotAI/CommunityMech/issues/1863) |
| Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium | 2 | [#2793](https://github.com/CultureBotAI/CommunityMech/issues/2793) |

The sole noncomparison is Bayan Obo
`ecological_interactions[0].evidence[0].snippet`, DOI
`10.1016/j.cej.2024.153492`. Native loading found the retained cache, but its
`content_type` is `unavailable` and `has_content` is false; matcher and substring
calls are zero. This is a source-content boundary, not an annotation omission
or proof that the paper is unavailable everywhere. Its exact cache SHA-256 is
`7a9cbc31e15a21e73c64d1aceb8d60e635ce10a9ac724f31c47d2599d2817cf4`.

The six Phase 2 targets have **270/270 actual comparisons**, 268 matches and
two known switchgrass Table S1 mismatches under #1996. All six failing
SupportingReference occurrences across the full corpus were actually compared;
the other 103 native issues are on EvidenceItem surfaces. No issue is closed
and no scientific scope is expanded by this accounting.

Reproduce the read-only reconciliation with
`python scripts/adhoc/reconcile_code006_reference_owners_20261115.py`.
Its pinned summary/raw/ledger checks and 11 focused controls reject changed
occurrence paths, references, classes, cache identities, record bytes,
duplicate rows and inconsistent counters. The historical ledger is unchanged.
