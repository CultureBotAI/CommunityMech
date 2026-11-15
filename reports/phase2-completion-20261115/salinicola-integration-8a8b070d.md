# Salinicola integration checkpoint

The bounded M5 correction for [Salinicola A11, 000553](../../reviews/structured/20261115T062629Z-gtdb-genus-000553-canary/review.md)
is integrated at `8a8b070d3ea9257d47af9fbcd9d6c71ce99ea273`. Its
[immutable proof](../gtdb-code006-20261115/batch147-genus-successors-002.json)
records the actual application at M5 revision
`90a00bc2781266cb315a8295ca40e8f1c01e46fc`, seven scoped checks and the two
unchanged outstanding-grounding tests. The genus correspondence is 46/46 named
reference genomes; it does not identify the study stock's species or genome.
All other biological content and historical scientific findings remain unchanged.

An independent read and native saved-pair audit verified all 84 inputs
(4,817,305 bytes), review validation, exact Markdown derivation and unchanged
input bytes. The saved YAML SHA-256 is
`f9f5b4b46f481405ef62b45dca6a0c70b905ef6fe19f231dff19cbd73f06d02e`;
the Markdown SHA-256 is
`81af44607d235bfc3dab57bdfaf764be486f8a3a68cc8d454ce0994e09e3f6a5`.
Separate complete snapshots retain the pair and all inputs on both machines.

On the clean integrated tree, ten historical-review, genus/species successor,
snapshot and writer modules passed **106 tests**, with 12 dependency deprecation
warnings in 35.57 seconds, exit 0. Native lint also passed: Black left 713 files
unchanged, Ruff passed, and mypy accepted 52 source files. The raw evidence is
retained as immutable JSON/log/exit triplets under
`.temp/phase2-schema-20261115/`:

| Run prefix | Log bytes | Log SHA-256 |
|---|---:|---|
| `integrated-salinicola-8a8b070d-002` | 903 | `bd282df5a1d61731f7f0e6eacc23282a2b885ae444bc408b7b0d883fff497cd4` |
| `integrated-salinicola-lint-8a8b070d-001` | 219 | `56a3b87700c834a40da34cac500e6c010dd7b75204efc69db3250ab93b57de5f` |
| `isolate-render-000553-8a8b070d-001` | 219 | `9c504cf244b5caefa70f6e96329782ff865e77549965ecdb36743ffb3552d897` |

The earlier test attempt `integrated-salinicola-8a8b070d-001` supplied a
mistyped test path, exited 4 and ran zero tests. It remains retained and is not
counted as validation.

The native renderer persisted a 60,159-byte HTML probe with the correct record
identifier under `.temp/phase2-schema-20261115/isolate-render-8a8b070d-001/`.
Its SHA-256 is `d28f8dd66db3b19ef7a907ad1691a39918075c73922f0996fc8cdf76e91a65fe`.
This isolate is outside the maintained community-page population; tracked
`docs/` is unchanged. These checks do not replace full corpus QC or scientific
review. The diagnostic explicitly records `scientific_review: false`.
