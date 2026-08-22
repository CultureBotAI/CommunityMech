# CommunityMech

CommunityMech is a LinkML knowledge base for microbial community composition,
ecological interactions, cultivation conditions, environments, and supporting
evidence. Curated YAML is the canonical record format; validation, static HTML,
and KGX exports are derived from it.

The project is adapted from the
[Monarch Initiative dismech project](https://github.com/monarch-initiative/dismech).

## What is in this repository

- `kb/communities/` — canonical `MicrobialCommunity` records.
- `data/isolates/` — additional `MicrobialCommunity` records kept separate from
  the main community collection.
- `kb/taxa/` — reusable `CommonTaxon` genome and gene records.
- `src/communitymech/schema/` — LinkML schemas.
- `src/communitymech/datamodel/communitymech.py` — generated Python datamodel;
  never edit it by hand.
- `src/communitymech/validators/` — cross-field checks LinkML cannot express.
- `references_cache/` — committed source text used for reproducible evidence
  checks.
- `history/` — append-only curation provenance.
- `docs/` — the committed GitHub Pages site and maintainer guides.
- `scripts/` — repository-oriented curation and validation utilities.

CommunityMech currently operates from a source checkout. Some commands resolve
the KB, caches, reports, and generated site relative to the repository root. The
long-term installed-package contract is being decided in
[#668](https://github.com/CultureBotAI/CommunityMech/issues/668).

## Architecture

```text
community YAML + taxon YAML
            |
            +--> LinkML schema validation
            +--> strict cross-field validators
            +--> ontology id/label validation
            +--> cached/network evidence validation
            |
            +--> deterministic custom Python KGX emitter
            +--> static browser and per-community HTML
```

The KGX path is a custom Python emitter, not a Koza transform. YAML retains the
full curation context and remains the source of truth.

## Requirements and installation

Core development supports Python 3.10 and newer. Deep-research and Edison
commands require Python 3.12 or newer because their optional dependencies do.

Install [uv](https://docs.astral.sh/uv/) and
[just](https://github.com/casey/just), then run:

```bash
git clone https://github.com/CultureBotAI/CommunityMech.git
cd CommunityMech
just install
just test
```

`just install` installs the `dev` extra from `pyproject.toml`. CI uses the frozen
`uv.lock`; commit `pyproject.toml` and `uv.lock` together when dependencies
change.

## Validate records

For one community record:

```bash
FILE=kb/communities/Yogurt_TwoSpecies_Starter_Culture.yaml
just validate "$FILE"
just validate-strict "$FILE"
just validate-gtdb "$FILE"
just validate-gtdb-domain "$FILE"
just validate-terms "$FILE"
```

Evidence validation is separate because it may use the committed cache and the
network:

```bash
just validate-references-explained "$FILE"
```

Repository-wide checks:

```bash
just qc                 # lint, tests, schema, strict, GTDB, scalar, and term gates
just qc-references      # qc plus the corpus-wide literature sweep
```

The corpus-wide reference sweep has a known evidence-repair backlog and is not a
CI gate. A red reference result is not permission to weaken the validator; fix
the evidence or record the unresolved curation work.

Validation layers serve different purposes:

| Layer | Command | What it checks |
|---|---|---|
| LinkML | `just validate FILE` | Schema shape, required fields, enums, patterns |
| Strict | `just validate-strict FILE` | Closed-schema and cross-field invariants |
| Taxonomy | `just validate-gtdb FILE` | GTDB grounding coherence |
| Domain | `just validate-gtdb-domain FILE` | Prokaryotic NCBI-domain expectations |
| Terms | `just validate-terms FILE` | Ontology identifier/label correspondence |
| Evidence | `just validate-references-explained FILE` | Snippets against cached or fetched source text |
| History | `just validate-history PATH` | Append-only history record shape |

## Curation workflow

1. Read the schema and a strong neighboring record before editing.
2. Make the smallest source-supported YAML change.
3. Use canonical ontology identifiers and labels; never invent CURIEs.
4. Add `EvidenceItem` entries at the assertions they support.
5. Add an append-only history record as described in
   [history/README.md](history/README.md).
6. Run focused validation, then `just qc` when the change is ready.
7. Regenerate committed HTML when a community record or renderer changes.

Evidence is a curation policy as well as a data structure. The schema permits
some assertions without an `evidence` list, so schema validity alone does not
prove that every claim has support. Curators should leave unsupported claims
absent or explicitly uncertain rather than infer them from co-occurrence.

## Generate outputs

```bash
just gen-html             # render docs/ from community YAML and templates
just check-docs-current   # fail if committed docs disagree with the KB
just gen-browser          # regenerate faceted-browser data
just kgx-export           # write output/kgx/{nodes.tsv,edges.tsv,manifest.json}
just kgx-validate         # validate the generated KGX files
```

`just gen-umap` additionally requires the local embedding artifact documented in
the [UMAP guide](docs/UMAP_VISUALIZATION.md). `just gen-all` combines HTML and
UMAP generation.

GitHub Pages serves the committed `docs/` tree. Do not hand-edit generated
community pages; update their YAML or templates and regenerate them.

## KGX downstream contract

Release builds publish `nodes.tsv.gz`, `edges.tsv.gz`, and `manifest.json`.
Local output is written under `output/kgx/`.

`nodes.tsv` columns:

```text
id, category, name, description, provided_by
```

`edges.tsv` columns:

```text
id, subject, predicate, object, category, publications, supporting_text,
knowledge_level, agent_type, primary_knowledge_source
```

Edge identifiers are deterministic UUID5 values derived from the edge tuple.
Evidence-bearing edges propagate publication CURIEs and supporting snippets.
See the implementation in
[`src/communitymech/export/kgx_export.py`](src/communitymech/export/kgx_export.py)
and the release workflow in
[`kgx-release.yaml`](.github/workflows/kgx-release.yaml).

## Deep research

Provider triage does not run a provider or spend credits:

```bash
just deep-research-providers
just deep-research-providers datasets_environment
just deep-research-provider claude_code ecological_mechanism
```

An actual research run requires Python 3.12+, provider authentication, and may
incur cost:

```bash
just research-community claude_code CommunityMech:000164 --dry-run
```

Research reports under `research/` are raw artifacts, not canonical data.
Accepted findings must be curated into community YAML with exact source support,
ontology grounding, validation, and history. Never read, print, or commit `.env`
credentials.

## Schema-valid example

This minimal record is derived from the curated yogurt community. A regression
test extracts this fenced block and validates it against the current LinkML
schema.

```yaml
id: CommunityMech:000164
name: Yogurt Two-Species Starter Culture
ecological_state: ENGINEERED
community_origin: SYNTHETIC
environment_term:
  preferred_term: laboratory yogurt fermentation culture
  term:
    id: ENVO:01001405
    label: laboratory environment
taxonomy:
  - taxon_term:
      preferred_term: Streptococcus thermophilus
      term:
        id: NCBITaxon:1308
        label: Streptococcus thermophilus
    functional_role: [CROSS_FEEDER]
    evidence:
      - reference: PMID:30594386
        supports: SUPPORT
        evidence_source: IN_VITRO
        snippet: Streptococcus thermophilus and Lactobacillus delbrueckii ssp. bulgaricus
  - taxon_term:
      preferred_term: Lactobacillus delbrueckii subsp. bulgaricus
      term:
        id: NCBITaxon:1585
        label: Lactobacillus delbrueckii subsp. bulgaricus
    functional_role: [CROSS_FEEDER]
    evidence:
      - reference: PMID:30594386
        supports: SUPPORT
        evidence_source: IN_VITRO
        snippet: Lactobacillus delbrueckii ssp. bulgaricus
ecological_interactions:
  - name: Streptococcus Formate Support
    interaction_type: CROSS_FEEDING
    source_taxon:
      preferred_term: Streptococcus thermophilus
      term:
        id: NCBITaxon:1308
        label: Streptococcus thermophilus
    target_taxon:
      preferred_term: Lactobacillus delbrueckii subsp. bulgaricus
      term:
        id: NCBITaxon:1585
        label: Lactobacillus delbrueckii subsp. bulgaricus
    metabolites:
      - preferred_term: formate
        term:
          id: CHEBI:15740
          label: formate
    evidence:
      - reference: PMID:20889781
        supports: SUPPORT
        evidence_source: IN_VITRO
        snippet: S. thermophilus is suggested to provide L. bulgaricus with formic acid
```

## Documentation

- [Quick-start guide](docs/QUICK_START.md)
- [Automation tools](docs/AUTOMATION_TOOLS.md)
- [Network quality guide](docs/NETWORK_QUALITY_GUIDE.md)
- [Cross-repository linking](docs/cross_repo_linking.md)
- [Growth-media linking](docs/media_linking.md)
- [Curation history](history/README.md)
- [Historical implementation notes](notes/README.md)

## Contributing

Keep changes focused and preserve unrelated work in dirty checkouts. Do not
hand-edit generated models or generated community pages. Pull requests should
include the relevant validation results and any required regenerated artifacts.

CommunityMech is licensed under the [BSD 3-Clause License](LICENSE).
