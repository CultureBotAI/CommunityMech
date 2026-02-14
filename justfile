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

# Run tests
test:
    uv run pytest tests/ -v

# Generate Python datamodel from schema
gen-python:
    uv run gen-python src/communitymech/schema/communitymech.yaml > src/communitymech/datamodel/communitymech.py

# Generate schema documentation
gen-doc:
    uv run gen-doc src/communitymech/schema/communitymech.yaml -d docs/

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
qc: validate-all lint test
    @echo "✅ All QC checks passed!"
