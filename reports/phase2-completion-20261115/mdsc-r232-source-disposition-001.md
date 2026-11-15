# Retained R232 evidence for the MDSC hold

[Issue #2877](https://github.com/CultureBotAI/CommunityMech/issues/2877) holds the
entire MDSC record 000392 while two earlier curator dispositions are reconciled
with the pinned native crosswalk. Inspection of the retained official R232
workbook now shows that its Desulfovibrio population has a majority **unnamed**
species cluster. The current note's claim of no majority is inaccurate for
that source. This finding does not authorize a record change or release the hold.

The workbook is the exact anonymous download already retained for [#2833](gtdb-population-provenance.md):
860,792 bytes, SHA-256
`e401d80c914c727268c184d19201aa35dcd23aabfd027a0d6e5a57476e71f3de`.
An ignore-independent search across the CommunityMech work area recovered it in
the code004 evidence checkout. One-file copy verification confirmed its persisted
hash before the source receipt was copied and compared. No new download occurred.

The [read-only inspector](../../scripts/adhoc/inspect_mdsc_r232_correspondence_20261115.py)
captures the workbook, receipt, exact current record and helper bytes. It checks
the official URL, workbook hash and size, record hash and four-column header,
then reads all 9,623 data rows of the Species worksheet from the captured bytes.
It reports exact NCBI-name rows separately from mentions in the GTDB result
column, and checks all captured files again before returning. The nonempty
[metadata output](mdsc-r232-correspondence-001.json) is copied verbatim from the
actual run: 13,532 bytes, SHA-256
`c72f3372b3382ff7193121332e3c2a66ab09f627e657f47b3915509cec45b71c`.
Its source receipt, all selected raw cells and the two stored descriptors remain
inspectable; workbook bytes stay private.

| Exact NCBI name | Worksheet result | Meaning |
|---|---|---|
| Desulfovibrio piger | Row 544: 76 genomes, six GTDB species clusters | `Desulfovibrio sp900556755` has 57.89%; named `D. piger` has 22.37%, `D. piger_A` 15.79%, and three other clusters 1.32% each. This source has a majority, but that does not identify DSM 749T's genome. |
| Faecalibacterium duncaniae | No exact NCBI-name row under this spelling | This is not absence of the GTDB species. The name occurs in the GTDB result column of five different NCBI-name rows. |
| Faecalibacterium prausnitzii | Row 136: 948 genomes, 57 GTDB species clusters | The largest cluster is F. longum at 30.38%; F. duncaniae is 8.65%. This historical-name population is not an exact current-species or DSM 17677T population. |

The other four NCBI-name rows mentioning GTDB F. duncaniae are Coprococcus comes,
[Ruminococcus] lactaris, Butyribacter intestini and Faecalibacterium hominis. Their
different denominators must not be pooled or substituted for a current-species
correspondence. Cells do not independently verify numeric NCBI identifiers,
full lineages or any experimental-stock assembly.

The pinned native crosswalk `761d5537...` is a separate source. Its accepted
read-only route report records D. piger by name with 156 reference genomes and
F. duncaniae by NCBI identifier with 5,099 reference genomes, both with a reported
fraction of 1.0. Its GTDB release is unestablished: describing it as older or
newer than R232 is not supported by these artifacts. A source-note correction
and any subsequent descriptor correction require separate reviewed transitions;
neither the native result nor the R232 majority supplies stock-specific evidence.

All four manually curated R232 blocks, both held descriptors, the original
`FIX_MDSC_GTDB_GROUNDINGS` event and all biology remain unchanged. The original
ten-record proposal and its failed source disposition remain preserved; 392 is
outside the active nine-record species batch. The existing history must stay
immutable, with any correction explained by a new event and saved assessment.

The run used revision `a4a2f5d983a0179662d6861c6c6007ac4f0de70b`, with the new
inspector and an unrelated PAH source plan recorded as untracked. Its receipt,
exit and log are retained under `.temp/phase2-schema-20261115/` as
`mdsc-r232-retained-inspection-001`. Exit 0 establishes this bounded source read;
it is not native record QC, scientific completion or approval to apply a mapping.
