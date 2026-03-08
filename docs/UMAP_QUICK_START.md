# UMAP Visualization Quick Start

## 🚀 Generate the Visualization

```bash
# Simple one-liner
just gen-umap
```

That's it! The visualization will be generated at `docs/community_umap.html` in ~10-15 seconds (after initial cache).

## 📊 View the Visualization

**Important:** The visualization requires `docs/d3.v7.min.js` (included in repo).

### Local Browser
```bash
open docs/community_umap.html
```

### GitHub Pages
1. Push to GitHub
2. Enable GitHub Pages for the `docs/` directory
3. Navigate to: `https://[your-username].github.io/[repo-name]/community_umap.html`

### From Index Page
Click the blue "View Community Embedding Space →" button at the top of the index page.

## 🎯 What You'll See

**73 interactive points** representing microbial communities projected into 2D space based on their taxonomic similarity.

**Interactive features:**
- **Hover** over points to see metadata
- **Click** points to navigate to community detail pages
- **Search** for communities by name
- **Color** by category, ecological state, or origin (dropdown)
- **Size** by number of taxa or interactions (dropdown)
- **Zoom/pan** to explore clusters

## 🔧 Common Use Cases

### Regenerate After Adding Communities
```bash
just gen-umap
```

### Adjust UMAP Parameters
```bash
# More local structure (tighter clusters)
uv run communitymech generate-umap --n-neighbors 30

# More global structure (spread out)
uv run communitymech generate-umap --n-neighbors 5

# Tighter point spacing
uv run communitymech generate-umap --min-dist 0.01
```

### Include Low-Coverage Communities
```bash
# Lower coverage threshold from 50% to 30%
uv run communitymech generate-umap --min-coverage 0.3
```

### Force Reload Embeddings
```bash
# If embeddings file was updated
uv run communitymech generate-umap --force-reload
```

## 📈 Interpreting the Visualization

**Communities close together** have similar taxonomic composition:
- Shared taxa
- Phylogenetically related taxa
- Similar functional roles

**Expected clusters:**
- **AMD communities**: Leptospirillum + Ferroplasma dominated
- **DIET communities**: Geobacter + methanogen pairs
- **SynComs**: Designed synthetic communities
- **Biomining**: Metal-resistant acidophiles

**Outliers** may indicate:
- Unique taxonomic composition
- Highly specialized niches
- Under-sampled community types

## 🎨 Visualization Controls

**Color Dropdown:**
- `category` - Community type (AMD, DIET, SynCom, etc.)
- `ecological_state` - Stability (STABLE, TRANSIENT, etc.)
- `origin` - Natural vs Synthetic

**Size Dropdown:**
- `num_taxa` - Number of unique taxa (default)
- `num_interactions` - Number of ecological interactions

**Search Box:**
- Type any community name or ID
- Matching points highlighted in yellow
- Non-matching points fade out

## ⚡ Performance Tips

**First run is slow** (~90-120s):
- Parsing 3.2GB embeddings file
- Filtering to 882K NCBITaxon nodes
- Caching to `.umap_cache/NCBITaxon_embeddings.pkl`

**Subsequent runs are fast** (~10-15s):
- Loads from pickle cache
- Only reruns UMAP and HTML generation

**Clean cache if needed:**
```bash
rm -rf .umap_cache/
```

## 📁 Output Files

```
docs/
  community_umap.html          # 46 KB interactive visualization

.umap_cache/                   # Untracked (in .gitignore)
  NCBITaxon_embeddings.pkl     # ~1.8 GB cached embeddings
```

## 🐛 Troubleshooting

**"Coverage too low" warnings:**
- Normal: 9 communities skipped due to missing embeddings
- Reason: Taxa not in KG-Microbe or different taxonomy source
- Fix: Lower `--min-coverage` threshold or wait for KG-Microbe updates

**"Module not found" errors:**
- Run: `uv sync` to install dependencies

**Slow first-time generation:**
- Expected: 90-120s to parse 3.2GB embeddings file
- Subsequent runs will be fast (cached)

**Empty visualization:**
- Check that `data/embeddings/DeepWalk*.tsv.gz` exists
- Verify communities exist in `kb/communities/`

## 📚 More Information

- Full documentation: `docs/UMAP_VISUALIZATION.md`
- Implementation details: `UMAP_IMPLEMENTATION_SUMMARY.md`
- Tests: `tests/test_embedding/test_aggregator.py`

## ✨ Example Workflow

```bash
# 1. Add new community YAML
vim kb/communities/My_New_Community.yaml

# 2. Validate it
just validate kb/communities/My_New_Community.yaml

# 3. Regenerate all HTML
just gen-all

# 4. View UMAP
open docs/community_umap.html

# 5. Push to GitHub
git add kb/communities/My_New_Community.yaml docs/
git commit -m "Add My New Community"
git push
```

---

**Need help?** See `docs/UMAP_VISUALIZATION.md` for detailed documentation.
