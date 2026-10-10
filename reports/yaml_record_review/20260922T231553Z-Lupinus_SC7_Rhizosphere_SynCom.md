# YAML Record Review: Lupinus SC-7 Rhizosphere SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml
- Started UTC: 2026-09-22T23:10:24Z
- Finished UTC: 2026-09-22T23:15:53Z
- Verdict: pass

## Target

Reviewed maintained `MicrobialCommunity` record
`kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml`.

- ID: `CommunityMech:000427`
- Label: `Lupinus SC-7 Rhizosphere SynCom`
- Primary source: `PMID:42602126`
- DOI: `10.3389/fpls.2026.1891479`
- Maintained or generated: maintained YAML
- New history entry:
  `history/records/Lupinus_SC7_Rhizosphere_SynCom/2026-09-22T231024Z-codex-427.yaml`

## Validation

| Check | Result |
|---|---|
| `just validate kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | Blocked before validation by `uv` rebuilding `llvmlite==0.46.0` under Python 3.13. |
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | Pass, no issues found. |
| `just validate-history history/records/Lupinus_SC7_Rhizosphere_SynCom/2026-09-22T231024Z-codex-427.yaml` | Blocked before validation by the same `uv` / `llvmlite==0.46.0` rebuild failure. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Lupinus_SC7_Rhizosphere_SynCom/2026-09-22T231024Z-codex-427.yaml` | Pass, no issues found. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | Pass; 1 file scanned, 0 error rows. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | Pass; 28 snippets scanned, 28 exact matches, 0 weak or missing snippets. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml history/records/Lupinus_SC7_Rhizosphere_SynCom/2026-09-22T231024Z-codex-427.yaml` | Pass; 2 files checked, 0 truncated scalars. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | Pass; 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | Pass; 0 reused ids. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml` | Pass; 0 contradictory lineages. |

## Identity and Grounding

The record denotes a single bounded community: the full `SC-7` synthetic
community from Table 1 of `PMID:42602126`. Its `ENGINEERED` state,
`SYNTHETIC` origin, and `RHIZOSPHERE` category agree with the paper's assembly
of defined lupin isolates for gnotobiotic FlowPot and non-sterile soil
inoculation.

The `rg --no-ignore --hidden` duplicate search over `kb`, `data`, `history`,
`pages`, `docs`, `reports`, `references_cache`, `research`, and `tmp` found
`PMID:42602126` only in scouting queues/stubs, the new maintained record and
history entry, and the local source cache. No older maintained
`kb/communities` or `data/isolates` record already represented SC-7.

All twelve members are curated at the genus plus strain-code level reported in
the article's main composition table. The NCBITaxon ids and labels pass the
id/label gate. The duplicate Streptomyces genus id is not an identity collapse:
`LARHCF249` and `LARHCF252` are distinct strain-designated SC-7 members.

## Evidence

The source support is exact:

- The design evidence cites the co-occurrence-network analysis, the random
  representative-strain selection, and the Table 1 strain counts.
- Each `taxonomy` entry cites the exact Table 1 strain-code/genus pair for that
  member.
- Interaction claims are community-level and avoid a pairwise or
  richness-only causal edge; the record quotes the paper's own warning that
  complexity and composition varied simultaneously.
- FlowPot, equal-ratio inoculum, TSB/TY growth, nitrogen-free BD medium, and
  CAS-soil pot evidence all quote Methods text.
- BioProject accessions `PRJNA1178901` and `PRJNA1335402` quote the data
  availability statement and both NCBI BioProject landing pages returned HTTP
  200.

No evidence snippet mismatch, weak rendering fallback, or wrong-reference case
was found.

## Completeness

The record captures the consequential SC-7 facts exposed by the open primary
article: exact full-SynCom composition, strain codes, assembly rationale,
gnotobiotic and non-sterile soil inoculation, growth/transcription endpoints,
public NCBI BioProject accessions, and metal non-relevance.

The record deliberately leaves species-level taxonomy unasserted. Table 1
defines the SC-7 composition with genus names plus strain codes; moving closest
16S relatives from the supplement into `term` would add false precision.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- When a local kg-microbe `NCBI2GTDB.tsv.gz` crosswalk is available, rerun
  `PYTHONPATH=src .venv/bin/python scripts/gtdb_ground.py --community kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml --apply`
  to see whether any genus-level bacterial taxa can move from `UNRESOLVED` to
  `GROUNDED` or `AMBIGUOUS`.
- Re-run the standard `just` validator wrappers after the Python 3.13
  `llvmlite` rebuild issue is resolved, to confirm the direct `.venv/bin`
  invocations continue to match the declared recipes.

## Additional Notes

`scripts/gtdb_ground.py --apply` stopped before editing because the
kg-microbe `NCBI2GTDB.tsv.gz` mapping was not present in any default search
location, and `find . -name NCBI2GTDB.tsv.gz -print` found no in-repository
copy. This is not a record defect: every new bacterial taxon currently carries
`gtdb_grounding_status: UNRESOLVED`, and the GTDB coherence and prokaryotic
lineage validators pass.
