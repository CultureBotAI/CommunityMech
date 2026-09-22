# YAML Record Review: PPCP Wastewater Sphingopyxis-Ochrobactrum-Apiotrichum SMC

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml
- Started UTC: 2026-09-22T12:06:12Z
- Finished UTC: 2026-09-22T12:12:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MicrobialCommunity |
| ID | CommunityMech:000420 |
| Label | PPCP Wastewater Sphingopyxis-Ochrobactrum-Apiotrichum SMC |
| Maintained path | kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml |
| Generated paths | docs/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.html, docs/browser.html, docs/index.html |
| Primary source | PMID:42526243; doi:10.1016/j.jhazmat.2026.143098 |
| Review source text | references_cache/PMID_42526243.txt |

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml` | Passed, 0 ERROR rows |
| `.venv/bin/linkml-term-validator validate-data kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed after correcting the ENVO label for `ENVO:00002001` to `waste water` |
| `.venv/bin/linkml-reference-validator validate data kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed; reported 0 issues |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-nocontent --list-rendering --list-assembled kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml` | Passed; 17 MATCH, 0 RENDERING, 0 ASSEMBLED, 0 WEAK, 0 MISMATCH, 0 NOCONTENT |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml` | Passed |
| `.venv/bin/linkml-validate -s src/communitymech/schema/history.yaml history/records/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC/2026-09-22T120612Z-codex-420.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed; rendered 410 community pages |
| `PYTHONPATH=src .venv/bin/python -m communitymech.cli audit-network --json` | No finding for this record; exited 1 because of pre-existing findings in unrelated records |
| `git diff --check` | Passed |

Skipped or unavailable:

- `scripts/gtdb_ground.py --community ... --apply` could not run because the local KG-Microbe `NCBI2GTDB.tsv.gz` crosswalk was absent from every default sibling path tried by the script. The three genus-level taxa therefore remain explicitly `UNRESOLVED`; coherence and prokaryotic-lineage validators accept that state.
- `just new-history` could not scaffold the history record because `uv run` tried to build `llvmlite==0.46.0` under the local Python 3.13 environment and hit `Popen.__init__() got an unexpected keyword argument 'dry_run'`. The replacement hand-written history record validates against the vendored history schema.

## Identity and Grounding

- The PMID cache identifies the article as *A synthetic microbial community for the enhanced removal of complex emerging pollutants from domestic wastewater* in *Journal of Hazardous Materials*, DOI `10.1016/j.jhazmat.2026.143098`, PMID `42526243`.
- The cached abstract directly identifies an SMC comprising `Sphingopyxis sp. GC21`, `Ochrobactrum sp. TCC-2`, and `Apiotrichum sp. IB-1`, and directly names chloramphenicol, triclocarban, and naproxen as the three target PPCPs.
- NCBITaxon, ENVO, GO, and CHEBI labels in the record pass the term-label validator.
- A gitignore-independent search with `rg --no-ignore --hidden` found `PMID:42526243`, `10.1016/j.jhazmat.2026.143098`, and the target slug only in the new record, new history, new generated pages, new PubMed cache, and pre-existing scout scratch files. No prior curated `kb/` or `data/` record for this article was found.

## Evidence

- All 17 snippets in the current record are exact whitespace-normalized matches against `references_cache/PMID_42526243.txt`.
- The membership, target PPCP, wastewater, aerobic/anoxic endpoint, reactor-colonization, DOI, and title claims are all backed by the cached abstract.
- The record correctly does not assert the simulated wastewater recipe, inoculation ratio, hydraulic setup, or strain-by-strain PPCP reaction allocation, none of which are available from the cached abstract.

## Completeness

- The source record is complete enough for an abstract-backed entry: exact three-member SMC membership, three grounded target PPCPs, simulated and real wastewater context, aerobic/anoxic removal endpoints, stable PMID/DOI links, and a concrete discussion gap for inaccessible reactor and mechanistic details.
- `growth_media` and `cultivation_setup` are intentionally absent because the PubMed abstract does not report the recipe, volumes, inoculation ratios, or operating parameters.
- Associated datasets were not curated because the PubMed abstract does not report a stable accession.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Taxon-level `functional_role: PRIMARY_DEGRADER` over-allocates an aggregate SMC activity to each named strain. | PMID:42526243 says the introduced Sphingopyxis, Ochrobactrum, and Apiotrichum were collectively responsible for CAP/TCC/NPX transformations, but the cached abstract does not allocate those transformations strain by strain. | kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml |
| Major | `abundance_level: DOMINANT` is asserted for all three taxa without a source-supported ordinal abundance basis. | The abstract reports introduced genus relative abundances in the SMC reactor of Sphingopyxis 6.45%, Ochrobactrum 0.23%, and Apiotrichum 51.06%; those values do not support declaring all three co-dominant. | kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml |
| Minor | The engineering design lists mobile genetic element, pathogen, and ARG responses as measurement endpoints but does not cite the abstract sentence supporting that endpoint. | The cache has a direct sentence that SMC alleviated pollutant-imposed selection pressure, reduced mobile genetic elements and pathogens, and suppressed ARG dissemination. | kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml |

## Recommended Edits

1. In `kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml`, remove `functional_role: PRIMARY_DEGRADER` from the three taxonomy entries or move the degradation role to a community-level assertion only.
2. In the same file, remove the unsupported `abundance_level: DOMINANT` assignments from the three taxonomy entries unless a full-text source establishes an initial equal inoculation ratio or another defensible closed-SMC abundance basis.
3. In the same file, add a third `engineering_design.evidence` item that quotes the abstract's mobile genetic element, pathogen, and ARG sentence.

## Follow-up Checks

- Re-run LinkML, strict, scalar, term, snippet, GTDB, shared-taxon, prokaryotic-lineage, history, render, network, and `git diff --check` after the recommended edits.
- Re-read the taxonomy entries and engineering evidence to confirm no per-strain PPCP role remains and the ARG endpoint is supported at the field where it appears.

## Additional Notes

- The DOI and PMID were not present in curated `kb/` or `data/` records before this record was added; the duplicate search included ignored and hidden files.
- The broader network audit reports known unrelated findings for `Algal_Methanotroph_Biogas_Valorization_Coculture`, `Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom`, `Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom`, `Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom`, and `Space_Habitat_SevenMember_Stress_Tolerance_SynCom`.
