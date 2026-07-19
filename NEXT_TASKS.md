# Next Tasks — CommunityMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / TraitMech).

Last reconciled: 2026-07-18.

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

**Item 2 — STILL DEFERRED — close the systemic gap:** enum `meaning:` groundings
are **not** covered by
   any id↔label gate — `validate-products` only checks record-level
   `term.{id,label}` pairs, so these drifted wrong undetected while the gated
   record pairs stayed correct (spot-checked: `Ion_Adsorption_REE_Indigenous_`
   `Community.yaml` uses the *correct* CHEBI:33377/CHEBI:49962). **Follow-up:** add
   a small test (or extend the label gate) that validates every enum `meaning:` id
   against its canonical ChEBI/ENVO/etc. label so this class of bug can't recur —
   without it, item 1 could silently regress on the next hand-edit. See
   [[ontology-term-cleanup]] / [[chebi-mislabels-backlog]].

**Impact:** shipped community records mostly ground REEs via their own (correct)
`term.{id,label}` pairs, so the KGX export from those is largely fine; the wrong
groundings live in the schema enum + `metal_extraction.py` map (any enum-driven
export/analysis inherits them). Low blast radius today, but a latent correctness
bug and a clear gate gap.

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

Open issue: enhance environment/isolation-source links between CommunityMech,
CultureMech, and MIM (shared ENVO grounding, cross-references). Scope and
sequence against the MIM single-source-of-truth direction before building.

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
