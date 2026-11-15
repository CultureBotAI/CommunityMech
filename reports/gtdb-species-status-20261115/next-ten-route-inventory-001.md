# Bounded next-ten native route inventory

This read-only inventory covers exactly the ten whole records in the [frozen plan](next-ten-route-plan-001.json), SHA256 `dd943ca17882b840c05e64ef6e4bae8588fb000fad43abe46e6661e13b87e4c5`. It proposes no canonical writes and is not a scientific review. The [complete per-occurrence summary](next-ten-native-routes-001.json) retains existing blocks, all native results including null, classifier statuses and manual holds.

Execution used reviewed reporter `2d4732edafccba24741b728b9e672ca7fada5e50d8220162a9ccf3c5d8d875ef`, revision `d7ffb6d4a7ba49d4860a738f5c0ccc877c2cef98`, local frozen Python 3.13.12, crosswalk SHA256 `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`, and the existing local NCBI adapter. NCBI adapter provenance is a stable file-stat observation, not a database content hash or release certification. No source acquisition occurred.

One real record, 000388, ran first through `run_phase2_schema_checks_20261115.py` and persisted 9,991 bytes of native JSON; all 13 captured input hashes were verified. The same launcher, shell, environment, serial execution mode and output directory then ran all ten records, persisting 2,082,526 bytes; all [22 captured inputs](next-ten-native-route-inputs-001.sha256) [verified unchanged](next-ten-native-route-inputs-verified-001.log.txt). Both native exits were zero. This proves route computation and receipt persistence on this local path, not M5 curation or the later eight validation gates.

| Record | Proposed taxonomy indices | Fresh missing-block native correspondence | Scope retained |
| --- | --- | --- | --- |
| 000388 | 0, 1 | Rhizorhabdus wittichii: 7 / 0.86; Cupriavidus pinatubonensis: 1 / 1.0 | Species-reference YL-JM2C versus exact-strain JMP134 routes remain distinct. |
| 000517 | 0, 2 | Lactobacillus helveticus: 378 / 1.0; L. delbrueckii: 37 / 1.0 | Exact Set1 stocks and the NCBI subspecies descriptor remain. |
| 000431 | 0, 2 | Same two species populations | Exact Set2 stocks and the existing S. thermophilus block remain. |
| 000522 | 0, 2 | Same two species populations | Exact Set3 stocks and the existing S. thermophilus block remain. |
| 000396 | 0 | Peptacetobacter hiranonis: 82 / 1.0 | Unreported study-strain identity remains unresolved; WT/KO experiment distinction remains. |
| 000397 | 0 | Pseudobacillus badius: 26 / 1.0 | NBRC 15713, source Bacillus wording, other two blocks and abstract-only limits remain. |
| 000053 | 0 | Syntrophorhabdus aromaticivorans: 3 / 1.0 | UI type strain and the methanogenic pair remain distinct from the alternative Desulfovibrio coculture. |
| 000313 | 2 | Pseudoduganella rivuli: 3 / 1.0 | FT92W stock, four-isolate treatment structure, existing genus blocks and eukaryotic null routes remain. |
| 000426 | 0 | Burkholderia cepacia: 548 / 0.93 | ZY1 species-reference route; G1B remains natively unresolved and unchanged. |
| 000362 | 1 | Nitrososphaera viennensis: 3 / 1.0 | EN76 stock, existing Sphingobium genus block and abstract-only experiment limits remain. |

Numbers are native `total_genomes / majority_fraction`, not study-strain counts or measured inoculum proportions. Every proposed new block above follows `ncbi_id`; existing name and higher-rank routes in the same records are preserved. No exact numerator is inferred from a rounded fraction.

The independently reviewed [Parmigiano source plan](../phase2-completion-20261115/parmigiano-source-context-001.yaml) and [000397 source plan](../phase2-completion-20261115/nitrifier-000397-source-context-001.yaml) are copied unchanged from `eea53a5b0800e29f4c0af7941529d26e7b241029`. Their expected historical populations now agree with fresh native results; local authority rows and exact source/guard bindings are still required in the next authored source proof. The other records likewise require their own source-context judgments and guarded candidates before application.

Historical callers retain their biological predicates. Batches 93, 82, 84, 105 and 141 inspect the last prior history event; batch142 requires the prior curation action. Those checks must use an explicitly admitted predecessor projection while preserving current non-GTDB content. 000396 and 000397 must retain their existing remediation chains before the new GTDB successor. The batch14 exact-byte check requires a bounded successor; batch8's YB2 biology predicates must remain unchanged. No old ledger or review is rewritten by this inventory.

Private native triplets remain under `.temp/phase2-schema-20261115/`:

| Run | JSON log SHA256 | Receipt SHA256 | Exit SHA256 |
| --- | --- | --- | --- |
| species-route-388-canary-001 | `3192463a784371506fcfe187caa5d53cb4f6435f51e5e8727d52b1a706d03286` | `8a83ffc120a78699b38f569ca8047d9b61ab6b8c4167be56c6a66557c812fd24` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| species-route-ten-001 | `12309d2473eb63a427dbf7d6bfbaf6c918f2cb7fbd24352936bbbd36dde825e4` | `228a830e380cf05ef588b18660131a8d588e9494c03c7705812050c9e0dfda57` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |

The summary is derived by `scripts/adhoc/gtdb_route_summary_20261115.jq`, SHA256 of output `522f785809cc50e63be79a5975452ec4af95dce731b7334d12f1a7918c9c9a27`. Input check lines are derived by `scripts/adhoc/gtdb_route_input_hash_lines_20261115.jq`. Raw reports and native receipts remain immutable; no record in this next-ten plan is counted as corrected by this inventory.
