# BR1: replace the unsupported M. lacus assignment with exact genome evidence

This read-only investigation addresses the GTDB identity of
`data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml`
(CommunityMech:000531), original SHA-256
`c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5`.
It is bounded source research for [#2849](https://github.com/CultureBotAI/CommunityMech/issues/2849),
not a full-record scientific review, applied correction or validator pass.

The stored `GTDB:s__Microbacterium_lacus` is contradicted by an exact assembly
identity chain. The [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_002812725.1/dataset_report)
identifies **Microbacterium sp. BR1**, NCBI taxon **1070896**, RefSeq
**GCF_002812725.1**, paired GenBank **GCA_002812725.1**, BioSample
**SAMN07351343**, and BioProject **PRJNA394223**. The BioSample describes BR1
from activated sludge collected in Birsfelden, Switzerland, in 2010.

The official [GTDB genome card](https://gtdb-api.ecogenomic.org/genome/GCF_002812725.1/card)
binds the same assembly pair, NCBI taxon, strain and BioSample to
**s__Microbacterium sp002812725**. Its
[release-specific taxon history](https://gtdb-api.ecogenomic.org/genome/GCF_002812725.1/taxon-history)
explicitly gives that species and the following lineage in **R220**, matching
R226 and R232:

```text
d__Bacteria;p__Actinomycetota;c__Actinomycetes;o__Actinomycetales;f__Microbacteriaceae;g__Microbacterium;s__Microbacterium sp002812725
```

This is release-specific evidence from the authority's history endpoint,
not an inference from a current card or a file timestamp. The separately
captured `/meta/version` value **2.28.1** is API software version, not a GTDB
database release. An independent R220 bulk taxonomy download and genome/ANI
recalculation were not performed.

The [2026 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13472149/)
(PMID42598292; DOI10.1021/acs.estlett.6c00474) uses BR1 in its Methods and
axenic/coculture assays. Its Introduction discusses a separate *M. lacus*
strain isolated from a soil mesocosm, citing the SDZm4 study
[PMID23396336](https://pubmed.ncbi.nlm.nih.gov/23396336/), while BR1's prior
work is separately cited. Those narrative references do not establish
BR1 = SDZm4 or BR1 = *M. lacus*. The exact primary XML was reused from the
parallel Terrabacter research capture, rather than fetched twice; its identifiers
and digest were independently verified here. The producer's initial capture
guard rejected the `pmcid` spelling; this report does not relabel that producer
attempt as successful.

The SHA-pinned NCBI2GTDB table
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`
has **zero exact taxon1070896 rows** and **zero exact BR1 species-name rows**.
The target GTDB placeholder species does occur in a row for **NCBI2079201,
Microbacterium sp. CJ77**, carrying `total genomes: 3` and `majority fraction: 1.0`.
That is a different NCBI population. The live genome card's species-cluster
count of **2** is also a different population. Neither is a BR1 crosswalk
denominator, and neither justifies retaining the stored BR1 counts of 1/1.

The source-supported disposition is therefore:

- Retain NCBITaxon1070896 and the BR1 strain identity.
- Correct the GTDB ID to `GTDB:s__Microbacterium_sp002812725`, the taxon label
  to `Microbacterium sp002812725`, and the lineage to the explicit R220 value.
  Correct the same obsolete GTDB name in the opening record description.
- Mark this deliberately selected assembly/history-based block `curated: true`
  with a `curation_note` explaining the exact stock/assembly/R220 chain and
  why the native crosswalk route returns no result. Record source URLs,
  capture date and digests in provenance; do not retain the unsupported
  `latest (built 2026-07-25)` mapping-source claim.
- Omit `majority_fraction` and `total_genomes`: their schema definitions refer
  to an NCBI2GTDB population, which this exact-genome route does not measure.
  These fields are optional. Do not insert the CJ77 row's denominator or
  the GTDB species-cluster count.

This is a reasoned curation proposal, not a flag added to make a test pass.
Application, append-only history, native checks and the final structured
scientific assessment remain with the curation owner. No canonical bytes,
reference caches, mapping table or ontology database were changed here.

The [machine-readable evidence](grounding-evidence-003.json) retains the exact
R220/current lineage, authority identities, crosswalk row, proposed disposition
and all source digests. The anonymous captures are private under
`.temp/br1-source-review-20261115/`; full text is not included in this report.

| Source | Bytes | SHA-256 |
|---|---:|---|
| NCBI assembly report | 3,588 | `d94ccc026216f2751d7d758e85c435a6f7464e797089ad9e639c8825b18c6dea` |
| GTDB exact-genome card | 5,279 | `3d9c1d568a0423d638dc272ab79ee1335e364472e172e7074d86df4438ca36e4` |
| GTDB release history | 1,750 | `f96b4c8f28a77e385d2017b66455022e621f0dfb1f9e4013cc4618f6ed31c583` |
| Primary study XML | 59,580 | `21e4eab4a11a23d72b2e0b22d83d6d98d8e0fb5897bb1485dfcbe484d80e9cb8` |

Provenance scripts are
`scripts/adhoc/capture_br1_authority_20261115.py` (one fixed anonymous endpoint
per invocation, exclusive private outputs) and
`scripts/adhoc/inspect_br1_grounding_evidence_20261115.py` (read-only exact
identity/hash/crosswalk checks; JSON on stdout). The first NCBI capture was
verified persisted and parsed before further authority captures. Black and
Ruff pass after replacing the XML parser with `defusedxml`; initial lint
failure and pre-fix metadata are retained privately. No new network call was
needed for that parser correction.
