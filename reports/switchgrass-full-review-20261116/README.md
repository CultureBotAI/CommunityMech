# Full current Switchgrass review checkpoint

The new [native YAML review](../../reviews/structured/20261116T011931Z-switchgrass-full-source-successor/review.yaml)
and [rendered Markdown](../../reviews/structured/20261116T011931Z-switchgrass-full-source-successor/review.md)
complete an evidence-backed assessment of the current Switchgrass record. The
verdict is **needs_curation**. The Methods/Table S1 stock correspondence remains
an open major finding under [issue1548](https://github.com/CultureBotAI/CommunityMech/issues/1548).
The narrow supplement-routing finding is resolved for this record; that does
not close the multi-record issue or resolve the scientific stock discrepancy.

The review covers identity and design, sixteen individual stock/deposit/taxon
assertions, environment, assay-specific media and conditions, two populated
community relations, all five discussions and quotations, the absent causal
graph, and provenance. Thirty assessments draw on the retained main article,
Table S1 stock columns and selected cells, actual Figures 2/3/5, the two related
papers' Methods, and retained taxonomic authority observations. This does not
claim a fresh catalogue, assembly or raw-data audit, experimental replication,
or scientific completion of the related records.

The source revision is `f4807c459e0986ff9d2aa41365f393b1e9ba4d2d`, with
working-tree context captured explicitly. The canonical target is
`kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml`, SHA256
`bcc2759c9da7c4059330726a1b154df600ec394d1106be2dcc1f4d247eed5eb9`.
No scientific content was changed while building or saving this review.

Nine of the ten recorded native commands passed. The full-corpus network audit
**failed with exit 1** for warnings elsewhere; it reports no Switchgrass key.
The failed required command remains failed in the saved review. The eight
structural/history checks retain their actual M5 execution at `3b1c7426` plus
the applied working record, whereas normal references and measured coverage
retain their actual `f4807c45` execution. These are separate observations, not
a full-QC run at one revision.

Both hosts measured 37/37 current Switchgrass snippets through the normal source
dispatcher, including the three exact supplement cells. The separate
[six-record M5 measurement](../phase2-reference-measurements-20261115/m5-six-normal-f4807c45-001.md)
compared and matched 270/270 snippets. Quotation matching does not establish
scientific interpretation or whole-corpus coverage.

## Saved evidence and checks

Root read all thirty actual draft assessments, checks, evidence, findings,
ownership and limitations before native save. The saved-pair audit then
validated the native schema and exact Markdown rendering, and rehashed all
86 declared inputs (5,218,236 bytes). Root independently rehashed those inputs
and verified the complete local checkpoint: **88 files, 5,395,155 bytes**,
including the saved pair. Private paper bodies and images remain private.

| Artifact | SHA256 |
| --- | --- |
| Saved review YAML | `83d4aa59145ddd04383bb61c29f19dc73c778a6d54967bedbb3db7b97ebfba0d` |
| Saved review Markdown | `135982ead076883634dc9c5a76a706e2e9eceb0cb9bc413832ab249f28be0735` |
| Actual draft002 JSON | `07311fa9cf93ba69493ea90ab54f5bb459b04886616e040e46c6e81ee2422143` |
| Native inspection002 JSON | `a898a024770bef7114d0b05b0ae6b8acf81dfa1143dde88204336e837d0b9d17` |
| Local input-checkpoint002 manifest | `5737295d3ab6dfaa74717b1802ce4abdb22fef381094e63035551cac3c3b006d` |
| Executed config004 | `40685ae10bee4aa92406be5a37017c3eeed097c124bb3637ae858efb508ff03e` |
| Executed repaired builder | `cec067b5cb23fd4392f48227b2b5c7c2f3da9d79b77bfa6e27679ec79b827ca6` |
| Builder regression tests | `a17e2756f2f30259c3300106bf1c66bd3bac78cf5c0fe7b404861643fa5ae63e` |

The draft, inspection and checkpoint are under
`.temp/switchgrass-full-review-20261116/`, in `review-draft-002/` and
`input-checkpoint-002/`. Execution receipts and raw logs are retained under
`.temp/phase2-schema-20261115/`:

| Native recorder | Exit | Raw log SHA256 |
| --- | ---: | --- |
| `switchgrass-full-review-build-001` | 1 | `935c5f7224f8089abf71c4e7605c917b9808f1eb938f2912ce9aa0fe5ec086f6` |
| `switchgrass-full-review-build-002` | 0 | `208faf73bc765a3305f6b6a081d27a18af0fc729ca2794e1afaaa72d10a1533a` |
| `switchgrass-full-review-save-002` | 0 | `94478d6479291776d0e1d719eaae1b74709db1ffd45f0b3f88aa8c27ce93ab40` |
| `switchgrass-full-review-saved-audit-002` | 0 | `b3a9051f7695ce6f46ca36db3f1fd8f82fdc4a840d1ccc0e24d592f6f8715db4` |
| `switchgrass-full-review-checkpoint-verify-002` | 0 | `89ec2b4326e406ff29ad3bcdac3a3af398fb09186b0269d90b3cec38b4fe6aa8` |

## Preserved errors and repairs

The prior immutable review remains unchanged. Its incorrect omitted-genus and
Bosea-reference statements are superseded here with source-bound assessments
under [2938](https://github.com/CultureBotAI/CommunityMech/issues/2938).
Rejected authored001 remains alongside corrected authored002: the latter
describes the FSR allocation correctly and limits 24 C to seed germination,
as recorded under [2940](https://github.com/CultureBotAI/CommunityMech/issues/2940)
and [2941](https://github.com/CultureBotAI/CommunityMech/issues/2941).

Additive configs preserve the rejected missing-owner/terminal-lineage payload
under [2942](https://github.com/CultureBotAI/CommunityMech/issues/2942).
The measurement guard now checks actual per-assertion comparisons, validity,
calls, source bindings, completion, errors and drift, addressing
[2943](https://github.com/CultureBotAI/CommunityMech/issues/2943). The actual
37/37 measurement bytes were not changed to satisfy the guard.

Actual build001 stopped before inspection or draft output because its copied
network-warning list disagreed with the native auditor. Under
[2944](https://github.com/CultureBotAI/CommunityMech/issues/2944), the repaired
builder uses the captured maintained severity function and its per-finding
overrides. Genuine errors still refuse; the original corpus exit 1 remains.
The exact executed old helper is preserved as
`scripts/adhoc/build_switchgrass_full_review_attempt001_20261116.py`, SHA256
`c1cedb4a2aae0830edc5ad2fc9880ea853234d43642aca7172bfd9ca9221199e`.
The failed receipt/log/exit and old configs remain unchanged. The repaired
builder passed 46 regression controls before actual build002.

Publication review also found that the failed-build log and actual audit test
fixture matched the broad log ignore. [2945](https://github.com/CultureBotAI/CommunityMech/issues/2945)
records this finding. The staged tracked-report check also exposed the already
published Switchgrass source-plan JSON and the Wetland measurement log tracked
under [2922](https://github.com/CultureBotAI/CommunityMech/issues/2922). Four exact
path exceptions admit these files while preserving their bytes and the general
ignore rules. The first staged check remains a retained failure; the unchanged
check passed after the two additional exact exceptions, with all 26 intended
publication paths staged. No force-add or assertion change was used.

## Current successor admission

The new [manifest003](../phase2-completion-20261115/scientific-successor-provenance-003.yaml),
SHA256 `15ac1e37677af0342783ea1b2c7ad15c005c341ced2ec2c469e7d3b67e0cdbcf`,
binds the current Switchgrass record to this saved full assessment, five
Phase 2 sidecars and four actual application receipts. The other four record
rows remain exactly unchanged. The prior manifest, historical scientific
checks and native validation requirements remain intact. Its generator is
`scripts/adhoc/build_switchgrass_successor_manifest_20261116.py`, SHA256
`4134deecf295e391d4724a54b192a9078db891bb35ed19ebaaac473ad25b9e79`.
Actual generation passed at `f4807c45`; raw recorder
`switchgrass-full-successor-actual-003` has SHA256
`f90113aad728f45f2a7c4725cd1ce58c7bfb0dbfce99ebecdfaf3e13a43bac00`.

One actual current-record positive canary passed before the affected tests.
The subsequent run passed **56 tests** in 47.08 seconds, with 12 existing
deprecation warnings. It covers the new current review, old scientific
successor controls, historical batches 36/61 and writer tracing. This includes
the eleven existing refusal cases against the real current review and the
unchanged all-five-record verifier; no historical assertion was removed.
Native lint then passed Black (807 files), Ruff and mypy (52 source files).

| Native recorder | Exit | Raw log SHA256 |
| --- | ---: | --- |
| `switchgrass-full-successor-positive-003` | 0 | `c018a388767c909a8bb9aced049780da5d63294b665aea5266efb24bc9679cca` |
| `switchgrass-full-successor-controls-003` | 0 | `6859b2dede284ad6941c88284c6bc4953eca877e7878a42cb0a9372d76398832` |
| `switchgrass-full-successor-lint-003` | 0 | `138698affb226cc5305d988580d909a7af3f13c93a1a02b74963a32a8784eb3f` |
| `switchgrass-staged-report-ignore-001` | 1 | `31cbb27a289e8fd9255122d601acab1b98751686912f3208e76f4c47fd405f4d` |
| `switchgrass-staged-report-ignore-002` | 0 | `bc4c2ff1a05d78db864338a871f51116604f720d25667467a47cb7c30039c666` |

At this checkpoint the saved review, local evidence package and strict
successor admission are verified. The complete M5 input checkpoint remains
pending; matching private source files already exist in the approved earlier
M5 snapshot and can be reused by hash. Final combined QC, corpus references,
current generated products and merge approval remain separate requirements.
Passing validators cannot resolve the retained scientific finding.
