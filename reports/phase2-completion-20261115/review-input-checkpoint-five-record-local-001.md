# Five-record private evidence package: local verification

The combined package is **verified locally** and its M5 transfer is **NOT RUN**. It includes the exact declared inputs and native YAML/Markdown of three saved reviews covering five maintained records:

- [EcoFAB 000025, dopamine 000516 and switchgrass 000087](../../reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.yaml)
- [Human gut 000122](../../reviews/structured/20261115T025440Z-phase2-gut-completion/review.yaml)
- [Brachypodium 000088](../../reviews/structured/20261115T025413Z-phase2-brachypodium-drought/review.yaml)

| Verified local property | Value |
|---|---|
| Reviewed source files and saved review pairs | 401 files; 64,786,342 bytes |
| Additional snapshot manifest | 1 file; 172,648 bytes |
| Additional standalone verifier | 1 file; 2,699 bytes |
| Complete proposed transfer | **403 files; 64,961,689 bytes** |
| Snapshot manifest SHA-256 | `da38c9123ade6a83f1cfbd0be22870e4bc0dc0428b0386aabe0f1c9bb6cbf0fe` |
| Prepared transfer-plan SHA-256 | `75678f85042d06764b777c6c6b17fc0b4a140a6a5155c7ff198618c2148333f3` |
| Planned one-file canary | Final three-record review YAML; 180,783 bytes |
| Canary SHA-256 | `8c0858a89c224421ab05a9a7a02cdb882e501f687fe5fef24a7d56ef4fc26563` |
| Standalone verifier SHA-256 | `f77728df53246eccfb8cf628807e654c6657d30102041f164c469848796a8096` |

The existing reviewed checkpoint helper validated the native review documents, exact Markdown rendering, every declared input SHA-256 and saved review pair before capture. It then checked the persisted snapshot's complete file inventory, sizes and hashes. Local transfer preparation copied and verified that snapshot again. Each review retains its own namespace and original relative input paths; versions shared between reviews remain distinct. Raw source bodies and private evidence are not published in this report.

The local plan, verified snapshot and transfer staging are retained under `.temp/phase2-brachypodium-20261115/` as `five-record-checkpoint-plan-001.json`, `five-record-checkpoint-snapshot-001/` and `five-record-checkpoint-transfer-001/`. The prior two-review attempt and blocked historical-input plans remain intact. No changed current source was substituted for a historical reviewed input.

The proposed destination is the fresh private namespace `.temp/phase2-review-input-checkpoints-20261115/final-five-001/` in the dedicated M5 CommunityMech checkout. The exact host and checkout are bound in the private reviewed transfer plan. This attempt has run only the local `prepare` command; it has no transfer-started marker, network-command logs or transfer receipt. It makes no remote-persistence claim. The [earlier automatic approval rejection](review-input-checkpoint-local-001.md) remains in force until the human approves this concrete payload and destination.

After approval, the reviewed launcher would copy exactly the one saved YAML canary using the same rsync file-list path and destination as the remaining files, verify its remote SHA-256 and size, then copy the remaining 402 files and verify the entire remote snapshot with the hash-bound verifier. It refuses existing attempt destinations, uses `--ignore-existing`, and has no delete operation.

This package preserves scientific evidence; it does not change the saved scientific verdicts or imply that every native check passed. The final three-record review retains 26 passed checks and one failed LBNL reference check for two exact supplementary-table snippets. Its source-correspondence and source-routing findings remain explicit. The other saved reviews retain their own limitations. Integrated technical QC and merge status are reported separately.
