# Full Switchgrass review: M5 input checkpoint

The saved full review now has a complete verified input checkpoint on M5 as
well as locally. The M5 audit verifies all 86 captured inputs, native review
validation and exact rendered Markdown. The standalone checkpoint verifier
verifies 88 files / 5,395,155 bytes under the exact manifest below. This is
persistence evidence for the existing review, not a new scientific assessment.

The reviewed public commit `626961a3a7c8101f0cf3c179df2ff0874f160869` was fetched
and fast-forwarded on the named M5 branch
`fix/supplement-adoption-m5-1996-20261115`. The canonical record, normal
reference configuration, adjacent backup and lock file remained unchanged:

| Input | SHA256 |
| --- | --- |
| Current Switchgrass record | `bcc2759c9da7c4059330726a1b154df600ec394d1106be2dcc1f4d247eed5eb9` |
| `conf/reference_validator.yaml` | `8d6620c22f3f0cfd02bdc129a3bdc3d9319ea9d63266756580868798cce6120a` |
| `conf/reference_validator.yaml.bak-before-normal-source-20261115` | `297b1fbd8a77ba2f89ca7126339deabc0f61ee91013d054d0fa64caef59a630d` |
| `uv.lock` | `1e1374a77207de170502a89ea7eebcb018d65daac8b0faecc39988d955f3df62` |

The backup remains intentionally untracked. The original inspection, full
assessment and native save retain their historical `f4807c45` revision; the
checkpoint operation does not relabel them as M5 execution or rerun them.

Six missing public inputs and the saved pair arrived through Git. Four private
source files were copied locally on M5, without overwriting, from the already
approved `final-five-001/snapshot` checkpoint in `phase2-completion-20261115`.
Its manifest is `da38c9123ade6a83f1cfbd0be22870e4bc0dc0428b0386aabe0f1c9bb6cbf0fe`.
All four source hashes matched before copying. A grounding-JSON canary was
copied and rehashed before the three figure files followed the same path;
every destination matched. The original checkpoint was not changed.

Three older application receipts were reconstructed at their captured paths
from exact public copies already on M5. Two local coverage-result files were
reconstructed from byte-identical M5 measurement outputs. These copies retain
the original receipt identities and historical execution context; they do not
create new application or measurement claims.

Only five new metadata files were uploaded: the failed corpus network
receipt/log/exit and the local coverage started/final receipts, totaling
610,316 bytes. The reviewed selector generated exact manifest
`78817238ca3039d34e6710fdd31daaf42b8ef9b3543944cfba0515e447e0db77`.
The 845-byte receipt canary was verified before the remaining four files used
the same `rsync --ignore-existing` path; all five final hashes match. No new
article, figure or other private source body was uploaded. The initial
read-only pre-update command used a wrong config filename and failed before
any mutation; its receipt is retained alongside the corrected successful check.

The unchanged native saved-pair audit passed for:

- [YAML](../../reviews/structured/20261116T011931Z-switchgrass-full-source-successor/review.yaml), SHA256 `83d4aa59145ddd04383bb61c29f19dc73c778a6d54967bedbb3db7b97ebfba0d`.
- [Markdown](../../reviews/structured/20261116T011931Z-switchgrass-full-source-successor/review.md), SHA256 `135982ead076883634dc9c5a76a706e2e9eceb0cb9bc413832ab249f28be0735`.
- All 86 input files / 5,218,236 bytes, with native validation, exact Markdown and unchanged captured bytes.

The exclusive M5 checkpoint is
`.temp/switchgrass-full-review-20261116/input-checkpoint-m5-001/` beneath the
adoption checkout. Its manifest SHA256 is
`f57036d4751d4c1cd18227a8381b4db9df18bc5ae1b621c568fafa50a92b34b2`.
The standalone verifier passed all 88 files / 5,395,155 bytes. The previously
verified local checkpoint remains unchanged at manifest
`5737295d3ab6dfaa74717b1802ce4abdb22fef381094e63035551cac3c3b006d`.
The two manifests retain their distinct creation times; each preserves the
same review and exact declared source bytes.

| Actual M5 recorder under `.temp/phase2-schema-20261115/` | Exit | Raw log SHA256 |
| --- | ---: | --- |
| `switchgrass-full-review-saved-audit-m5-001` | 0 | `b3a9051f7695ce6f46ca36db3f1fd8f82fdc4a840d1ccc0e24d592f6f8715db4` |
| `switchgrass-full-review-checkpoint-plan-m5-001` | 0 | `30062d2b3d363502dbb3ebeb83627d9339b3abceec2e865fd105cbdf389bb69d` |
| `switchgrass-full-review-checkpoint-create-m5-001` | 0 | `eaaa716b09414477c422c3224db523faa1ae57fb0a8ee7ffb49767992ffe90c6` |
| `switchgrass-full-review-checkpoint-verify-m5-001` | 0 | `0445e27a9935c2072f2b1a3b884f775f137cd3177a422d009a50840dd7a38cd3` |

The manifest and these four raw triplets were mirrored without overwriting
under `.temp/switchgrass-full-review-20261116/m5-checkpoint-metadata-001/`.
Final state recorder `switchgrass-full-review-m5-final-state-001` has raw hash
`c5d6aa615ff22748ec83056ee5f173ec39285f94a1ceedf83a8ee9b67c64189c`.

The full review still concludes `needs_curation`: the source-roster conflict
under issue 1548 remains open, and the required corpus network command remains
failed with exit 1. Its absence of a Switchgrass finding is not a corpus pass.
The accepted current 37-assertion lexical measurement and exact supplement
selection do not settle the biological conflict. Aggregate QC, corpus
references, generated products and merge approval remain separate.
