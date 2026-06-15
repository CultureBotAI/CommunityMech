# Next Tasks — CommunityMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / TraitMech).

Last reconciled: 2026-06-14.

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

## 2. Cross-repository environmental linking (issue #30)

Open issue: enhance environment/isolation-source links between CommunityMech,
CultureMech, and MIM (shared ENVO grounding, cross-references). Scope and
sequence against the MIM single-source-of-truth direction before building.

## 3. Cross-Mech validator pin guard covers only the .py — DONE

**Done** (2026-06-15, culturebotai-claw#6 Option 1): the pin now covers the full
vendored set via a `VENDORED_IDLABEL_FILES` manifest — the validator `.py` **plus**
the two byte-identical shared tests (`tests/test_id_label_empty_adapter.py`,
`tests/test_id_label_unknown_prefix.py`). CommunityMech's two test copies had
drifted (cosmetic: a `not_empty`→`NOT_empty` rename + whitespace); resynced to the
CultureMech/MIM canonical bytes (`55a432e0…` / `f01d2264…`) and re-pinned, so all
three Mechs now share an identical 3-line `.sha256` manifest. CI's `sha256sum -c`
step enforces all three; `verify-validator-pin` passes; the 17 vendored tests pass.
`conf/id_label_targets.yaml` stays **unpinned** (intentionally per-repo).

TraitMech remains outside the trio (no validator yet) — adoption is its own task,
not a sync; see TraitMech `NEXT_TASKS.md` item 2.
