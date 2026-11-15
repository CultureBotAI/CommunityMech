# Adopt the approved SupportingReference merge

The explicitly approved [Claw PR #1219](https://github.com/CultureBotAI/culturebotai-claw/pull/1219)
merged through its required queue at `2026-11-15T08:21:28Z` as
`68d8b2b6e02c1ca4fda2524f348460ecfa566402`. All merge-group workflows passed.
The remote feature branch was deleted by GitHub, and its local branch was removed
after preserving the original checkout and evidence at detached `bb67dda8`.
An isolated checkout of the actual merge supplied the downstream governance code.

CommunityMech commit `78673fc6eab55e2c3745aec6f12ac87cf8494122` adopts that
merge in `scripts/.vendored_canon_ref`. Native governance found and changed only
this pin: the already adopted SupportingReference schema bytes remain SHA-256
`cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11`.
The new pin file SHA-256 is
`cfb2d8425f0b4fa2a3c77636c68644002c140281181d69d4186d4c78671595e9`.

The independently reviewed [adoption helper](../../scripts/adhoc/adopt_merged_reference_pin_20261115.py)
preserves the earlier executed adoption helper. It validates the exact repository,
clean source and target revisions, native CLI configuration, pin-only plan and
preimage bytes. Application uses `LockManager` and the native transactional
synchronizer. Post-application governance found no remaining drift. A second
review independently checked the actual receipts, saved preimage, configuration
logs and one-file Git diff. No other consumer was adopted; sixteen unconfigured
consumers were explicitly outside this invocation.

Both operations ran on clean `87bb3989393e2bb6afaeaa3e2c1d9bc063f56b36`.
Their exclusive evidence directories are under
`.temp/phase2-integration-20261115/`, with the names below. Each receipt is also
the verbatim stdout of its separately recorded command.

| Operation | Result | Receipt bytes | Receipt SHA-256 |
|---|---|---:|---|
| `merged-reference-pin-plan-001` | Plan verified; target unchanged | 1,368 | `8dd7d51685ee073a4baa9c7cf722a22b37952f464239f459bcb0c083111c7af0` |
| `merged-reference-pin-apply-001` | Applied and verified | 1,375 | `c31c32920a0d1a9e27a249994eba4cc31701261910c8bd285798c819f3bcf85f` |

The saved preimage is the former pin `fde0154a8f2d56514a738c4800657348391c2b66`,
file SHA-256 `76ce001530ab4dbf2ae08e4bbb27216f72a983e398b3c059d9679f3a8233381a`.
Recovery is a reviewed revert of the pin commit; no shared history rewrite or
change to a live Claw deployment is needed.

At clean `78673fc6`, the native reference-CLI coverage, vendored-workflow and
historical-fetch modules passed **12 tests** with fourteen existing warnings in
28.77 seconds. Native lint passed Black on 739 files, Ruff and mypy on 52 source
files. No files changed during these checks. Recorder triplets are retained under
`.temp/phase2-schema-20261115/`:

| Run | Result | Log bytes | Log SHA-256 |
|---|---|---:|---|
| `merged-reference-pin-integration-001` | Exit 0; 12 passed | 1,612 | `e0a3100215d36e23da9bb45e9938ebb3bcea1d8d4f091cc6bb180de5051db60f` |
| `merged-reference-pin-lint-001` | Exit 0; lint passed | 219 | `e79f0489b3248b94fffec4d0343233904c920258373301f80e509efb9d91d361` |

This records the approved upstream merge and downstream branch adoption. The
CommunityMech PR remains unmerged. Existing frozen M5 executions keep their
recorded revisions. Full combined M5 QC, reference-source blockers, regenerated
products and the subsequent all-record scientific campaign remain unfinished.
