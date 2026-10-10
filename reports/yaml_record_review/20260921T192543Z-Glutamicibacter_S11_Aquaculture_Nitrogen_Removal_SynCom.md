# YAML Record Review: Glutamicibacter S11 Aquaculture Nitrogen Removal SynCom

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml`
- Started UTC: 2026-09-21T19:16:00Z
- Finished UTC: 2026-09-21T19:25:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| Maintained path | `kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` |
| ID | `CommunityMech:000411` |
| Label | `Glutamicibacter S11 Aquaculture Nitrogen Removal SynCom` |
| Category / origin / state | `BIOREMEDIATION` / `SYNTHETIC` / `ENGINEERED` |
| Members | `Glutamicibacter arilaitensis NFB2-4`; `Glutamicibacter nicotianae CYN-C5` |
| Primary reference | `PMID:41260371`; DOI `10.1016/j.biortech.2025.133683` |
| Generated? | No. Canonical curated YAML; generated HTML lives under `docs/`. |

The record denotes a two-member synthetic consortium, S11, constructed from the two named `Glutamicibacter` strains to remove ammonium and nitrite nitrogen from aquaculture wastewater. It is not an isolate record, a broad aquaculture community, or a generated copy.

The append-only history entry exists at `history/records/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom/2026-09-21T191424Z-codex-a7d4c2.yaml` and records the creation of `CommunityMech:000411`.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` | Passed: `No issues found` |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom/2026-09-21T191424Z-codex-a7d4c2.yaml` | Passed: `No issues found` |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml --out /tmp/communitymech_s11_strict.tsv` | Passed: 1 file scanned, 0 files with errors |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml history/records/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom/2026-09-21T191424Z-codex-a7d4c2.yaml` | Passed: 2 files checked, 0 truncated scalars |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` | Passed: 1 file checked, 0 reused IDs |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` | Passed: 1 file checked, 0 contradictory lineages |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed: rendered all 401 community pages plus browser and landing pages |
| `git diff --check`; `git diff --cached --check` | Passed before commit |
| `PYTHONPATH=src .venv/bin/pytest tests/test_id_uniqueness.py tests/test_no_duplicate_yaml_keys.py tests/test_docs_do_not_contradict_the_kb.py` | 1250 passed / 1 failed. The failure is unrelated to this record: `test_isolates_pass_schema_validation` shells out via `uv run`, and local `uv` cannot build `llvmlite==0.46.0` under Python 3.13. The four isolate records surfaced by that test all passed direct `.venv/bin/linkml-validate`. |

Not checked:

- `just qc`, `just validate`, `just validate-strict`, and other `uv run`-based recipes were not used for final judgement because this local `uv` environment fails while building `llvmlite==0.46.0`.
- A full-text or PDF check of the Elsevier article was not possible through open sources. Europe PMC returned `isOpenAccess=N`, `inPMC=N`, and `hasPDF=N`.
- GTDB species grounding could not be completed because the local `kg-microbe/data/raw/NCBI2GTDB.tsv.gz` crosswalk was absent; the record explicitly marks both member species `gtdb_grounding_status: UNRESOLVED`.

## Identity and Grounding

The PubMed XML for `PMID:41260371` resolves to:

- title: "A synthetic Glutamicibacter consortium efficiently removes ammonium and nitrite from aquaculture wastewater."
- journal: `Bioresource technology`, volume 442, page/article 133683
- electronic article date: 2025-11-17
- PubMed article ID: `41260371`
- DOI: `10.1016/j.biortech.2025.133683`

Europe PMC also resolves the same PMID and DOI, while reporting that the article is not open access, not in Europe PMC full text, not in PMC, and has no PDF exposed there.

NCBI Taxonomy exact scientific-name searches resolved:

- `Glutamicibacter arilaitensis[Scientific Name]` -> `256701`; efetch reports `ScientificName` = `Glutamicibacter arilaitensis`, rank `species`, lineage under `Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales; Micrococcaceae; Glutamicibacter`.
- `Glutamicibacter nicotianae[Scientific Name]` -> `37929`; efetch reports `ScientificName` = `Glutamicibacter nicotianae`, rank `species`, lineage under the same genus.

`ENVO:01001405` / `laboratory environment`, `CHEBI:28938` / `ammonium`, `CHEBI:16301` / `nitrite`, `GO:0019329` / `ammonia oxidation`, and `GO:0019333` / `denitrification pathway` passed the label gate.

An ignored-inclusive search for `CommunityMech:000411`, `PMID:41260371`, `41260371`, the DOI, and `Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom` across the repository, excluding `.git/`, `.venv/`, and `tmp/`, found only the new maintained YAML, new history record, generated HTML, committed PubMed cache, pytest cache, and the pre-existing scout stub. No duplicate maintained community record was found.

## Evidence

All record snippets match the committed `references_cache/PMID_41260371.txt` abstract or PubMed metadata, and all use stable `PMID:41260371` references.

Supported claims:

- The source constructs and names synthetic consortium S11 from `G. arilaitensis NFB2-4` and `G. nicotianae CYN-C5`.
- The abstract directly reports pH 6-9, C/N at least 15, 95% NH4+-N removal, 97% NO2--N removal, 30 mg/L initial concentration of each inorganic nitrogen species, 24 h endpoint, and a 15%-25% improvement over single-strain cultures.
- The hydrophilic sponge recirculating-system claim is abstract-supported, including the 20 min HRT and 76% / 96% NH4+-N / NO2--N removal.
- The industrial-scale recirculating aquaculture trial and residual NO2--N percentages are abstract-supported.
- The DOI external resource is supported by PubMed metadata.

Over-scoped or unsupported claims:

- None found at blocker or major severity.

The interaction is typed as `MUTUALISM` although the source phrase is "synergistic nitrogen removal." The accessible source does not expose a transferred metabolite or reciprocal growth measurement. However, the schema lacks a `SYNERGISM` interaction type; `MUTUALISM` is a coarse positive/positive bucket, and this record keeps the assertion at `COMMUNITY_LEVEL` scope with both members as participants instead of inventing a pairwise exchange.

## Completeness

Consequential gaps:

- The record lacks `modeled_environment` even though `src/communitymech/schema/communitymech.yaml` says that slot captures "the natural or applied environment(s) this community derives from, models, or represents" for engineered/synthetic communities. The primary reference repeatedly frames S11 as a synthetic consortium for aquaculture wastewater and reports an industrial-scale recirculating aquaculture trial. Neighboring wastewater SynCom records use `environment_term: laboratory environment` plus `modeled_environment` for the applied wastewater context.

Correctly bounded open gaps:

- The `glutamicibacter_s11_methods_details` discussion is warranted. The PubMed abstract exposes strain identity and headline conditions/results, while Europe PMC reports no OA full text or PDF; exact S11 inoculation ratios, full wastewater/medium chemistry, sponge immobilization protocol, reactor geometry, operating temperature, and field-trial deployment details remain behind the version of record.
- GTDB grounding is explicitly unresolved for both taxa because the NCBI2GTDB crosswalk was unavailable.

Bounded searches:

- An ignored-inclusive repository search for "aquaculture wastewater", "aquaculture water", "recirculating aquaculture", and possible aquaculture ENVO usage found no more-specific local modeled-environment precedent than a generic `ENVO:00002001` / `waste water` value used by existing wastewater model records.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| Minor | `kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` should add `modeled_environment` for the aquaculture wastewater / recirculating aquaculture application. Keeping only `environment_term: laboratory environment` preserves the assay setting but drops the applied environment that the synthetic consortium represents, which weakens environment-based joins. | `kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` |

No blocker findings.

No major findings.

## Recommended Edits

1. Add `modeled_environment` to `kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml` near `environment_term`.
2. Use `preferred_term: aquaculture wastewater` and the broad available grounding `ENVO:00002001` / `waste water` unless a more exact ENVO aquaculture-wastewater term is verified before editing.
3. Add notes tying the modeled environment to the target aquaculture wastewater and the industrial-scale recirculating aquaculture trial.
4. Append a normal curation event and a new append-only history record for the edit.
5. Regenerate `docs/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.html`, `docs/browser.html`, and `docs/index.html`.

## Follow-up Checks

Run the same focused checks that passed for the original record:

- `linkml-validate` on the community record.
- `linkml-validate` on the new history record.
- `validate_strict.py`, `validate_gtdb_coherence.py`, `validate_yaml_scalars.py`, `validate_shared_taxon_ids.py`, `validate_prokaryotic_lineage.py`.
- `linkml-reference-validator` and `linkml-term-validator`.
- `PYTHONPATH=src .venv/bin/python -m communitymech.render`.
- `git diff --check`.

Re-run the focused docs tests if local `uv` remains blocked:

- `PYTHONPATH=src .venv/bin/pytest tests/test_no_duplicate_yaml_keys.py tests/test_docs_do_not_contradict_the_kb.py`

## Additional Notes

The first-pass record's caution around method details is important. Do not move sponge-immobilization protocol, wastewater recipe, inoculation ratios, or industrial-trial operating conditions out of `discussions` without inspecting the version of record or an author-accepted manuscript.
