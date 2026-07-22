# Next Tasks — CommunityMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / TraitMech).

Last reconciled: 2026-07-21.

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
  the slot, so future records render automatically. **Remaining (optional):** apply the
  same `modeled_environment` matching to the (draft) ingredient suggester.

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
(000031–033 DIET, 000068–070 syntrophies) were left as-is. ~65/304 records now carry
`downstream` causal edges. **Next:** continue on high-value syntrophies; always use the
RECORD's canonical taxon ids (Edison groundings have had
errors, e.g. sulfite → CHEBI:16731 *(E)-cinnamaldehyde* instead of CHEBI:17359). NB: when
the primary full text isn't retrievable, keep edges to abstract-supported/directly-implied
claims and file the rest as a KNOWLEDGE_GAP (000176 is the worked example).

**PENDING — enrich the single-edge records via a full causal-graph run.** Six 2-node
records already carry one hand-authored `downstream` edge (donor→acceptor) from original
curation but have not had an Edison causal-graph pass: the DIET trio
`Geobacter_Clostridium_DIET` (000031, PMID:28287150),
`Geobacter_Methanosaeta_DIET` (000032, doi:10.1039/C3EE42189A),
`Geobacter_Methanosarcina_DIET` (000033, PMID:24837373); and the syntrophies
`Syntrophobacter_Methanobacterium_Syntrophy` (000068), `Syntrophobacter_Methanospirillum_Syntrophy`
(000069), `Syntrophomonas_Methanospirillum_Syntrophy` (000070). A full run could add
mechanistic nodes/edges (e.g. conductive pili / OmcS-OmcZ cytochromes, conductive-material
mediation, formate-vs-H2 routes, reverse/feedback edges) beyond the single existing edge.
Run `just research-community-causal CommunityMech:0000NN` per record, then curate
conservatively as usual. NB: stray untracked `*.yaml.bak` backups exist alongside these in
`kb/communities/` (gitignored, not in the repo) — target the `.yaml` files.

**Edison auth (resolved 2026-07-21):** the key was refreshed in `.env`
(`EDISON_API_KEY`) and authenticates (HTTP 200). The stale-key shadowing footgun is
**fixed in the runner** (#245): `load_api_key()` now treats the repo `.env` FILE as the
source of truth (via `dotenv_values`), preferring it over any ambient/inherited
`EDISON_PLATFORM_API_KEY`. So a plain `just research-community-causal <id>` now works —
**no `env -u` workaround needed** (000268 was curated this way). See
[[edison-auth-env-shadowing]]. NB: `.bash_profile`'s export was already commented out;
the stale value was only inherited into the launching terminal session.

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
`modeled_environment` → ENVO:01000747 "regolith". See [[space-regolith-scouting-gap]].
