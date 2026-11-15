# Final parser evidence and local native receipt persistence

Verified **2026-11-14 at 23:42:47 UTC**. All 25 files in the
[immutable reference-evidence list](final-reference-files-20261114.txt)
now match on M5 against the [local SHA-256 manifest](final-reference-local-20261114.sha256).
The [native verification](final-reference-remote-verified-20261114.log) records
25 successful comparisons. This includes final reference log/summary snapshots,
all earlier listed snapshots, parser canaries, the exact expected-record list,
and the two completed local parser-test triplets. It does not include the
running downstream native pipeline's output or any helper source.

The [before check](final-reference-before-20261114.log) found five identical
existing files and 20 missing files; no existing mismatch was found. The
[dry-run plan](final-reference-plan-20261114.log) identified 5,289,714 missing
bytes. Transfer used `rsync --archive --checksum --ignore-existing
--omit-dir-times --no-perms --no-owner --no-group --files-from=<exact-list>`.
The [100-byte canary](final-reference-canary-transfer-20261114.log) was the
completed local parser-guard log. Its [remote hash and nonempty-byte check](final-reference-canary-verified-20261114.log)
matched before the [remaining batch](final-reference-batch-transfer-20261114.log)
copied 19 files totaling 5,289,614 bytes. Existing files were not overwritten;
no file was deleted. The resulting 25-file evidence inventory is 7,202,808 bytes.

A final ignored/hidden-inclusive inventory covered **every local native raw
triplet currently present**: 35 JSON, 35 log and 35 exit files. All **105 files**
matched M5. The [exact file list](all-local-raw-files-20261114-final.txt),
[hash manifest](all-local-raw-20261114-final.sha256), and
[105 successful native comparisons](all-local-raw-remote-verified-20261114-final.log)
are retained. Both newly copied parser-test log hashes also match their native
JSON receipts; the prior 33 native logs were checked in the earlier persistence
audit. This establishes the current two-clone location claim before their
public evidence export, without revising earlier immutable receipts.

Only private evidence files were copied. No M5 code, environment, canonical
record, or source cache was a transfer input. The pre-existing divergent
`pr-body.md` drafts were not included and remain untouched. Later files require
their own verification; this audit makes no claim about future receipt creation
or the scientific correctness of native passes.
