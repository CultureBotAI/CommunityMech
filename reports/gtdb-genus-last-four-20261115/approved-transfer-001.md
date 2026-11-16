# Approved genus input transfer

The user explicitly approved the eight previously held inputs, totaling
6,328,356 bytes, for the isolated M5 checkout
`/Users/marcin/agent-work/CommunityMech/gtdb-genus-last-four-20261115`.
The original automatic-review rejection remains unchanged in
`.temp/gtdb-genus-last-four-20261115/m5-private-transfer-rejection-001.md`.
This later approval applies to the named payload and destination; it does not
authorize a different rejected payload or bypass the per-record review gates.

The frozen lists remain byte-identical:

- `441-transfer-canary-001.files`: `98672b76bbfde2a108399c35ea075f159a5dc8c8148dea4307d9767d44e183d7`.
- `441-transfer-remaining-001.files`: `6bbfeb517ce1e5cd9a9d5a7662b048202891ac612ebf20f38a275f70f17e0344`.

Fresh M5 inspection verified the named branch
`review/gtdb-genus-last-four-20261115` at
`308081a8cf3f82472c542db87e135a5b96da61be`, Python 3.13.2, with unchanged
record 441 (`d4da92fc50e4b006fcaaf2d830d5c668e1e2671cea3b00655909a97a8c5e4bd1`)
and frozen lock (`712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4`).

The first dry-run incorrectly used `--from0` with these newline-delimited
lists. It refused a newline-suffixed missing path with exit 23 and copied
nothing. The failed triplet remains retained. The corrected dry-run used the
original list unchanged with normal `--files-from` parsing and passed.

The actual canary copied only `NCBI2GTDB.tsv.gz` with `rsync -aRi
--ignore-existing --files-from=...`. Its remote size was 2,895,086 bytes and
its SHA256 was the expected
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
Only after verifying this persisted file did the remaining seven files pass
their dry-run and copy through the same launcher, shell, environment and
non-overwriting destination. All eight final hashes and the complete byte
total matched. Existing files were not overwritten or deleted.

| Retained recorder under `.temp/phase2-schema-20261115/` | Exit | Raw log SHA256 |
| --- | ---: | --- |
| `genus-last-four-approved-m5-state-001` | 0 | `60a402ceb0dff2065803e8532ee78a1caab11427477f886162f5767506864279` |
| `genus-last-four-transfer-approved-plan-001` | 23 | `3e5dd251bd25c706466a7c99f594cf05b665cf32e8c064be0643414e8e5da931` |
| `genus-last-four-transfer-approved-plan-002` | 0 | `e000cb8e0c6701247267786ba27a1255d57133c0c9de3c4c407965d3260749a4` |
| `genus-last-four-transfer-approved-canary-001` | 0 | `e000cb8e0c6701247267786ba27a1255d57133c0c9de3c4c407965d3260749a4` |
| `genus-last-four-transfer-approved-canary-verify-001` | 0 | `149bdd0ff0dc2d5de80db3d982e3dd007970d92ca2a160c67e38277e80cd104d` |
| `genus-last-four-transfer-approved-remaining-plan-001` | 0 | `1529e8e792264efe3fe7e4e72aec74c1f40d4dbb3779af17457b571ed96471a4` |
| `genus-last-four-transfer-approved-remaining-001` | 0 | `1529e8e792264efe3fe7e4e72aec74c1f40d4dbb3779af17457b571ed96471a4` |
| `genus-last-four-transfer-approved-all-hashes-001` | 0 | `ef7ef103c83ec5fefa10eba06eacbc6be943d1aaffeb0d64a666e4b96614fa67` |

This transfer establishes availability of the approved source inputs. It does
not establish canonical curation or scientific completion. Record 441 must
complete the separately reviewed actual candidate, guarded application,
native gates, saved partial diagnostic and verified input checkpoint before
the remaining records can follow the same path. Original membership,
source-genome and mechanistic limitations remain unchanged.
