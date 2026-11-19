# LDSynCom, Community G and fucoidan reference correspondences

The remaining three prepared records now retain 22 native GTDB correspondences:
11 LDSynCom descriptors, six Community G descriptors and five fucoidan-panel
descriptors. The guarded applications changed only those blocks/statuses and
two native inline events per record. Existing source quotations, stock and
assembly identifiers, biological claims, old history and unresolved descriptors
remain unchanged. Each record also has a new native history sidecar.

| Record | Current record SHA-256 | Preserved source boundary |
| --- | --- | --- |
| 383, LDSynCom | `78ae367fef57e79fca7762cf49ea96f2651dd038a39504b14c344b434e69e645` | Eleven distinct stocks and existing assemblies remain separate, including repeated species. Selected preprint/code excerpts do not resolve completeness, phenolic-proxy or quotation findings 2314–2316. |
| 387, Community G | `4df2afef7cee457738dd2774e0f5656defee918369ffab9b1dae13d7aa5283d2` | The six relative-profile reference taxa retain null stock fields. They are not a complete cultured roster; GENIA, upstream assays and findings 2591/2592/2604 remain separate from the correspondence repair owned by 2593. |
| 449, Fucoidan panel | `dd5f3213940fe8ac0787c79d7550688802a088760483d0d8fe9a52ed1bedad36` | AS12/AS25 remain unresolved, G88 remains excluded, and the seven-stock/127-combination scope is preserved. Separate supplement columns, stock aliases and existing assemblies are unchanged; findings 1465 and 1996 remain. |

Reference genome totals and rounded fractions describe the native lookup
populations. They do not newly classify the study stocks' assemblies, supply
exact numerators for rounded fractions, or establish formal species renaming.
The crosswalk is pinned by SHA-256
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
its upstream release and chronology remain unestablished.

Actual M5 staging, guarded applications, history, checks and native review save
used frozen public revision `14d95aa224ca0968a5008fb2b07b9500ce30f5bc`, Python
3.13.2 and unchanged frozen dependencies. The preceding 476 canary completed
before these three applications. Every target then passed all eight native
commands through the same retained checker: schema, strict, GTDB coherence,
prokaryotic domain, scalars, new-history, history and ontology terms. The 24
receipts bind each accepted current record, actual exit 0, nonempty logs and
unchanged execution inputs. Strict reports one file and zero errors for each;
terms explicitly reports validation passed. These commands do not include a
source-snippet sweep or full corpus QC.

The immutable [native YAML](../../reviews/structured/20261115T114547Z-lignin-genx-fucoidan-species-reference-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T114547Z-lignin-genx-fucoidan-species-reference-diagnostic/review.md)
contain nine scoped assessments, 24 required passed checks and 178 declared
inputs. This is a completed diagnostic with partial coverage and
`scientific_review: false`, not a full scientific assessment.

| Saved artifact | SHA-256 |
| --- | --- |
| Review YAML | `955f81f1f3d041e87130f0651111a35689256f6076f43c79bafe2e0dff490a1e` |
| Derived Markdown | `4b8a3b7f4492e86b7391a5a137e79b65df2a4f93c095b7d5cc489fe3e5867c24` |
| Complete input namespace manifest | `009c6c6bd8d0ccd623e3c77f557977c84aecf659749dd4b09733b9d1ba828106` |

Saved-pair audits verified all 178 inputs (7,893,418 bytes), native validation
and exact Markdown. Before any historical caller changed, the complete
180-file namespace, including the saved pair, was preserved and independently
verified on both machines: 8,080,936 bytes under
`.temp/gtdb-species-fourth-batch-20261115/three-complete-inputs-001`.
The missing-only transfer first verified its nonempty manifest, then copied and
verified every retained file. Later local caller edits do not rewrite that
immutable input namespace or relabel the original M5 receipts.

The unchanged exporter completed its plan and publication from the same
captured bytes. All 81 public artifacts rehashed successfully. Each externally
pinned successor manifest binds the record's actual application, native
recomputation, source evidence, saved pair, sidecar and eight public gate
triplets:

| Manifest | SHA-256 |
| --- | --- |
| [383](383-001-successor.json) | `6e29abd24fb717245958e6a8ed1cc4537c989f2c1ea9c63c6d934ace3d808efc` |
| [387](387-001-successor.json) | `4771fd0355980efbbb95759eecbe765572f2571f2ac28641aedca03c4691b72d` |
| [449](449-001-successor.json) | `b73e838d9fb280c400814cd4f807198b442691ca99c83a8744b08a8958270f15` |

No new source body was exported. The initial checksum-list invocation omitted
jq's slurp option and produced an empty list; its failed hash-check receipt
remains retained. The corrected `jq -Rsr -f` invocation used the unchanged
helper and original exporter output, then all 81 checks passed. No exported
payload or native gate was changed to obtain that result.

The strict registry adds only these three exact proofs. Batch5 admits the
current LDSynCom record before its original current biological predicates;
batch23 verifies the current admitted Community G bytes. Batch42 uses the
admitted fucoidan predecessor only for the old history predicate, after checking
the current document against current bytes. Its Transwell historical path and
all GENIA/current biological predicates remain unchanged. No unknown changed
record is admitted by fallback.

Local tests used Python 3.13.12 in the working tree based on
`b8e882ba278c5fd8523aec38931db1b246a7d401`, with the disclosed new canonical,
evidence and caller files. These are not clean combined-revision receipts.
The 383 proof canary passed before the remaining two cases. Together the two
runs passed **51 actual-proof controls**, including rehashed tamper/refusal and
restoration checks. All **24 tests** in the three affected historical modules
also passed. Each pytest run reported 12 existing deprecation warnings.

| Retained local run | Actual result | Raw log SHA-256 |
| --- | --- | --- |
| `species-fourth-local-383-proof-canary-001` | 17 passed, 51 deselected; 14.39 s | `3b60a19d4a9fedff7d3f774edaf976645ba091a61200d529419dcd1e1852eaed` |
| `species-fourth-local-387-449-proofs-001` | 34 passed, 34 deselected; 27.17 s | `0624cd8c59ef5842cb560da81f3a2ed546ce19bbdc3454ca18ee67327e3c1e0a` |
| `species-fourth-local-three-historical-001` | 24 passed; 4.33 s | `adfc02b5b31dbce294bff5c9ec946a2eb29a8c508df6c468969773eea77aba55` |
| `species-fourth-local-three-lint-001` | Black 753 files, Ruff and mypy 52 source files passed | `fcb9f1c5f3f9843ef2fcbed7e77d70240efd90d963dfc0192303fd5422b0c36f` |
| `species-fourth-local-three-native-reviews-001` | 326 valid bundles; `declared_scopes_only` | `01e3fa7e33080504557f6a7cd3529e390a5283d903b2cf3e66dd4f63d1ed3ab1` |

Those JSON/log/exit triplets are retained under
`.temp/phase2-schema-20261115/`. The native append-only check against b8e882ba
checks bundle integrity, not full scientific coverage. Earlier canary evidence,
failed invocation evidence and historical reviews remain unchanged. Combined
integration, generated pages, full M5 QC, measured reference validation and
scientific blocker disposition remain separate work.
