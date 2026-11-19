# Optimized rumen 398 reference-correspondence checkpoint

Record 398 now has four native species-reference blocks and GROUNDED statuses
at indices 1-4. Three use exact NCBI species IDs; Lactobacillus delbrueckii 5812
uses a species-name fallback. Index 0, Streptococcus equinus 5640, retains all
three equinus/pasteurianus/ruminicola alternatives. All five optimized stocks,
source and NCBI names, quotations, biological content, three graph nodes, zero
downstream arrows and earlier history remain unchanged. Two native inline
events and one native sidecar record the bounded correction. This is a partial
technical diagnostic with `scientific_review: false`.

Actual staging, guarded application, all eight native checks and native review
persistence ran on M5 at frozen
`c9bb51a8b2a5591400dc8f170f043e59642116ce`, Python 3.13.2, named branch
`review/gtdb-final-four-m5-20261116`. Sorghum 348 completed the end-to-end canary;
Transwell 091 and LaCa 395 completed their saved-input checkpoints before this
application. Local copies are verified mirrors of actual M5 bytes, not a
second local application. Local proof/caller tests used Python 3.13.12 at
`bfe81b5d2a840c6f97c8a583ceddd4955222c128` with recorded working changes. No
clean-revision aggregate QC is inferred.

| Bound artifact | SHA-256 |
| --- | --- |
| Original record | `ee1333388f5d7353daf7713abf744220accf40a855bdbe8b66389f9b7c5031c6` |
| Actual candidate/current record | `ce1036c5582769e2e77ad179a68254a5c7516d9f78bc996095e9d56ff18b4380` |
| Actual stage receipt, `398-m5-candidate-001/receipt.json` | `3940c2557791cb4275dca39c967e9ecf9ca81ebc397901d0cbcca325e15c42dc` |
| Actual application receipt, `398-applied-001/receipt.json` | `1c63dd32bc4504570ec860962892a19bd418dcacdd5503a1709d96e81edd431a` |
| Native sidecar, `2026-11-16T013801Z-codex-6c2589.yaml` | `398795b7687832611441431f3f3f58039c80c1611cf31384caa620847a56378a` |
| Authored diagnostic config, `398-review-config-001.json` | `33a57b99216eabd1efa7182522b9895ef5be1dccda877b51e5b829557c307ebe` |
| Export config, `398-export-config-001.json` | `b24a021ad71a98cac215d22efb98ef1f58c78e4dc86cc46351ae53d727fd505b` |
| Public successor manifest, `398-001-successor.json` | `cc2ee66fc53f0e2405f1d051251138ac001484213c67bfbd7fe938d82ca470e6` |

Private stage/application paths are under
`.temp/gtdb-final-four-20261115/`; the sidecar is under
`history/records/Optimized_Rumen_Fiber_Degrading_SynCom3/`. Every gate used a
free plan followed by the actual command. Native schema, strict, GTDB
coherence, domain, scalar, new-history, history and term commands all completed
with exit 0 and unchanged captured inputs. Strict scanned one file with zero
errors; GTDB reported zero incoherent blocks, malformed lineages and conflicts.
Terms explicitly passed without an assertion denominator. All eight actual
logs and their input hashes were independently reviewed. Their raw artifacts
remain in `398-<gate>-001`; the public manifest binds each exported triplet.

The independently accepted [saved YAML](../../reviews/structured/20261116T014512Z-rumen-four-reference-diagnostic/review.yaml)
and [native Markdown](../../reviews/structured/20261116T014512Z-rumen-four-reference-diagnostic/review.md)
have hashes `129e0a5f8b873f0183d1d0667c7e66e6b696ef26693f2375bbd86486b63bf5bb`
and `7166e9e3cc8deb6a68cd2bef691a5f7e08006b0b36f572a5c43e28e32b2fa768`.
Both-host native audits verified all 82 inputs, 9,069,749 bytes, exact rendered
Markdown and unchanged captured bytes before caller edits. Complete private
checkpoints contain 84 files and 9,157,137 bytes each. Standalone verifiers
checked exact membership and hashes, with manifests:

- Local: `cca813f9ee1922e31b59b5411b731dd38e64fefe6d4371b9cd987ce88161b03a`.
- M5: `20c1db662db1f6fcad08faa45977b976ccfebabe90d709ed088f862ff762a734`.

Both checkpoints remain at
`.temp/gtdb-final-four-20261115/398-input-checkpoint-001/` on their respective
hosts. The independent reviewer also verified the complete local checkpoint
and read the actual M5 audit/verifier results. The unchanged exporter produced
27 public artifacts. Every persisted hash matched the accepted plan, and
actual stdout equaled plan stdout. Caller changes followed this preservation
and export boundary.

The fixed registry binds only the exact current transition. Batch 79 checks
parsed-current-document equality and strict admission before its biological
assertions. Only the old digest and last-LLM-event expectations use the
authenticated predecessor; the literal ledger, current rumen biology, sibling
records and separate Okeke historical path remain unchanged. Existing 348,
091 and 395 registry/test cases remain intact, and the shared proof engine is
unchanged.

The retained historical-before run passed nine tests and failed its old
last-event assertion on the new native event, which has no `llm_assisted`
field. After strict adaptation all ten historical tests pass. The positive
actual-proof canary's persisted one-pass pytest summary was inspected before
launching the 17-control matrix; its recorder finalized exit 0 about two
seconds after the matrix launcher started. Both finalized receipts are
retained, and no source or code changed during that wrapper overlap. The
17-control matrix includes the positive case, not an additional eighteenth
unique control, and includes mutation/refusal/restoration checks.

All recorder triplets below are retained under
`.temp/phase2-schema-20261115/`.

| Recorder | Actual result | Raw log SHA-256 |
| --- | --- | --- |
| `final-four-398-saved-audit-local-001` and `-m5-001` | Native pair and all 82 inputs pass; identical logs | `1c14a55c193bfcc13034967ceede1e491c7719224343c7da4a85c7dc33897a75` |
| `final-four-398-checkpoint-verify-local-001` | 84 files verified | `b2f80fa1d88a0321ceafc18f91041618b4bbc46e3a10664c1ea1795e7f4a975c` |
| `final-four-398-checkpoint-verify-m5-001` | 84 files verified | `83145f3ee0f63d76c6af0dd94d480af4c67cb915ab3b24937e1f21e86434b1bf` |
| `final-four-398-export-actual-001` | 27 artifacts persisted; all hashes verified | `08ee5e00af4e8ee13d820d538fa00acbcf1026ebddcbf996e7998936dfb3976d` |
| `final-four-398-historical-before-001` | Expected old-event refusal; 9 passed, 1 failed | `d3a4f24433107d0a1175ccbb70c0f07ec8cf2a7f459dd4c1cc050a30b255da8d` |
| `final-four-398-proof-canary-001` | 1 passed | `f9cd100e88b27fe93a461484c92a1285935575940a4764b4179ae71d647503cd` |
| `final-four-398-proof-matrix-001` | 17 passed, 12 existing warnings | `e81ca03ead406e8546bd9a556f3bbccfa65e2bade9d562a096bd838cd4468a15` |
| `final-four-398-historical-after-001` | 10 passed, 12 existing warnings | `60fdd4c7be85de26b3901fea1448c4118d1b592758be8eca0ce0f52e3dd14b82` |
| `final-four-395-398-lint-001` | Black 790 files, Ruff and mypy 52 source files pass on final code | `ff43b4c0c6750ccfafb2f1cc2dcf36269b613ec88b2159d133e61770d60c970e` |
| `final-four-398-current-input-post-caller-001` | Expected refusal naming changed batch 79 input | `a0eb6b151343ca5537110846e8f275b79afaddc606946a7af133b22b13b43944` |

The post-caller refusal is retained rather than weakening immutable input
checks or rewriting the saved review. Its original caller remains in both
complete checkpoints; current strict admission uses the verified public proof.
The native execution and saved-input audits remain distinct from later local
caller tests. Lint ran on the final reviewed code; subsequent changes are
reports only.

Species reference totals/fractions remain 376/1.0, 1/1.0, 574/0.99 and 7/1.0,
without invented support numerators or study-assembly matches. Five optimized
stocks remain separate from earlier designs; measured laboratory outcomes,
genomic predictions, time-specific cattle effects, nonsignificant fiber
trends and nested bags remain distinct. Durable engraftment and taxon-specific
causal effects are not established. Historical unresolved-grounding notes are
retained as earlier observations. Captured issue 1658 remains a non-graph
provenance limitation; the earlier issue 1655 graph correction is not reopened
or newly certified by this mapping.

No fresh snippet-comparison count, current generated products, whole-corpus
scientific completion or full `just qc` pass is claimed. Native whole-bundle
integrity was not rerun for this checkpoint; the exact saved pair and inputs
were validated as described above. Separate integration and existing CI
failure triage remain necessary. No merge is authorized by this report.
