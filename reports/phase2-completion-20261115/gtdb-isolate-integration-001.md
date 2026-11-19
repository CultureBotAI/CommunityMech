# Isolate grounding integration checkpoint

Two further M5 corrections are integrated with their actual application receipts,
append-only history and immutable native YAML/Markdown assessments. Both are
partial technical assessments with `scientific_review: false`; prior scientific
findings and biological assertions remain unchanged.

| Record | Assessed correspondence | Actual M5 revision | Independently verified saved inputs |
|---|---|---|---:|
| [000552, Pelagerythrobacter N7](../../reviews/structured/20261115T060539Z-gtdb-genus-000552-canary/review.md) | Same-genus reference correspondence, 16/16 named reference genomes; no study-stock species or genome inference | `90a00bc2781266cb315a8295ca40e8f1c01e46fc` | 84; 4,813,906 bytes |
| [000555, JMP134](../../reviews/structured/20261115T055930Z-jmp134-gtdb-diagnostic/review.md) | Exact NCBI stock descriptor correspondence to the one-genome GTDB row; no assembly accession or population extrapolation | `f95ad0d731bc53634336ae7b794a7b23aa96a3c0` | 66; 4,838,169 bytes |

The independent audits verified every retained input hash, native review
validation, exact Markdown derivation and unchanged input bytes. These audits
verify persistence and provenance; they are not fresh scientific assessments.
The [genus proof](../gtdb-code006-20261115/batch147-genus-successors-001.json)
and [JMP134 outcome](../gtdb-species-status-20261115/jmp134-canary-outcome.md)
retain the scoped native checks and their limitations. The genus term check used
the native CLI with explicit local adapters; it is not relabelled as the literal
`just validate-terms` recipe.

At integrated revision `a2feecbbd92d63fb917b10e9430fdb54c0b9ddc2`, six JMP134,
shared-evidence and writer-provenance modules passed 77 tests with 12 deprecation
warnings in 16.93 seconds, exit 0. The immutable raw log SHA-256 is
`2fe6214dbd47823e7cf945ca8008c74985b2c18411cfcee872b814c75d7920f2`
(902 bytes). JSON/log/exit triplets are retained at
`.temp/phase2-schema-20261115/integrated-jmp134-a2feecbb-001.*`.
All 27 published JMP134 artifacts also passed an independent checksum check
after integration.

The subsequent combined tree at `fd8de406be0df55e9a1934f7ef7505a568f54b85`
passes the ten genus, species, joint historical-caller and writer modules:
97 tests, 12 deprecation warnings, 21.06 seconds, exit 0. Its raw log is
902 bytes, SHA-256
`7f50a1a1c4fc7781dd01acbd5c3ca21a497f1a8b2b8891e875ad9e66251e596d`.
The same tree passes native lint: 696 files unchanged by Black, Ruff clean and
52 source files accepted by mypy. The lint log is 219 bytes, SHA-256
`100b7c00c2673b12b7fb2cf9a87c943aee45936d8a5fbee418e1cd6db2920b97`.
Retained triplets use prefixes `integrated-genus-joint-fd8de406-001` and
`integrated-isolate-lint-fd8de406-001` in the same private evidence directory.
Only this report and its README link were uncommitted during those checks.

The native renderer also persisted two nonempty isolate probes with their
correct record identifiers. The 000552 page was inspected before the 000555
run, using the same launcher, environment and output directory:
`.temp/phase2-schema-20261115/isolate-render-fd8de406-001/`.

| Probe | Bytes | HTML SHA-256 |
|---|---:|---|
| 000552 | 58,383 | `1d1a071d95fa9ec99b3b83f52c81e232bf755227f02835eaa603e0c4270597c6` |
| 000555 | 54,707 | `f5fb3c1fb06e81d969a45ff7b3e8d61893c1feeb914886b6c3f030fb35e5701f` |

Both renderer commands exited 0; their retained log hashes are
`81fd37f36531b2b742b8fd9987fafe123a828a9ce8d19e09cd97e4d8e05f4537`
and `d886d4c552fb7b23f915e389743943eb8e42ba5315a4ec0bb3e48ea1afa58a9f`.
These isolates are outside the normal `kb/communities` page population.
No new published page was introduced and tracked `docs/` has no changes.

The historical scientific ledgers remain unchanged. Admission of either
corrected record requires its saved partial assessment and actual application
and source proof. Unknown changed records retain the exact predecessor-hash
requirement. Full corpus QC, the remaining status corrections and the subsequent
all-record scientific review campaign are separate, unfinished work.
