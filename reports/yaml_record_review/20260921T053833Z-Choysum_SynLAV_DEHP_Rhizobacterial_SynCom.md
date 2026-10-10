# YAML Record Review: Choysum SynLAV DEHP-Degrading Rhizobacterial SynCom

- Repository: `CommunityMech`
- Record: `kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml`
- Started UTC: `2026-09-21T05:38:33Z`
- Finished UTC: `2026-09-21T05:38:55Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000403` |
| Label | Choysum SynLAV DEHP-Degrading Rhizobacterial SynCom |
| Maintained/generated | Maintained curated community YAML |

The record denotes the five-member SynLAV rhizobacterial synthetic community from PMID:42482240, not the sibling SynHAV community in the same paper.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | Pass: 1 file scanned, 0 error rows |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Failed with 2 label mismatches for `NCBITaxon:1827` |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml --list-mismatch --list-nocontent --list-rendering --list-assembled` | Pass: 21 `MATCH`, 0 `MISMATCH`, 0 `NOCONTENT` |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_cross_repo_ids.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` | Pass |
| History/docs presence | Missing for this new record at review time |

## Identity and Grounding

SynLAV membership is supported by supplement Table S2: Flavobacterium sp. L11, Pseudomonas sp. L29, Sphingomonas sp. L75, Rhodococcus sp. L44, and Gordonia sp. L115. The YAML correctly keeps these at NCBI genus rank because the source does not resolve the isolates below genus.

The record correctly avoids curating the supplement's phylum labels for Flavobacterium and Sphingomonas, which conflict with current taxonomy. Those source labels appear only inside exact evidence snippets.

The `Rhodococcus` NCBITaxon term is not label-canonical: the term validator reports `NCBITaxon:1827` should be labelled `Rhodococcus <high G+C Gram-positive bacteria>`.

## Evidence

Evidence is attached to the design, five member taxa, the community-level DEHP-degradation outcome, the 100 mg/kg pot soil condition, the OD600 0.2 SynCom suspension, the MSM recipe, the 100 mg/L DEHP 72 h assay, the BioProject, and the primary DOI URL.

All 21 `EvidenceItem` snippets in the YAML matched the newly committed PMID:42482240 cache. Supplement-backed snippets were also copied into `references_cache/PMID_42482240.supplement.md` and preserved under a `SUPPLEMENTARY FILE TEXT` marker in `references_cache/PMID_42482240.txt`.

One engineering claim is currently under-evidenced at its nearest slot: `inoculation_strategy` says each seedling received 5 mL, but the engineering-design evidence does not quote the 5 mL inoculation sentence even though the cached source contains it.

## Completeness

The record covers exact SynLAV membership, initial DEHP-degradation screening, non-antagonism screening, equal-ratio assembly, pot inoculation, 100 mg/kg DEHP stress, DEHP residue/accumulation endpoints, the PRJNA1263734 sequencing accession, and the 10-day targeted-ASV uncertainty for Rhodococcus/Gordonia endpoint persistence.

The sibling SynHAV community is deliberately absent and should remain a separate record if curated.

No append-only repository history entry or generated `docs/`, `pages/`, or `output/` artifact for `Choysum_SynLAV_DEHP_Rhizobacterial_SynCom` was found. This absence was checked with `find` over `history`, `docs`, `pages`, `output`, and `reports`; `find` is gitignore-independent.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | `NCBITaxon:1827` is labelled `Rhodococcus` in `taxonomy[3]` and `ecological_interactions[0].participating_taxa[3]`; the canonical NCBI label expected by the term gate is `Rhodococcus <high G+C Gram-positive bacteria>`. | `linkml-term-validator` failed with two label mismatches for `NCBITaxon:1827`. | `kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` |
| major | `ecological_interactions[0].interaction_type: MUTUALISM` overstates the DEHP outcome as a mutualistic ecological edge. The source supports individual DEHP degradation by each isolate and pot-level DEHP reduction after SynLAV inoculation, but not a benefit-bearing organism-to-organism mutualism among the five members. | Supplement Table S2 gives individual 72 h DEHP degradation rates; the main-text Results report reduced DEHP residues/accumulation under SynLAV. Neither passage establishes reciprocal benefit. | `kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` |
| major | The 5 mL per-seedling inoculation detail appears in `engineering_design.inoculation_strategy` but is not cited in `engineering_design.evidence`. | The cached source says seedlings were inoculated with 5 mL of each SynCom inoculum; no engineering-design `EvidenceItem` quotes that text. | `kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml` |
| major | This new community has no append-only repository history entry yet. | A gitignore-independent `find` over `history`, `docs`, `pages`, `output`, and `reports` found no artifact for the Choysum/SynLAV stem, `CommunityMech:000403`, or PMID:42482240 before this report was written. | `history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/` |
| major | The committed generated HTML has not been rendered for the new community yet. | The same gitignore-independent `find` found no Choysum/SynLAV or `CommunityMech:000403` page under `docs`, `pages`, or `output`. | generated `docs/` community page |

## Recommended Edits

1. Change both `NCBITaxon:1827` labels in the maintained YAML to `Rhodococcus <high G+C Gram-positive bacteria>`, then rerun the term gate.
2. Remove the unsupported `interaction_type: MUTUALISM` from the community-level DEHP-degradation interaction unless a narrower supported interaction type is introduced.
3. Add the exact 5 mL SynCom inoculation snippet to `engineering_design.evidence` or remove the 5 mL detail from `inoculation_strategy`.
4. Add the append-only history record for this creation under `history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/`.
5. Regenerate committed HTML so the new community has a current page under `docs/`.

## Follow-up Checks

- `.venv/bin/linkml-term-validator validate-data kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels`
- `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml --list-mismatch --list-nocontent --list-rendering --list-assembled`
- `.venv/bin/linkml-reference-validator validate data kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml`
- `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom/<new-history>.yaml`
- Regenerate/check docs with the repository's `gen-html` and `check-docs-current` equivalents.

## Additional Notes

Before creating the YAML, duplicate searches for the DOI, PMID, title, SynLAV/SynHAV labels, and choysum host were run with ignored and hidden files included; only generated or cache-heavy directories were excluded, and the hits were limited to scouting reports/stubs.
