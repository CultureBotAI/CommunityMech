# C2 native reference-cache effects

The C2 checkout started clean at
`e9ae9dee132ab210c87f76460c5d6247af9ea99c`. Native reference fetching changed
136 tracked cache files and created 31 untracked acquisition files. No tracked
changes occurred outside `references_cache/`. These runtime additions and changes
are preserved privately; they have not been committed or scientifically accepted.
The full native reference command exited 1. Its
[final inventory](reference-sweep-final.json) records all 549 expected paths,
535 native-pass results and 14 records with 103 retained errors.

All native checker/writer processes had stopped before capture at
`2026-11-14T23:41:13Z`. The complete current cache archive contains 975 files,
matching the ignore-independent SHA-256 file inventory; no symlinks were found.
The baseline archive contains the exact cache tree from the frozen C2 commit.
Both archives, the binary Git diff, complete Git status, tracked/untracked path
lists and file hashes remain under this private path in both fresh checkouts:

`.temp/m5-completion-20261114/final-c2-runtime-cache-capture/`

| Private artifact | SHA-256 |
|---|---|
| `baseline-cache.tar` | `121e17e80c109c50fad18d4262c7b9f2077c7e324bb64c2e555ae8d3d76b09a2` |
| `current-cache.tar` | `04d09c2b2f15849599e813d0c05817df7177cc1d931a33c9af87446873ca6d58` |

The local copies passed `shasum -a 256 -c archives.sha256` against the M5
manifest. Raw cache bodies and the binary diff are intentionally absent from
this public report.

## Capture verification

One actual changed cache, `doi_10.1099_ijs.0.65409-0.md`, was archived first
through the same native `tar`/`git archive` paths and output directory as the
full capture. Extracted current bytes matched the live source SHA-256
`7237a741dc90c6865dc31c46eb17e66a3e828cbcb91eebe783620e8c2a7bbc6d`;
extracted baseline bytes matched `git show` SHA-256
`8466cb915d13c51c0801276c9fb6298ac355c534b5b6bc21b602b49d3384aeb8`.
Only after these checks were the full trees captured. The complete current
archive's file count also matched the 975-entry hash inventory.

This cache contains the challenge-page enrichment defect filed as
[#2790](https://github.com/CultureBotAI/CommunityMech/issues/2790). Its exact
observed bytes were additionally preserved before the full capture. A native
matcher outcome does not accept newly fetched content as article evidence.

## Overlap with the six immutable scientific reviews

The independently checked [review cache manifest](review-cache-input-manifest.json)
identifies five distinct direct cache inputs across nine occurrences in the six
review bundles. Every final M5 hash below equals its **C2 baseline** hash. None
of these five paths overlaps the runtime-changed set.

| Reviewed cache input | SHA-256, identical at C2 baseline and final capture |
|---|---|
| `references_cache/PMID_36472419.txt` | `af090796fe581c590b97b09d340412fef5bc735f0b4c94e8cef3f92a31f4c1a6` |
| `references_cache/pmc_full_pmid_36472419.txt` | `da4d9680169efe9af031454a40a72612e1ee47f5d357e936a0a4056939e54b99` |
| `references_cache/PMID_40920748.md` | `e941bcf804a045b43ed4cede7eddc57cc7bf3fe078d5915d1d1d8a89660b217f` |
| `references_cache/doi_10.1126_sciadv.adg7888.md` | `53e9c9a977f934231d7855b11d459de2a740a0e474b908180c3d17fb9fac5150` |
| `references_cache/PMID_42660928.md` | `4b0186047599fd515aebc524d5e008ffbdf72ade572fc308443b60af2298bcdf` |

The private `review-cache-inputs.sha256` file records the final native hashes.
Four historical review occurrences have earlier hashes because three cache
headers were deliberately corrected before C2 and then reassessed. The public
manifest retains those predecessor hashes separately; they are not runtime
fetch changes. This comparison covers direct cache inputs, not every transitive
or private source used in the reviews.

No cache restoration was performed. The M5 checkout retains the native runtime
effects. The PR's tracked source continues to use the separately reviewed cache
edits.
