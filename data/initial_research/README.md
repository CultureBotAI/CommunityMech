# Initial Research Data

This directory contains seed data and literature surveys for CommunityMech development.

## Files

### `microbial_community_systems v2.tsv`

Curated collection of **35 microbial communities** from published literature.

#### Dataset Overview

| Category | Communities | Description |
|----------|-------------|-------------|
| Plant Rhizosphere | 9 | Maize, sorghum, wheat, Arabidopsis, Lotus, soybean |
| Synthetic Phototroph-Heterotroph | 6 | Synechococcus, Chlamydomonas partnerships |
| Marine Systems | 3 | Diatoms, cyanobacteria, phytoplankton |
| Syntrophic Pairs | 10 | DIET, H2/formate transfer, methanogens |
| Lignocellulose Degradation | 5 | Cellulose, hemicellulose degraders |
| Aromatic/Hydrocarbon | 4 | Benzoate, phenol, oil degradation |

#### Fields

- **Community Name** - Identifier from literature
- **Ecological Origin** - Environment/habitat
- **Member Count** - Number of organisms (2-35)
- **Keystone Biosensor** - Central organism for monitoring
- **Key Support Members** - Supporting organisms
- **Biosensor Signal** - Monitoring target (iModulon, metabolite)
- **Relevance to DOE** - Mission alignment (bioenergy, carbon cycling, etc.)
- **Publication URL** - DOI link

#### Usage

This dataset serves as:

1. **Schema validation** - Ensures schema handles diverse community types
2. **Example source** - Basis for first community YAML files
3. **Literature starting point** - DOIs for evidence extraction
4. **DOE relevance** - All communities align with DOE mission areas

#### Recommended First Communities

For initial YAML file creation:

1. **Synechococcus-E.coli SPC**
   - Simple (2 members)
   - Well-defined interaction (sucrose cross-feeding)
   - Biosensor ready
   - Publication: https://doi.org/10.1038/s41467-020-17612-8

2. **Geobacter-Methanosarcina DIET**
   - Direct electron transfer (novel mechanism)
   - Well-studied syntrophy
   - Bioenergy relevance
   - Publication: https://doi.org/10.1128/AEM.00895-14

3. **SF356 Cellulose Degrader**
   - Lignocellulose focus (DOE priority)
   - Thermophilic (50°C, industrial relevant)
   - 5 members (moderate complexity)
   - Publication: https://doi.org/10.1128/AEM.71.11.7099-7106.2005

4. **Sorghum SRC1**
   - Field-tested bioenergy crop enhancement
   - Moderate complexity (16-20 members)
   - Multiple interaction types
   - Publication: https://doi.org/10.1093/ismejo/wrae126

## Adding New Research Data

When adding new datasets:

1. Add file to `data/initial_research/`
2. Update this README with description
3. Commit with descriptive message
4. Include source/citation information

## References

See individual publication URLs in the TSV file for primary literature.
