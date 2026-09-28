# YAML Record Review: Panax Bacillus-Serratia Root-Rot Biocontrol SynCom

- Repository: CommunityMech
- Record: `kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml`
- Started UTC: 2026-09-28T06:38:22Z
- Finished UTC: 2026-09-28T06:40:19Z
- Verdict: needs curation

## Target

- Class: `MicrobialCommunity`
- ID: `CommunityMech:000460`
- Label: `Panax Bacillus-Serratia Root-Rot Biocontrol SynCom`
- Maintained path: `kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml`
- Generated status: maintained source YAML, with generated page at
  `docs/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.html`
- Primary source: `PMID:41872736`

The record adds the next local identifier after `CommunityMech:000459`; the ID
ceiling check used `rg --hidden --no-ignore`, so ignored files were included.
Duplicate searches for `PMID:41872736`, `s12870-026-08617-4`, `XY-6`, `XB-7`,
and the Bacillus-Serratia consortium also used `rg --hidden --no-ignore` across
curated records, caches, research artifacts, reports, docs, scripts, history,
and `.claude`.

## Validation

| Check | Result |
|---|---|
| `just validate kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` | Blocked by the repo `uv run` Python 3.13 `llvmlite==0.46.0` build failure before validation |
| `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` | Passed |
| `PYTHONPATH=src python scripts/validate_strict.py kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` | Passed |
| `PYTHONPATH=src python scripts/validate_gtdb_coherence.py kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` | Passed |
| `PYTHONPATH=src python scripts/validate_shared_taxon_ids.py kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` | Passed |
| `PYTHONPATH=src python scripts/validate_prokaryotic_lineage.py kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` | Passed |
| `linkml-term-validator validate-data kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed |
| `linkml-reference-validator validate data kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed |
| `linkml-validate -s src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom/2026-09-28T063822Z-claude-code-fdaf1f.yaml` | Passed |
| `git diff --check` | Passed |

The focused validation had to use sibling virtualenv and `uvx` executables
because the checkout's own `uv run` path currently cannot build `llvmlite` on
Python 3.13.

## Identity and Grounding

The record identity is sound: it denotes the engineered two-member BS SynCom
from Deng et al. 2026, not the Hafnia-containing alternatives. `ecological_state:
ENGINEERED`, `community_origin: SYNTHETIC`, and `community_category:
RHIZOSPHERE` agree with the greenhouse rhizosphere SynCom context.

`Bacillus subtilis XY-6` is grounded to `NCBITaxon:1423` and reuses a
corpus-existing `GTDB:s__Bacillus_subtilis` block. `Serratia marcescens XB-7`
is grounded to `NCBITaxon:615` and intentionally left GTDB-unresolved because
the local crosswalk could not be inspected.

## Evidence

The source supports:

- the two-member BS identity of `Bacillus subtilis` XY-6 plus `Serratia
  marcescens` XB-7;
- the equal-volume XY-6-centered SynCom construction;
- greenhouse disease suppression relative to single-strain treatments;
- enhanced cell-free filtrate inhibition of `F. solani` LP2 mycelia;
- induction of host antioxidant enzyme activity;
- rhizosphere bacterial and fungal amplicon profiling under BS treatment;
- deposition of raw soil microbiome sequence data under `PRJNA1379223`.

Three assertions overreach the inspected source and should be narrowed before
merge: the record calls XY-6 and XB-7 rhizosphere-soil isolates when the paper
only states that bacterial isolates came from the same root-rot-affected Panax
plantation soil used for fungal isolation; it types a fungal community shift as
`COLONIZATION_FACILITATION` without direct priority-effect or establishment
evidence; and it types host systemic-resistance activation as `MUTUALISM`
without showing that P. notoginseng resistance reciprocally benefits the two
inoculant strains.

## Completeness

The record is complete enough for the primary greenhouse and filtrate claims. It
does not need optional growth-media modeling: LB/PDA cultures are preparatory,
and omitting them is safer than importing plate details as community
maintenance conditions.

Consequential uncertainty is correctly represented as a discussion for
strain-resolved colonization and unmeasured antifungal metabolites.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The description, `environment_term.notes`, and both `taxonomy[].strain_designation.isolation_source` fields call XY-6/XB-7 rhizosphere isolates, but the accessible methods only state that bacterial isolates were obtained from the same P. notoginseng plantation soil samples as the Fusarium isolates. | `kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` |
| Major | `BS Rhizosphere Fungal-Community Remodeling` uses `interaction_type: COLONIZATION_FACILITATION`, which encodes one organism facilitating another's colonization via priority effects or niche modification. The source reports endpoint fungal restructuring and co-occurrence networks, not direct colonization facilitation. | `kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` |
| Minor | `BS Host-Systemic Resistance Activation` uses `interaction_type: MUTUALISM` for a host-defense phenotype. The source supports host benefit under BS treatment but not reciprocal benefit to the bacterial strains. | `kb/communities/Panax_Bacillus_Serratia_RootRot_Biocontrol_SynCom.yaml` |

## Recommended Edits

1. Replace rhizosphere-isolate wording with root-rot-affected P. notoginseng
   plantation-soil wording, and adjust both member `isolation_source` values.
2. Drop `interaction_type` from the fungal-community-remodeling interaction,
   leaving it as a community-level profiled outcome.
3. Drop `interaction_type` from the host-systemic-resistance interaction,
   leaving the host defense response as a community-level outcome.

## Follow-up Checks

- Re-run schema, strict, GTDB, taxon-ID, prokaryotic-lineage, term-label,
  reference, and history validation for the fixed record.
- Re-render community HTML and confirm a second render produces no further
  `docs/` drift.
- Re-read the final record around the edited descriptions, interactions,
  discussion, and history event.

## Additional Notes

iModulonDB structured adapters were not applicable: this is a rhizosphere
biocontrol SynCom record without E. coli, Bacillus subtilis 168, or another
covered iModulonDB transcriptional module claim.
