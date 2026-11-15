# HT RW8: completed species-name correspondence canary

CommunityMech:000347 was applied on M5 at exact execution revision
`10810fc7c1346fbceb05503e7c2485ee4edc21e3`, after the reviewed replacement
[nine-record preparation](second-nine-source-binding-002.md). Only the existing
RW8 descriptor's GTDB block/status and two native inline events changed. One
native append-only history sidecar records the actual application. RW5, HT
membership, source quotations, biological endpoints, uncertainty and old history
remain unchanged.

The native route has no exact NCBI species-ID row for 72361 and uses the
species-name fallback: one reference genome, fraction 1.0, and
`GTDB:s__Bacillus_vallismortis`. This is a species correspondence, not an RW8
assembly assignment. OQ996934 remains a 16S accession. Source coverage remains
the cached abstract and labeled Figure 4 transcriptions; this pass did not newly
read the figure image, full paper or supplements. Crosswalk SHA-256 identifies
the exact bytes without establishing their upstream release or chronological
relationship to R232.

The [saved native YAML](../../reviews/structured/20261115T083337Z-ht-rw8-species-name-correspondence-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T083337Z-ht-rw8-species-name-correspondence-diagnostic/review.md)
are **partial, with `scientific_review: false`**. Their three authored assessments
cover the source identity, reference population and actual provenance. All eight
scoped native commands passed on the accepted current record, including ontology
terms and history. This does not establish whole-record scientific approval,
source-snippet coverage or a corpus QC pass.

The YAML is 31,162 bytes, SHA-256
`be66405c91a6c3b1eb68faeac3791066d0998f50892abee38e225d470bb4b6d4`;
Markdown is 41,679 bytes, SHA-256
`62e9f4fc6916786697701a8f954426e156967fd001008f0eadbb2ba4d997a314`.
All 81 inputs (5,121,544 bytes), native validation and exact Markdown derivation
were verified on M5 and locally, and independently reproduced by a separate
reviewer. Before any registry change, the full namespace plus saved pair was
snapshotted on M5, copied without replacing existing files and verified locally:
83 files, 5,194,385 bytes, manifest SHA-256
`32539cb67febeb00be683838cd166fc0ee399e5eae3ffd6618ec538cd67c811c`.
It remains under `.temp/gtdb-species-status-20261115/second-347-input-checkpoint-003/`
in both execution and local checkouts.

The [strict successor manifest](second-nine-347-003-successor.json) binds the
actual application, native history, complete public gate triplets and saved
review. Its SHA-256 is
`7d04740e4d7804b150dd8bd1fbd3ece154c434dc62cefffc17e52d5fa18afb7a`.
All 27 exported artifacts match the [hash manifest](second-nine-347-public-files-003.sha256)
and [on-disk verification](second-nine-347-public-files-verified-003.log.txt).
The explicit species registry delegates enforcement to the existing shared
admission core. The thin new test adapter reuses the shared positive and
tampering/restoration controls, adding unknown-record refusal. Batch 6's current
biological assertions remain unchanged; no predecessor projection or competing
edit to its other successor routes was needed.

The actual-proof and unchanged batch 6 tests passed **24 tests**, with twelve
existing deprecation warnings, in 22.80 seconds. The 823-byte log has SHA-256
`84a45d5ffe056665e036a1c157039ed52fa961a78813c82e5a16a97c28c47b8c`;
its raw local triplet is
`.temp/phase2-schema-20261115/species-second-347-actual-controls-local-003.{json,log,exit}`.
Native local lint passed Black on 679 files, Ruff and mypy on 52 source files;
log SHA-256 `b08d0ed8d45cc10e91e23a1f8a270eea18c382c34eb60b6843664678b51f933f`.
These checks are isolated canary evidence; combined integration, generated pages
and final full QC remain separate.

The new transfer selector's eleven focused controls and actual one-record M5
transfer precede any wider transfer. It fixes the duplicate/missing-ID defect
recorded in [#2873](https://github.com/CultureBotAI/CommunityMech/issues/2873),
while preserving the earlier executed selector and evidence. Independent review
also rejected the draft 002 phrase “older crosswalk” because release chronology
was unestablished. [The finding under #2877](https://github.com/CultureBotAI/CommunityMech/issues/2877#issuecomment-6891746632)
is corrected to “pinned crosswalk” in additive draft 003. The executed 002 config,
draft and metadata remain historical evidence; no native gate was rerun or
relabeled for that wording correction.

Record 392 remains entirely held under #2877. The remaining eight records in
this nine-record plan have not been applied at this checkpoint. Existing
scientific findings 2352–2356/2360 remain outside this mapping correction.
