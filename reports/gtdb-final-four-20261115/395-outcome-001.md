# LaCa 395 reference-correspondence checkpoint

Record 395 now has nine native species-reference blocks and GROUNDED statuses,
with seven exact NCBI-ID routes and two species-name fallbacks. The exact
accepted application preserves all nine inoculum stocks, original source and
NCBI names, quotations, experimental boundaries, empty interaction graph and
earlier history. Two native inline events and one native sidecar record the
bounded correction. This is a partial technical diagnostic with
`scientific_review: false`, not new scientific approval.

Actual staging, guarded application, all eight native checks and native review
persistence ran on M5 at frozen
`c9bb51a8b2a5591400dc8f170f043e59642116ce`, Python 3.13.2, named branch
`review/gtdb-final-four-m5-20261116`. Sorghum 348 had completed its full canary;
Transwell 091 had completed its saved-input checkpoint before this application.
Local copies are verified mirrors of actual M5 bytes, not a second local
application. Local post-admission tests used Python 3.13.12 on published
`bfe81b5d2a840c6f97c8a583ceddd4955222c128` with the explicitly recorded working
changes. These are not clean-revision aggregate QC results.

| Bound artifact | SHA-256 |
| --- | --- |
| Original record | `4bd66811333c6960ebab5553e7ce71c8a4f92aa1d81f0fc2c9e2b4f6b75dac2e` |
| Actual candidate/current record | `a61c65e955695342999b9ec8b822740d1bd88e135de2d170a4890a2550a40475` |
| Actual stage receipt, `395-m5-candidate-001/receipt.json` | `d4d920934db1fe21896fa13b9f09493e04c5909b06759c27351d5c27ad8682b8` |
| Actual application receipt, `395-applied-001/receipt.json` | `ba2598fa9a9abe453d226666b0e0a20c0125b1f1bcd50eadd959d98af475df77` |
| Native sidecar, `2026-11-16T012133Z-codex-4e8002.yaml` | `4f4839e7b07203d5bef547fecede0deb919e61d13189c261632f006d2f07bc3b` |
| Authored diagnostic config, `395-review-config-001.json` | `dd6f200ceaf0bc11c8ad6be03f13e27c2f27ab91a024a80e62f758046b99fae9` |
| Export config, `395-export-config-001.json` | `c0fbec6605cf285d6d61d7a8a1aed33dc87ffd4380f0080fc22ee0e02fa7aa19` |
| Public successor manifest, `395-001-successor.json` | `c61d31cce2a289926e1f24702e7aca2f5fba26d10ba35def1206e8fe92a708b5` |

Private stage/application paths are under
`.temp/gtdb-final-four-20261115/`; the sidecar is under
`history/records/Nasal_SynCom_C_Bioreactor/`. The actual sidecar and both inline
events are append-only. Native schema, strict, GTDB coherence, domain, scalar,
new-history, history and term commands all completed with exit 0 and unchanged
captured inputs. Strict scanned one file with zero errors; GTDB reported zero
incoherent blocks, malformed lineages and conflicts. Terms explicitly passed
without an assertion denominator. Each raw command/log/exit is retained under
`395-<gate>-001`; the public manifest binds the exported gate artifacts.

The independently accepted [saved YAML](../../reviews/structured/20261116T012623Z-laca-nine-reference-diagnostic/review.yaml)
and [native Markdown](../../reviews/structured/20261116T012623Z-laca-nine-reference-diagnostic/review.md)
have hashes `f4e2191a86e57b2e07732b942743ef75fcf9f07140291b0c94be795677dbb5c5`
and `83a38c6a01657b61da57bad7a10b69eadebff3403ef7211f23f27e613a36169f`.
Both-host native audits verified all 80 inputs, 9,096,036 bytes, exact rendered
Markdown and unchanged captured bytes before caller edits. Complete private
checkpoints contain 82 files and 9,181,260 bytes each. Standalone verifiers
checked exact membership and hashes, with manifests:

- Local: `ab297b554b006828cfe71eb8baa448311fc19b0a74e6a299a2853e6cfa5f7850`.
- M5: `3cc50bf0982035d32ffa963a3c4378f71b31e6d98dd251e609250fad0e0629a4`.

Both checkpoints remain at
`.temp/gtdb-final-four-20261115/395-input-checkpoint-001/` on their respective
hosts. The independent reviewer also verified the complete local checkpoint.
The unchanged exporter produced 27 public artifacts; every persisted hash
matched the accepted plan, and actual stdout equaled plan stdout. Only after
that preservation boundary did the historical caller change.

The fixed registry admits exactly this manifest and predecessor. Batch 77
authenticates the current parsed document before biological assertions and
projects only the historical digest/event obligations. Its original unchanged
decision, zero events, empty graph, needs-research disposition and sibling
admissions remain intact. Existing Sorghum 348 and Transwell 091 cases and the
shared proof engine are preserved. The original historical run retained eight
passes and the expected unknown-changed-record refusal. After adaptation all
nine batch 77 tests pass. The positive actual-proof canary passed before the
17-control matrix, which includes that positive case rather than adding an
eighteenth unique control. Mutation/refusal/restoration controls remain active.

All recorder triplets below are retained under
`.temp/phase2-schema-20261115/`.

| Recorder | Actual result | Raw log SHA-256 |
| --- | --- | --- |
| `final-four-395-saved-audit-local-001` and `-m5-001` | Native pair and all 80 inputs pass; identical logs | `c7c091a937900398873de481f85da880f2ea42cc13a534e48027d8b3fb63077f` |
| `final-four-395-checkpoint-verify-local-001` | 82 files verified | `a81a6f40f5574761457621be3e172dac07385dddc07815f488a57060c6b8ce64` |
| `final-four-395-checkpoint-verify-m5-001` | 82 files verified | `73b1bdf57b7ca4ab46542bfc3bfe5481a5dfd182cd1708b0a448d5d8c5b5d934` |
| `final-four-395-export-actual-001` | 27 artifacts persisted; all hashes verified | `676a1c9731f639bf76f0ffdfee3c5f2a356ae153d66f6d78c33ce17d83abd54b` |
| `final-four-395-historical-before-001` | Expected refusal; 8 passed, 1 failed | `49684496faf53133ed8bc169fceb3dde0bbd5d1a2e90f09923ba2915e70e1946` |
| `final-four-395-proof-canary-001` | 1 passed | `2712b6b90ca40c4ebd695af8480adabba116212915a6fa953ced24f8818a381a` |
| `final-four-395-proof-matrix-001` | 17 passed, 12 existing warnings | `2641315609abab5e17d2c94c4e517f085f8643385fdc80e7e5ce09d1ddb219dd` |
| `final-four-395-historical-after-001` | 9 passed, 12 existing warnings | `29cfbed0084833e039a88736de81b7ad7b47adb0f3887de7186143a102934def` |
| `final-four-395-398-lint-001` | Black 790 files, Ruff and mypy 52 source files pass | `ff43b4c0c6750ccfafb2f1cc2dcf36269b613ec88b2159d133e61770d60c970e` |
| `final-four-395-current-input-post-caller-001` | Expected refusal naming changed batch 77 input | `aa5f0009be222090196eb4ccf642eacc6b64e5479d532a182ea7f19e3ae53254` |

The post-caller refusal is preserved rather than weakening immutable input
checks or rewriting the saved review. Its original caller remains in both
complete checkpoints; current strict admission uses the verified public proof.
The native execution and saved-input checks therefore remain distinct from
the later local caller tests.

Source-stock, preprint and publication limits remain as recorded in the saved
diagnostic. Reference totals/fractions do not supply support numerators or
study-genome identities. Ct C and Ph C retain explicit name fallbacks. The
nine inoculum stocks exclude the two challenge rows; all-nine persistence,
the proposed tyrosine mechanism and the empty graph remain unresolved under
[issue 1640](https://github.com/CultureBotAI/CommunityMech/issues/1640).
No fresh snippet-comparison count, current generated products, whole-corpus
scientific completion or full `just qc` pass is claimed. Native whole-bundle
integrity was not rerun for this checkpoint; the exact saved pair and inputs
were validated as described above. Separate integration and existing CI
failure triage remain necessary. No merge is authorized by this report.
