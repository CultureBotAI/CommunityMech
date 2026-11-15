# Phase 2 scientific curation checkpoint

The first canary, `CommunityMech:000087`, is saved and independently reviewed. It represents the **Methods-defined final 16-stock collection**, with the paper's earlier 18/17-member observations preserved separately. This checkpoint does not complete Phase 2, the all-record campaign, or full repository QC.

- [Immutable scientific review YAML](../../reviews/structured/20261115T021628Z-phase2-lbnl-canary/review.yaml) and [derived Markdown](../../reviews/structured/20261115T021628Z-phase2-lbnl-canary/review.md).
- [Dated persistence audit](lbnl-canary-retained-inputs.json): all 100 recorded inputs matched on 2026-11-15 at 02:17:28 UTC; Markdown exactly matched the native renderer. These are checkpoint hashes, not a promise that later curation leaves every input unchanged.
- Current record SHA256: `aa146b5e21d2480725ed8a017372fd1dd9dc8b1e89778e7ca1f83477566845c4`.
- Saved YAML: 76,175 bytes, SHA256 `6f96e422653a4f6925d592f06b08ef6b0bcaf72ed32ed6b671deda0af546a3cd`; Markdown: 112,100 bytes, SHA256 `9162b07c8cd1951a12e53e878237e9cd6f1d074eee8f215f48067dda6d825160`.

The record restores all 16 source strain/DSM assertions with current genus-level NCBI labels. GTDB mapping retains 13 genus correspondences, two ambiguous genera and one unresolved renamed genus; none is claimed as an independently verified study-stock genome. Laboratory environment is distinguished from modeled/source soil. Isolate, community, host and preservation conditions are separated. Three earlier-assay observations retain their original evidence in discussions, avoiding the schema's whole-community graph interpretation for an incompatible final roster.

Two predecessor findings are resolved narrowly: pooled assay metadata and physical-versus-source environment. Three remain open:

| Remaining boundary | Existing ownership | Next acceptance condition |
| --- | --- | --- |
| Main Methods and Table S1 stock discrepancy | [1548](https://github.com/CultureBotAI/CommunityMech/issues/1548) | Verify OAE515/OAE516 and the Marmoricola/Bacillus panel discrepancy without inventing aliases; other two records remain separately assigned. |
| Native discussion evidence coverage | [476](https://github.com/CultureBotAI/CommunityMech/issues/476) | Repair canonical shared-schema coverage and measure actual traversal; manual scientific review does not resolve this tooling gap. |
| Related-record stock metadata and reciprocal prose | [2674](https://github.com/CultureBotAI/CommunityMech/issues/2674), [2774](https://github.com/CultureBotAI/CommunityMech/issues/2774), [2806](https://github.com/CultureBotAI/CommunityMech/issues/2806) | Correct EcoFAB/Dopamine OAP107 rank, consortium versus individual deposit and paired descriptions from sources; validate integrated full-roster relations. |

All nine focused native gates passed on the corrected hash: schema, strict, term labels, references, GTDB coherence, GTDB domain, history, scalar safety, and a network audit over an exact one-record copy. The reference check used three retained cache copies with `--no-full-text` after native cache-hit preflight. Its printed `Total checks: 0` is a retained-issue count; it is not an evidence-assertion count. Discussion `SupportingReference` snippets remain unannotated and were manually source-checked. Full QC and integrated current-revision assertion coverage are separate work.

The canary exposed and recorded two implementation findings before completion: [2805](https://github.com/CultureBotAI/CommunityMech/issues/2805) required exact supplementary stock-cell quotations; [2808](https://github.com/CultureBotAI/CommunityMech/issues/2808) required moving generic genus caveats out of curated-override metadata. The first strict run's 13 errors remain retained. The initial term attempt was interrupted when a default adapter began an unnecessary download; the final run explicitly used existing local NCBI/ENVO adapters. An incorrect issue link in a new history sidecar was corrected by a separate immutable audit sidecar. No historical review or sidecar was rewritten.

Reproduction helpers are under `scripts/adhoc/*phase2_lbnl*20261115.py`; the final audit uses `scripts/adhoc/audit_phase2_saved_review_20261115.py`. Private primary XML, original figures, separately downloaded DOCX/ZIP, exact table extraction, grounding receipts and all native logs remain under `.temp/phase2-science-20261115/`. Source inputs are recorded in the immutable review; no supplement was merged into an article cache. Six guard regression tests passed, covering duplicate keys, unsafe tags, legacy aliases, section/history preservation, wrong-record refusal and output-overwrite refusal.

The next dependent correction is the source-backed EcoFAB/Dopamine stock metadata and reciprocal links. Previously corrected issues 2708–2710 are pending merge in PR 2775, not newly unfixed. No merge is authorized by this checkpoint.
