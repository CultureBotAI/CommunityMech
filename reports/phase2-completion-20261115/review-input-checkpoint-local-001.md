# Private review-input checkpoint: local attempt 001

The local checkpoint is **verified**. The M5 transfer is **NOT RUN**: automatic approval review rejected process launch because it did not find explicit human authorization for this private payload and destination. No SSH or rsync command executed, and no remote persistence is claimed.

The snapshot preserves the exact declared inputs and native YAML/Markdown for these two saved assessments:

- [Brachypodium 000088](../../reviews/structured/20261115T025413Z-phase2-brachypodium-drought/review.yaml)
- [Human gut 000122](../../reviews/structured/20261115T025440Z-phase2-gut-completion/review.yaml)

| Verified local property | Value |
|---|---|
| Files, including saved review pairs | 203 |
| Source and review bytes | 44,628,699 |
| Snapshot manifest SHA-256 | `c1e9f533946bc6ebd330d78a71edfc8a289b49685d0dbc992db6ab2779c9d9c5` |
| Prepared canary | Gut review YAML, 57,122 bytes |
| Canary SHA-256 | `ec301661050a11d2968e36efb03d39f97dbdf9158fa3e4db7b8c3b35a09c9366` |
| Standalone verifier SHA-256 | `f77728df53246eccfb8cf628807e654c6657d30102041f164c469848796a8096` |

Only explicit `source.inputs` and saved review pairs were read. Each reviewed version has its own review-ID namespace, including the original relative input paths. Every copied file was checked against its reviewed SHA-256; the completed snapshot was checked for exact file membership, sizes and hashes. The manifest is additional checkpoint metadata and is not included in the source/review byte total above.

The local plan and snapshot are retained under `.temp/phase2-brachypodium-20261115/` as `input-checkpoint-plan-002.json`, `input-checkpoint-snapshot-001/` and `input-checkpoint-transfer-001/`. The original source files and earlier plans remain intact. The linked-record draft `20261115T025004Z` was excluded because its EcoFAB input had changed; the earlier LBNL canary and earlier gut review also had changed historical inputs. Those exact mismatches remain recorded in the plan. No current bytes were substituted for historical inputs.

The prepared destination is a fresh private namespace, `.temp/phase2-review-input-checkpoints-20261115/brach-gut-001/`, inside the dedicated M5 CommunityMech checkout. It has not been created by this attempt. Transfer requires explicit human approval for the final concrete payload and destination. The reviewed launcher would copy exactly one nonempty saved review through the same native rsync file-list path as the remaining files, verify its remote SHA and size before continuing, preserve existing files, and run the hash-bound standalone verifier over the complete snapshot. It has no delete operation or overwrite mode.

The [local checkpoint helper](../../scripts/adhoc/checkpoint_phase2_review_inputs_20261115.py) passed six focused controls. The [transfer helper](../../scripts/adhoc/replicate_phase2_review_checkpoint_20261115.py) and [standalone verifier](../../scripts/adhoc/verify_phase2_review_checkpoint_20261115.py) passed four mocked transport controls, including canary failure, an existing destination, a modified file list and duplicate execution. These tests do not establish real remote persistence. Black and Ruff passed for the new code.

This is a durability checkpoint, not a new scientific assessment or a claim of Phase2 completion. Raw source bodies, database captures and the private snapshot are not published here. The forthcoming final three-record assessment will receive a separate local checkpoint before a combined payload is presented for approval.
