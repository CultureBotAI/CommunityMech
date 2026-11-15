# GTDB reproducibility diagnosis — code006

The two failing GTDB tests reproduce locally at exact CommunityMech revision
`c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a`: **2 failed, 0 skipped**, exit 1,
205.67 seconds. This is diagnostic evidence, not a passing QC result or an
approved curation change. The local frozen environment uses Python 3.13.12;
the original M5 run uses Python 3.13.2, so the reproduction does not claim an
identical patch runtime.

The [machine-readable discrepancy ledger](native-discrepancies-002.json) parses the
completed native log, SHA256
`1423d2d13d60854e938ad7f29cf50f6dd7364017d1254954d32a68a73420b009`.
The raw log, execution receipt and prerequisite proof remain in the diagnostic
checkout's `.temp/gtdb-code006-20261115/`. Earlier parser outputs remain there;
output003 removes two pytest assertion-summary repetitions from the separate
three-row mapping list. Public output002 binds the final formatted parser;
the preceding public output and pre-format helper bytes remain retained.
No existing test or classifier was changed.

## What the failures count

| Native discrepancy | Rows |
|---|---:|
| UNRESOLVED → NOT_ATTEMPTED |337|
| UNRESOLVED → AMBIGUOUS |69|
| AMBIGUOUS → NOT_ATTEMPTED |6|
| AMBIGUOUS → UNRESOLVED |1|
| UNRESOLVED → NO_GTDB_EQUIVALENT |1|
| Candidate-list mismatch |78|
| Total status/candidate discrepancies |492|

These 492 rows cover 125 record filenames and 395 distinct record/label pairs.
They are not 492 taxa: a taxonomy occurrence can yield both a status and a
candidate-list error, and a record can repeat a taxon label. The raw error
format does not retain taxonomy indexes, so a label-pair count must not be
presented as a unique-organism or exact occurrence count. The second test names
three separate stored GTDB blocks. None of the six Phase 2 record filenames is
in either failure list; the ledger binds the exact six-record scope source.

Owners are [2848](https://github.com/CultureBotAI/CommunityMech/issues/2848)
(status/candidate reproducibility) and
[2849](https://github.com/CultureBotAI/CommunityMech/issues/2849)
(three stored blocks). Existing provenance and strain-lookup limitations remain
separate, including [624](https://github.com/CultureBotAI/CommunityMech/issues/624)
and [746](https://github.com/CultureBotAI/CommunityMech/issues/746).

## The source is identified, not inferred from its date

All probes use the preserved table SHA256
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
Its MD5 is `eca29d35869dd9035730caa12de12598`, exactly the artifact pinned in
kg-microbe's `download.yaml` at inspected checkout revision
`e3d1213a8bf7a4408204ebd48c19e42ec2e14b5e`; that file's SHA256 is
`209669d1de7e2dfea17712a755217fd201241d2e32f763366ff0570270610153`.
The native acquisition configuration describes this as GTDB r220 versus
NCBI 2025-07-28 and deliberately pins its copy instead of refreshing from an
unversioned upstream URL. No replacement source was acquired.

The old stored phrase `GTDB release latest (built 2026-07-25)` does not establish
a source release. The maintained `describe_mapping()` documentation records
that `latest` was a hardcoded literal and `built` came from filesystem mtime;
624 introduced content digests for new groundings. The inspected old blocks
lack such a digest. Their precise original crosswalk bytes therefore remain
unestablished by these strings. This evidence does not justify declaring the
current pinned table incomplete or automatically replacing it.

## One status case traced through its saved review

`Acidic_Nitrification_Minimal_Consortium.yaml` (000434),
`taxonomy[1].taxon_term`, has NCBITaxon:1763/Mycobacterium and UNRESOLVED since
its original September 26 commit `e88f1582f`. The current table has 2223 matching
higher-rank rows; the native resolver produces GTDB:g__Mycobacterium at the
same genus, with 18589/18589 named genomes and no alternative genus.

The November 5 immutable scientific review
`20261105T223042Z-pr2035-acidic-nitrification-successor` explicitly retained
UNRESOLVED and the unknown species/genome identity. Its broader identity
limits remain valid. Current native status semantics describe **computability
from the stored ID/label**: NOT_ATTEMPTED means the resolver can produce a
block that is absent. It does not establish that no human ever tried, that the
source's exact organism is known, or that a scientific review has been redone.

One unapplied scratch candidate runs the maintained native `--apply-status`
writer on an exact private copy. Its complete diff is one UNRESOLVED →
NOT_ATTEMPTED change plus one native append-only inline history event.
Candidate SHA256:
`4e9420a0704050b77742bc3bc48ac428572aa8a7d7d9c9d2c0bd7ba8ae8e86e3`;
receipt SHA256:
`785f174e6a5654c861e885bb4946df65d6c5cac0e18f0efcdf8457b287ff248a`.
Native exit 0 and nonempty candidate/log were verified. The canonical record,
historical review, source table and helper inputs stayed unchanged; the local
NCBI database's size/mtime stayed unchanged. Network acquisition was blocked.
No canonical application or native history sidecar was made. Independent
review subsequently found that this first receipt omitted the imported helper
implementation from its input manifest
([2851](https://github.com/CultureBotAI/CommunityMech/issues/2851)). Its bytes
remain unchanged; it is not the receipt to authorize a canonical application.
The corrected input binding has a positive, mutation-during-staging, restored
positive regression, with the expected failed pre-fix diagnostic preserved.

Corrected candidate002 completed through the same staging path with exit 0,
nonempty artifacts and unchanged inputs. Its separately reviewed candidate
SHA256 is `d58669e049476d801fa68cdb50184e6ac9c21c07cdbc2517ef32579f75acb7f8`,
and receipt SHA256 is
`d9e909d3eed4483e6d17c4cc41bd6fe3b23242e46edfb084c3b13ddd7b4e5bc3`.
The diff remains one status and one native inline event. Native stdout says
two taxa were processed; exactly one taxonomy entry changed. The imported
route helper now has a bound SHA256 of
`3aa215f1a720bebcc4109d61aacf73ad4697fe71e54eada23d0956446b65175e`.
Staging ran at c9 with these retained helper bytes; a later M5 application must
record its separate committed execution revision. That application and its
gates are pending at this report checkpoint.

The status writer checks taxonomy/ID alignment, duplicate keys, semantic
equality outside status/candidate fields, and append-only inline history.
A future application still needs explicit reviewed-input binding, canonical
concurrency checks, a native sidecar and relevant validation. No125-record
batch is authorized by this candidate. Any manual withholding or conflicting
scientific disposition requires individual resolution before inclusion.

## The three stored blocks have different failure mechanisms

| Record / source taxon | Exact pinned-source result | Boundary |
|---|---|---|
|000531, Microbacterium sp. BR1 /1070896|No exact ID or species-name rows; native result is null|The stored species-level Microbacterium lacus block is not reproduced. A genus-only diagnostic cannot establish that strain's species identity.|
|000532, Terrabacter sp. 2APm3 /1472881|No exact ID or species-name rows; native result is null|Stored provenance explicitly describes a genus-ancestor fallback. The native strain route has no such fallback. A separate genus lookup yields12/12 genomes and Actinomycetales/Dermatophilaceae, differing from the stored9/9 and Mycobacteriales/Intrasporangiaceae.|
|Industrial Bioreactor, Sulfobacillus acidophilus /53633|No exact ID row; two exact species-name rows,679936 and1051632, both state Sulfobacillus_A acidophilus|The native species-name route yields the suffixed name and4genomes; the stored unsuffixed name and1genome disagree directly with this source.|

The two isolate blocks were introduced by `201f5b09` (November8) and their
creation sidecars describe the new isolate baselines, without binding a
crosswalk hash. The older paired coculture000462 keeps these same strain IDs
UNRESOLVED. The Sulfobacillus block is inherited from `c8c398c2f` (September10).
An independent read-only SQL query of the available local NCBITaxon snapshot
returns the stored labels for all three IDs, each at species rank. It does not
resolve the crosswalk absences by renaming those IDs to the stored GTDB taxon.
These facts locate the provenance gap; they do not license arbitrary curated
flags, species reassignment, genus fallback, or automatic block replacement.

Helpers are retained under `scripts/adhoc/`: native reproduction,
`summarize_code006_gtdb_log_20261115.py`,
`inspect_code006_gtdb_route_20261115.py`, and
`stage_code006_gtdb_status_20261115.py`. The inspection helper prints only to
stdout. The staging helper is restricted to a new private namespace and has
no canonical-apply mode. No canonical, cache, classifier, validator, or old
review bytes changed during this diagnosis.
