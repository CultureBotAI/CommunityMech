# UMAP Visualization Color Guide

## Category Colors (14 distinct, semantic colors)

Each community category has a semantically meaningful color:

| Category | Color | Hex Code | Communities |
|----------|-------|----------|-------------|
| AMD | 🔴 Red | `#e74c3c` | 6 |
| BIOMINING | 🟠 Orange | `#f39c12` | 10 |
| BIOREMEDIATION | 🟢 Green | `#27ae60` | 7 |
| BIOTECHNOLOGY | 🔵 Blue | `#3498db` | 4 |
| CARBON_SEQUESTRATION | 🔷 Teal | `#16a085` | 1 |
| DIET | 🟣 Purple | `#9b59b6` | 3 |
| EXTREME_ENVIRONMENT | 🔴 Dark Red | `#c0392b` | 2 |
| LIGNOCELLULOSE | 🟤 Brown-Orange | `#d35400` | 4 |
| METAL_REDUCTION | ⚫ Gray | `#95a5a6` | 1 |
| METHANOGENESIS | 🟣 Dark Purple | `#8e44ad` | 1 |
| OTHER | ⚫ Medium Gray | `#7f8c8d` | 5 |
| PHYTOPLANKTON | 🔷 Cyan | `#1abc9c` | 5 |
| RHIZOSPHERE | 🟢 Bright Green | `#2ecc71` | 16 |
| SYNTROPHY | 🟠 Orange-Red | `#e67e22` | 8 |

**Total: 73 communities, 14 unique colors**

## Ecological State Colors (3 colors)

| State | Color | Hex Code | Meaning |
|-------|-------|----------|---------|
| STABLE | 🟢 Green | `#27ae60` | Long-term stable community |
| PERTURBED | 🟠 Orange | `#f39c12` | Disturbed/transitional |
| ENGINEERED | 🔵 Blue | `#3498db` | Designed/controlled system |

## Origin Colors (3 colors)

| Origin | Color | Hex Code | Meaning |
|--------|-------|----------|---------|
| NATURAL | 🟢 Green | `#27ae60` | Found in nature |
| ENGINEERED | 🔵 Blue | `#3498db` | Human-designed |
| SYNTHETIC | 🟣 Purple | `#9b59b6` | Fully synthetic/lab-created |

## Design Principles

✅ **All 14 categories have unique colors** (no duplicates!)  
✅ **Semantic meaning**: Red = extreme, Green = natural/plant, Blue = engineered  
✅ **High contrast**: Colors are visually distinct  
✅ **Color-blind friendly**: Uses variety of hues and brightness  
✅ **Professional palette**: Based on Flat UI Colors

## Color Accessibility

- **Red tones**: AMD, EXTREME_ENVIRONMENT (different brightness)
- **Green tones**: BIOREMEDIATION, RHIZOSPHERE (different brightness)
- **Orange tones**: BIOMINING, LIGNOCELLULOSE, SYNTROPHY (different hues)
- **Purple tones**: DIET, METHANOGENESIS (different brightness)
- **Blue/Cyan tones**: BIOTECHNOLOGY, PHYTOPLANKTON, CARBON_SEQUESTRATION (different hues)

No two similar categories use similar colors!

## Usage in Visualization

**Default view**: Communities colored by **category** (14 colors)  
**Dropdown options**: Switch to **ecological_state** (3 colors) or **origin** (3 colors)

**Legend updates** automatically when you change the color dropdown.
