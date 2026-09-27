# Common semantic text map inputs

Includes canonical community records and separately stored isolate records in
the text map; the graph community projection keeps its own population policy.
Stable CommunityMech IDs link to existing community pages. Text includes names,
descriptions, ecological class/state, environments, named taxa/roles,
interactions and measured environmental factors. Citations, evidence snippets,
history, grounding annotations and identifiers are excluded.

Export with `just text-map-inputs --output data/text_map/inputs.jsonl`. Without `--output`, the command validates a preview. `--record` (repeatable repository-relative YAML path) and `--limit` explicitly select canary subsets; ordinary exports cover every eligible record.

Each JSONL row has exactly `identifier`, `label`, `category`, `page`, `source_path`, `text`, `text_sha256`, and `adapter_version`. The text digest is SHA-256 over the exact UTF-8 text. Input order and text are deterministic; duplicate IDs and unreadable records fail. This adapter makes no model call. Common model/projection generation and publication require the fleet pipeline and full-input checks.

Changing provenance-only fields leaves semantic text unchanged. Editing a selected semantic field changes its digest. This text view supplements the existing graph view; it does not alter graph aggregation or its scientific interpretation.

The `page` field is relative to the directory containing the published map
folder: from `text-map/index.html`, the shared renderer uses `../` plus `page`.
This repository publishes the contents of `docs/`, so the bundle is staged at
`docs/text-map/` and links resolve to records in the same published site root.

Isolate detail pages are published in `docs/isolates/` by `just gen-html`;
the community browser and graph population remain communities only.


## Publish the common semantic view

`conf/text_map.yaml` is enabled and the shared runtime is installed. The selected
common bundle is recorded by `data/text_map/current.json`; its `manifest.json`
reports the complete input identity and coverage counts. The enabled build
verifies freshness against the current corpus and refuses a stale bundle until
the cache-backed refresh is complete.

The installed CLAW runtime is `scripts/embedding_pipeline.py`; its separate
locked environment and exact build commands are in the [maintained runtime guide](../conf/embedding-runtime/README.md).
Normal rendering and verification do not install that model environment or run
inference. When record membership or selected semantic fields change, export
fresh full inputs, reuse the existing profile-bound vector cache to encode only
new or changed text, regenerate PaCMAP, and validate the complete bundle before
rendering. A stale bundle must be refreshed before publishing curated changes.

`just stage-text-map` validates and stages the three public files at
`docs/text-map/` without inference. It requires the pinned fleet BGE model,
revision, 1,024 dimensions and 512-token window, actual PaCMAP, valid checksums and
fresh full adapter inputs. It binds the exact generation approved by preflight,
refusing pointer changes or manifest substitution before publication.

After refreshing the validated bundle, run `just gen-html` to regenerate the
landing/browser navigation and per-record pages. The renderer preflights the
full bundle before writing pages. The Pages workflow validates the same inputs
before uploading `docs/`; a standalone stage does not regenerate browser pages.

The text map includes communities and isolates. Specialty graph views retain
their separate community-only population and source/corpus/reducer receipts;
curation that changes their corpus also requires their own verified refresh.
Record URLs are relative to `docs/`, so the shared map's `../` prefix resolves
to the existing browser/detail routes.
