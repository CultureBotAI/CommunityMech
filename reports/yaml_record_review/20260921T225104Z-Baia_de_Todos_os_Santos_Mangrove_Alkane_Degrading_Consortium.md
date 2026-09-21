# YAML Record Review: Baia de Todos os Santos Mangrove Alkane-Degrading Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml`
- Started UTC: 2026-09-21T22:50:00Z
- Finished UTC: 2026-09-21T22:51:04Z
- Verdict: needs curation

## Target

Maintained `MicrobialCommunity` record:

- ID: `CommunityMech:000413`
- Label: `Baia de Todos os Santos Mangrove Alkane-Degrading Consortium`
- Class: `MicrobialCommunity`
- Maintained path: `kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml`
- Generated page: `docs/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.html`
- Primary source: `PMID:41893893`

The record denotes the 36-organism petroleum-contaminated mangrove consortium described in PMID:41893893, with only the nine Table 1 representative strains curated because the remaining members are not named in the inspected article text or table page.

## Validation

Focused validation run during review:

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml` | Pass |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml` | Pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium/2026-09-21T224917Z-claude-code-d532cf.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml history/records/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium/2026-09-21T224917Z-claude-code-d532cf.yaml` | Pass |

The equivalent `just validate`, `just validate-strict`, `just validate-gtdb`, and `just validate-references-explained` wrappers did not reach these validators because `uv run` attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before running CommunityMech code. Direct `.venv` invocations covered the same focused checks.

## Identity and Grounding

The record identity is defensible: PMID:41893893 describes a patented 36-member consortium isolated from Baia de Todos os Santos and selects nine bacterial strains for Table 1 taxonomic identification, genome sequencing, and paraffinic-oil alkane-degradation analysis.

Taxonomy is intentionally conservative. The source table reports genus-level TaxIDs for Brevibacillus, Pseudomonas PD6/PD7, and Stenotrophomonas RC6/PD5/PD8, so the record keeps these strains at genus rank even where the table gives a closest-relative species name. Existing repo-vetted GTDB genus blocks were reused for those three NCBI genus IDs; the two `NCBITaxon:427562` Bacillus rows are unresolved because no fresh local GTDB crosswalk was available.

## Evidence

The Table 1 image from the Springer table page was transcribed into `references_cache/PMID_41893893.txt`, allowing every sample-code row to validate as an exact snippet. Methods, Results, and Conclusions snippets were matched from the Europe PMC full-text cache.

Community-level synergy, rapid/delayed alkane-degradation timing, the Bushnell-Haas crude-oil batch assay, and 31-day GC-FID endpoints are all grounded to narrow snippets from the source article. No pairwise interaction was asserted, which is appropriate because the paper reports genus-level ecological roles rather than exact directional metabolite transfer between two named strains.

## Completeness

The record correctly leaves public sequencing datasets absent: the paper reports that generated/analyzed datasets are available from the corresponding author on reasonable request and does not provide a BioProject, SRA, or assembly accession.

The record correctly carries a discussion for the 27 unnamed members of the patented 36-organism source consortium. Ignored-file-inclusive searches for `41893893`, `10.1007/s00284-026-04858-6`, and the paper title found no maintained duplicate community record under `kb/communities/`, `data/isolates/`, `history/`, or `references_cache/` before creation.

## Findings

### minor: RA2 note lists an unused source TaxID without explaining the conservative genus grounding

- Maintained owner: `kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml`
- Evidence: Table 1 reports `RA2 MW881196 Pseudomonas cedrina 1453560`, while a live NCBI Taxonomy check resolved `1453560` as `Pseudomonas sp. Sp03`, not `Pseudomonas cedrina`.
- Problem: RA2 is correctly grounded to the broader genus `NCBITaxon:286`, but the note says only that Table 1 reported Taxon ID 1453560. Without the reason for not reusing that source TaxID, future readers could read the broader grounding as accidental drift.

### minor: the open discussion overstates the bounded missing-member search

- Maintained owner: `kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml`
- Evidence: the review inspected the committed PubMed/PMC cache, PMC XML, Springer article HTML, and Springer full-size Table 1 page for the 27 additional members.
- Problem: the discussion rationale says the remaining members were absent from the PDF too. The PDF was downloaded, but its full text was not parsed or OCR-audited for this negative claim.

## Recommended Edits

1. Update the RA2 taxon note to state that Table 1's source TaxID 1453560 resolves to `Pseudomonas sp. Sp03` in NCBI Taxonomy, so RA2 is curated at the supported `Pseudomonas` genus.
2. Remove the unsupported `PDF` portion of the bounded negative search from the unresolved-36-member discussion rationale.

## Follow-up Checks

After edits:

- `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml`
- `.venv/bin/linkml-term-validator validate-data kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels`
- `.venv/bin/linkml-reference-validator validate data kb/communities/Baia_de_Todos_os_Santos_Mangrove_Alkane_Degrading_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml`
- Regenerate HTML and confirm the generated page reflects the tightened note and discussion text.

## Additional Notes

None found.
