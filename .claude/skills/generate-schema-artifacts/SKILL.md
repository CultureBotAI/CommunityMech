---
name: generate-schema-artifacts
description: Regenerate LinkML-derived artifacts after schema changes — Python datamodels, documentation, browser export, HTML pages, and UMAP visualization
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
tags: [linkml, schema, codegen, python, documentation, umap, browser, html, artifacts]
---

# Generate Schema Artifacts Skill

## Overview

CommunityMech uses a LinkML schema (`src/communitymech/schema/communitymech.yaml`) as
the authoritative source of truth. Several derived artifacts must be regenerated whenever
the schema changes:

- **Python dataclasses** — used by all Python scripts for type-safe record handling
- **Documentation** — Markdown/HTML docs auto-generated from schema annotations
- **Browser export** — JSON/TSV for the web browser interface
- **HTML pages** — per-community HTML cards
- **UMAP visualization** — embedding-based community scatter plot

**Run from `CommunityMech/CommunityMech/` directory.**

---

## When to Regenerate

| Trigger | Artifacts needed |
|---------|-----------------|
| Schema field added/removed/renamed | All (`gen-python` first, then others) |
| New community records added | `gen-browser`, `gen-html`, `gen-umap` |
| Embeddings file updated | `gen-umap` only |
| Documentation annotation changed | `gen-doc` only |
| Quarterly maintenance | All |

**Critical**: Always run `gen-python` first after schema changes — all other scripts
import from the generated Python datamodel.

---

## Recipes

```bash
# Regenerate Python dataclasses from LinkML schema (run FIRST after schema changes)
just gen-python

# Regenerate documentation
just gen-doc

# Regenerate browser export (JSON/TSV for web UI)
just gen-browser

# Regenerate HTML community pages
just gen-html

# Regenerate UMAP visualization (requires KG-Microbe embeddings)
just gen-umap

# Full regen of all artifacts (run after schema changes)
just gen-python && just gen-doc && just gen-browser && just gen-html && just gen-umap
```

---

## Output Locations

| Recipe | Output |
|--------|--------|
| `gen-python` | `src/communitymech/datamodel/communitymech.py` |
| `gen-doc` | `docs/` directory |
| `gen-browser` | `app/` or `browser/` directory |
| `gen-html` | `docs/communities/` HTML pages |
| `gen-umap` | `app/umap.html` (embedding visualization) |

---

## UMAP Visualization

The `gen-umap` recipe uses the same KG-Microbe DeepWalk embeddings as CultureMech:

```
DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_2026-02-01_05_54_01.tsv.gz
```

Each community is represented by aggregated embeddings of its member taxa and
associated media. Points are colored by community type (soil, gut, aquatic, etc.).

---

## Schema Location

```
src/communitymech/schema/communitymech.yaml   — primary schema
src/communitymech/schema/                     — schema directory
```

The schema defines all field names, types, ranges, required status, and
pattern constraints (e.g. `CommunityMech:NNNNNN` ID format).

---

## Dependency: `gen-python` Must Run First

After any schema change, Python scripts that import the datamodel will fail
until `gen-python` is run. If you see `ImportError` for `communitymech.datamodel`,
regenerate the Python artifacts:

```bash
just gen-python
```

---

## Validation After Regen

After regenerating artifacts, run validation to catch issues:

```bash
# Validate all community records against schema
communitymech audit-network

# Or use review-communities skill for full QA
```

---

## Related Skills

- `review-communities` — validates records against the schema (use after `gen-python`)
- `manage-identifiers` — ID assignment; IDs must match schema pattern
- `evidence-curation` — evidence fields defined in schema
