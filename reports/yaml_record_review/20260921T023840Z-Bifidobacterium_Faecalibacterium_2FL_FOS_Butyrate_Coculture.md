# YAML Record Review: Bifidobacterium-Faecalibacterium 2′-FL/FOS Butyrate Coculture

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml`
- Started UTC: 2026-09-21T02:38:40Z
- Finished UTC: 2026-09-21T02:39:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000401` |
| Label | `Bifidobacterium-Faecalibacterium 2′-FL/FOS Butyrate Coculture` |
| Path | `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` |
| Maintained or generated | Maintained YAML record |
| Primary source | `PMID:42655156`, `doi:10.3390/microorganisms14081812` |

The record denotes a defined, two-strain anaerobic laboratory coculture of
`Bifidobacterium bifidum JCM1254` and `Faecalibacterium prausnitzii A2-165`
grown in YCFA− medium with reciprocal 2′-FL/FOS ratios at 0.5% total
carbohydrate.

## Validation

| Check | Result |
|---|---|
| `just validate kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Failed before validation; `uv run` attempted to build `llvmlite==0.46.0` and hit `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. |
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Passed: `No issues found`. |
| `just validate-strict kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Failed before validation with the same `uv` / `llvmlite` build error. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Passed: 0 incoherent blocks, malformed lineages, or lineage conflicts. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Passed: 0 truncated scalars. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Passed: 0 reused IDs. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Passed: 0 contradictory lineages. |
| `just validate-terms kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Failed before validation with the same `uv` / `llvmlite` build error. |
| `just validate-references-explained kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Failed before validation with the same `uv` / `llvmlite` build error. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Completed but reported 0 checks, so it did not prove snippet support for this record. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-nocontent --list-rendering --list-assembled kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` | Passed: 29 evidence snippets scanned; 29 `MATCH`, 0 `RENDERING`, 0 `ASSEMBLED`, 0 `WEAK`, 0 `MISMATCH`, 0 `NOCONTENT`. |
| `just validate-history history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-09-21T023720Z-codex-64dd83.yaml` | Failed before validation with the same `uv` / `llvmlite` build error. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-09-21T023720Z-codex-64dd83.yaml` | Passed. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed and rendered 391 community pages, including the new page. |
| `PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | Passed. |
| `git diff --check` | Passed. |
| Manual `docs/communities/*.html` orphan-page check | Passed: no published community pages lacked backing `kb/communities/*.yaml` records. |

## Identity and Grounding

The record identity is sound:

- `CommunityMech:000401` was not present in `kb/communities/`, `data/isolates/`,
  or `kb/taxa/`.
- The selected paper’s PMID, DOI, title phrases, member pair, and
  `2'-Fucosyllactose` string were searched with `rg -uu` over the checkout;
  ignored and hidden files were included, and no exact pre-existing record for
  `PMID:42655156` or `doi:10.3390/microorganisms14081812` was found.
- `Bifidobacterium bifidum JCM1254` is source-named and grounded to
  `NCBITaxon:1681` with an existing species-level GTDB mapping.
- `Faecalibacterium prausnitzii A2-165` / `JCM31915` is source-named and
  grounded to `NCBITaxon:853`. The `UNRESOLVED` GTDB fallback mirrors
  `Amsterdam_10Species_Gut_Invasion_SynCom.yaml`; a gitignore-independent
  `find` search of accessible paths under `/Users/marcin/Documents/VIMSS/ontology/KG-Hub`
  did not locate `NCBI2GTDB.tsv.gz`, though the search hit permission denials in
  unrelated sibling directories.
- The actual environment is correctly modeled as `ENVO:01001405` laboratory
  environment, with `ENVO:2100002` intestine environment only in
  `modeled_environment`.

## Evidence

Supported:

- The taxon list is supported by the exact Materials and Methods strain line.
- 2′-FL/FOS ratios, YCFA−, 0.5% total carbohydrate, and the 48-well-plate
  vessel are supported by the growth-experiment methods.
- qPCR and organic-acid endpoints are supported by Methods 2.3 and 2.4.
- The 10% 2′-FL / 90% FOS butyrate maximum is directly supported by Results
  3.3 and the Conclusions.
- The pH, residual-substrate, and direct-flux limitations are directly
  supported by the Discussion limitation paragraph.
- All 29 snippets in the current YAML match `references_cache/PMID_42655156.txt`
  exactly after whitespace normalization.

Unsupported, over-scoped, or too weakly placed:

- See findings `major-01`, `minor-01`, and `minor-02`.

## Completeness

Complete enough:

- The record has a DOI and PubMed primary publication.
- It records exact strain names and culture collection IDs.
- It records the modeled gut environment separately from the physical laboratory
  environment.
- It records the YCFA− 48-well batch setup, substrate ratio perturbation, qPCR
  composition readout, and organic-acid outputs.
- It carries an explicit knowledge-gap discussion for pH, residual 2′-FL/FOS,
  and stable-isotope flux, which the source named as limitations.
- It omits a CHEBI grounding for `fructooligosaccharides`; that is preferable
  to asserting an unverified or too-narrow FOS structure.
- It omits associated datasets; the paper points only to the article and its
  supplementary Figure S1 rather than a stable repository accession.
- It omits metal and rare-earth claims; none are relevant to this dietary
  prebiotic coculture.

Remaining curation needed:

- The pairwise cross-feeding metabolite list needs tightening.
- The FOS related-ingredient evidence should cite the FOS-growth result.
- The 48-well working-volume field should not imply that the final co-culture
  volume was 800 µL.

## Findings

| Severity | ID | Finding | Maintained owner |
|---|---|---|---|
| major | major-01 | `ecological_interactions[1].metabolites` lists lactate and butyrate on a `B. bifidum` → `F. prausnitzii` pairwise cross-feeding edge even though the source only infers that acetate “and possibly other fermentation products” from `B. bifidum` may contribute to `F. prausnitzii` butyrate formation. Lactate was measured, and butyrate was the terminal output, but neither is shown as the transferred Bifidobacterium-to-Faecalibacterium metabolite on that exact edge. | `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` |
| minor | minor-01 | The community-level ratio-dependent butyrate interaction cites the observed butyrate peak and the non-growth-proportional result, but the description’s stronger interpretation about a balance between FOS-maintained `F. prausnitzii` and `B. bifidum` metabolites should also cite the Discussion or Conclusions text that makes that interpretation. | `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` |
| minor | minor-02 | `related_ingredients[1]` says FOS “supported F. prausnitzii growth,” but its only evidence is the methods sentence saying the 2′-FL/FOS ratios were varied. The source does support the claim via the Results 3.1 `F. prausnitzii` growth sentence; the evidence should be moved or duplicated there. | `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` |
| minor | minor-03 | `cultivation_setup[0].working_volume` is `800` µL while the co-culture received `8 μL` of each species into `800 μL` medium. The note says “800 μL batch culture even though 16 μL total inoculum was added,” but the final co-culture working volume is 816 µL if the inoculum is included. | `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml` |

No blocker findings.

## Recommended Edits

1. In `kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml`, narrow `ecological_interactions[1].metabolites` to acetate unless a directly supported lactate-transfer or butyrate-transfer claim is added from the paper.
2. Add the Conclusions or Discussion “substrate complementarity and metabolite-mediated interactions” snippet to the community-level ratio-dependent butyrate interaction.
3. Add the `F. prausnitzii` FOS-containing growth snippet to the fructooligosaccharides related ingredient.
4. Either change `cultivation_setup[0].working_volume` to 816 µL, or leave it empty and keep the source-stated 800 µL medium plus two 8 µL inocula in `instrument_detail` / `notes`.

## Follow-up Checks

- Re-run direct schema validation: `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml`.
- Re-run strict checks: `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml`.
- Re-run term validation: `.venv/bin/linkml-term-validator validate-data kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels`.
- Re-run snippet audit: `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-nocontent --list-rendering --list-assembled kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml`.
- Re-render docs with `PYTHONPATH=src .venv/bin/python -m communitymech.render` and rerun `git diff --check`.

## Additional Notes

- The official `just` wrappers for focused validation are currently blocked by
  an environment failure in `uv` dependency resolution for `llvmlite==0.46.0`
  under Python 3.13. Direct `.venv` invocations were used for the underlying
  validation tools where possible.
- The initial guarded write produced YAML aliases for reused evidence objects;
  the record was rewritten through the guarded writer with shared object
  identity broken before this review.
