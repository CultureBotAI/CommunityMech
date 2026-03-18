# Network Integrity Issues Triage

**Total:** 12 communities with network issues (123 total issues, 98 disconnected taxa)

## Strategy

### Category 1: Intentional Disconnected Taxa (Strain Collections)
**Action: Document as expected behavior**

These are strain screening/collection studies where individual strains are cataloged but pairwise interactions aren't the focus:

1. **GLBRC_Populus_Variovorax_SynCom28** (31 issues, 28 disconnected)
   - 28-strain collection testing compartment partitioning
   - Interactions describe community-level phenomena (niche partitioning, competition)
   - **Resolution**: Add note documenting that disconnected strains are intentional

2. **PMI_Variovorax_Thermotolerance_Collection** (8 issues, 6 disconnected)
   - Strain collection for thermotolerance screening
   - **Resolution**: Add note documenting intentional design

### Category 2: Missing Interaction Source/Target (Fixable)
**Action: Add missing source/target taxa to interactions**

These have interactions that reference non-existent taxa or are missing source_taxon fields:

3. **BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom** (12 issues: 1 missing source, 11 disconnected)
   - Fix: Add source_taxon to "Bifidobacterium HMO Degradation" interaction
   - Review: 11 disconnected taxa may indicate incomplete interaction network

4. **BioModels_MODEL2407300002_Sponge_Holobiont_Network** (6 issues: 3 missing source, 3 disconnected)
   - Fix: Add source_taxon to 3 interactions
   - Review: 3 disconnected taxa

5. **GLBRC_UFMP_Fermentation_Community** (14 issues: 2 missing source, 1 unknown source, 1 unknown target, 10 disconnected)
   - Fix: Add missing source_taxon fields
   - Fix: Correct interaction references to match taxonomy

6. **Mercury_SFA_EFPC_Sediment_Community** (14 issues: 3 missing source, 11 disconnected)
   - Fix: Add source_taxon to interactions
   - Review: Many disconnected taxa

7. **Rice_Duckweed_Bacillus_SynCom** (7 issues: 1 missing source, 1 unknown source, 1 unknown target, 4 disconnected)
   - Fix: Add/correct interaction taxa references

### Category 3: Minimal Interaction Networks (Review for Expansion)
**Action: Consider adding interactions or document as minimal**

These are intentionally simple communities with few interactions:

8. **BioModels_MODEL2204300001_Kefir_Community_Model** (2 disconnected)
   - 6 taxa, 4 interactions
   - L. kefiri and L. lactis disconnected
   - **Resolution**: Review literature for interactions or document as incomplete model

9. **KBase_Models_for_Zahmeeth_Original_PLOS** (3 issues: 1 missing source, 2 disconnected)
   - 4 taxa, 2 interactions
   - Minimal computational model

10. **KBase_ORT_Workflow_Community_Model** (6 issues: 2 missing source, 4 disconnected)
    - 4 taxa, 2 interactions
    - Minimal computational model

11. **TYQ1_Nematode_Biocontrol_SynCom** (8 issues: 1 missing source, 7 disconnected)
    - 8 taxa, 4 interactions
    - Many taxa without interactions

12. **mCAFEs_Brachypodium_RCC** (12 issues: 2 missing source, 10 disconnected)
    - 10 taxa, 2 interactions
    - Very sparse interaction network

## Action Plan

### Phase 1: Quick Fixes (Missing source_taxon fields)
Target: ~10 issues
- Add source_taxon to interactions missing them
- Correct interaction taxon references that don't match taxonomy

### Phase 2: Document Intentional Designs
Target: ~35 issues
- Add engineering_design notes to strain collections
- Document minimal models as computational/incomplete

### Phase 3: Literature-Based Expansion (Optional)
Target: Remaining disconnected taxa
- Review literature for additional interactions
- Use LLM repair tool for suggestions
- Manual curation for high-value communities

## Expected Impact

- **Phase 1**: Fix 10 critical errors → Quality score +50 points
- **Phase 2**: Reclassify 35 intentional issues → Quality score +70 points
- **Total**: Quality score improvement from 36/100 to ~80+/100
