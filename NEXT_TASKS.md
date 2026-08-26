# Next Tasks — CommunityMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / TraitMech).

Last reconciled: 2026-08-11.

## Reconciliation 2026-08-11 — 26 PRs open, nothing merged

**The backlog's shape has inverted.** On 2026-08-08 the constraint was "what is
left to do". Today it is "what is left to *merge*": **26 PRs are open and every
one is `CLEAN`**, and no merge has happened since. `main` has not moved.

Merging the queue closes **11 open issues** — #312, #325, #347, #410, #514,
#516, #518, #521, #523, #526, #529 — and advances #183, #199 and #543. Nothing
else on this list unblocks as much.

**Merge order matters. Two are stacked:**

```
#515 -> #517      (#517 bases on enrich-cultivation-183g)
#527 -> #528      (#528 bases on curation-history-325)
```

The other 22 are independent of each other and of `main`:
#520 #522 #525 #530 #531 #533 #534 #535 #536 #537 #538 #539 #540 #541 #542
#544 #545 #546 #547 #548 #549 #550.

**Loose end:** `origin/enrich-cultivation-183y` is pushed with a commit
(`2de2e11`, hCom2) and **has no PR**. Open one or delete the branch.

### The queue has started blocking new work

Not merging is no longer neutral. A concrete case, measured today:

The snippet-rendering artefact fixed in #539 (`MPOB T` -> `MPOBT`) and #552
(`CO 2` -> `CO2`) has now bitten twice, which makes it a candidate for a
committed gate. **That gate cannot be added.** Run against `main` it reports
**6 violations** — the three strain designations in
`Syntrophobacter_Methanobacterium_Syntrophy` and the three formula subscripts in
`hCom2_Complex_Gut_Microbiome` — because both fixes live only on unmerged
branches. A guard committed today would be red on `main` on arrival.

The same applies to anything else that would assert a corpus-wide property: 17
curated records and two schema changes are queued, so `main` is 28 PRs behind
what the tests would be written against.

**A caution on the sweep that established the artefact is isolated.** The first
version flattened the snippet but compared it against the cache file's *raw*
text, so any occurrence spanning a line break was invisible. Re-run with both
sides flattened it finds exactly the six above and nothing else — so #540's
"isolated, no batch fix needed" conclusion is true, but it was reached by a check
that could not have shown it. Corrected on #552.

### What the 26 PRs contain

- **17 records** curated for #183 (`cultivation_setup`), each with the "what is
  this number about" question resolved explicitly rather than assumed.
- **Four gates** for defect classes this repo keeps re-hitting: unit slots that
  looked controlled and were not (#514), a vocab-sync invariant that could not
  notice a new enum (#518), record directories the audit did not cover (#350),
  and a cited source that was never about the community (#529).
- **Two schema changes**: `participating_taxa` on `EcologicalInteraction`
  (#312), and six unit enums on `CultivationSetup` (#514).
- **Two records repaired** that were not on any list — `SPRUCE_Peatland_Warming`
  (8 reference failures -> 0) and `Syntrophobacter_Methanobacterium_Syntrophy`
  and `hCom2` (superscript-rendering artefacts).

### Three findings worth keeping

**#183 is smaller than it looks, and not batchable.** 278 records lack a
`cultivation_setup`; 186 are `ENGINEERED`; only **13** have a >20 KB full-text
cache. Of 8 of those 13 read so far: 2 refused, 1 partial, 5 curated. #543
records why no metadata field separates "grown in a vessel" from "sampled from
the world" — `community_origin`, `ecological_state` and `community_category` all
have verified counterexamples.

**My own predictions failed 3 of 5 times.** #543's "likely refuse" group rested
on *plant-associated ⇒ grown on a plant*; `ORNL_PMI_Populus_PD10_SynCom`,
`Suillus_Bacillus` and `hCom2` all falsified it, each differently. A plausible
rule over record names is still a rule over record names.

**The palette question is structural, not a hex swap (#532).** The network
palette fails the rubric's normal-vision floor at ΔE 10.3. A search over 775
single candidates and ~207k saturated warm pairs found nothing clearing both
gates — this repo's CIELAB ΔE76 all-pairs test and the rubric's OKLab ΔE100
adjacent-pairs check use different metrics over different pair sets, and
optimising against either alone produces a change that looks verified and is
not. Nine mutually separable saturated hues is at or past what the space allows.

### Still needs a decision (unchanged, do not start without one)

- **#374** — type-species rule vs genome-count majority. Implementable either
  way; the 0.5 floor is `if frac > 0.5` tool policy, not a schema bound.
- **#182** — 75 of 201 instances have no specificity retained in
  `preferred_term`, concentrated in `CHEBI:50860` (20/22) and `CHEBI:64709`
  (6/6). "Accept as-is" is unavailable for those.
- **#532** — fold a ninth interaction type into "Other", facet, or accept the
  measured failure.

## Reconciliation 2026-08-08 — the 31-issue sweep

PRs **#472–#499** merged: 20 issues closed across all six clusters of the
31-issue backlog (GTDB 10/11, Tooling 4/5, Schema 3/5, Network 2/3, Docs 2/3,
Evidence 1/4).

**The backlog materially overstated remaining work.** Four issues picked up in
this pass were already resolved and still open — #356 (record fixed, both
halves, with notes citing the issue), #259 (DOI cache path implemented, blocked
DOI cached at 67 KB, record curated with 7 citations), #377 (`UBA10281` absent
from the KB entirely; *Acidiphilium* at `g__Acidiphilium @1.0`), #375
(`exclude_unnamed` already defaults to True throughout `gtdb_ground.py`). Each
was closed with the verification rather than assumed.

Two more had **drifted** from their filed numbers rather than being done: #319
counted 23 participants outside `taxonomy` and it is 27 findings over 25
distinct participants; #312 measured 412/518 taxa credited solely by the
community-level rule and it is 407/522. Both are now pinned by tests so the
next drift is visible.

**Verify against the artifact, not the issue text.** Two near-misses in this
pass: #375's filter looked undecided because `reports/gtdb_denominators.tsv`
shows all four denominator options side by side — reading a comparison *of*
options is not reading which is *in force*, and it had been the default for
weeks. And #347 looked resolved because `SPRUCE_Peatland_Methane_Cycling` now
reports 0 issues; the 17 failures are on `SPRUCE_Peatland_Warming`, the sibling
record. Checking the second file is the only reason that was caught.

### Still open from the 31, honestly classified

**Needs a decision (do not start without one):**
- **#374** — should GTDB's type-species rule override a genome-count majority?
  Implementable either way: the 0.5 floor is `if frac > 0.5` in
  `gtdb_ground.py`, a tool policy, *not* a schema bound. An earlier claim in
  this session that it was representationally blocked was wrong.
- **#319** — do the 6 hosts and 3 antagonists belong in `taxonomy`? Now scoped:
  of 25 participants outside it, 14 are UMBRELLA names for members that *are*
  present, so the real question is 9.

**Needs design, not a decision:**
- **#270** — 9 interaction types cannot map 1:1 onto d3's 7 built-in symbols
  minus `circle` (taken by taxa). Needs shape x fill or custom paths, then
  re-validation and eyeballing at the 28x18 node size where the label already
  overflows. Palette measured: fails the OKLab normal-vision floor too
  (`#56bbe6` vs `#57c7ab` at ΔE 10.3), not only CVD as filed.

**Curation passes — each needs the record's cited source read:**
- **#347** — 17 paraphrase failures, confirmed today on
  `SPRUCE_Peatland_Warming_Community` (all 3 refs cached, so these are real
  mismatches rather than missing full text).
- **#497** — 22 rhizobial taxa carrying trophic roles that may be the #301
  substitution. Being a rhizobium does not establish N fixation is what that
  source reports.
- **#182** — measured: the "specificity is retained in `preferred_term`"
  safeguard holds for 126 of 201 instances and fails for 75, concentrated in
  `CHEBI:50860` (20/22) and `CHEBI:64709` (6/6). "Accept as-is" is unavailable
  for those — nothing is holding the specificity.
- **#183**, **#199**.

**Partially addressed, residual scope recorded on the issue:**
- **#410** (nothing working depends on the dead scripts now; delete-or-port
  undecided), **#325** (threshold fixed; backfill undecided, and #491 blocks the
  `history/`-tree option upstream), **#312** (coarseness now counted, refinement
  waits on #307's participant question).

## Reconciliation 2026-08-06 — the wrong-organism thread

Since the 2026-08-03 pass, PRs **#388–#425** merged. That run was almost entirely
one thread, and naming it makes the remaining work legible: **a grounding can be
wrong in a way that every gate reads as right.** Three defects of that shape have
now been found, and each needed its own gate because each is invisible to the
others:

| Defect | Why nothing saw it | Gate | Shipped |
|---|---|---|---|
| One id for two organisms (*B. ovatus* on `NCBITaxon:821`, *Phocaeicola vulgatus*) | `id`↔`label` agree; only `preferred_term` dissents, and that legitimately differs KB-wide across NCBI renames | `shared_taxon_ids` — one id, two different named organisms, rank-gated | #425 (#292) |
| A plant id under a bacterial lineage (`NCBITaxon:169215`, *Bosea*, Amaranthaceae) | `ncbi_source_id == term.id`, and "Bosea" really is that id's label | `prokaryotic_lineage` — GTDB is prokaryote-only, so a non-prokaryotic id cannot carry a GTDB lineage | #436 (#365) |
| A class id where the genus has its own (*Accumulibacter* on `NCBITaxon:28216`) | Nothing is *false*; the id is merely coarser than the name | none — needs a curator call, see #419 | pending |

**Method note worth keeping.** All three were found by *reviewing a fix for a
neighbouring one*, not by a sweep. The generalisable move is: after correcting a
grounding, ask what class of error the correction belongs to and whether a
mechanical signal separates it from the legitimate cases. Where one exists
(rank, domain) it becomes a gate and needs no waiver list; where it does not
(#419), it stays a curation call and should be filed rather than automated.

**Also newly true:** `validate-references-all` is out of `qc` (#418) — it was
first in the chain, so `lint` and `test` never ran. `qc` now reaches lint, test
and every offline validator, and is green.

For which of these suit an autonomous `/goal` run, see
[NEXT_TASKS_LOOP.md](NEXT_TASKS_LOOP.md).

## Priority menu (reconciled 2026-07-30; re-reconciled after PR #274 merged)

Ranked, **actionable-now** work. Everything here was re-measured against the KB
on this date — three long-standing numbers below had drifted and are corrected
in place. Blocked items are listed further down so the gaps are explained, not
hidden; **do not** pull them off the shelf as "next".

**Changed since the first pass on this date:** PR #274 merged, so the workflow it
repairs now runs and **#273 is no longer gated** — it is the only actionable
thread with a live CI gate waiting on it. Reviewing and verifying #274 produced
three new issues (#280, #281, #282), all small and all folded into existing menu
rows rather than added as new threads.

| # | Item | Size | Why this rank |
|---|---|---|---|
| 1 | **GTDB grounding backfill** (#276, `ground-taxa-gtdb`) | L, mechanical | Largest unblocked gap in the KB and the only one needing nothing external |
| ~~2~~ | ~~**Network audit triage (#273) + the CLI fixes (#281, #282)**~~ | — | **DONE** — #281/#282 shipped earlier; #273 closed by PR #316 (2026-08-03) with #313 and #315. The gate is restored and both its branches verified live. |
| 3 | **Causal-edge curation, next batch** | M per record | Active thread with a worked method; highest scientific value per record |
| 4 | **Growth conditions for the 25 curatable ENGINEERED records** (#183 slice) | M | Less paywalled than #183 claims — 6 were never even attempted |
| 5 | **Redundant encoding in the network diagram (#270)** | S–M | Self-contained frontend work, fully specified |
| 6 | **Decide the #182 ontology remaps** | S | A curator decision, not an implementation task |
| 7 | **Auto-fetch the Unpaywall OA location (#259 slice)** | S | Self-contained; drops the manual `--from-file` step for OA-but-not-PMC sources |
| 8 | **Cross-Mech vendored-sync gaps (#278, #280)** | S | Two distinct defects in the same guard; worth one cross-Mech sweep, not three PRs |
| ~~9~~ | ~~**Inline the four dangling `[[wiki-links]]` (#277)**~~ | — | **DONE** (2026-08-07). Two were redundant with the prose beside them; the load-bearing one turned out to document a blocker that no longer exists, so `validate-terms-all` is now a CI gate. |

**Recommended next: #1, GTDB grounding.** It is the biggest coverage gap that
depends on nothing outside this repo — the mapping table is local
(kg-microbe `NCBI2GTDB.tsv.gz`) and the `ground-taxa-gtdb` skill already exists.
It needs no literature access, no curator judgment calls, and no sibling repo.
Measured 2026-07-30: **569/995 taxa (57%) carry `gtdb_classification`**, spread
as **91 records fully grounded, 140 partially, 72 with none**. The *partial* 140
are the sharpest problem — a single record where some taxa carry a GTDB
classification and others don't is internally inconsistent, and that is exactly
what a downstream KGX consumer will trip over. Finishing the partials first is
the cheapest way to make the field trustworthy. Note the skill also surfaces
GTDB reclassifications (NCBI *Agrobacterium deltae* → GTDB *A. leguminum*), so
this is a correctness pass, not only a coverage one.

**Row 2 is now done (2026-08-03, PR #316)** — and the reasoning recorded here
was half wrong, which is worth keeping rather than deleting. This file said #273
"splits into two halves", one mechanical and one needing **a curator to resolve
the 4 dangling ANME/SRB references**. There was no curator half. All four were
auditor false positives (#315): the record names the same NCBITaxon under a short
name on the interaction and a long one in `taxonomy`, and the auditor compared
the free-text names rather than the ids. Measuring before scheduling would have
caught it; repeating the issue's framing across this file and several PR bodies
did not. See the #273 section below for the full correction.

The `DISCONNECTED` policy call landed where this file predicted: warning
severity, reported but never gating.

### Numbers corrected this reconcile

- **Causal-edge coverage: 59/305, not "~65/304".** The "Causal-graph curation"
  section below overstated it. 246 records carry no `downstream` edge.
- **Records with no growth conditions: 80/305, not "52/295"** as issue #183
  states. But the shortfall is smaller than that sounds: **52 of the 80 are
  STABLE or PERTURBED** (34 + 18) field communities that legitimately have no
  cultivation conditions — all NATURAL-origin, though note **57** of the 80 carry
  `community_origin: NATURAL`, the extra 5 being NATURAL-origin records that are
  ENGINEERED in `ecological_state` and so counted in the 28 below. The split that
  matters is by `ecological_state`. The curatable slice is the **28 ENGINEERED**
  records, and even that includes three pure computational models
  (`BioModels_…`, two `KBase_…`) which honestly have none. Real target:
  **25 records** — see the #183 section, which names them.
- **GTDB coverage was never tracked here at all** — no section mentioned it
  despite the schema slot and skill both existing. Added as item 1.

### Blocked — keep, but never recommend as "next"

- **#259** (the non-OA remainder only) — sources that are in neither Europe PMC
  nor any OA location; there `cache_fulltext.py --from-file` is the honest escape
  hatch, not a gap to close. **The rest of #259 is not blocked** — most of the
  issue shipped in #260/#261 and the Unpaywall fetch is item 8 above. This entry
  used to read "general case: publishers that block programmatic download", which
  overstated it.
- **#183** (thin membership, `000274` + `000285`) — needs institutional
  full-text access. The *growth-conditions* half of #183 is **not** wholly
  blocked; see its section.
- **#30** — waiting on CultureMech / MediaIngredientMech schema; §2 records that
  this repo has no actionable remainder.
- **§1 `validate-terms-all`** — blocked, but not as uniformly as this entry used
  to claim. Per §1's own 2026-06-17 triage, roughly **14 of the 34** residuals
  (~9 CHEBI + 3 ENVO + 2 NCBITaxon) need a term that does not exist and that we
  cannot mint — those are the genuinely upstream-blocked ones. The **~12 obsolete
  GO ids need a curator-accepted repoint, not minting**, and §1 records one
  near-repoint already found (`CHEBI:86154` sodium metasilicate → `CHEBI:60720`
  sodium silicate, a generalisation, not applied). So the gate stays blocked
  overall — it fails on any unresolved row — but part of the 34 is decidable here.
- **Space-regolith, remaining 4** — membership is commercial or undefined, so
  members cannot be grounded to NCBITaxon. Revisit only if a follow-up study
  names them.

### In flight

**No work is in flight — PR #283 is this reconcile and nothing else is open.**
PRs #268, #274, #275 and #279 all merged 2026-07-31 UTC, clearing the batch.

- **PR #274** (#272) — **MERGED** (`d588f3d`). `network-quality.yml` parses and
  runs for the first time; **#273 is no longer gated** and is the top of the
  actionable CI thread. Verification is recorded in the CI-hygiene section below.
- **#199** stays open for two cosmetic items (hero gradient, filter placement). Its
  checkboxes were stale — the legend item and the stale-template item were both
  done but still unticked; reconciled on the issue 2026-07-30, so the issue and
  this file now agree.

### Cross-Mech note (advisory — sibling repos not edited)

The file header asks that cross-Mech items stay in sync with CultureMech / MIM /
TraitMech. Nothing changed in this reconcile touches the two designated
cross-Mech threads (§2 `#30`, §3 validator pin), so **no sync is owed**. One
observation worth passing on rather than acting on: **CultureMech and TraitMech
both ground taxa to NCBITaxon but neither tracks GTDB**, and neither mentions it
in its `NEXT_TASKS.md`. If #276 establishes a house pattern here, those two are
the natural next adopters — but that is their call, not a divergence this repo
introduced.

## 0. Element enum CHEBI groundings are wrong + ungated (found 2026-07-18)

**Trigger:** `MetalElementEnum.PALLADIUM` was grounded to `CHEBI:33373`
(*promethium atom*), not palladium — fixed to `CHEBI:33363` (PR #206). An audit
of the full `MetalElementEnum` + `RareEarthElementEnum` (`meaning:` id → current
ChEBI label, via the local `~/.data/oaklib/chebi.db`) then found **13 more wrong
groundings**, almost all in the rare-earth block:

| enum value | current (wrong) id → label | correct id (candidate) |
|---|---|---|
| INDIUM | CHEBI:49464 → *aluminium trifluoride* | CHEBI:49664 indium(3+) |
| LANTHANUM | CHEBI:32359 → *dodecanoyl group* | CHEBI:49701 lanthanum(3+) |
| CERIUM | CHEBI:32998 → *(not in build)* | CHEBI:48782 cerium(3+) |
| PRASEODYMIUM | CHEBI:49648 → *holmium atom* | CHEBI:229784 praseodymium(3+) |
| SAMARIUM | CHEBI:33376 → *terbium atom* | CHEBI:49890 samarium(3+) |
| EUROPIUM | CHEBI:30688 → *(not in build)* | CHEBI:49591 europium(3+) |
| TERBIUM | CHEBI:33374 → *samarium atom* | CHEBI:49902 terbium(3+) |
| DYSPROSIUM | CHEBI:49782 → *(in no CHEBI release)* | CHEBI:33377 dysprosium atom |
| HOLMIUM | CHEBI:49649 → *(not in build)* | CHEBI:49650 holmium(3+) |
| ERBIUM | CHEBI:49650 → *holmium(3+)* | CHEBI:33379 erbium |
| THULIUM | CHEBI:33377 → *dysprosium atom* | CHEBI:33380 thulium atom |
| YTTERBIUM | CHEBI:33378 → *(not in build)* | CHEBI:49980 ytterbium(3+) |
| YTTRIUM | CHEBI:49976 → *zinc dichloride* | CHEBI:49962 yttrium(3+) |

The pattern is off-by-one shifts within the CHEBI:333xx lanthanide block plus a
couple of digit transpositions — a copy/paste grounding error, same class as
PALLADIUM.

**Item 1 — fix the groundings — DONE (2026-07-18, PR #207).** All 13 REE/INDIUM
`meaning:` ids in `schema/communitymech.yaml` (both element enums) and the mirror
`REE_CHEBI_MAP`/`METAL_CHEBI_MAP` in `src/communitymech/metal_extraction.py` were
repointed and the datamodel regenerated. **Curation decision taken: ground REEs as
the `(3+)` cation** (matches every `description:` "X(3+) cation"); this also
normalised the previously-atom-grounded NEODYMIUM/GADOLINIUM/LUTETIUM/SCANDIUM to
their cation ids. Three lanthanides have **no `(3+)` term in ChEBI** — DYSPROSIUM
(CHEBI:33377 atom), ERBIUM (CHEBI:33379), THULIUM (CHEBI:33380) — so they stay
atom-grounded with descriptions annotated to say so. Re-audit: 0 mismatches;
validate-all + 197 tests green.

**Item 2 — close the systemic gap — DONE for the element enums (2026-07-18, PR
#208).** The root cause was that enum `meaning:` groundings are **not** covered by
any id↔label gate — `validate-products` only checks record-level
`term.{id,label}` pairs, so these drifted wrong undetected while the gated record
pairs stayed correct (spot-checked: `Ion_Adsorption_REE_Indigenous_Community.yaml`
uses the *correct* CHEBI:33377/CHEBI:49962). Added the guard test (PR #208, then
generalised in PR #209) — runs in the `validate-strict` pytest step (already a
blocking gate) with no network.

**Item 2b — generalise the guard — DONE (2026-07-19, PR #209).** A survey found
only **3 enums carry `meaning:` groundings** at all — `MetalElementEnum` (17
CHEBI), `RareEarthElementEnum` (16 CHEBI), and `CultivationSystemEnum` (1 OBI:
BIOREACTOR_UNSPECIFIED → OBI:0001046 "bioreactor"). (The `validate-terms-all`
blocker is about *data-level* `term.id` bindings across community files — a
different surface — so it does **not** block an enum-meaning guard.) Renamed the
test to `tests/test_enum_groundings.py` and made it **auto-discover** every
grounded enum from the schema, so a newly grounded enum/value is covered
automatically (or fails until registered in `EXPECTED`): (a) full discovered
`{enum: {value: meaning}}` must equal the frozen `EXPECTED`; (b) no two values
inside one enum share an id; (c) each id resolves to a non-obsolete term whose
canonical label fits (element name must appear for the element enums), per prefix,
skipped when that ontology's sqlite isn't cached locally. Covers CHEBI + OBI;
verified the label check flags all three historical bugs.

**Note (not the same task) — RESOLVED 2026-08-07, #277.** A full LinkML-native
schema gate over term.id *data* bindings (`just validate-terms-all` /
`linkml-term-validator`) was deferred because that tool has no exceptions
mechanism and failed on 34 curator-accepted residuals. The residuals were
cleaned up over time rather than waived — the last went in #350, which removed
the final obsolete `GO:0055114` instances and corrected 22 isolate terms. The
gate now passes **316 of 316 files, zero warnings, exit 0**, and is enabled as a
blocking step in `label-correspondence.yaml`. It was already in `just qc`.

(This passage previously deferred to `[[ontology-term-cleanup]]` /
`[[chebi-mislabels-backlog]]`, which are agent-memory links resolving to nothing
from a fresh clone — the whole of #277.)

**Impact:** shipped community records mostly ground REEs via their own (correct)
`term.{id,label}` pairs, so the KGX export from those is largely fine; the wrong
groundings live in the schema enum + `metal_extraction.py` map (any enum-driven
export/analysis inherits them). Low blast radius today, but a latent correctness
bug and a clear gate gap — now guarded for every grounded enum (CHEBI + OBI).

## 1. Phase-2 id↔label enforcement rollout (report-only → blocking)

**`validate-products` is now a BLOCKING gate** (done 2026-06-14):
`.github/workflows/label-correspondence.yaml` still generates + uploads the
drift report, then runs `just validate-products` as a failing step. Verified
locally: 5362 OK_CANONICAL, 184 OK_EXCEPTION, 0 errors (exit 0). The 34
curator-accepted residuals in `conf/id_label_targets.yaml` (`exceptions:`) all
resolve as OK_EXCEPTION (184 pair-instances across files).

**ENABLED 2026-08-07 (#277) — was: deferred as a blocking gate.**
linkml-term-validator (`--labels`) has NO exceptions mechanism, so it used to
fail on these residuals — it errored on obsolete `GO:0055114`
"oxidation-reduction process" and on the CHEBI mislabels needing minting. That
class is fixed (the last of it in #350), and the gate now passes 316 of 316
files, so it runs as a blocking step in `label-correspondence.yaml`.

Read the rest of this section as history, with one correction that matters: the
34 did not all get cleaned. Three still resolve to nothing in OAK
(`CHEBI:75315`, `GO:0070812`, `NCBITaxon:1807132`) and are still waived in
`conf/id_label_targets.yaml`. This tool passes them by *silently skipping ids it
cannot resolve*, not because they were fixed — so option 2 below is still
genuinely upstream-blocked, and the gate is green partly by blindness. It also
does not catch a nonexistent CURIE at all (#471).

**Partly closed 2026-08-07 (PR #473).** Engine B — which *does* report
`ID_NOT_FOUND` — now has a `data/isolates/*.yaml` target, so that defect class
is covered for the isolate records as well as the communities. It found one
immediately: `CHEBI:49782 "dysprosium(3+)"`, an id in no CHEBI release, in
`Methylobacterium_REE_Ewaste_Platform.yaml`. Note this was a *record-level*
`term.{id,label}` pair, not the enum `meaning:` in the table above — that
repoint landed 2026-07-18 in PR #207. The correction had been sitting in
`chebi_fix_apply.py`'s REPOINT map the whole time, unapplied, because the
script globbed `kb/communities` alone; it now sweeps the isolates and taxa too.
What stays open on #471: Engine A still cannot fail on an unresolvable id
(upstream in `linkml-term-validator`), and nothing pins the ontology release.

The original framing, kept because it is still the right analysis of what
enabling *would* have required:
  - mint/clean the 34 residuals (see chebi-mislabels backlog — 11 CHEBI need
    minted terms; obsolete GO terms; 2 absent NCBITaxon), then drop them from
    `exceptions:`; or
  - teach the LinkML gate to consume a shared waiver (a feature the vendored
    Engine-B script already has but linkml-term-validator does not).

**Triage 2026-06-17 (option 2 attempt):** re-checked all 34 residuals against the
CURRENT OAK snapshot (`/tmp/triage.py`). Finding is sharper (and worse) than
"needs minting": every residual id resolves to an UNRELATED entity in the current
build, and broad `runoak search` finds NO repoint target for the intended label —
i.e. the compound/environment is genuinely absent from ChEBI/ENVO, and the
placeholder id is semantically wrong. Examples: CHEBI:33104 "chromium(III)
hydroxide"→*hydridoarsenic*; CHEBI:34818 "humic acid"→*Leucomycin A8*; CHEBI:38292
"uranyl(2+)"→*nido-undecaborane*; CHEBI:89981 "yeast extract"→*LPS with O-antigen*;
ENVO:00000274 "soda lake"→*continental rise*; ENVO:01001442 "phyllosphere"→
*agriculture*; NCBITaxon:3050471 "Stenotrophomonas goyi"→*unclassified
Dissulfuribacter*. Only near-repoint found: sodium metasilicate (CHEBI:86154) →
CHEBI:60720 "sodium silicate" (a generalization, label changes; not applied).
**Conclusion: option 2 is genuinely upstream-blocked** — I cannot mint
ChEBI/ENVO/GO/NCBITaxon terms. (That conclusion stands; what changed in #277 is
that the gate no longer *needs* it, because the residuals it can see were fixed
and the three it cannot see are invisible to it. The three remain real.) The
real fixes are external: (a) submit the ~9 CHEBI + 3 ENVO + 2 NCBITaxon compounds/taxa as
term requests (ROBOT template / OBO issue), (b) repoint the ~12 obsolete GO ids to
current terms where a curator accepts a replacement, then (c) drop resolved
entries from `exceptions:`. The `exceptions` allow-list keeps `validate-products`
green meanwhile, but note these groundings are semantically wrong in the KGX
export (the id ≠ the labelled compound) — a data-quality item worth tracking.

## 2. Cross-repository environmental linking (issue #30)

**Scoping finding (2026-07-19):** most of #30's *schema* is already built — the
`RelatedMedia` / `RelatedIngredient` classes, `related_media` /
`related_ingredients` slots, `GrowthMedia.culturemech_id`, and
`GrowthMediaComponent.mediaingredientmech_id` all exist, and cross-repo **ID**
existence checks ship in `scripts/validate_cross_repo_ids.py`. The name-based
`scripts/link_growth_media.py` links growth_media → CultureMech recipes. What was
missing is the **ENVO-based** cross-repo layer (issue Use Cases 1–2): match a
community's `environment_term` against CultureMech `source_environment[].term.id`
and MIM `environmental_context[].environment_term`. Both sibling env fields now
exist (CultureMech 18 real records, MIM ~44); read siblings from local paths via
`COMMUNITYMECH_SIBLING_REPOS`.

**Item a — ENVO coverage dashboard — DONE (2026-07-19, PR #210).**
`src/communitymech/cross_repo_environment.py` (byte-prefiltered ENVO index across
the three repos, no network) + `scripts/env_coverage_dashboard.py` +
`just env-coverage`. First real run: **41 community ENVO terms, only 1 (soil) with
both media+ingredients, 34 with neither** — sibling ENVO fields are still sparse,
so the near-term value is showing *where* to populate. Offline unit tests in
`tests/test_cross_repo_environment.py`.

**Item b — ENVO-based media suggester — DONE (2026-07-19, PR #211).**
`scripts/suggest_related_media.py` + `just suggest-related-media`: for each
community, matches its `environment_term` against CultureMech
`source_environment` and emits paste-ready `related_media` blocks
(`relationship_type: ENVIRONMENT_ANALOG`, `shared_environment_term`,
`culturemech_id`), skipping media already linked via `related_media`/`growth_media`.
Suggestion-only (edits nothing). Over-generic environments (`ENVO:01001405`
"laboratory environment", ~110 communities) are excluded by default — `--include-generic`
to override — and the skipped count is reported (no silent drop). First real run:
**351 suggestions across 60 communities** (rhizosphere/sediment/compost/freshwater),
110 lab-only communities skipped. Verified a suggested block LinkML-validates when
pasted into a real record. Reuses `cross_repo_environment.culturemech_media_by_environment`;
tests in `tests/test_suggest_related_media.py` + `tests/test_cross_repo_environment.py`.

**Item c — ENVO-based INGREDIENT suggester — was DEFERRED (two blockers); both now
actioned (2026-07-19, PR #212).**

- **Blocker 1 (schema, ours) — RESOLVED.** Added `shared_environment_term` (Term,
  id-binding REQUIRED) to `RelatedIngredient`, mirroring `RelatedMedia`, so an
  environment→ingredient link is now expressible. Datamodel regenerated; verified a
  `related_ingredient` with `shared_environment_term` + `chebi_term`
  LinkML-validates; regression test in `tests/test_cross_repo_linking.py`.
- **Blocker 2 (MIM id scheme) — RAISED with MIM (MediaIngredientMech#119).**
  Investigation resolved the *facts*: MIM's canonical ingredient CURIE is
  **`MIM:<name>`** (2200 SSSOM subjects; `MIM:` expands to
  `.../data/ingredients/mapped/`), mapped to CHEBI/FOODON via SSSOM —
  **not** `MediaIngredientMech:NNNNNN` (that style exists only in two MIM
  `analysis/` reports and in zero canonical records / the unified mapping TSV). So
  CommunityMech's `RelatedIngredient.mediaingredientmech_id` pattern references a
  scheme MIM never adopted; its docstring now says so and points at #119. MIM#119
  asks MIM to confirm (a) `MIM:<name>` as the stable cross-repo id, (b)
  `environmental_context` durability/coverage, and (c) whether citing the
  ingredient's `CHEBI:` id (already supported by `RelatedIngredient.chebi_term`) is
  an acceptable equivalent link — the likely fast path.

**Ingredient suggester — DONE (2026-07-20, PR #220; MIM#119 CLOSED as answered).**
MIM confirmed: (1) `MediaIngredientMech:NNNNNN` is vestigial — drop the pattern;
(2) the equivalence-safe join is the ingredient's CHEBI term from MIM's SSSOM
**`skos:exactMatch`** rows (NOT the record `identifier`, NOT close/narrowMatch —
those would generalise); (3) `environmental_context` coverage is **10 records, not
~44** (a seawater/soil/sulfur cluster). `scripts/suggest_related_ingredients.py` +
`just suggest-related-ingredients` implement the CHEBI route accordingly:
`cross_repo_environment.mim_exactmatch_chebi` parses the SSSOM (exactMatch→CHEBI
only) and `mim_ingredients_by_environment` joins each `environmental_context`
record (`MIM:<file-stem>` subject) to it; emits `RelatedIngredient`
(`chebi_term` with the **canonical** ChEBI label + `shared_environment_term`), reads
env keys from `environment_term` + `modeled_environment`, supports `--subsumption`.
Real yield today: 1 suggestion (Sulfur CHEBI:26833 → the hot-spring mat community) —
data-limited by MIM's 10 context records, correct + scales. Supersedes draft PR #215.
**Vestigial-pattern drop — DONE (2026-07-20, PR #223).** Removed the
`^MediaIngredientMech:\d{6}$` pattern from **both** schema fields
(`RelatedIngredient.mediaingredientmech_id`, `GrowthMediaComponent.media_ingredient_mech_id`)
per #119 §1; descriptions mark the scheme vestigial/deprecated and point to
`chebi_term` as the join. Datamodel regenerated; a `MIM:<name>` value now validates.
**Validator retirement — DONE (2026-07-20, PR #224).** Removed the
`related_ingredients` / `mediaingredientmech_id` branch from
`src/communitymech/validators/cross_repo_ids.py` (+ the `MEDIAINGREDIENTMECH_ID_RE`
constant, the `--mediaingredientmech` script flag, and the vestigial pattern tests
in `test_cross_repo_ids.py` / `test_cross_repo_linking.py`). The validator now only
checks `related_media` CultureMech ids; ingredient linking joins on `chebi_term`
(covered by the id-label validator). A rename-stable MIM surrogate id would need its
own MIM issue if we later want to persist `MIM:<name>` as a key.
**Other follow-ups (grounding-quality):**
- **ENVO subsumption matching — DONE (2026-07-19, PR #213).** `suggest-related-media
  --subsumption` also matches media whose environment is an ENVO `is_a` *subtype*
  of the community's (e.g. "marine sediment" medium for a "sediment" community),
  via a locally-cached ENVO adapter (skips gracefully in CI). Ancestors are
  intentionally excluded (they'd match super-generic parents), and generic media
  envs (`ENVO:01001405`) are filtered from subtype expansion too. Current
  real-data yield is ~0 extra non-generic matches (CultureMech `source_environment`
  is too sparse to have `is_a`-subtype overlap yet) — the capability is correct and
  future-proofs as coverage grows. NB: some intuitive relations aren't `is_a` in
  ENVO (rhizosphere is *not* a subtype of soil), so those still won't match — an
  ontology limitation, not a bug.
- **`ENVO:01001405` over-application report — DONE (2026-07-19, PR #214).**
  `scripts/env_grounding_quality.py` + `just env-grounding-quality`: ranks
  community `environment_term` usage and flags **generic** (curated set incl.
  ENVO:01001405 "laboratory environment") and **over-applied** (>= `--threshold`,
  default 15) groundings for curator review; `--list` names the affected records,
  `--strict` exits 1 on any generic grounding. Report-only (edits nothing). Current
  state: **110 communities** on "laboratory environment" (GENERIC + over-applied)
  and 42 on "rhizosphere" (over-applied but legitimate). The generic set is shared
  with the suggester (`cross_repo_environment.GENERIC_ENVIRONMENT_TERMS`). (ENVO
  `is_a` depth was tried as a genericness signal and rejected — "laboratory
  environment" is deeper than "soil".)

- **Lab-env re-grounding via a new `modeled_environment` slot — IN PROGRESS
  (2026-07-19).** Rather than overwrite `environment_term` (which honestly records
  the *study setting*, often "laboratory environment"), a new **`modeled_environment`**
  slot on `MicrobialCommunity` (multivalued, optional, `EnvironmentDescriptor`,
  ENVO-grounded) captures the natural/applied habitat an engineered community
  derives from or represents. **DONE:** schema slot + test (PR #216); populated for
  the 23 triaged records (PR #217) — groundwater×2, anaerobic digester×3,
  bioreactor×3, regolith×4, dairy×4, intestine×2, marine×3, digestive-tract×1,
  AMD×1; the other ~67 de-novo cocultures keep only `laboratory environment`.
  Triage buckets REGROUND 18 / REVIEW 25 / LAB-KEEP 67. **Suggester now matches on
  `modeled_environment`** (PR #218): the media suggester's env keys are
  `environment_term` + every `modeled_environment`, so the 23 lab-env communities
  are no longer skipped (skip count 110 → 87) — they'll match media automatically as
  CultureMech populates `source_environment` for those habitats (0 today; data-limited,
  not logic-limited). **`docs/` page regen — DONE:** the 23 triaged records rendered in
  #221; the 4 later regolith records (000308–000311) rendered in **PR #239** (304 pages
  total; `modeled_environment → regolith` blocks render). The template already supports
  the slot, so future records render automatically. **Former "remaining (optional)" item —
  DONE (verified 2026-07-29):** applying `modeled_environment` matching to the ingredient
  suggester was already shipped with the suggester itself in PR #220 —
  `scripts/suggest_related_ingredients.py` reads `environment_term` + every
  `modeled_environment` (see its `_env_keys`). The note was stale, not pending.
  **§2 / issue #30 now has no actionable remainder in this repo**; further yield is
  data-limited by sibling coverage (MIM has 10 `environmental_context` records).

## 3. Cross-Mech validator pin guard — DONE (4-repo invariant)

**Current governance update (2026-08-25; supersedes the topology chronology
below):** reviewed `CultureBotAI/culturebotai-claw#133` makes
`CultureBotAI/culturebotai-claw` the canonical manifest and payload source.
CommunityMech is one of five pinned consumers. Shared changes land in claw first
and then roll to all five Mechs at one immutable claw commit. The older notes
below remain as incident history; their CultureMech-hub instructions are no
longer active.

**Done** (2026-06-15, culturebotai-claw#6 Option 1): the pin now covers the full
vendored set via a `VENDORED_IDLABEL_FILES` manifest — the validator `.py` **plus**
the two byte-identical shared tests (`tests/test_id_label_empty_adapter.py`,
`tests/test_id_label_unknown_prefix.py`). CommunityMech's two test copies had
drifted (cosmetic: a `not_empty`→`NOT_empty` rename + whitespace); resynced to the
CultureMech/MIM canonical bytes (`55a432e0…` / `f01d2264…`) and re-pinned, so all
three Mechs now share an identical 3-line `.sha256` manifest. CI's `sha256sum -c`
step enforces all three; `verify-validator-pin` passes; the 17 vendored tests pass.
`conf/id_label_targets.yaml` stays **unpinned** (intentionally per-repo).

**Phase 0 vendored-sync — DONE (2026-07-21, PR #235 + #236).** #235 brought
`scripts/validate_id_label_correspondence.py` to fleet-canonical `1775583c`
(merges TraitMech's `_LABEL_CACHE`/`_FORMULA_LOOKUPS` clear-in-`run()` fix +
CultureMech's drop of `ID_OUT_OF_RANGE` from waivable exceptions) and refreshed
the validator `.sha256` line; #236 synced `chem_formula.py` (R-prefixed elements +
hydrate separators, a different pin line). Prerequisite for replacing the
self-referential per-repo pin with a shared-reference cross-repo drift check
(plan: `culturebotai-claw/.../vendored_sync_action_plan_2026-07-21.md`).

**Shared-reference drift check — DONE (2026-07-21, PR #238).** The `vendored-sync`
CI job now runs `scripts/check_vendored_sync.sh`, diffing the five vendored files
against `CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>` — the reference
lives in another repo, so a one-copy edit fails CI (the flaw the self-pin missed).
The canonical hub is covered by CultureMech's nightly `vendored-fleet-audit.yml`.
The self-generated sha256 pin (`verify-/refresh-validator-pin`, the
`VENDORED_IDLABEL_FILES` manifest, `scripts/.validate_id_label_correspondence.sha256`)
was then retired (Phase 2 step 2d). `schema-pin` is a separate set, unaffected.

**Settled architecture — CultureMech stays the hub (confirmed 2026-07-30).**
Recorded because the alternative was tried and reverted, and a stale version of
it has been circulating in sibling backlogs: claw PR #21 ("Enforce id-label
vendored files match claw canonical") moved the canonical source into
culturebotai-claw on 2026-07-22 and was **reverted by claw PR #22** on 2026-07-25
as off-model for claw-as-mirror. The settled design (claw #19, restated in #22)
is that **CultureMech is the hub and `claw/shared/idlabel/` is a passive mirror
of it**, with both directions covered: spokes == hub via CultureMech's
`scripts/audit_vendored_fleet.sh` (nightly `vendored-fleet-audit.yml`), and
mirror == hub via claw's `matches-hub` job, which claw PR #24 put on a nightly
schedule (2026-07-25, closes claw #23) — until then it fired only on claw-side
changes and so could never notice the hub moving. So: do **not** repoint
`CANON_REPO` or bump `.vendored_canon_ref` to a claw commit. Any note that this
is "blocked on claw being made public", or that claw Actions fail on exhausted
runner minutes, is stale — claw is public, that blocks nothing now, and
its scheduled runs were green daily 2026-07-25 through 2026-07-30. **CommunityMech
never carried that claim** (verified 2026-07-30: `CANON_REPO` here is
`CultureBotAI/CultureMech` and `.vendored_canon_ref` is `6be694f3`, matching MIM
and TraitMech); this paragraph guards against re-proposing it rather than
correcting anything.

**`check_vendored_sync.sh` drift — RESOLVED; but the script itself is unguarded.**
TraitMech's backlog flagged this script as having drifted specifically in
CommunityMech. It has since converged: MIM, TraitMech and CommunityMech all carry
**byte-identical** copies (sha256 `f05b5ad6…`) against the same
`scripts/.vendored_canon_ref` = `6be694f3`, and TraitMech's own "Re-converge
drift check on CultureMech hub" (TraitMech #182, alongside CommunityMech #247 and
MIM #157) is what closed it. Nothing to do here.

**Remaining gap this surfaced — the enforcer is outside the invariant it
enforces.** Neither guard covers `scripts/check_vendored_sync.sh` or
`scripts/.vendored_canon_ref` themselves. The hub's `audit_vendored_fleet.sh`
compares five vendored files plus `mech_shared.yaml` across all four repos, and
each spoke's check compares the same set — but the script doing the checking
exists **only in the three spokes and never in the hub**, so there is no
canonical copy to diff it against. The three are identical today; nothing keeps
them that way, and a one-copy edit to the checker would go unnoticed by exactly
the mechanism designed to catch one-copy edits. Two ways to close it: vendor the
script into CultureMech so it joins `FILES` in both scripts, or teach
`audit_vendored_fleet.sh` a spoke-only list that cross-compares the three copies
against each other. Low effort, and it is the same class of gap as the ungated
enum `meaning:` groundings in §0 and the palette↔enum gap fixed in #268.
**Filed as #278**, with the verification table (all three spokes at sha256
`f05b5ad6…`, hub absent) recorded there.

**A second, separate hole in the same guard — #280.** Where #278 is about *what
is compared*, #280 is about *when the comparison runs*. The `vendored-sync` job
lives in `.github/workflows/label-correspondence.yaml` behind a `paths:` filter
that is **narrower than the list of files the job diffs**, so a PR touching only
the unlisted ones never fires the check. Verified 2026-07-30 against this repo:

| file compared by `check_vendored_sync.sh` | in `trigger_paths`? |
|---|---|
| `scripts/validate_id_label_correspondence.py` | yes |
| `src/communitymech/schema/mech_shared.yaml` | yes, via `src/communitymech/schema/**` |
| `scripts/chem_formula.py` | **no** |
| `tests/test_id_label_empty_adapter.py` | **no** |
| `tests/test_id_label_unknown_prefix.py` | **no** |
| `tests/test_id_label_plausibility.py` | **no** |

So **4 of the 6** are unguarded at PR time, as are `check_vendored_sync.sh` and
`.vendored_canon_ref` themselves. This is a PR-time hole, not an unguarded one —
CultureMech's nightly `vendored-fleet-audit.yml` still catches divergence within
a day, so the realistic failure is a vendored edit merging green and surfacing
against `main` the next morning: confusing to attribute, not silent corruption.
CommunityMech is better off than TraitMech here, whose filter misses
`mech_shared.yaml` too (TraitMech#184). **Neither issue subsumes the other** and
fixing one leaves the other open, though one PR will likely close both. Best fix:
derive the `paths:` filter from the same source `check_vendored_sync.sh` reads,
rather than hand-listing — hand-listing is precisely the failure this is an
instance of. `conf/id_label_targets.yaml` stays out of the vendored set **by
design** (per-repo adapters/targets/exceptions) and is already in `trigger_paths`
on its own merit. Worth one cross-Mech sweep rather than three independent PRs.

Update (2026-06-15): **TraitMech has now joined** — the trio is a **4-repo
invariant**. TraitMech vendored the validator + tests byte-identical (same
`142bbe1…` / `55a432…` / `f01d22…` manifest) and enforces a blocking
`validate-products` gate (TraitMech PR #110 Phase 1, PR #111 Phase 2 — 14 wrong
CURIEs in `node_grounding.tsv` fixed, gate green). The pin invariant now covers
CultureMech, MIM, CommunityMech, and TraitMech.

Follow-up (2026-06-15): the resync reintroduced the canonical test bytes
(`test_NOT_empty_*`, long asserts) which violate CommunityMech's ruff (N802/E501)
and black — breaking the `lint` CI gate (a conflict between the byte-pin and the
local style gate). Resolved by EXCLUDING the two vendored test files from both
ruff and black in `pyproject.toml` (they are externally-canonical and pin-locked;
local restyling would break the pin). `lint` + `verify-validator-pin` are both
green again. NOTE for sibling Mech repos: if any also run a ruff/black gate, apply
the same exclude.

## Per-community network rendering + CI hygiene (2026-07-30)

Started from the last remaining in-repo item on the **web design review (#199)** —
the other four open issues (#259, #183, #182, #30) are all blocked on things this
repo cannot supply (publisher access, curator judgment, sibling-repo schema).

**Legend renders only the types present — DONE (2026-07-30, PR #268).** The
network legend in `src/communitymech/templates/community.html` was a static block
of ten rows (a Taxon swatch plus all nine interaction types) emitted on every
page regardless of content. Of the 300 pages with a network, only 857 legend rows
were meaningful — 120 pages needed 2 rows, 108 needed 3, 67 needed 4, 5 needed 5 —
so ~2,100 rows advertised categories the graph did not contain. The nine colours
now live in one `interaction_legend` list driving **both** the legend and the
script's `interactionColors` map (previously two hand-maintained copies), the SVG
`<desc>` lists the actual types, and a typeless interaction gets the grey "Other"
swatch the script already draws it with (one record,
`SynCom_Sesame_Flavor_Baijiu_Fuqu_13Genus`). The second #199 item — delete
`templates/community.html.j2` — was **already done**; note the surviving
`src/communitymech/templates/community.html.j2` is a **different, live** file
driving `just gen-community-pages`, so do not delete it. **#199 stays open** for
its two cosmetic items (hero gradient, filter placement).

**Palette was not colourblind-safe — DONE (2026-07-30, PR #268, issue #269).**
The nine interaction colours never got the CVD treatment PR #198 applied to the
UMAP. Measuring CIE ΔE under simulated protanopia/deuteranopia
(Viénot–Brettel–Mollon), **10 of 55 swatch pairs sat below ΔE 15**. Two mattered:
COMPETITION `#ef4444` / PREDATION `#dc2626` were **ΔE 10.7 apart in *normal*
vision** (a plain legibility bug, not just accessibility), and MUTUALISM/SYNTROPHY
collapsed to **ΔE 4.1 under deuteranopia** — the 2nd and 3rd most common
interaction types (187 and 130 occurrences). Full-set minimum went 0.0 → **15.4**
(0.0 because taxon and MUTUALISM shared `#3b82f6`; a taxon circle and a mutualism
rectangle were the same colour). Semantics kept where they didn't conflict
(cross-feeding green, mutualism blue, syntrophy purple, competition red);
predation moved off red, niche partitioning off teal. **Curation note:** the
taxon/"Other" neutrals must be re-picked *with* the hues, not after — the first
candidate plum for PREDATION landed ΔE 6.5 from the grey "Other" swatch.

**Palette↔enum gate — DONE (2026-07-30, PR #268, issue #271).** Nothing tied the
template palette to `InteractionTypeEnum`; a tenth enum value would have rendered
silently grey on every page without failing anything — the same class of gap as
the enum-`meaning:` groundings in §0. `tests/test_network_palette.py` asserts
exact enum coverage and pins the ΔE floor, in the blocking `validate-strict`
pytest step, no network. Mutation-verified: restoring the old reds fails 4 tests,
dropping a type fails the coverage test.

### Still open from this batch

1. **Redundant (non-colour) encoding for interaction type (#270).** Every
   interaction is the same rounded rectangle, so colour is the *only* channel
   separating nine types. That is past what colour can carry: reaching ΔE ~30
   needs an aesthetically extreme set that collapses back to ΔE 5–9 if any single
   colour shifts, and tritanopia still merges two of them — **there is no
   nine-colour set safe under all three deficiency types.** `community_umap.html`
   already solves this with a `symbolScale` (its legend is literally "Legend
   (Color + Shape)") and gets away with a ΔE 6.9 palette because colour isn't
   load-bearing. Options: `d3.symbol()` per type, a letter inside each rect, or
   varied stroke style. This is the real fix; the palette swap only raised the floor.
2. **`network-quality.yml` triage (#273), gated behind PR #274.** See below.

**`network-quality.yml` had never run — DONE (2026-07-31, PR #274, issue #272).** GitHub
could not parse the file, so all 15 most recent runs failed in **0 seconds** and
the network audit never executed once. Tell-tale: the Actions API lists it under
its *path* rather than its `name:`, unlike every other workflow. Three defects,
only the first visible: (a) lines 139–150 were a JS template literal at column 0,
outside the `script: |` block scalar — indenting them would have fixed the parse
*and* baked 12 spaces into every line of the posted comment, so the message is now
array-joined (that step is dropped outright); (b) `secrets.ANTHROPIC_API_KEY` in
three step-level `if:`s, where the `secrets` context is unavailable — now a
job-level `env`; (c) `Generate detailed report` / `Upload audit reports` /
`Comment on PR` guarded by `failure()` while the audit step sets
`continue-on-error: true`, which keeps the job green and leaves `failure()`
permanently false — **even with the file parsing, none of those steps would have
run.** Now keyed off `steps.audit.outcome`.

Two judgment calls in #274, both revisitable: the audit **reports without
failing** (see #273), and `suggest-repairs` is **`workflow_dispatch`-only** — it
calls the Anthropic API for up to 20 records and previously fired automatically on
every audit failure, which given the standing findings means every push.

**A fourth defect, found reviewing #274 before merge.** The reporting-only job
still went red on the one input it most needs to handle. `audit-network` exits
**2 and writes no report** when one community YAML fails to parse (issue #281 —
a single bad file aborts the loop over all 305). `steps.audit.outcome` is
`failure` there exactly as for real findings, so the job ran `head -c 60000`
against a file that does not exist; `head` exits 1, GitHub runs `run:` steps under
`bash -e`, and the step failed — a red "reporting-only" job whose summary claimed
findings and showed none. There are **three** outcomes, not two:

| | exit | report | treatment |
|---|---|---|---|
| clean | 0 | written | "no issues found" |
| findings | 1 | written | reporting-only, per #273 |
| **crash** | 2 | **absent** | **fails the job, loudly** |

The summary now branches on all three and cannot fail in any of them; a final step
fails the job only in the crash case, placed after the reporting steps so the
summary is written first. The PR comment is `continue-on-error` (a fork PR gets a
read-only token, and a failed comment must not redden a job whose premise is that
it does not fail).

**Verified live, not by inspection (2026-07-31).** GitHub now registers the
workflow under its `name:` — "Network Quality Check" — instead of its path, which
was the tell-tale that it never parsed. A manual `workflow_dispatch` run
([30604391167](https://github.com/CultureBotAI/CommunityMech/actions/runs/30604391167))
**succeeded: the first successful run in this workflow's history.** The audit job
stayed green while reporting the 26 standing findings; `Generate Repair
Suggestions` was **skipped** (no API spend); `Comment on PR` and `Fail if the
audit could not run` were both correctly skipped; and the artifact downloaded
clean, containing the 4 ANME/SRB dangling references.

**Two CLI defects fell out of that verification**, both small and both belonging
with #273's pass rather than on their own:
- **#281** — one unparseable community YAML aborts the whole audit, so the other
  304 records go unchecked *and* no report is written. Fix: catch per file and
  record the parse failure as a finding against that record. Composes with the
  severity levels #273 proposes — a parse failure is unambiguously error-severity.
- **#282** — the report labels findings `UNKNOWN_SOURCE` under Python 3.10 (CI)
  but `IssueType.UNKNOWN_SOURCE` under 3.14 (local venv), because `str`-mixin enum
  `__format__` changed in 3.11. Found only by diffing the CI artifact against a
  local run. Now user-visible, since the workflow publishes that report as an
  artifact and pastes it into PR comments. One-line fix (`.value`), worth a test
  pinning the format.

**#273 — DONE (2026-08-03, PR #316), together with #313 and #315.** The gate is
restored: the audit carries error/warning severity, `--check-only` exits 3 on
error-severity findings and 1 on warnings, and `network-quality.yml` fails on the
former while only reporting the latter. `audit-network --json` is fixed (it
printed the human report to stdout ahead of the JSON). Both branches of the gate
were exercised live on PR #316 — a temporary canary commit breaking one
`downstream.target` turned the job red at `Fail on broken references`, and the
revert turned it green again.

**The premise recorded here was wrong, and this is the correction.** The "4
genuine dangling references" in `ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia`
were **auditor false positives**, not curation debt — filed and fixed as #315.
That record writes `ANME-1` on an interaction and `ANME-1 (anaerobic
methanotrophic archaea, clade 1)` in `taxonomy`, for the same
`NCBITaxon:588814`. `preferred_term` is free text on purpose, so a paper's own
name survives an NCBI rename; the auditor matched participants on that string
alone, so every such pair looked dangling. Measured across the whole KB: **4
name-mismatch-but-id-present, 0 genuinely absent.** No curator pass was needed
and none was done. Participant resolution is now name first, ontology id only as
a fallback and only when exactly one taxonomy entry carries it — the precedence
matters in both directions, since id-first collapses `Lotus_LjSC3`'s three
strains (all on `NCBITaxon:68287`, no strain-level NCBI term) onto one entry.

The **`DISCONNECTED` policy question** is settled the way this file predicted:
warning severity, reported but never gating. 19 stand, across 8 records.

**#313 came with it.** `DANGLING_EDGE`/`DANGLING_ANCHOR` — a causal
`downstream.target` or a `discussions.attaches_to` anchor naming an interaction
that does not exist — were written in PR #260 but lived only in
`scripts/audit_network_integrity.py`, which no recipe or workflow ran. Restoring
a hard gate over a checker blind to them would have baked the gap in, which is
why the two were done together. Both detectors are ported into the module, the
orphaned script is deleted, and each was canaried by injecting a break into a
copy of the KB. The live KB has zero, since #264 fixed all 14.

Audit total: **23 → 19**, all warnings. Error-severity findings: **0**.

## GTDB grounding backfill (issue #276; new section 2026-07-30)

**Priority-menu item 1.** The schema has carried
`TaxonomicComposition.taxon_term.gtdb_classification` (range `GtdbClassification`)
and the repo has shipped the `ground-taxa-gtdb` skill for some time, but coverage
was never measured or tracked here, so it has been filled in opportunistically
during other curation passes and is now uneven.

**Measured 2026-07-30:** `569/995` taxa (57%) carry a `gtdb_classification`,
distributed as **91 records fully grounded, 140 partially grounded, 72 with
none** (the remaining 2 have no `taxonomy`).

**Why the 140 partials come first.** A record where some taxa carry a GTDB
classification and others don't is internally inconsistent in a way that is worse
than uniformly absent: a downstream KGX consumer cannot tell "not grounded" from
"no GTDB equivalent exists". Finishing the partials converts the field from
"sometimes populated" to "populated where a mapping exists", which is the state
it needs to be in before anything queries it.

**Why it's the top pick.** Nothing external blocks it. The mapping table is local
(kg-microbe `NCBI2GTDB.tsv.gz`), so there is no literature access, no curator
judgment, and no sibling-repo dependency — the three things blocking most of the
rest of this backlog. It is also a **correctness** pass, not only coverage: the
skill flags GTDB reclassifications and renames (NCBITaxon *Agrobacterium deltae*
→ GTDB *Agrobacterium leguminum*), so filling it in surfaces taxonomy drift that
is currently invisible.

**Method:** `ground-taxa-gtdb` resolves an NCBITaxon id (or species name) to its
canonical GTDB CURIE, taxon name, full lineage and mapping confidence, and emits
a ready-to-paste `gtdb_classification` block. Existing records show the expected
shape — see `Maize_Root_Simplified_Community.yaml`, whose entries carry
`gtdb_id` / `gtdb_taxon` / `gtdb_lineage` / `ncbi_source_id` /
`majority_fraction` / `is_reclassified` / `mapping_source`.

**Suggested order:** the 140 partials (finish what's started), then the 72 with
none, largest/most-cited records first. Worth a gate afterwards so new records
don't reintroduce partial grounding — the same shape as the enum guard in §0 and
`tests/test_network_palette.py`.

## Growth conditions + thin membership (issue #183; section added 2026-07-30)

**Priority-menu item 4.** #183 was filed as two gaps left over from the #180
deep-research passes, both scoped as "resolvable only with institutional
full-text access". Re-measuring on 2026-07-30 shows that framing holds for one
half and is too pessimistic for the other, so the two are separated here.

**Growth conditions — the issue's own number is stale.** #183 says "52/295
records still have no `growth_media`/`cultivation_setup`"; the current count is
**80/305**. The gap is smaller than that sounds: **52 of the 80 are STABLE or
PERTURBED** (34 + 18) field communities with no cultivation conditions to record.
The split is by `ecological_state`, not `community_origin` — 57 of the 80 are
NATURAL-origin, the extra 5 being NATURAL-origin records that are ENGINEERED in
state, so they belong with the curatable set rather than the field communities.
That leaves the **28 ENGINEERED** records, of which three are pure
computational models that honestly have none —
`BioModels_MODEL2310020001_Mouse_Metaorganism_Model`,
`KBase_Models_for_Zahmeeth_Original_PLOS`, `KBase_ORT_Workflow_Community_Model`.
**The real target is 25 records:**

`Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment`,
`Bacillus_Bradyrhizobium_Straw_Humification_SynCom`,
`Bayan_Obo_REE_Tailings_Consortium`,
`Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding`,
`Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium`,
`Cyprus_Copper_Sulphide_Bioleaching_Consortium`,
`Legume_Rhizobia_Mars_Simulant_Symbiosis`, `Mars_Meteorite_EETA79001_Growth_Panel`,
`Mars_Regolith_Cyanobacteria_Biofertilizer_Panel`,
`Miscanthus_REE_Tailings_Nitrogen_SynCom10`,
`Moss_Microbe_Complex_Regolith_Biofertilizer`,
`PSY_Transgenic_Rice_Rhizosphere_Methane_Community`,
`Peanut_Seed_Bacterial_CS_SynCom`, `Pinus_armandii_Endophytic_Biocontrol_SynCom`,
`Pleuromutilin_Degrading_Artificial_Consortium_5_Strain`,
`Populus_Salt_Tolerant_SynComs`, `Rice_Acid_Soil_Bioinoculant_SynCom`,
`Rifle_Aquifer_Bioanode_EET_Community`,
`Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture`,
`Suillus_Bacillus_Thiamine_Ectomycorrhizal_SynCom`,
`SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience`,
`SynCom_Pseudomonas_Rahnella_Artemisia_Phytoremediation`,
`Thiocyanate_Afipia_Thiobacillus_Bioreactor_Community`, `Tomato_Oxylipin_SynCom3`,
`Wheat_Straw_Biogas_Pretreatment_SynCom`.

**How much of that is really paywalled — measured 2026-07-30.** Checking each of
the 25 against `references_cache/`: **1** has real full text
(`Mars_Meteorite_EETA79001_Growth_Panel`, `PMID_38665180.txt`, 56 KB), **18** have
an abstract stub only (0.8–5.4 KB), and **6 have nothing cached at all** —
`Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium`
(PMID:42343824), `Pinus_armandii_Endophytic_Biocontrol_SynCom` (PMID:42322490),
`Pleuromutilin_Degrading_Artificial_Consortium_5_Strain`,
`Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture`
(PMID:42285537), `SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience`
(doi:10.1016/j.rhisph.2025.101142) and
`SynCom_Pseudomonas_Rahnella_Artemisia_Phytoremediation`. The 6 have never been
*attempted*, which is different from being paywalled — running
`cache_fulltext.py` on them is the cheapest next step in this whole section and
needs no access anyone lacks.

**Thin membership — genuinely blocked.** Two records whose sources name only
functional groups, so `taxonomy` is empty or domain-level:
`CommunityMech:000274` (Multi-stage AD SynCom-YSJ/-J, *Bioresour. Technol.*,
closed access) and `CommunityMech:000285` (Chlorella + biogas-slurry SynCom,
grounded only at *C. sorokiniana* + domain Bacteria). Both need member taxa
(NCBITaxon + GTDB) from Methods-level text nobody has retrieved yet.

**Next action, in order:** (1) curate `Mars_Meteorite_EETA79001_Growth_Panel`
from the full text already cached — it needs nothing anyone has to fetch; (2) run
`cache_fulltext.py` across the 6 with no cache and the 18 abstract-only ones, a
mechanical pass that separates genuine paywalls from never-attempted; (3) curate
whatever full text lands, with `add-growth-conditions`. Only what survives step 2
belongs on the blocked list, recorded per record with its reason rather than in
bulk. #183's stale "52/295" is worth correcting on the issue at the same time.

## Ontology remap refinement (issue #182; section added 2026-07-30)

**Priority-menu item 6.** A curator decision, not an implementation task — no
tooling is missing, someone has to choose per row.

The #180 id↔label cleanup cleared 167 drift rows by remapping each to the nearest
**valid** ontology term. That made the gate green, but some choices are
deliberately broad or approximate, in two kinds:

- **Obsolete-GO remaps**, where GO offers no official replacement. The one that
  is arguably wrong on type grounds rather than merely broad is `GO:0055114`
  "oxidation-reduction process" → `GO:0016491` "oxidoreductase activity" — a
  biological-process → molecular-function shift. The rest collapse to generic
  parents or near neighbours: `GO:0071704` → `GO:0008152` metabolic process;
  `GO:1901575`/`GO:0019439` → `GO:0009056` catabolic process; `GO:0051704` →
  `GO:0044419` interspecies-interaction process; `GO:0051238` → `GO:0140487`
  metal ion sequestering activity; `GO:0015103` → `GO:0008509`.
- **Bucket A** — the intended term is absent from the ontology, so the row was
  remapped to the nearest existing term with the specific concept retained in
  `preferred_term`: lead/zinc sulfide → `CHEBI:46718` sulfide salt; organic
  matter → `CHEBI:50860` organic molecular entity; humic acid → `CHEBI:64709`
  organic acid; yeast extract → `CHEBI:60004` mixture; phyllosphere →
  `ENVO:01001001` plant-associated environment; anaerobic environment →
  `ENVO:01001825`; *Stenotrophomonas goyi* → `NCBITaxon:40323` (genus).

**Not the same surface as §1**, and the two are easy to conflate. §1's 34
`exceptions:` residuals are rows that were **never** remapped — they still carry
a placeholder id resolving to an unrelated entity, and they are upstream-blocked
because the intended term does not exist anywhere. #182 covers rows that now
resolve to a real, correct-but-broad term. Nothing blocks #182; it is simply
undecided.

**Options per row** (from the issue): accept as-is, since `preferred_term` keeps
the specificity; pick a better GO/CHEBI/ENVO term; request or mint the intended
term (e.g. via METPO); or drop the annotation where it has been generalised far
enough to carry no information. **Next action:** settle the `GO:0055114` BP→MF
case first — it is the only one asserting something of the wrong *type* — then
sweep the remainder as a single curator pass.

## DOI full-text retrieval — mostly shipped (issue #259; section added 2026-07-30)

**Correction to how this has been carried.** #259 has sat on the blocked list as
"publishers that block programmatic download", but most of what the issue asked
for shipped in PRs #260/#261, and the part that remains is not upstream-blocked.

**Shipped.** `scripts/cache_fulltext.py` now takes a DOI as well as a PMID
(`scripts/cache_fulltext.py doi:10.1128/spectrum.00941-23`), resolves it against
Europe PMC by `DOI:"<doi>"` — which covers OA papers holding a PMC record but no
PMID, the exact case the issue was filed on — and writes to
`DOI_<doi with / → _>.md`, the cache filename the reference validator already
reads, appending under the same marker so re-runs stay idempotent. `--from-file`
ingests a curator-supplied PDF or HTML; that is how the Li 2024 *Water* paper
landed in #261.

**Still open, and actionable (menu item 8).** When Europe PMC has no full text,
Unpaywall is queried only to **name** the OA location — the script reports
"retrieve by hand" and stops rather than fetching it, so an OA-but-not-PMC source
still costs a manual round trip. Automating that fetch is self-contained work in
this repo. Two things to know before starting: the lookup needs `UNPAYWALL_EMAIL`
set or it does not run at all, and the script still refuses to start unless an
abstract cache already exists for the reference.

**Genuinely blocked remainder:** sources in neither Europe PMC nor any OA
location. There `--from-file` is the honest escape hatch, and the current
"report and skip, never fabricate" behaviour is the right one to preserve.

## Adopt DisMech knowledge-gaps + datasets + QC dashboard (claw#7)

Coordinated cross-Mech adoption of DisMech's domain-general features. Full plan,
locked decisions, and DisMech schema references live in culturebotai-claw#7 (the
shared, pinned LinkML module is authored once and vendored across all four Mechs).
This repo's slice — **ALL DONE** (reconciled 2026-07-21; the section had gone
stale marking the last two "pending" when they had already shipped):
- Knowledge gaps — **DONE (2026-07-20, PR #226).** Added the `discussions` slot
  (broad `Discussion` supertype; `kind` incl. KNOWLEDGE_GAP / OPEN_QUESTION /
  CONTROVERSY / CURATION_TODO) to `MicrobialCommunity`, imported from the shared
  module, with `attaches_to` anchors bound to `ecological_interactions#…`. First
  real use: a KNOWLEDGE_GAP block in `Cellulose_Methane_Quad_Culture_SynCom`. The
  standing **`knowledge-gap-scan` recipe** (Europe PMC, free; shared
  `kg_microbe_kgscan` in claw; `conf/kgscan_config.yaml`) shipped in **PR #166** —
  dry-runs to `reports/knowledge_gap_scan.{json,md}`, `--apply` seeds
  `Discussion(kind=KNOWLEDGE_GAP)`.
- Datasets — **DONE (PR #163).** The shared Discussion + Dataset module was
  adopted and `associated_datasets` migrated from the former local
  `AssociatedDataset` to the canonical shared `Dataset` (mech_shared.yaml). No
  records use the old fields; the 149 records with `associated_datasets`
  LinkML-validate against the shared class. `DatasetTypeEnum`/`DatasetRepositoryEnum`
  come from the shared module.
- QC dashboard — **DONE (PR #165).** `just gen-qc-dashboard` (shared
  `kg_microbe_qc` generator in claw; `conf/qc_config.yaml`) renders
  `dashboard/index.html` + `dashboard/coverage.png`. Current run: 304 records,
  13 slots, 0 FAIL, overall 75.7% coverage. Regenerate periodically to track the
  growing record set.

## Causal-graph curation over ecological_interactions (in progress)

New capability built this session: the `deep-research-community` skill gained a
**causal-edge mode** (scoped to one community at a time) that runs an Edison
PaperQA3 causal-graph template and returns node/edge/DOT artifacts under
`research/communities/<slug>-*-causal-artifacts/` (gitignored). Curated records
get directed `downstream` edges on their `ecological_interactions` (and, where the
causal branch has no taxon↔taxon `interaction_type` home, `environmental_factors`
for chemical perturbations). Supporting work: `templates/community_causal_graph_research.md`
(PR #225), `scripts/cache_fulltext.py` for OA full-text snippet validation (PR #227;
**cache-path fix PR #230** — append to the file the reference validator reads,
`PMID_<id>.md` when present else legacy `.txt`).

**Done so far:** `Cellulose_Methane_Quad_Culture_SynCom` (#226; + acetate→CHEBI:30089
in #228), `Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy` (#229),
`ANME_SRB_Marine_Methane_Seep_Consortium` (#230),
`Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture` (#243; CommunityMech:000190,
syntrophic loop 1→2→3→1 + negative product-inhibition edge from the Edison graph on
PMID:30038609), `Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture` (#246;
CommunityMech:000268, reversible magnetite-"battery" loop 2⇄3 + both half-reactions →
battery, PMID:25814583), `ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model` (#249;
CommunityMech:000176 — conservative: full text unretrievable, so 2 directly-implied
donor→partner edges + a KNOWLEDGE_GAP discussion, modeled-limitation node left isolated).
**Syntrophy/DIET batch (#251):** `Dehalococcoides_Syntrophomonas_TCE_Dechlorination_Coculture`
(000183, 2 edges), `Trichococcus_Syntrophomonas_Methanospirillum_Butyrate_Coculture`
(000188, 2 HYPOTHESIZED mediator edges + KG), `Syntrophomonas_Methanococcus_Butyrate_Growth_Coordination_Coculture`
(000189, 1 edge + KG), `DIETsimp_Lignocellulose_to_Methane_DIET_Consortia` (000297, NO edge
justified — parallel proposed DIET pathways — KG only). The 6 already-wired matches
(000031–033 DIET, 000068–070 syntrophies) were left as-is. **59/305 records carry `downstream`
causal edges** (re-measured 2026-07-30; this line previously read "~65/304",
which overstated it — 246 records have no causal edge at all).
**Next:** continue on high-value syntrophies; always use the
RECORD's canonical taxon ids (Edison groundings have had
errors, e.g. sulfite → CHEBI:16731 *(E)-cinnamaldehyde* instead of CHEBI:17359). NB: when
the primary full text isn't retrievable, keep edges to abstract-supported/directly-implied
claims and file the rest as a KNOWLEDGE_GAP (000176 is the worked example).

**DONE — single-edge record enrichment (#254).** All six 2-node records got an Edison
causal-graph pass and conservative curation. What actually landed, per record:

- **000070 `Syntrophomonas_Methanospirillum`** — reverse feedback edge (methanogen H2
  scavenging → enables butyrate β-oxidation). Best evidence was already in the cached
  abstract, not in the Edison report: PMID:16345745 reports both the dependency
  ("Growth and degradation of fatty acids occur only in syntrophic association with
  H(2)-using bacteria") and the perturbation ("The addition of H(2) … stopped growth and
  butyrate degradation"). No new reference needed.
- **000069 `Syntrophobacter_Methanospirillum`** — reverse feedback edge, on the
  axenic-vs-syntrophic contrast in PMID:9828440 (exact pair: M. hungateii).
- **000068 `Syntrophobacter_Methanobacterium`** — reverse feedback edge + **fixed a real
  misattribution**: two evidence items quoted the Harmsen M. *hungateii* passage but were
  explained as establishing M. *formicicum* (this record's partner). Downgraded to PARTIAL,
  added exact-pair support from PMID:29611893, and filed discussion
  `kg-syntrophobacter-methanobacterium-partner-attribution`.
- **000033 `Geobacter_Methanosarcina`** — new `T6SS-Associated Delay of DIET Establishment`
  interaction + NEGATIVE edge to the DIET node (>30 d lag wild-type vs very little lag for
  the Hcp-deficient mutant, PMID:37650614, OA full text cached). Curated as *T6SS-associated*,
  not T6SS-caused: the mutant is pleiotropic (also reduces Fe(III) oxide faster).
- **000031 `Geobacter_Clostridium`** — no new edge; filed CONTROVERSY discussion
  `kg-geobacter-clostridium-contact-dependence-contested`. **Superseded — record RE-SCOPED
  (2026-07-28, PR #262), issue #256 closed.** See the dedicated section below; the
  "curator decision still open" note that stood here was resolved once the discovery
  study's OA full text was cached.
- **000032 `Geobacter_Methanosaeta`** — no new edge (000176 precedent). Edison proposed an
  acetate cross-feeding node, but its quotations came from secondary reviews; the primary
  (doi:10.1039/C3EE42189A) is cached abstract-only and is silent on acetate. Filed as
  `kg-geobacter-methanosaeta-acetate-route-unresolved`.

Verification: all 6 `just validate` clean; snippet audit MATCH 4086→4101 (all 12 new
snippets match, zero new mismatches) and caching PMID:29611893 OA full text also cleared the
3 pre-existing 000068 Methods-snippet mismatches (169→166 repo-wide); network-integrity audit
clean for all 6. New reference caches: PMID:34939136, PMID:37650614.

**Follow-ups this batch surfaced** (all filed as issues; statuses reconciled 2026-07-29):
1. **000031 re-scoping decision** (#256) — **DONE (2026-07-28, PR #262; issue closed).**
   See "000031 re-scoping" section below.
2. **Li et al. 2024** (`doi:10.3390/w16243551`, *Water*) — **INGESTED (2026-07-28, PR #261).**
   The curator supplied the publisher PDF; `cache_fulltext.py --from-file` cached 66,496
   chars to `references_cache/DOI_10.3390_w16243551.md`, and the exact-pair results are
   curated into 000068 (new `Exogenous Formate Dosage` environmental factor + FDH
   downregulation evidence). ⚠️ **Correction to the summary that stood here:** it said
   "5–10 mM promotes, ≥30 mM inhibits". The **≥30 mM claim was wrong** — it came from the
   Edison report and describes the paper's *anaerobic-sludge* system. In the coculture the
   response is **non-monotonic**: 30 mM "was improved instead of inhibited in the later
   stage"; only 50 mM inhibits. A quoted snippet from that report
   ("MMC metabolism of propionate was inhibited when the formate dosage reached 50 mM")
   also **appears nowhere in the paper** and was replaced with the real wording.
   #259 stays open only for the general case: automated retrieval from publishers that
   block programmatic download (`--from-file` is a manual escape hatch, not a fix).
3. **`just validate-references` reporting** (#257) — **DONE (2026-07-29, PR #265).**
   ⚠️ **Correction to an earlier note here**: it was once recorded as a "no-op". Wrong —
   it validates and does fail on a bad snippet. Two real bugs were in
   `evidence_snippet_audit.py` instead: (a) a `.md` cache was trusted only with
   `content_type:` frontmatter or a `## Content` heading, so genuine full texts fetched
   with neither (200 KB / 138 KB / 88 KB among 55 files, 642 KB) were discarded as stubs
   and the audit fell back to a short abstract `.txt`; (b) the curated-snippet stripper ran
   to EOF and ate real full text that followed a notes section. MISMATCH 166→140,
   NOCONTENT 794→756. The residual disagreement is now an explicit **RENDERING** bucket
   (62 repo-wide, `--list-rendering`): faithful quotes whose CACHE carries a PDF/XML
   artefact (`10% CO 2` vs `10% CO2`, `beta-5` vs `β-5`). **validator errors == RENDERING
   + MISMATCH.** Do NOT "fix" a RENDERING hit by editing the snippet — a discarded draft
   that did so produced `cDCE (4 to 5 mg/ L)`. `Total checks: N` counting issues lives in
   the pip package; the justfile recipe now explains it. New: `just audit-snippets`.
4. **14 dangling causal edges** (#258) — **DONE (2026-07-29, PR #264).** Detection shipped
   in #260; the triage resolved all 14 with no new claims: **7 retargeted** (the target
   named an existing node under different wording, e.g. `DNT Biotransformation` →
   `DNT Biotransformation with Photosynthetic Carbon Input`) and **7 dropped** as
   self-referential restatements — each checked first against its source node's
   description, where all seven claims survive verbatim, so no information was lost. Two of
   the dropped MSC2 edges had no description at all. Network-integrity issues 40→26,
   affected communities 18→8, dangling 14→0. No interaction nodes were minted: several
   targets ("community methane production", "Bioremediation potential") name plausible
   community-level processes, but minting them means asserting a curated interaction, which
   needs a fresh source pass rather than an inference from a broken edge.

NB: stray untracked `*.yaml.bak` backups still exist alongside these in `kb/communities/`
(gitignored, not in the repo).

**Edison auth (resolved 2026-07-21):** the key was refreshed in `.env`
(`EDISON_API_KEY`) and authenticates (HTTP 200). The stale-key shadowing footgun is
**fixed in the runner** (#245): `load_api_key()` now treats the repo `.env` FILE as the
source of truth (via `dotenv_values`), preferring it over any ambient/inherited
`EDISON_PLATFORM_API_KEY`. So a plain `just research-community-causal <id>` now works —
**no `env -u` workaround needed** (000268 was curated this way). NB:
`.bash_profile`'s export was already commented out;
the stale value was only inherited into the launching terminal session.

## 000031 re-scoping — DONE (2026-07-28, PR #262, issue #256)

`Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml` (CommunityMech:000031) asserted contact-dependent DIET
via conductive pili/nanowires. Caching the discovery study's **OA full text**
(PMID:28287150, PMC5347079 — it had been abstract-only) showed this was **never supported
by the record's own cited source**, so it was a defect, not the two-papers-disagree
controversy #256 was filed as:

- "pili"/"nanowire" appear nowhere in that paper's abstract, and in the full text only as
  generic *Geobacter* background citing prior work.
- Its discussion says the opposite of the record's claim — pre-cultures held "both
  nanowire-rich aggregates and nanowire-poor planktonic cells", and growth on conductive
  material is offered as a future option "to ensure electrical connections".
- Evidence items cited that background sentence, and an unrelated "sole electron acceptor"
  sentence, as if they demonstrated contact-mediated transfer. One was truncated mid-word.

Changes: `community_category` **DIET → SYNTROPHY** (the schema defines DIET specifically as
"Direct interspecies electron transfer"; SYNTROPHY is the neutral bucket); pili/nanowire
claims stripped from description, environment notes, taxon notes and the interaction; both
interactions renamed mechanism-neutral (`Acetate Oxidation and Interspecies Electron
Transfer`, `Glycerol Fermentation with Electron-Transfer-Induced Metabolic Shift`) with the
downstream edge + discussion anchors updated; `Cell Contact and Nanowire Formation` →
`Electrical Connection Between Cells` carrying a REFUTE item. The cobamide alternative is
**not** asserted in its place (PMID:34939136 calls its own model "putative" and is not OA).

**Rename — DONE (2026-07-29, PR #266).** The record's `name` and filename no longer say
"DIET": `Geobacter_Clostridium_DIET.yaml` → `Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml`,
and "Geobacter-Clostridium DIET Community" → "Geobacter-Clostridium Interspecies Electron
Transfer Coculture". The id `CommunityMech:000031` is **unchanged** — it is the stable
cross-repo key, and only the human-readable label and path moved. Generated artifacts
(`docs/`, `reports/validation_results.tsv`) were regenerated rather than hand-edited.

## Suillus-Bacillus thiamine SynCom — MERGED (2026-07-29, PR #255)

Had been open and unlogged since 2026-07-26 (branch `claude/session-s1rw5b`). Adds
`CommunityMech:000312` — `Suillus_Bacillus_Thiamine_Ectomycorrhizal_SynCom.yaml`, a
thiamine cross-feeding ectomycorrhizal SynCom on PMID:41454778 — plus its reference cache.
Reviewed before merge: id 000312 follows 000311 with no collision; validates clean; no
snippet mismatches; and the `DANGLING_EDGE`/`DANGLING_ANCHOR` script (not a CI gate) is
clean for it. Four interactions in a coherent recruitment → ureidosuccinic-acid → thiamine
→ colonization chain, single-source (PMID:41454778 throughout).

**Optional follow-up:** it carries **no `downstream` causal edges**, though its four
interactions read as a natural chain — a good candidate for a
`just research-community-causal CommunityMech:000312` pass.

The record count is now **305**.

## Space-regolith community curation (curatable subset DONE, 9/16)

Scout report `reports/scout_space_regolith.md` lists **16 defined-community
candidates**. **9 curated** (CommunityMech:000303–000311):
- **000303–000307** (earlier): BioRock basalt biomining (#1; folds in vanadium #6
  PMID:33868198 + cell-conc #7 PMID:33154740 as evidence), lettuce PGPB SynCom (#2),
  P-solubilizers for *N. benthamiana* (#3), Anabaena/MGS-1 anaerobic-digestion
  methanogen consortium (#4), BioAsteroid ISS chondrite biomining (#5; #16 is its
  preprint — cite the published npj Microgravity version).
- **000308 Mars Meteorite EETA79001 Growth Panel** (#11, PMID:38665180) and **000309
  Mars Regolith Cyanobacteria/Microalga Biofertilizer Panel** (#10, PMID:35865930) —
  PR #232. Both are individual-screening panels (members never co-cultured) → no
  `ecological_interactions` block (accepted honest pattern; 3 other records also have
  none).
- **000310 Moss-Microbe Complex Regolith Biofertilizer** (#8,
  doi:10.1016/j.ecolind.2025.114023; abstract cached via OpenAlex→DOI `.md`) and
  **000311 Legume-Rhizobia Mars Simulant Symbiosis** (#12, PMID:34879082) — PR #233.
  These carry real grounded interactions (COLONIZATION_FACILITATION / MUTUALISM;
  nodulation GO:0009877 + N-fixation GO:0009399).

**Remaining 4 candidates are NOT curatable as defined microbial communities** — their
membership is commercial or undefined, so members can't be grounded to NCBITaxon:
- #9 AMF+PGPB tomato (PMID:41597718): commercial AMF formulation "TM-73MR" + undefined
  "PBB"; no named species.
- #13 microbial-fertilizer consortia (PMID:41829787): three commercial fertilizer
  products, composition undefined.
- #14 AMF chickpea (PMID:41786794): AMF + vermicompost microbiome, community loosely
  defined.
- #15 sealed mini-ecosystems (PMID:39487149): Biosphere-2-style enclosures that
  *quantify proliferating* communities without defined membership.
These are logged for completeness; revisit only if a follow-up study names their
members. **The defined-community subset of the scout report is complete.** House style
for any future regolith record: `ecological_state: ENGINEERED`, `community_origin:
SYNTHETIC`, `environment_term` → ENVO:01001405 "laboratory environment" with
`modeled_environment` → ENVO:01000747 "regolith".
