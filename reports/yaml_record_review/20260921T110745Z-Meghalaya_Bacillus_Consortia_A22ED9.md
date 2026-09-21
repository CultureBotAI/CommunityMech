# YAML Record Review: Meghalaya Bacillus Consortia-A22ED9

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml`
- Started UTC: 2026-09-21T11:07:45Z
- Finished UTC: 2026-09-21T11:08:35Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000406` |
| Label | Meghalaya Bacillus Consortia-A22ED9 |
| Maintained path | `kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` |
| Generated | No |
| Primary source | `PMID:42135302`; DOI `10.1038/s41598-026-49136-4`; PMC `PMC13443631` cached in `references_cache/PMID_42135302.txt` |
| Scope | Two-member Bacillus sp. SK22 plus Bacillus sp. KHED9 synthetic consortium for pH-5.0 in vitro Fe, Cr, and Cd removal |

The target is a maintained community record for Consortia-A22ED9, one of the
two pairwise consortia built by Ka-Ot et al. 2026. It is not the sibling
Consortia-B18-4M11, the five-isolate input panel, or a field AMD community.

A gitignore-independent `rg -uu --hidden` search over `kb`, `data`, `reports`,
`research`, `history`, and `references_cache` for `CommunityMech:000406`,
`PMID:42135302`, `10.1038/s41598-026-49136-4`, `A22ED9`, `KX896657`, and
`MK554507` found no existing curated `kb` or `data` record before this branch;
pre-curation hits were confined to scout queue/stub files and the source cache.
Ignored and hidden files were included.

## Validation

`just` wrappers were unavailable in this checkout where they invoked
`uv run`: `uv` attempted to build `llvmlite==0.46.0` for Python 3.13 and the
build failed with `TypeError: Popen.__init__() got an unexpected keyword
argument 'dry_run'`. Direct `.venv` equivalents were used where possible.

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` | pass; 0 ERROR rows |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml -s src/communitymech/schema/communitymech.yaml --labels` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` | pass; 19 MATCH / 0 RENDERING / 0 ASSEMBLED / 0 WEAK / 0 MISMATCH / 0 NOCONTENT |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | pass but non-substantive; reported `Total checks: 0` |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Meghalaya_Bacillus_Consortia_A22ED9/2026-09-21T110007Z-claude-code-ff9f69.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/taxon_absent_from_source.py kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` | pass for A22ED9; corpus-level output listed older non-A22ED9 defects only |
| `PYTHONPATH=src .venv/bin/python -m communitymech.cli audit-network --json` | pass for A22ED9; corpus-level output listed 13 older warnings only |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | pass; rendered 396 community pages plus browser and landing pages |
| `PYTHONPATH=src .venv/bin/python -m pytest tests/test_id_uniqueness.py tests/test_no_case_conflicting_cache_pairs.py tests/test_cache_is_source_text_not_notes.py tests/test_no_paywalled_text_in_repo.py tests/test_reference_cache_resolution.py tests/test_snippet_truncation.py tests/test_snippets_are_not_truncated.py -q` | 450 pass; 2 local-environment failures from the `uv run` isolate-schema subprocess and pre-existing untracked PDFs under `tmp/` / `references_cache/files/` |
| Direct `.venv/bin/linkml-validate` over all four `data/isolates/*.yaml` files | pass; confirms the `test_isolates_pass_schema_validation` failure was the `uv run` build path |
| `git diff --check` and `git diff --cached --check` | pass |

## Identity and Grounding

The identity is sound. `ENGINEERED`, `SYNTHETIC`, and `BIOREMEDIATION` match a
defined laboratory consortium deliberately assembled from two screened isolates
for heavy-metal removal. The record correctly uses `ENVO:01001405` laboratory
environment for the physical assay and uses `ENVO:00001997` acid mine drainage
only as the modeled context.

The two members are exactly the source members of Consortia-A22ED9:

- `Bacillus sp. SK22` from active mine sites, 16S accession `KX896657`
- `Bacillus sp. KHED9` from active mine sites, 16S accession `MK554507`

Both are conservatively grounded at genus rank to `NCBITaxon:1386` with the
canonical `Bacillus <firmicutes>` label. GTDB grounding is explicitly
`UNRESOLVED` because the local NCBI2GTDB table was unavailable; no finer
species or genome assertion is made.

## Evidence

Supported claim groups:

- The engineering design cites the 16-isolate screen, the five-isolate
  shortlist, the SK22/KHED9 compatibility result, and the 1 mL + 1 mL OD600 0.5
  construction method.
- Both taxon entries cite the exact sentence that names SK22 and KHED9 as
  active-mine Bacillus sp. isolates and gives their GenBank accessions.
- The community-level interaction cites source snippets for A22ED9's mean Fe,
  Cr, and Cd removal percentages.
- The environmental factors preserve pH 5.0 and the 50-1000 mg/L Fe and
  1-32 mg/L Cr/Cd concentration ranges.
- The growth-medium record cites the 100 mL LB, 250 mL flask, 37 degrees
  Celsius, 150 rpm, 24 h, 1% v/v inoculation conditions.
- DOI, PMID, and PMCID external resources all point to stable primary-source
  identifiers rather than to generated summaries.

Unsupported or over-scoped claims:

- None found at finding severity. The first curation draft over-described the
  consortium as pH-neutralizing and used a Cd snippet with insufficient local
  context; both were fixed before this review report.

One low-scope ambiguity remains: the `Fe-Cd-Cr removal` strings in the
interaction and growth-medium names could be read as a simultaneous mixed-metal
assay, while the record body and Table 3 evidence support separate Fe, Cr, and
Cd concentration series.

## Completeness

The record is complete enough for the article. It captures the bounded
two-member community, the active-mine strain sources, the equal-volume assembly
method, the pH-5.0 LB assay geometry and challenge ranges, the measured Fe/Cr/Cd
removal outcomes, the primary DOI/PMID/PMCID, and two open questions: species
resolution/field performance and the lack of demonstrated emergent consortium
advantage.

Appropriately absent fields:

- `associated_datasets`: the inspected source reports 16S nucleotide
  accessions, not SRA, BioProject, metagenome, or model accessions.
- species-rank NCBITaxon and genomes: the article names SK22 and KHED9 as
  `Bacillus sp.` isolates and reports 16S accessions only.
- `metals_present: CADMIUM`: cadmium is curated as `CHEBI:48775` in the
  interaction because `MetalElementEnum` has no cadmium value.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| minor | The names `Consortia-A22ED9 Fe-Cd-Cr removal` and `pH 5.0 LB Fe-Cd-Cr removal assay` may imply that Fe, Cd, and Cr were co-supplied in one mixed-metal treatment rather than in the separately summarized Fe, Cr, and Cd concentration series in Table 3. | `kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` |

No blocker or major findings.

## Recommended Edits

Rename the interaction and growth-medium labels in
`kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml` to say
`single-metal`, update the discussion attachment to the renamed interaction,
append a curation-history event, and regenerate
`docs/communities/Meghalaya_Bacillus_Consortia_A22ED9.html`.

## Follow-up Checks

After the recommended edit, rerun:

- `.venv/bin/linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml`
- `.venv/bin/linkml-term-validator validate-data kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml -s src/communitymech/schema/communitymech.yaml --labels`
- `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml`
- `PYTHONPATH=src .venv/bin/python -m communitymech.render`
- `git diff --check`
- `git diff --cached --check`

## Additional Notes

`references_cache/PMID_42385706.txt`, `references_cache/PMID_42613016.txt`,
and the untracked PDFs under `references_cache/files/` were already present in
the worktree and are unrelated to this record.
