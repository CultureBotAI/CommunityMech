---
name: ground-taxa-gtdb
description: Ground CommunityMech taxa in GTDB (Genome Taxonomy Database) alongside their NCBITaxon term, using the local kg-microbe NCBI<->GTDB mapping. Resolves an NCBITaxon id (or species name) to its canonical GTDB CURIE, taxon name, full lineage, and mapping confidence; flags GTDB reclassifications/renames (e.g. NCBITaxon "Agrobacterium deltae" -> GTDB "Agrobacterium leguminum"); and emits a ready-to-paste gtdb_classification block for the taxon.
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
---

# Ground Taxa in GTDB (kg-microbe local mapping)

## Overview

CommunityMech taxa are grounded in **NCBITaxon**. GTDB (the Genome Taxonomy
Database) is a genome-based, phylogenetically-consistent taxonomy that
frequently **renames or reclassifies** relative to NCBI. Adding a GTDB
classification alongside the NCBITaxon term gives each taxon a second,
genome-based identity — valuable for cross-referencing against kg-microbe's KG
and for catching NCBI/GTDB disagreements.

This skill resolves a taxon's NCBITaxon id (or species name) to its GTDB
classification using the **local kg-microbe** mapping (no network, no API), and
writes it into the record's `gtdb_classification` slot.

Worked example: `CommunityMech:000272` SynCom Y — *A. deltae* (NCBITaxon:1183412)
grounds to **GTDB:s__Agrobacterium_leguminum** (a GTDB rename, flagged
`is_reclassified: true`); *B. velezensis* (NCBITaxon:492670) grounds to
**GTDB:s__Bacillus_velezensis** (unchanged).

## Data source (local, no network)

`<kg-microbe>/data/raw/NCBI2GTDB.tsv.gz` — kg-microbe's precomputed NCBI→GTDB
mapping with per-rank lineages and a `majority fraction` (share of genomes under
the NCBI taxon that land on the GTDB taxon = mapping confidence). Companion
files in the same dir: `GTDB2NCBI.tsv.gz`, `gtdb/bac120_taxonomy.tsv`,
`gtdb/ar53_taxonomy.tsv`, `gtdb_{species,genus,family}_summary.jsonl.gz`.

`<kg-microbe>` is resolved as: `--kg-microbe-dir`, else `$KG_MICROBE_DIR`, else
`../../kg-microbe` (walking up from the repo to tolerate the nested
`CommunityMech/CommunityMech` layout). Default local checkout:
`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe`.

## GTDB CURIE scheme

Matches kg-microbe / Bioregistry: the species name with spaces replaced by
underscores, prefixed `GTDB:`, e.g. `s__Bacillus velezensis` ->
`GTDB:s__Bacillus_velezensis`. Resolvable at
`https://gtdb.ecogenomic.org/tree?r={id}`. GTDB names are only **best-effort
stable across releases**, so `gtdb_classification.mapping_source` records the
release/build provenance — always keep it.

## Schema

`gtdb_classification` lives on **`TaxonDescriptor`** (so it attaches to
`taxonomy[].taxon_term`, and optionally to interaction `source_taxon`/
`target_taxon`). Fields: `gtdb_id` (CURIE), `gtdb_taxon` (name), `gtdb_lineage`
(full lineage string), `ncbi_source_id` (the NCBITaxon it mapped from),
`majority_fraction` (0-1 confidence), `is_reclassified` (GTDB name ≠ NCBI name),
`mapping_source` (provenance). It is **not** an OAK-validated term — GTDB is not
in `conf/oak_config.yaml`, and the id↔label validator deliberately ignores it
(the `gtdb_id` is a pattern-checked plain string, not a bound `Term`).

## Workflow

### 1. Ground a whole community (usual case)

```bash
just ground-taxa-gtdb --community kb/communities/<File>.yaml --emit-yaml
# or:
uv run python scripts/gtdb_ground.py --community kb/communities/<File>.yaml --emit-yaml
```

Prints, per `taxonomy[].taxon_term`, the GTDB taxon / CURIE / lineage /
confidence, flags reclassifications, and (with `--emit-yaml`) prints a
paste-ready `gtdb_classification` block.

### 2. Ground a single taxon

```bash
uv run python scripts/gtdb_ground.py --ncbi-id NCBITaxon:492670 --emit-yaml
uv run python scripts/gtdb_ground.py --name "Bacillus velezensis"
```

### 3. Apply to the record

Fastest: let the script write the blocks in place (add-only text edits — it does
not reflow or reformat anything else, and skips taxa already grounded):

```bash
uv run python scripts/gtdb_ground.py --community kb/communities/<File>.yaml --apply
```

Or paste each `--emit-yaml` block into the matching `taxon_term` (as a sibling of
`preferred_term`/`term`/`notes`) by hand. Then validate:

```bash
just validate kb/communities/<File>.yaml          # schema
just validate-terms kb/communities/<File>.yaml    # id↔label (GTDB ignored, as intended)
```

## Rank-aware grounding

Grounding happens at the **rank of the input**:

- **Species** (binomial label) → `GTDB:s__...`, via exact NCBI id, else NCBI
  species-name fallback (the mapping is strain/genome-keyed, so species ids often
  miss on id alone). GTDB species split → AMBIGUOUS.
- **Genus / family / order / …** (single-name label) → `GTDB:g__...` (or
  `f__`/`o__`/…): the script aggregates the GTDB rank column over the genomes
  under the NCBI taxon and grounds to the GTDB taxon holding a **strict majority
  (>50%)** of them; otherwise AMBIGUOUS. An exact 50/50 tie is not a majority and
  does not ground (#382). `mapping_source` records the rank and how many
  GTDB taxa fall under the NCBI taxon (NCBI genus *Bacillus* → `g__Bacillus` at
  0.57, noted as 44 GTDB genera).

  **Since #372 this counts only rows naming an actual binomial.** Rows whose NCBI
  species is `sp.`, `uncultured`, or informal (`Firmicutes bacterium CAG:176`,
  `gamma proteobacterium HTCC2080`) are excluded before the majority is computed
  — `exclude_unnamed`, on by default (#375). `Candidatus` names are kept: those
  are provisional *species* names, not placeholders. Pass `exclude_unnamed=False`
  for the pre-#372 behaviour; *Bacillus* was `g__Bacillus` at 0.508 across 102
  GTDB genera under that rule.

## Grounding status (#294)

Every `taxonomy[].taxon_term` carries `gtdb_grounding_status`, written by
`gtdb_ground.py --community <file> --apply-status`. Absence of a
`gtdb_classification` cannot say *why* it is absent, and the reasons are not
comparable: a missing block implies 317 open items, of which only 9 are
unambiguously outstanding work (#276).

| status | count | meaning |
|---|---|---|
| `GROUNDED` | 715 | a `gtdb_classification` is present |
| `UNRESOLVED` | 221 | the tool produced no grounding; **why is not established** |
| `AMBIGUOUS` | 85 | GTDB splits the NCBI taxon with no majority; `gtdb_candidates` carries every contender |
| `NOT_ATTEMPTED` | 9 | the tool *would* ground it and the KB does not — unambiguously outstanding work |
| `WITHHELD` | 2 | the tool can ground it and a curator decided it must not (#292) |
| `NO_GTDB_EQUIVALENT` | 0 | **curator-assigned only** — the tool cannot establish it (#393) |

`UNRESOLVED` deliberately does not claim finality. Some of it is final (viruses,
eukaryotes — GTDB is bacteria/archaea only) and some is this tool's limits, e.g.
a clade the crosswalk spells differently (NCBI *Sulcia* is `Candidatus
Karelsulcia`). Reading it as "no GTDB equivalent" is the substitution #294 exists
to stop; what remains unseparated is #393.

Rank support runs **domain through genus**. Domain was added in #393, which
moved 72 entries out of `UNRESOLVED`: *Bacteria* and *Archaea* had recorded "no
grounding produced" for the two roots of GTDB. Domain is tried last so a
shallower rank can never pre-empt a deeper one — defensive rather than load
bearing, since no name occupies two rank columns in this crosswalk today.

Those 72 are **10% of all grounded blocks and carry no information beyond the
NCBITaxon id** — *Bacteria* → `d__Bacteria` is a tautology. Filter on
`mapping_source`, which records `[grounded at d__ rank]`, before quoting a
grounding-coverage figure (#403).

`GROUNDED` is redundant with the block's presence on purpose: a consumer should
read a state, not infer one from whether a field exists. The two must agree, and
`communitymech.validators.gtdb_coherence` enforces that — the schema cannot.

`--apply-status` is independent of `--apply`: it writes no groundings, only
status. It is idempotent, and refuses the file rather than guessing if the
taxonomy entries and their id anchors do not line up.

## Interpreting the output

- **`majority_fraction`** — for species, the mapping's majority fraction; for
  genus/higher, the share of the NCBI taxon's **named-binomial** genomes that land
  on the chosen GTDB taxon. Lower values (e.g. *Bacillus* 0.57) warrant a curator
  glance.

- **`total_genomes`** — how many genomes the majority was computed over, i.e.
  what the fraction is a fraction *of* (#383). Read it *before* trusting a
  fraction: `1.0` on `7/7` and `1.0` on `7000/7000` are the same number and very
  different claims. **197 of the KB's groundings rest on fewer than 10 genomes
  and 25 on a single genome**, almost all reading `1.0`. `majority_fraction` is
  rounded, so this cannot be recovered from it. The CLI prints it inline and
  marks a total under 10 `⚠ THIN`.

  For genus-and-higher it counts only what was *counted* — rows dropped by the
  named-species filter are excluded, so it shrinks when the filter bites.

  **For species it is scoped to the rows the grounding was resolved from** — the
  taxon's own rows on an NCBI-id match, the name group on a species-name match.
  Those scopes differ, so an id-matched block can report far less than the
  evidence that exists for its species: `NCBITaxon:562` reports 166398 while
  2610 rows name *E. coli*. Widening it needs a key as stable as the id, and the
  only wider set available is keyed on `term.label` — a synonym moved one taxon
  9.5x — so #389 stays open.

  Counted at **one depth**: a species-rank row and its strain rows overlap, so
  the larger of the two is taken and never their sum.

- **`support_genomes`** — the numerator, on genus-and-higher groundings only.
  Species blocks deliberately carry none: there `majority_fraction` is the
  crosswalk's own column, which holds **two decimal places**, so a numerator
  derived from it would assert precision the source lacks — at 17191 genomes and
  `0.99` the true count spans ~170. A thin grounding is not automatically wrong;
  a small genus is legitimately small. The point is that you can now tell.

  A **true** 50/50 tie never grounds: it is not a majority, so the tool reports
  AMBIGUOUS and records both contenders (#382). Note the stored value is rounded
  to 3 places, so a block *can* read `0.5` legitimately — 5004/10000 is 0.5004,
  a real if slender majority. Read `support_genomes`/`total_genomes` to tell
  them apart; a genuine tie has no block at all. The name tie-break
  survives, but only to make the *option list* reproducible — it no longer
  decides an answer. `--withdraw-ambiguous` removes a stored grounding that has
  become ambiguous, which `--refresh` deliberately cannot do.

  A grounding the majority vote gets *wrong* is pinned **in the block**:

  ```yaml
  gtdb_classification:
    curated: true
    curation_note: why the tool's answer was rejected
  ```

  `--refresh` and `--withdraw-ambiguous` skip a block carrying `curated: true`,
  and `validate-gtdb` rejects the flag without a note — or a note without the
  flag, which reads as a decision while protecting nothing. (`--apply` only ever
  touches *ungrounded* taxa, so it could not have overwritten a pin anyway.)
  Two blocks carry it: `NCBITaxon:18` (*Pelobacter* SFB93 → `g__Syntrophotalea`,
  where the vote picks a selenate reducer) and `NCBITaxon:340177` (*Chlorobium*).

  The script also keeps a `CURATED_GROUNDINGS` list as a fallback, but prefer the
  flag: a list protects only what someone remembered to add, which is how
  *Chlorobium* went unprotected — it survived earlier sweeps only because its
  recompute happened to fail (#376).
- **`is_reclassified: true`** — GTDB uses a different name than NCBI at that rank
  (e.g. *A. deltae* → *A. leguminum*, *Enterococcus* → *Enterococcus_B*). Keep
  both groundings; the disagreement is the point.
- **AMBIGUOUS** — GTDB splits the NCBI taxon into several with no majority
  (e.g. *E. coli* at species; *Bacillus* group members). No block is emitted; a
  curator picks or leaves it ungrounded.
- **No mapping** — rank absent from the NCBI2GTDB table, or a eukaryote (GTDB is
  bacteria/archaea only).

## Notes & limitations

- GTDB is **bacteria/archaea only** — eukaryotic taxa (fungi, microalgae) never
  ground.
- Requires the local kg-microbe checkout with `data/raw/NCBI2GTDB.tsv.gz`
  present (it is a large gzipped TSV; the script streams it, matching only the
  requested ids/names — memory-safe).
- Refreshing GTDB: re-run kg-microbe's `download_gtdb.yaml` there; `mapping_source`
  will pick up the new build date automatically.

## Related

- `manage-identifiers`, `review-communities`, `id-label-correspondence` —
  minting, QC, and NCBITaxon id↔label validation.
- `scout-communities`, `deep-research-community` — discovery + enrichment that
  produce the taxa this skill then grounds in GTDB.

## Related scripts

- `scripts/gtdb_ground.py` — this skill's runner (streams the kg-microbe
  NCBI2GTDB mapping; resolves by NCBITaxon id, name, or whole community; emits
  `gtdb_classification` blocks).
