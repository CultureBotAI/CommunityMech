# M5 code004 outcome

The unchanged native run at
`012d755bdf591e1f0e814fddb52b0ad0aeddabaa` failed at the test stage.
It did **not** complete aggregate QC or start the global reference sweep.

The dedicated M5 checkout ran this exact command from 2026-11-15 03:21:05 UTC
through 03:36:52 UTC, with exit code **1**:

```text
/opt/homebrew/bin/just --verbose --no-dotenv --color never qc-references
```

This invokes the native full-QC dependency once. No `--no-deps`, test selection,
validator waiver or source edit was introduced during execution. The preceding
[plan](technical-evidence/phase2-code004-plan.receipt.json) was explicitly a dry
run. The [native history preparation](technical-evidence/phase2-code004-history.receipt.json)
fetched and verified the eight exact CI historical objects. The same launcher
then persisted a successful [single-record strict canary](technical-evidence/phase2-code004-canary.receipt.json)
before the full run.

The [completed receipt](technical-evidence/phase2-code004-qc.receipt.json),
[sanitized native log](technical-evidence/phase2-code004-qc.log.txt) and
[exit artifact](technical-evidence/phase2-code004-qc.exit.txt) retain the failure.
Pytest reported **10 failed, 5,751 passed, 103 skipped, 8 deselected and 18
warnings**, in 943.36 seconds. Skipped and deselected tests are not counted as
validated checks. Lint passed; the test recipe failed. The runner records
`validate-all`, `validate-taxa`, `validate-strict`, `validate-gtdb-all`, both scalar
gates, both term gates, `qc`, `validate-references-all` and `qc-references` as
**NOT RUN** after that failure. Prior scoped checks and the separate cache-only
measurement do not substitute for those unexecuted native stages.

The ten failures have six owners:

| Issue | Failed tests | Observed boundary |
| --- | ---: | --- |
| [#2830](https://github.com/CultureBotAI/CommunityMech/issues/2830) | 1 | Two former aggregate-taxonomy records remained in the blind-record inventory after their rosters were grounded. |
| [#2831](https://github.com/CultureBotAI/CommunityMech/issues/2831) | 1 | An old gut discussion still described the former Bacteria placeholder as current. The page faithfully exposed that stale record claim. |
| [#2832](https://github.com/CultureBotAI/CommunityMech/issues/2832) | 2 | Historical-fetch controls still expected five ledger bases, omitting three required scientific-review bases. |
| [#2833](https://github.com/CultureBotAI/CommunityMech/issues/2833) | 1 | The count comparison conflated a verified 25-genome R232 population with a 15-genome native-crosswalk population. |
| [#2835](https://github.com/CultureBotAI/CommunityMech/issues/2835) | 2 | The participant census still required a Switchgrass graph after source review preserved its earlier 18/17-stock observations as discussions. |
| [#476](https://github.com/CultureBotAI/CommunityMech/issues/476) | 3 | Two historical probes and one gap assertion still expected SupportingReference discussion excerpts to be omitted; native execution now traverses them. |

These are findings from this revision. Repairs and new scientific successors
must be independently reviewed and validated on their subsequent revision;
this receipt remains failed. Scientific limitations retained in the five full
reviews remain in force. A successful technical retry would not resolve those
scientific findings by itself.

The execution receipt's Python field describes the orchestration interpreter
(`/usr/bin/python3`, **3.9.6**). The frozen native environment was separately
verified as **Python 3.13.2**. The receipt also binds the runner, lockfile and
justfile hashes. Initial and final tracked Git status were empty.

Exact raw log/receipt/exit bytes were mirrored from M5 into the local private
evidence checkout and their hashes independently compared before export:

| Raw artifact | SHA-256 |
| --- | --- |
| Log (788,419 bytes) | `df138b077a8e7c03ed8e36b53da9f34fe129effad18a6748200dace313223969` |
| Receipt | `d9afa98335c20331205df5e8da024e365cf01fa755e3442d926a6f6314e7b76d` |
| Exit | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |

Private whole-directory `references_cache` archives were captured on M5 before
and after the run. Both are **47,403,520 bytes** with SHA-256
`2284f07a11f0e6482ce2cee3d6dd5cb1f7bde4e065554203c6a83c8aa273162b`.
They are byte-identical. The archive files remain private on M5; only checksum,
Git-index/status and native-Python metadata were mirrored locally. The archive
directory is `.temp/m5-completion-20261114/phase2-code004-runtime-cache/`.
No cache restore, fetch retry or subsequent validator run was used to produce
this outcome. The original November 6 checkout was not changed.

The separate five-record private evidence package remains local and its M5
transfer remains **NOT RUN pending explicit human approval**. The completed
M5-to-local receipt mirror does not claim that this different payload was sent.
