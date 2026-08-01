---
name: id-label-correspondence
description: Validate that every ontology ID carries its correct ontology LABEL across CommunityMech community YAMLs and KGX node exports. Uses LinkML schema bindings + linkml-term-validator for term.{id,label} (canonical label) and a shared OAK validator for products. Run report-then-enforce; triage drift as wrong-label vs wrong-id.
category: validation
requires_database: false
requires_internet: true
version: 1.0.0
---

# ID↔Label correspondence (CommunityMech)

## The invariant

Every ontology **ID** must carry its **correct ontology label**, everywhere —
community YAML inputs and the KGX product export. Checking that an ID *exists*
is not enough; the **label must be the right label for that ID**. A wrong label
often signals a **wrong ID** (the more serious bug).

Policy (**Hybrid**):
- **`Term.label`** (under every `term:` block: `taxon_term`, `metabolites`,
  `biological_processes`, `environment_term`, `chebi_term`,
  `shared_environment_term`) must equal the **canonical** ontology label (e.g.
  `ENVO:00002046` → `activated sludge`). The free/project name lives in the
  sibling `preferred_term`, **not** in `term.label`.
- **KGX `name` column** accepts the canonical label OR an exact/related synonym.

See `docs/ID_LABEL_CORRESPONDENCE.md` for the cross-repo rationale.

## How it's enforced

**Engine A — LinkML-native (YAML).** The schema marks `Term.label`
`slot_uri: rdfs:label` and gives every descriptor `term` slot a range-less
`binding` (`binds_value_of: id`). `linkml-term-validator validate-data --labels`
then verifies `term.label` against OAK's canonical label and **fails** on drift.

```bash
just validate-terms kb/communities/<file>.yaml   # one file
just validate-terms-all                          # all communities
```

**Engine B — shared OAK validator (products).**
`scripts/validate_id_label_correspondence.py` (vendored byte-identical across
the Mech repos) checks `output/kgx/nodes.tsv` (`id`/`name`) per
`conf/id_label_targets.yaml`.

```bash
just validate-products       # enforce (exit 2 on mismatch / unknown id)
just report-label-drift      # baseline: reports/label_drift.tsv, never fails
```

## Rollout: report → baseline → enforce

The gates are **not** in `qc` blocking yet — enforcing surfaces existing drift
(e.g. `ENVO:00002046` labeled "sludge" vs canonical "activated sludge";
obsolete `GO:0055114`). CI workflow `label-correspondence.yaml` runs
`report-label-drift` **non-blocking** and uploads the report.

1. `just report-label-drift` → open `reports/label_drift.tsv`.
2. **Triage** each row (below).
3. Once cleared, ensure `validate-terms-all` + `validate-products` run as
   **blocking** in CI / `qc` (Phase 2).

## Triage: wrong label vs wrong ID

- **Stale/wrong label, right ID** → set `term.label` to the canonical ontology
  label; keep the human name in `preferred_term`.
- **Wrong ID** → the label names a *different* term; fix the **ID**. Use
  `scripts/validate_ncbitaxon_ids.py` (suggests the correct NCBITaxon ID from
  the name) and `scripts/term_fix_apply.py`.
- **`ID_NOT_FOUND` / obsolete** → re-map to the current term.

## Surfaces (`conf/id_label_targets.yaml`)

- `kb/communities/*.yaml` (`term.{id,label}`) — canonical
- `output/kgx/nodes.tsv` (`id`/`name`) — canonical-or-synonym

Prefixes without an OAK adapter (`CommunityMech:`, `CultureMech:`,
`MediaIngredientMech:`) are reported `SKIPPED_NO_ADAPTER`.

## Related

- `scripts/validate_ncbitaxon_ids.py` (per-name NCBITaxon label check + ID
  suggestions), `scripts/term_fix_apply.py`, `conf/oak_config.yaml`.
