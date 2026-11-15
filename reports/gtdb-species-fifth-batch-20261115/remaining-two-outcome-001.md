# Barley DT and Quinoa SCDY1 bounded database corrections

The two remaining eligible records now retain thirteen native GTDB reference
correspondences and three complete ambiguity lists. Barley has ten new blocks,
twelve selected statuses and two ambiguity lists; Quinoa has three new blocks,
four selected statuses and one ambiguity list. Each application appended two
native inline events and one native history sidecar. All original stock fields,
source quotations, scientific claims and earlier history remain unchanged.

| Record | Reference population and source limits |
| --- | --- |
| 000428 Barley DT | Ten populations of 3, 20, 6, 7, 2, 3, 217, 3, 9 and 4 reference genomes in index order 0,1,4,6,8,10,11,12,13,15; fractions 1.0 except rounded 0.85 and 0.94 at indices 1 and 11. Complete three-option Mesorhizobium and four-option Priestia/Virgibacillus ambiguities remain unselected. Sixteen experimental B-series stocks, four native-null descriptors, partial 16S qualification, duplicate reference accessions and the timing findings remain intact. |
| 000459 Quinoa SCDY1 | Three populations of 5, 9 and 127 reference genomes, each fraction 1.0, at indices 0,2,6; complete four-option Priestia/Virgibacillus ambiguity at index 7. Nine species-like isolates, the native-null descriptor and four unselected existing blocks remain unchanged. The stored Acidovorax population of 375 differs from the fresh diagnostic 324; this correction does not refresh or certify that old block. |

These are reference-taxon observations, not study-stock genome assignments,
inoculum abundances or formal nomenclatural rulings. Rounded fractions do not
establish an exact numerator. Barley's B7 is not newly identified as reference
stock B8W22. Its prior full scientific review remains `needs_curation` with
reference-identity and cultivation/timing findings. Quinoa retains selected
preprint excerpt coverage, the separately recorded historical abstract check,
Arabidopsis host versus quinoa origin, and source/reciprocal-fitness limits.
Neither record gains a new mechanistic or whole-record scientific approval.

Actual M5 staging, applications, sixteen native commands and native review save
ran at frozen `24f0185a869377f74ecad1425756cb5413d9aa72`, Python 3.13.2. Local
verification used Python 3.13.12 and the working tree based on Apple checkpoint
`60e35fbb4da1b79f63c818d41b0b9fcdae581854`. The dependency lock remained
`712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4`.
The crosswalk is exactly
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
its upstream release and chronology remain unestablished. Every actual stage
and input set was independently reviewed before the guarded application.

| Record | Before SHA-256 | Actual after SHA-256 |
| --- | --- | --- |
| 000428 | `b4cbe1a4ec5082d224bad75aeefecc74c6cce5bf6f3b3f6a77d41959f8b93e89` | `8e6258c021a3c3629bc59e17d8b9d11234294bbdd3c82d81aa20a5dbce21b47c` |
| 000459 | `dd5e67d01f8c707eb6e7ef178fcdee359a9bb3a57df210d4256dab0efcb266c3` | `4b9244ce2486f6a943079f7032251a19aa7af21a3ef47bfb3b79fe9d60717ab9` |

The byte-identical actual application receipts are
[Barley](428-001-apply.raw.json), SHA-256
`42525c929259958512eb36ef6718784b992319fc1385cdbb156a71188376170d`,
and [Quinoa](459-001-apply.raw.json), SHA-256
`b33d35fa28eef5943700181f394594aae42b6cce04a9a18c81e295270753e459`.
The new sidecar hashes are respectively
`a09e833c6c469f0de54a5d982c1f18fbdb952b1fd806a768754ca265e616636a`
and `e788eeda7e04b0e9edb1e01028b76de3b4b0b914e6c35348ce311c7c7e55414d`.

All eight scoped commands passed for each record: schema, strict, GTDB
coherence, prokaryotic domain, scalars, new-history, history and ontology terms.
Each retained receipt binds the actual current record and unchanged execution
inputs, nonempty log and native exit 0. Both strict logs report one scanned file
and zero errors; both term logs explicitly report validation passed. The
new-history command is scaffolding; the other seven commands are validators.
No source-snippet comparison or whole-corpus gate is included in this result.

The immutable [two-record YAML](../../reviews/structured/20261115T124033Z-barley-quinoa-species-reference-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T124033Z-barley-quinoa-species-reference-diagnostic/review.md)
contain six assessments, sixteen required passed checks, partial coverage and
`scientific_review: false`. Their SHA-256 values are
`6ec0976913b6e53e53d978ce20b59b978577f9f3fb16b8475d5bd03b09884be9`
and `83ba81adc6507c703726e1f55cf402edc2401e0089300843df676616ae531a6e`.
Local and M5 audits verified all 126 inputs (5,688,331 bytes), native validation,
exact Markdown and unchanged inputs. The parent independently repeated the audit.

Before caller edits, the complete 128-file namespace, including the saved pair,
was preserved under
`.temp/gtdb-species-fifth-batch-20261115/two-input-checkpoint-001`.
The exact manifest is
`71f46d077f9d2e7ecdd20ae798540d24b336e435cd6bd7e0ce48f1cf5e4f418b`;
all 5,822,942 bytes were verified on both hosts and independently by the parent.
A nonempty manifest transfer canary matched before the remaining missing-only
copy. The immutable namespace retains the original batch92 input despite later
caller evolution.

The unchanged exporter produced identical plan/publication metadata, stdout
SHA-256 `3485ffb4c48c6acc9e656404d68f1c27b6ffcb9011d4066f0697bc1e89145734`.
All 54 persisted artifacts rehashed successfully. The fixed
[Barley successor](428-001-successor.json), SHA-256
`28cde99f83401b130a0d477ea7950c3e9c8f368c34470286eaf20e8b1937a69e`,
and [Quinoa successor](459-001-successor.json), SHA-256
`49d85fd3b6e92671ca3d735754cdd668131ec50a25ad34d6af8074e2f785674d`,
bind the saved pair, raw actual receipt, source metadata, sidecar, native
recomputation and every public gate triplet. No source body was newly exported.

The strict registry adds only these two fixed proofs. Batch92 adds Quinoa to the
existing species predecessor projection for old digest/history predicates;
the current-document equality guard, 424 remediation/genus chain, 361 admission
and all current biological/source-count predicates remain unchanged. Batch7
requires no modification. The shared mutation engine remains unchanged.

The actual Barley proof canary passed **18 tests** (17 shared positive,
mutation/refusal/restoration and unknown-target controls, plus direct current
production admission), with 35 unrelated cases deselected and 12 existing
warnings in 12.61 seconds. Only after that success, the Quinoa proof passed its
**17 controls**, with 36 unrelated cases deselected and 12 existing warnings in
11.61 seconds. These are two actual runs, not an asserted single 35-test run.
Their raw log hashes are respectively
`d18c4a8e785e7ec2c253c3046b56cfe894e3397c1c22a603542adfddfb558ee1`
and `a538b434948a2ee85f8f95fee7a9b37b16ce8577207515bc4abc4164e10409a5`.
Previously completed Apple mutation cases were not repeated for counts.

All **18 historical caller tests** in unchanged batch7 and composed batch92
passed, with 12 existing warnings in 5.16 seconds; raw log SHA-256
`bfaa7eea391e4240209b16dbc9df52644f8ca17b60d43b7ff5df9dc9df8d6c0a`.
Full native `just lint` passed: Black checked 758 files, Ruff passed, and mypy
found no issues in 52 source files. Its raw log hash is
`a24c26d9a36dcbba108f7b582ff56170ce3cc3b76640662122cda99bad0fa607`.
These receipts describe the isolated working tree based on 60e35fbb, not a
clean combined integration run. No source, schema or shared execution helper
was changed for these two units.

The native append-only review check against 24f0185a passed for **334 retained
bundles**, explicitly reporting `declared_scopes_only`. It finished with exit 0
at 12:49:53 UTC; raw log SHA-256
`0c72c28a07c34bb7709f75957baeb667a92e07d9145d2341658e9dfda723e6fa`.
This verifies bundle integrity at the declared scopes, not additional scientific
coverage. The raw local recorder triplets are retained under
`.temp/phase2-schema-20261115/species-fifth-two-` with suffixes
`actual-canary-001`, `actual-459-001`, `callers-001`, `lint-001` and `reviews-001`.

The earlier [Apple outcome](377-canary-outcome-001.md) remains a historical
checkpoint with its own actual evidence. All three eligible records now have
separately verified bounded corrections. Wetland471 remains unchanged under
[2898](https://github.com/CultureBotAI/CommunityMech/issues/2898) and
[2899](https://github.com/CultureBotAI/CommunityMech/issues/2899); its identity
correction requires a separate source-backed candidate and guarded path.
Combined integration, generated products, full M5 QC, measured reference
validation and whole-record scientific review remain separate requirements.
