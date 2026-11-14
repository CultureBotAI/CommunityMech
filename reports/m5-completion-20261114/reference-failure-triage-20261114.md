# Native reference failure triage: completed C2 sweep

The native reference sweep finished at **2026-11-14 23:37:48 UTC**, exit **1**.
The [final reconciled inventory](reference-sweep-final.json) contains all
**549 expected records** at `e9ae9dee132ab210c87f76460c5d6247af9ea99c`,
with no missing, unexpected, duplicate, or incomplete records. There are
**535 native passes and 14 records with 103 errors**: 102 substring mismatches
and one unavailable source. These are validator outcomes, not whole-record
scientific verdicts. Older checkpoint observations below remain preserved.

The immutable private log
`.temp/m5-completion-20261114/final-c2-reference-parser-input-final.log`
is 1,060,795 bytes, SHA-256
`a4f5aa46520a8b350f3054a6ed5783bd183bbc6922bd629bb32b267834e4a868`.
The private `final-c2-reference-summary-final.json` has SHA-256
`0f2fb18783972428e2f2b3e07ca90b4890acc5778217a67b1d3224a2d785e45c`.
The exact expected Git inventory has SHA-256
`34115cfa848fb168ac24f5e61cb4cb6cffc94230d881fe2f2f74db56f7759f0b`.

| Record under `kb/communities/` (`.yaml`) | Errors | Issue ownership |
|---|---:|---|
| `Caragana_Wheat_Drought_SynCom15` | 15 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `Prymnesium_Parvum_B12_Limited_SynCom` | 15 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `Fucoidan_Seven_Degrader_Combinatorial_SynCom` | 14 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), same routing requirement; exact earlier recurrence preserved in closed [#1469](https://github.com/CultureBotAI/CommunityMech/issues/1469) |
| `Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom` | 12 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `Nasal_SynCom_C_Bioreactor` | 11 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `SynCom_ARC_Peanut_Aflatoxin_Nodulation` | 9 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `Choysum_SynLAV_DEHP_Rhizobacterial_SynCom` | 8 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium` | 5 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom` | 4 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), supplement routing |
| `Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism` | 3 | [#703](https://github.com/CultureBotAI/CommunityMech/issues/703), full-source cache discovery |
| `Coscinodiscus_Synthetic_Community` | 3 | [#596](https://github.com/CultureBotAI/CommunityMech/issues/596), abstract-only selected source |
| `Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium` | 2 | New [#2793](https://github.com/CultureBotAI/CommunityMech/issues/2793), unmatched quotations requiring primary-source verification; broader roles remain [#1961](https://github.com/CultureBotAI/CommunityMech/issues/1961) |
| `Bayan_Obo_REE_Tailings_Consortium` | 1 | [#1261](https://github.com/CultureBotAI/CommunityMech/issues/1261), source/identity scope; [#1093](https://github.com/CultureBotAI/CommunityMech/issues/1093), unavailable stub |
| `Mixed_Gallium_LED_Recovery_Consortium` | 1 | [#1618](https://github.com/CultureBotAI/CommunityMech/issues/1618), retained non-graph source mismatch; [#1617](https://github.com/CultureBotAI/CommunityMech/issues/1617), provenance |
| **Total** | **103** | **13 known recurrence records; one newly filed exact-quotation finding** |

All 79 occurrences explicitly enumerated in #1996 appeared, plus Fucoidan's
14 previously documented supplementary mismatches. No normal native pass is
claimed for those records. All cache/hash statements below identify the moment
inspected; runtime source preservation and the exact overlap with the six saved
reviews are separate audits using the [cache-input union](review-cache-inputs.md).

## Earlier checkpoint observations

Read-only triage completed on **2026-11-14 at 23:18 UTC**. The active M5
`just qc-references` run started at commit
`e9ae9dee132ab210c87f76460c5d6247af9ea99c`; the checkout still reported that
HEAD during this inspection. This handoff covers the first four records with
native errors in the retained snapshot. It is not a final corpus result or an
extension of the four-record scientific curation scope.

The native log is `.temp/m5-completion-20261114/final-c2-qc-references.log`.
The immutable diagnostic snapshot is
`.temp/m5-completion-20261114/final-c2-reference-parser-input-002.log`
(887,378 bytes; SHA-256
`7f86fb1b8f98898137840e0733e7609689db08d88216e1bec39a0846cd0cf025`).
Its companion `final-c2-reference-summary-002.json` has SHA-256
`3c88ae437b10c8d77cb8e2ebab621ff1e6adc58a6af799d1ede403a47e06fe13`.
That snapshot has 113 started records, 112 completed records, and 27 retained
errors across four records. Native `Total checks` counts retained findings,
not inspected excerpts; zero is not an excerpt-coverage measurement.

| Record | Exact native failure scope | Existing owner and disposition |
|---|---|---|
| `CommunityMech:000142`, `Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism` | Three substring errors against `PMID:16782812`: `ecological_interactions[2].evidence[0].snippet`, `growth_media[0].evidence[0].snippet`, and `growth_media[0].evidence[1].snippet`; snapshot lines 8352–8367. | [#703](https://github.com/CultureBotAI/CommunityMech/issues/703), open. Exact previously recorded cache-discovery failure; no new issue. |
| `CommunityMech:000005`, `Bayan_Obo_REE_Tailings_Consortium` | One `No content available` error against `doi:10.1016/j.cej.2024.153492`, at `ecological_interactions[0].evidence[0].snippet`; lines 8425–8434. | [#1261](https://github.com/CultureBotAI/CommunityMech/issues/1261), open, owns source/identity uncertainty; [#1093](https://github.com/CultureBotAI/CommunityMech/issues/1093), open, owns unavailable cache stubs. Preserve both distinctions. |
| `CommunityMech:000456`, `Caragana_Wheat_Drought_SynCom15` | Fifteen substring errors against `PMID:41634815`, at `taxonomy[0..14].evidence[0].snippet`, the CM-1 through CM-15 table excerpts; lines 8729–8780. | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), open, explicitly enumerates these 15 supplement-only failures. No new issue. |
| `CommunityMech:000403`, `Choysum_SynLAV_DEHP_Rhizobacterial_SynCom` | Eight substring errors against `PMID:42482240`: `taxonomy[3..4].evidence[0].snippet`, `ecological_interactions[0].evidence[0..4].snippet`, and `growth_media[0].evidence[0].snippet`; lines 8930–8960. | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), open, explicitly enumerates these eight supplement-only failures. No new issue. |

The Bacteroides/Methanobrevibacter excerpts occur in the retained full source
`references_cache/pmc_full_pmid_16782812.txt`: Figure 1 caption at line 168 and
Methods at line 228. The canonical `PMID_16782812.txt` is abstract-only.
The earlier [batch-6 diagnostic](../causal_graph_review/validation-20261005-batch6.json)
records exactly the same three native errors and names #703; its temporary
canonical-name check is historical evidence, not a check repeated here. Both
current source hashes match the [October 21 review](../../reviews/structured/20261021T095437Z-bacteroides-methanobrevibacter-mutualism-record/review.yaml).

For Bayan Obo, the current Markdown cache still declares
`content_type: unavailable` and has an empty `## Content` section. Its sole
observed difference from the tested commit is `full_text_attempted: true`.
That flag records an attempt, not successful retrieval or exhaustive global
source unavailability. No new provider request was made during this triage.

Caragana and Choysum record, article, and supplement hashes match their saved
October 21 reviews exactly:
[Caragana](../../reviews/structured/20261021T161103Z-caragana-wheat-drought-syncom15-record/review.yaml)
and [Choysum](../../reviews/structured/20261021T192924Z-choysum-synlav-record/review.yaml).
Both reviews visibly retain the same native failures. The earlier
[source-boundary audit](../reference_cache_separation/20261013-1994/snippet-audit.json)
locates these excerpts in separate supplements, including the Caragana S7
roster. Its explicit supplement-matcher diagnostics are not normal native
reference passes. Preserve source separation; do not concatenate supplementary
text into article caches or weaken matching.

## Current input identities

These SHA-256 values were read from M5 after the failed record checks. They
are current-cache observations, not saved failure-time cache snapshots. The
active aggregate may make other cache changes after this inspection.

| Path | SHA-256 |
|---|---|
| `kb/communities/Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism.yaml` | `ad17adfb48af6e2ca459d02eebd9cded64948ad0085a81c284fc6f21df8ae584` |
| `references_cache/PMID_16782812.txt` | `dc3d8632ec77c3f6af3925eb04470a5343a9a88ff1abbf8b4cafd6d2fa7a7053` |
| `references_cache/pmc_full_pmid_16782812.txt` | `eab16fa2e50eababee737122f313bc3ee8e1e181eb8e4f5b38ad68e1edd1c8d7` |
| `kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml` | `655ff223cc2775123bf63fe23caa3445c1775988dd1d292a7a9edf79c4959a3f` |
| `references_cache/doi_10.1016_j.cej.2024.153492.md`, current M5 | `b2f70f76646ef4696850712dd6193f86fa1dabf2f62a4efa1fa8527544281a30` |
| Same DOI cache at tested commit | `7a9cbc31e15a21e73c64d1aceb8d60e635ce10a9ac724f31c47d2599d2817cf4` |
| `kb/communities/Caragana_Wheat_Drought_SynCom15.yaml` | `5fe2262acd9eb4de81a2f454ac2954ab5d347a1ce7915d1cdcaf73fc584ff678` |
| `references_cache/PMID_41634815.txt` | `0dc288d29a3f599742315a0034ddf4aad7c0f6523c898bd0e7f54091f5131037` |
| `references_cache/PMID_41634815.supplement.md` | `99cbaf310c20323f40cf7005ad997da21098e7ef867c86336a2f0affd8e929a9` |
| `kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | `23c898adcb069d4f4f36cc49783674e02fa33a814b11cdc8a3a7ed7f84f74239` |
| `references_cache/PMID_42482240.txt` | `fa818b4fb415527b08960aeb8aa118fef46555bc01b18126eb99b66dbae61210` |
| `references_cache/PMID_42482240.supplement.md` | `45614f71bd112451ce0a5bb4b11f201c4e80278cb56c2cc591d5fc9bd0fcc726` |

Installed `linkml-reference-validator` is 0.2.1. Under
`.venv/lib/python3.13/site-packages/linkml_reference_validator/`:

- `etl/reference_fetcher.py`: SHA-256 `acf0861d3c79594c7daf39886e60f78ad772224ecd231475d8b195d0ba218426`.
  `get_cache_path` / `_load_from_disk` select the canonical reference-derived
  `.md` or same-stem `.txt`; they do not discover `pmc_full_pmid_` or automatically
  route separate `.supplement.md` files. `_extract_content_from_markdown` reads
  the content section. `_maybe_retry_full_text` and `_enrich_with_full_text`
  distinguish an attempted retrieval from usable returned text.
- `validation/supporting_text_validator.py`: SHA-256 `52473b443f3ad8d674457a59bf02b233f1263a09bcdb0d5957cda0dc782978da`.
  Lines 181–199 return the native content-unavailable error when the fetched
  reference has no content.

## Search and follow-up limits

Issue titles/bodies were checked live by exact PMID, DOI, record name, and
existing owner number; every issue linked above was open at inspection.
Related canonical curation findings remain separate from these matcher failures.
The bounded local report/review search and M5 cache inventory included ignored
and hidden files (`rg --no-ignore --hidden`). The cache inventory found the
two named PMID text files for 16782812, the article/supplement pairs for
41634815 and 42482240, and the DOI Markdown plus legacy metadata JSONs for
153492. Issue comments and all external source repositories were not searched
exhaustively.

No new issue, comment, validator run, provider fetch, canonical edit, or cache
edit was made by this triage. Continue the authorized aggregate separately;
retain later errors and deduplicate them by existing owner. This snapshot
does not close #703, #1261, #1093, or #1996, and does not certify the underlying
records as scientifically complete.

## Snapshot 003: Coscinodiscus, 23:26 UTC

The next immutable log snapshot is
`.temp/m5-completion-20261114/final-c2-reference-parser-input-003.log`
(903,257 bytes; SHA-256
`bce0da62034a786513cf1de6b6552c4fd074a7361a7bdac8b0ccc278a5812db3`).
Its companion `final-c2-reference-summary-003.json` has SHA-256
`7b28601afe7fc13e6ec31401f0a8b44230e68b969703d2dee5e22c8b092a379a`.
This cutoff has 151 started records, 150 completed, five records with findings,
and 30 retained errors. The first four records retain their earlier findings.
The sweep is still active; these are snapshot counts, not final coverage.

The fifth record is `CommunityMech:000020`,
`kb/communities/Coscinodiscus_Synthetic_Community.yaml`. Snapshot lines
9220–9236 retain three `Text part not found as substring` errors against
`PMID:36300970` at `ecological_interactions[0].evidence[0].snippet`,
`ecological_interactions[1].evidence[0].snippet`, and
`ecological_interactions[3].evidence[0].snippet`. Native output explicitly
says only the abstract is available. A separate `epmc_preprint` provider
timeout is an acquisition warning; it does not turn these mismatches into
scientific rejection of the excerpts.

The exact existing owner is open
[#596](https://github.com/CultureBotAI/CommunityMech/issues/596).
Closed [#1357](https://github.com/CultureBotAI/CommunityMech/issues/1357)
explicitly retained these three Results-excerpt failures under #596 after its
graph correction. The [batch-25 diagnostic](../causal_graph_review/validation-20261005-batch25.json)
records the same paths and phrases and the prior source-reading limitation.
The [October 22 review](../../reviews/structured/20261022T012643Z-coscinodiscus-record-review/review.yaml)
also keeps the three failures visible; its saved record/cache hashes and those
of the [November 6 authority addendum](../../reviews/structured/20261106T155915Z-coscinodiscus-current-genus-authority/review.yaml)
match current M5 bytes exactly:

| Current M5 input | SHA-256 |
|---|---|
| `kb/communities/Coscinodiscus_Synthetic_Community.yaml` | `96bf155c9e47de5f8934bbf367f392bfcee5073098125c841db171fd0b9dda1a` |
| `references_cache/PMID_36300970.md` | `27c42cb32ffce7ca994a115959fbb6aa13ef7d2d64fc9c6179ab588a0007daad` |

The cache declares `content_type: abstract_only`. The bounded ignored- and
hidden-inclusive M5 cache inventory found only that canonical file for this
PMID; the inspected record/cache had no working-tree diff, and HEAD remained
`e9ae9dee132ab210c87f76460c5d6247af9ea99c`. These hashes were observed after
the native check, not captured at failure time. This diagnostic reuses prior
documented source review and makes no new whole-article scientific assessment.

Exact-PMID and record-name searches of all-state GitHub issue titles/bodies
found the existing owner and distinct open metadata/authority follow-ups.
Those unrelated curation findings are not expanded or closed here. No new
issue is warranted for this recurrence; no provider fetch, validator rerun,
source/cache edit, or old snapshot rewrite was performed.

## Snapshot 004: Fucoidan and Ginseng, 23:30 UTC

The retained snapshot
`.temp/m5-completion-20261114/final-c2-reference-parser-input-004.log`
is 930,448 bytes, SHA-256
`9f1a16d68e85d4805d2d2fac86576d064174f09370211df168e37dd6a59f66f4`.
Its `final-c2-reference-summary-004.json` has SHA-256
`52a0a43b0185f8cfe8ac21ccbe3edd3687e12e8c992d563d9652888efd718b37`.
This cutoff contains 213 distinct started records, 212 completed records,
seven records with findings and 56 native errors. The sweep is still active.
The earlier 30 errors are unchanged; two further records contribute 26.

| Record | Native scope in snapshot 004 | Existing ownership |
|---|---|---|
| `CommunityMech:000449`, `Fucoidan_Seven_Degrader_Combinatorial_SynCom` | Fourteen substring errors against `PMID:42649294`, at `taxonomy[0..6].evidence[1..2].snippet`; genome/accession and strain/role table excerpts. Lines 9770–9818. | The exact recurrence is preserved in closed [#1469](https://github.com/CultureBotAI/CommunityMech/issues/1469) and its batch-42 correction. Open [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) owns the general supplementary-source routing requirement; this PMID is additional to that issue's enumerated 79 occurrences. |
| `CommunityMech:000376`, `Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom` | Twelve substring errors against `PMID:42305112`, at `engineering_design.evidence[1].snippet`, `taxonomy[0..4].evidence[0..1].snippet`, and `ecological_interactions[1].evidence[1].snippet`. Lines 9877–9919. | Open [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) explicitly enumerates these 12 supplement-only occurrences. Closed #1994 records the earlier source separation. |

Fucoidan's [retained batch-42 diagnostic correction](../causal_graph_review/reference-validator-correction-20261006-batch42.json)
records the same 14 field-specific failures on the earlier baseline. Its
article and supplementary source hashes still match the
[saved decision record](../causal_graph_review/decisions/20261006-three-records-batch42.yaml).
The inspected sidecar's Supplementary Table 2 rows contain the accession and
strain/role substrings. The original spreadsheet was not inspected during this
triage, and the sidecar's historical statement that normal validation matches
it is not evidence of current native routing. The article file explicitly
labels itself curated open-access excerpts. This does not certify complete or
independently retrieved article coverage. Open
[#1465](https://github.com/CultureBotAI/CommunityMech/issues/1465) concerns
separate scientific graph work; it is not resolved or expanded here. Closed
#1147 corrected a cache sentinel, and closed #1362 concerns selected-text trust;
neither is presented as a new current finding.

Ginseng's current article/supplement hashes match the
[source-separation manifest](../reference_cache_separation/20261013-1994/manifest.json).
The corresponding [snippet audit](../reference_cache_separation/20261013-1994/snippet-audit.json)
retains exact separate-source locations and the twelve article-only failures.
That prior diagnostic is not relabeled as a current normal validation pass.

| Current M5 input | SHA-256 |
|---|---|
| `kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | `61c3e21e1a830b7d0b3e2d3ee2fc7bc17ecc1724aa79414c106e04312c63f468` |
| `references_cache/PMID_42649294.txt` | `ea0c737a5ae104f6e65b7a2224929e4e120d412fdb5bce531bca9c3a2061ebc8` |
| `references_cache/PMID_42649294.supplement.md` | `a3b7db48ee4097692c3833ed377c0914e138161ca37a27ec6b15b9bb8d50a26c` |
| `kb/communities/Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom.yaml` | `e228c2b46ce20acca93762d68d61fe0945620902a42deb516e65fb5f87eee720` |
| `references_cache/PMID_42305112.txt` | `8fb13fc57c6f0be2aef871a80ba0d89f99b991aa0933c1eec2c4862a4de0a415` |
| `references_cache/PMID_42305112.supplement.md` | `7a67c97aa2aead8294100ba895a393e1259010c9d14553273d2fc46facba197b` |

The bounded ignored- and hidden-inclusive M5 inventory found only these two
article/supplement pairs for the exact PMIDs. Both records and both pairs had
no working-tree difference when inspected. Hashes are post-check observations,
not failure-time snapshots. Exact-PMID and record-name all-state issue searches,
relevant owner reads and ignored-inclusive local report searches found the
prior occurrences. No new issue or source/cache change is warranted for these
recurrences; no fetch, validator rerun or scientific scope expansion occurred.

## Snapshot 005: five further known failures, 23:36 UTC

The immutable snapshot
`.temp/m5-completion-20261114/final-c2-reference-parser-input-005.log`
is 1,004,820 bytes, SHA-256
`c8ea058cbbc2a9bf45bd1192f64efdc4bfae01fa7051b6c5c2778a6879e0fb19`.
Its `final-c2-reference-summary-005.json` has SHA-256
`3fecc9c6fb47d84a2a67526f7a34c868193e9d8b15120d1001dc148e68408746`.
It contains 402 distinct started records, 401 completed, twelve records with
findings, and 92 native errors. Five newly encountered records contribute 36
substring errors; the earlier seven records retain their 56 errors. This is
still an incomplete sweep snapshot.

| Record | Native fields and reference | Existing owner |
|---|---|---|
| `CommunityMech:000045`, `Mixed_Gallium_LED_Recovery_Consortium` | One error, `environmental_factors[2].evidence[0].snippet`, `doi:10.1016/j.jece.2025.120403`; lines 10670–10679. | Open [#1618](https://github.com/CultureBotAI/CommunityMech/issues/1618), explicitly named by the earlier batch-73 native failure receipt. Open [#1617](https://github.com/CultureBotAI/CommunityMech/issues/1617) separately owns primary-source provenance and mechanism research. |
| `CommunityMech:000395`, `Nasal_SynCom_C_Bioreactor` | Eleven errors, `engineering_design.counter_selection[0].evidence[0..1].snippet` and `taxonomy[0..8].evidence[0].snippet`, `doi:10.64898/2026.03.16.712028`; lines 10828–10867. | Open [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), explicitly enumerated. |
| `CommunityMech:000381`, `Prymnesium_Parvum_B12_Limited_SynCom` | Fifteen errors, `taxonomy[1..15].evidence[0].snippet`, `PMID:42549325`; lines 11321–11372. | Open [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), explicitly enumerated. |
| `CommunityMech:000424`, `QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium` | Five errors, `growth_media[0].evidence[0..4].snippet`, `PMID:42511722`; lines 11502–11523. | Open [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), explicitly enumerated. |
| `CommunityMech:000388`, `Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom` | Four errors, `taxonomy[0].evidence[1].snippet`, `ecological_interactions[2].evidence[1].snippet`, `environmental_factors[1].evidence[0].snippet`, and `growth_media[1].evidence[1].snippet`, `PMID:42364169`; lines 11545–11563. | Open [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), explicitly enumerated. |

Gallium's exact one-error recurrence is retained in
[batch-73 validation](../causal_graph_review/validation-20261007-batch73.json),
including the identical parent-record error and explicit #1618 ownership.
The current cache contains the rejected sentence in `## Abstract`, before
`## Content`. The installed Markdown loader selects text after `## Content`,
so this failure does not show the sentence is absent from the whole file.
The content section identifies selected quotations despite the `full` header;
the earlier [adversarial assessment](../causal_graph_review/adversarial-review-20261007-batch73.yaml)
and #1617/#1618 preserve this provenance problem. This triage does not certify
the full paper, repair the cache, or infer assay support from the header.

All eight current article/supplement hashes for the other four records match
the saved [source-separation manifest](../reference_cache_separation/20261013-1994/manifest.json).
The [prior snippet audit](../reference_cache_separation/20261013-1994/snippet-audit.json)
preserves their explicit supplementary locations and article-only failures.
These are native routing failures with prior separate-source evidence, not
new determinations that the scientific statements are unsupported.

| Current M5 input | SHA-256 |
|---|---|
| `kb/communities/Mixed_Gallium_LED_Recovery_Consortium.yaml` | `c9e9c9642b62987399daa4d82a3778b14f9cbb794085e7eb8d0dd562eb4dc117` |
| `references_cache/doi_10.1016_j.jece.2025.120403.md` | `c434ae59abbb4a6ec12fe8e075935fd59b3b945b39cf247942d98ad9bcd584a8` |
| `kb/communities/Nasal_SynCom_C_Bioreactor.yaml` | `4bd66811333c6960ebab5553e7ce71c8a4f92aa1d81f0fc2c9e2b4f6b75dac2e` |
| `references_cache/doi_10.64898_2026.03.16.712028.md` | `269c016a80b6efdb7215dad886853871c0b8e3cbaa849516c85c66cb1256f0ac` |
| `references_cache/doi_10.64898_2026.03.16.712028.supplement.md` | `90b71bdcf0f071f2b99b53174601664edf903690f1bc4e61cda1b282ee85e23e` |
| `kb/communities/Prymnesium_Parvum_B12_Limited_SynCom.yaml` | `2e1d674f45e85230bfdd1d05aeb6f6c6b0f58b44fb478515d13b3aa7535c1225` |
| `references_cache/PMID_42549325.txt` | `67e0171a0f2c978c23abad3bb55ddc20b23823acd0eaa8c38601bab17a07e7f3` |
| `references_cache/PMID_42549325.supplement.md` | `4b30395e5db1c46bfb2f87a8737c55f825dfb80394485a5315736b006ec9f50e` |
| `kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml` | `2eede18215821618a8acacbe5d47754774d268e044e47b80368100e8e4927fc0` |
| `references_cache/PMID_42511722.txt` | `e7ce26edc63832f754798c439403265bf167c8eb883e4d8184a8fedd101f94ac` |
| `references_cache/PMID_42511722.supplement.md` | `6ddcbad463b48ca43da2a266f2f81e2e696c65ee54b7b4cc56b7adcd838df757` |
| `kb/communities/Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom.yaml` | `5b74bd01d770c894a9dd65240bf47b4754d997013fa2681a63abf653a1fb82d0` |
| `references_cache/PMID_42364169.txt` | `76ae187fe615a75d522443b9deb085bc8499efb54df080407563f901c514a4d4` |
| `references_cache/PMID_42364169.supplement.md` | `baca59f4f9ac9c772f51d4c28be1ad8244ee94b016a70e5b464694c0e3590a7f` |

The bounded M5 cache inventory included ignored and hidden files; it found
these source pairs plus Gallium's canonical Markdown and legacy metadata
JSONs. All five inspected records and named caches had no working-tree diff.
These are current post-check hashes, not failure-time captures. Exact DOI,
record-name, relevant existing-owner and ignored-inclusive local diagnostic
searches were used for deduplication. No new issue is warranted for these
known recurrences. No fetch, validator rerun, source/cache change, or broader
scientific review was performed.

## Peanut checkpoint: final immutable snapshot pending

Read-only inspection of the growing native log found nine errors for
`CommunityMech:000314`, `SynCom_ARC_Peanut_Aflatoxin_Nodulation`, at lines
12153–12186. All cite `PMID:42099455`. Exact fields are
`growth_media[0].evidence[0..2].snippet`,
`growth_media[1].evidence[0..1].snippet`,
`growth_media[2].evidence[0].snippet`, and
`cultivation_setup[0].evidence[0..2].snippet`.

Open [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996)
explicitly enumerates these nine supplementary-methods failures. The source
pair matches its [prior separation manifest](../reference_cache_separation/20261013-1994/manifest.json)
and the exact field occurrences are retained in the
[earlier snippet audit](../reference_cache_separation/20261013-1994/snippet-audit.json).
The inspected M5 record and source pair had no working-tree diff. The bounded
ignored- and hidden-inclusive inventory found the named article and supplement
for this PMID. These are post-check hashes, not failure-time captures:

| Current M5 input | SHA-256 |
|---|---|
| `kb/communities/SynCom_ARC_Peanut_Aflatoxin_Nodulation.yaml` | `8128a35b7336eb6a0e2da4768e456cd12e84db5632b771708a70f07d6bebd5b5` |
| `references_cache/PMID_42099455.txt` | `ceea4d8b5362fc7c69fbc04693442c19bfcc8a35f7d8d7431338c1246e817504` |
| `references_cache/PMID_42099455.supplement.md` | `65ecfb230839593cded3ad746a58d0274dc2b2441fdf2f500aa80b8b61398144` |

Together with the previous checkpoints, all eight reference buckets explicitly
enumerated by #1996 have now appeared: 15 + 9 + 12 + 4 + 8 + 5 + 15 + 11 = 79.
Fucoidan's 14 are an additional known supplement-routing recurrence, outside
that enumerated 79. This reconciliation is not a final corpus count and does
not close #1996. No new issue, source edit, fetch, or validator rerun occurred.
The final immutable log hash, complete coverage and any remaining outcomes
will be recorded separately after the native process finishes.

## Final added record: Wollastonite

The final snapshot adds `CommunityMech:000404`,
`Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium`, with two errors at
`taxonomy[0].evidence[1].snippet` and `taxonomy[1].evidence[1].snippet`, both
against `PMID:42478817` (native lines 12838–12850). The duplicated quotation
ends with a comparison of 26.80% and 19.70% against hzt-3 monoculture. The
currently inspected cache contains the earlier leaching values but a different
comparison; a bounded ignored/hidden-inclusive search found neither percentage
nor the word `surpassing` in that exact cache. This is not a fresh complete-paper
scientific verdict. Primary-source/version verification is still required.

The record SHA-256 is
`cc6165ecc72e89e7945cd433d963ce1105ccc8a08078de656f5485a098ccd49d`;
`references_cache/PMID_42478817.txt` is
`a16fc2b369d4bab42a84959c670d1b6e1306e5959731af305e964cf2e6d7d0d9`.
Both were unchanged on M5 when inspected after the sweep. The bounded
ignored/hidden-inclusive cache inventory found this exact PMID text file.
Git blame dates the duplicate evidence blocks to `7f8208db9`, after the older
[batch-123 native pass](../causal_graph_review/validation-20261008-batch123.json).
Closed [#2113](https://github.com/CultureBotAI/CommunityMech/issues/2113)
describes the later annotation work; open #1961 addresses the separate role and
inoculum interpretation. Exact-PMID/name and exact failing-phrase all-state
issue searches found no existing owner for these two mismatches, so the
completed read-only pass filed [#2793](https://github.com/CultureBotAI/CommunityMech/issues/2793).
No record/cache edits, provider fetches, or validator reruns were performed.
