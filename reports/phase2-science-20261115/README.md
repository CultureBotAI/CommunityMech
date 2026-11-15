# Phase 2 scientific curation checkpoints

The full current scientific assessment of EcoFAB 000025, dopamine SynCom16 000516 and the Methods-defined LBNL collection 000087 is saved at source commit `a821ec7ca48adb5232cfc7a92e86d1d20330d278`. Its 105 assessments cover all 49 stock assertions, ten interaction nodes, four downstream arrows, cultivation and host contexts, related communities, resources, discussions and provenance. EcoFAB now has four explicit treatment arms, four arm/timepoint-bound relative-read observations and 17 exact source-reported IMG/GOLD pairs.

- [Full scientific review YAML](../../reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.yaml) and [native Markdown](../../reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.md).
- [Dated persistence audit](final-three-retained-inputs.json): all 196 inputs matched at 03:15:33 UTC on 2026-11-15; Markdown exactly matched the native renderer. The YAML is 180,783 bytes and Markdown is 268,923 bytes.
- [Six actual applied writes and seven native sidecars](applied-chain-ecofab-final-002/chain.json), preserving all earlier receipt bytes and checkpoints.
- [Source correction checkpoint](ecofab-source-checkpoint.md), including the exact current record hashes and focused gate provenance.

| Verification | Actual result | Interpretation |
| --- | --- | --- |
| Maintained current reference measurement | 149 of 149 snippet occurrences compared; 147 matched, two mismatched | Actual traversal includes `SupportingReference`; the native issue count is not used as a coverage proxy. |
| Focused native gates | 26 passed, one failed out of 27 | LBNL references fail on the two exact Table S1 cells. All checks executed; failure is retained. |
| Generated documents | `check-docs-current` passed on the committed source | Generated pages match canonical records. |
| Review persistence | Native validation/save passed; 196 input hashes and native Markdown verified | Persistence does not establish scientific truth or repository-wide QC completion. |

The final review resolves the three retained EcoFAB causal/study-stage/genome findings and the narrow LBNL unannotated-discussion finding. Two boundaries remain: the Methods/Table S1 stock correspondence under [1548](https://github.com/CultureBotAI/CommunityMech/issues/1548), and source-aware routing of two correct supplemental quotations under [1996](https://github.com/CultureBotAI/CommunityMech/issues/1996). The earlier linked-stock review separately resolved the paired metadata defects. Source ambiguity and native reference failure are not silently converted to passing verdicts.

The full review has `completion: completed`, `verdict: needs_curation`, and `scientific_review: true`. Every scoped claim was assessed and every required focused check executed. Combined Phase 2 QC, other records, the broader campaign and merge decisions remain separately accounted for. The metrics correction recorded in [2825](https://github.com/CultureBotAI/CommunityMech/issues/2825) preserves the rejected draft and uses the native zero-node default without inventing an evidence-per-node ratio; a capped score never overrides findings or failed checks.

## Historical first canary — 02:17 UTC

The status descriptions below describe the original canary checkpoint. Its immutable review and receipts remain unchanged; the full current assessment above supersedes its current-state descriptions where explicitly stated.

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
