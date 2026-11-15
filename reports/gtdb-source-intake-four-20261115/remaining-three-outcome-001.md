# T1, Fahmy T4 and C6 mapping checkpoint

Records 498, 369 and 405 now have the reviewed reference correspondences and
complete native ambiguity sets, actual guarded M5 applications, eight native
checks each, one immutable partial diagnostic and a complete input checkpoint.
The [KZ344 canary](344-canary-outcome-001.md) completed the same workflow before
these three units ran serially. This checkpoint does not certify the records'
scientific claims or complete corpus QC.

| Record | Bounded change | Final record SHA256 | Actual proof |
|---|---|---|---|
| 498 T1 | Two reference blocks; three complete ambiguity sets; five statuses | `96c2e5dc7633b38de4dbc6cd959ec36476d12c50bb35df19037ad4dd63e17807` | [Manifest](498-001-successor.json) |
| 369 Fahmy T4 | Four reference blocks; two complete ambiguity sets; six statuses | `57678380021330f5d0e6f880bbd16c141e020e2c341ef4d61c0a831deeb5e7c9` | [Manifest](369-001-successor.json) |
| 405 C6 | Three reference blocks; three complete ambiguity sets; six statuses | `d7e0e6ea175dbdafe54dde46233e341acc82573347a0d1d9c1d71078f0488134` | [Manifest](405-001-successor.json) |

The nine blocks and eight ambiguity sets concern 17 selected taxonomy
descriptors across 18 stock occurrences. T1 Re2's existing 23 alternatives
remain unchanged. Each record retains its six distinct stocks, all scientific
content and previous history, and gains only the two actual native grounding
and status events plus a new native sidecar. Repeated species identifiers in C6
do not collapse its distinct stocks. T1's MALDI best matches remain reference
matches, and the T4/C6 partial16S assignments are not new stock-genome proofs.

The retained crosswalk SHA256 is
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
its release remains unestablished. Counts and fractions describe the native
reference populations. The T4 prior review's salinity, assay-temperature and
protocol-detail findings and issue 1371 remain unresolved. C6 retains the
94.41% versus 95.26% assay distinction, 50 versus 100 mg/L source discrepancy,
ammonia-production boundary and recovery limitations. No causal edge, role,
cultivation parameter, quote, source stock name or existing discussion is repaired
or newly endorsed by this mapping work.

Actual execution used frozen M5 commit
`8ad0caccd37c5903daa0cbcebd4f682bae63449a`, Python 3.13.2, the unchanged
native resolver and accepted shared stage/apply/check helpers. All three
candidates and their captured inputs received independent review before
application. Each unit then passed native schema, strict, GTDB correspondence,
domain, scalar, history, new-history and term checks. The strict logs each
report one file and zero errors, and term logs report the literal native pass.
All 24 actual command triplets retain successful exits and unchanged-input
bindings to their final record bytes. Every old sidecar remains unchanged.

The first local SSH launch of the T1 staging plan refused hostname resolution
with exit 255 before any remote command. Its raw log is retained as
`intake498-m5-stage-plan-launch-001` under `.temp/phase2-schema-20261115/`
(SHA256 `44166c803ed367c797668ee1b6b5ee10f3289a1649c17322a1a135468df7b20f`).
The same scoped plan then succeeded with network authorization; the successful
staging and actual application receipts remain separate from that refusal.

The [native YAML](../../reviews/structured/20261115T130434Z-t1-t4-c6-reference-correspondence-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T130434Z-t1-t4-c6-reference-correspondence-diagnostic/review.md)
have SHA256 `1edb85d41241d2c8da7283892ff8e2fb96f0e01b5e9e73f876425a4021a89233`
and `92879237fccf54db680e5d5ec384c5a1ae275ec3526682ed3e44bf82f90d097d`.
This is a three-target, nine-assessment, 24-check diagnostic with
`scientific_review: false`, partial coverage and a qualified pass. Independent
pre-save review checked every actual input and native log. After native save,
the unchanged audit on both machines verified all 176 inputs / 6,925,736 bytes
and exact native Markdown; the two audit outputs are byte-identical.

Before historical caller edits, the complete private namespace was preserved
on M5 and mirrored locally using a verified one-file canary followed by the
remaining files without overwriting existing paths. Both copies verify
178 files / 7,101,171 bytes against manifest SHA256
`52f42aadce10c8d23b6c1d6565b0720970fc0a06b352071eba3a70f9a5499cff`.
The namespace is `.temp/gtdb-source-intake-four-20261115/remaining-three-input-checkpoint-001`.
It preserves the original inspected callers, source bodies, helper bytes,
receipts and native review pair. Later caller changes do not rewrite the saved
review's earlier observation.

The unchanged captured-input exporter used the independently accepted
[export config](remaining-three-export-config-001.json), first in plan mode.
Its 81 emitted artifacts all match the planned SHA256 values. Actual apply
receipts and source metadata remain byte-identical; public gate logs and
receipts use the existing sanitizer and retain their raw hashes. No raw paper
body or private checkpoint is published here.

The explicit registry admits only the three pinned actual proofs, alongside
the existing KZ proof. Shared admission and mutation engines remain unchanged.
Batch 28 checks current T4 biology after admission; batch 50 uses the admitted
C6 predecessor only for its historical last-event obligation; batch 137 adds
T1 while preserving the existing 499/500 admissions and current parsed-history
mutation guard. All old ledger literals, scientific predicates and other
record obligations remain in place.

Local verification recorded start revision
`d54cbc1dd1e234e1d25fec2304f7b93d1b1819d4` plus its explicitly captured working
changes; these are not clean-commit aggregate-QC claims. Receipts and raw logs
are retained under `.temp/phase2-schema-20261115/`:

| Receipt stem | Actual result | Raw log SHA256 |
|---|---|---|
| `intake-three-proof-canary-001` | One actual T1 successor positive passed; 12 dependency warnings | `ec9bcd978e63d67aed3c46ceca04120e20ac5dfbc355ee01b374ac4203eb00c3` |
| `intake-three-proof-matrix-001` | 83 actual-proof, mutation/restoration and historical-caller checks passed in 54.87 s; 12 dependency warnings | `8b94bb6cce184e1f3ee559037f59944631881211f1365a41874e7b4f9a0caf1c` |
| `intake-three-lint-001` | Black 759 files, Ruff and mypy 52 source files passed | `05f0240121ab921f9fceb8e24a811cb2008523f83e0f978b918950dafb67ff27` |
| `intake-three-export-checksums-001` | All 81 public artifact hashes matched | `620e3b4fdf623532c6bd03b20f5f78a11ee8bbfb1c59b5e7be62070b944226fb` |
| `intake-three-native-review-check-001` | Native `record_review.py check --base HEAD` passed for 334 retained bundles, declared scopes only | `0c72c28a07c34bb7709f75957baeb667a92e07d9145d2341658e9dfda723e6fa` |

Full record science, unresolved source findings, corpus QC, reference validation
and integrated product regeneration remain separate work. No issue is closed
or previous scientific review superseded by these technical checks.
