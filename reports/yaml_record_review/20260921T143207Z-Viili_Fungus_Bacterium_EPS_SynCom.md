# YAML Record Review: Viili Fungus-Bacterium EPS SynCom

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml`
- Started UTC: 2026-09-21T14:32:07Z
- Finished UTC: 2026-09-21T14:32:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000408` |
| Label | Viili Fungus-Bacterium EPS SynCom |
| Maintained path | `kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` |
| Generated | No |
| Primary source | `PMID:42372608`; DOI `10.1016/j.ijfoodmicro.2026.111922`; PubMed abstract cached in `references_cache/PMID_42372608.txt` |
| Scope | Top-down three-strain Viili fermented-milk SynCom composed of `Lactococcus lactis V9`, `Lacticaseibacillus paracasei V21`, and `Geotrichum candidum Y1` |

This target is a maintained community record for the Viili fungus-plus-lactic-acid-bacteria
model used by Hu et al. 2026 to test exopolysaccharide production, fungal
nitrogen supply, and AI-2-linked quorum sensing in vitro. It is not a natural
Viili microbiome record, a general yogurt or kefir starter, or a record for
undefined fermented-milk flora.

Before curation, gitignore-independent `rg --no-ignore --hidden` searches over
the repository for `PMID:42372608`, `10.1016/j.ijfoodmicro.2026.111922`, the
exact publication title, `Lactococcus lactis V9`, and `Geotrichum candidum Y1`
found no existing curated `kb/communities` or `data/isolates` duplicate. Ignored
and hidden files were included.

## Validation

`just` wrappers were unavailable in this checkout where they invoked `uv run`:
`uv` attempted to build `llvmlite==0.46.0` for Python 3.13 and failed. Direct
`.venv` equivalents were used where possible.

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` | pass; 0 ERROR rows |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | pass but non-substantive; reported `Total checks: 0` |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-rendering --list-assembled --list-nocontent kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` | pass; 15 MATCH / 0 RENDERING / 0 ASSEMBLED / 0 WEAK / 0 MISMATCH / 0 NOCONTENT |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` | pass; 1 file, 0 incoherent blocks |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` | pass; 1 file, 0 truncated scalars |
| `PYTHONPATH=src .venv/bin/python scripts/validate_cross_repo_ids.py kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml` | pass |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Viili_Fungus_Bacterium_EPS_SynCom/2026-09-21T142956Z-claude-code-b29e11.yaml` | pass |
| `PYTHONPATH=../../culturebotai-claw/src .venv/bin/python -m kg_microbe_history validate --structural-only history/records/Viili_Fungus_Bacterium_EPS_SynCom/2026-09-21T142956Z-claude-code-b29e11.yaml` | pass structurally; full schema validation used the vendored CommunityMech history schema above |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | pass; rendered 398 community pages plus `docs/browser.html` and `docs/index.html` |
| `git diff --check` | pass |

Unavailable or intentionally skipped checks:

- `just new-history` failed through the local `uv run`/Python 3.13 `llvmlite`
  build path; `kg_microbe_history new` was run through `.venv` instead.
- `kg_microbe_history validate` without `--structural-only` spawned bare
  `linkml-validate`, which resolved to a pyenv shim for an unavailable Python
  `3.13`; the same history record passed direct `.venv/bin/linkml-validate`.
- `scripts/validate_ncbitaxon_ids.py` and
  `scripts/validate_id_label_correspondence.py` are corpus-level sweeps in this
  checkout. The three NCBI labels for this record were checked directly before
  curation, and the OAK-backed term validator accepted the labels in the YAML.

## Identity and Grounding

The identity is sound. `ENGINEERED`, `SYNTHETIC`, and `BIOTECHNOLOGY` match a
defined laboratory consortium assembled from a top-down Viili model to study
fungus-bacterium regulation of fermented-milk EPS production. `ENVO:03600040`
is a starter-like engineered fermentation environment, and `ENVO:00003862`
keeps the broader dairy context modeled rather than treating this as an
uncurated natural dairy community.

The three member claims match the source abstract:

- `Lactococcus lactis V9`
- `Lacticaseibacillus paracasei V21`
- `Geotrichum candidum Y1`

NCBI ESummary resolved `NCBITaxon:1358` to `Lactococcus lactis`,
`NCBITaxon:1597` to `Lacticaseibacillus paracasei`, and
`NCBITaxon:1173061` to `Geotrichum candidum` during curation. The two bacterial
species conservatively keep `gtdb_grounding_status: UNRESOLVED`; the fungal
member correctly uses `NO_GTDB_EQUIVALENT`.

## Evidence

Supported claim groups:

- The engineering-design block cites the source's model system, exact three
  strains, top-down construction, and monoculture, co-culture, and supernatant
  assays.
- Each member taxon cites the local source text that names V9, V21, and Y1 as
  members of the Viili SynCom.
- The nitrogen-supply interaction is supported by metabolomics plus validation,
  amino-acid depletion, and amino-acid supplementation claims in the abstract.
- The valine and amino-acid annotations are scoped to enhanced growth, biofilm
  formation, and EPS in the lactic acid bacteria.
- The AI-2 quorum-sensing node is supported as a downstream fungal co-culture
  response that was experimentally activated and inhibited, not as a claim that
  `G. candidum` itself secretes AI-2.
- The full three-species EPS output is supported by the abstract's comparison
  with all tested microbial combinations.
- PubMed and DOI external resources point to stable primary-source identifiers.

Unsupported or over-scoped claims:

- None found.

One near miss was checked and cleared: `InteractionTypeEnum` has no dedicated
signaling value. Given its finite values, `CROSS_FEEDING` is the closest
available type for the fungal-metabolite, nitrogen, valine, and AI-2 activation
claims as long as the text does not assert fungal secretion of AI-2.

## Completeness

The record is complete enough for the legally available source. It captures the
three exact strains, the Viili model scope, the major assay families, the
fungal nitrogen/valine interaction, the AI-2 quorum-sensing/EPS arm, the
highest-EPS full consortium outcome, non-metal relevance, primary PubMed and
DOI resources, and append-only local plus repository history.

Appropriately absent fields:

- `growth_media`: the inspected PubMed/Europe PMC abstract does not provide
  medium, temperature, atmosphere, inoculation ratio, or incubation duration.
- `associated_datasets`: no SRA, BioProject, model, or metabolomics repository
  accession was present in the inspected source text.
- precise GTDB species clusters for `L. lactis` and `L. paracasei`: local GTDB
  grounding was unresolved, and no genome accessions were reported in the
  abstract.
- `metals_present` and `rare_earth_elements_present`: the record concerns
  fermented-milk EPS, amino-acid exchange, and quorum sensing rather than metal
  or rare-earth chemistry.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Before merging, rerun or confirm:

- `git diff --check`
- `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml`
- `.venv/bin/linkml-term-validator validate-data kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels`
- `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-rendering --list-assembled --list-nocontent kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml`
- `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Viili_Fungus_Bacterium_EPS_SynCom/2026-09-21T142956Z-claude-code-b29e11.yaml`

## Additional Notes

`references_cache/PMID_42385706.txt`, `references_cache/PMID_42613016.txt`,
and untracked PDFs under `references_cache/files/` were already present in the
worktree and are unrelated to this record.
