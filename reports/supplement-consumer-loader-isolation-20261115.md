# Consumer schema generation isolation

This test-only change ports the independently reviewed Claw fix
`8d09d230bb5953c8dc8ed9c68059a260d549c013` to the consumer's actual
`EvidenceItem` and `SupportingReference` schemas. It preserves all original
locator and generated-model assertions. The fixture generates a closed schema
in a subprocess using the current Python interpreter, schema path and explicit
top class; no schema, runtime, pin or canonical data is changed by this work.

The original consumer fixture passed before mutation. A deliberately damaged
parent YAML loader then caused the actual in-process fixture to fail with
`ConstructorError: tag None`; the same one-class control passed after isolation.
Each new regression proves the poison is active through a direct generator
failure, validates old and selected citations through the isolated fixture,
rejects missing-cell and zero-row selections, verifies the parent remains
poisoned until restoration, and validates again after restoration. Both classes
passed in the final focused run. This is preventive consistency with the
observed Claw CI failure, not a claim of an observed consumer CI failure.

The boundary was recorded before the fix in
[issue 1996](https://github.com/CultureBotAI/CommunityMech/issues/1996#issuecomment-6903649679),
linked to Claw issue 263. Original fixture bytes remain at
`.temp/supplement-consumer-loader-20261115/original-001/test_supplement_source_locator_schema.py`
with SHA256 `754c7c2a9461d4bfe2eb2618b11858b8b35acc56c1bdbb95eb0f53750d59084b`;
the old fixture plus new regression is retained beside it.

All commands used the existing immutable recorder at revision
`b5cb827fa8dfac6e00f824f7d91de3ba74b123b8` with recorded working changes.
The adopted lockfile SHA256 was
`1e1374a77207de170502a89ea7eebcb018d65daac8b0faecc39988d955f3df62`.
Root's concurrent document generation and separate curation helper remained
outside this change. Raw triplets are under `.temp/phase2-schema-20261115/`.

| Recorder prefix | Actual result | Raw log SHA256 |
| --- | --- | --- |
| `supplement-consumer-loader-baseline-001` | Original EvidenceItem positive: 1 passed, 12 warnings, 5.46 s | `d735173508667840908912010d4033503541ca95cd25e66a9563567335a23b98` |
| `supplement-consumer-loader-poison-before-001` | Deliberate poison: 1 failed at the old fixture, 12 warnings, 4.01 s | `5a999c3c840834e0249160a668b4bac99d33dd50e0eb18575a7db9e0626f709f` |
| `supplement-consumer-loader-poison-after-001` | Same EvidenceItem poison/restoration control: 1 passed, 12 warnings, 7.44 s | `9a99104e3b561ea8baa18a50c5738fc454f44429284e8f64dc420f59f359051a` |
| `supplement-consumer-loader-schema-model-001` | Both schema roots, models and existing validator behavior: 44 passed, 12 warnings, 41.25 s | `b03e096e98a003480d282679b1148f7561b23402163873f159f3b1f1c02a804f` |
| `supplement-consumer-loader-format-001` | Targeted Black check passed | `1a56c7cd8457fd05d978cfbd139d7bfd86e86acaa9b57668e718ef8bccc0cf48` |
| `supplement-consumer-loader-ruff-001` | Targeted Ruff passed | `82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18` |

The broader five-module run is retained separately as
`supplement-consumer-loader-focused-001`: **14 failed, 53 passed, 14 warnings**,
36.03 s, raw SHA256
`c7af03030d899b9a21eab58ddd177f65cd7b1c7dbe6522df2f7d3073fbe8c806`.
It exposed the old reference-coverage tracer's rejection of the adopted
runtime's `source_locator` argument and exact development version, filed as
[issue 2937](https://github.com/CultureBotAI/CommunityMech/issues/2937).
Root owns that separate tracer/probe/test repair. These failures are not waived
by the 44-test schema/model pass; full combined checks and hosted CI remain
separate. The prior 37/37 runtime supplement trial is a distinct execution path.

Final test SHA256:
`3a15f2f725207e3b5e370d5f80511784fbf3bdf36f01132012ac66f6287b06af`.
