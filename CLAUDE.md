# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CommunityMech is a LinkML-based knowledge base for modeling microbial community structure, function, and ecological interactions. Community data lives as curated YAML files in `kb/communities/` (312 files), each validated against a LinkML schema. Every claim is evidence-backed with PMID/DOI references and snippet validation against abstracts.

Adapted from Monarch Initiative's dismech: YAML is the source of truth, with lossy Koza transforms planned for KG export.

## Commands

```bash
just install              # Install deps (uv sync --extra dev)
just test                 # Run pytest
just validate FILE        # Validate one YAML against schema
just validate-all         # Validate all community YAMLs
just validate-references FILE  # Check evidence references (PubMed snippets)
just qc                   # Full QC: lint + test + every offline validator
just qc-references        # qc + the literature sweep (network; fails on main, #417)
just gen-python           # Regenerate datamodel from schema
just format               # black + ruff --fix
just lint                 # black --check + ruff + mypy
```

`validate-references` is not a CI gate and does not pass on `main` — most cited
DOIs resolve to no fetchable content (#259) and some snippets paraphrase rather
than quote (#347). It is out of `qc` on purpose: `just` stops at the first
failing dependency, so having it there meant `lint` and `test` never ran (#417).

Single test: `uv run pytest tests/test_datamodel.py::test_name -v`

## Architecture

```
src/communitymech/
├── schema/communitymech.yaml    # LinkML schema (source of truth for datamodel)
├── datamodel/communitymech.py   # AUTO-GENERATED from schema (just gen-python)
├── literature.py                # PubMed/CrossRef/Unpaywall fetcher + snippet validation
├── validators/                  # cross-field checks the LinkML schema cannot express.
│                                #   scripts/validate_strict.py (the CI gate) runs
│                                #   gtdb_coherence, gtdb_lineage_tree, prokaryotic_lineage
│                                #   (which pulls in ncbi_domain), shared_taxon_ids and
│                                #   yaml_scalars. cross_repo_ids is separate:
│                                #   `just validate-cross-repo-ids`. Evidence/reference
│                                #   checking is NOT here — `just validate-references` runs
│                                #   the official linkml-reference-validator against
│                                #   conf/reference_validator.yaml (the custom one was
│                                #   replaced in 4dd299a)
└── cli.py                       # Entry point (not yet implemented)

kb/communities/                  # curated community YAML files (root class MicrobialCommunity)
kb/taxa/                          # reusable per-taxon gene records (root class CommonTaxon);
                                  #   referenced from taxonomy[].common_taxon; `just validate-taxa`
vocab/                            # controlled-vocabulary staging files (e.g. cultivation_terms.yaml):
                                  #   definitions/synonyms/ontology-mapping for METPO proposals;
                                  #   kept in sync with the schema enums by tests/
conf/oak_config.yaml             # OAK ontology adapter config (NCBITaxon, ENVO, CHEBI, GO)
references_cache/                # Cached PubMed abstracts (committed for reproducibility)
scripts/                         # Utility scripts for curation (not part of package)
NEXT_TASKS.md                    # The deferred-work backlog (source of truth)
NEXT_TASKS_LOOP.md               # Which of those suit an autonomous /goal run
                                 #   (and which need a human decision first)
prompts/                         # Reusable agent prompts, pasted whole (e.g. `/goal`);
                                 #   backlog-loop.goal.md drives the issue->PR->review->
                                 #   merge cycle. Kept under the 4000-char /goal limit.
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
- Python 3.10+ target
- Uses `uv` for package management (never requirements.txt)
