# Isolated M5 product-label verification

The complete product run passed at published revision
`f471548888761bd217084c4405a9a5d4e222251a` on 2026-11-15. A fresh, independent
M5 checkout and frozen offline environment preserved the separate active code006
checkout, its environment and reference cache. The reviewed product helper first
completed one Yolo canary, then ran the full batch through the same `nohup`,
`UV_OFFLINE=1`, Python environment and `--validate-labels` path. No canonical
record, reference cache, validation exception or ontology database was changed.

| Run | UTC interval | Native exit | KGX nodes / edges | Structural errors / warnings | Native label outcomes |
|---|---|---:|---:|---:|---|
| [Canary](canary-001.receipt.json) | 04:38:55–04:39:51 | 0 | 13 / 13 | 0 / 0 | 10,390 canonical; 5 configured exceptions; 596 non-adapter skips |
| [Batch](batch-001.receipt.json) | 04:42:01–04:43:16 | 0 | 1,538 / 2,535 | 0 / 0 | 11,395 canonical; 4 synonyms; 5 configured exceptions; 1,112 non-adapter skips |

Each run completed rendering, KGX export, strict KGX structural validation and
the exact native `just --verbose --no-dotenv --color never validate-products`
recipe. The batch KGX manifest records 512 community inputs. The native label
recipe includes canonical communities, reusable taxa, isolates and generated
KGX node pairs; the canary's label counts therefore exceed its 13 KGX nodes.
Configured non-ontology identifiers and prefixless identifiers are skipped under
the existing policy. The summary provides no per-prefix skip census; these rows
were not ontology-validated. Existing exceptions and synonym acceptance remain
visible, with no new waiver beyond the reviewed `uuid` namespace classification
in [#2844](https://github.com/CultureBotAI/CommunityMech/issues/2844).

All four canary products were checked against native receipt SHA-256/size values
and preserved before the batch regenerated those paths. All four full products
were independently checked and preserved afterward. Their verified values are
embedded in each public receipt. The final full render restored the tracked
checkout exactly: `git status --porcelain=v1` was empty. Native final product
hashes, actual Python 3.13.2 / uv 0.6.13 / just 1.58.0 versions and revision are
retained in [the final verification output](m5-final-product-verification-001.txt).
This output was captured locally from read-only SSH; it is not asserted to have
been copied back to M5.

Raw native receipts, eight stage logs, original canary/full products and lookup
evidence remain privately on M5 and in a local mirror. The native
[M5 checksum listing](m5-raw-checksums-001.txt) was captured after completion and
compared against the local bytes before export. Its SHA-256 is recorded in both
public receipts. The original product runner binds implementation and product
hashes but does **not** bind its logs: the public receipts explicitly distinguish
this independent post-completion log verification. Public logs and receipts were
sanitized by [the evidence exporter](../../scripts/adhoc/export_product_label_evidence_20261115.py)
and preserve raw/public SHA-256 values. Raw evidence was not overwritten.

| Stage | Canary log | Full batch log |
|---|---|---|
| HTML render | [log](canary-001-render.log.txt) | [log](batch-001-render.log.txt) |
| KGX export | [log](canary-001-export.log.txt) | [log](batch-001-export.log.txt) |
| KGX structure | [log](canary-001-validate-export.log.txt) | [log](batch-001-validate-export.log.txt) |
| Native labels | [log](canary-001-validate-labels.log.txt) | [log](batch-001-validate-labels.log.txt) |

The local machine's earlier same-revision canary002 remains failed: 21 label
mismatches and 5 missing identifiers, with no unknown prefix; canary001 remains
an explicit missing-UO skip. On M5, all seven used ontology adapters resolved to
already downloaded builds, and direct [native NCBI lookups](ncbi-label-snapshot-001.log.txt)
confirmed `Lodderomyces parapsilosis` for 5480, `Aspergillus` for 5052 and
`Candidatus Sodalinema alkaliphilum` for 3723519. The local output instead gave
`Candida parapsilosis`, `Aspergillus <genus>` and an absent identifier. These
observed environment differences are tracked in
[#2852](https://github.com/CultureBotAI/CommunityMech/issues/2852); exact ontology
release dates and whole-database hashes were not established. No record was
recurated to accommodate the older-looking local labels.

This is completed **product** evidence, not a replacement for the failed code006
aggregate, a completed reference audit, or scientific approval. Historical failed
runs and remaining scientific findings retain their separate dispositions.

The exporter was checked with two focused controls: unchanged evidence passes;
changed product bytes fail both before and after updating a host checksum;
zero-exit native `SKIPPED, NOT PASSED` fails; restored inputs pass. Black, Ruff
and `git diff --check` also passed. Local control log SHA-256:
`f82a884500ee5dacbcd40ace23ee4917c67c68b8178ae024959f221c789faae5`.

The additional local writer-inventory run initially reported four passes and
five setup errors: its internal `uv run` attempted build-dependency acquisition
before this new local worktree had its own installed environment. That log is
preserved as `export-writer-controls-002.log`. After a frozen offline install,
the identical two-module invocation passed all nine tests in 115.52 seconds,
without changing production source, tests or exemptions. The passing log remains
`export-writer-controls-003.log`. Neither local preparation outcome changes the
completed M5 native product results above.
