---
name: add-growth-conditions
description: Deep-research and add source-backed growth/cultivation conditions (medium, temperature, pH, atmosphere, salinity, light, incubation, shaking, inoculum, vessel — and reactor/mode for engineered systems) to CommunityMech community records. For one record or a whole-KB sweep. Extracts conditions from the record's cited source (Europe PMC abstract + OA full-text Methods), adds a growth_media (and cultivation_setup where applicable) block with verbatim evidence snippets, and validates. Never fabricates — records whose sources report no conditions (or are paywalled) are left unchanged.
category: research
requires_database: false
requires_internet: true
version: 1.0.0
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
3. If open-access, fetch Methods from full text: get `pmcid` from the core
   result, then `…/webservices/rest/<PMCID>/fullTextXML` (`curl --compressed`).
   Optionally WebSearch/WebFetch for the Methods if not OA.
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

1. Enumerate records lacking `growth_media`:
   ```bash
   for f in kb/communities/*.yaml; do
     grep -qE '^growth_media:|^cultivation_setup:' "$f" || echo "$f"
   done
   ```
2. Fan out one agent per record (or a few records per agent), each following the
   per-record workflow. Cap concurrency; process in waves.
3. **Expect partial yield.** Many sources are paywalled, so a large fraction will
   legitimately get no conditions — that is the correct outcome, not a failure.
   Track: enriched vs. no-conditions-reported vs. paywalled.
4. After each wave, run `just validate-all` + `just validate-terms-all` and
   commit the enriched records.

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

- Slots: `MicrobialCommunity.growth_media` (`GrowthMedia`),
  `MicrobialCommunity.cultivation_setup` (`CultivationSetup`) — see
  `src/communitymech/schema/communitymech.yaml`.
