# CommunityMech

**Microbial Community Mechanisms Knowledge Base**

A LinkML-based knowledge base for modeling microbial community structure, function, and ecological interactions with evidence-based validation.

---

## 🎯 Project Vision

Model specific microbial communities as individual YAML files, combining:
- Rich, expressive YAML for agent consumption
- Validated evidence chains (anti-hallucination)
- Ontology-grounded terms (NCBITaxon, ENVO, CHEBI, GO)
- Causal graphs for ecological interactions
- Faceted browser for scientists
- KG export for integration (via Koza)

**Adapted from**: [Monarch Initiative's dismech](https://github.com/monarch-initiative/dismech)

---

## 🏗️ Architecture

```
Rich YAML Source
  kb/communities/Human_Gut_Healthy_Adult.yaml
       ↓
  Validation Stack
  ├── Schema validation (linkml-validate)
  ├── Term validation (linkml-term-validator + OAK)
  └── Reference validation (snippets vs PubMed)
       ↓
  Dual Output
  ├── Koza Transform → KGX Edges (for KG stacks)
  └── Browser Export → Faceted Search (for scientists)
```

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/CultureBotAI/CommunityMech.git
cd CommunityMech

# Install dependencies
just install

# Or with uv directly
uv sync --extra dev
```

### Validate a Community

```bash
# Schema validation
just validate kb/communities/Human_Gut_Healthy_Adult.yaml

# Reference validation (prevent hallucination)
just validate-references kb/communities/Human_Gut_Healthy_Adult.yaml

# Term validation (check ontology terms)
just validate-terms
```

### Generate Outputs

```bash
# Export to KG (Koza transform)
just kgx-export

# Generate faceted browser
just gen-browser

# Generate HTML pages
just gen-html-all
```

> **Note**: Commands above are planned for implementation. See [COMMUNITY_MECH_PLAN.md](COMMUNITY_MECH_PLAN.md) for development roadmap.

---

## 📁 Repository Structure

```
CommunityMech/
├── src/
│   └── communitymech/
│       ├── schema/
│       │   └── communitymech.yaml      # LinkML schema
│       ├── datamodel/                   # Generated Python models
│       ├── export/
│       │   ├── kgx_export.py           # Koza transform to KG
│       │   └── browser_export.py       # Faceted browser export
│       ├── render.py                    # HTML page generator
│       └── templates/                   # Jinja2 templates
├── kb/
│   └── communities/
│       ├── Human_Gut_Healthy_Adult.yaml
│       ├── Human_Gut_IBD_UC.yaml
│       ├── Soil_Grassland_Temperate.yaml
│       └── ...
├── conf/
│   ├── oak_config.yaml                  # OAK ontology adapters
│   └── qc_config.yaml                   # QC configuration
├── app/                                  # Faceted browser
│   ├── index.html
│   ├── data.js
│   └── schema.js
├── pages/
│   └── communities/                     # Rendered HTML pages
├── tests/
│   └── test_communities.py
├── .claude/
│   └── skills/                          # Claude Code curation skills
├── justfile                             # Task runner
├── pyproject.toml
├── COMMUNITY_MECH_PLAN.md              # Full implementation plan
├── QUICK_START.md                       # Quick reference
└── README.md
```

---

## 📖 Documentation

- **[Implementation Plan](COMMUNITY_MECH_PLAN.md)** - Complete 11-phase plan
- **[Quick Start Guide](QUICK_START.md)** - Quick reference
- **[Schema Documentation](docs/)** - LinkML schema reference
- **[Cross-Repo Linking](docs/cross_repo_linking.md)** - Environmental linking to CultureMech and MediaIngredientMech
- **[Growth Media Linking](docs/media_linking.md)** - Cultivation-based media linking

---

## 📦 KGX export (downstream consumer contract)

CommunityMech publishes its community knowledge graph as KGX TSV on
every release. The artifact has stable column shapes, deterministic
edge IDs, and propagates literature evidence directly into edge
metadata so downstream graphs preserve provenance.

### Where to find it

- **Latest release:** GitHub Releases page → `nodes.tsv.gz`,
  `edges.tsv.gz`, and `manifest.json` attached to each release.
- **CI artifacts:** every push and release run uploads the same
  files to the workflow's Artifacts panel
  (`.github/workflows/kgx-release.yaml`, ~90-day retention).
- **Local build:** `just kgx-export` writes them to
  `output/kgx/`. `just kgx-validate` runs structural checks.

### File schemas

`nodes.tsv` columns: `id, category, name, description, provided_by`

`edges.tsv` columns: `id, subject, predicate, object, category, publications, supporting_text, knowledge_level, agent_type, primary_knowledge_source`

Edge `id` values are deterministic UUID5 derived from `(subject,
predicate, object, qualifier)` — re-running the export with the
same input produces byte-identical IDs.

### Edge types

| Predicate | Subject category | Object category | Edge category |
|---|---|---|---|
| `biolink:located_in` | `biolink:OrganismalEntity` (community) | `biolink:EnvironmentalFeature` (ENVO) | `biolink:OrganismToEnvironmentAssociation` |
| `biolink:has_part` | `biolink:OrganismalEntity` (community) | `biolink:OrganismTaxon` (NCBITaxon) | `biolink:OrganismToOrganismAssociation` |
| `biolink:related_to` | `biolink:OrganismalEntity` (community) | `biolink:ChemicalEntity` (CHEBI metals/REE) | `biolink:ChemicalEntityToOrganismalEntityAssociation` |
| `biolink:occurs_in` | `biolink:OrganismalEntity` (community) | growth medium | `biolink:Association` |

### Provenance & evidence

Every edge derived from a community evidence claim carries:

- `publications`: pipe-separated CURIEs (e.g.
  `PMID:18936492|DOI:10.1099/00207713-50-4-1539`)
- `supporting_text`: pipe-separated verbatim snippets (the same
  ones that pass MIM's anti-hallucination Phase 1 validator)
- `knowledge_level`: `knowledge_assertion` (curator-asserted)
- `agent_type`: `manual_agent`
- `primary_knowledge_source`: `infores:communitymech`

### Stability commitments

- Column order in both TSVs is fixed; new columns will only be
  appended at the right.
- Edge IDs are stable across runs unless the underlying
  `(subject, predicate, object, qualifier)` tuple changes.
- `infores:communitymech` is the canonical knowledge-source id.
- Bare element names in `metals_present` / `rare_earth_elements_present`
  are auto-resolved to verified CHEBI atom CURIEs (26 elements
  covered as of 2026-05); see `_ELEMENT_CHEBI` in
  `src/communitymech/export/kgx_export.py` for the full table.

### Upstream details

The export is implemented as a custom Python emitter (no Koza
dependency for a 78-record / ~580-edge scale). Schema, evidence
slots, and edge selection are documented in:
[`../../culturebotai-claw/docs/proposals/phase3_communitymech_kgx_export_with_publications.md`](../../culturebotai-claw/docs/proposals/phase3_communitymech_kgx_export_with_publications.md).

---

## 🧬 Example Community File

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
        snippet: "F. prausnitzii represents more than 5%..."

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
```

---

## 🔬 Key Features

### 1. Evidence-Based
- Every claim backed by PMID references
- Snippets validated against PubMed abstracts
- Prevents AI hallucination

### 2. Ontology-Grounded
- **NCBITaxon** - Microbial taxa
- **ENVO** - Environments
- **CHEBI** - Chemical entities/metabolites
- **GO** - Biological processes
- **UBERON** - Host anatomy

### 3. Causal Graphs
- Model ecological interactions as directed graphs
- Represent cross-feeding, competition, mutualism
- Visualize with D3.js/Cytoscape

### 4. Dual Output
- **Rich YAML** - For agent consumption (full context)
- **Simple KG** - For graph algorithms (Biolink edges)

### 5. Cross-Repository Linking
- **Environmental linking** to CultureMech media and MediaIngredientMech ingredients
- Environment-based discovery via shared ENVO terms
- `related_media` for environmentally relevant media (complements `growth_media`)
- `related_ingredients` for environmentally significant compounds
- SPARQL query patterns for cross-repo joins

### 6. Scientist-Friendly
- Faceted browser (no coding required)
- Click-through to evidence
- Interactive visualizations

---

## 🛠️ Development Status

**Current Phase**: Foundation (Sprint 1)

- [x] Repository created
- [x] Implementation plan documented
- [x] Reference implementation analyzed (Monarch dismech)
- [x] Seed data added (35 communities)
- [x] Schema design (LinkML schema with full validation)
- [x] First example community YAML
- [x] Cross-repo environmental linking (CultureMech + MediaIngredientMech)
- [ ] Validation stack setup
- [ ] Koza transform implementation
- [ ] Faceted browser adaptation
- [ ] HTML rendering

See [COMMUNITY_MECH_PLAN.md](COMMUNITY_MECH_PLAN.md) for the complete roadmap.

---

## 🤝 Contributing

This is a private repository during initial development. Once the core infrastructure is in place, we'll open it up for community contributions.

### Development Workflow

1. Create a new branch for your feature/community
2. Add/modify community YAML files
3. Run validation: `just qc`
4. Commit with evidence validation
5. Create PR for review

---

## 📊 Validation Stack

```bash
# Schema validation
just validate kb/communities/YourCommunity.yaml

# Reference validation (anti-hallucination)
just validate-references kb/communities/YourCommunity.yaml

# Term validation (ontology checking)
just validate-terms-file kb/communities/YourCommunity.yaml

# Full QC
just qc
```

---

## 🎓 Citation

(TBD once published)

Based on the dismech framework:
- Monarch Initiative. (2024). dismech: Disorder Mechanisms Knowledge Base. https://github.com/monarch-initiative/dismech

---

## 📝 License

BSD-3-Clause (matching the dismech framework)

---

## 🔗 Related Projects

- [dismech](https://github.com/monarch-initiative/dismech) - Disease mechanisms KB (inspiration)
- [LinkML](https://linkml.io/) - Modeling framework
- [Koza](https://github.com/monarch-initiative/koza) - KG transformation tool
- [BugSigDB](https://bugsigdb.org/) - Microbial signatures database
- [OAK](https://github.com/INCATools/ontology-access-kit) - Ontology access toolkit

---

## 📧 Contact

For questions or collaboration inquiries, please open an issue.

---

**Status**: 🚧 Under active development
