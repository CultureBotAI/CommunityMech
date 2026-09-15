# CommunityMech community graph provenance

Graph maps retain their KG-Microbe DeepWalk features and domain matching policies. The fleet's common BGE text map is a separate view. This work follows #900 and #905.

Use `UMAPVisualizationGenerator().generate(embeddings_path="/path/to/source.tsv.gz", method="pacmap")` from `communitymech.visualization.umap_generator`. It defaults to `kb/communities` and `docs/community_umap.html`. For the retained graph layout pass `method="sfdp", output_path="docs/community_graph.html"`. Each HTML gains sibling `.points.json` and `.metadata.json` artifacts. `method="umap"` is an explicit alternative.

The population is communities. Isolate files are explicitly recorded as outside this graph view. The coverage denominator is all unique requested taxon IDs; missing graph vectors do not identify hosts. The ledger includes found/missing taxa, coverage, aggregation weights and communities omitted below the threshold. Host exclusion still requires independent evidence and is not inferred here.

New generation reads the selected TSV or TSV.gz stream directly and hashes the exact bytes while parsing. Old basename/size/mtime pickle caches are ignored, including when `force_reload` is false. The scan is streaming and retains only required node vectors; the full source file is still read once per generation. Do not infer source identity by hashing a different file beside old coordinates.

Schema-v2 receipts bind the full corpus, matching/omission ledger, ordered reducer matrix, actual algorithm/normalization/settings and installed backend versions to checksums of every output. PaCMAP records fitted pair counts. The sfdp backend, where available, records the symmetric union-kNN construction, DOT checksum, Graphviz version and command arguments. Failed generation leaves previous outputs unchanged; publication rolls back ordinary write failures. A process kill can leave a `.graph-recovery-*` directory for recovery and is not claimed to be an atomic website deployment.

Validate a completed generation with:

```python
from pathlib import Path
from communitymech.graph_embedding_receipts import load_receipt

receipt = load_receipt(Path("path/to/projection.metadata.json"))
```

This verifies all sibling artifacts declared by the receipt. It is not a tool for attaching newly guessed provenance to legacy arrays. Full published artifacts must be regenerated from reviewed current inputs before the graph correction is considered complete.

## Deployment gate

`python scripts/check_graph_receipts.py` verifies the complete intended HTML/points/receipt sets against the current corpus before Pages publication. It rejects missing or altered artifacts, wrong output membership or reducer, invalid point identities/coordinates, and changed source YAML. This check uses only the Python standard library and reads no source graph vectors or model. The retained historical media views, where present, do not borrow these verified graph receipts.
