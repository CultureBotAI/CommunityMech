# Rumen status-only correspondence integrated

The [rumen275 checkpoint](../gtdb-native-null-275-20261115/rumen275-outcome-001.md)
is integrated at `c464cc8942f563721b4ace656dcf1cc9bac4176b`, after the narrow
native-null guard and source preparation. Actual M5 execution remains frozen
at `2b6e5ec23cae668529891650fcf4aba1c00bafba`. The selected Pseudoselenomonas
ruminantium member retains no GTDB mapping and now records the native unresolved
status with an empty options list. Its former three Selenomonas_A candidates
were not supported by the current native classifier. The other two members,
source names and biological content remain unchanged.

The new guard admits only an explicit null mapping, a fresh native unresolved
result, an empty option list and the single recorded `--apply-status` operation.
The existing resolver and classifier are unchanged. The older local NCBI name
failed the source binder; the current M5 name and synonym passed. Both results
remain recorded and neither taxonomy database was edited.

The immutable YAML/Markdown review contains three scoped assessments and eight
actual passed native checks. Independent verification accepted all 79 captured
inputs (4,831,055 bytes), the native pair and both complete 81-file checkpoints
(4,907,763 bytes). Local manifest
`cc6c9dd09a1273ef10cc0453265de9ba94e640dff5a04098d9590db4414986f5`
and M5 manifest
`1cf8ef1907832db88bb17ac2a9bf3de929bf1996082ea3ee57523c2d774148ca`
preserve the original caller before its narrow admission. All 27 exported
artifacts were hash-verified; the externally pinned successor manifest binds
the application and native gate evidence. The scientific assessment remains
partial with `scientific_review: false`; issue1268 remains open.

The clean combined revision `c464cc8942f563721b4ace656dcf1cc9bac4176b` passed:

| Retained run | Result | Raw log SHA-256 |
| --- | --- | --- |
| `integration-rumen275-core-001` | 91 shared-core, native-null guard and batch8 tests passed; 12 existing warnings; 30.99 s | `6694aa93dcc25756e0d1ce7df5f8d3df24334186331d12edc1dcecaad59115f6` |
| `integration-rumen275-actual-001` | 17 actual275 proof controls passed; 187 deselected; 12 existing warnings; 8.12 s | `fdc72ab4c4ee222213de0f5a0966c11d5bb7f13ec2e1405ccb49f1e51d2d0458` |
| `integration-rumen275-phage467-001` | 17 actual467 compatibility controls passed; 357 deselected; 12 existing warnings; 9.93 s | `93a083138c1e633c3bc346c7dc423647bbb0534d366c777900c020d0575fc36c` |
| `integration-rumen275-lint-001` | Black754, Ruff and mypy52 passed | `a1ab4a5ecac24ddf55a7c881df0f15379c8b04948d385fdd6d3b426821e8d682` |

Exact JSON/log/exit triplets remain under `.temp/phase2-schema-20261115/`.
These integration checks are distinct from the leaf checks and actual native
M5 checks; overlapping test counts are not added together.

The integrated count is now **78 taxonomy corrections**, including **74 of the
historical 126-record partition**, with **52 partition records remaining**.
Pending468,448,392,346,476 and other preparations are excluded.
Final combined M5 QC, regenerated products, separate measured reference checks
and scientific blocker disposition remain unfinished. The all-record campaign
follows Phase 2 and has not resumed.
