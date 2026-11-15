# Five additional taxonomy corrections integrated

Clean combined revision `b4351920e3e150b6b78e1f775b8125fa5a637cc4` integrates
Pepper105, BL6 and the LDSynCom383, Community G387 and Fucoidan449 records.
Actual native M5 executions remain distinct from these integration commits.

| Scope | Integration commit | Native execution | Evidence |
| --- | --- | --- | --- |
| Pepper105 | `07f065092138d3a42a8084c5d86656ddd6ab7b23` | `b195783d` | [Canary outcome](../gtdb-ambiguity-five-20261115/105-canary-outcome-001.md) |
| BL6 | `2a60b609b80453134913c6675a446c6bdf83e261` | `849247f9`, following the distinct note execution | [Two-transition outcome](../gtdb-source-holds-20261115/bl6346-final-outcome-001.md) |
| 383/387/449 | `b4351920e3e150b6b78e1f775b8125fa5a637cc4` | `14d95aa2` | [Three-record outcome](../gtdb-species-fourth-batch-20261115/three-record-outcome-001.md) |

All five have eight passed native commands and immutable partial diagnostics
with `scientific_review: false`. Source stock identities, experimental conditions
and scientific limits remain explicit. No reference population is treated as a
fresh classification of an experimental stock's assembly. The BL6 proof retains
its real maintained2139 note intermediate and prior three scientific findings.
Pepper105 retains issues1690/1691; the three-record bundle retains its source,
causal and supplement-routing findings.

Before callers changed, independent native saved-pair audits verified all
captured inputs and exact derived Markdown. Complete checkpoints were then
independently verified both locally and on M5:

| Review scope | Input bytes | Complete checkpoint | Manifest SHA-256 |
| --- | --- | --- | --- |
| 105 | 78 inputs /6,205,960 bytes | 80 files /6,276,290 bytes | `78309720a138ec8fdc1ab982b01f339f4745406af141e6be9c19774b2863c04e` |
| 346 | 95 inputs /6,989,336 bytes | 97 files /7,075,192 bytes | `5ebd6d3460d2debf3085eb30e2a623abc2e8df8e909dd01ef0ad2ca970a20ce3` |
| 383/387/449 | 178 inputs /7,893,418 bytes | 180 files /8,080,936 bytes | `009c6c6bd8d0ccd623e3c77f557977c84aecf659749dd4b09733b9d1ba828106` |

Independent conflict-resolution review accepted only additive entries. The
ambiguity registry preserves Rumen275 and all old pins, adding Pepper105; its
SHA-256 is `cef74946063b67dc3f34d52ebb232e7805fbe6bc905424c4144bfb79bf990936`.
The species registry preserves the nine earlier third-batch entries and476,
adding exactly383/387/449; its SHA-256 is
`09b0a36b9f51bbb23c7960a7e7345ba08ddbcd3371110baddeaaf6556f2723f5`.
No shared proof engine, old ledger or current biological predicate changed.

| Clean combined run | Result | Raw log SHA-256 |
| --- | --- | --- |
| `integration-pepper105-rumen275-proof-001` | 34 passed;187 deselected;12 warnings;14.24s | `d99173369fb3c7e3d9a57b5122c7c1dcc450c0859b33f32d1da338ef121addaf` |
| `integration-bl6346-proof-001` | 27 passed;162 deselected;12 warnings;14.54s | `e6ce57a75ae4fdd0f7d40e80a2d48ab016ba2e469f520505dd66ca1cc8d798c0` |
| `integration-three-species-proof-001` | 51 passed;17 deselected;12 warnings;39.33s | `d14ac6fae8c4369048faff4ec080623376a62c36e0af710d709b20a09bd31989` |
| `integration-five-new-callers-001` | 55 batch83/11/5/23/42, composite-core and inventory drift controls passed;12 warnings;22.07s | `5968d1bc0a97fe017eb3d8f2c01522ad01906fdd62ef92b08518731fb753a05d` |
| `integration-five-new-lint-001` | Black759, Ruff and mypy52 passed | `3fb7076571879fba232cae18510f176ad9419e204fd8d39e563553a043f3a1d5` |

Exact command/log/exit triplets remain under `.temp/phase2-schema-20261115/`.
Overlapping leaf/native/integration controls are not summed. The independently
reviewed inventory helper fix under issue2897 has its own real file/HEAD drift
controls; [its report](assignment-byte-inventory-320b21d5.md) preserves the earlier
unprotected output and explicitly separates byte changes from completion.

There are now **87 integrated taxonomy corrections**, including **83 of the
historical126 partition**, with **43 remaining**. The corrected helper's fresh
byte scan also finds83 changed and43 unchanged at this revision, without using
that fact as review approval. Its output SHA-256 is
`7acb9b7abe0a0e6cace7f6e7d27e38c612e5987e480bde3f1ae7ee2c401f2941`.
The four later ambiguity applications and Amsterdam/FOS work are excluded from
these integrated counts. Full combined M5 QC, current generated products,
measured references and scientific blocker disposition remain unfinished.
The all-record campaign follows Phase2 and has not resumed.
