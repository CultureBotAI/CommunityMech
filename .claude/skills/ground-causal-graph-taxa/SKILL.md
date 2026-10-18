---
name: ground-causal-graph-taxa
description: "Review CommunityMech records and ground taxonomic descriptors in NCBITaxon, GTDB, and LPSN/ICNP across taxonomy, reusable taxon records (kb/taxa/), and causal graph elements (source_taxon, target_taxon, participating_taxa, and counter_selection.excluded_taxon)."
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
---

# Ground Causal Graph & Record Taxa (NCBITaxon + GTDB + LPSN)

## Overview

CommunityMech represents microbial communities (`kb/communities/*.yaml`), isolate baselines (`data/isolates/*.yaml`), and reusable taxon records (`kb/taxa/*.yaml`) with causal ecological interaction graphs (`ecological_interactions`). Every taxonomic reference in a record — both in the community's `taxonomy` inventory and inside causal graph edges — is typed as a **`TaxonDescriptor`** in `src/communitymech/schema/communitymech.yaml`.

This skill defines the workflow and invariants for reviewing records and grounding every `TaxonDescriptor` across three complementary taxonomic authorities:

1. **NCBITaxon** (`sqlite:obo:ncbitaxon` via OAK) — primary ontology CURIE (`term.id`) and canonical label/synonym (`term.label`).
2. **GTDB** (Genome Taxonomy Database via `scripts/gtdb_ground.py` and `<kg-microbe>/data/raw/NCBI2GTDB.tsv.gz`) — genome-based phylogenetic classification (`gtdb_grounding_status`, `gtdb_classification`, `gtdb_candidates`).
3. **LPSN / ICNP** (List of Prokaryotic names with Standing in Nomenclature / International Code of Nomenclature of Prokaryotes) — nomenclatural standing, type strains, 2021 ICNP phylum renames, and homotypic/heterotypic synonymy documented in `taxon_term.notes` or `gtdb_classification.curation_note`.

---

## All 6 `TaxonDescriptor` Slots in the Schema

`communitymech.taxon_blocks.iter_taxon_descriptors(document)` walks every `TaxonDescriptor` slot defined by `src/communitymech/schema/communitymech.yaml`:

| # | Schema Class & Slot | YAML Path | Role & Grounding Expectations |
|---|---|---|---|
| 1 | `CommonTaxon.taxon_term` | `taxon_term` (`kb/taxa/*.yaml`) | Reusable taxon record root; carries `preferred_term`, `term: {id, label}`, `gtdb_grounding_status`, `gtdb_classification`, and LPSN/ICNP nomenclature & type strain details in `notes`. |
| 2 | `TaxonomicComposition.taxon_term` | `taxonomy[].taxon_term` | Primary community member inventory; carries `preferred_term`, `term: {id, label}`, `gtdb_grounding_status`, and `gtdb_classification` (or `gtdb_candidates` when `AMBIGUOUS`). |
| 3 | `EcologicalInteraction.source_taxon` | `ecological_interactions[].source_taxon` | Directed causal graph edge origin; carries `preferred_term` and `term: {id, label}` synchronized with `taxonomy[].taxon_term`. |
| 4 | `EcologicalInteraction.target_taxon` | `ecological_interactions[].target_taxon` | Directed causal graph edge target; carries `preferred_term` and `term: {id, label}` synchronized with `taxonomy[].taxon_term`. |
| 5 | `EcologicalInteraction.participating_taxa` | `ecological_interactions[].participating_taxa[]` | Multi-partner consortium/guild causal graph participants; each item carries `preferred_term` and `term: {id, label}` synchronized with `taxonomy[].taxon_term`. |
| 6 | `CounterSelection.excluded_taxon` | `engineering_design.counter_selection[].excluded_taxon` | Counter-selected or excluded taxon in an engineered community; carries `preferred_term` and `term: {id, label}`. |

All six locations are inspected by the repository validators:
- `src/communitymech/taxon_blocks.py` (`iter_taxon_descriptors`)
- `src/communitymech/validators/gtdb_coherence.py`
- `src/communitymech/validators/gtdb_lineage_tree.py`
- `src/communitymech/validators/prokaryotic_lineage.py`

---

## Causal Graph Taxon Grounding Rules

### Rule 1: Every causal graph participant must carry `preferred_term` and `term: {id, label}`

Every `source_taxon`, `target_taxon`, `participating_taxa[]`, and `counter_selection[].excluded_taxon` must include:

```yaml
source_taxon:
  preferred_term: Geobacter sulfurreducens
  term:
    id: NCBITaxon:35554
    label: Geobacter sulfurreducens
```

- `term.id` must be a valid `NCBITaxon:<id>` CURIE.
- `term.label` must match the canonical `rdfs:label` or an `oio:hasExactSynonym` in `sqlite:obo:ncbitaxon` (enforced by `just validate-terms`).

### Rule 2: Exact synchronization between causal graph nodes and `taxonomy[].taxon_term`

When a causal graph participant's `preferred_term` appears in `taxonomy[].taxon_term`, its `term: {id, label}` must be **identical** to `taxonomy[].taxon_term.term`:

- **Keep causal graph participant blocks compact**: In `kb/communities/*.yaml` and `data/isolates/*.yaml`, causal graph participants (`source_taxon`, `target_taxon`, `participating_taxa[]`) store `{preferred_term, term: {id, label}}`, while `gtdb_grounding_status` and `gtdb_classification` live on `taxonomy[].taxon_term`. The causal graph review batch tests (`tests/test_causal_review_batch*.py`) assert `set(participant) == {"preferred_term", "term"}`.
- **Validator coverage**: If a `gtdb_classification` or `gtdb_grounding_status` is ever attached to a causal graph participant or `counter_selection.excluded_taxon`, `gtdb_coherence`, `gtdb_lineage_tree`, and `prokaryotic_lineage` validate it automatically.

### Rule 3: Grounding functional guilds in causal graphs

When an ecological interaction is formulated at the guild or consortium level (e.g., `"Sulfate-reducing bacteria"`, `"Hydrogenotrophic methanogens"`, `"Purple sulfur bacteria"`, `"Fermentative bacteria"`):

1. Ground `term` to the **most specific monophyletic clade** in NCBITaxon that encompasses the guild in that community:
   - Purple sulfur bacteria -> `NCBITaxon:1046` (`Chromatiaceae`)
   - Green sulfur bacteria -> `NCBITaxon:191412` (`Chlorobiaceae`)
   - Hydrogenotrophic methanogens (Methanobacteria) -> `NCBITaxon:183925` (`Methanobacteria`)
   - Fermentative clostridia -> `NCBITaxon:186801` (`Clostridia`)
   - Polyphyletic bacterial guild spanning multiple phyla -> `NCBITaxon:2` (`Bacteria`) or `NCBITaxon:1224` (`Pseudomonadota`) / `NCBITaxon:1239` (`Bacillota`) as appropriate.
2. If two entries in the same record share a coarse `NCBITaxon` ID (such as two distinct functional guilds grounded to `NCBITaxon:2` `Bacteria`), explain the functional or strain-level distinction in `taxonomy[].taxon_term.notes` so `scripts/validate_shared_taxon_ids.py` (`just validate-shared-taxon-ids`) can verify it is an intentional guild/strain split and not an ID collision (#292).

---

## Step-by-Step Three-System Grounding Workflow

### Step 1: Ground and Verify in NCBITaxon (OAK)

Query the local NCBITaxon SQLite database via OAK:

```bash
# Look up an ID and check its canonical label
uv run runoak -i sqlite:obo:ncbitaxon info NCBITaxon:35554

# Search by scientific name or synonym
uv run runoak -i sqlite:obo:ncbitaxon search "Geobacter sulfurreducens"

# Check lineage/domain to guard against cross-kingdom homonyms
uv run python -c '
from communitymech.validators.ncbi_domain import domain_of, outside_gtdb_scope
print(domain_of("NCBITaxon:35554"), outside_gtdb_scope("NCBITaxon:35554"))
'
```

**Watch for cross-kingdom homonyms (#292, #365)**:
- *Bosea*: `NCBITaxon:169215` is a **plant** genus (Amaranthaceae); the alphaproteobacterium is `NCBITaxon:85413` (*Allobosea* in NCBI, `g__Bosea` in GTDB).
- *Sulcia*: `NCBITaxon:2716471` is a **spider** genus; the bacterial endosymbiont is `NCBITaxon:336809` (*Candidatus Karelsulcia* in NCBI, `g__Sulcia` in GTDB).
- Always confirm `domain_of(curie)` returns `NCBITaxon:2` (Bacteria) or `NCBITaxon:2157` (Archaea) for prokaryotes, and `NCBITaxon:2759` (Eukaryota) or `NCBITaxon:10239` (Viruses) for non-prokaryotes.

### Step 2: Ground in GTDB (`scripts/gtdb_ground.py`)

For prokaryotic taxa (`NCBITaxon:2` and `NCBITaxon:2157`), resolve the GTDB classification against the local `kg-microbe` `NCBI2GTDB.tsv.gz` crosswalk:

```bash
# Inspect a single taxon's GTDB grounding and emit YAML
uv run python scripts/gtdb_ground.py --ncbi-id NCBITaxon:35554 --emit-yaml
uv run python scripts/gtdb_ground.py --name "Shewanella oneidensis" --emit-yaml

# Ground an entire community or CommonTaxon record (kb/communities/ or kb/taxa/) and write gtdb_grounding_status
uv run python scripts/gtdb_ground.py --community kb/communities/<Record>.yaml --apply
uv run python scripts/gtdb_ground.py --community kb/communities/<Record>.yaml --apply-status
uv run python scripts/gtdb_ground.py --community kb/taxa/<Record>.yaml
```

Verify the resulting `gtdb_grounding_status` and `gtdb_classification`:
- `GROUNDED`: accompanied by `gtdb_classification` (`gtdb_id`, `gtdb_taxon`, `gtdb_lineage`, `ncbi_source_id`, `majority_fraction`, `total_genomes`, optional `support_genomes` on genus-and-higher, `is_reclassified`, `mapping_source`).
- `AMBIGUOUS`: GTDB splits the NCBI taxon with no strict majority (`<= 0.5`); `gtdb_candidates` lists ranked `GTDB:` CURIEs.
- `WITHHELD`: curator-withheld grounding where the automated vote is misleading for the record's organism (#292, #396, #416).
- `NO_GTDB_EQUIVALENT`: **only** when `outside_gtdb_scope(curie)` is `True` (provably `Eukaryota` or `Viruses` in `sqlite:obo:ncbitaxon`).
- `UNRESOLVED`: in-scope prokaryote (or above-domain taxon) with no crosswalk resolution.

### Step 3: Cross-Check LPSN / ICNP Standing & Document Synonyms

When curating `kb/taxa/*.yaml` (`CommonTaxon.taxon_term.notes`), resolving `is_reclassified: true` disagreements between NCBI and GTDB, or pinning a curated GTDB block (`curated: true` + `curation_note`), cross-check **LPSN** (`https://lpsn.dsmz.de/`) / **ICNP** nomenclature:

1. **Valid Publication & Type Strain**:
   - Record the validly published authority under ICNP (e.g., `Caccavo et al. 1994`, `Venkateswaran et al. 1999`) and type strain culture collection accessions (e.g., `PCA = ATCC 51573 = DSM 12127`, `MR-1 = ATCC 700550 = CIP 106686`).
2. **2021 ICNP Phylum Names (Oren & Garrity 2021, *Int J Syst Evol Microbiol* 71:005056)**:
   - Note divergences between ICNP/NCBI valid phylum names and GTDB phyla:
     - `Pseudomonadota` (`NCBITaxon:1224`, formerly *Proteobacteria*)
     - `Bacillota` (`NCBITaxon:1239`, formerly *Firmicutes*; split in GTDB into `p__Bacillota`, `p__Bacillota_A`, etc.)
     - `Actinomycetota` (`NCBITaxon:201174`, formerly *Actinobacteria*)
     - `Bacteroidota` (`NCBITaxon:976`, formerly *Bacteroidetes*)
     - `Thermodesulfobacteriota` (`NCBITaxon:200940`, encompassing former *Deltaproteobacteria*; `p__Desulfobacterota` in GTDB)
     - `Nitrososphaerota` (`NCBITaxon:651137`, formerly *Thaumarchaeota*; demoted to class `c__Nitrososphaeria` under `p__Thermoproteota` in GTDB)
3. **Homotypic / Heterotypic Synonyms & Genus Reclassifications**:
   - Document when NCBI and GTDB use different validly published synonyms or genus splits (e.g., *Lactobacillus* -> *Lactiplantibacillus* / *Limosilactobacillus* / *Levilactobacillus* per Zheng et al. 2020; *Pelobacter carbinolicus* -> *Syntrophotalea carbinolica* in LPSN/GTDB; *Allobosea* in NCBI vs. *Bosea* in GTDB).

Example `kb/taxa/*.yaml` `CommonTaxon.taxon_term` with full three-system grounding:

```yaml
taxon_term:
  preferred_term: Geobacter sulfurreducens
  term:
    id: NCBITaxon:35554
    label: Geobacter sulfurreducens
  notes: >-
    Model dissimilatory metal-reducing bacterium; type species of the genus
    Geobacter. Validly published under the ICNP (Caccavo et al. 1994; LPSN
    species Geobacter sulfurreducens, type strain PCA = ATCC 51573 = DSM
    12127); placed in phylum Thermodesulfobacteriota in LPSN/NCBI and phylum
    Desulfobacterota (class Desulfuromonadia, order Geobacterales, family
    Geobacteraceae) in GTDB.
  gtdb_grounding_status: GROUNDED
  gtdb_classification:
    gtdb_id: GTDB:s__Geobacter_sulfurreducens
    gtdb_taxon: Geobacter sulfurreducens
    gtdb_lineage: d__Bacteria;p__Desulfobacterota;c__Desulfuromonadia;o__Geobacterales;f__Geobacteraceae;g__Geobacter;s__Geobacter sulfurreducens
    ncbi_source_id: NCBITaxon:35554
    majority_fraction: 1.0
    total_genomes: 19
    is_reclassified: false
    mapping_source: kg-microbe NCBI2GTDB.tsv.gz; GTDB release latest (built 2026-07-25)
```

---

## Corpus-Wide Audit & Verification Commands

### Audit all records and causal graph elements against `sqlite:obo:ncbitaxon`

```bash
uv run python -c '
from pathlib import Path
import yaml
from communitymech.ontology_adapters import ncbitaxon_adapter
from communitymech.paths import taxon_descriptor_roots
from communitymech.taxon_blocks import iter_taxon_descriptors

adapter = ncbitaxon_adapter()
assert adapter is not None, "NCBITaxon SQLite adapter unavailable"

missing_id, label_mismatch, graph_mismatch = [], [], []
for root in taxon_descriptor_roots():
    for path in sorted(root.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text()) or {}
        tax_by_pref = {
            (e.get("taxon_term") or {}).get("preferred_term"): (e.get("taxon_term") or {}).get("term")
            for e in (doc.get("taxonomy") or [])
            if isinstance(e, dict) and isinstance(e.get("taxon_term"), dict)
        }
        for desc in iter_taxon_descriptors(doc):
            term = desc.get("term") or {}
            tid, tlabel = term.get("id"), term.get("label")
            if not tid or not tlabel:
                missing_id.append((path.name, desc.get("preferred_term")))
                continue
            primary = adapter.label(tid)
            syns = set(adapter.entity_aliases(tid) or [])
            if primary != tlabel and tlabel not in syns:
                label_mismatch.append((path.name, tid, tlabel, primary))
        for ix in doc.get("ecological_interactions") or []:
            if not isinstance(ix, dict):
                continue
            nodes = [ix.get("source_taxon"), ix.get("target_taxon"), *(ix.get("participating_taxa") or [])]
            for node in [n for n in nodes if isinstance(n, dict)]:
                pref = node.get("preferred_term")
                if pref in tax_by_pref and node.get("term") != tax_by_pref[pref]:
                    graph_mismatch.append((path.name, ix.get("name"), pref))

print(f"missing_id={len(missing_id)} label_mismatch={len(label_mismatch)} graph_mismatch={len(graph_mismatch)}")
assert not (missing_id or label_mismatch or graph_mismatch)
'
```

### Run all taxonomic & causal graph validation gates

```bash
# 1. GTDB count/status/curated coherence across all records
just validate-gtdb-all

# 2. Shared NCBITaxon ID / homonym / guild check
just validate-shared-taxon-ids

# 3. Targeted pytest suite for taxonomic & causal graph grounding
uv run pytest \
  tests/test_taxon_records.py \
  tests/test_gtdb_coherence_validator.py \
  tests/test_gtdb_lineage_tree.py \
  tests/test_prokaryotic_lineage.py \
  tests/test_ncbi_domain_scope.py \
  tests/test_shared_taxon_ids.py
```

> **Note on hash-pinned community & isolate records**: All 462 existing records in `kb/communities/` and `data/isolates/` have their `record_sha256` pinned in `reports/causal_graph_review/inventory.tsv` and `reports/causal_graph_review/decisions/*.yaml` (enforced by `tests/test_causal_review_batch*.py`). If you intentionally modify an existing community or isolate YAML file, update its corresponding causal review decision artifact and `inventory.tsv` hash in the same change.

---

## Related Skills & Scripts

- `ground-taxa-gtdb` (`../ground-taxa-gtdb/SKILL.md`) — deep dive on `scripts/gtdb_ground.py`, `NCBI2GTDB.tsv.gz` majority-fraction rules, `total_genomes`/`support_genomes`, and `is_reclassified` semantics.
- `id-label-correspondence` (`../id-label-correspondence/SKILL.md`) — OAK `id` <-> `label` validation across all ontologies.
- `audit-network-quality` (`../audit-network-quality/SKILL.md`) — causal ecological interaction network topology and evidence auditing.
- `scripts/gtdb_ground.py` — GTDB grounding CLI and status classifier.
- `scripts/validate_shared_taxon_ids.py` — detects accidental NCBITaxon ID collisions vs. documented guild/strain splits.
