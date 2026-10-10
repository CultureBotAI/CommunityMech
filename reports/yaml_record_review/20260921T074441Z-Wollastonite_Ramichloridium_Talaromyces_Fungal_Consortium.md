# YAML Record Review: Wollastonite Ramichloridium-Talaromyces Fungal Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml`
- Started UTC: 2026-09-21T07:41:05Z
- Finished UTC: 2026-09-21T07:44:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000404` |
| Label | Wollastonite Ramichloridium-Talaromyces Fungal Consortium |
| Maintained path | `kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml` |
| Generated | No |
| Primary source | `PMID:42478817`; full text committed at `references_cache/PMID_42478817.txt` |
| Scope | Synthetic two-fungus wollastonite bioleaching mixed culture |

The maintained record represents a defined shake-flask consortium of
`Ramichloridium apiculatum` CMS-1 and `Talaromyces pseudofuniculosus` hzt-3′
from Chang et al. 2026, not a natural mineral-soil community or a reusable
taxon record.

Hidden/ignored-inclusive searches over `kb`, `data`, `references_cache`,
`research`, `tmp`, `.claude`, `reports`, and `history` were used before
creation to check for `PMID:42478817`, `10.1128/aem.02519-25`, wollastonite /
Ramichloridium / Talaromyces title cues, and `CommunityMech:000404`; no
pre-existing maintained record or ID collision was found.

## Validation

`just` recipes were mapped to their direct `.venv` equivalents because this
checkout's `uv run` path currently fails while trying to build an optional
`llvmlite`/`umap-learn` dependency under Python 3.13.

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml --out /private/tmp/wollastonite-strict-final3.tsv` | pass; 0 ERROR rows |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml` | pass |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium/2026-09-21T074105Z-claude-code-8a2e95.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | pass; rendered 394 community pages plus browser and landing pages |
| `docs/communities/*.html` orphan loop from `check-docs-current` | pass |
| `git diff --check` | pass |

## Identity and Grounding

The record identity is sound. The title, `ENGINEERED` state, `SYNTHETIC`
origin, and `BIOMINING` category describe the constructed two-member mixed
fungal culture used for wollastonite bioleaching.

The two species-level NCBITaxon IDs were resolved against NCBI E-utilities:
`NCBITaxon:470080` for `Ramichloridium apiculatum` and `NCBITaxon:2015341` for
`Talaromyces pseudofuniculosus`. The exact strain symbols from the paper are
preserved as `CMS-1` and `hzt-3′`. Both members correctly carry
`NO_GTDB_EQUIVALENT` with notes explaining that GTDB does not classify fungi.

The ENVO, CHEBI, and GO labels in the record passed the term validator. The
record intentionally uses `ENVO:01001405` for the laboratory culture and a
separate `ENVO:00001998` modeled environment for the mineral-rich soil source.

## Evidence

Every curated biological and cultivation claim is backed by `PMID:42478817`
with an exact snippet from either the PubMed abstract or the committed
open-access Europe PMC full-text cache.

Supported claim groups:

- the exact mixed-culture identity and the six CMS-1:hzt-3′ starting ratios;
- membership and strain designations for `R. apiculatum` CMS-1 and
  `T. pseudofuniculosus` hzt-3′;
- CMS-1 extracellular polysaccharide/protein production and hzt-3′ utilization
  of those extracellular products;
- organic-acid and amino-acid upregulation in mixed culture, including oxalic
  acid, gluconic acid, isocitric acid, L-glutamine, and L-tyrosine;
- the 20% CMS-1 + 80% hzt-3′ optimum for calcium and silicon leaching;
- 100 mL modified Czapek medium, 0.5 g wollastonite, 250 mL conical flasks,
  30°C, and 150 rpm batch shake-flask cultivation.

The pH 7.5 medium detail was left out of `growth_media.ph`: the source gives it
inside `[pH 7.5]`, and the local reference validator strips bracketed text
before substring matching. The rest of the medium sentence was split into
validator-compatible, exact snippets instead of weakening the evidence gate.

Unsupported or over-scoped claims: None found.

## Completeness

The record is complete enough for the source: it captures community identity,
taxonomy, engineered assembly, the principal cross-feeding edge, the emergent
leaching outcome, environmental context, Czapek/wollastonite growth conditions,
and curation history.

Appropriately empty or absent fields:

- `associated_datasets`: the paper did not report a genome, BioProject, or SRA
  accession for CMS-1 or hzt-3′.
- `external_resources`: no model repository, protocol DOI, or durable
  non-paper resource was needed.
- `related_media` / `related_ingredients`: no CultureMech or
  MediaIngredientMech cross-repo grounding was established in this curation.
- `metals_present`: wollastonite calcium/silicon leaching is the functional
  outcome, but no curated metal enum was required.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

Run the normal CI gates after committing:

- `gh pr checks`
- merge-queue checks after `gh pr merge --auto --squash --delete-branch`

## Additional Notes

This review was run after a focused self-review had already corrected the
`hzt-3′` prime mark in the `Talaromyces` strain designation and exact snippets
that were split around the reference validator's bracketed-text behavior.
