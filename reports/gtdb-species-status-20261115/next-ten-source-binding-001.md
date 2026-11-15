# Source binding for the ten-record species plan

The [authored source context](next-ten-authored-source-context-001.json), SHA256 `d3f8c7e6ace5dcbc9977b71b85e985b9be6c93ee171ff327b07c7ca47dc2a1d6`, was independently read together with the current records, primary caches, accepted Parmigiano/000397 source plans and historical guard scopes. It selects fourteen taxonomy occurrences in ten whole records. It preserves all other biology, existing GTDB blocks, source limitations and null outcomes.

The [expanded configuration](next-ten-source-config-001.json), SHA256 `07cda7b4fc2d9b7e88f742cbae442a453a17d910e12f297ff5f28517aae63391`, contains the complete retained native results. `scripts/adhoc/compose_gtdb_source_config_20261115.jq` verifies each authored identity and expected native population before copying that result; it binds both its own bytes and the authored configuration. Independent reproduction matched the configuration exactly.

Native route generation 002 uses the source binder's supported `.venv/bin/python` command prefix. The earlier valid generation 001 used `uv run --offline python`; its receipts remain unchanged. The generation 002 canary and ten-record JSON outputs were byte-identical to generation 001, and every captured input hash verified. The ten-record generation 002 raw receipt is `.temp/phase2-schema-20261115/species-route-ten-002.json`, SHA256 `13743e5b761423956606cb5e5f9f16de485a597a362b2e563664ff7308988276`; its native JSON remains SHA256 `12309d2473eb63a427dbf7d6bfbaf6c918f2cb7fbd24352936bbbd36dde825e4`.

The accepted shared binder then ran one real 000388 unit through the persisted launcher at revision `095b9e5df68d1311ab73e145a0824d8c66da3533`. Its nonempty 17,862-byte result retained three primary-source locators and both explicit member routes; all 35 captured input hashes verified. Only after this did the same launcher and environment bind all ten records: 106,499 bytes, with all 64 captured input hashes verified. These are read-only source/authority bindings, not canonical applications or full scientific reviews.

| Binding | Raw JSON path under `.temp/phase2-schema-20261115/` | SHA256 |
| --- | --- | --- |
| One-record canary | `species-context-388-canary-001.log` | `af52834f0ee5a979a2aac6393c75d13e506dde32002af79663c425f66b1509c7` |
| Ten-record binding | `species-context-ten-001.log` | `4a20d03c848c25b9f0f77821c34434364dfa3c2d197d85aee3d9f3cd3c62c47d` |

The one-record staging canary retained the exact source proof and produced candidate SHA256 `6dd5d30d6c218beb0bd622fabdfffe87cb1a790dbdce07b185228bed61442f55` and receipt SHA256 `d7eb5799ad1c279a2c650637284505cac2c812d1394f8d928628f8327ce2118f`. Its diff changes only the two declared GTDB blocks/statuses and appends two native events. Independent candidate review accepted those bytes. Actual M5 application, native history, eight gates, saved diagnostic review, complete input checkpoint and strict historical successor admission remain required before counting this canary as completed or applying the remaining nine.

Primary-text, abstract-only and selected-preprint coverage remain explicit per record. Reference genome populations do not establish study-stock genome membership. The local NCBI SQLite query verifies labels/ranks and retains identity rows; its stable file-stat observation is not a content hash or release certification. No source or cache acquisition occurred in this preparation.
