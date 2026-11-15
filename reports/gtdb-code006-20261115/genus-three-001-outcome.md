# Three-record genus correspondence checkpoint

Six taxonomy occurrences in three records now carry native genus-reference
correspondences. Existing stock identities, experimental conditions, biological
claims, evidence and prior history remain unchanged. Reference-genome counts
do not identify the study stocks' species or assemblies.

| Record | Selected occurrences | Reference population | Retained scientific boundary |
| --- | --- | --- | --- |
| 000342 Z123 LDPE consortium | Nitratireductor Z-1; Gordonia Z-2 and Z-3 separately | 49/61; 450/453 for each Gordonia descriptor | Abstract-bounded strain roles and proteomic hypotheses; the two Gordonia stocks remain distinct. |
| 000390 peptide preparation panel | Kamptonema descriptor | 5/5 | C1/C2 preparations retain an empty ecological graph; Limnospira ambiguity and the three eukaryotic exclusions are unchanged. |
| 000406 A22ED9 consortium | Bacillus SK22 and KHED9 separately | 4,981/8,737 for each descriptor, across 44 reference genera | Genus correspondence does not resolve species, isolate genomes, exclusive biosorption, chromium redox or field performance. |

The guarded applications and all 24 scoped native commands ran on M5 using
Python 3.13.2 at `23d84a2d5567559a9693303c3ac9c07ff498e037`, through the
same shared engine and persisted launcher used for the accepted 000340 canary.
Source binding and staging ran locally with Python 3.13.12 at that revision;
the earlier native reporter receipts retain revision `dfe2fe44`. The crosswalk
SHA-256 is `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
Its recorded file mtime is not a database release.

Each record passed schema, strict, GTDB coherence, GTDB domain, scalar,
history creation, history validation and ontology-term commands. Each strict
TSV is a 34-byte header with zero error rows. Terms reported “Validation
passed” without an assertion denominator. These are scoped native checks,
not source-snippet matching or whole-corpus QC.

The public exporter persisted 81 artifacts, including exact application
receipts, source metadata, eight check triplets per record and three manifests:

| Record | Public successor proof | SHA-256 |
| --- | --- | --- |
| 000342 | [Manifest](genus-three-342-001-successor.json) | `ebd654e13f0d50704b6df613ecf3f70e2be0e737e1de3993576aead436a9f7ea` |
| 000390 | [Manifest](genus-three-390-001-successor.json) | `eccb05d97e0090aa425305e50d08889b9d713a37fb96112eac58010c8b1a3fa0` |
| 000406 | [Manifest](genus-three-406-001-successor.json) | `543cb76351719c0eb378f5ef7c214f2731f491fd6a6a8c32c20fc637976749be` |

The immutable [partial batch diagnostic](../../reviews/structured/20261115T072827Z-three-genus-reference-diagnostic/review.yaml)
has YAML SHA `0ac4a56fe5047a5d6117a812cde16b8f133cc7ac3eea49484ffc8c14e588a1eb`
and [native Markdown](../../reviews/structured/20261115T072827Z-three-genus-reference-diagnostic/review.md)
SHA `5f7417034c88bcd72d827f8d26833db1a323e0c6878a26d2672dff6d2345eb9f`.
Independent local and M5 saved-pair audits verified all 171 inputs
(7,199,804 bytes), native validation and exact Markdown. Complete private
checkpoints preserve 173 files (7,364,198 bytes), including the saved pair:

| Checkpoint | Repository-relative manifest | SHA-256 |
| --- | --- | --- |
| Local | `.temp/gtdb-code006-20261115/genus-three-input-checkpoint-local-001/manifest.json` | `e2f145cbfa25bc123998d41591be931fcb2e916a6dbf77ff4271c4b206445a9d` |
| M5 | `.temp/gtdb-code006-20261115/genus-three-input-checkpoint-m5-001/manifest.json` | `cab299315ba2a831b2d001b65e324676b84f1b80cfc559560a5db65b49594f88` |

The complete M5 checkpoint was also copied locally and verified. These
snapshots retain the original batch69/72/77 callers before their strict
successor admission changed. Historical scientific ledgers are untouched;
current biological predicates remain enforced. The three historical hash/event
failures are retained in `genus-three-historical-before-001.log` under
`.temp/phase2-schema-20261115/` (3 failed, 21 passed).

The actual 000342 proof passed the same-launcher canary: 17 positive,
mutation/restoration and production-registry controls. The remaining 000390
and 000406 proofs then passed 34 controls. Logs under the same private receipt
directory are `genus-three-successor-canary-342-001.log` (SHA
`b05ad778880647d1dab41f62b7282b46c51884e7688c0c354bc54b0a13269c19`)
and `genus-three-successor-remainder-001.log` (SHA
`1726d2d0d896201dc6146ba12edda1718d80963dc1063203033eca78dad7cc60`).
All controls use isolated copies of actual public evidence.

The historical callers, existing 000554/000340 actual proofs and shared-core
controls passed 96 tests (12 pre-existing deprecation warnings). The retained
log `genus-three-historical-and-existing-002.log` has SHA
`1b7e71915760164841ab59db4ee997c808389638f9c845b6b3faf57ee9837893`;
attempt001 is retained as a collection error from a mistyped test filename.
The isolated checkout did not claim execution of the absent 000401/000388
default proofs; integration runs those cases on the composed tree. Native
lint passed Black over 675 files, Ruff and mypy over 52 source files;
`genus-three-lint-001.log` has SHA
`9a97bb8cb5227fa9b2688478f631612583c3d6f1d5143b73a97e32ff490e529c`.

This checkpoint is partial and `scientific_review: false`. It preserves
the existing open scientific findings and does not close
[taxonomy repair #2848](https://github.com/CultureBotAI/CommunityMech/issues/2848).
Generated-page integration and final corpus QC remain separate.
