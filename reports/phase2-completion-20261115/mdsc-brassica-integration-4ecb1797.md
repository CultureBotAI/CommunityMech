# MDSC and Brassica diagnostics integrated

The [MDSC392 correction](../gtdb-source-holds-20261115/mdsc392-final-outcome-001.md)
is integrated at `1a7695d9`; the [Brassica476 canary](../gtdb-species-fourth-batch-20261115/476-canary-outcome-001.md)
at `4ecb17971a724c1434d092d96fab84aadebaa93b`. Actual native M5 executions
remain `f4e10146` and `14d95aa2`, respectively. BL6 source preparation is also
integrated at `abfd0aa8`, but its final mapping is not counted here.

MDSC's two notes and two mapping changes preserve fourteen study stocks and
four unselected manual R232 blocks. Its proof binds the real maintained0794
note intermediate and distinguishes crosswalk populations from the official
R232 worksheet and experimental stock genomes. Brassica's three mappings
preserve its four members, unresolved Leifsonia, source notes and all biological
claims. Its causal/interaction findings remain under issue2891. Both reviews
retain partial coverage with `scientific_review: false`.

Independent audits verified the actual M5 saved pairs and every captured input:

| Record | Captured inputs | Complete checkpoint | Manifest SHA-256 |
| --- | --- | --- | --- |
| 392 | 100 files /6,288,253 bytes | 102 files /6,378,505 bytes, both machines | `0b93c196dccaa1f133b36764b645c83fbac2fe98f326ae1ee3a1e9d9865e188e` |
| 476 | 78 files /6,922,593 bytes | 80 files /7,001,995 bytes, both machines | `328340dd13b93f48c72dd280b60b978fa0103b2b90e9ea1942e90b590eb597b2` |

Every public export artifact rehashed successfully. Each externally pinned
manifest binds its application and native gate evidence; original caller inputs
remain in the complete checkpoints. The leaf476 append-only check also passed
325 retained bundles with `declared_scopes_only`, not new scientific clearance.

The additive476 registry conflict was independently reviewed after resolution:
only its seven-line fixed allowance was added, preserving all nine earlier
species entries and every existing pin. The resulting registry SHA-256 is
`57ba8a5c9971419aa2ce633fd459a86f292666cc809c3037bf374ec9506644fc`.
Batch74 and batch133 continue to test current biological content; only strict
admitted predecessors satisfy their immutable historical hash/event obligations.

Clean combined revision4ecb1797 passed:

| Retained run | Result | Raw log SHA-256 |
| --- | --- | --- |
| `integration-mdsc392-proof-001` | 27 actual composite/mapping controls;135 deselected;12 warnings;19.60s | `6c4008326f16e3c9ff009a5da58046af66882a5efb7b5223bf88553d68eec060` |
| `integration-brassica476-proof-001` | 17 actual proof controls;12 warnings;8.53s | `d40c4450cedbc2748c088168fe2517e44cf750f2cfd67a9496f9a82fdb25c2f7` |
| `integration-mdsc-brassica-callers-001` | 24 batch74/133, composite-core and fresh-clone history tests;12 warnings;29.02s | `7027f0b35df2cbb9dca07f8863c851d10e0db20b8b6fa5c6293d6625f8964fce` |
| `integration-mdsc-brassica-lint-001` | Black757,Ruff,mypy52 passed | `f0e8657628460a68286bcc209ca988dd4bc9a1084b7a77216ca625fba252ca19` |

Exact triplets remain in `.temp/phase2-schema-20261115/`; overlapping native,
leaf and integration tests are not summed. Counts are now **82 integrated
taxonomy corrections**, including **78 of the historical126 partition**, with
**48 remaining**. Pending346,383,387,449, the new five-record group and other
preparations are excluded. Full combined M5 QC, current generated products,
measured reference validation and scientific blocker disposition remain
unfinished. The all-record campaign follows Phase2 and has not resumed.
