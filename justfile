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
