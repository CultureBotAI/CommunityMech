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

# Append open-access full text (Europe PMC) to a PMID's reference cache, so
# `validate-references` can verify snippets taken from a paper's Methods/Results,
# not just its abstract. Only OA papers are cached; idempotent. e.g.:
#   just cache-fulltext PMID:36847519
cache-fulltext *pmids:
    PYTHONPATH=src uv run python scripts/cache_fulltext.py {{pmids}}

# Validate evidence references in a community file.
#
# NB on the output (issue #257): the tool's "Total checks: N" line counts
# ISSUES, not checks performed — a clean file prints "Total checks: 0", which
# reads like "nothing was validated". It IS validating (a fabricated snippet
# fails it); only the label is wrong, and it lives in the pip package.
#
# Its matching is strict-substring, so it also reports faithful quotes whose
# CACHE carries a PDF/XML extraction artefact (record "10% CO 2" vs cached
# "10% CO2", "beta-5" vs "β-5"). `scripts/evidence_snippet_audit.py` counts that
# class separately as RENDERING; validator errors == RENDERING + MISMATCH there.
# Do not "fix" a RENDERING hit by editing the snippet to match the cache.
validate-references FILE:
    uv run linkml-reference-validator validate data {{FILE}} -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml

# Snippet audit across ALL records (the tool that actually reconciles with
# validate-references). Buckets: MATCH / RENDERING / WEAK / MISMATCH / NOCONTENT.
audit-snippets *args:
    uv run python scripts/evidence_snippet_audit.py {{args}}

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

# Suggest environment-matched CultureMech media as related_media blocks for
# review (issue #30, Use Case 1). Needs a CultureMech path via
# COMMUNITYMECH_SIBLING_REPOS or --culturemech. Suggestion-only; edits nothing.
# Add --subsumption to also match ENVO subtype environments.
suggest-related-media *args:
    PYTHONPATH=src uv run python scripts/suggest_related_media.py {{args}}

# Suggest environment-matched MIM ingredients as related_ingredients blocks (CHEBI
# route via SSSOM skos:exactMatch, per MediaIngredientMech#119). Needs a MIM repo
# path via COMMUNITYMECH_SIBLING_REPOS or --mediaingredientmech. Suggestion-only.
suggest-related-ingredients *args:
    PYTHONPATH=src uv run python scripts/suggest_related_ingredients.py {{args}}

# Environment-grounding quality report: rank community environment_term usage and
# flag generic (e.g. laboratory environment) / over-applied groundings for review
# (issue #30 follow-up). Report-only; edits nothing. --list shows affected records.
env-grounding-quality *args:
    PYTHONPATH=src uv run python scripts/env_grounding_quality.py {{args}}

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

# NOTE: the id↔label validator + its shared tests are vendored byte-identical
# across the Mech repos. The old self-generated sha256 pin (verify-/refresh-
# validator-pin) was retired — it only compared a copy to a hash from the SAME
# repo, so all repos could pass while diverged. Drift is now caught by the
# shared-reference check: the `vendored-sync` CI job runs
# scripts/check_vendored_sync.sh, which diffs these files against
# CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>. To propagate a change:
# PR into that hub → merge → bump .vendored_canon_ref here.

# NOTE: the shared LinkML module (mech_shared.yaml) is vendored byte-identical
# across the Mech repos (package-namespaced path per repo). Its self-generated
# sha256 pin (verify-/refresh-schema-pin) was retired — same self-referential
# flaw as the id-label pin. It is now covered by the shared-reference drift check
# (scripts/check_vendored_sync.sh diffs src/*/schema/mech_shared.yaml against the
# hub's copy at CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>) plus the
# hub's nightly vendored-fleet-audit.yml.

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
# Portable so CI can run it: `python3` from PATH rather than a Homebrew path, and
# CLAW_SRC to relocate the claw checkout (CI checks claw out as a sibling). The
# guard is deliberately fail-loud — a skip-when-missing variant of this pattern is
# what let a vendored-sync job pass while checking nothing (CultureMech#112 lane).
knowledge-gap-scan *args:
    #!/usr/bin/env bash
    set -euo pipefail
    claw_src="${CLAW_SRC:-../../culturebotai-claw/src}"
    if [ ! -d "$claw_src/kg_microbe_kgscan" ]; then
      echo "knowledge-gap-scan: kg_microbe_kgscan not found under '$claw_src'." >&2
      echo "Set CLAW_SRC to the src/ directory of a culturebotai-claw checkout." >&2
      exit 1
    fi
    PYTHONPATH="$claw_src" python3 -m kg_microbe_kgscan \
      --config conf/kgscan_config.yaml {{args}}

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

# Edison deep research in CAUSAL-GRAPH mode for ONE community: extracts
# source-backed interaction nodes + directed causal edges (ecological_interactions
# + InteractionDownstream). Same Edison plumbing as research-community-edison, with
# the causal template + a `causal` label so it does NOT overwrite the mechanism run.
#   just research-community-causal Cellulose_Methane_Quad_Culture_SynCom --dry-run
research-community-causal target *args="":
    uv run --extra dev python scripts/research_community_edison.py \
      --target {{target}} \
      --template {{templates_dir}}/community_causal_graph_research.md \
      --label causal \
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
