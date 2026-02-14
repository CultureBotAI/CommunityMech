# CommunityMech: Microbial Community Mechanisms Knowledge Base

**Full Stack Implementation Plan**

Adapted from the Monarch dismech project for modeling specific microbial communities as individual YAML files per community.

---

## Executive Summary

This plan adapts the dismech (Disorder Mechanisms Knowledge Base) architecture for microbial communities, creating **CommunityMech** - a LinkML-based knowledge base for modeling microbial community structure, function, and interactions.

### Key Components

1. **LinkML Schema** - Define microbial community data model
2. **YAML Knowledge Base** - One file per community (e.g., `Human_Gut_Healthy.yaml`)
3. **Validation Stack** - Schema validation, reference validation, term validation
4. **KG Export** - Koza transform from rich YAML to KG (lossy but KG-friendly)
5. **Faceted Browser** - Interactive web interface for scientists to explore communities
6. **HTML Pages** - Rendered community pages with evidence

### Design Principles

- **YAML as source of truth** - Rich, expressive, nested YAML for agent consumption
- **Evidence-based** - All claims backed by PubMed references with validated snippets
- **Ontology-grounded** - NCBITaxon, ENVO, GO, CHEBI, etc.
- **Causal graphs** - Represent ecological interactions as directed graphs
- **Lossy KG transform** - Koza script preserves core facts for KG stacks

---

## Phase 1: Schema Design

### 1.1 Core Classes

Define core classes for microbial ecology (based on dismech's Disease/Pathophysiology model):

```yaml
classes:
  MicrobialCommunity:
    description: >
      A specific microbial community defined by environment, host, and ecological state.
    attributes:
      name:
        required: true
        description: Community identifier (e.g., "Human Gut Healthy Adult")

      environment_term:
        range: EnvironmentDescriptor
        description: ENVO term for the environment

      host_term:
        range: HostDescriptor
        description: NCBITaxon or anatomy term for host

      ecological_state:
        range: EcologicalStateEnum
        description: Health status (healthy, dysbiotic, diseased)

      description:
        multivalued: false
        description: Overview of the community

      taxonomy:
        range: TaxonomicComposition
        multivalued: true
        description: Taxonomic composition with abundance

      ecological_interactions:
        range: EcologicalInteraction
        multivalued: true
        description: Interactions between taxa and environment

      metabolic_functions:
        range: MetabolicFunction
        multivalued: true
        description: Community-level metabolic capabilities

      diversity_metrics:
        range: DiversityMetrics
        description: Alpha/beta diversity measurements

      stability:
        range: Stability
        description: Resilience, resistance, temporal dynamics

      environmental_factors:
        range: EnvironmentalFactor
        multivalued: true
        description: Environmental conditions (pH, O2, temperature)

      datasets:
        range: Dataset
        multivalued: true
        description: Omics datasets (16S, metagenome, metabolome)

  TaxonomicComposition:
    description: A taxon present in the community with abundance info
    attributes:
      taxon_term:
        range: TaxonDescriptor
        required: true
        description: NCBITaxon term for the organism

      abundance_level:
        range: AbundanceEnum
        description: Relative abundance (DOMINANT, ABUNDANT, COMMON, RARE)

      abundance_value:
        description: Quantitative abundance (% or count)

      functional_role:
        range: FunctionalRoleEnum
        multivalued: true
        description: Keystone, core, transient, pathobiont

      evidence:
        range: EvidenceItem
        multivalued: true

  EcologicalInteraction:
    description: >
      Interaction between taxa or between taxa and environment.
      Uses causal graph pattern with downstream edges (similar to dismech pathophysiology).
    attributes:
      name:
        required: true
        description: Interaction name (e.g., "Butyrate Cross-Feeding")

      description:
        description: Detailed explanation of the interaction

      interaction_type:
        range: InteractionTypeEnum
        description: Mutualism, competition, predation, commensalism, etc.

      source_taxon:
        range: TaxonDescriptor
        description: Source organism (if taxon-taxon)

      target_taxon:
        range: TaxonDescriptor
        description: Target organism

      metabolites:
        range: MetaboliteDescriptor
        multivalued: true
        description: CHEBI terms for metabolites involved

      biological_processes:
        range: BiologicalProcessDescriptor
        multivalued: true
        description: GO terms for processes

      downstream:
        range: InteractionDownstream
        multivalued: true
        description: Causal graph edges to other interactions

      evidence:
        range: EvidenceItem
        multivalued: true

  MetabolicFunction:
    description: Community-level metabolic capability
    attributes:
      name:
        required: true
        description: Function name (e.g., "Butyrate Production")

      description:
        description: Detailed explanation

      pathways:
        range: PathwayDescriptor
        multivalued: true
        description: KEGG or MetaCyc pathways

      metabolites:
        range: MetaboliteDescriptor
        multivalued: true
        description: Input/output metabolites

      genes:
        range: GeneDescriptor
        multivalued: true
        description: Key genes (e.g., bai operon for bile acid conversion)

      quantitative_value:
        description: Measured concentration or flux

      evidence:
        range: EvidenceItem
        multivalued: true

  DiversityMetrics:
    description: Ecological diversity measurements
    attributes:
      alpha_diversity:
        description: Within-community diversity (Shannon, Simpson)

      beta_diversity:
        description: Between-community diversity (Bray-Curtis, UniFrac)

      richness:
        description: Number of observed taxa

      evenness:
        description: Distribution of abundance across taxa

      anna_karenina_effect:
        type: boolean
        description: Increased stochasticity in dysbiotic state

      evidence:
        range: EvidenceItem
        multivalued: true

  Stability:
    description: Community stability and resilience
    attributes:
      resilience:
        description: Ability to return to baseline after perturbation

      resistance:
        description: Ability to resist perturbation

      alternative_stable_states:
        type: boolean
        description: Whether community exhibits bistability

      temporal_dynamics:
        description: Changes over time

      evidence:
        range: EvidenceItem
        multivalued: true
```

### 1.2 Descriptor Classes (Ontology Bindings)

```yaml
  TaxonDescriptor:
    description: Binds a taxon to NCBITaxon ontology
    attributes:
      preferred_term:
        required: true
        description: Human-readable taxon name
      term:
        range: Term
        required: true
        description: NCBITaxon ID

  EnvironmentDescriptor:
    description: Binds environment to ENVO
    attributes:
      preferred_term:
        required: true
      term:
        range: Term
        required: true
        description: ENVO ID (e.g., ENVO:0001998 for soil)

  MetaboliteDescriptor:
    description: Binds metabolite to CHEBI
    attributes:
      preferred_term:
        required: true
      term:
        range: Term
        required: true
        description: CHEBI ID (e.g., CHEBI:30089 for acetate)

  PathwayDescriptor:
    description: Binds pathway to KEGG/MetaCyc
    attributes:
      preferred_term:
        required: true
      term:
        range: Term
        description: KEGG pathway ID
```

### 1.3 Enums

```yaml
enums:
  EcologicalStateEnum:
    permissible_values:
      HEALTHY:
        description: Healthy, eubiotic state
      DYSBIOTIC:
        description: Dysbiotic but not necessarily diseased
      DISEASED:
        description: Associated with disease state
      PERTURBED:
        description: Recently perturbed (antibiotic, diet change)
      RECOVERING:
        description: Recovering from perturbation

  AbundanceEnum:
    permissible_values:
      DOMINANT:
        description: >1% relative abundance, dominant member
      ABUNDANT:
        description: 0.1-1% relative abundance
      COMMON:
        description: 0.01-0.1% relative abundance
      RARE:
        description: <0.01% relative abundance (rare biosphere)

  FunctionalRoleEnum:
    permissible_values:
      KEYSTONE:
        description: Low abundance but high network connectivity
      CORE:
        description: Consistently present across individuals
      TRANSIENT:
        description: Sporadically present
      PATHOBIONT:
        description: Commensal that can become pathogenic
      PRIMARY_DEGRADER:
        description: Degrades complex substrates
      CROSS_FEEDER:
        description: Utilizes metabolites from other taxa

  InteractionTypeEnum:
    permissible_values:
      MUTUALISM:
        description: Both benefit (+/+)
      COMMENSALISM:
        description: One benefits, other unaffected (+/0)
      COMPETITION:
        description: Both negatively affected (-/-)
      PREDATION:
        description: One benefits, other harmed (+/-)
      AMENSALISM:
        description: One harmed, other unaffected (-/0)
      CROSS_FEEDING:
        description: Metabolite exchange
      QUORUM_SENSING:
        description: Chemical signaling
```

---

## Phase 2: Knowledge Base Structure

### 2.1 Directory Layout

```
CommunityMech/
├── src/
│   └── communitymech/
│       ├── schema/
│       │   └── communitymech.yaml          # LinkML schema
│       ├── datamodel/                       # Generated Python models
│       ├── export/
│       │   ├── kgx_export.py               # Koza transform to KG
│       │   └── browser_export.py           # Faceted browser export
│       ├── render.py                        # HTML page generator
│       └── templates/                       # Jinja2 templates
├── kb/
│   └── communities/
│       ├── Human_Gut_Healthy_Adult.yaml
│       ├── Human_Gut_IBD_UC.yaml
│       ├── Human_Oral_Healthy.yaml
│       ├── Soil_Grassland_Temperate.yaml
│       ├── Marine_Surface_Oligotrophic.yaml
│       └── ...
├── conf/
│   ├── oak_config.yaml                      # OAK ontology adapters
│   └── qc_config.yaml                       # QC configuration
├── app/                                      # Faceted browser
│   ├── index.html                           # Browser UI
│   ├── data.js                              # Exported community data
│   └── schema.js                            # Schema metadata
├── pages/
│   └── communities/                         # Rendered HTML pages
├── tests/
│   └── test_communities.py
├── justfile                                 # Task runner
├── pyproject.toml
└── README.md
```

### 2.2 Example Community File

`kb/communities/Human_Gut_Healthy_Adult.yaml`:

```yaml
name: Human Gut Healthy Adult
ecological_state: HEALTHY
description: >
  The healthy adult human gut microbiome is dominated by Firmicutes and Bacteroidetes,
  with high diversity and metabolic capacity for fiber fermentation to SCFAs. Keystone
  taxa include Faecalibacterium prausnitzii (butyrate producer) and Akkermansia
  muciniphila (mucin degrader). The community exhibits resilience to dietary
  perturbations and maintains colonization resistance against pathogens.

environment_term:
  preferred_term: human gut
  term:
    id: ENVO:0001998  # or appropriate UBERON term
    label: human gut environment

host_term:
  preferred_term: Homo sapiens
  term:
    id: NCBITaxon:9606
    label: Homo sapiens

# Taxonomic composition
taxonomy:
  - taxon_term:
      preferred_term: Faecalibacterium prausnitzii
      term:
        id: NCBITaxon:853
        label: Faecalibacterium prausnitzii
    abundance_level: ABUNDANT
    abundance_value: "5-15%"
    functional_role:
      - KEYSTONE
      - CORE
    evidence:
      - reference: PMID:18936492
        supports: SUPPORT
        snippet: "F. prausnitzii represents more than 5% of the total bacterial population in healthy adults"
        explanation: Establishes F. prausnitzii as abundant core member

  - taxon_term:
      preferred_term: Akkermansia muciniphila
      term:
        id: NCBITaxon:239935
        label: Akkermansia muciniphila
    abundance_level: COMMON
    abundance_value: "1-4%"
    functional_role:
      - KEYSTONE
    evidence:
      - reference: PMID:23985875
        supports: SUPPORT
        snippet: "Akkermansia muciniphila comprises 1-4% of the human intestinal microbiota"

  - taxon_term:
      preferred_term: Bacteroides
      term:
        id: NCBITaxon:816
        label: Bacteroides
    abundance_level: DOMINANT
    abundance_value: "20-40%"
    functional_role:
      - CORE
      - PRIMARY_DEGRADER

# Ecological interactions (causal graph)
ecological_interactions:
  - name: Dietary Fiber Degradation
    description: >
      Primary degraders (Bacteroides, Prevotella) break down complex plant
      polysaccharides into oligosaccharides and monosaccharides, enabling
      cross-feeding to secondary fermenters.
    interaction_type: CROSS_FEEDING
    source_taxon:
      preferred_term: Bacteroides
      term:
        id: NCBITaxon:816
        label: Bacteroides
    biological_processes:
      - preferred_term: polysaccharide catabolic process
        term:
          id: GO:0000272
          label: polysaccharide catabolic process
    downstream:
      - target: Butyrate Production by Secondary Fermenters
        description: Oligosaccharides released by Bacteroides feed butyrate producers
    evidence:
      - reference: PMID:21995823
        supports: SUPPORT
        snippet: "Bacteroides encode extensive polysaccharide utilization loci enabling degradation of diverse plant glycans"

  - name: Butyrate Production by Secondary Fermenters
    description: >
      Faecalibacterium and Roseburia use acetyl-CoA pathway to produce butyrate
      from acetate and oligosaccharides released by primary degraders.
    interaction_type: CROSS_FEEDING
    source_taxon:
      preferred_term: Faecalibacterium prausnitzii
      term:
        id: NCBITaxon:853
        label: Faecalibacterium prausnitzii
    metabolites:
      - preferred_term: butyrate
        term:
          id: CHEBI:30089
          label: butyric acid
    biological_processes:
      - preferred_term: short-chain fatty acid biosynthetic process
        term:
          id: GO:0046460
          label: short-chain fatty acid biosynthetic process
    downstream:
      - target: Host Colonocyte Energy Metabolism
    evidence:
      - reference: PMID:18936492
        supports: SUPPORT
        snippet: "F. prausnitzii is one of the most important butyrate-producing bacteria in the human gut"

  - name: Host Colonocyte Energy Metabolism
    description: >
      Butyrate serves as primary energy source (~70%) for colonocytes via
      beta-oxidation, supporting epithelial barrier function and reducing
      inflammation via HDAC inhibition.
    biological_processes:
      - preferred_term: fatty acid beta-oxidation
        term:
          id: GO:0006635
          label: fatty acid beta-oxidation
    evidence:
      - reference: PMID:12480426
        supports: SUPPORT
        snippet: "Butyrate is the preferred energy source for colonocytes, providing approximately 70% of their energy needs"

  - name: Mucin Degradation and Cross-Feeding
    description: >
      Akkermansia muciniphila degrades mucin layer, releasing oligosaccharides
      that support other community members. Maintains gut barrier via mucin
      turnover stimulation.
    source_taxon:
      preferred_term: Akkermansia muciniphila
      term:
        id: NCBITaxon:239935
        label: Akkermansia muciniphila
    biological_processes:
      - preferred_term: mucin metabolic process
        term:
          id: GO:0006682  # glycoprotein metabolic process
          label: glycoprotein metabolic process
    evidence:
      - reference: PMID:23985875
        supports: SUPPORT
        snippet: "A. muciniphila is specialized in degrading mucin and resides in the mucus layer"

# Metabolic functions
metabolic_functions:
  - name: Short-Chain Fatty Acid Production
    description: >
      Community-level production of acetate, propionate, and butyrate from
      dietary fiber fermentation. Total SCFA ~50-150 mM in healthy adults.
    metabolites:
      - preferred_term: acetate
        term:
          id: CHEBI:30089
          label: acetic acid
      - preferred_term: propionate
        term:
          id: CHEBI:30768
          label: propionic acid
      - preferred_term: butyrate
        term:
          id: CHEBI:30089
          label: butyric acid
    quantitative_value: "Total SCFA 50-150 mM (molar ratio ~60:20:20)"
    evidence:
      - reference: PMID:12480426
        supports: SUPPORT
        snippet: "Total SCFA concentrations in the human colon range from 50 to 150 mM with a molar ratio of approximately 60:20:20 for acetate:propionate:butyrate"

  - name: Secondary Bile Acid Production
    description: >
      7α-dehydroxylation of primary bile acids (CA, CDCA) to secondary bile
      acids (DCA, LCA) by Clostridium scindens and other Clostridia carrying
      the bai operon. Provides colonization resistance against pathogens.
    genes:
      - preferred_term: bai operon
        description: Bile acid-inducible operon for 7α-dehydroxylation
    metabolites:
      - preferred_term: deoxycholic acid
        term:
          id: CHEBI:28834
          label: deoxycholic acid
    evidence:
      - reference: PMID:28066726
        supports: SUPPORT
        snippet: "C. scindens metabolizes primary bile acids to secondary bile acids via the bai operon"

# Diversity metrics
diversity_metrics:
  alpha_diversity: "Shannon index ~3.5-4.5 in healthy adults"
  richness: "~150-200 species-level OTUs typically detected"
  evenness: "High evenness with no single taxon >40% relative abundance"
  anna_karenina_effect: false
  evidence:
    - reference: PMID:22972295
      supports: SUPPORT
      snippet: "Healthy human gut microbiomes show high diversity with Shannon indices typically ranging from 3.5 to 4.5"

# Stability
stability:
  resilience: "High resilience - returns to baseline within 1-2 weeks after dietary perturbation"
  resistance: "Moderate resistance - composition shifts with diet but core taxa persist"
  alternative_stable_states: false
  temporal_dynamics: "Stable over months to years in adults; more variable in infants/elderly"
  evidence:
    - reference: PMID:25383538
      supports: SUPPORT
      snippet: "The gut microbiota of healthy adults is relatively stable over time, with return to baseline composition following perturbations"

# Environmental factors
environmental_factors:
  - name: pH
    value: "5.5-7.0 (varies by colonic region)"
    evidence:
      - reference: PMID:15831824
        supports: SUPPORT
        snippet: "Colonic pH ranges from approximately 5.5 in the proximal colon to 7.0 in the distal colon"

  - name: Oxygen availability
    value: "Anaerobic (<1% O2)"
    evidence:
      - reference: PMID:26185088
        supports: SUPPORT
        snippet: "The healthy gut lumen is predominantly anaerobic with oxygen concentrations below 1%"

# Datasets
datasets:
  - name: HMP Human Gut 16S
    description: Human Microbiome Project 16S rRNA gene sequencing of healthy adults
    reference: geo:GSE42722

  - name: MetaHIT metagenomes
    description: Metagenomic sequencing of European healthy cohort
    reference: PMID:20203603
```

---

## Phase 3: Validation Stack

### 3.1 Schema Validation

Use `linkml-validate` for schema conformance:

```bash
just validate kb/communities/Human_Gut_Healthy_Adult.yaml
```

### 3.2 Reference Validation

Implement reference validation to validate evidence snippets against PubMed abstracts (following dismech's approach):

```bash
just validate-references kb/communities/Human_Gut_Healthy_Adult.yaml
```

Prevents hallucination of evidence quotes.

### 3.3 Term Validation

Use `linkml-term-validator` to validate ontology term bindings:

```bash
just validate-terms
```

Checks that NCBITaxon, ENVO, CHEBI, GO terms exist and labels match.

### 3.4 OAK Configuration

`conf/oak_config.yaml`:

```yaml
adapters:
  # Taxonomy
  NCBITaxon:
    selector: sqlite:obo:ncbitaxon

  # Environment
  ENVO:
    selector: sqlite:obo:envo

  # Chemical entities
  CHEBI:
    selector: sqlite:obo:chebi

  # Biological processes
  GO:
    selector: sqlite:obo:go

  # Anatomy (for host)
  UBERON:
    selector: sqlite:obo:uberon

  # Cell types (for host cells affected by microbiome)
  CL:
    selector: sqlite:obo:cl
```

---

## Phase 4: KG Export (Koza Transform)

### 4.1 Koza Script Design

Create `src/communitymech/export/kgx_export.py` to transform YAML → KG edges (based on dismech's `src/dismech/export/kgx_export.py` pattern).

**Key transformations** (lossy but preserves core facts):

1. **Taxon → Community**: `biolink:part_of`
   ```
   NCBITaxon:853 (F. prausnitzii) --[part_of]--> CommunityMech:Human_Gut_Healthy
   ```

2. **Taxon → Metabolite**: `biolink:produces`
   ```
   NCBITaxon:853 --[produces]--> CHEBI:30089 (butyrate)
   ```

3. **Taxon → Taxon Interaction**: `biolink:interacts_with` + qualifier
   ```
   NCBITaxon:816 (Bacteroides) --[interacts_with]--> NCBITaxon:853
   qualifiers: [interaction_type: CROSS_FEEDING]
   ```

4. **Metabolite → Biological Process**: `biolink:participates_in`
   ```
   CHEBI:30089 (butyrate) --[participates_in]--> GO:0006635 (fatty acid beta-oxidation)
   ```

5. **Community → Environment**: `biolink:located_in`
   ```
   CommunityMech:Human_Gut_Healthy --[located_in]--> ENVO:0001998
   ```

### 4.2 Koza Configuration

`src/communitymech/export/kgx_export.py`:

```python
from koza import KozaTransform
import koza

@koza.transform_record()
def koza_transform(koza_ctx: KozaTransform, record: dict[str, Any]) -> None:
    """
    Transform community YAML to KGX edges.
    """
    community_id = f"CommunityMech:{record['name'].replace(' ', '_')}"

    # Taxon → Community edges
    for taxon in record.get("taxonomy", []):
        taxon_id = taxon["taxon_term"]["term"]["id"]
        edge = Association(
            id=_make_edge_id(),
            subject=taxon_id,
            predicate="biolink:part_of",
            object=community_id,
            publications=_extract_pmids(taxon.get("evidence", [])),
            primary_knowledge_source="infores:communitymech",
        )
        koza_ctx.write(edge)

    # Ecological interaction edges
    for interaction in record.get("ecological_interactions", []):
        if interaction.get("source_taxon") and interaction.get("target_taxon"):
            source_id = interaction["source_taxon"]["term"]["id"]
            target_id = interaction["target_taxon"]["term"]["id"]
            edge = Association(
                id=_make_edge_id(),
                subject=source_id,
                predicate="biolink:interacts_with",
                object=target_id,
                qualifiers=[f"interaction_type:{interaction.get('interaction_type')}"],
                publications=_extract_pmids(interaction.get("evidence", [])),
                primary_knowledge_source="infores:communitymech",
            )
            koza_ctx.write(edge)

    # ... similar for metabolic functions, etc.
```

### 4.3 Running Koza Transform

```bash
just kgx-export
# Outputs: output/communitymech_edges.tsv (KGX format)
```

This can then be loaded into any KG stack (KGX, Neo4j, SPARQL endpoint, etc.).

---

## Phase 5: Faceted Browser

### 5.1 Browser Export

Create `src/communitymech/export/browser_export.py` to aggregate community data for faceted search (based on dismech's browser_export.py).

**Facets for communities:**
- Environment (ENVO categories: soil, marine, gut, etc.)
- Host (human, mouse, plant, none)
- Ecological state (healthy, dysbiotic, diseased)
- Key taxa (Bacteroides, Faecalibacterium, etc.)
- Metabolic functions (SCFA production, methanogenesis, etc.)
- Diversity level (high, medium, low)
- Study type (16S, metagenome, metabolome)

### 5.2 Browser UI

Create `app/index.html` for microbial communities (based on dismech's faceted browser):

```html
<div class="facets">
  <div class="facet">
    <h3>Environment</h3>
    <label><input type="checkbox" value="human gut"> Human Gut</label>
    <label><input type="checkbox" value="soil"> Soil</label>
    <label><input type="checkbox" value="marine"> Marine</label>
  </div>

  <div class="facet">
    <h3>Ecological State</h3>
    <label><input type="checkbox" value="healthy"> Healthy</label>
    <label><input type="checkbox" value="dysbiotic"> Dysbiotic</label>
  </div>

  <div class="facet">
    <h3>Key Taxa</h3>
    <label><input type="checkbox" value="Faecalibacterium"> Faecalibacterium</label>
    <label><input type="checkbox" value="Bacteroides"> Bacteroides</label>
  </div>

  <div class="facet">
    <h3>Functions</h3>
    <label><input type="checkbox" value="SCFA"> SCFA Production</label>
    <label><input type="checkbox" value="bile_acid"> Bile Acid Metabolism</label>
  </div>
</div>
```

### 5.3 Generation Script

```bash
just gen-browser
# 1. Exports kb/communities/*.yaml to app/data.js
# 2. Aggregates facets (environment, taxa, functions)
# 3. Creates searchable index
```

Deploy to GitHub Pages:
```bash
just deploy
# Deploys app/ to https://YOUR-ORG.github.io/CommunityMech/app/
```

---

## Phase 6: HTML Page Rendering

### 6.1 Template Design

Create `src/communitymech/templates/community.html.jinja` (based on dismech's disorder.html.jinja):

**Sections:**
1. **Overview** - Description, environment, host
2. **Taxonomic Composition** - Table with taxa, abundance, functional roles
3. **Ecological Interactions** - Interactive causal graph visualization
4. **Metabolic Functions** - SCFA production, bile acids, etc.
5. **Diversity & Stability** - Metrics with evidence
6. **Environmental Conditions** - pH, O2, temperature
7. **Datasets** - Links to GEO, SRA, etc.
8. **References** - All PMIDs cited

### 6.2 Causal Graph Visualization

Use D3.js or Cytoscape.js to render `ecological_interactions` as interactive graph.

Example:
```
[Bacteroides] --fiber degradation--> [oligosaccharides] --cross-feeding--> [F. prausnitzii]
                                                                                  |
                                                                            butyrate production
                                                                                  |
                                                                                  v
                                                                        [Host Colonocyte Energy]
```

### 6.3 Generation

```bash
just gen-html kb/communities/Human_Gut_Healthy_Adult.yaml
# Outputs: pages/communities/Human_Gut_Healthy_Adult.html
```

---

## Phase 7: Integration with Kevin's Koza PR

### 7.1 Review Kevin's PR

From the PR list, Kevin's open PRs are:
- #336: Remove case-colliding Holt-Oram page
- #319: Add Central Core Myopathy disorder entry

Let me check for koza-related PRs or branches in the repo history.

**Action:** Review the cloned dismech repository for koza implementation patterns:

```bash
cd dismech  # The locally cloned reference repo
cat src/dismech/export/kgx_export.py
# Study the pattern for our implementation
```

### 7.2 Koza Transform Pattern

Based on the existing `src/dismech/export/kgx_export.py`, Kevin's pattern:

1. **Pure transform function** (`transform()`) - testable without Koza runner
2. **Koza-decorated wrapper** (`@koza.transform_record()`) - called by Koza
3. **Biolink model compliance** - Uses `pydantic` Biolink models
4. **Evidence formatting** - Preserves PMID + snippet in `supporting_text`
5. **Knowledge provenance** - Sets `primary_knowledge_source` and `agent_type`

**Apply same pattern to CommunityMech:**

```python
def transform(record: dict[str, Any]) -> Iterator[Association]:
    """Pure function for extracting KGX edges from community record."""
    community_id = f"CommunityMech:{record['name'].replace(' ', '_')}"

    # Extract edges...
    for taxon in record.get("taxonomy", []):
        edge = taxon_to_edge(community_id, taxon)
        if edge:
            yield edge

    for interaction in record.get("ecological_interactions", []):
        edge = interaction_to_edge(community_id, interaction)
        if edge:
            yield edge

@koza.transform_record()
def koza_transform(koza_ctx: KozaTransform, record: dict[str, Any]) -> None:
    """Koza wrapper - called by Koza runner."""
    for edge in transform(record):
        koza_ctx.write(edge)
```

---

## Phase 8: Testing & QC

### 8.1 Test Suite

```python
# tests/test_communities.py

def test_schema_validation():
    """All community files validate against schema"""
    for yaml_file in Path("kb/communities").glob("*.yaml"):
        validate_yaml(yaml_file, "src/communitymech/schema/communitymech.yaml")

def test_taxon_terms_exist():
    """NCBITaxon terms exist in ontology"""
    # Use OAK to verify

def test_evidence_references():
    """All evidence snippets match PubMed abstracts"""
    # Use linkml-reference-validator

def test_causal_graph_acyclic():
    """Ecological interaction graphs are acyclic (or explicitly model cycles)"""
    # Build graph, check for cycles

def test_kgx_export():
    """Koza transform produces valid KGX edges"""
    # Run transform, validate output
```

### 8.2 QC Commands

```bash
# Full QC
just qc

# Individual checks
just validate-all
just validate-terms
just validate-references
just pytest-all

# Compliance scoring (% of recommended fields filled)
just compliance-all
```

---

## Phase 9: Skills & Agent Integration

### 9.1 Claude Code Skills

Create `.claude/skills/` for agent-assisted curation:

1. **`community-curation`** - General community curation workflow
2. **`microbe-terms`** - NCBITaxon, ENVO lookup with OAK
3. **`metabolite-terms`** - CHEBI lookup for metabolites
4. **`ecological-interactions`** - Template for causal graph patterns
5. **`bugsigdb-integration`** - Query BugSigDB for taxa signatures

### 9.2 Agent Workflows

**Example: Adding a new community**

```bash
# User: "Add a community for soil grassland temperate"
# Agent uses `community-curation` skill:

1. Search BugSigDB, literature for taxonomic signatures
2. Generate YAML template with:
   - Environment term (ENVO:0000106 - grassland)
   - Dominant taxa (NCBITaxon terms)
   - Metabolic functions (nitrogen fixation, cellulose degradation)
3. Validate evidence snippets against PMIDs
4. Run full QC
5. Generate HTML preview
6. Create PR
```

### 9.3 YAML as Agent Input

**Why YAML > KG for agents:**
- **Rich structure** - Nested causal graphs, evidence chains
- **Human-readable** - Easy for agents to understand context
- **Evolvable** - Can add new fields without KG schema migration
- **Evidence-bound** - Every claim has snippet + PMID
- **Validation** - Schema enforces consistency

Agents can:
1. Read YAML to understand community structure
2. Reason over causal graphs
3. Generate hypotheses about interactions
4. Add new evidence from literature
5. Propose new communities based on existing patterns

---

## Phase 10: Deployment & Documentation

### 10.1 GitHub Pages Deployment

```bash
# Deploy faceted browser
just deploy

# Deployed to:
# https://YOUR-ORG.github.io/CommunityMech/app/
# https://YOUR-ORG.github.io/CommunityMech/pages/communities/
```

### 10.2 Documentation

1. **README.md** - Quick start, installation, usage
2. **docs/** - MkDocs documentation site
   - Schema reference
   - Curation guide
   - Ontology term guidelines
   - Evidence validation SOP
3. **CLAUDE.md** - Agent-facing guidance (like the dismech project)
4. **Skills README** - How to use curation skills

### 10.3 CI/CD

`.github/workflows/`:
- **validate.yml** - Run QC on PRs
- **deploy.yml** - Deploy browser on merge to main
- **kgx-export.yml** - Generate KG edges on release

---

## Phase 11: Future Enhancements

### 11.1 Quantitative Models

Integrate with systems biology models:
- **BIGG models** - Link to metabolic reconstructions
- **VMH** - Virtual Metabolic Human models
- **Flux balance analysis** - Community-level FBA

### 11.2 Dynamic Simulations

Link to:
- **MICOM** - Microbial community modeling
- **BacArena** - Agent-based modeling
- **cFBA** - Community flux balance analysis

### 11.3 Comparative Genomics

Add `genome_annotations`:
```yaml
genome_annotations:
  - taxon_term:
      preferred_term: Faecalibacterium prausnitzii
      term:
        id: NCBITaxon:853
    genome_id: GCF_000162535.1
    key_genes:
      - gene: butyryl-CoA dehydrogenase
        locus_tag: FAEPRA_01234
        function: Butyrate production
```

### 11.4 Temporal Dynamics

Model time-series:
```yaml
temporal_dynamics:
  - timepoint: Week 0 (pre-antibiotic)
    diversity: "Shannon 4.2"
    dominant_taxa: [Bacteroides, Faecalibacterium]

  - timepoint: Week 1 (post-antibiotic)
    diversity: "Shannon 2.1"
    dominant_taxa: [Enterococcus, Klebsiella]

  - timepoint: Week 4 (recovery)
    diversity: "Shannon 3.8"
    dominant_taxa: [Bacteroides, Faecalibacterium]
```

---

## Implementation Roadmap

### Sprint 1: Foundation (Week 1-2)
- [x] Repository structure created
- [x] Seed data added (35 communities)
- [ ] Design core schema (MicrobialCommunity, TaxonomicComposition, EcologicalInteraction)
- [ ] Set up OAK adapters for NCBITaxon, ENVO, CHEBI
- [ ] Create first example from seed data (e.g., Synechococcus-E.coli SPC)
- [ ] Implement schema validation

### Sprint 2: Validation (Week 3)
- [ ] Set up reference validator for evidence
- [ ] Set up term validator for ontology bindings
- [ ] Add pytest test suite
- [ ] QC dashboard

### Sprint 3: KG Export (Week 4)
- [ ] Implement Koza transform (pure function + decorator)
- [ ] Map ecological interactions → Biolink edges
- [ ] Test KGX output
- [ ] Document lossy transformations

### Sprint 4: Browser (Week 5-6)
- [ ] Adapt browser export script
- [ ] Design faceted search UI
- [ ] Implement community page renderer
- [ ] Add causal graph visualization (D3.js/Cytoscape)
- [ ] Deploy to GitHub Pages

### Sprint 5: Skills & Agents (Week 7)
- [ ] Create curation skills
- [ ] CLAUDE.md agent guidance
- [ ] Test agent workflows
- [ ] BugSigDB integration

### Sprint 6: Production (Week 8)
- [ ] Add 10+ diverse communities (gut, soil, marine, oral, etc.)
- [ ] Full QC on all files
- [ ] Documentation
- [ ] CI/CD setup
- [ ] Release v1.0

---

## Success Metrics

1. **Coverage**: 20+ diverse communities modeled
2. **Validation**: 100% schema compliance, term validation, reference validation
3. **Browser**: Functional faceted search deployed
4. **KG**: Koza export produces valid KGX edges
5. **Agent-friendly**: Agents can read YAML and generate new communities
6. **Scientist-friendly**: Browser makes work accessible to non-programmers

---

## Appendix A: Ontologies

| Ontology | Purpose | OAK Adapter |
|----------|---------|-------------|
| NCBITaxon | Microbial taxa | `sqlite:obo:ncbitaxon` |
| ENVO | Environments | `sqlite:obo:envo` |
| CHEBI | Chemical entities | `sqlite:obo:chebi` |
| GO | Biological processes | `sqlite:obo:go` |
| UBERON | Host anatomy | `sqlite:obo:uberon` |
| CL | Cell types | `sqlite:obo:cl` |
| KEGG | Metabolic pathways | Custom adapter |

## Appendix B: Key References

### Ecological Concepts
- Anna Karenina: PMID:28836573
- Diversity/stability: PMID:22972295
- Keystone species: PMID:21995823

### Gut Microbiome
- HMP: PMID:22699609
- MetaHIT: PMID:20203603
- F. prausnitzii: PMID:18936492
- A. muciniphila: PMID:23985875

### Methods
- BugSigDB: https://bugsigdb.org
- MICOM: PMID:32393734
- Koza: https://github.com/monarch-initiative/koza

---

**End of Plan**
