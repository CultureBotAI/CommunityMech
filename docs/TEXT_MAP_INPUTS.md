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

`conf/text_map.yaml` is explicitly disabled until a reviewed full-input bundle
exists at `data/text_map/current.json` and the canonical CLAW runtime is vendored
at `scripts/embedding_pipeline.py`. Enablement requires the pinned fleet BGE
model, revision, dimension and 512-token window, actual PaCMAP, valid checksums,
and fresh complete adapter inputs. Missing or stale enabled inputs fail loudly.

`just stage-text-map` validates and stages the three public files at
`docs/text-map/` without inference. It binds the exact immutable generation
approved by preflight, refusing pointer changes or manifest substitution before
publication. The Pages workflow performs the same validation before uploading
`docs/`; a standalone stage does not regenerate existing browser pages.

The shared text map complements the existing domain graph views. Record URLs
are relative to `docs/`, so the shared map's `../` link prefix resolves to the
existing browser/detail routes. No legacy graph vector or model artifact is
relabeled as BGE.

After enabling the map, run `just gen-html` to regenerate the landing/browser
links and per-record pages. Its renderer preflights the full bundle before
writing pages; normal checks use the same path.
