# Next Tasks — CommunityMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / TraitMech).

Last reconciled: 2026-06-14.

## 1. Phase-2 id↔label enforcement rollout (report-only → blocking)

The id↔label validator is vendored and in sync (byte-identical `.py` with
MIM/CultureMech; `just verify-validator-pin` passes), and the `exceptions` /
`OK_EXCEPTION` enforcement path is restored (issue #134). But the gate is still
**Phase-1 report-only**: `.github/workflows/label-correspondence.yaml` runs
`just report-label-drift`, not the blocking `just validate-products`.

- Triage `reports/label_drift.tsv`; confirm the curator-accepted residuals in
  `conf/id_label_targets.yaml` (`exceptions:`) still resolve as OK_EXCEPTION.
- Then switch CI to `just validate-products` (blocking) and add
  `validate-terms-all` for the community YAMLs.

## 2. Cross-repository environmental linking (issue #30)

Open issue: enhance environment/isolation-source links between CommunityMech,
CultureMech, and MIM (shared ENVO grounding, cross-references). Scope and
sequence against the MIM single-source-of-truth direction before building.

## 3. Cross-Mech validator pin guard covers only the .py (cross-repo)

`verify-validator-pin` pins the validator **script** but not the vendored tests
or conf, which can silently drift. Tracked in culturebotai-claw#6 — fix across
all Mech copies together.
