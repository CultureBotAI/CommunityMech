# Verified private checkpoint on M5

The user explicitly approved this exact checkpoint and destination. Transfer
completed on 2026-11-15 at 03:44:17 UTC, with exit 0. A complete review YAML
served as the one-file canary; its 180,783 bytes and SHA-256 matched on M5 before
the remaining files were copied through the same rsync path. The destination
was new, and the transfer refused overwrites.

Destination relative to the dedicated M5 Phase 2 checkout:
`.temp/phase2-review-input-checkpoints-20261115/final-five-001/`.
The original stalled checkout was not changed. Private source bodies remain
private; this report contains only verification metadata.

| Component | Files | Bytes | Verification |
|---|---:|---:|---|
| Evidence and review snapshot | 401 | 64,786,342 | Every manifest entry rehashed on M5 |
| Snapshot manifest | 1 | 172,648 | Exact expected manifest hash verified remotely |
| Standalone verifier | 1 | 2,699 | Exact approved verifier hash verified remotely |
| Approved transfer total | **403** | **64,961,689** | All three components verified |

The plan's `files_verified=401` counts the evidence entries; it excludes the
manifest and verifier. Automatic approval initially held the transfer over
this count difference. An ignored-inclusive file inventory and byte/hash checks
established the exact approved 403-file total before the unchanged transfer
command was allowed to run. Neither rejected attempt launched SSH or rsync.

| Artifact | SHA-256 |
|---|---|
| Snapshot manifest | `da38c9123ade6a83f1cfbd0be22870e4bc0dc0428b0386aabe0f1c9bb6cbf0fe` |
| Standalone verifier | `f77728df53246eccfb8cf628807e654c6657d30102041f164c469848796a8096` |
| Canary review YAML | `8c0858a89c224421ab05a9a7a02cdb882e501f687fe5fef24a7d56ef4fc26563` |
| Transfer plan | `75678f85042d06764b777c6c6b17fc0b4a140a6a5155c7ff198618c2148333f3` |
| Completed raw transfer receipt | `800170c29e5ae207004cd5f87efb7364cd2510cf7e4f25b23288a0a8aaf8890c` |

The raw plan, completed receipt, stdout/stderr for all eight transfer steps and
exit artifact remain in the Brachypodium evidence checkout under
`.temp/phase2-brachypodium-20261115/five-record-checkpoint-transfer-001/`.
The committed [transfer helper](../../scripts/adhoc/replicate_phase2_review_checkpoint_20261115.py)
and [standalone verifier](../../scripts/adhoc/verify_phase2_review_checkpoint_20261115.py)
describe the exact checks.

This immutable checkpoint contains the three-record full review
`20261115T031503Z-phase2-three-record-final-science`, the Brachypodium review
`20261115T025413Z-phase2-brachypodium-drought`, and the earlier gut full review
`20261115T025440Z-phase2-gut-completion`: five records in three bundles. The newer
gut historical-scope successor was not substituted into this approved snapshot.
Its committed bundle and additional private inputs remain separately retained.
Successful replication establishes durability, not scientific approval or QC.
