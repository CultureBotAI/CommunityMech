# Approved Thermophilic and Sahara input transfers

The user explicitly approved both previously held payloads in this conversation.
On 2026-11-16, the exact three Thermophilic 416 files and two Sahara 494 files
were copied to M5 at `marcins-MacBook-Pro-3.local`, beneath
`/Users/marcin/agent-work/CommunityMech/gtdb-shrimp-thermophilic-sahara-20261115/`.
Each source-log canary was copied with `rsync -a --ignore-existing` and its
persisted remote SHA256 verified before the remaining files used that same
path. Every final remote hash matched its approved local source. Existing
files were preserved. These transfers did not apply either record or run QC.

The earlier automatic approval refusals remain retained, without alteration,
in `.temp/gtdb-shrimp-thermophilic-sahara-20261115/` as
`thermophilic416-transfer-refusal-001.md` and
`sahara494-transfer-refusal-001.md`. The new explicit approvals authorize these
payloads; no other pending transfer is implied.

All five input paths below are relative to `.temp/phase2-schema-20261115/` on
both hosts. The Thermophilic payload totals 1,859,202 bytes; Sahara totals
171,574 bytes.

| Input | Bytes | Verified SHA256 |
| --- | ---: | --- |
| `thermophilic416-source-binding-001.log` | 1,855,683 | `542824ce02648384346aabc49e8c70aaf39f608270903c5b209902cb26412af4` |
| `source-issue1932-snapshot-001.log` | 1,769 | `522792413616396d02a84ad7be4b57ab7df0be2b594fc369d802551745518005` |
| `source-issue1935-snapshot-001.log` | 1,750 | `7fb1d6ee9d66733a1fb6fa47bcce5191c915ba5c02dc269c70a9a4cedb92a967` |
| `sahara494-source-binding-001.log` | 168,866 | `bf2f16c15c82c111a2da8855345aad1d7b3df9c94e4daaea4f7e9e2aadea74cf` |
| `source-issue2924-snapshot-001.log` | 2,708 | `81ba949503c2c60b35c495d8c310603f752ecae36bf4a4b58e9fffadccc8c800` |

The existing repository recorder saved immutable log/JSON/exit triplets at
local revision `cb10773aa462f501fd07d41b766b80215b5b3858`. For each record, the
prefixes are `<record>-m5-metadata-canary-001`,
`<record>-m5-metadata-canary-verify-001`,
`<record>-m5-metadata-remaining-001`, and
`<record>-m5-metadata-all-verify-001`, with `<record>` equal to
`thermophilic416` or `sahara494`. All commands exited zero. The copy commands'
empty stdout is not used as proof of persistence: the independent SSH hash
readbacks provide that evidence.

| Actual remote readback | Completion UTC | Raw log SHA256 |
| --- | --- | --- |
| Thermophilic source-log canary | 01:46:52 | `2c2b2e7d3e0b5a8111c0991d58ad035c39ffb332c562d1fd38e878306109ce9c` |
| All three Thermophilic inputs | 01:47:52 | `7c5e879f53de366912c66820ce927e7569c87e3053118a5aae9d912ef7068750` |
| Sahara source-log canary | 01:48:25 | `092f042ecf4b35c191fae69b1e9088bdae462b996de028a02d205dea42b06e7a` |
| Both Sahara inputs | 01:49:17 | `c438b369ad92f0d8b9a2e1d68d1d4b583a6ed9448a0e490826e75371483d6043` |

The canaries establish the actual transfer path and persistent bytes. Source
adjudication, actual M5 staging, guarded application, native checks, saved
diagnostics, complete checkpoints and strict historical admission remain
separate obligations. No scientific finding or issue was closed by copying
these files.
