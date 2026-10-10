# YAML Record Review: Staged Ensifer-Bacillus Cattle-Manure Wastewater SynCom

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml`
- Started UTC: 2026-09-22T09:24:07Z
- Finished UTC: 2026-09-22T09:24:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000418` |
| Label | Staged Ensifer-Bacillus Cattle-Manure Wastewater SynCom |
| Maintained or generated | Maintained curated record |
| Category / state / origin | `BIOTECHNOLOGY` / `ENGINEERED` / `SYNTHETIC` |
| Primary source | `PMID:42341825`, `doi:10.1093/jambio/lxag151` |

The record denotes the Wang et al. defined two-member staged cattle-manure-wastewater consortium pairing Ensifer sp. S2-8-1 with Bacillus subtilis. The scope is the abstract-level SYC design and its maize-pot outcomes, not the missing full staging protocol.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` | Pass, no issues found |
| `scripts/validate_strict.py kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` | Pass, 1 file scanned and 0 ERROR rows |
| `linkml-term-validator validate-data ... --labels` | Pass, all ontology labels resolved |
| `scripts/evidence_snippet_audit.py --list-mismatch --list-rendering --list-assembled ...` | Pass, 15 `MATCH`, 0 `MISMATCH`, 0 `WEAK`, 0 `RENDERING`, 0 `ASSEMBLED`, 0 `NOCONTENT` |
| `linkml-reference-validator validate data ... --target-class MicrobialCommunity --no-full-text` | Pass, but the upstream tool printed `Total checks: 0`; the snippet audit above is the meaningful exact-snippet reconciliation |
| `scripts/validate_gtdb_coherence.py kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` | Pass, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `scripts/validate_yaml_scalars.py kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` | Pass, 0 truncated scalars |
| `scripts/validate_shared_taxon_ids.py kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` | Pass, 0 reused IDs |
| `scripts/validate_prokaryotic_lineage.py kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` | Pass, 0 contradictory lineages |
| `communitymech.network.auditor.NetworkIntegrityAuditor().audit_community(...)` | Pass, `[]` |
| `git diff --check` | Pass |

The generated HTML renderer also completed for the full corpus, rendering 408 community pages and regenerating `docs/browser.html` and `docs/index.html`.

## Identity and Grounding

The primary identity is sound. PubMed cache `references_cache/PMID_42341825.txt` identifies a 2026 Journal of Applied Microbiology paper by Wang et al. with DOI `10.1093/jambio/lxag151` and PMID `42341825`; its title exactly matches the new external-resource snippet.

A gitignore-independent duplicate search over `kb`, `data`, `history`, `docs`, `references_cache`, `reports`, `research`, and `tmp` found this new maintained record, its new history/doc/cache artifacts, and prior scout stubs or queues for `PMID:42341825`. It did not find an older maintained curated record for the same PMID, DOI, title, or Ensifer sp. S2-8-1 organism string.

The two curated members are supported by the PubMed abstract and by ontology validation:

| Source name | Grounded term | Review |
|---|---|---|
| Ensifer sp. S2-8-1 | `NCBITaxon:106591` Ensifer | Sound at genus level; the record preserves the strain designation and correctly uses the ambiguous Ensifer/Sinorhizobium GTDB genus candidates already used for Ensifer sp. isolates in the corpus |
| Bacillus subtilis | `NCBITaxon:1423` Bacillus subtilis | Sound; the GTDB species block is coherent with the NCBI species term |

The environment groundings are reasonable after term validation aligned `ENVO:00002001` to its canonical `waste water` label.

## Evidence

Supported by exact snippets:

- The engineering objective, two-member composition, S2-8-1 core role, Bacillus subtilis auxiliary role, and staged SYC-versus-controls design are abstract-backed.
- SYC's stronger viable bacterial density, cattle-manure wastewater conversion, enhanced rhizosphere nitrification, higher nitrate availability, maize-growth promotion, and 41.4% higher whole-plant dry matter are abstract-backed.
- Nitrate and cytokinin are both named outcomes in the abstract.
- The record correctly leaves the wastewater recipe, pre-modification sequence, inoculation ratio, temperature, and aeration as an open knowledge gap because those protocol details are absent from the PubMed abstract.

Unsupported or over-scoped:

- The member-level `CROSS_FEEDER` roles assert a metabolite-use relationship that is not present in the PubMed abstract.
- The soil-maize pot-experiment results are stored as `IN_VITRO` evidence even though comparable greenhouse or plant-pot claims in CommunityMech use `IN_VIVO`.
- The abstract says the transcriptomic result suggests coordinated activation of nitrogen-transformation and plant-growth-promoting signaling pathways; the current interaction title/description directly assert pathway activation.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| CM-STAGED-001 | major | Both taxa are assigned `functional_role: CROSS_FEEDER`, which the enum defines as utilizing metabolites from other taxa. The abstract identifies a core Ensifer strain and an auxiliary Bacillus strain, but it does not state that either member consumes the other's metabolites. | `kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` |
| CM-STAGED-002 | major | The evidence items for SYC's soil-maize pot outcomes are marked `IN_VITRO`. Those snippets come from the abstract sentence beginning `In a soil-maize pot experiment`, so they should be `IN_VIVO`, matching the plant-pot convention used elsewhere in the corpus. | `kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` |
| CM-STAGED-003 | minor | `S2-8-1 nitrogen and cytokinin pathway activation` overstates an inferred mechanism. The abstract reports upregulation of heterotrophic ammonia oxidation-related and cytokinin-related genes and says this suggests coordinated activation; the record should name observed gene upregulation rather than direct pathway activation. | `kb/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.yaml` |

## Recommended Edits

1. Remove the two unsupported `CROSS_FEEDER` functional-role assignments.
2. Change the evidence source for soil-maize pot nitrate, cytokinin, and dry-matter snippets from `IN_VITRO` to `IN_VIVO`.
3. Retitle and reword the metatranscriptomic interaction so it states S2-8-1 gene upregulation under SYC conditions, preserving the exact abstract snippet.
4. Append a `FIX_ADVERSARIAL_REVIEW_FINDINGS` curation event, add an append-only history entry, regenerate `docs/`, and re-run validators.

## Follow-up Checks

- Re-run schema, strict, term, snippet, reference, GTDB coherence, scalar, shared-taxon-ID, prokaryotic-lineage, and history validation on the edited files.
- Re-render `docs/communities/Staged_Cattle_Manure_Ensifer_Bacillus_SynCom.html`, `docs/browser.html`, and `docs/index.html`.
- Re-read the changed taxonomy, pot-experiment evidence, metatranscriptomic interaction, curation-history, repository-history, and rendered HTML sections after generation.

## Additional Notes

The current pass reviewed only the committed PubMed abstract cache plus local schema and validator behavior. It did not fetch Oxford full text, supplementary methods, or publisher tables.
