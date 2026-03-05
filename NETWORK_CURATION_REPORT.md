# Network Data Integrity Curation Report

## Overview

Systematic audit and curation of network data integrity across all 76 communities in CommunityMech.

## Summary

- **Communities audited**: 76
- **Communities with issues**: 51 (67%)
- **Total issues identified**: 235
- **Automatically fixed**: 50+ NCBITaxon ID mismatches across 33 communities
- **Remaining for manual curation**: ~185 issues across 41 communities

## Issues Identified

### 1. NCBITaxon ID Mismatches (✅ FIXED)

**Status**: Automatically corrected across 33 communities

NCBITaxon IDs in `ecological_interactions` didn't match the IDs in the `taxonomy` section for the same organism.

**Examples**:
- *Ferroplasma acidiphilum*: NCBITaxon:97398 → NCBITaxon:74969
- *Leptospirillum ferriphilum*: NCBITaxon:178899 → NCBITaxon:178606
- *Acidiphilium cryptum*: NCBITaxon:226539 → NCBITaxon:524
- *Geobacter sulfurreducens*: NCBITaxon:243231 → NCBITaxon:35554

**Impact**: These mismatches didn't affect network visualization (which matches by `preferred_term`) but created data integrity issues.

**Fix**: Automated script replaced all incorrect IDs with correct ones from taxonomy section.

### 2. Disconnected Taxa (⚠️ MANUAL CURATION NEEDED)

**Status**: 41 communities with ~130 disconnected taxa

Taxa in the `taxonomy` section with no connections in `ecological_interactions`.

**Examples**:
- **AMD_Acidophile_Heterotroph_Network** (✅ FIXED): All 6 taxa now connected
  - Added "Photoheterotrophic Carbon Cycling" for *Acidisphaera rubrifaciens*
  - Added "Complex Polysaccharide Degradation" for *Acidobacterium capsulatum*

- **At_RSPHERE_SynCom**: 3 disconnected
  - *Arabidopsis thaliana* (host plant)
  - *Flavobacterium sp.*
  - *Streptomyces sp.*

- **Australian_Lead_Zinc_Polymetallic**: 2 disconnected
  - *Acidiphilium cryptum*
  - *Sulfobacillus thermosulfidooxidans*

- **ORNL_PMI_Populus_PD10_SynCom**: 8 disconnected
  - 8 of 10 member strains have no interactions defined

**Tool Created**: `scripts/suggest_missing_interactions.py`
- Analyzes functional roles to suggest plausible interactions
- Generates templates based on role compatibility
- Provides confidence scores for suggestions

### 3. Missing source_taxon (⚠️ MANUAL CURATION NEEDED)

**Status**: ~25 interactions missing source organisms

Interactions that describe community-level processes but don't specify which organism performs the function.

**Examples**:
- **Bayan_Obo_REE_Tailings_Consortium**:
  - "REE Dissolution from Bastnaesite and Monazite" - no source

- **Chromium_Sulfur_Reduction_Enrichment**:
  - "Chromium Immobilization via Cr(III) Precipitation" - no source

- **Copper_Biomining_Heap_Leach**:
  - "Copper Sulfide Dissolution" - no source

**Next Step**: For each interaction, determine the primary organism(s) responsible based on:
1. Functional roles in taxonomy
2. Evidence snippets
3. Literature descriptions

### 4. Unknown Taxa References (⚠️ MANUAL CURATION NEEDED)

**Status**: ~30 interactions reference community-level abstractions

Interactions that reference collective taxa rather than specific organisms.

**Examples**:
- **Dangl_SynComm_35**:
  - Source: "SynComm 35 bacterial community"
  - Source: "Bacterial suppressors (10 robust strains)"
  - Source: "Suppressor bacteria"

- **Sorghum_SRC1_Subset**:
  - Source: "SRC1 bacterial community"

**Resolution Options**:
1. Replace with individual organism interactions (preferred)
2. Create separate community-level interaction class (requires schema change)
3. Select representative organism

## Files Created

1. **scripts/audit_network_integrity.py**
   - Audits all communities for network data issues
   - Generates detailed report

2. **scripts/fix_network_integrity.py**
   - Automatically fixes NCBITaxon ID mismatches
   - Reports issues requiring manual review
   - Usage: `python scripts/fix_network_integrity.py --apply`

3. **scripts/suggest_missing_interactions.py**
   - Suggests interactions for disconnected taxa based on functional roles
   - Provides confidence scores and rationales
   - Usage: `python scripts/suggest_missing_interactions.py`

4. **network_integrity_audit.txt**
   - Detailed audit report of all issues found

## Commits

1. **7d21476**: Fixed AMD_Acidophile_Heterotroph_Network as proof-of-concept
   - Fixed NCBITaxon IDs
   - Added 2 new interactions for disconnected taxa
   - All 6 taxa now properly connected

2. **5c55ba6**: Automated fixes across 33 communities
   - Fixed 50+ NCBITaxon ID mismatches
   - All modified files validated successfully

## Next Steps for Manual Curation

### High Priority

1. **Plant-Microbe Communities** (highest impact)
   - Host plants often disconnected (Arabidopsis, Triticum, Zea, Glycine, etc.)
   - Add plant-microbe mutualism/symbiosis interactions
   - Examples: At_RSPHERE_SynCom, Wheat_Consortium_C1/C6, Soybean_N_Fixation_sfSynCom

2. **Large SynComs with Many Disconnected Members**
   - ORNL_PMI_Populus_PD10_SynCom: 8/10 members disconnected
   - Maize_Root_Simplified_Community: 7 members disconnected
   - Okeke_Lu_Cellulolytic_Consortium: 5 members disconnected

3. **Interactions Missing Sources**
   - Biomining/bioleaching processes (Copper, PGM, Gallium recovery)
   - Biogeochemical transformations (Cr reduction, V reduction, U reduction)
   - REE dissolution processes

### Medium Priority

4. **Aerobic Heterotrophs in AMD Communities**
   - Often present but not explicitly connected
   - Add organic matter scavenging interactions

5. **Secondary Degraders in Consortia**
   - Connect to primary degraders via cross-feeding

### Lower Priority

6. **Rare/Minor Community Members**
   - May legitimately have weak or no interactions in simplified models
   - Evaluate whether they should be in taxonomy at all

## Validation

All automatic fixes validated:
- ✅ Schema validation passed (linkml-validate)
- ✅ HTML regenerated successfully
- ✅ No breaking changes to network rendering
- ✅ Committed and pushed to GitHub Pages

## Recommendations

1. **Adopt interaction templates** for common patterns:
   - Primary Producer → Cross-Feeder
   - Primary Degrader → Cross-Feeder
   - Syntrophic Partner ↔ Syntrophic Partner
   - Host ↔ Symbiont

2. **Curation guidelines**:
   - Every taxon should have at least one interaction (unless host/matrix)
   - Community-level processes should specify primary organism
   - Use evidence snippets to validate interaction assignments

3. **Consider schema enhancements**:
   - Optional "community-level" flag for interactions
   - Support for indirect/weak connections
   - Confidence scores for inferred interactions

## Impact

**Before**: 51 communities had incomplete/inconsistent network data
**After**: 33 communities have corrected NCBITaxon IDs, 1 community fully curated
**Remaining**: 41 communities need interaction additions for disconnected taxa

This systematic curation ensures:
- Data integrity across taxonomy and interactions
- Complete network visualizations
- Accurate representation of microbial community structure
- Better queryability and downstream analysis
