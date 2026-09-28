# YAML Record Review: FOS Lactobacillus-Minimal Core Gut-Liver SynCom

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml`
- Started UTC: 2026-09-28T18:03:00Z
- Finished UTC: 2026-09-28T18:05:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000466` |
| Label | `FOS Lactobacillus-Minimal Core Gut-Liver SynCom` |
| Maintained/generated | Maintained curated YAML |

The target is a maintained YAML record for a defined seven-strain anaerobic
in-vitro gut model from Finazzi et al. 2026. It combines three human-derived
`Lactobacillus` probiotic strains with a four-strain minimal human-gut core,
grows probiotic, minimal-core, and combined whole-community assays in mMRS
with FOS DP ~ 10 or glucose, and connects strain qPCR, Lactobacillus
FOS-expression, GC-MS organic-acid, and HepG2 metabolite-extract readouts.

## Validation

| Check | Result |
|---|---|
| `PYTHONPATH=src ../TraitMech/.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Pass |
| `PYTHONPATH=src ../TraitMech/.venv/bin/python scripts/validate_strict.py kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Pass; 1 file scanned, 0 files with ERROR |
| `PYTHONPATH=src ../TraitMech/.venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Pass; 1 file checked, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `PYTHONPATH=src ../TraitMech/.venv/bin/python scripts/validate_yaml_scalars.py kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Pass; 1 file checked, 0 truncated scalars |
| `PYTHONPATH=src ../TraitMech/.venv/bin/python scripts/validate_cross_repo_ids.py kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Pass |
| `PYTHONPATH=src ../TraitMech/.venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-rendering --list-assembled --list-nocontent kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Pass; 29 snippets scanned, all 29 MATCH |
| independent normalized snippet walk over `references_cache/PMID_42781020.txt` | Pass; 29 `PMID:42781020` snippets checked, 0 missing |
| `../TraitMech/.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom/2026-09-28T180219Z-claude-code-8ee97f.yaml` | Pass |
| `just validate-terms kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Not checked by the dedicated CLI: project-level `uv run` tried to build `llvmlite==0.46.0` through `umap-learn` and failed in the local Python 3.13/3.11 environments |
| `just validate-references kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` | Not checked by the dedicated CLI: the same project-level `uv run`/`llvmlite==0.46.0` failure blocked `linkml-reference-validator`; the repository snippet audit and independent exact matcher both verified the cached source text |

`communitymech.export.browser_export` and `communitymech.render` both ran
successfully with `PYTHONPATH=src ../TraitMech/.venv/bin/python` and generated
the 456-record browser and per-community HTML corpus including this record.

## Identity and Grounding

The ID, filename, name, `ENGINEERED` ecological state, `SYNTHETIC` origin, and
`DIET` category agree with a defined human-gut in-vitro SynCom grown on the FOS
prebiotic carbon source. `ENVO:01001405` / `laboratory environment` is the
physical batch-culture setting; `ENVO:2100002` / `intestine environment`
correctly marks the modeled human gut context.

The seven member strains match Table 1 in `PMID:42781020`: `L. plantarum`
PBS067 DSM 24937, `L. acidophilus` PBS066 DSM 24936, `L. reuteri` PBS072 DSM
25175, `Bacteroides cellulosilyticus` CL02T12C19 HM-726, `Clostridium
symbiosum` WAL-14673 HM-319, `Flavonifractor plautii` 1_3_50AFAA HM-303, and
`E. coli` ATCC 25922. Existing curated records support the reused NCBITaxon and
GTDB species-level assignments for `Lactiplantibacillus plantarum`,
`Lactobacillus acidophilus`, `[Clostridium] symbiosum`, and `Escherichia coli`;
`Limosilactobacillus reuteri`, `Bacteroides cellulosilyticus`, and
`Flavonifractor plautii` are honestly left `UNRESOLVED` for GTDB because the
local NCBI-to-GTDB crosswalk was unavailable.

iModulonDB was not applicable: the record names gut consortium strains,
FOS-utilization genes in Lactobacillus, and RT-qPCR/metabolite readouts, not an
E. coli K-12 expression component covered by the structured adapter.

## Evidence

All 29 curated snippets matched the cached `PMID:42781020` PubMed plus
open-access PMC full text exactly after whitespace normalization.

The cached paper supports the seven-member assembly, the 10 mL mMRS plus 0.3%
L-cysteine batch setup, the 2% FOS DP ~ 10 and 1% glucose sole-carbon-source
conditions, per-strain OD600-normalized inoculation into the probiotic,
minimal-core, and whole-community arms, 37 degrees C static anaerobic
incubation, species-specific RT-qPCR, Lactobacillus FOS-gene RT-qPCR, GC-MS
organic-acid profiling, and the palmitate-induced HepG2 extract assay. The open
knowledge-gap discussion correctly preserves that the exact HepG2-active
metabolite or metabolite mixture was not identified.

The unsupported edge is the repeated `functional_role: PRIMARY_DEGRADER`
classification on every member. Table 1 proves membership, human isolation
source, and DSM/BEI/ATCC stock identity; the growth and qPCR text proves a
strain-dependent FOS response. Neither evidence object supports assigning all
seven taxa a uniform primary FOS-degrader role in the whole reconstructed
community.

## Completeness

The record is complete for the in-vitro claims in the primary paper. It
correctly leaves the host-cell causal metabolite identity open, keeps the BEI
HM stocks in `notes` because the local culture-collection enum has no BEI
entry, and marks three GTDB mappings unresolved instead of inventing a manual
pin while the local crosswalk is missing.

Ignored-inclusive searches were run over `kb`, `data`, `history`, `docs`,
`references_cache`, `reports`, and `.claude` for the new DOI/PMID, record stem,
and exact strain names. They found this new maintained YAML, generated docs,
history, the new PMID cache, known different records for `E. coli ATCC 25922`
and a different `Flavonifractor plautii` strain, and no pre-existing duplicate
curated record for `PMID:42781020`, the record stem, or the seven-strain
composition.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | Every member is tagged as `PRIMARY_DEGRADER`, but the source reports strain-dependent FOS growth and the member-level evidence only identifies the strains. The role therefore overstates source support, especially for members that are tracked or low-abundance rather than demonstrated as primary FOS degraders in the whole seven-strain culture. | `kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml` |

## Recommended Edits

- Remove the seven unsupported `functional_role: PRIMARY_DEGRADER` blocks from
  `kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml`; retain
  the supported strain-dynamic and FOS-expression claims under
  `ecological_interactions`, `environmental_factors`, and `growth_media`.
- Append a guarded `curation_history` event and repository history record for
  the role-scope fix.
- Regenerate `docs/browser.html`, `docs/index.html`, and the per-community HTML
  page after editing the maintained YAML.

## Follow-up Checks

- Re-run schema, strict closed-mode, GTDB coherence, YAML-scalar, cross-repo,
  snippet-audit, and history validation after the maintained YAML edit.
- Re-run the browser and HTML generators and inspect `git diff --check`.
- Re-read the taxonomy blocks to confirm no unsupported `PRIMARY_DEGRADER`
  values remain while the supported FOS strain-dynamic interaction is still
  present.

## Additional Notes

The `just validate-terms` and `just validate-references` recipes should still
run in CI or in a local environment whose `uv run` path can install
`llvmlite==0.46.0`.
