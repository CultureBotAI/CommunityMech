# Akkermansia source populations and lineages

The official R232 sources substantiate the manually retained Akkermansia
population and lineage in records 351 and 392. They do not make that population
equal to the pinned native crosswalk used for record 382. This source
adjudication addresses [#2833](https://github.com/CultureBotAI/CommunityMech/issues/2833)
and [#2948](https://github.com/CultureBotAI/CommunityMech/issues/2948); it changes
no canonical record, validator, threshold or historical proof.

## Exact source observations

The retained official [NCBI-to-GTDB R232 workbook](https://data.gtdb.ecogenomic.org/releases/release232/232.0/auxillary_files/ncbi_vs_gtdb_r232_bacteria.xlsx)
is 860,792 bytes, SHA-256
`e401d80c914c727268c184d19201aa35dcd23aabfd027a0d6e5a57476e71f3de`.
The new offline reader parsed the captured bytes, scanned all 9,623 Species
data rows and found this exact row:

| Selector | NCBI name | Genomes | GTDB species clusters | Leading GTDB species |
| --- | --- | ---: | ---: | --- |
| Species worksheet, row 34 | `s__Akkermansia muciniphila` | 1,806 | 110 | `s__Akkermansia muciniphila`, 73.09% |

The stored fraction `.731` is consistent with rounding the published 73.09%
to three decimal places. Neither the workbook percentage nor the stored
fraction is an independently observed integer numerator. The complete raw
four-cell row and all GTDB-column Akkermansia mentions are retained in
[workbook-inspection-001.json](workbook-inspection-001.json), copied byte-for-byte
from the actual extraction. Mentions in other NCBI-name rows are not pooled into
the 1,806-genome denominator.

A separate one-file taxonomy capture used the official
[R232 bacterial taxonomy](https://data.gtdb.ecogenomic.org/releases/release232/232.0/bac120_taxonomy_r232.tsv.gz),
with the publisher's [MD5 declarations](https://data.gtdb.ecogenomic.org/releases/release232/232.0/MD5SUM.txt)
and [version](https://data.gtdb.ecogenomic.org/releases/release232/232.0/VERSION.txt).
It persisted 9,886,191 compressed bytes, SHA-256
`d565d92730db443cd394a4b685ea682fe3691a3a1da3713804bbef2025d2cc71`.
Both compressed and expanded publisher MD5s matched; the same declaration also
confirmed the retained workbook's MD5. The helper parsed the verified captured
taxonomy bytes and rechecked its inputs before returning.

Of 878,998 bacterial rows, 2,323 have exact genus `g__Akkermansia`, all with class
`c__Verrucomicrobiia`. The exact named species has 1,372 GTDB taxonomy rows and
one full lineage:

```text
d__Bacteria;p__Verrucomicrobiota;c__Verrucomicrobiia;o__Verrucomicrobiales;f__Akkermansiaceae;g__Akkermansia;s__Akkermansia muciniphila
```

These 1,372 GTDB-name rows are a different selection from the workbook's 1,806
NCBI-name rows. They verify the lineage spelling, not an alternative NCBI
denominator. [lineage-evidence-001.json](lineage-evidence-001.json) preserves all
selected accessions, line numbers, exact lineages, source receipts and counts.
The raw workbook and taxonomy remain private local captures.

## Three current assertions

| Record and selector | Stored reference population | Class spelling | Source-stock boundary |
| --- | --- | --- | --- |
| Amsterdam 382, taxonomy[0] | 4,983 / fraction 1.0; native `ncbi_name` route | `Verrucomicrobiae` | Primary Methods name DSM 22959 and 16S identity confirmation; no study-stock assembly was classified here. |
| MUC2 351, taxonomy[13] | 1,806 / fraction .731; manual R232 tally | `Verrucomicrobiia` | Primary Methods report ATCC BAA-83. The record preserves that text and does not equate it with ATCC BAA-835. |
| MDSC 392, taxonomy[0] | 1,806 / fraction .731; manual R232 tally | `Verrucomicrobiia` | Primary Experimental Procedures 2.1 name DSM 22959T; the stock and type-strain assertion are retained, not newly established by these correspondence rows. |

The existing immutable Amsterdam
[native proof](../gtdb-code006-20261115/gut-pair-382-001-native-proof.json)
(`ce0d0aedaecc45d61db8575c131145f9380670a1d171e0eff145f32199b89a0d`)
has no exact NCBI 239935 lookup row, two species-name lookup row hashes, and the
complete 4,983 / 1.0 native result with `Verrucomicrobiae`. Its
[strict successor manifest](../gtdb-code006-20261115/gut-pair-382-001-successor.json)
binds the current record to that completed native computation. This is retained
execution evidence, not a fresh grounding run in this branch. The release behind
crosswalk SHA `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`
remains unestablished; no older/newer relationship to R232 is asserted.

The three whole records were read, together with the relevant primary stock
passages. Cache hashes are `32a05bcd...` (PMID 42007376, Methods stock list),
`d71d87de...` (PMID 42109165, Experimental Procedures 2.1), and `c1f6c5bf...`
(PMID 41960919, Materials and Methods). This is a bounded taxonomy/provenance
assessment, not a repeat of their full ecological, cultivation or causal review.
The original R232 bac120 metadata and exact experimental-stock assembly matches
have not been recovered or verified. Existing curation notes about type-material
genomes therefore retain that verification limit.

## Proposed bounded repair, not implemented

The source evidence supports comparison **within a verified source population**.
It does not support rewriting the manual R232 lineage to match the native
crosswalk, replacing the manual denominator with 4,983, or widening a numerical
tolerance.

An implementation should bind the exact current Akkermansia assertions in 351,
382 and 392 to these immutable source proofs. Different-source comparison may
then retain both observed lineages and denominators. All same-source hierarchy
and denominator consistency checks must remain active, including the two R232
records compared to each other. A `curated` flag, arbitrary `mapping_source`
text, changed record path, changed block or copied label must not grant admission.
Unknown or modified assertions must refuse pending source review. Controls must
mutate source bytes, lineage, denominator, fraction and identity, prove refusal,
then restore the actual positive source-bound case. No canonical change or
historical-note exemption follows from this design.

## Reproducibility and limits

Both helpers are additive and preserve previously executed inspectors:

- [inspect_akkermansia_r232_population_20261116.py](../../scripts/adhoc/inspect_akkermansia_r232_population_20261116.py),
  SHA `ded4c6ca0e561187b53dcb01ab5d52758049dd941a5be28b04460f595debe353`;
  actual workbook output `d5d7726fe35bd235df89d3bdd4480cf238e4ba5a3159a62ae4c578adfadbb296`.
- [capture_akkermansia_r232_lineage_20261116.py](../../scripts/adhoc/capture_akkermansia_r232_lineage_20261116.py),
  SHA `90b892536dec37faa462f143c634b5a13b0adfbe74091de26befc55a738a104b`;
  actual lineage output `3436d0cbc2fa8fa8bd29351af4b3da517517c060fcf2a91e5c71f716ac879589`.

Native recorder triplets are retained under `.temp/phase2-schema-20261115/`:

| Run | Result | Raw log SHA-256 |
| --- | --- | --- |
| `akkermansia-r232-workbook-inspection-001` | Exit 0; all captured inputs unchanged | `0db518e6833792b2abc455cd260de12ce987911adc2765dcdfbbdf7e9f7a5484` |
| `akkermansia-r232-lineage-plan-001` | Exit 0; fixed three-URL, bounded one-taxonomy plan | `7fc2710396a6407eb1726f301d63690e83ca17cb1e372466f9a5be22543a913c` |
| `akkermansia-r232-lineage-capture-001` | Exit 0; persisted capture and publisher checksums verified | `d2863d85d6d325f877882501ba7255146dcc8bdb363af889dd95539d191b3010` |

Execution revision was `d7350491aa238da3d158df30f535e84b5d4a9f8d` with the new
helpers recorded as untracked. Black and Ruff passed for both helpers. An
ignore-independent filename search covered local CommunityMech worktrees,
`.data` and `.cache`; it located R226 taxonomy, but no R232 taxonomy filename.
This bounded filename result motivated the official R232 capture, not a claim
that all possible renamed copies were absent. An initial display-only jq query
omitted a leading dot and refused; the corrected query inspected the unchanged
JSON. No native record validation, new scientific review bundle, canonical
application, test change, global QC or issue closure is claimed here.
