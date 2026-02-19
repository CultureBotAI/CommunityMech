# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CommunityMech is a LinkML-based knowledge base for modeling microbial community structure, function, and ecological interactions. Community data lives as curated YAML files in `kb/communities/` (60 files), each validated against a LinkML schema. Every claim is evidence-backed with PMID/DOI references and snippet validation against abstracts.

Adapted from Monarch Initiative's dismech: YAML is the source of truth, with lossy Koza transforms planned for KG export.

## Commands

```bash
just install              # Install deps (uv sync --group dev)
just test                 # Run pytest
just validate FILE        # Validate one YAML against schema
just validate-all         # Validate all community YAMLs
just validate-references FILE  # Check evidence references (PubMed snippets)
just qc                   # Full QC: validate-all + lint + test
just gen-python           # Regenerate datamodel from schema
just format               # black + ruff --fix
just lint                 # black --check + ruff + mypy
```

Single test: `uv run pytest tests/test_datamodel.py::test_name -v`

## Architecture

```
src/communitymech/
├── schema/communitymech.yaml    # LinkML schema (source of truth for datamodel)
├── datamodel/communitymech.py   # AUTO-GENERATED from schema (just gen-python)
├── literature.py                # PubMed/CrossRef/Unpaywall fetcher + snippet validation
├── validators/
│   └── reference_validator.py   # Validates evidence items in YAML files
└── cli.py                       # Entry point (not yet implemented)

kb/communities/                  # 60 curated community YAML files
conf/oak_config.yaml             # OAK ontology adapter config (NCBITaxon, ENVO, CHEBI, GO)
references_cache/                # Cached PubMed abstracts (committed for reproducibility)
scripts/                         # Utility scripts for curation (not part of package)
```

## Key Patterns

- **Schema-first**: Edit `schema/communitymech.yaml`, then `just gen-python` to regenerate the datamodel. Never hand-edit `datamodel/communitymech.py`.
- **Ontology-grounded terms**: All taxa use NCBITaxon, environments use ENVO, metabolites use CHEBI, processes use GO. Terms are `{id, label}` pairs.
- **Evidence on everything**: `EvidenceItem` requires a `reference` (PMID/DOI), `supports` enum, `evidence_source` enum, and a `snippet` that must fuzzy-match the cited abstract.
- **Community YAML structure**: Root class is `MicrobialCommunity` with `taxonomy` (list of `TaxonomicComposition`), `ecological_interactions`, and `environmental_factors`.
- **Validation layers**: Schema validation (linkml-validate), reference validation (snippet matching), and term validation (OAK).

## Ontology Prefixes

NCBITaxon (taxonomy), ENVO (environments), CHEBI (chemicals/metabolites), GO (biological processes), UBERON (anatomy), CL (cell types). References use PMID and doi prefixes.

## Style

- Line length: 100 (black + ruff)
- Python 3.9+ target
- Uses `uv` for package management (never requirements.txt)
