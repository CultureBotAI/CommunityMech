# Community Embedding Space UMAP Visualization

## Overview

An interactive 2D UMAP visualization of all microbial communities in CommunityMech based on their taxonomic composition embeddings from KG-Microbe.

## Requirements

- **D3.js v7**: Included locally as `docs/d3.v7.min.js` (273KB)
  - **Why local?** The `file://` protocol blocks CDN requests for security
  - **For deployment**: Works with both `file://` and `https://` protocols

## Features

- **Interactive scatterplot**: Zoom, pan, hover, and click to explore 73 communities
- **Color encoding**: Communities colored by category (AMD, DIET, SynCom, etc.), ecological state, or origin
- **Size encoding**: Point size represents number of taxa or interactions
- **Search**: Fuzzy search to highlight and filter communities
- **Direct navigation**: Click any point to navigate to the community's detail page

## How It Works

### 1. Embedding Aggregation

Each community is represented by aggregating the KG-Microbe node embeddings (512-dimensional DeepWalk vectors) of its constituent taxa:

```
Community Vector = mean(taxon_embeddings)
```

- **Source**: KG-Microbe DeepWalk embeddings (1.45M nodes × 512 dims)
- **Filter**: NCBITaxon nodes only (882,939 taxa)
- **Aggregation**: Mean pooling across all taxa in each community
- **Coverage threshold**: Communities with <50% taxa coverage are skipped

### 2. Dimensionality Reduction

UMAP (Uniform Manifold Approximation and Projection) reduces the 512-dimensional community vectors to 2D for visualization:

```python
UMAP(
    n_neighbors=15,      # Balance local vs global structure
    min_dist=0.1,        # Minimum spacing between points
    metric='cosine',     # Similarity metric for embeddings
    random_state=42      # Reproducibility
)
```

### 3. Visualization

D3.js renders an interactive scatterplot where:
- **Proximity**: Communities close together have similar taxonomic composition
- **Color**: Categorical metadata (category, state, origin)
- **Size**: Quantitative metadata (number of taxa, interactions)

## Usage

### Generate Visualization

```bash
# Using justfile
just gen-umap

# Or directly with CLI
uv run communitymech generate-umap

# With custom parameters
uv run communitymech generate-umap \
    --n-neighbors 20 \
    --min-dist 0.05 \
    --min-coverage 0.7 \
    --force-reload
```

### CLI Options

| Option | Default | Description |
|--------|---------|-------------|
| `--communities-dir` | `kb/communities` | Directory with community YAML files |
| `--embeddings-path` | `data/embeddings/DeepWalk...tsv.gz` | Path to KG-Microbe embeddings |
| `--output` | `docs/community_umap.html` | Output HTML file |
| `--cache-dir` | `.umap_cache` | Cache directory for embeddings |
| `--force-reload` | `false` | Ignore cache, reload embeddings |
| `--n-neighbors` | `15` | UMAP n_neighbors parameter |
| `--min-dist` | `0.1` | UMAP min_dist parameter |
| `--min-coverage` | `0.5` | Min fraction of taxa with embeddings |

### View Visualization

1. Open `docs/community_umap.html` in a web browser
2. Or navigate to https://[your-github-pages-url]/community_umap.html
3. Or click "View Community Embedding Space" from the main index page

## Performance

- **First run**: ~90-120 seconds (load + parse 3.2GB embeddings file)
- **Cached runs**: ~10-15 seconds (load from pickle cache)
- **Cache location**: `.umap_cache/NCBITaxon_embeddings.pkl` (~1.8GB)

## Coverage Statistics

Out of 82 communities, 73 (89%) have sufficient embedding coverage:

**Skipped communities** (9 total):
- BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis
- BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia
- BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia
- BioModels_MODEL2204300001_Kefir_Community_Model
- BioModels_MODEL2310020001_Mouse_Metaorganism_Model
- BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom
- BioModels_MODEL2407300002_Sponge_Holobiont_Network
- KBase_Models_for_Zahmeeth_Original_PLOS
- KBase_ORT_Workflow_Community_Model

These communities likely contain taxa not yet in KG-Microbe or use different taxonomy sources.

## Architecture

```
Pipeline:
  kb/communities/*.yaml
    ↓ Extract NCBITaxon IDs
  KG-Microbe Embeddings (882K taxa)
    ↓ Lookup & mean pool
  Community Vectors (73 × 512 dims)
    ↓ UMAP
  2D Coordinates (73 × 2)
    ↓ Jinja2 + D3.js
  docs/community_umap.html

Modules:
  src/communitymech/
  ├── embedding/
  │   ├── loader.py         # Stream TSV.gz, cache to pickle
  │   ├── aggregator.py     # Mean pooling aggregation
  │   └── dimensionality.py # UMAP wrapper
  ├── visualization/
  │   └── umap_generator.py # Orchestration pipeline
  └── templates/
      └── community_umap.html # D3.js interactive plot
```

## Interpretation

### What Does Proximity Mean?

Communities close together in the UMAP space have **similar taxonomic composition** based on their KG-Microbe embeddings. This captures:

1. **Direct taxonomic overlap**: Shared species/genera
2. **Evolutionary relationships**: Phylogenetically related taxa have similar embeddings
3. **Functional similarity**: Taxa with similar metabolic roles cluster in embedding space

### Expected Clusters

- **AMD communities**: Dominated by Leptospirillum, Ferroplasma, Acidithiobacillus
- **DIET communities**: Geobacter + methanogen pairs
- **SynCom communities**: Designed synthetic communities with specific taxa
- **Biomining communities**: Metal-resistant acidophiles

### Outliers

Isolated points may represent:
- Unique taxonomic composition
- Highly specialized niches
- Under-sampled community types
- Novel community architectures

## Limitations

1. **Embedding quality**: Depends on KG-Microbe's node embedding quality
2. **Taxonomy resolution**: Limited to NCBITaxon-annotated taxa
3. **Missing embeddings**: Taxa not in KG-Microbe are excluded
4. **Aggregation simplicity**: Mean pooling ignores abundance and interactions
5. **UMAP stochasticity**: Minor variations across runs despite fixed random seed

## Future Enhancements

- **Multi-modal embeddings**: Incorporate metabolites, processes, environments
- **Abundance weighting**: Weight embeddings by relative abundance
- **3D visualization**: Three.js for exploring additional dimensions
- **Clustering**: HDBSCAN with auto-labels
- **Comparison mode**: Visual diff between community pairs
- **Embedding quality metrics**: Silhouette scores, trustworthiness

## References

- **KG-Microbe**: https://github.com/Knowledge-Graph-Hub/kg-microbe
- **UMAP**: McInnes et al. (2018) https://arxiv.org/abs/1802.03426
- **DeepWalk**: Perozzi et al. (2014) https://arxiv.org/abs/1403.6652
