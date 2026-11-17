# Supplemental persistence of completed reference-parser snapshots

Verified **2026-11-14 at 23:20:10 UTC**. This additive audit covers exactly five
completed, immutable local diagnostic files under
`.temp/m5-completion-20261114/`. The live reference sweep remained active;
neither its output nor its code was replaced.

The [before check](parser-snapshots-before-20261114.log) found all five exact
destination paths missing. The [dry-run plan](parser-snapshots-plan-20261114.log)
identified 1,913,094 bytes. Missing-only replication used
`rsync --archive --checksum --ignore-existing --omit-dir-times --no-perms
--no-owner --no-group` with explicit filenames, not a directory sweep.

The [canary transfer](parser-snapshots-canary-transfer-20261114.log) copied
`final-c2-reference-parser-canary-001.json` first. Its
[M5 verification](parser-snapshots-canary-verified-20261114.log) confirmed
3,298 nonempty bytes and the expected SHA-256 before the
[four-file batch](parser-snapshots-batch-transfer-20261114.log) copied the
remaining 1,909,796 bytes. No existing file was overwritten or deleted.

All five copies passed the [remote SHA-256 verification](parser-snapshots-remote-verification-20261114.log)
against the [saved local manifest](parser-snapshots-local-20261114.sha256):

- `final-c2-reference-parser-input-001.log`
- `final-c2-reference-parser-canary-001.json`
- `final-c2-reference-summary-001.json`
- `final-c2-reference-parser-input-002.log`
- `final-c2-reference-summary-002.json`

The local parser helper was not installed on M5. This is a narrow exception
for completed snapshot files to the earlier audit's blanket `final-c2-*`
exclusion. Active C2 outputs, source files, environment, records, and caches
were not transfer inputs. This persistence result makes no claim about later
snapshots, current corpus completion, or scientific validation.
