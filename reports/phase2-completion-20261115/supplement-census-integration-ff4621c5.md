# Supplement, saved reviews and census repair integration

The combined branch at `ff4621c5b8e019d77608a88d19084abe654abe33`
includes the reviewed supplement adoption, the current full Switchgrass
assessment and both-host checkpoint, completed Transwell091/Nasal395/Rumen398
technical diagnostics, and four bounded CI repairs. Full combined QC is still
incomplete. The all-record scientific campaign has not resumed.

## Integrated work

The supplement adoption through `02fed876d9672d0a8cb6a57107ba42e605585006`
adds three explicit supplement-cell locators without changing their quotations.
It retains the exact owned runtime revision
`6b71e7f4b353b5b36000fda03da78b61734e3fc8` and lock SHA256
`1e1374a77207de170502a89ea7eebcb018d65daac8b0faecc39988d955f3df62`.
The runtime's separate full-suite limitation remains recorded in issue2934;
its draft PR1 has not been approved or merged.

The new immutable Switchgrass review
`20261116T011931Z-switchgrass-full-source-successor` has 30 assessments,
`scientific_review: true`, and outcome `needs_curation`. Its YAML SHA256 is
`83d4aa59145ddd04383bb61c29f19dc73c778a6d54967bedbb3db7b97ebfba0d`;
the Markdown SHA256 is
`135982ead076883634dc9c5a76a706e2e9eceb0cb9bc413832ab249f28be0735`.
The substantive Methods/Table S1 roster discrepancy under issue1548 remains
open. Supplement routing is resolved for this record; matching a quotation
does not resolve its biological interpretation. The
[M5 checkpoint report](../switchgrass-full-review-20261116/m5-checkpoint-001.md)
records all 86 inputs and both complete 88-file checkpoints. Its frozen
execution revision and old failed receipts remain unchanged.

Final-four commits `bfe81b5d2a840c6f97c8a583ceddd4955222c128` and
`9116659f6880fd34eab0d90827a1ec1de9e18a2d` add the three completed
technical transitions and their strict historical admissions. Each record has
eight actual M5 native gates, a saved partial diagnostic, both-host input
checkpoints and public provenance. Their diagnostics retain
`scientific_review: false`. The assay-specific findings and historical
biological predicates remain in force. See the
[final-four report](../gtdb-final-four-20261115/README.md).

The [CI repair report](../phase2-ci-triage-20261116/ci-repair-outcome-001.md)
records exact-source freshness admission, authenticated phage predecessor
censuses, the actual Algal415 near-tie proof, and the dated 2026-10-23
reclassification census with current semantic guards. Source commits are
`b2c2a30ffe46d7e2bf5933dd47a77a0646b26f34`,
`e95e4ac90b73cd4301d29b4f6a2af71a20af1899`,
`affa853c758b79b3738b6446c2ec2c7ef08c0f28`, and
`511bad18e65903f371c2f0ac3189e601285c779e`.
The only cherry-pick conflict was the generated model timestamp; the incoming
generation timestamp was retained. The schema page was then regenerated and
committed as `ff4621c5`. No canonical record conflict was resolved by hand.

## Actual reference comparisons

On clean integration revision `d7350491aa238da3d158df30f535e84b5d4a9f8d`,
the normal native reference path processed all six Phase 2 records: 270
snippet occurrences, 270 actual comparisons, 270 matches, zero native issues
and zero title-only validations. Record counts were 025:72, 087:37, 088:63,
122:44, 515:14 and 516:40. The one-record Switchgrass canary first persisted
and verified 37 actual comparisons through the same launcher, environment,
normal catalog and output root. The batch followed its successful free plan.

The measurement receipt at
`.temp/supplement-adoption-1996-20261115/integration-six-coverage-001/receipt.json`
has SHA256 `ec181cb0f3717671c714273d18709910e5c60eb298c977241a25fd94434c450e`.
The measurement JSON SHA256 is
`849b227a67d4ae99c5d5728bdc55d526247c4141927bf07b7d412ccbf1489cd8`;
its log SHA256 is
`501f467772aae943b059fb80061c9e1044b3669e64123f431484eafd67228b24`.
All 1,502 captured input hashes were independently checked at that revision.
The later dated schema-prose change does not relabel this historical result
as an execution at `ff4621c5`. The 549 declared paths are the inventory, not
the number of records validated by this selected run.

The [separate M5 six-record measurement](../phase2-reference-measurements-20261115/m5-six-normal-f4807c45-001.md)
already established the same 270 actual matches at `f4807c45`, with exact
canonical inputs and its own receipts. Neither measurement replaces the full
reference sweep or claims that scientific blockers are resolved.

## Combined checks

These are actual native recorder runs under `.temp/phase2-schema-20261115/`.
The distinct revisions are intentional; focused results are not a full-QC pass.

| Run | Recorded revision | Result | Raw log SHA256 |
| --- | --- | --- | --- |
| `integration-supplement-proof-canary-001` | `09a9abe3` | 1 passed | `1e36460d7ec6c7a4d4f9b8b4ba5d788cf93e65e861e35e9c1186f595a43a9e22` |
| `integration-supplement-controls-001` | `09a9abe3` | 202 passed, 14 warnings | `b6d868e5f05600c2aa4ce537766e2c46eaf4fbd5ca53aeca18859836cd23296f` |
| `integration-final-four-canary-001` | `d7350491` | 1 passed | `df6a28b7bdc898a8ee4eefdf253fa45db521368149d475fb7a33ee6a49e88391` |
| `integration-final-four-controls-001` | `d7350491` | 112 passed, 12 warnings | `88ddf4b9797eef4e45741086da7a4829ee5393130618386253a35f346da0337b` |
| `integration-supplement-measure-actual-001` | `d7350491` | 37 actual comparisons, 37 matches | `e62e938ddae79c423d9774dfba578d37fdbf25eb97b6e929c12c4e546716338e` |
| `integration-six-measure-actual-001` | `d7350491` | 270 actual comparisons, 270 matches | `e9ecaaa281a0bcb3752075f5f17fc48c37c49bbfd7a7384df175f5a637fc9ee0` |
| `integration-render-current-001` | `d7350491` | 512 community pages and bulk products generated; no tracked delta | `2efe3a84aa164772da68c01e5a32098d62060afd2230f486719b49420f9781b1` |
| `integration-ci-lint-001` | `9efc4a2c` | Black 817 files, Ruff, mypy 52 sources passed | `31a144671f65a4a5618470b1bd3a39cae2612cc44107cbe68a32dccb26b45832` |
| `integration-ci-proof-canary-001` | `9efc4a2c`, generated schema-page delta present | 1 actual freshness proof passed | `b365d324350f32de27cd1e1e98f041e6066e72dafcbfa43822e0dd9017795d80` |
| `integration-ci-proof-controls-001` | `ff4621c5` | 33 passed, 12 warnings; actual source-proof and refusal/restoration controls | `af7f7910fce37ce4d6100f24580309838be60d089a857f13b39796284631ed5e` |
| `integration-ci-docs-current-001` | `9efc4a2c` | Failed: generated schema page needed the dated census prose | `964ef8122b0f5ff4c8611db2a70cf79432294f6506917b2a23fe6766a43adad1` |
| `integration-ci-docs-current-002` | `ff4621c5` | Passed after committing the exact generated schema page; all docs current | `8d01cb9a8aa8859780826efc0dda97e7d4451d2c53b1febe4a5fc60778d87b89` |

Independent read-only review checked the quoted receipts and linked outcomes.
Its one finding, a malformed Transwell commit reference in this draft, was
filed as [issue2952](https://github.com/CultureBotAI/CommunityMech/issues/2952)
and corrected before publication. No executed receipt was changed.

## Approved transfers and merge

The eight approved genus inputs and the three Thermophilic416 and two
Sahara494 files are now present on M5 with every destination hash verified.
Each transfer verified its first file before the remaining files and preserved
existing destinations. The exact five Thermophilic/Sahara files and original
denials are recorded in the
[approved-transfer report](../gtdb-shrimp-thermophilic-sahara-20261115/approved-input-transfers-20261116.md).
The separate 40-file ambiguity transfer is still awaiting explicit permission
after automatic approval review rejected it. No additional transfer is inferred
from these approvals.

The explicitly approved [Claw PR1283](https://github.com/CultureBotAI/culturebotai-claw/pull/1283)
merged through its normal queue at 2026-11-16 02:02:02 UTC, commit
`0710413e8bbb057e943aa0629b1f15d377b19bda`, reviewed head
`8d09d230bb5953c8dc8ed9c68059a260d549c013`. The four merge-queue workflows
passed. The six reviewed feature files were unchanged in the queued commit.
The merged commit was verified as an ancestor of fetched `origin/main`.
GitHub had already removed the remote feature branch; the matching local
branch and stale tracking ref were then removed. The checkout remains detached
at the reviewed head, with all private evidence preserved. To recover the local
branch, use `git branch fix/supplement-source-locator-1996-20261115 8d09d230bb5953c8dc8ed9c68059a260d549c013`
in that preserved Claw checkout. No live Claw deployment was updated.

The Claw recorder retained `pr1283-merged-readback-001.log`, SHA256
`297d14aa663b8210369fa00e87e510f1bfcb7e957bad03a1c267d242fd958b5c`,
and separate ancestry, preserved-checkout and ref-cleanup receipts under
`.temp/supplement-schema-20261115/`. Other PRs require their own approval.

## Remaining work

The immutable assignment inventory at `d7350491`, SHA256
`fca8b171750d101cecd416da88fc58ac0b77f976adaf8bda93ec9a077da00809`,
records 116 changed and 10 unchanged files among 126 historical assignments.
It is a byte inventory, not completion evidence. The unchanged IDs were 363,
376, 381, 389, 416, 419, 441, 482, 494 and 501. Pending worktrees are excluded.
The genus and Thermophilic/Sahara lanes are now active with their authorized
inputs; their unfinished applications do not count as integrated here.

Akkermansia lineage and population adjudication under issues2948/2833 remains
separate, as do the ambiguity transfer and remaining strict admissions. The
last full-QC failure and later stages marked not run remain the aggregate
status until a complete required run succeeds on a recorded current revision.
The earlier full reference sweep's 109 issues across 17 records remain owned;
this six-record result does not erase them. Native terms, schema validators,
saved partial diagnostics and matched quotations cannot complete scientific
review. After Phase 2 completion, resume the all-record campaign with one full
native review and verified durable checkpoint before independent batches.
