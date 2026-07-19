# CommunityMech Justfile
# Task runner for common development commands

set dotenv-load := true

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
    set -uo pipefail
    rc=0
    for file in kb/communities/*.yaml; do
        echo "Validating $file..."
        uv run linkml-validate -s src/communitymech/schema/communitymech.yaml "$file" || rc=1
    done
    exit $rc

# Validate the reusable per-taxon gene records (kb/taxa/) against CommonTaxon.
# These files have CommonTaxon as their root, not MicrobialCommunity, so the
# target class must be given explicitly.
validate-taxa:
    #!/usr/bin/env bash
    set -uo pipefail
    rc=0
    for file in kb/taxa/*.yaml; do
        echo "Validating $file..."
        uv run linkml-validate -s src/communitymech/schema/communitymech.yaml \
            --target-class CommonTaxon "$file" || rc=1
    done
    exit $rc

# id↔label gate for kb/taxa/ CommonTaxon records (enforces the GeneAnnotation.go_terms
# binding: go_terms[].label must be the canonical GO label). Needs --target-class
# CommonTaxon since these files are not MicrobialCommunity (the schema tree_root).
validate-terms-taxa:
    #!/usr/bin/env bash
    set -uo pipefail
    rc=0
    for file in kb/taxa/*.yaml; do
        echo "Validating terms in $file..."
        uv run linkml-term-validator validate-data "$file" \
            -s src/communitymech/schema/communitymech.yaml --labels \
            --target-class CommonTaxon || rc=1
    done
    exit $rc

# Strict in-process validation in *closed* mode (rejects unknown fields).
# Emits reports/instance_validation_failures.tsv and exits 1 on any ERROR.
# Catches the same drift class that gave CultureMech 59k silent errors;
# closed-mode + non-zero exit is what the per-file linkml-validate loop
# above silently passes today. Use this for the corpus-wide health check.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Audit every YAML-writing Python module under scripts/ and
# src/communitymech/ for safeguards (curation_history append,
# --dry-run/--apply, validates before write, wired into justfile).
# Writes reports/pipeline_writers_audit.tsv. Useful for tracking
# adoption of write_validated_community + record_curation_event.
audit-writers *args:
    uv run python scripts/audit_writers.py {{args}}

# Validate evidence references in a community file
validate-references FILE:
    uv run linkml-reference-validator validate data {{FILE}} -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml

# Validate references in all community files
validate-references-all:
    #!/usr/bin/env bash
    set -uo pipefail
    rc=0
    for file in kb/communities/*.yaml; do
        echo "\\nValidating references in $file..."
        uv run linkml-reference-validator validate data "$file" -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml || rc=1
    done
    exit $rc

# Validate cross-repo IDs (CultureMech, MediaIngredientMech) in one community file.
# Pattern checks always run; existence checks run when sibling-repo paths are
# configured via COMMUNITYMECH_SIBLING_REPOS env (Name=path,Name=path).
validate-cross-repo-ids FILE:
    PYTHONPATH=src uv run python scripts/validate_cross_repo_ids.py {{FILE}}

# Validate cross-repo IDs across all community files.
validate-cross-repo-ids-all:
    PYTHONPATH=src uv run python scripts/validate_cross_repo_ids.py kb/communities/*.yaml

# Environmental coverage dashboard: per-ENVO counts of communities vs CultureMech
# media vs MediaIngredientMech ingredients (issue #30). Reads sibling repos from
# COMMUNITYMECH_SIBLING_REPOS env (Name=path,Name=path); pass --tsv to also write
# a report. Without siblings configured it lists community ENVO terms only.
env-coverage *args:
    PYTHONPATH=src uv run python scripts/env_coverage_dashboard.py {{args}}

# Validate ontology terms in a community file
validate-terms FILE:
    uv run linkml-term-validator validate-data {{FILE}} -s src/communitymech/schema/communitymech.yaml --labels

# Validate terms in all community files. Now that the schema binds the
# descriptor `term` slots, --labels verifies term.label is the CANONICAL
# ontology label for term.id. Fails (non-zero) if any file has label drift.
validate-terms-all:
    #!/usr/bin/env bash
    set -uo pipefail
    rc=0
    for file in kb/communities/*.yaml; do
        echo "Validating terms in $file..."
        uv run linkml-term-validator validate-data "$file" -s src/communitymech/schema/communitymech.yaml --labels || rc=1
    done
    exit $rc

# id↔label gate (Engine B): verify (id,label) pairs in DATA PRODUCTS
# (KGX node export) correspond to the ontology. Exits 2 on any mismatch.
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# Baseline (non-failing): unified id↔label drift report across community
# YAMLs + KGX products to reports/label_drift.tsv. Use before enforcing.
report-label-drift:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv

# Vendored id-label files that must stay byte-identical across the CultureMech /
# MIM / CommunityMech Mech repos and must not silently diverge: the validator +
# its two shared tests. conf/id_label_targets.yaml is deliberately per-repo
# (different adapters/targets/exceptions) so it is NOT here.
VENDORED_IDLABEL_FILES := "scripts/validate_id_label_correspondence.py tests/test_id_label_empty_adapter.py tests/test_id_label_unknown_prefix.py"

# Durability guard: fail if any vendored id-label file (the validator + its two
# shared tests) drifts from its pinned sha256 (vendored byte-identical across the
# Mech repos — see the validator's docstring + culturebotai-claw#6). CI runs this
# so an accidental edit to one copy can't silently diverge. Uses sha256sum on CI
# (ubuntu), shasum -a 256 on macOS.
verify-validator-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum -c scripts/.validate_id_label_correspondence.sha256
    else
        shasum -a 256 -c scripts/.validate_id_label_correspondence.sha256
    fi

# Intentional sync only: re-pin the sha256 manifest to the CURRENT contents of the
# vendored files after a deliberate, all-repos byte-identical update. Run this in
# every Mech copy.
refresh-validator-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    : > scripts/.validate_id_label_correspondence.sha256
    for f in {{VENDORED_IDLABEL_FILES}}; do
        if command -v sha256sum >/dev/null 2>&1; then h=$(sha256sum "$f" | cut -d' ' -f1); else h=$(shasum -a 256 "$f" | cut -d' ' -f1); fi
        printf '%s  %s\n' "$h" "$f" >> scripts/.validate_id_label_correspondence.sha256
        echo "re-pinned $f to $h"
    done
    echo "re-pinned $f to $h"

# Durability guard for the shared LinkML module (Discussion + Dataset), vendored
# byte-identical across the Mech repos — see culturebotai-claw#7.
SHARED_SCHEMA_MODULE := "src/communitymech/schema/mech_shared.yaml"
verify-schema-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum -c src/communitymech/schema/.mech_shared.sha256
    else
        shasum -a 256 -c src/communitymech/schema/.mech_shared.sha256
    fi

# Intentional sync only: re-pin after a deliberate, all-repos byte-identical update.
refresh-schema-pin:
    #!/usr/bin/env bash
    set -euo pipefail
    f={{SHARED_SCHEMA_MODULE}}
    if command -v sha256sum >/dev/null 2>&1; then h=$(sha256sum "$f" | cut -d' ' -f1); else h=$(shasum -a 256 "$f" | cut -d' ' -f1); fi
    printf '%s  %s\n' "$h" "$f" > src/communitymech/schema/.mech_shared.sha256
    echo "re-pinned $f to $h"

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
    # Format the generated file so `black --check src/` (just lint) stays green
    # without a manual `just format` after every regen.
    uv run black -q src/communitymech/datamodel/communitymech.py

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

# QC coverage dashboard (shared kg_microbe_qc generator in culturebotai-claw).
# This repo is nested one level deeper, so PYTHONPATH is ../../culturebotai-claw/src.
gen-qc-dashboard:
    PYTHONPATH=../../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_qc --config conf/qc_config.yaml --output dashboard

# Knowledge-gap scan (Europe PMC, free) via shared kg_microbe_kgscan in claw.
# Dry-run by default → reports/knowledge_gap_scan.{json,md}. Pass `--apply`
# (and e.g. --limit/--min-score) to seed Discussion(kind=KNOWLEDGE_GAP).
# Nested repo → PYTHONPATH is ../../culturebotai-claw/src.
knowledge-gap-scan *args:
    PYTHONPATH=../../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_kgscan --config conf/kgscan_config.yaml {{args}}

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

# Full QC (validate + strict validate + lint + test)
qc: validate-all validate-taxa validate-strict validate-terms-all validate-terms-taxa validate-references-all lint test
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

# ============== Deep Research ==============

research_dir := "research"
templates_dir := "templates"

# Deep research on a community using a specified provider.
# Examples:
#   just research-community falcon Yogurt_TwoSpecies_Starter_Culture --dry-run
#   just research-community falcon CommunityMech:000164
research-community provider target *args="":
    uv run --extra dev python scripts/research_community.py \
      --provider {{provider}} \
      --target {{target}} \
      --template {{templates_dir}}/community_mechanism_research.md \
      --research-dir {{research_dir}} \
      {{args}}

# Alias for repo-specific entity research.
research-entity provider target *args="": (research-community provider target args)

# Edison Scientific deep research (PaperQA3) for one community record.
# target = filename stem, CommunityMech id, or YAML path.
# Examples:
#   just research-community-edison Yogurt_TwoSpecies_Starter_Culture --dry-run
#   just research-community-edison CommunityMech:000164 --job literature-high
research-community-edison target *args="":
    uv run --extra dev python scripts/research_community_edison.py \
      --target {{target}} \
      --template {{templates_dir}}/community_mechanism_research.md \
      --out-dir {{research_dir}}/communities \
      {{args}}

# Edison deep research for a batch of communities (JSON list of stems/ids/paths).
research-community-edison-batch batch *args="":
    uv run --extra dev python scripts/research_community_edison.py \
      --batch {{batch}} \
      --template {{templates_dir}}/community_mechanism_research.md \
      --out-dir {{research_dir}}/communities \
      {{args}}

# Retroactively backfill Edison provenance sidecars (no re-billing).
enrich-edison-response *args="":
    uv run --extra dev python scripts/enrich_edison_response.py {{args}}

# Scout recent literature for NEW communities (Europe PMC, free; dedups vs kb/communities).
#   just scout-communities --preset syntrophy --since 2024
#   just scout-communities --query "gut butyrate cross-feeding consortium" --emit-stubs
scout-communities *args="":
    uv run python scripts/scout_communities.py {{args}}

# Ground taxa in GTDB via the local kg-microbe NCBI<->GTDB mapping (no network).
#   just ground-taxa-gtdb --community kb/communities/Foo.yaml --emit-yaml
#   just ground-taxa-gtdb --ncbi-id NCBITaxon:492670 --emit-yaml
ground-taxa-gtdb *args="":
    uv run python scripts/gtdb_ground.py {{args}}

# List available deep-research-client providers.
research-providers:
    #!/usr/bin/env bash
    set -euo pipefail
    if [[ -z "${EDISON_API_KEY:-}" && -n "${FUTUREHOUSE_API_KEY:-}" ]]; then
        EDISON_API_KEY="${FUTUREHOUSE_API_KEY}" uv run --extra dev deep-research-client providers
    else
        uv run --extra dev deep-research-client providers
    fi

# Show detailed availability and parameters for one provider.
research-provider provider:
    #!/usr/bin/env bash
    set -euo pipefail
    if [[ -z "${EDISON_API_KEY:-}" && -n "${FUTUREHOUSE_API_KEY:-}" ]]; then
        EDISON_API_KEY="${FUTUREHOUSE_API_KEY}" uv run --extra dev deep-research-client providers --provider {{provider}}
    else
        uv run --extra dev deep-research-client providers --provider {{provider}}
    fi

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

# Render per-community HTML detail pages from kb/communities/*.yaml
# into pages/community/. Includes a Mermaid membership flowchart via
# the shared kg_microbe_browser.graph builder in claw. See
# ../../culturebotai-claw/docs/proposals/phase5_mkdocs_material_and_browser_parity.md
gen-community-pages *args:
    /opt/homebrew/bin/python3.13 src/communitymech/render_community_pages.py {{args}}

# Discussions / knowledge-gap browser (shared kg_microbe_discussions in claw).
# Nested repo → PYTHONPATH is ../../culturebotai-claw/src.
gen-discussions-data:
    PYTHONPATH=../../culturebotai-claw/src /opt/homebrew/bin/python3.13 \
      -m kg_microbe_discussions --config conf/discussions_config.yaml --output app/discussions
