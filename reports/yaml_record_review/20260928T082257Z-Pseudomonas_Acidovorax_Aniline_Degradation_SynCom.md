# YAML Record Review: Pseudomonas-Acidovorax Aniline-Degradation SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml
- Started UTC: 2026-09-28T08:18:11Z
- Finished UTC: 2026-09-28T08:22:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000461` |
| Label | Pseudomonas-Acidovorax Aniline-Degradation SynCom |
| Maintained or generated | Maintained canonical YAML |

The record denotes one defined, synthetic, two-member RF-PH consortium composed
of Pseudomonas sp. RF and Acidovorax sp. PH for in vitro aniline degradation.
It does not represent the source aniline-contaminated soil community or the
monoculture assays.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` via the local `culturebotai-claw` venv | Pass |
| `scripts/validate_strict.py kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` via `PYTHONPATH=src` and the TraitMech venv | Pass; 1 file scanned, 0 error rows |
| `linkml-term-validator validate-data kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` via `uvx` | Pass |
| `linkml-reference-validator validate data kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` via `uvx --with 'linkml>=1.9.3'` | Pass |
| `scripts/validate_gtdb_coherence.py kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` | Pass; 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `scripts/validate_prokaryotic_lineage.py kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` | Pass; 0 contradictory lineages |
| `scripts/validate_shared_taxon_ids.py kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` | Pass; 0 reused IDs within the file |
| `scripts/validate_yaml_scalars.py kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` | Pass; no truncated scalars |
| `linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom/*.yaml` via the local `culturebotai-claw` venv | Pass for both append-only history records |
| `PYTHONPATH=src python -m communitymech.render` via the TraitMech venv | Pass; rendered 451 community pages plus `docs/browser.html` and `docs/index.html` |
| `git diff --check` | Pass |
| Docs orphan check over `docs/communities/*.html` against `kb/communities/*.yaml` | Pass; no orphan pages printed |

Skipped direct `just` wrappers because this checkout's `uv run` currently tries
to build `llvmlite==0.46.0` under Python 3.13 and fails before invoking the
underlying validators. The checks above run the same narrow validation logic
through working local tool environments.

## Identity and Grounding

- **Record ID and label:** `CommunityMech:000461` was minted after a
  gitignore-independent scan of `kb/communities` and `data/isolates` showed
  `CommunityMech:000460` as the highest existing ID.
- **Duplicate state:** no existing canonical record was found for
  `PMID:41900437`, `10.3390/microorganisms14030678`,
  `Pseudomonas sp. RF`, `Acidovorax sp. PH`, `PX736765`, `PX736766`, or
  `RF-PH` in a gitignore-independent search covering `kb`, `data`,
  `references_cache`, `history`, `reports`, generated docs, scouting queues,
  and ignored `tmp` queues.
- **Scope:** `ecological_state: ENGINEERED`,
  `community_origin: SYNTHETIC`, and `community_category: BIOREMEDIATION`
  match a two-strain, lab-assembled aniline-degradation consortium.
- **Taxonomy:** both members are curated at genus rank because the source names
  them only as Pseudomonas sp. RF and Acidovorax sp. PH after 16S rRNA
  sequencing. The NCBITaxon labels `Pseudomonas` and `Acidovorax` match the
  local id-label validator.
- **GTDB:** both genus-level GTDB blocks are coherent and bacterial:
  `GTDB:g__Pseudomonas` from `NCBITaxon:286` and `GTDB:g__Acidovorax` from
  `NCBITaxon:12916`.

## Evidence

- The assembly design is supported by exact `PMID:41900437` snippets for
  constructing the aniline-degrading synthetic consortium and for optimizing
  the RF:PH ratio to 3:1.
- The taxon entries are supported by exact snippets for 16S placement in the
  genera Pseudomonas and Acidovorax, monoculture aniline degradation by RF and
  PH, and the GenBank accessions `PX736766` and `PX736765`.
- The only curated interaction is community-level enhanced aniline degradation.
  Its evidence now covers both the 500 mg/L and 1000 mg/L comparisons against
  the RF and PH monocultures.
- The growth-medium record is limited to source-stated RF-PH conditions:
  100 mL mineral salt medium with 500 mg/L aniline, RF and PH OD600 2.0
  suspensions added by ratio, 150 rpm shake-flask cultivation, and 3 days.
- Exact reference validation passed against the committed open-access cache
  in `references_cache/PMID_41900437.txt`.

Unsupported or over-scoped claims after fixes: None found.

## Completeness

- The record includes the two final RF-PH members, final RF:PH ratio, final
  enhanced degradation outcome, mineral-salts aniline assay, primary PubMed
  resource, GTDB genus groundings, metal non-relevance, and two append-only
  history events.
- The record deliberately omits a pairwise `CROSS_FEEDING` or `SYNTROPHY`
  interaction because Pan et al. 2026 proposed cooperative and complementary
  characteristics but did not identify a transferred intermediate or a
  directional RF-to-PH or PH-to-RF mechanism.
- The record omits species-level NCBITaxon IDs and genome accessions because
  the inspected article reported genus-level 16S assignments and 16S GenBank
  accessions, not species calls or assemblies.
- The record omits a BioProject dataset because `PRJNA1186943` covers the
  source soil amplicon sequencing that guided screening, not the defined RF-PH
  consortium itself.

## Findings

| Severity | Issue | Status | Owner |
|---|---|---|---|
| Major | The draft RF-PH `growth_media` asserted `temperature: 30` and `atmosphere: AEROBIC` even though the cited 30 °C sentence supported the monoculture assay and the consortium section only stated 500 mg/L aniline, 100 mL mineral salt medium, 150 rpm, and 3 days. Filed as #1189. | Fixed by removing the unsupported fields. | `kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` |
| Major | The RF-PH enhanced-degradation description mentioned the 1000 mg/L 12 h improvement, but its evidence cited only the 500 mg/L improvement. Filed as #1190. | Fixed by adding exact 1000 mg/L evidence. | `kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` |
| Major | `strain_designation.notes` named `PX736766` for RF and `PX736765` for PH without a nearby evidence item quoting the GenBank accession sentence. Filed as #1191. | Fixed by adding the accession snippet to both taxon entries. | `kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` |
| Minor | The knowledge-gap prompt asked which metabolites or stress-protection functions are exchanged between RF and PH, assuming an exchange that the paper did not establish. Filed as #1192. | Fixed by rewording the prompt as an open mechanism question. | `kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` |

No unresolved blocker, major, or minor findings remain after the fixes above.

## Recommended Edits

None remaining.

The concrete edits from #1189, #1190, #1191, and #1192 have already been
applied to the maintained YAML, a second in-record
`FIX_ADVERSARIAL_REVIEW_FINDINGS` curation event was appended, and a second
append-only repository history file was added.

## Follow-up Checks

Completed after the fixes:

- schema validation with `linkml-validate`;
- closed-mode strict validation;
- GTDB coherence and prokaryotic-lineage validation;
- shared NCBITaxon reuse validation;
- ontology id-label validation;
- exact reference-snippet validation;
- YAML scalar validation;
- LinkML validation for both history records;
- HTML/browser regeneration;
- generated-page inspection for the added 1000 mg/L and GenBank evidence; and
- a gitignore-independent search of the maintained YAML plus generated HTML
  confirming the unsupported `30 C`/`AEROBIC` display no longer appears.

## Additional Notes

- The repo-local `just` wrappers remain blocked by the Python 3.13
  `llvmlite==0.46.0` build error. Direct validator invocations were used for
  the focused gates.
- The scouting duplicate search that established this was a novel curation
  target included ignored files with `rg --hidden --no-ignore`.
