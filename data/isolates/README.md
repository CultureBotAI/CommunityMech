# Microbial Isolates

This directory contains single-organism communities (isolates) that were originally in `kb/communities/` but represent monocultures rather than multi-member microbial communities.

## Rationale

These files are maintained in the CommunityMech knowledge base format for:
- **Interoperability**: Consistent schema with multi-member communities
- **Evidence tracking**: Full PMID/DOI reference support
- **Metadata standardization**: Engineering design, environmental factors, etc.
- **Reusability**: Can be referenced as members of larger synthetic communities

## Contents

### Biomining Isolates

1. **Aspergillus_Indium_LED_Recovery.yaml**
   - Organism: *Aspergillus niger*
   - Application: Indium recovery from waste LCD/LED panels
   - Method: Indirect bioleaching via organic acid production
   - Performance: 100% indium yield in 1.5 hours at 70°C

2. **Methylobacterium_REE_Ewaste_Platform.yaml**
   - Organism: *Methylobacterium extorquens*
   - Application: Rare earth element recovery from e-waste
   - Category: BIOMINING

### Biotechnology Isolates

3. **Chromobacterium_Gold_Biocyanidation.yaml**
   - Organism: *Chromobacterium violaceum*
   - Application: Gold extraction via biocyanidation
   - Category: BIOTECHNOLOGY

4. **BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml**
   - Organism: *Rothia*
   - Application: Kefir fermentation modeling
   - Source: BioModels database
   - Category: BIOTECHNOLOGY

## File Format

All isolates follow the `MicrobialCommunity` LinkML schema with:
- Single entry in `taxonomy` section
- Full evidence references (PMID/DOI)
- Engineering design metadata (where applicable)
- Environmental factors and growth conditions

## Usage

To validate an isolate file:
```bash
just validate data/isolates/Aspergillus_Indium_LED_Recovery.yaml
```

To include isolates in analysis pipelines, treat them as single-member communities with `len(taxonomy) == 1`.

---

**Migration Date**: March 8, 2026
**Original Location**: `kb/communities/`
**Communities Remaining**: 78 multi-member communities
