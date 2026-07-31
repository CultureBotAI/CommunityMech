---
name: add-growth-conditions
description: Deep-research and add source-backed growth/cultivation conditions (medium, temperature, pH, atmosphere, salinity, light, incubation, shaking, inoculum, vessel — and reactor/mode for engineered systems) to CommunityMech community records. For one record or a whole-KB sweep. Extracts conditions from the record's cited source (Europe PMC abstract + OA full-text Methods), adds a growth_media (and cultivation_setup where applicable) block with verbatim evidence snippets, and validates. Never fabricates — records whose sources report no conditions (or are paywalled) are left unchanged.
category: research
requires_database: false
requires_internet: true
version: 1.1.0
---

# Add Growth Conditions to Community Records

## Overview

Enrich CommunityMech records with **growth/cultivation conditions** mined from
each community's cited source. Conditions live in two schema slots, both on
`MicrobialCommunity`, both evidence-backed:

- **`growth_media`** (list of `GrowthMedia`) — medium + physicochemical
  conditions: `name`, `composition`, `temperature`(+`_unit`/`_range`), `ph`
  (+`_range`), `atmosphere` (enum), `headspace_gas`, `salinity`(+unit),
  `pressure`(+unit), `light_regime`/`light_intensity`(+unit),
  `redox_potential`(+unit), `inoculum_source`/`inoculum_size`(+unit),
  `incubation_time`(+unit), `shaking_speed`(+unit), `vessel_type`,
  `preparation_notes`, `evidence`.
- **`cultivation_setup`** (list of `CultivationSetup`) — for defined engineered
  systems: `cultivation_mode` (enum), `system_type` (enum), `working_volume`,
  `operating_temperature`, `retention_time`(+type), `applied_potential`,
  `electrode_detail`, control flags, `evidence`. Add only when a real
  reactor/bioelectrochemical/continuous system is described.

Enum values:
- `AtmosphereEnum`: AEROBIC, ANAEROBIC, MICROAEROBIC, FACULTATIVE_ANAEROBIC, FACULTATIVE_AEROBIC, CAPNOPHILIC
- `CultivationModeEnum`: BATCH, FED_BATCH, CONTINUOUS, SEMI_CONTINUOUS, CHEMOSTAT, TURBIDOSTAT, PERFUSION, SEQUENCING_BATCH, RETENTOSTAT, OTHER
- `CultivationSystemEnum`: STIRRED_TANK_BIOREACTOR, PHOTOBIOREACTOR, MICROBIAL_FUEL_CELL, BIOELECTROCHEMICAL_SYSTEM, CHEMOSTAT_VESSEL, MEMBRANE_BIOREACTOR, SERUM_BOTTLE, FLASK, GAS_LIFT_REACTOR, PACKED_BED_REACTOR, MICROFLUIDIC_DEVICE, HOLLOW_FIBER_REACTOR, BIOREACTOR_UNSPECIFIED, OTHER

## Cardinal rule: no fabrication

Add only conditions actually stated in the record's cited source (or a clearly
related source you can cite). Every added block carries an `evidence` item with a
**verbatim** snippet (≥10 chars), the `reference` (PMID:/doi:), `supports:
SUPPORT`, and an `evidence_source`. If the source reports no conditions — common
when the paper is **paywalled** (abstract-only) — make **no change** and say so.
Growth values in `growth_media` are strings (ranges allowed); `cultivation_setup`
numerics are floats.

## Deep-research workflow (per record)

1. Read the record; find its primary `reference` (a PMID/doi in the evidence).
2. Fetch the abstract — Europe PMC core:
   `…/webservices/rest/search?query=EXT_ID:<pmid>%20AND%20SRC:MED&format=json&resultType=core`
   (DOI: `query=DOI:"<doi>"`).
3. Locate legal full text via the access ladder — `scripts/fulltext_access.py
   --pmid <pmid>` (or `--doi <doi>`). It tries, in order: **Europe PMC OA**
   (`fullTextXML`) → **Unpaywall** best OA location (free) → **CORE** (set
   `CORE_API_KEY`) → and if none, prints an **author-request email draft**.
   - `ACCESS <method> <url>` → fetch that URL for the Methods (`curl --compressed`
     for the EPMC XML).
   - `NO_LEGAL_OA` → the paper is closed-access with no legal OA copy; use only
     abstract-level conditions, and surface the author-request draft to the
     curator. **Never** use Sci-Hub or other gray-area sources.
4. Extract conditions → one `growth_media` entry (+ `cultivation_setup` if a
   defined reactor). Insert as new top-level keys (append near end of file);
   keep existing content byte-for-byte.
5. Validate — both must pass:
   ```bash
   just validate kb/communities/<File>.yaml
   just validate-terms kb/communities/<File>.yaml
   ```

## Running for one record

Point an agent (or yourself) at the record with the workflow above. Minimal
`growth_media` example (anaerobic AD community, paywalled → only atmosphere +
notes recoverable):
```yaml
growth_media:
- name: unspecified (glucose-based anaerobic fermentation medium)
  atmosphere: ANAEROBIC
  preparation_notes: Glucose carbon source; 0.1 mM riboflavin supplementation.
  evidence:
  - reference: PMID:42203120
    supports: SUPPORT
    evidence_source: IN_VITRO
    snippet: <verbatim phrase naming the conditions>
    explanation: Anaerobic succinic-acid fermentation with riboflavin mediator.
```

## Running for the whole KB (sweep)

Use the **sweep runner** — `scripts/growth_conditions_sweep.py` — to do the
deterministic prep (enumerate candidates, resolve each record's primary
reference, fetch the abstract, run the access ladder) *once*, so extraction
agents start from a ready source bundle instead of each re-fetching. The runner
**never edits `kb/`**; it only writes staging files under
`reports/growth_conditions_sweep/`, so a curator can review the prep first.

1. **List** candidates (records with neither `growth_media` nor
   `cultivation_setup`):
   ```bash
   uv run python scripts/growth_conditions_sweep.py --list
   ```
2. **Prep** the source bundles (live network fetch; `--limit N` for a test batch,
   or pass explicit record paths):
   ```bash
   uv run python scripts/growth_conditions_sweep.py --prep            # all missing
   uv run python scripts/growth_conditions_sweep.py --prep --limit 5  # test batch
   ```
   This writes one `reports/growth_conditions_sweep/<Record>.md` per record
   (primary ref, title, **frequency-ranked list of every cited ref**, abstract,
   and either the OA Methods URL to `curl --compressed` or an author-request
   draft) plus an **`INDEX.md`** progress report bucketing each record as
   `OA_FULLTEXT` / `ABSTRACT_ONLY` / `NO_REFERENCE` with counts.
3. **Read `INDEX.md`.** Start with the `OA_FULLTEXT` rows — Methods are reachable,
   so those yield the richest blocks. `ABSTRACT_ONLY` rows are paywalled: extract
   only abstract-level conditions (often just `atmosphere` + notes) or leave
   unchanged and keep the author-request draft.
4. **Fan out** one agent per record (or a few per agent), each fed its bundle +
   the per-record workflow above. Cap concurrency; process in waves. ⚠️ The
   *primary* (most-cited) ref is sometimes a **review**, not the community's
   methods paper — if its abstract/full text describes no cultivation of *this*
   community, have the agent pick a better ref from the ranked list in the bundle.
5. **Expect partial yield.** Many sources are paywalled, so a large fraction will
   legitimately get no conditions — that is the correct outcome, not a failure.
   The `INDEX.md` buckets set the expectation up front.
6. After each wave, run `just validate-all` + `just validate-terms-all` and
   commit the enriched records. Re-running `--prep` regenerates `INDEX.md`, and
   enriched records drop out of `--list` automatically (they now have a block).

## Interpreting results

- **Enriched** — conditions found and added with evidence.
- **No conditions reported** — the accessible source (abstract ± OA full text)
  states none; record unchanged.
- **Paywalled** — no OA full text; only abstract-level conditions (if any) are
  recoverable. Note this so a later pass with institutional access can revisit.

## Related

- `deep-research-community` — deeper Edison/PaperQA enrichment when the abstract
  is thin and full text is reachable.
- `review-communities`, `evidence-curation` — validate the added evidence.
- `ground-taxa-gtdb` — the sibling enrichment skill (taxa → GTDB).

## Related scripts / schema

- `scripts/growth_conditions_sweep.py` — sweep prep runner (`--list` / `--prep`);
  reuses `scripts/fulltext_access.py` for the access ladder.
- Slots: `MicrobialCommunity.growth_media` (`GrowthMedia`),
  `MicrobialCommunity.cultivation_setup` (`CultivationSetup`) — see
  `src/communitymech/schema/communitymech.yaml`.
