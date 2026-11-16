# Transwell reference correspondence checkpoint

CommunityMech:000091 now stores five reviewed GTDB reference blocks and statuses.
The three C. subtsugae descriptors each map to a population of 25 reference
genomes, E264 to B. thailandensis with 6, and DC3000 to Pseudomonas_E avellanae
with 2; each native fraction is 1.0. These are correspondence populations, not
new assignments of study-stock genomes or formal renamings of source strains.

The Cv017/Cv026 reporter pair and the separate SC11/E264/DC3000 assay remain
distinct. The qualified SC11,368/SC11,378 discrepancy, source wording,
cultivation and causal limitations under issue 1467, historical lookup notes,
two observations without arrows and all earlier history are preserved. The
pinned crosswalk's release remains unestablished. The saved diagnostic is
partial with `scientific_review: false`; this checkpoint is not a new full
scientific assessment or source-snippet validation.

Actual staging, application and eight serial native checks used the isolated,
named M5 branch at `c9bb51a8b2a5591400dc8f170f043e59642116ce`, Python 3.13.2.
The accepted candidate `d0185ba94a608de9668f9a0a75c784685667e4821040987c33152e802e632489`
changed only five blocks/statuses and two inline native events. All 33 stage
inputs verified. Actual stage receipt `c8eaec1597a5cc0793311ff175a1ed6b7139f1906d94ce6c6112251166ae949f`
and apply receipt `92e9550fbb6366786a815c8d3b8888bc184ea13ffc70ee49865d5ca65ef2490b`
bind the original `51bf55d56342aa28864c0dd458a172209f9ef1e14e51a0cd210bb46521a17f47`.
The new native history sidecar hashes to
`13747baefd57c7887e3da00b3c80455e5865f13e17742e6a135bc3ac8082397c`.
Every actual native command exited zero with unchanged captured inputs;
strict validation scanned one file with zero errors and terms explicitly passed.

The fourteen required metadata inputs were inventoried together, transferred
through a verified one-file canary followed by the same bounded path, and
rehashed on M5. Existing matching common inputs were reused. Earlier source
anchor failure and additive correction under issue 2926 remain preserved;
initial SSH hostname-resolution failures did not mutate canonical bytes.
No previous denied payload was silently substituted or treated as permission.

The native [saved YAML](../../reviews/structured/20261116T010605Z-transwell-five-reference-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261116T010605Z-transwell-five-reference-diagnostic/review.md)
hash to `449a013a43bae1ef643894e6d22db8695623eab77ae7567bbe08fe84b786c2b2`
and `9032e8138bea27c4c2090028fe55a86ac790b570b4e33b2cbc1fbbc5a3786c01`.
Both hosts passed native saved-pair audits for all 85 inputs / 9,057,607 bytes
and exact Markdown. Complete checkpoints preserve 87 files / 9,145,446 bytes:
local manifest `b074f71741144290720ce2f4433a2b8dcae226afa2312828c6e25c765e0d56a3`
and M5 manifest `f3d97116f71a33ec0519626bbf6d1f24a4e6f588f02f81d59941e8abffc4d765`.
Root independently verified the saved content, all 85 inputs and all 87 local
checkpoint files before export or caller changes.

All 27 public artifacts rehash, and export plan/actual stdout are byte-identical.
The [strict successor manifest](091-001-successor.json) hashes to
`acc4ef8ccc5a81b2e7fbe6cdef606bf0ed2a6f56bd65bbb336cc4c9e9269070a`.
Its fixed registry delegates to the unchanged shared admission core. Current
biological assertions and their mutation controls remain direct; only the
old mapping clauses and old ledger hash use the admitted predecessor. The
original corpus census floors and exact five-unresolved versus one-grounded
delta now run against authenticated Git baseline `68699871415fda3c9eebf20382a315f9f3c7b17a`,
whose Transwell bytes equal the admitted predecessor. No floor was lowered
to accommodate today's other reviewed corrections. Batch 42's existing
historical Transwell route is unchanged.

Local validation ran at working revision `f3ecf5dba91f50c7b3c30daa4953c9cc7425f762`.
The independently coordinated Nasal 395 files were present during later local
checks but are outside this 091 checkpoint and publication.

| Recorder under `.temp/phase2-schema-20261115/` | Actual result | Raw log SHA256 |
| --- | --- | --- |
| `final-four-091-historical-before-001` | 7 failed, 1 passed; retained pre-admission mapping/hash/census failures | `e20466abf13536b4ce43f53b100684eab047094f4b5b4cd3cd0887f211385053` |
| `final-four-091-proof-canary-001` | 1 passed before the remaining proof controls | `915ad942ca2fcd87b16d4a240356558a416ead9fad7d5092ab7b9d489bb812ab` |
| `final-four-091-proof-matrix-001` | 17 passed, 17 deselected; actual 091 proof/registry controls | `37601cfe49dcaaeac8923860a601e840847fbb99ce055a0d44155131b0f2632c` |
| `final-four-091-historical-after-001` | All 17 participant and batch42 tests passed | `8deb61a22617a88974135481bd49b1b91ff82c7116e35e95fd18390ac008a916` |
| `final-four-091-lint-001` | Launch refused invalid `JUST_NO_DOTENV=1`; no lint pass claimed | `3e6bdd695c4f518ccb8857917f42178c0601fc4cfad25b5023237d9101c6ff3e` |
| `final-four-091-lint-002` | Black 790 files, Ruff and mypy 52 source files passed with explicit boolean environment | `ff43b4c0c6750ccfafb2f1cc2dcf36269b613ec88b2159d133e61770d60c970e` |
| `final-four-091-integrity-001` | Native append-only review integrity passed for 352 reviews, `declared_scopes_only` | `ce6e34d46d838756ee7ec7aea65db218d3cddfd9b19d6183e2008aff86dcd2fd` |

Native append-only review integrity completed with exit zero at 01:42:01 UTC.
Its 352-review count covers the declared scopes available to that invocation,
including the separate Nasal diagnostic; it is not a whole-corpus scientific
approval. Aggregate QC, corpus references, generated products, full scientific
completion and merge approval remain separate.
