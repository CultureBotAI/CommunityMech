# Distinct GTDB source populations (#2833)

The official R232 correspondence workbook independently confirms the Mucin
record's stored **25** genomes for *Blautia hydrogenotrophica*. The native
crosswalk used for the newly reviewed gut record reports **15**. Neither count
has been changed to satisfy the corpus comparison.

The [official release index](https://data.gtdb.ecogenomic.org/releases/release232/232.0/auxillary_files/)
links the [bacterial correspondence workbook](https://data.gtdb.ecogenomic.org/releases/release232/232.0/auxillary_files/ncbi_vs_gtdb_r232_bacteria.xlsx).
One anonymous download on 2026-11-15 at 03:29:36 UTC persisted 860,792 bytes,
SHA-256 `e401d80c914c727268c184d19201aa35dcd23aabfd027a0d6e5a57476e71f3de`.
The server's Last-Modified header was 2026-04-14 09:07:34 GMT.

In worksheet **Species**, row **800** contains:

| NCBI species | Number of genomes | Number of R232 species | List of R232 species |
| --- | ---: | ---: | --- |
| s__Blautia hydrogenotrophica | 25 | 1 | s__Blautia_A hydrogenotrophica 100.0% |

The [metadata-only proof](gtdb-r232-blautia-source-proof.json) retains the exact
headers/cells, workbook hash, extraction-helper hash and semantic hash of the
stored Mucin classification. These cells verify the species correspondence,
denominator and fraction. They do **not** independently reverify the complete
higher-rank lineage or the numeric NCBI identifier. The semantic block hash
detects changes requiring review; it does not turn every field into a newly
verified source claim.

The gut record's retained native grounding receipt
`.temp/phase2-gut-20261115/grounding-roster-002.json` has SHA-256
`ba758094c3d1cef0c9f604bbe2b3a974c78f09881d2d198e25a4b109868a2f6f`.
Its `BH` row reports 15 genomes and fraction 1.0 for the same species through
the native `ncbi_id` path. The bound crosswalk SHA-256 is
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
That receipt is also an input of the saved full gut review. It does not establish
an unrecorded crosswalk release date or make its population equal to R232.

The bounded test change groups only the exact Mucin record, NCBI identifier and
reviewed semantic classification block into the independently verified R232
population. The immutable proof bytes are checked before accepting that group.
Every other record remains subject to the existing shared-population comparison.
Neither a `curated` flag nor arbitrary `mapping_source` prose grants an exemption.

Before the repair, the actual 15/25 control failed, while replacing the pinned
25 with 15 incorrectly passed. Controls also exercise conflicting counts within
one source, invented source labels, altered pinned assertions and changed proof
bytes. Raw before/after logs remain in the private code004 evidence directory.
The active M5 run at `012d755bdf591e1f0e814fddb52b0ad0aeddabaa` remains unchanged;
it will truthfully retain its original failure. The local repair requires a
subsequent reviewed revision and native run.

The saved helper is
[verify_gtdb_r232_population_20261115.py](../../scripts/adhoc/verify_gtdb_r232_population_20261115.py).
The first extraction missed the rank-prefixed species string; the original
capture, helper bytes and output remain preserved. Corrected extraction read the
same hash-verified workbook offline. No second download or source-record rewrite
was used. Workbook bytes remain private; this report publishes only metadata.
