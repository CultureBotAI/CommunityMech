# YAML Record Review: Rhodococcus-Acinetobacter RAMC Mixed Plastic Upcycling SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml
- Started UTC: 2026-09-21T21:00:00Z
- Finished UTC: 2026-09-21T21:02:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MicrobialCommunity |
| ID | CommunityMech:000412 |
| Label | Rhodococcus-Acinetobacter RAMC Mixed Plastic Upcycling SynCom |
| Maintained path | kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml |
| Generated page | docs/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.html |
| Source | Diao et al. 2025, PMID:41381587, PMCID:PMC12816627, DOI:10.1038/s41467-025-67409-w |
| Scope | Bottom-up, two-member Rhodococcus jostii strain PET / Acinetobacter baylyi ADP1 synthetic consortium for mixed-plastic oxygenate consumption and RAMC-P product conversion |

The record is a maintained community YAML file, not a generated transform. The HTML page and `docs/browser.html` are generated from the YAML and should be regenerated after fixes.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml` | Pass |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom/2026-09-21T205633Z-codex-9d823a.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml --out /tmp/communitymech_ramc_strict.tsv` | Pass, 0 ERROR rows |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml history/records/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom/2026-09-21T205633Z-codex-9d823a.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml` | Pass |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `git diff --check` | Pass |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Pass, rendered 402 communities and generated the new RAMC HTML page |

## Identity and Grounding

The record identity matches the primary paper. The PubMed, DOI, and PMC identifiers resolve in the cached Europe PMC/PubMed/PMC XML material, and the record correctly denotes the RAMC/RAMC-P two-member synthetic consortium rather than a natural plastic-waste enrichment or a single-species engineered strain.

The member identities are appropriately bounded:

| Member | Grounding review |
|---|---|
| Rhodococcus jostii strain PET | Supported by the methods statement naming WT Rhodococcus jostii strain PET from the in-house collection. NCBITaxon:132919 resolved by an exact NCBI scientific-name lookup; GTDB is explicitly left UNRESOLVED because the local NCBI2GTDB crosswalk was absent. |
| Acinetobacter baylyi ADP1 | Supported by the methods statement naming WT Acinetobacter baylyi ADP1 and ATCC 33305. NCBITaxon:202950 and the reused Acinetobacter baylyi GTDB block are coherent. |

An ignored-inclusive search covering the repository except `.git`, `.venv`, and `tmp` for `41381587`, `s41467-025-67409-w`, `Rhodococcus_Acinetobacter_RAMC`, `mixed plastic upcycling`, and `CommunityMech:000412` found only the new maintained record, its new history/cache/generated files, the prior scout stub, and generated page references. No preexisting maintained duplicate record was found in that search.

## Evidence

Supported:

- The SR/SA bottom-up division of labor is directly supported by the paper's statements that RAMC consists of Rhodococcus jostii strain PET and Acinetobacter baylyi ADP1 and that the strains specialize in aromatic and aliphatic carboxylic acid degradation, respectively.
- The initial SR:SA ratio series, OD600 0.2 total inoculum, 30 C / 250 rpm cultivation, 50 mL glass tubes, 10 mL working volume, 1 g/L ammonium sulfate, and simulated mixed-plastic stock composition all have exact Methods support.
- The 125-750 mM simulated-carbon envelope is supported by the full-text result and Methods paragraphs.
- The record correctly avoids asserting a directional succinate cross-feeding edge and keeps the succinate-node relationship as an open Discussion.

Unsupported or under-supported:

- `cultivation_setup[0].system_type` standardizes 50 mL glass tubes as `FLASK`; the source says glass tubes, and `CultivationSystemEnum.FLASK` is described as an Erlenmeyer / shake flask.
- The only grounded metabolites on the community-level DOL edge are the aromatic substrates terephthalic acid and benzoic acid. The Acinetobacter/aliphatic half of the same edge should ground acetic acid, lactic acid, succinic acid, glutaric acid, adipic acid, and pimelic acid too.
- The RAMC-P_9/1 engineered derivative and lycopene/lipid production claims are in the source, but the engineering-design evidence currently stops at wild-type RAMC assembly and specialist selection. The exact SR-P/SA-P assembly and RAMC-P_9/1 product passages should be cached and cited at that node.

## Completeness

The record is complete enough on identity, member count, source provenance, and baseline simulated-medium cultivation. The following consequential gaps remain:

- Standardized aliphatic metabolite grounding is missing from both `ecological_interactions[0].metabolites` and most of `growth_media[0].composition`.
- RAMC-P-specific genetic construction and product-conversion claims need narrow evidence.
- No fed-batch or continuous cultivation should be added: the paper explicitly discusses submerged fed-batch validation as future work, not as performed RAMC work.

Optional slots correctly left empty:

- No pairwise succinate cross-feeding interaction should be asserted from the current paper.
- No Rhodococcus jostii GTDB classification should be fabricated while the local NCBI2GTDB crosswalk is absent.
- No `modeled_environment` term was obvious from the article for this de novo laboratory upcycling platform.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | `cultivation_setup[0].system_type` uses `FLASK` for 50 mL glass tubes. `FLASK` is the schema term for Erlenmeyer / shake flasks; this experiment used glass tubes shaken in a benchtop incubator, so the standardized slot should be `OTHER` with the existing detail retained. | PMID:41381587 Methods; `CultivationSystemEnum` in `src/communitymech/schema/communitymech.yaml` | `kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml` |
| major | The aliphatic half of the aromatic/aliphatic DOL is ungrounded. The edge grounds terephthalic and benzoic acids but omits the Acinetobacter-side aliphatic acids even though the description and source make those acids central substrates. | PMID:41381587 names acetic, lactic, succinic, glutaric, adipic, and pimelic acids in the simulated oxygenate stock and uses C4-C7 DCAs plus AA/LA to model PE/PP variability. | `kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml` |
| major | RAMC-P product claims are under-evidenced at `engineering_design`. The record says RAMC-P_9/1 uses engineered SR-P/SA-P to produce lycopene and lipids from real mixed-plastic effluents, but the local engineering-design evidence only cites wild-type RAMC construction and specialist substrate selection. | PMID:41381587 reports assembly of the SR-P/SA-P coculture as RAMC-P, selection of RAMC-P_9/1, and product measurements in BM and altered PET/PS/PE/PP real-plastic conditions. | `kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml`; `references_cache/PMID_41381587.txt` for exact source excerpts |

## Recommended Edits

1. In `kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml`, change `cultivation_setup[0].system_type` from `FLASK` to `OTHER` and keep `instrument_detail: 50 mL glass tubes shaken in a benchtop incubator`.
2. Ground the Acinetobacter-side aliphatic acids by adding CHEBI-backed metabolite descriptors for acetic acid, lactic acid, succinic acid, glutaric acid, adipic acid, and pimelic acid to `ecological_interactions[0].metabolites`, and by adding matching `chebi_term` blocks to their `growth_media[0].composition` entries.
3. Add a compact RAMC-P evidence item under `engineering_design.evidence` from the source passage that assembles SR-P and SA-P as RAMC-P and selects RAMC-P_9/1, plus a compact evidence item for the BM product assay.
4. Append the exact supporting RAMC-P excerpts to `references_cache/PMID_41381587.txt` without mixing in supplementary-material text.
5. Regenerate `docs/` and append a new `history/records/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom/*.yaml` entry for the edit.

## Follow-up Checks

- `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml --out /tmp/communitymech_ramc_strict_after_review.tsv`
- `.venv/bin/linkml-term-validator validate-data kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels`
- `.venv/bin/linkml-reference-validator validate data kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom.yaml history/records/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom/*.yaml`
- `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Rhodococcus_Acinetobacter_RAMC_Mixed_Plastic_Upcycling_SynCom/*.yaml`
- `git diff --check`
- `PYTHONPATH=src .venv/bin/python -m communitymech.render`

## Additional Notes

The configured reference-validator run succeeded after the cache/snippet normalization fixes, but `Discussion.evidence` uses the shared `SupportingReference` class and is not checked by `linkml-reference-validator`; the succinate-node snippet was therefore manually compared with `references_cache/PMID_41381587.txt`.

The local `.venv/bin/runoak -i ols:chebi search ...` calls returned the needed glutaric, adipic, pimelic, and lactic acid CHEBI candidates before the OLS client timed out. Validate final CHEBI choices with the term validator after editing rather than relying on the timed-out process exit status.
