# YAML Record Review: Quinoa SCDY1 Salt-Stress SynCom

- Repository: CommunityMech
- Record: `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml`
- Started UTC: 2026-09-28T04:54:03Z
- Finished UTC: 2026-09-28T04:59:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000459` |
| Label | `Quinoa SCDY1 Salt-Stress SynCom` |
| Maintained path | `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` |
| Generated status | Maintained YAML with generated `docs/communities/Quinoa_SCDY1_Salt_Stress_SynCom.html` |
| Source | `doi:10.64898/2026.07.15.738596` |

The target is a new engineered, synthetic, plant-associated bacterial SynCom record for the nine-member SCDY1 consortium selected from quinoa isolates and assayed on Arabidopsis under NaCl stress.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` via the TraitMech venv | Pass |
| `python scripts/validate_strict.py kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` via the TraitMech venv | Pass; 0 errors |
| `linkml-term-validator validate-data ... --labels` via the MediaIngredientMech venv | Pass |
| `python scripts/validate_cross_repo_ids.py kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` via the TraitMech venv | Pass |
| `python scripts/validate_gtdb_coherence.py kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` via the TraitMech venv | Pass; 0 incoherent blocks |
| `python scripts/validate_prokaryotic_lineage.py kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` via the TraitMech venv | Pass; 0 contradictory lineages |
| `python scripts/validate_yaml_scalars.py kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` via the TraitMech venv | Pass; 0 truncated scalars |
| `linkml-reference-validator validate data ... --target-class MicrobialCommunity --config conf/reference_validator.yaml` via `uvx` | Did not provide an effective check: the CLI exited 0 but reported `Total checks: 0` |
| Manual structured snippet audit over YAML `EvidenceItem` objects | Pass; 20 evidence snippets checked, 0 missing from `references_cache/doi_10.64898_2026.07.15.738596.md` |
| `linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Quinoa_SCDY1_Salt_Stress_SynCom/2026-09-28T045749Z-claude-code-8ed785.yaml` | Pass |
| `python -m communitymech.render` via the TraitMech venv | Pass; rendered 449 community pages and generated browser/landing pages |
| `docs/communities/*.html` orphan check | Pass; 0 orphan pages |

## Identity and Grounding

The CommunityMech ID is new, the filename matches the record label, and the record scope is correctly limited to the defined SCDY1 SynCom rather than all quinoa-associated isolates.

The nine `taxonomy` entries agree with the source paragraph that names isolates 82, 85, 88, 91, 94, 97, 100, 103, and 106. Each member is worded as a species-like isolate because the paper identified them from partial 16S rRNA sequences.

The ontology labels pass the term gate. GTDB blocks present for `Novosphingobium subterraneum`, `Herbaspirillum frisingense`, `Acidovorax`, and `Bacillus subtilis` pass the focused GTDB validators; the unresolved GTDB entries are explicit rather than falsely grounded.

## Evidence

The source cache contains exact supporting text for the cube design, the 100 mM NaCl primary screen, the full nine-isolate membership list, Arabidopsis root elongation and biomass promotion under 120 mM NaCl, recovery of a subset of bacteria from seedlings, host RNA-seq/RT-qPCR modulation, root-hair phenotyping, and the SynCom plate-spreading method.

Three evidence placements still need curation:

- The description and `metal_notes` attribute the work to “Chavarro Carrero et al.”, but the source metadata names the article by Dangjarean, Murata, Kobayashi, Neyrot, Ogata, Fujita, and coauthors.
- `SCDY1 root-associated recovery` is modeled as a `COMMENSALISM` ecological interaction, but the cited snippet only says that a subset of SCDY1 bacteria was recoverable from seedlings; recovery shows persistence in the assay, not a +/0 interaction.
- `SCDY1 modulation of Arabidopsis root epidermal state` is modeled as a second `MUTUALISM` ecological interaction, but the cited transcriptomic and root-hair snippets are host-response readouts downstream of the SynCom treatment, not an independent ecological relationship between community participants.

## Completeness

The record is complete enough to preserve the SCDY1 identity, member list, salt-stress selection condition, NaCl as the stressor, and the main Arabidopsis plant-growth endpoint.

The growth-medium block is not complete enough: it is named `half-strength Murashige and Skoog salt-stress agar`, but its `composition` lists only sodium chloride and the attached snippet proves SynCom suspension application rather than MS basal salts, MES/KOH, agar concentration, pH, or a complete salt-stress medium formulation.

The exact DOI/title searches for the Quinoa source were gitignore-independent during curation; no pre-existing curated SCDY1 record or source cache was found before this record was added. Ignored files were included.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | Wrong author attribution: the maintained YAML says “Chavarro Carrero et al.” in the description and `metal_notes`, but the Quinoa SCDY1 source metadata identifies Dangjarean et al. | `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` |
| major | `SCDY1 root-associated recovery` overstates assay recovery as a `COMMENSALISM` interaction. | `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` |
| major | `SCDY1 modulation of Arabidopsis root epidermal state` overstates host transcript/root-hair readouts as a second `MUTUALISM` interaction. | `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` |
| major | The `growth_media` item asserts a half-strength Murashige and Skoog salt-stress agar medium without a complete composition or a snippet that names that medium. | `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml` |

No blocker findings.

## Recommended Edits

1. Replace both instances of “Chavarro Carrero et al.” with “Dangjarean et al.” in `kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml`.
2. Remove the `SCDY1 root-associated recovery` ecological-interaction block unless the source text is re-modeled as a non-interaction assay note in a schema-supported field.
3. Remove `SCDY1 modulation of Arabidopsis root epidermal state` as a standalone ecological interaction; keep the RNA-seq and root-hair claims only if they are attached to a narrower, schema-supported host-response assertion.
4. Remove the `growth_media` block unless the exact half-strength MS formulation can be cached and represented with its major ingredients.
5. Rerun the guarded writer, focused validators, snippet audit, history validation, and HTML renderer after editing the YAML.

## Follow-up Checks

- `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml`
- `python scripts/validate_strict.py kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml`
- `linkml-term-validator validate-data kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels`
- `python scripts/validate_gtdb_coherence.py kb/communities/Quinoa_SCDY1_Salt_Stress_SynCom.yaml`
- Structured evidence-snippet audit against `references_cache/doi_10.64898_2026.07.15.738596.md`
- `linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Quinoa_SCDY1_Salt_Stress_SynCom/*.yaml`
- `python -m communitymech.render`
- `git diff --check`

## Additional Notes

The documented `just` validators could not run directly because `uv run` attempted to rebuild the local Python 3.13 `.venv` and failed while building `llvmlite==0.46.0`. Equivalent schema, strict, ontology-term, GTDB, scalar, history, and render commands were run with sibling virtualenvs instead.
