# Next Tasks — CommunityMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / TraitMech).

Last reconciled: 2026-07-19.

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
| DYSPROSIUM | CHEBI:49782 → *(not in build)* | CHEBI:33377 dysprosium atom |
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

**Note (not the same task):** a full LinkML-native schema gate over term.id
*data* bindings (`just validate-terms-all` / `linkml-term-validator`) is still
deferred — that tool has no exceptions mechanism and fails on the 34
curator-accepted residuals. Unblock by minting/cleaning them or teaching the gate
a shared waiver (see §1). See [[ontology-term-cleanup]] / [[chebi-mislabels-backlog]].

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

**Deferred — `validate-terms-all` as a blocking gate.** linkml-term-validator
(`--labels`) has NO exceptions mechanism, so it fails on exactly those residuals
(confirmed: it errors on obsolete `GO:0055114` "oxidation-reduction process",
and would also flag the CHEBI mislabels needing minting and the taxa absent
from the OAK snapshot). Enabling it as blocking requires one of:
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
ChEBI/ENVO/GO/NCBITaxon terms. validate-terms-all stays deferred. The real fixes
are external: (a) submit the ~9 CHEBI + 3 ENVO + 2 NCBITaxon compounds/taxa as
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

**Remaining before emitting ingredient suggestions:** decide the id per MIM#119.
The **CHEBI route works today** — env-matched MIM ingredients that `skos:exactMatch`
a CHEBI term can be emitted as `RelatedIngredient` (`chebi_term` +
`shared_environment_term`) with no id decision needed; build once MIM confirms (c).
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
  not logic-limited). **Remaining:** regenerate `docs/` pages for the 23 records;
  optionally apply the same `modeled_environment` matching to the (draft) ingredient
  suggester.

## 3. Cross-Mech validator pin guard — DONE (4-repo invariant)

**Done** (2026-06-15, culturebotai-claw#6 Option 1): the pin now covers the full
vendored set via a `VENDORED_IDLABEL_FILES` manifest — the validator `.py` **plus**
the two byte-identical shared tests (`tests/test_id_label_empty_adapter.py`,
`tests/test_id_label_unknown_prefix.py`). CommunityMech's two test copies had
drifted (cosmetic: a `not_empty`→`NOT_empty` rename + whitespace); resynced to the
CultureMech/MIM canonical bytes (`55a432e0…` / `f01d2264…`) and re-pinned, so all
three Mechs now share an identical 3-line `.sha256` manifest. CI's `sha256sum -c`
step enforces all three; `verify-validator-pin` passes; the 17 vendored tests pass.
`conf/id_label_targets.yaml` stays **unpinned** (intentionally per-repo).

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

## Adopt DisMech knowledge-gaps + datasets + QC dashboard (claw#7)

Coordinated cross-Mech adoption of DisMech's domain-general features. Full plan,
locked decisions, and DisMech schema references live in culturebotai-claw#7 (the
shared, pinned LinkML module is authored once and vendored across all four Mechs).
This repo's slice:
- Knowledge gaps — add a `discussions` slot (broad `Discussion` supertype; `kind`
  incl. KNOWLEDGE_GAP / OPEN_QUESTION / CONTROVERSY / CURATION_TODO) to
  `MicrobialCommunity`, imported from the shared module; bind `attaches_to`
  anchors to `ecological_interactions#…`. Wire a `knowledge-gap-scan` recipe over
  the existing Edison harness.
- Datasets — migrate the existing `AssociatedDataset` (DatasetRepositoryEnum) to
  the canonical shared `Dataset` (data-preserving; reconcile repository/accession
  into the canonical enum, which also carries omics `data_type`).
- QC dashboard — adopt the generalized dashboard from Phase 3 (CommunityMech
  currently has only the `qc` recipe, no rendered dashboard).
