# Ambiguity correction integration

Integrated revision `5cc6f2aac3028551a062903825c928b080dc840e` contains the
actual M5 correction and [saved partial diagnostic](../../reviews/structured/20261115T061642Z-faecalibacterium-ambiguity-diagnostic/review.md)
for CommunityMech:000546. It retains all three native alternatives for the
existing species descriptor without selecting one as the identity of
A2-165/JCM31915. Study-stock nomenclature, original biological claims and the
historical scientific ledger remain unchanged.

The [M5 outcome](../gtdb-ambiguity-20261115/README.md) records eight completed
native commands at `4a5999d5`: seven validation commands and one history-sidecar
creation. A separate ROOT audit verified all 67 saved inputs (5,226,886 bytes),
native review validation and exact Markdown before the historical caller was
updated. The original inspected caller remains recoverable; the saved review
does not claim to have inspected its later successor.

| Integration check | Result | Raw log SHA-256 |
|---|---|---|
| Eight focused modules | 57 passed, 12 deprecation warnings, 19.37 seconds; exit 0 | `c5c32a623e7162fad6c0d4283bdbc8b7d39acd266543687c094c0c284dcd5622` |
| Native lint | Black: 708 files unchanged; Ruff clean; mypy: 52 source files; exit 0 | `eff350a5fa275c5f8e4b6b25fc3fd52ceea35d729d9347305e5de709a8f8bfa8` |
| Native isolate render | Correct identifier, nonempty HTML persisted; exit 0 | `bd05880184372be80cec843cb3edfa4e388bfbcc6a564d00ed58157e10667331` |

The unchanged command runner retained JSON/log/exit triplets under
`.temp/phase2-schema-20261115/`, with prefixes
`integrated-ambiguity-5cc6f2aa-001`,
`integrated-ambiguity-lint-5cc6f2aa-001` and
`isolate-render-000546-5cc6f2aa-001`. The focused test log is 822 bytes and the
lint log is 219 bytes. All three runs started from a clean tracked tree.

The retained isolate HTML probe is 54,846 bytes, SHA-256
`4191e20c603cef98dfe57e0ffbd606ae4a6d131d5e605f3e7a5baa904f28676f`,
under `.temp/phase2-schema-20261115/isolate-render-5cc6f2aa-001/`.
This record is outside the default `kb/communities` page population; the probe
adds no published page. These checks do not replace final combined M5 QC,
measured references or a full scientific review.
