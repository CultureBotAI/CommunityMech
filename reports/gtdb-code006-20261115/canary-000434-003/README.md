# One-record GTDB correspondence canary

The native M5 path applied the reviewed Mycobacterium genus correspondence and passed six scoped gates plus both unchanged outstanding-grounding tests. This is a technical mapping assessment, not a full scientific review or corpus QC pass.

The earlier status-only step remains recorded: six scoped gates passed, but both completion tests failed. Its immutable needs_curation assessment and actual receipt remain in the chain.

| Phase | Canonical SHA prefix | Scoped gates | Completion tests |
|---|---|---:|---:|
| Status diagnostic | d58669e0 | 6 passed | 2 failed |
| Genus correspondence | c2cf66bb | 6 passed | 2 passed |

The mapping is NCBITaxon:1763 → GTDB:g__Mycobacterium, 18589/18589 named genomes, with no reclassification, using exact crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. The paper's exact species/genome and ecological mechanism remain unresolved; notes, evidence quotations and every other taxon/biological field are unchanged.

Execution revision 956d00c6143020810ef7a60a6298e67fb0ee0caf used native Python 3.13.2 on the isolated M5 checkout plus explicitly hashed orchestration helpers. [Metadata and raw/public hashes](summary.json) bind both actual receipts, 15 retained native logs, both saved assessments and the original status failure. Each exported log and exit file matches its exact saved-review input hash. The earlier scaffold log remains private because that review bound its resulting sidecar rather than the scaffold log.

- [20261115T050137Z-gtdb-status-000434-canary](../../../reviews/structured/20261115T050137Z-gtdb-status-000434-canary/review.yaml): 59 input hashes and exact native Markdown verified on M5.
- [20261115T051302Z-gtdb-genus-000434-canary](../../../reviews/structured/20261115T051302Z-gtdb-genus-000434-canary/review.yaml): 78 input hashes and exact native Markdown verified on M5.

Raw application receipts are byte-identical metadata copies. Native log derivatives replace private paths/addresses when present, retaining raw and public hashes. Original raw files remain private on both checkouts. Work tracked by #2848/#2849 and all older scientific limitations remains outstanding.
