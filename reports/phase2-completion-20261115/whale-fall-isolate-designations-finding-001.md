# Preserve the source's whale-fall isolate designations

Stable finding key: `cm-000474-isolate-designations`.

`CommunityMech:000474`, `kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml`, represents a sediment enrichment and a reconstituted isolate coculture. Both taxonomy entries lack structured strain designations. The primary article identifies the cultured Vallitalea isolate as **sp2** and Trichloromonas as **sp17**. Their identity should remain distinguishable from genus-level observations of the mixed enrichment.

Evidence inspected on 2026-11-15:

- Record SHA-256: `afddcb4da0903a9eb3ba3859641c9cbb60e3b90742bc6bc7a928e38da1c86885`.
- [Primary article](https://doi.org/10.1093/ismejo/wrag151), PMID42297039 / PMC13374861. Retained `references_cache/PMID_42297039.txt`, SHA-256 `5c1f67ef420c1aff46bc86678763c725f728a20688c094a776373a8a214e8989`, Methods isolation, partial 16S sequencing and coculture paragraphs at lines81–85; Results isolate/coculture paragraphs at lines141–143.
- Short source excerpt: “Vallitalea sp. (sp2) and Trichloromonas sp. (sp17)”.
- The Methods report partial 16S accessions PX642411/PX642410. This pass did not independently resolve each accession to its isolate or verify any whole-genome assembly. Neither a genus-reference mapping nor these two accessions establish an exact study-stock GTDB genome identity.
- The fresh publisher request was inaccessible; this finding relies on the pinned retained source passages, not a new full-paper or supplement review.

Acceptance: curate the two source designations with claim-specific evidence and clear enrichment-versus-coculture scope; independently verify any accession associations before encoding them. Preserve genus-rank authority until a narrower identity is supported. Append native history, run the scoped native checks and assess the changed assertions in a new immutable review. Do not edit old reviews, infer species/assemblies from reference-genome counts, or use this change to certify the existing causal graph.

The current #2848 correction only concerns reference taxonomy correspondences and leaves these stock fields unchanged. This scientific completeness finding remains separate.

Deduplication: live all-state GitHub searches for `474`, `whale` and `Vallitalea` in issue titles/bodies, plus ignored-inclusive local issue-report search for stock/name terms. The numeric search returned unrelated #1338; the two name searches returned no matches. Comments and PR reviews were not exhaustively searched.
