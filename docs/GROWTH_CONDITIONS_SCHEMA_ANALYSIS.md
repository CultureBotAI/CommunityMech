# Growth Conditions Schema Analysis

## Current Schema Capabilities

### GrowthMedia Class
**Existing fields:**
- `name` (required) - Name of growth medium
- `culturemech_id` - Link to CultureMech database
- `culturemech_url` - URL to CultureMech entry
- `composition[]` - List of GrowthMediaComponent
- `ph` - pH of medium (string)
- `temperature` - Incubation temperature (string)
- `temperature_unit` - Unit for temperature
- `atmosphere` - Atmospheric conditions (string, freetext)
- `preparation_notes` - Additional details
- `evidence[]` - Evidence items

### EnvironmentalFactor Class
**Existing fields:**
- `name` (required) - Factor name
- `value` - Measured/specified value
- `unit` - Unit of measurement
- `description` - Description
- `evidence[]` - Evidence items

## Gap Analysis

### Missing/Underspecified Fields

#### 1. **Atmosphere/Oxygen Requirements**
**Current:** Freetext string
**Issues:** Inconsistent terminology, hard to query
**Recommendation:** Add enum for standardization

```yaml
AtmosphereEnum:
  AEROBIC:
    description: Requires oxygen
  ANAEROBIC:
    description: No oxygen required
  MICROAEROBIC:
    description: Reduced oxygen (2-10%)
  FACULTATIVE_ANAEROBIC:
    description: Can grow with or without oxygen
```

#### 2. **Salinity**
**Current:** Can use EnvironmentalFactor but no standard field
**Recommendation:** Add to GrowthMedia

```yaml
salinity:
  description: Salinity of growth medium (NaCl equivalent)
salinity_unit:
  description: Unit for salinity (%, M, g/L, ppt)
```

#### 3. **Pressure**
**Current:** Not captured
**Recommendation:** Add to EnvironmentalFactor or GrowthMedia for extremophiles

```yaml
pressure:
  description: Pressure for cultivation (e.g., deep-sea communities)
pressure_unit:
  description: Unit for pressure (atm, bar, MPa, psi)
```

#### 4. **Light Conditions**
**Current:** Can use EnvironmentalFactor
**Recommendation:** Add structured fields for phototrophs

```yaml
light_regime:
  description: Light/dark cycle (e.g., "16h/8h", "continuous", "dark")
light_intensity:
  description: Light intensity value
light_intensity_unit:
  description: Unit (μmol photons/m²/s, lux, etc.)
wavelength:
  description: Specific wavelength if relevant (e.g., red/blue LED)
```

#### 5. **Growth Rate Parameters**
**Current:** Not captured
**Recommendation:** Add to TaxonomicComposition

```yaml
doubling_time:
  description: Population doubling time
doubling_time_unit:
  description: Unit (hours, days, minutes)
growth_rate:
  description: Specific growth rate (μ)
growth_rate_unit:
  description: Unit (1/h, 1/day)
```

#### 6. **Redox Potential**
**Current:** Not captured
**Recommendation:** Add for metal-cycling and anaerobic communities

```yaml
redox_potential:
  description: Oxidation-reduction potential
redox_potential_unit:
  description: Unit (mV vs SHE, Eh)
```

#### 7. **Inoculum Information**
**Current:** Not captured
**Recommendation:** Add to GrowthMedia

```yaml
inoculum_source:
  description: Source of inoculum
inoculum_size:
  description: Initial cell density or %v/v
inoculum_unit:
  description: Unit (cells/mL, OD600, %v/v)
```

## Recommended Schema Updates

### Option 1: Minimal Updates (Add Enums Only)
- Add `AtmosphereEnum` for standardized oxygen requirements
- Keep other parameters in `EnvironmentalFactor`

### Option 2: Comprehensive Updates (Recommended)
- Add atmosphere enum
- Add structured fields for salinity, pressure, light
- Add growth rate fields to TaxonomicComposition
- Add redox potential field
- Add inoculum fields to GrowthMedia

### Option 3: New GrowthConditions Class
Create a comprehensive `GrowthConditions` class that encompasses:
- All physical parameters (temp, pH, pressure, salinity)
- Atmospheric requirements
- Light conditions
- Redox conditions
- Links to GrowthMedia

## Community Type Analysis

### By Category - Growth Parameter Requirements

**AMD/Biomining Communities (19 communities):**
- Critical: pH (extreme acidic), temperature, redox potential, metal concentrations
- Media: Acidic mineral salts media (9K, modified 9K)
- Atmosphere: Often aerobic/microaerobic

**Syntrophy Communities (8 communities):**
- Critical: Strict anaerobic, temperature, pH (near neutral)
- Media: Defined anaerobic media
- Atmosphere: Strictly anaerobic (H2/CO2 headspace common)

**Phytoplankton/Algal Communities (4 communities):**
- Critical: Light intensity/regime, temperature, pH, salinity
- Media: Marine/freshwater media (f/2, BG-11)
- Atmosphere: Aerobic, often CO2-enriched

**Rhizosphere SynComs (12 communities):**
- Critical: Temperature, pH, atmosphere, plant nutrients
- Media: R2A, TSA, KB, plant-specific media
- Atmosphere: Aerobic to microaerobic

**Lignocellulose Degraders (3 communities):**
- Critical: Temperature, pH, substrate concentration
- Media: Cellulose/xylan-containing media
- Atmosphere: Anaerobic to aerobic

## Curation Priority

### High Priority (Structured Data Available)
1. Synthetic communities with published protocols
2. Model systems (DIET, syntrophy)
3. Communities with deposited strains (DSM, ATCC)

### Medium Priority (Literature Mining Required)
1. Natural communities with cultivation attempts
2. Enrichment cultures
3. Bioreactor communities

### Low Priority (Environmental Only)
1. Uncultivated communities
2. Metagenome-only studies
3. Field samples without cultivation

## Curation Workflow

1. **Literature Search**
   - Original publication + citing papers
   - Methods sections for media composition
   - Supplementary materials for detailed protocols
   - Culture collection records (DSMZ, ATCC, JGI)

2. **Data Extraction**
   - Growth media composition
   - Physical parameters (temp, pH, atmosphere)
   - Incubation conditions
   - Growth rates (if available)

3. **Evidence Recording**
   - PMID/DOI for each parameter
   - Direct quotes from methods
   - Protocol URLs if available

4. **Quality Control**
   - Cross-reference with CultureMech
   - Verify CHEBI terms for components
   - Validate units and ranges

## Next Steps

1. **Schema Decision:** Determine which option to implement
2. **Pilot Curation:** Start with 5-10 well-documented communities
3. **Template Creation:** Create YAML templates for different community types
4. **Batch Curation:** Scale to all communities
5. **Validation:** Run QC checks and generate reports
