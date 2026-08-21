# CLAUDE.md

Operational guidance for Claude Code and other coding agents working in this
repository.

## Project model

CommunityMech is a LinkML knowledge base for microbial community composition,
ecological interactions, cultivation, environments, and evidence. Curated YAML
is the canonical record format. Validators, Python models, HTML, and KGX files
are derived products.

The repository currently runs as a source checkout. `communitymech.paths`
anchors the KB, reference cache, reports, and generated site to the checkout.
Do not assume an installed wheel has those repository data paths; the long-term
packaging decision is tracked in issue #668.

Before changing anything:

- Read any applicable `AGENTS.md` plus this file.
- Inspect `git status` and preserve unrelated or uncommitted user work.
- Work in a dedicated branch/worktree for multi-file changes.
- Never read, print, modify, or commit `.env` or credential values.
- Do not make network calls, spend provider credits, or apply generated curation
  unless the task authorizes it.

## Canonical and generated files

| Path | Role | Editing rule |
|---|---|---|
| `src/communitymech/schema/communitymech.yaml` | Main LinkML schema | Edit first for model changes |
| `src/communitymech/schema/mech_shared.yaml` | Shared discussion types | Keep synchronized with its canonical source |
| `src/communitymech/schema/history.yaml` | Vendored history schema | Do not diverge casually from shared tooling |
| `src/communitymech/datamodel/communitymech.py` | Generated Python model | Never hand-edit; run `just gen-python` |
| `kb/communities/` | Canonical community records | Root class `MicrobialCommunity` |
| `data/isolates/` | Additional community records | Root class `MicrobialCommunity` |
| `kb/taxa/` | Reusable taxon/gene records | Root class `CommonTaxon` |
| `references_cache/` | Committed evidence source text | Preserve source/provenance boundaries |
| `history/` | Append-only curation provenance | Never revise old history entries |
| `src/communitymech/templates/` | HTML templates | Regenerate committed HTML after edits |
| `docs/` | Published GitHub Pages tree and guides | Do not hand-edit generated community pages |
| `scripts/` | Repository curation utilities | Not part of the public package API |

The generated datamodel and published HTML are tracked. `just clean` must never
delete them.

## Environment

- Core package and validation: Python 3.10+.
- Deep research and Edison: Python 3.12+.
- Package/environment manager: `uv`; do not add `requirements.txt`.
- Task runner: `just`.
- Style: Black and Ruff, line length 100.
- Static typing: mypy over `src/`.

Install development dependencies with:

```bash
just install
```

Several optional repository commands use modules from a sibling
`culturebotai-claw` checkout. They resolve `CLAW_SRC`, defaulting to
`../../culturebotai-claw/src`, and fail loudly when it is absent. These include
`just gen-qc-dashboard`, `just knowledge-gap-scan`,
`just gen-discussions-data`, and `just new-history`.

## Schema and ontology invariants

- Change `src/communitymech/schema/communitymech.yaml`, then run
  `just gen-python`. Never patch the generated datamodel directly.
- Taxa use NCBITaxon; environments use ENVO; chemicals/metabolites use CHEBI;
  biological processes use GO; anatomy uses UBERON; cells use CL; experimental
  concepts may use OBI.
- Ontology values use `{id, label}` pairs. The `label` is the canonical ontology
  label; curator wording belongs in `preferred_term` or notes.
- A pairwise ecological interaction normally names source and target taxa from
  the record taxonomy. Community-level interactions use `scope` and optionally
  `participating_taxa`.
- `kb/taxa` has a different root class and therefore needs the dedicated taxon
  validation recipes.

## Evidence policy

Every curated claim should have evidence at the assertion it supports. This is
a curation policy, not a blanket schema guarantee: taxonomy, interaction, and
environment evidence lists are optional in LinkML. Schema validity alone does
not prove evidence completeness.

An `EvidenceItem` requires:

- a stable `PMID:`, `doi:`, or supported dataset reference;
- `supports`;
- `evidence_source`;
- an exact supporting `snippet`.

Reference validation can match against committed abstracts, cached open-access
full text, and separately cached supplementary text. Do not paraphrase a
snippet, combine non-contiguous text, remove meaningful bracketed text, or move
supplement text into the article cache. If support is absent, omit the claim or
record uncertainty instead of weakening the validator.

`just qc-references` is separate from `just qc`: it can use the network and the
corpus has a known evidence-repair backlog. It is not a CI gate.

## Editing a community or taxon record

1. Read the target, schema, and strong neighboring records.
2. Check whether the same taxon should reference a reusable record in `kb/taxa`.
3. Make the smallest source-supported change; preserve experimental context and
   do not generalize strain-pair evidence to a natural community.
4. Verify CURIEs and canonical labels from authoritative local/source data.
5. Add evidence at each changed assertion.
6. Create a new append-only history record following `history/README.md`.
   `just new-history` requires the shared claw checkout.
7. Run focused validators, review the diff, then run the proportional wider
   checks.
8. If a community record or renderer changed, regenerate/check `docs/`.

Never change the schema, validator, exception list, threshold, or baseline merely
to make generated prose pass.

## Validation commands

```bash
just test
just lint
just validate FILE
just validate-strict FILE
just validate-gtdb FILE
just validate-gtdb-domain FILE
just validate-terms FILE
just validate-references-explained FILE
just validate-history PATH
```

Corpus-level validation:

```bash
just validate-all
just validate-taxa
just validate-terms-all
just validate-terms-taxa
just qc
just qc-references
```

Use a focused test during development:

```bash
uv run pytest tests/test_datamodel.py::test_name -v
```

`just qc` runs lint, pytest, schema validation, closed-schema/cross-field checks,
GTDB checks, scalar checks, and ontology-term checks. Evidence/reference checking
is deliberately outside it.

## Generated outputs

```bash
just gen-python
just gen-html
just check-docs-current
just gen-browser
just kgx-export
just kgx-validate
```

- `just gen-html` renders the committed `docs/` site.
- `just check-docs-current` is the drift gate after community or template edits.
- `just gen-umap` needs a large local embedding artifact that is absent in CI.
- `just kgx-export` uses the custom Python emitter under
  `src/communitymech/export/`; it is not a Koza transform.

## Deep research

Provider ranking is read-only and does not call a provider:

```bash
just deep-research-providers
just deep-research-provider claude_code ecological_mechanism
```

Commands that invoke `deep-research-client` or Edison require Python 3.12+, an
available provider, and appropriate authorization. They can incur cost. Use a
dry run before an authorized call:

```bash
just research-community claude_code CommunityMech:000164 --dry-run
```

Raw reports under `research/` are not schema-compliant deliverables. Verify each
accepted taxon, strain, metabolite, condition, causal direction, accession,
citation, and snippet before curating it into YAML. Record LLM assistance in the
new history entry.

## Code changes

- Keep reusable runtime code under `src/communitymech/`; keep one-off curation
  workflows under `scripts/`.
- Add regression tests for the failure being fixed, including command/CI wiring
  when relevant.
- The console entry point is implemented in `src/communitymech/cli.py` and
  currently exposes network audit/repair and UMAP generation commands.
- Preserve vendored byte-identical files and their synchronization guards.
- Finish with focused tests, `just lint`, `git diff --check`, and the widest
  validation justified by the change.
