# CommunityMech Justfile
# Task runner for common development commands

# List all commands
default:
    @just --list

# Install dependencies
install:
    uv sync --group dev

# Validate a single community YAML file against schema
validate FILE:
    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml {{FILE}}

# Validate all community files
validate-all:
    #!/usr/bin/env bash
    for file in kb/communities/*.yaml; do
        echo "Validating $file..."
        uv run linkml-validate -s src/communitymech/schema/communitymech.yaml "$file"
    done

# Validate evidence references in a community file
validate-references FILE:
    uv run linkml-reference-validator validate data {{FILE}} -s src/communitymech/schema/communitymech.yaml

# Validate references in all community files
validate-references-all:
    #!/usr/bin/env bash
    for file in kb/communities/*.yaml; do
        echo "\\nValidating references in $file..."
        uv run linkml-reference-validator validate data "$file" -s src/communitymech/schema/communitymech.yaml
    done

# Validate ontology terms in a community file
validate-terms FILE:
    uv run linkml-term-validator validate-data {{FILE}} -s src/communitymech/schema/communitymech.yaml --labels

# Validate terms in all community files
validate-terms-all:
    #!/usr/bin/env bash
    for file in kb/communities/*.yaml; do
        echo "\\nValidating terms in $file..."
        uv run linkml-term-validator validate-data "$file" -s src/communitymech/schema/communitymech.yaml --labels
    done

# Validate schema-level ontology term meanings
validate-schema-terms:
    uv run linkml-term-validator validate-schema src/communitymech/schema/communitymech.yaml

# Repair references with suggested fixes (dry-run)
repair-references FILE:
    uv run linkml-reference-validator repair data {{FILE}} -s src/communitymech/schema/communitymech.yaml --dry-run

# Run tests
test:
    uv run pytest tests/ -v

# Generate Python datamodel from schema
gen-python:
    uv run gen-python src/communitymech/schema/communitymech.yaml > src/communitymech/datamodel/communitymech.py

# Generate schema documentation
gen-doc:
    uv run gen-doc src/communitymech/schema/communitymech.yaml -d docs/

# Generate browser data for faceted search
gen-browser:
    uv run python -m communitymech.export.browser_export

# Generate HTML pages for communities
gen-html:
    uv run python -m communitymech.render

# Generate UMAP visualization of community embedding space
gen-umap:
    uv run communitymech generate-umap
    @echo "✅ UMAP visualization generated at docs/community_umap.html"

# Generate all HTML (communities + UMAP)
gen-all: gen-html gen-umap
    @echo "✅ All HTML pages regenerated"

# Clean generated files
clean:
    rm -rf src/communitymech/datamodel/*.py
    rm -rf docs/*.md
    rm -rf .linkml-cache

# Format code
format:
    uv run black src/ tests/
    uv run ruff check --fix src/ tests/

# Run linting
lint:
    uv run black --check src/ tests/
    uv run ruff check src/ tests/
    uv run mypy src/

# Full QC (validate + lint + test)
qc: validate-all validate-terms-all validate-references-all lint test
    @echo "✅ All QC checks passed!"

# Check which community strains are represented in UniProt reference proteomes
uniprot-reference COMMUNITY_PATH="kb/communities":
    uv run python -m communitymech.uniprot_reference_proteomes {{COMMUNITY_PATH}}

# Build proteome-oriented CSV with communities per UniProt proteome/taxon
uniprot-proteome-csv COMMUNITY_PATH="kb/communities" OUT="reports/uniprot_strain_proteome_communities.csv":
    uv run python -m communitymech.uniprot_reference_proteomes {{COMMUNITY_PATH}} --proteome-csv-out {{OUT}}

# Audit network integrity for all communities
audit-network:
    uv run communitymech audit-network

# Check network quality (CI mode - exits with error if issues found)
check-network-quality:
    uv run communitymech audit-network --check-only

# Audit network integrity with JSON output
audit-network-json:
    uv run communitymech audit-network --json

# Audit network integrity and write report to file
audit-network-report FILE="network_integrity_audit.txt":
    uv run communitymech audit-network --report {{FILE}}

# LLM-assisted network repair for a single community (requires ANTHROPIC_API_KEY)
repair-network FILE:
    uv run communitymech repair-network {{FILE}}

# LLM-assisted repair in dry-run mode (show suggestions only)
repair-network-dry FILE:
    uv run communitymech repair-network {{FILE}} --dry-run

# Generate LLM-assisted repair suggestions for all communities
suggest-network-repairs:
    uv run communitymech repair-network-batch --report-only

# Generate repair suggestions with limits
suggest-network-repairs-limited MAX='10':
    uv run communitymech repair-network-batch --report-only --max-communities {{MAX}}

# Apply approved suggestions from batch report
apply-batch-repairs REPORT:
    uv run communitymech repair-network-batch --apply-from {{REPORT}}

# Link growth media to CultureMech/MediaIngredientMech (dry-run)
link-media-dry:
    uv run python scripts/link_growth_media.py --dry-run \
        --culturemech-index ../../CultureMech/data/normalized_yaml/recipe_index.json \
        --mediaingredientmech-index ../../MediaIngredientMech/data/curated/all_ingredients_index.json

# Link growth media to CultureMech/MediaIngredientMech (apply)
link-media:
    uv run python scripts/link_growth_media.py \
        --culturemech-index ../../CultureMech/data/normalized_yaml/recipe_index.json \
        --mediaingredientmech-index ../../MediaIngredientMech/data/curated/all_ingredients_index.json

# Generate ingredient/media mapping reports
link-media-report:
    uv run python scripts/link_growth_media.py --dry-run \
        --culturemech-index ../../CultureMech/data/normalized_yaml/recipe_index.json \
        --mediaingredientmech-index ../../MediaIngredientMech/data/curated/all_ingredients_index.json \
        --ingredient-report reports/ingredient_mapping.csv \
        --media-report reports/media_mapping.csv \
        --summary-report reports/media_linking_summary.txt

# Export the community knowledge graph as KGX TSV (nodes.tsv +
# edges.tsv) with publications and supporting_text propagated from
# evidence claims. Phase 3 of the dismech-pattern port. See
# ../../culturebotai-claw/docs/proposals/phase3_communitymech_kgx_export_with_publications.md
kgx-export:
    PYTHONPATH=src /opt/homebrew/bin/python3.13 -m communitymech.export \
      --kb kb/communities --output output/kgx

# Lightweight structural validation of the KGX TSV outputs.
# No external deps; checks columns, CURIE shape, biolink predicate
# names, duplicate IDs, dangling subjects/objects.
kgx-validate:
    PYTHONPATH=src /opt/homebrew/bin/python3.13 -m communitymech.export.validate_kgx \
      --kgx-dir output/kgx --strict
