# Integrated scientific and product checkpoint

Revision `012d755bdf591e1f0e814fddb52b0ad0aeddabaa` combines the reviewed Phase 2 schema, rendering, reference instrumentation and scientific corrections. Full M5 QC on this revision remains pending at this checkpoint. The original November 6 checkout and stalled session remain preserved.

## Scoped scientific evidence

| Record | Current assessment | Retained limits |
| --- | --- | --- |
| EcoFAB 000025 | [Full three-record review](../../reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.yaml) | Four treatment arms and relative-read observations; treatment effects and proposed mechanisms remain distinct; exact source IMG/GOLD pairs replace the pseudo-range |
| Switchgrass 000087 | Same full review | Methods/Table S1 stock correspondence and two supplemental-source reference mismatches remain blockers |
| Dopamine SynCom 000516 | Same full review | Associations, isolate interventions and whole-community endpoints remain distinct; genus grounding is not exact stock-genome placement |
| Brachypodium 000088 | [Full record review](../../reviews/structured/20261115T025413Z-phase2-brachypodium-drought/review.yaml) | Fifteen source stocks; nine experimental arms; rewatering benefit is not sustained-drought benefit; genomic and molecular uncertainties remain explicit |
| Human gut 000122 | [Full record review](../../reviews/structured/20261115T025440Z-phase2-gut-completion/review.yaml) | Twelve source stocks; pairwise feedback is not a twelve-member molecular mechanism; two exact-stock genome mappings remain unresolved |
| Yolo 000515 | [Recovered full assessment](../../reviews/structured/20261114T213322Z-m5-yolo-scientific-completion/review.yaml) and [reviewed correction delta](../../reviews/structured/20261114T221158Z-m5-postcuration-scientific-delta/review.yaml) | Unchanged during Phase 2; the full assessment's older bytes and later bounded correction are separate immutable evidence, not a newly issued full-record review |

The final three-record review has 105 assessments. All 27 focused gates executed: 26 passed and the switchgrass reference gate failed. Actual traversal on its recorded source revision compared 149 of 149 assertions, with 147 matches and two supplement mismatches. The Brachypodium and gut saved reviews each retain their nine executed focused checks. Validator scores and native review validity do not certify scientific truth.

The [successor manifest](scientific-successor-provenance.yaml) links the five Phase 2 record revisions to three saved review pairs, eight actual write receipts and ten new native history sidecars. It preserves the old graph-review evidence. Its purpose is persistence and correction history; it does not grant independent scientific approval.

The [five-record private checkpoint](review-input-checkpoint-five-record-local-001.md) is verified locally: 403 files, 64,961,689 bytes including the manifest and standalone verifier. Its M5 transfer remains unrun pending explicit human approval. Private source bodies are not published in the repository.

## Combined verification

Native rendering regenerated the Brachypodium page and browser indexes from the corrected fifteen-stock record. The generated diff was independently reviewed. A fresh Yolo product canary persisted its HTML and a 13-node/13-edge KGX export with zero errors or warnings. The same launcher then rendered/exported the complete community set: **1,538 nodes, 2,535 edges, zero errors and zero warnings**.

Both product runs used `scripts/adhoc/check_phase2_products_20261115.py` at `1ae757b284d0c28ec268be49eb873d64cba0cb90`, with unchanged renderer/export implementation hashes. The batch receipt is retained at `.temp/phase2-integration-20261115/final-products-batch-001/receipt.json`, SHA-256 `9692f2bfd6b2132176e4916c7d971aa175f91c1ce90d589ed83b618549ca7154`; its strict export-validation log has SHA-256 `8f773214b074ab79594d876eeaf806a04ae7128863d7d42cfa7316adb3a4de4e`.

Fourteen linked-record source-boundary and apply-guard controls passed. The integrated successor run initially had 54 passes and one batch-61 wiring failure: records without an intermediate review bypassed the new successor verifier. The one-line correction was independently reviewed under #2816, and all nine tests in that affected module subsequently passed. Historical scientific assertions and immutable reviews remain unchanged. Native lint passed after the separately reviewed formatting-only correction recorded in #2826. These focused results do not replace the full M5 QC run.

## Separate reference measurement

The cache-only M5 measurement at `20185647ad327b686b37dcf3a0036cf298028779` processed all 549 records. Its single-record canary persisted 25 actual comparisons with no issues and unchanged inputs before the corpus run. The corpus run retained exit 1 and its raw logs and receipts. Public aggregate export is still undergoing verification; the raw run is not a validation pass, and it is distinct from native online `qc-references`.

Phase 2 completion and the broader scientific campaign remain separate. The next campaign record is prepared read-only; no campaign batch completion is claimed here. No merge of Phase 2 is authorized by this checkpoint.
