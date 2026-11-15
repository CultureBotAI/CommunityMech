# Historical reference-validation blocker ledger

Measurement: `20185647ad327b686b37dcf3a0036cf298028779`; [published aggregate](../phase2-reference-measurements-20261115/m5-final-reference-corpus-001.json), SHA-256 `4dd2d4fcb8cad8ac95a0a645ba7a70fc4e21f267429f6fbd25d34530086ff147`.

All **549 records** were processed. **109 native issues in 17 records** comprise 108 actual lexical mismatches and one no-content occurrence that was not compared. Native exit1 and incomplete assertion coverage remain unchanged. These outcomes do not establish scientific falsity.

The six Phase2 targets contain **270/270 comparisons**, 268 matches and two mismatches, both in switchgrass. The other 543 records contain 107 issues across 16 records. This is the retained run, not a measurement of the final current revision.

## Six Phase2 targets

| Record | Compared/surfaces | Matched | Native issues | Disposition |
|---|---:|---:|---:|---|
| CommunityMech:000516 · Brachypodium_Natural_Variation_Dopamine_SynCom16 | 40/40 | 40 | 0 | No issue in this run |
| CommunityMech:000025 · EcoFAB_Ring_Trial_SynCom17 | 72/72 | 72 | 0 | No issue in this run |
| CommunityMech:000088 · LBNL_Brachypodium_Drought_SynCom15 | 63/63 | 63 | 0 | No issue in this run |
| CommunityMech:000122 · LBNL_Human_Gut_Interaction_SynCom | 44/44 | 44 | 0 | No issue in this run |
| CommunityMech:000087 · LBNL_Switchgrass_Soil_SynCom16 | 37/37 | 35 | 2 | [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996): two TableS1 cells need source routing |
| CommunityMech:000515 · Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm | 14/14 | 14 | 0 | No issue in this run |

## All affected records in measured inventory order

| Record | Source | Issues | Boundary / owner |
|---|---|---:|---|
| CommunityMech:000142 · Bacteroides_Methanobrevibacter_Gnotobiotic_Mouse_Mutualism | PMID:16782812 | 4 | Full-source cache discovery; [#703](https://github.com/CultureBotAI/CommunityMech/issues/703) |
| CommunityMech:000005 · Bayan_Obo_REE_Tailings_Consortium | doi:10.1016/j.cej.2024.153492 | 1 | No content available; [#1261](https://github.com/CultureBotAI/CommunityMech/issues/1261), [#1093](https://github.com/CultureBotAI/CommunityMech/issues/1093) |
| CommunityMech:000456 · Caragana_Wheat_Drought_SynCom15 | PMID:41634815 | 15 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000403 · Choysum_SynLAV_DEHP_Rhizobacterial_SynCom | PMID:42482240 | 8 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000020 · Coscinodiscus_Synthetic_Community | PMID:36300970 | 3 | Selected source is abstract-only; [#596](https://github.com/CultureBotAI/CommunityMech/issues/596) |
| CommunityMech:000449 · Fucoidan_Seven_Degrader_Combinatorial_SynCom | PMID:42649294 | 15 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000376 · Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom | PMID:42305112 | 12 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000087 · LBNL_Switchgrass_Soil_SynCom16 | PMID:36472419 | 2 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000045 · Mixed_Gallium_LED_Recovery_Consortium | doi:10.1016/j.jece.2025.120403 | 1 | Retained quotation/source mismatch; [#1618](https://github.com/CultureBotAI/CommunityMech/issues/1618) |
| CommunityMech:000395 · Nasal_SynCom_C_Bioreactor | doi:10.64898/2026.03.16.712028 | 11 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000051 · Panzhihua_Vanadium_Titanium_Tailings | PMID:33125214 | 1 | Quotation/source notation discrepancy; [#2841](https://github.com/CultureBotAI/CommunityMech/issues/2841), [#1683](https://github.com/CultureBotAI/CommunityMech/issues/1683), [#1680](https://github.com/CultureBotAI/CommunityMech/issues/1680) |
| CommunityMech:000381 · Prymnesium_Parvum_B12_Limited_SynCom | PMID:42549325 | 15 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000424 · QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium | PMID:42511722 | 5 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000388 · Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom | PMID:42364169 | 4 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000314 · SynCom_ARC_Peanut_Aflatoxin_Nodulation | PMID:42099455 | 9 | Supplement routing; [#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996) |
| CommunityMech:000167 · Synechococcus_Pseudomonas_PhotoPHA_DNT_Coculture | PMID:38609451 | 1 | Known PDF rendering difference; [#1863](https://github.com/CultureBotAI/CommunityMech/issues/1863) |
| CommunityMech:000404 · Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium | PMID:42478817 | 2 | Retained quotation/source mismatch; [#2793](https://github.com/CultureBotAI/CommunityMech/issues/2793) |

## Interpretation and retained limits

- **CommunityMech:000142**: Four occurrences select the canonical abstract cache. The additional dataset accession excerpt is present in the separately named retained full source; #703 owns discovery, not deletion of that evidence.
- **CommunityMech:000449**: Fourteen retained taxonomy-table failures plus one SupportingReference Table2 Lentimonas cell. The extra cell is present in the separate supplement, not the selected article cache.
- **CommunityMech:000087**: The full scientific review verifies the OAE516/OAE603 TableS1 cells and explicitly retains discussions[4].evidence[2/4] under #1996. Annotation coverage is complete here; source routing remains unresolved.
- **CommunityMech:000051**: New exact lexical occurrence #2841: record V V versus retained abstract VV. Broader source/community identity remains separately owned by #1683/#1680; no canonical correction was applied.
- **CommunityMech:000167**: Exact #1863 quote/cache case: PDF line-break hyphen and fi ligature. The issue's earlier CLI pass did not establish SupportingReference comparison. This run measures one actual native mismatch; #1863 is the existing rendering owner, not evidence that native normalization is fixed.

New bounded finding [#2841](https://github.com/CultureBotAI/CommunityMech/issues/2841) records the Panzhihua notation discrepancy after exact-phrase/record/PMID deduplication. All other rows map to existing owners. Current issue states and exact field/cache/hash identities are retained in [the JSON ledger](reference-blockers-20185647.json). No raw quotations, source bodies or absolute local paths are published.

- No native validation or primary-source acquisition was rerun; current issue ownership is layered onto the immutable 20185647 measurement.
- The six SupportingReference failures are Bacteroides dataset1, Fucoidan discussion1, switchgrass discussion2, Panzhihua discussion1 and Synechococcus discussion1; each was actually compared.
- Exact TableS1 source support is retained in the three-record full scientific review; previous source-boundary recurrence evidence remains in the M5 reference-failure triage report.
- GitHub searches covered exact identifiers, record names and candidate issue bodies; comments and every external repository were not exhaustively searched. Bounded local report/review searches included ignored/hidden files.
- This ledger does not reorder the scientific campaign or close issues; the final-current M5 aggregate and later source revisions remain separate.

Source-support context: [full three-record review](../../reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.md); [previous reference triage](../m5-completion-20261114/reference-failure-triage-20261114.md). These are scope/ownership evidence, not a replacement for the measured artifact.
