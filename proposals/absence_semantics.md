# Absence semantics in CommunityMech (#294, #304, #307)

Three open issues turn out to be one diagnosis. This proposal states it, quantifies each
instance, and recommends a remedy per instance — which is **not** the same remedy three
times.

**Decision requested:** approve or reject each of the three remedies in §4. They are
independent; approving one does not commit to the others.

---

## 1. The shared diagnosis

The schema can say *"this slot has value X"* and *"this slot is empty"*, and nothing else.
Empty is therefore overloaded. In the records it currently means at least four different
things:

| what the curator meant | example |
|---|---|
| **not done yet** | a taxon nobody has tried to ground |
| **impossible** | a virus, which GTDB will never classify |
| **undecidable from the source** | GTDB splits the NCBI taxon and the paper does not say which |
| **deliberately excluded** | a strain screened out of a consortium for antagonising its mutualist |

A consumer reading a record cannot tell these apart, and neither can a gate. Worse, in one
case (§3.2) the audit actively *rewards* filling a slot with an unsourced guess, because a
filled slot is treated as more complete than an honest blank.

The three issues are the three places this has already caused a concrete problem.

---

## 2. Why one mechanism will not fix all three

It is tempting to propose a single general "absence annotation" reused everywhere. That
would be wrong here, because the three instances differ in kind:

- **#294** is a *missing vocabulary* problem. The information mostly exists —
  `gtdb_ground.py` already computes three of the states — it simply is not persisted.
- **#307** is a *missing slot* problem. The information exists in the source and in the
  curator's head, and there is nowhere to put it.
- **#304** is **not a schema problem at all**. It is auditor logic. The schema is fine; the
  rule that reads it is wrong.

Bundling them into one schema change would drag a code fix into a data migration for no
benefit. They are proposed separately below and can be done in any order.

---

## 3. The three instances, with numbers

### 3.1 #294 — GTDB grounding: 372 blanks, none of which are pending work

Measured 2026-08-03 over 307 records / 1007 taxonomy entries:

| | count | share of ungrounded |
|---|---:|---:|
| grounded | 635 of 1007 (63%) | — |
| **no GTDB equivalent** — eukaryote, virus, environmental pseudo-taxon, absent from mapping | 285 | 76% |
| **ambiguous** — GTDB splits the NCBI taxon with no majority | 85 | 23% |
| **groundable by the tool** | 5 occurrences | 1% |

Checking what those last five are is what makes the case. Every one is an entry
**deliberately withheld** under #292 — *Bacteroides ovatus* on `NCBITaxon:821`
(*Phocaeicola vulgatus*) and `Nitrospiraceae bacterium` on `NCBITaxon:1236`
(Gammaproteobacteria), whose ids name a different organism, pinned by
`tests/test_gtdb_withheld_groundings.py` so a tool re-run cannot reinstate them.

So the honest tally is **370 permanently ungroundable, 2 deliberately withheld, and zero
pending work** — three distinct states rendered as one blank. GTDB grounding is complete to
its ceiling and the schema cannot say so. This is exactly why #276 read as ~40% outstanding
work when the achievable ceiling is ~63%: the issue — which I wrote — mistook impossibility
for backlog, and nothing in the data could have corrected that reading.

It also means #294 has a **fourth** state to represent, distinct from the other three:
grounding withheld pending an upstream correction.

### 3.2 #304 — DISCONNECTED fires on the wrong criterion

Two rules interact in `network/auditor.py`:

1. `connected_taxa` is built only from `source_taxon`/`target_taxon` (lines ~189, ~229). A
   `COMMUNITY_LEVEL` interaction has neither by design, so it contributes **no**
   connections. **107 of 302 records with interactions (35%) are entirely
   `COMMUNITY_LEVEL`** — structurally, a third of the KB has zero connected taxa.
2. A taxon carrying `abundance_level` **or** `functional_role` is exempt (line ~258).
   **931 of 1007 taxa (92%) are exempt on this basis.**

The exemption is doing essentially all the work. `DISCONNECTED` does not mean "this taxon
has no curated interaction"; it means "this taxon has no *pairwise* interaction **and** no
membership metadata" — a compound of connectivity and slot-completeness that the name does
not convey.

**The consequence is a perverse incentive.** In PR #298 I had invented `abundance_level`
values (`AbundanceEnum` is quantitative — `DOMINANT` is ">1% relative abundance" — and the
paper reported no abundances). Review removed them, which is unambiguously correct, and the
immediate result was five new `DISCONNECTED` findings. A curator optimising against the
audit would put the guesses back.

### 3.3 #307 — counter-selection has nowhere to live

`SynCom_ARC` (CommunityMech:000314) is *defined* by an exclusion: candidate *Bacillus*
isolates that inhibited *Bradyrhizobium* were screened out, so the shipped community is the
subset of effective antifungal strains that spares the nitrogen-fixing mutualist.

There were two places to put that, and both are bad:

- **As an `ecological_interaction`** — machine-readable but false. Excluded and retained
  isolates are indistinguishable at the genus-level grounding the source supports, so the
  typed edge asserts that an ARC *member* antagonises the mutualist ARC exists to spare.
- **As `engineering_design.notes` prose** — accurate but invisible to any query.

PR #305 chose prose. That was right for the record and means the fact is no longer
queryable. Screening is how most SynComs are built, so this recurs: 193 records carry
`engineering_design`, and only 40 carry free-text `notes` — the rest have no natural place
for a negative result at all.

---

## 4. Proposed remedies

### 4.1 #294 — add a grounding-status enum *(schema, small)*

Add to `TaxonDescriptor`, alongside `gtdb_classification`:

```yaml
gtdb_grounding_status:
  range: GtdbGroundingStatusEnum
  # GROUNDED | NO_GTDB_EQUIVALENT | AMBIGUOUS | WITHHELD | NOT_ATTEMPTED
  required: false
```

`WITHHELD` is needed because §3.1 found two real instances of it: grounding is possible and
deliberately not applied, pending an upstream fix (#292). Without it those two collapse into
`NOT_ATTEMPTED`, which is what the pin in `tests/test_gtdb_withheld_groundings.py` currently
exists to prevent — a test compensating for vocabulary the schema lacks.

`AMBIGUOUS` should carry the candidate GTDB taxa, since that is precisely what a curator
needs in order to resolve it. Either a companion multivalued `gtdb_ambiguous_candidates`
slot, or fold the status into the existing `GtdbClassification` class and allow it without
a `gtdb_id`.

`gtdb_ground.py` already distinguishes GROUNDED, AMBIGUOUS and NO_GTDB_EQUIVALENT
internally, so populating those three is a mechanical pass rather than a curation effort;
only WITHHELD needs to be asserted by hand, and there are two of them. Add a gate afterwards asserting the status matches
what the tool computes, so it cannot drift — the shape used by `tests/test_enum_groundings.py`.

**Cost:** one schema change, one datamodel regeneration, one backfill run, one test.
**Benefit:** ~63% coverage stops looking like ~63% completion.

### 4.2 #304 — fix the auditor, change no data *(code, small)*

Two independent changes:

1. **Credit `COMMUNITY_LEVEL` interactions.** Treat every taxon in a record as connected by
   a community-level interaction, which is what such an interaction asserts. This alone
   removes the structural penalty on 107 records.
2. **Drop the `abundance_level`/`functional_role` exemption.** With (1) in place, the
   exemption's original purpose — suppressing false positives on records that describe
   membership without pairwise edges — is served properly rather than by proxy.

Doing (1) without (2) is safe and strictly an improvement. Doing (2) without (1) would
surface a large backlog at once and should not be done alone.

**This is prerequisite for #273.** That issue cannot decide whether to restore the network
gate while `DISCONNECTED` means something other than its name.

### 4.3 #307 — add a counter-selection block *(schema, medium)*

Add to `CommunityEngineeringDesign`:

```yaml
counter_selection:
  multivalued: true
  range: CounterSelection      # excluded_taxon (TaxonDescriptor, optional), criterion, evidence
```

Deliberately **not** in `ecological_interactions`: excluded candidates are not members, and
these are not interactions within the community. Making them edges is what produced the
#300 defect.

`excluded_taxon` must be optional, because ARC is exactly the case where the excluded
strains cannot be distinguished from the retained ones at the available resolution. A
counter-selection with a criterion and evidence but no resolved taxon is still far more
useful than prose.

**Open question for the curator:** should excluded candidates ever appear in `taxonomy`?
Recommendation: **no** — they are not members, and adding them would re-create #304-style
connectivity noise.

---

## 5. Recommended sequence

1. **#304 change (1)** — credit `COMMUNITY_LEVEL`. Smallest, no data migration, unblocks
   #273, and removes an active perverse incentive.
2. **#294** — status enum plus mechanical backfill. Self-contained, and retires the
   recurring misreading of GTDB coverage as GTDB backlog.
3. **#307** — the largest, and the one most worth designing carefully rather than quickly,
   since it introduces a concept the schema does not yet have.

Note there is **no** independent quick win here: the five apparently-groundable taxa in
§3.1 are the withheld ones, blocked on #292 (correcting two NCBITaxon ids that name the
wrong organism). Fixing #292 is worth doing on its own merits and would let those two ground
themselves on the next tool run.

## 6. What is deliberately not proposed

- **A general absence-annotation framework.** Three instances is not enough evidence to
  design one, and §2 argues they are not the same kind of problem.
- **A `NOT_APPLICABLE` value anywhere.** It reintroduces the ambiguity this proposal is
  trying to remove; `NO_GTDB_EQUIVALENT` says why, and "not applicable" does not.
- **Backfilling `abundance_level`.** The perverse incentive in §3.2 should be removed by
  fixing the audit, never by filling the slot. `AbundanceEnum` is quantitative and most
  sources do not report abundances.
