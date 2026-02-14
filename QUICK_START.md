# CommunityMech Quick Start

## What You're Getting

A complete stack adapted from Monarch's dismech for modeling microbial communities:

```
Rich YAML Files → Validation → KG Export (Koza) → Faceted Browser
     ↑                                                    ↓
   Agent Input                                    Scientist-Friendly UI
```

## Key Design Decisions

### 1. YAML as Source of Truth
- **Why**: Rich, nested, agent-friendly
- **Not**: KG-first (KG is derived via lossy Koza transform)
- **Advantage**: Agents can reason over full causal graphs, evidence chains

### 2. Evidence-Based Everything
- Every claim has PMID + validated snippet
- Reference validator prevents hallucinations
- Like dismech: snippets must match PubMed abstracts

### 3. Causal Graphs for Ecology
```yaml
ecological_interactions:
  - name: Dietary Fiber Degradation
    downstream:
      - target: Butyrate Production
  - name: Butyrate Production
    downstream:
      - target: Colonocyte Energy
```

### 4. Ontology-Grounded
- NCBITaxon for taxa
- ENVO for environments
- CHEBI for metabolites
- GO for processes
- Term validator ensures no fake terms

### 5. Koza Transform (Lossy but KG-Friendly)
Converts rich YAML → simple KGX edges:
```
F. prausnitzii --[produces]--> butyrate
Bacteroides --[interacts_with]--> F. prausnitzii
```

## File Structure

```
kb/communities/Human_Gut_Healthy_Adult.yaml  # Rich source data
         ↓ (validation)
         ✓ Schema, terms, references validated
         ↓ (koza transform)
output/edges.tsv                              # KGX edges for KG stacks
         ↓ (browser export)
app/data.js                                   # Faceted search data
         ↓ (render)
pages/communities/Human_Gut_Healthy_Adult.html  # Human-readable page
```

## Commands

```bash
# Validate a community file
just validate kb/communities/Human_Gut_Healthy_Adult.yaml

# Validate evidence against PubMed
just validate-references kb/communities/Human_Gut_Healthy_Adult.yaml

# Validate ontology terms
just validate-terms

# Export to KG (Koza)
just kgx-export

# Generate faceted browser
just gen-browser

# Deploy to GitHub Pages
just deploy
```

## Example Community File Structure

```yaml
name: Human Gut Healthy Adult
ecological_state: HEALTHY

environment_term:
  preferred_term: human gut
  term:
    id: ENVO:0001998
    label: human gut environment

taxonomy:
  - taxon_term:
      preferred_term: Faecalibacterium prausnitzii
      term:
        id: NCBITaxon:853
        label: Faecalibacterium prausnitzii
    abundance_level: ABUNDANT
    functional_role: [KEYSTONE, CORE]
    evidence:
      - reference: PMID:18936492
        supports: SUPPORT
        snippet: "F. prausnitzii represents more than 5% of total..."

ecological_interactions:
  - name: Butyrate Production
    source_taxon:
      preferred_term: Faecalibacterium prausnitzii
      term:
        id: NCBITaxon:853
    metabolites:
      - preferred_term: butyrate
        term:
          id: CHEBI:30089
    downstream:
      - target: Host Colonocyte Energy
    evidence:
      - reference: PMID:18936492

metabolic_functions:
  - name: SCFA Production
    quantitative_value: "50-150 mM total SCFA"
    evidence:
      - reference: PMID:12480426
```

## What Makes This Better Than a Simple KG

### Rich YAML (Agent-Friendly)
```yaml
# Can represent complex evidence chains
evidence:
  - reference: PMID:123
    snippet: "Exact quote"
    explanation: "Why this supports the claim"
    evidence_source: HUMAN_CLINICAL  # vs MODEL_ORGANISM, IN_VITRO

# Can represent causal graphs with context
downstream:
  - target: Next Process
    description: "Why this leads to that"
```

### KG Export (KG-Stack-Friendly)
```
# Simplified for graph traversal
NCBITaxon:853 --[produces]--> CHEBI:30089
```

**Trade-off**: KG loses evidence detail, but gains graph algorithms.

**Solution**: Use YAML for agents, KG for integration.

## Integration with Kevin's Koza Work

Kevin's pattern from dismech (see `src/dismech/export/kgx_export.py`):

1. **Pure transform function** - testable without Koza
```python
def transform(record: dict) -> Iterator[Association]:
    # Extract edges from YAML
    for taxon in record["taxonomy"]:
        yield taxon_to_edge(taxon)
```

2. **Koza decorator** - for runner
```python
@koza.transform_record()
def koza_transform(ctx, record):
    for edge in transform(record):
        ctx.write(edge)
```

3. **Biolink compliance** - uses pydantic models
4. **Evidence preservation** - PMID + snippet in `supporting_text`

## Faceted Browser

Adapted from dismech's `app/index.html`:

**Facets:**
- Environment (gut, soil, marine)
- Ecological state (healthy, dysbiotic)
- Key taxa (Bacteroides, Faecalibacterium)
- Functions (SCFA, bile acids)
- Diversity (high, medium, low)

**Output**: Deployed to GitHub Pages at `YOUR-ORG.github.io/CommunityMech/app/`

## Why Scientists Will Love It

1. **No coding required** - Browse communities in web UI
2. **Evidence for every claim** - Click through to PubMed
3. **Interactive graphs** - Visualize ecological interactions
4. **Searchable** - Find communities by taxa, function, environment
5. **Linked to ontologies** - Terms link to OBO Foundry browsers

## Why Agents Will Love It

1. **Structured YAML** - Easy to parse and reason over
2. **Causal graphs** - Understand ecological dynamics
3. **Evidence chains** - See how we know what we know
4. **Schema-validated** - Guaranteed structure
5. **Rich context** - Not just facts, but mechanistic explanations

## Next Steps

1. **Review full plan**: `COMMUNITY_MECH_PLAN.md`
2. **Start Sprint 1**: Set up schema and first example
3. **Test Koza**: Ensure KGX export works
4. **Deploy browser**: Get it live for scientists

## Questions?

- Read `COMMUNITY_MECH_PLAN.md` for details
- Check dismech repo for reference implementation
- See dismech's `CLAUDE.md` for agent curation patterns
