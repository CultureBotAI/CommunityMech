Wetland471's production admission now connects the original record to the
maintained source-identity intermediate and then to the already applied mapping.
The [composite manifest](471-production-composite-001.json), SHA256
`eed9e903b5c1e9934394b984e2206dc6586a01df643239a880bb1b5994c261e5`, pins:

| Stage | Immutable revision or proof | Record SHA256 |
| --- | --- | --- |
| Original historical record | `68699871415fda3c9eebf20382a315f9f3c7b17a` | `2191214bbc8d7f8bb6341c6493344e2180eb63fe2098375f44aab9f49d35d199` |
| Maintained identity intermediate | `faad27a2d22971ab0e50594ff4cb4fdf6f63d8c7` | `b3234d5f041636195f4c9867aaccd0df802d22ff5f2fbc28b904868ee02b901a` |
| Current mapped record | [Actual mapping proof](471-mapping-001-successor.json), `0e043890bd5c2df05f3ff350d877af65461a00755e0394da770a2db7e7b52889` | `78c62a010943afa65623c06ebd6778f04048bf553717685f10d1fee412a3a97e` |

The thin registry delegates both transitions to the unchanged, independently
reviewed fixed guard. Its first leg verifies the exact source correction,
saved assessment, eight native gates and historical 16-surface reference
measurement. Its second leg delegates to the unchanged mapping guard. The
returned historical bytes are the original record, after both transitions
have been verified. No record, source, native assessment, sidecar or existing
public evidence was changed by this admission work.

Batch133 adds only the fixed 471 dispatch. Its six existing admissions
(472, 474, 475, 476, 477 and 481), loaded-current-document equality guard and
all current biological predicates remain in place. Only the historical hash
and last-event assertions use the verified predecessor. The CI fetch command
and its exact-list test both add the maintained `faad27a2` commit. The earlier
`38f11cfa` source-fixture tests remain intact and retain their original meaning.

Verification ran in a fresh worktree based on published integration
`acb0d4b95c4b4ec7e3b2837ee2bcb611a5de08d6`, with the six reviewed files recorded
as working changes. Offline frozen installation passed on Python 3.13.12,
with unchanged lock SHA256
`712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4`.
Before editing, the original batch133 hash test failed specifically on current
`78c62a01` versus historical `2191214b`; its actual failure remains retained.

One real production canary passed first, reading the maintained Git
intermediate and complete public two-leg proof. Its nonempty receipt/log and
unchanged manifest, guard and current-record hashes were verified before the
focused suite. The later nine-test suite includes that canary, the other four
production controls, both batch133 tests and both historical-fetch controls;
the initial canary is not an additional unique test. Mutations exercise a
changed identity, an unknown target and already loaded current description,
history and graph documents, with positive checks before refusal and after
restoration. Persisted records and proofs are never mutated by these controls.

| Retained recorder under `.temp/phase2-schema-20261115/` | Actual result | Raw log SHA256 |
| --- | --- | --- |
| `wetland-production-batch133-before-001` | 1 failed, 12 warnings; 8.97s | `36daa7ca36765217cc499e0a9fb47be916da3e2ee4c74bd57cbae0a6f0acc67b` |
| `wetland-production-canary-001` | 1 passed, 14 warnings; 5.18s | `22ff075afb7e16ea0d2243188ad9d6e655734d6b383733ba8437dcf4f915bfb8` |
| `wetland-production-focused-001` | 9 passed, 14 warnings; 53.28s | `bd88322f71d1574f136be93084742c38459f8d9903eece217b4eb272a45a8f16` |
| `wetland-production-native-lint-001` | Black 790 files, Ruff and mypy 52 sources passed | `378a2a08fb8004a5f884f9fed576b8b21a44dcb2e766d3c10f2b64a381fbd6bc` |

The existing nonfatal directive warning in `gtdb_ground.py` remains in the
lint log; no native implementation was edited to suppress it. The final
six-file hashes match the independently reviewed versions and `git diff
--check` passed.

This completes the bounded production caller connection on this branch.
The [prior mapping checkpoint](mapping-outcome-002.md) accurately describes
the earlier period when the maintained intermediate was unavailable. Its
original M5 execution identities remain `af80bc09` for source correction and
`70090231` for mapping; no execution receipt or immutable input namespace was
rebound. The reference measurement remains evidence for the identity
intermediate, not a fresh comparison of the final record. The scientific
roster and graph findings retained under 2898/2899 remain outside this
technical admission. Generated products, clean combined integration and full
corpus QC remain separate; no merge approval is inferred.
