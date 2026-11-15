# Dairy-panel mixed-rank correspondence canary

CommunityMech:000384 now contains two source-scoped database correspondences:
the Synechocystis genus descriptor maps to `g__Synechocystis` from 8/8 filtered
references, and the Desertifilum tharense species descriptor maps by exact NCBI
identifier to `s__Desertifilum_tharense` from one reference. These populations do
not identify the unnamed experimental stocks or their genomes. The two eukaryotic
descriptors retain `NO_GTDB_EQUIVALENT`.

The change preserves the paper's four monocultures, four paired cultures and
four sequential treatments, nonsterile background, source quotations, stock
uncertainty, empty ecological graph and prior scientific findings, including
issue 1537. It does not turn the cultivation panel into a universal four-member
inoculum. The actual application changed only the two declared GTDB blocks and
statuses, appended two native inline events and added one native history sidecar.

The [immutable review YAML](../../reviews/structured/20261115T093433Z-dairy-panel-mixed-rank-reference-diagnostic/review.yaml)
and [native Markdown](../../reviews/structured/20261115T093433Z-dairy-panel-mixed-rank-reference-diagnostic/review.md)
contain three assessments. This is a partial technical diagnostic with
`scientific_review: false`, not a replacement for the historical scientific
review, source-reference validation or final corpus QC.

| Actual transition or proof | SHA-256 |
|---|---|
| Canonical predecessor | `4fc81cfb17b74f44b121440c5375d5a8e2f42e76b60ee057fdc53deafa263831` |
| Actual M5 candidate and canonical successor | `0b837a73e603469d21643996c0564bdbc93d1f9852833fb789529257965dbce1` |
| Actual M5 stage receipt | `c13d4f12187f40218d19cc547bba55ce7bba8056a53ca26f36e956c26f8149a8` |
| Actual apply receipt | `1aad8d549e9ba0a799d39acf76998467cfa85c76d1f5babe23aa576f6fb96383` |
| Native history sidecar | `2da658ef8b90e3836e62c80f053fe83e43a1756b1477ee6e3bcd19dcb17cbd5d` |
| [Public successor manifest](genus-mixed-384-001-successor.json) | `bd8fd08c99cf2bf97298e93cc67719d4bdabd6266fb4e995f6e563878a55ad8e` |
| Saved review YAML, 31,460 bytes | `73e94a1b2e657327465ecb278d1a21671d2a1a2cd14e46377b5a1c99029c4551` |
| Native Markdown, 42,324 bytes | `86f6e18271e0fb670f24dd8584f6b6668fffa4dd377c9f79553db741f5a07c03` |

Source reporting and binding ran locally at
`ead20c0392805c2810d49e9a57aa2fd710578145`; their changed-tree receipts are
retained. The single-record reporting canary preceded the six-record read-only
route inventory. That inventory did not authorize or apply the other records.
The accepted source-binding proof is
`2807c5a43b6221eb4fc372abd3d36d293166cc3f1973cc0f65fd229bb7c39a4f`.
The local candidate remains retained separately. Fresh M5 native staging differed
only in its two actual event timestamps, which were independently reviewed
before application.

Actual M5 staging, application and checks used a fresh isolated checkout at
`70ef731cc6c35d9ffe08a391c9db2b4adb10abf4`, frozen offline development dependencies
and Python 3.13.2. The existing shared engine, matcher-independent taxonomy
classifier and gate runner were unchanged. The crosswalk remains exactly
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
its file mtime is not a release identifier. Local ontology observations are
stat-bound, not full database-checksum claims. No new literature acquisition,
provider call or article-cache change occurred.

All eight dry-run commands passed, followed by eight actual exit-0 commands:
schema, strict, GTDB coherence, domain, scalars, new-history, history validation
and terms. The strict TSV persisted as a nonempty 34-byte header-only artifact.
The native new-history command persisted the exact sidecar bound above. Terms
reported `Validation passed` without an assertion denominator; no examined-claim
count is inferred from that message.

The shared audit verified all 79 inputs, 61,443,698 bytes, native review validation
and exact derived Markdown on both machines before caller edits. Complete
checkpoints then preserved 81 files, 61,517,482 bytes, including the review pair.
Both checkpoints' exact membership and hashes were independently verified.

| Complete retained checkpoint | Manifest SHA-256 |
|---|---|
| Local `genus-mixed-384-local-input-checkpoint-001/` | `dfcc1812027eebdebc5d4c54a4468052244c4ee1d053adc3164745009cd15dd6` |
| M5 `genus-mixed-384-input-checkpoint-001/` | `a05573e31e87abc9cd87b9850432e4495d5ea814ed7af400e708f661b15e94a4` |

These namespaces are beneath `.temp/gtdb-code006-20261115/` in their respective
checkouts. Later caller edits deliberately make a new current-tree checkpoint
refuse: batch 59 is the only changed captured input. The other 78 inputs and
the saved pair still match. Both complete checkpoints preserve the exact old
caller; the later refusal does not replace the successful original audits.

The unchanged public exporter passed its plan, published 27 artifacts and
verified every artifact hash after writing. The hash-check output is
`d70079dfce8678d0c58d6b8bded0ce64338e24375bc762ba43228fff51c7bb8c`.
The manifest binds actual application, source evidence, sidecar, review pair
and all eight gate triplets. Sanitized public logs retain explicit raw and
derived digests; raw native outputs remain private and unchanged.

The historical caller initially rejected the changed canonical hash. Its narrow
successor admission now verifies the actual proof and uses the protected
predecessor only for the historical digest and last old `llm_assisted` assertion.
All dairy and unrelated Kefir biological predicates still inspect current
documents, with an explicit current-document equality guard. The shared mutation
engine was unchanged.

| Persisted local run | Actual result | Raw log SHA-256 |
|---|---|---|
| `genus-mixed-384-historical-before-001` | Expected old-hash refusal: 1 failed, 0.38 s | `96efe192ceca46d6a8a4150ac87082b6b2fce55f29cb8d630401420de7608842` |
| `genus-mixed-384-actual-canary-001` | 17 passed, 255 deselected, 12 warnings, 18.16 s | `faf63db843b17340629d6c44cf6340438823d25265a2122e0d43e2cb32dd8c4b` |
| `genus-mixed-384-historical-after-001` | 8 passed, 12 warnings, 2.88 s | `e33cef03c69aced7cc70c00e95f45b60120f294b82c5685ae93517227763511a` |
| `genus-mixed-384-lint-001` | Black 679 files, Ruff and mypy 52 source files passed | `b08d0ed8d45cc10e91e23a1f8a270eea18c382c34eb60b6843664678b51f933f` |
| `genus-mixed-384-post-caller-inputs-001` | Expected refusal: one changed caller input, exit 1 | `c6acb009ee2c735f8d0bbce457c741d26c2a9a7347dc6a04f1afa49924fad1e8` |

The post-caller inventory is an expected current-path refusal, not a failed
original checkpoint.
Local proof and lint receipts bind the changed working tree based on the same
`70ef731c` preparation commit. This canary establishes the bounded mixed
genus/species application, persistence and proof path, not the correctness of
other records or final corpus QC.
