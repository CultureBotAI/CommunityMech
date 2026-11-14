# M5 retained-evidence persistence audit

Verified on **2026-11-14 at 23:01:02 UTC**, against the M5 completion checkout at
`e9ae9dee132ab210c87f76460c5d6247af9ea99c`. Its tracked files remained clean.
This is a persistence audit, not a new scientific review or a QC pass.

The existing `scripts/adhoc/check_m5_retained_sources_20261114.py` audited each
immutable review before and after replication. The five earlier reviews already
matched their saved local audits exactly. The post-curation review was missing
two retained proof files: `postcuration-diff-check.json` and
`postcuration-input-reassessment.json`. Both were copied without replacing any
existing file. All six post-copy audits now match the saved local audits under
`../retained-inputs/` byte-for-byte.

| Review | Retained input checks | Before | After |
|---|---:|---|---|
| EcoFAB canary | 52 | [matched](ecofab-before.json) | [all matched](ecofab-after.json) |
| Yolo soil | 32 | [matched](yolo-before.json) | [all matched](yolo-after.json) |
| LBNL SynCom | 39 | [matched](lbnl-before.json) | [all matched](lbnl-after.json) |
| Dopamine SynCom | 56 | [matched](dopamine-before.json) | [all matched](dopamine-after.json) |
| LBNL environment addendum | 15 | [matched](lbnl-environment-before.json) | [all matched](lbnl-environment-after.json) |
| Post-curation delta | 74 | [two missing](postcuration-before.json) | [all matched](postcuration-after.json) |

These are 268 per-review checks; shared paths occur in more than one review.
The audit compares actual file bytes with each saved review's SHA-256 values.

Replication used `rsync --archive --checksum --ignore-existing --omit-dir-times
--no-perms --no-owner --no-group`, excluding `final-c2-*` and the audit directory.
The [dry-run plan](m5-persistence-plan-20261114-v1.log) found 77 missing files,
totaling 285,163 bytes. The same rsync path first copied one 241-byte native-review
log as the [canary](m5-persistence-canary-20261114-v1.log); its saved receipt,
local file and M5 file agreed on SHA-256
`2bf93226f259af7759d2493131afc3fad744118c299ca0e1b20beaba09b163b0`.
Only then did the [batch](m5-persistence-transfer-20261114-v1.log) copy the other
76 files. No existing destination file was replaced and no file was deleted.
No new helper source or tested checkout code was installed on M5.

All 33 `local-*` native logs were checked against the SHA-256 values recorded in
their completed native JSON receipts. The [expected log manifest](m5-persistence-expected-log-sha256-20261114-v1.txt)
transcribes those retained values. Both [local verification](m5-persistence-local-log-verification-20261114-v1.log)
and [M5 verification](m5-persistence-remote-log-verification-20261114-v1.log)
returned success for every entry. A separate [99-file manifest](m5-persistence-local-raw-sha256-20261114-v1.txt)
covers all corresponding JSON/log/exit triplets; the [M5 triplet check](m5-persistence-remote-triplet-verification-20261114-v1.log)
also passed every SHA-256 check.

The final [checksum dry-run](m5-persistence-post-copy-checksum-20261114-v1.log)
found no remaining missing file in this bounded private-state snapshot. One
pre-existing difference was intentionally preserved: the private `pr-body.md`
draft. Its [local hash](m5-persistence-preserved-local-difference-20261114-v1.sha256)
is `b8b1435dc1b4636d8ccd6d5ac53b741ffd7aaac662fbe308a3b78f87db67cb87`;
the [M5 hash](m5-persistence-preserved-remote-difference-20261114-v1.sha256)
is `c58b2810fa66a3d879e2eafa62de63d3cbabe8684a186c893d4ba1fcd4ce85cd`.
That draft is neither a saved-review input nor a native raw-check triplet.
The [final HEAD/status receipt](m5-persistence-head-and-status-20261114-v1.log)
confirms the same tested commit and no tracked-file changes.

## Dated correction for issue 2789

At publication, the immutable receipts for `local-final-native-reviews` and
`local-writer-classification-regressions` said their raw logs remained in both
clones, although those two M5 files had not yet been replicated. That location
claim was premature. On 2026-11-14, verified at 23:01:02 UTC, missing-only
replication established both copies and checked them against their original
native receipt hashes. The earlier receipt bytes remain unchanged; this dated
audit records the correction. The exporter's unconditional wording remains
tracked separately in [issue 2789](https://github.com/CultureBotAI/CommunityMech/issues/2789).

Active `final-c2-*` files were excluded throughout. Their execution state and
later evidence exports are independent of this snapshot. This audit does not
claim that future local files have already been replicated, nor that C2 QC has
finished.
