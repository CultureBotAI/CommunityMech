# Issue 1994 bounded source-provenance review: after

- Review: 20261013T044252Z-1994-source-boundaries-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-13T04:42:52Z
- Finished UTC: 2026-10-13T04:42:52Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

All 11 article/supplement boundaries repaired, with unchanged curated records and preserved source bytes. The scoped provenance repair passes; 79 native supplement-only failures remain explicitly recorded under #1996. Scientific claims are not re-reviewed.

## Scope And Provenance

Source-boundary and lexical/provenance audit only: 11 article caches, their supplementary sidecars, and 284 cited snippet occurrences in 11 canonical records.

Selection: Exact 11 files in #1994; recursive ignored-file-inclusive cache scan confirms the marker inventory. All kb/communities, kb/taxa and data/isolates YAML searched for these references.
Coverage: full; 11 reviewed / 11 in the declared population.
Source: working_tree at Git base 77ecab85bca112fde83ec221f5f4149666e01a78.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PMID:41634815 | references_cache/PMID_41634815.txt | source | PMID:41634815 article/supplement boundary |
| PMID:42099455 | references_cache/PMID_42099455.txt | source | PMID:42099455 article/supplement boundary |
| PMID:42305112 | references_cache/PMID_42305112.txt | source | PMID:42305112 article/supplement boundary |
| PMID:42307251 | references_cache/PMID_42307251.txt | source | PMID:42307251 article/supplement boundary |
| PMID:42364169 | references_cache/PMID_42364169.txt | source | PMID:42364169 article/supplement boundary |
| PMID:42482240 | references_cache/PMID_42482240.txt | source | PMID:42482240 article/supplement boundary |
| PMID:42511722 | references_cache/PMID_42511722.txt | source | PMID:42511722 article/supplement boundary |
| PMID:42549325 | references_cache/PMID_42549325.txt | source | PMID:42549325 article/supplement boundary |
| PMID:42602126 | references_cache/PMID_42602126.txt | source | PMID:42602126 article/supplement boundary |
| PMID:42604006 | references_cache/PMID_42604006.txt | source | PMID:42604006 article/supplement boundary |
| doi:10.64898/2026.03.16.712028 | references_cache/doi_10.64898_2026.03.16.712028.md | source | doi:10.64898/2026.03.16.712028 article/supplement boundary |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Article/supplement boundary regression | passed | True | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | The repaired corpus and control/mutation/restoration tests pass. |
| Native article-only reference validation | failed | False | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | Receipt generator completed successfully; native plugin had 0 pre-separation and 79 post-separation failures. Generator exit 0 is not a reference-validation pass. |
| Focused cache, source-text and writer tests | passed | True | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | 80 passed; 12 existing dependency deprecation warnings. |
| Maintained lint checks | passed | True | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | Black passed 386 files, Ruff passed, mypy passed 49 source files. Existing gtdb_ground.py noqa warning is unrelated. |
| Historical control reproduces the receipt | passed | True | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | Fresh historical worktree reproduced the final manifest, input hashes, targets, counts and all 284 native-validation rows exactly; only run timestamps differ. |
| Final bytes against historical Git inputs | passed | True | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | All 11 article outputs verified against the historical source plus one explicit separator LF removal each; ten sidecars unchanged, one extracted exactly, 11 curated records unchanged, no mixed article caches. |

## Scientific And Domain Assessments

### Article and supplementary source separation

provenance: supported. Targets: PMID:41634815.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42099455.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42305112.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42307251.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42364169.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42482240.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. same source body; retain existing retrieval header.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42511722.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42549325.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42602126.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. extract appended bytes to missing sidecar.

### Article and supplementary source separation

provenance: supported. Targets: PMID:42604006.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: supported. Targets: doi:10.64898/2026.03.16.712028.

Article text preserved byte-for-byte except for removal of one append-separator LF; supplement source body preserved separately without overwriting an existing sidecar. Table S2 preserved in larger sidecar with Tables S1-S4.

## Findings

### mixed-article-caches: Supplementary text embedded in 11 article caches

major / resolved / confirmed; issue key: 1994-mixed-article-supplements.

The legacy append path merged independently stored supplement source text into article caches, violating the source-boundary policy and masking supplement-only native reference failures.

Disposition: All 11 article outputs and retained/extracted sidecars match the reviewed SHA-256 receipts. The final plan removes exactly one append-separator LF per article (recorded as 0a and both prefix/output hashes) to avoid new blank lines at EOF; the initial pre-repair plan retained that separator. No source text or existing sidecar bytes were altered. No supplement marker remains in article caches; canonical record bytes are unchanged. Native supplement-only failures remain explicitly open under #1996, not waived.

### supplement-routing: 79 separately supported snippets remain native article-only validation failures

minor / open / confirmed; issue key: 1996-explicit-supplement-routing.

The pinned validator ignores separate supplement caches. These 79 occurrences have retained source locations, but the normal validator still reports failures. A source-specific routing design is a separate task, not grounds to re-append sources or remove supported claims.

## Recommended Actions And Acceptance Checks

### route-supplement

Resolve #1996 with explicit source-specific locations and end-to-end validation, preserving the current reported failures until then.

- No article/supplement concatenation, union/fallback, or threshold waiver.
- Wrong or missing source locations must fail in end-to-end control/mutation/restoration tests.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cache-1 | references_cache/PMID_41634815.txt; Original supplementary boundary line 89; manifest entry 0 | supports | byte-identical sidecar retained. Article prefix is 89545 bytes; appended section is 53816 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-2 | references_cache/PMID_42099455.txt; Original supplementary boundary line 148; manifest entry 1 | supports | byte-identical sidecar retained. Article prefix is 30600 bytes; appended section is 30878 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-3 | references_cache/PMID_42305112.txt; Original supplementary boundary line 811; manifest entry 2 | supports | byte-identical sidecar retained. Article prefix is 75397 bytes; appended section is 16294 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-4 | references_cache/PMID_42307251.txt; Original supplementary boundary line 227; manifest entry 3 | supports | byte-identical sidecar retained. Article prefix is 41623 bytes; appended section is 13713 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-5 | references_cache/PMID_42364169.txt; Original supplementary boundary line 277; manifest entry 4 | supports | byte-identical sidecar retained. Article prefix is 67827 bytes; appended section is 102240 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-6 | references_cache/PMID_42482240.txt; Original supplementary boundary line 25; manifest entry 5 | supports | same source body; retain existing retrieval header. Article prefix is 3999 bytes; appended section is 1664 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-7 | references_cache/PMID_42511722.txt; Original supplementary boundary line 476; manifest entry 6 | supports | byte-identical sidecar retained. Article prefix is 61450 bytes; appended section is 10372 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-8 | references_cache/PMID_42549325.txt; Original supplementary boundary line 370; manifest entry 7 | supports | byte-identical sidecar retained. Article prefix is 86562 bytes; appended section is 2995412 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-9 | references_cache/PMID_42602126.txt; Original supplementary boundary line 443; manifest entry 8 | supports | extract appended bytes to missing sidecar. Article prefix is 94715 bytes; appended section is 7260961 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-10 | references_cache/PMID_42604006.txt; Original supplementary boundary line 70; manifest entry 9 | supports | byte-identical sidecar retained. Article prefix is 85802 bytes; appended section is 8115 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-11 | references_cache/doi_10.64898_2026.03.16.712028.md; Original supplementary boundary line 133; manifest entry 10 | supports | Table S2 preserved in larger sidecar with Tables S1-S4. Article prefix is 85613 bytes; appended section is 1616 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| snippet-audit | reports/reference_cache_separation/20261013-1994/snippet-audit.json | context_only | Offline native 0.1.7 plugin examined all 284 occurrences in 11 canonical records: 0 failures before, 79 after article separation. All 79 have case/whitespace-normalized verbatim locations in separate supplements and pass its explicitly selected supplement matcher. This is not a normal CLI pass. 203 occurrences match article text with whitespace/case folding, and two additional article matches require native punctuation normalization. |
| policy | references_cache/README.md | supports | Repository policy requires supplementary text to remain separate from article caches. |
| regression | tests/test_article_supplement_boundaries.py | supports | After repair: the boundary gate and hash-bound migration tests pass. The before arm specifically identified the 11 mixed article files. |

## Limits And Additional Notes

- Self-review, not independent approval or scientific endorsement.
- No publication figures, underlying spreadsheets/PDFs, experimental mechanisms, or external licenses were re-assessed.
- Normal reference validation does not read supplement sidecars; #1996 remains open. Separate-source matching is diagnostic only.
- Two pre-existing snippets require native punctuation normalization: Lut versus (Lut) in PMID42604006 and co-inoculated versus the source Unicode hyphen in PMID42099455. They are not literal whitespace-only matches; neither was changed.
- No curated record, schema, validator, curation history or generated community page is changed; source-only repair does not create a record-level curation event.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T044252Z-1994-source-boundaries-after
kind: repository
repository: CultureBotAI/CommunityMech
title: 'Issue 1994 bounded source-provenance review: after'
started_at: '2026-10-13T04:42:52Z'
finished_at: '2026-10-13T04:42:52Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent implements and reviews this repair; not independent
    approval.
skill: pr-adversarial-review
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: 'All 11 article/supplement boundaries repaired, with unchanged curated records
  and preserved source bytes. The scoped provenance repair passes; 79 native supplement-only
  failures remain explicitly recorded under #1996. Scientific claims are not re-reviewed.'
source:
  git_revision: 77ecab85bca112fde83ec221f5f4149666e01a78
  state: working_tree
  inputs:
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    sha256: eeef4a3c72f6660c2263fe91ec7858610797c19fa513bf641e2a6234ff4414d4
    role: context
  - path: kb/communities/Caragana_Wheat_Drought_SynCom15.yaml
    sha256: 5fe2262acd9eb4de81a2f454ac2954ab5d347a1ce7915d1cdcaf73fc584ff678
    role: context
  - path: kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml
    sha256: 23c898adcb069d4f4f36cc49783674e02fa33a814b11cdc8a3a7ed7f84f74239
    role: context
  - path: kb/communities/Ginseng_CL95_Rusty_Root_Rot_Biocontrol_SynCom.yaml
    sha256: e228c2b46ce20acca93762d68d61fe0945620902a42deb516e65fb5f87eee720
    role: context
  - path: kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml
    sha256: 59a83e4d0b1defdc5f3bae63bccb38caa87fa9fd90a6c115e5be6f518998f6ff
    role: context
  - path: kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml
    sha256: 65986397aa530933ed3b2d65d9cf8110e96b30898c3458c1d024e98fa42a81b4
    role: context
  - path: kb/communities/Nasal_SynCom_C_Bioreactor.yaml
    sha256: 4bd66811333c6960ebab5553e7ce71c8a4f92aa1d81f0fc2c9e2b4f6b75dac2e
    role: context
  - path: kb/communities/Prymnesium_Parvum_B12_Limited_SynCom.yaml
    sha256: 2e1d674f45e85230bfdd1d05aeb6f6c6b0f58b44fb478515d13b3aa7535c1225
    role: context
  - path: kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
    sha256: a634e28075ce72c27b0bb6348b68bde7ece13d970a0457281aacb8f48710ae3c
    role: context
  - path: kb/communities/Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom.yaml
    sha256: 5b74bd01d770c894a9dd65240bf47b4754d997013fa2681a63abf653a1fb82d0
    role: context
  - path: kb/communities/SynCom_ARC_Peanut_Aflatoxin_Nodulation.yaml
    sha256: 8128a35b7336eb6a0e2da4768e456cd12e84db5632b771708a70f07d6bebd5b5
    role: context
  - path: references_cache/PMID_41634815.supplement.md
    sha256: 99cbaf310c20323f40cf7005ad997da21098e7ef867c86336a2f0affd8e929a9
    role: context
  - path: references_cache/PMID_41634815.txt
    sha256: 0dc288d29a3f599742315a0034ddf4aad7c0f6523c898bd0e7f54091f5131037
    role: target
  - path: references_cache/PMID_42099455.supplement.md
    sha256: 65ecfb230839593cded3ad746a58d0274dc2b2441fdf2f500aa80b8b61398144
    role: context
  - path: references_cache/PMID_42099455.txt
    sha256: ceea4d8b5362fc7c69fbc04693442c19bfcc8a35f7d8d7431338c1246e817504
    role: target
  - path: references_cache/PMID_42305112.supplement.md
    sha256: 7a67c97aa2aead8294100ba895a393e1259010c9d14553273d2fc46facba197b
    role: context
  - path: references_cache/PMID_42305112.txt
    sha256: 8fb13fc57c6f0be2aef871a80ba0d89f99b991aa0933c1eec2c4862a4de0a415
    role: target
  - path: references_cache/PMID_42307251.supplement.md
    sha256: 292f06d875760cea5d5ca2c659dae6a0f637d8cd98d297db2aaa635fdb3042b2
    role: context
  - path: references_cache/PMID_42307251.txt
    sha256: e0f0fee88ee885a2049f2f726e05f9b6ab816346dc5186e5f1fea325464aba4e
    role: target
  - path: references_cache/PMID_42364169.supplement.md
    sha256: baca59f4f9ac9c772f51d4c28be1ad8244ee94b016a70e5b464694c0e3590a7f
    role: context
  - path: references_cache/PMID_42364169.txt
    sha256: 76ae187fe615a75d522443b9deb085bc8499efb54df080407563f901c514a4d4
    role: target
  - path: references_cache/PMID_42482240.supplement.md
    sha256: 45614f71bd112451ce0a5bb4b11f201c4e80278cb56c2cc591d5fc9bd0fcc726
    role: context
  - path: references_cache/PMID_42482240.txt
    sha256: fa818b4fb415527b08960aeb8aa118fef46555bc01b18126eb99b66dbae61210
    role: target
  - path: references_cache/PMID_42511722.supplement.md
    sha256: 6ddcbad463b48ca43da2a266f2f81e2e696c65ee54b7b4cc56b7adcd838df757
    role: context
  - path: references_cache/PMID_42511722.txt
    sha256: e7ce26edc63832f754798c439403265bf167c8eb883e4d8184a8fedd101f94ac
    role: target
  - path: references_cache/PMID_42549325.supplement.md
    sha256: 4b30395e5db1c46bfb2f87a8737c55f825dfb80394485a5315736b006ec9f50e
    role: context
  - path: references_cache/PMID_42549325.txt
    sha256: 67e0171a0f2c978c23abad3bb55ddc20b23823acd0eaa8c38601bab17a07e7f3
    role: target
  - path: references_cache/PMID_42602126.supplement.md
    sha256: 799799b556a4e3d1013b57519d9e7cefa5f3c5d80b4f6290f603b4d6c11a3a6b
    role: context
  - path: references_cache/PMID_42602126.txt
    sha256: b6524569419d9d0679f8917a8362a6afa8979713fef2de4c9b0ba1e39f913ab5
    role: target
  - path: references_cache/PMID_42604006.supplement.md
    sha256: caa01b17167192dbcc5804e7179c5de549208d36213ae120952d3639996f2ef0
    role: context
  - path: references_cache/PMID_42604006.txt
    sha256: daa8ab01bbe41d21dc9877a4c30d2bda35665d681969266e1c3ef516fb6fb806
    role: target
  - path: references_cache/README.md
    sha256: 172873b0a8b8ad2165cf44104232f09bb965ba50fe32645e0122ee01c0a79a1f
    role: context
  - path: references_cache/doi_10.64898_2026.03.16.712028.md
    sha256: 269c016a80b6efdb7215dad886853871c0b8e3cbaa849516c85c66cb1256f0ac
    role: target
  - path: references_cache/doi_10.64898_2026.03.16.712028.supplement.md
    sha256: 90b71bdcf0f071f2b99b53174601664edf903690f1bc4e61cda1b282ee85e23e
    role: context
  - path: reports/reference_cache_separation/20261013-1994/README.md
    sha256: 9e4117c3b5ef8b4adfe8096859de1ec08b3e0fe19b335c31c7f46be277fd9c23
    role: context
  - path: reports/reference_cache_separation/20261013-1994/audit.py
    sha256: 4a969599b7d9105ff05fbfcfa7d8688774119d2f6cac6e9d82c1261e609b9245
    role: context
  - path: reports/reference_cache_separation/20261013-1994/before-inputs.json
    sha256: 0afaefa0d8372509d8efc70946d3fbdee3b6ca9424f9bba29dd94fb3fad064be
    role: context
  - path: reports/reference_cache_separation/20261013-1994/manifest.json
    sha256: f01f5aa082d57dcb5e51bc44359696b9c008f73e40a08cf256026845a3244a81
    role: context
  - path: reports/reference_cache_separation/20261013-1994/snippet-audit.json
    sha256: 6245aedba15fb31d1a8080c94cd77b6ddf40e869df2a0eb96e71bbcd8ee3c1d4
    role: context
  - path: reports/reference_cache_separation/20261013-1994/targets.json
    sha256: 0035919f15928db32f3fcab8e73ee86eff84e0e1c13939f30b32c02bfcaada39
    role: context
  - path: reports/reference_cache_separation/20261013-1994/verification.json
    sha256: 8ae2b2083799392bc7cf92decf9b98509c61c67d4cd16268650e0565501ff4a2
    role: context
  - path: reports/reference_cache_separation/20261013-1994/verify.py
    sha256: c439fb679910d689ce364b616a9ffafafec404a8f8eaebebc785065c7e5e6b3a
    role: context
  - path: scripts/separate_legacy_supplements.py
    sha256: dbc44bd9ce0d7aec2baf360e65880ed5fd409069aea2ae7c48f6e8301cc37f3f
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_article_supplement_boundaries.py
    sha256: 2de48569da97099a12c29d14aac9bdb93e36cc0811c7911dd8564adf4ab5f692
    role: context
  - path: uv.lock
    sha256: 937fc64c52ddde9859c4231c12177e5b662ca40a7323fe21a5c0794d58ebbbc0
    role: context
targets:
- target_id: PMID:41634815
  path: references_cache/PMID_41634815.txt
  label: PMID:41634815 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_41634815.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_41634815.supplement.md
    role: separate supplementary source
- target_id: PMID:42099455
  path: references_cache/PMID_42099455.txt
  label: PMID:42099455 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42099455.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42099455.supplement.md
    role: separate supplementary source
- target_id: PMID:42305112
  path: references_cache/PMID_42305112.txt
  label: PMID:42305112 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42305112.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42305112.supplement.md
    role: separate supplementary source
- target_id: PMID:42307251
  path: references_cache/PMID_42307251.txt
  label: PMID:42307251 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42307251.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42307251.supplement.md
    role: separate supplementary source
- target_id: PMID:42364169
  path: references_cache/PMID_42364169.txt
  label: PMID:42364169 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42364169.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42364169.supplement.md
    role: separate supplementary source
- target_id: PMID:42482240
  path: references_cache/PMID_42482240.txt
  label: PMID:42482240 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42482240.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42482240.supplement.md
    role: separate supplementary source
- target_id: PMID:42511722
  path: references_cache/PMID_42511722.txt
  label: PMID:42511722 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42511722.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42511722.supplement.md
    role: separate supplementary source
- target_id: PMID:42549325
  path: references_cache/PMID_42549325.txt
  label: PMID:42549325 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42549325.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42549325.supplement.md
    role: separate supplementary source
- target_id: PMID:42602126
  path: references_cache/PMID_42602126.txt
  label: PMID:42602126 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42602126.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42602126.supplement.md
    role: separate supplementary source
- target_id: PMID:42604006
  path: references_cache/PMID_42604006.txt
  label: PMID:42604006 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42604006.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42604006.supplement.md
    role: separate supplementary source
- target_id: doi:10.64898/2026.03.16.712028
  path: references_cache/doi_10.64898_2026.03.16.712028.md
  label: doi:10.64898/2026.03.16.712028 article/supplement boundary
  kind: source
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/doi_10.64898_2026.03.16.712028.md
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/doi_10.64898_2026.03.16.712028.supplement.md
    role: separate supplementary source
scope:
  description: 'Source-boundary and lexical/provenance audit only: 11 article caches,
    their supplementary sidecars, and 284 cited snippet occurrences in 11 canonical
    records.'
  selection: 'Exact 11 files in #1994; recursive ignored-file-inclusive cache scan
    confirms the marker inventory. All kb/communities, kb/taxa and data/isolates YAML
    searched for these references.'
  coverage: full
  population_size: 11
  reviewed_target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  exclusions:
  - target: Scientific validity, taxonomy, causal graphs, whole-record completeness
      and non-cohort references
    reason: Not changed or assessed by this provenance-only repair.
  - target: Publisher files, figures, external license verification and fresh retrieval
    reason: Existing source bytes relocated or deduplicated only; no new provider
      or publication content fetched.
checks:
- check_id: boundary-gate
  name: Article/supplement boundary regression
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_article_supplement_boundaries.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  summary: The repaired corpus and control/mutation/restoration tests pass.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  evidence_ids:
  - regression
- check_id: native-article-validation
  name: Native article-only reference validation
  status: failed
  required: false
  command: .venv/bin/python /private/tmp/communitymech-1994-audit.py
  exit_code: 0
  summary: Receipt generator completed successfully; native plugin had 0 pre-separation
    and 79 post-separation failures. Generator exit 0 is not a reference-validation
    pass.
  scope_note: Diagnostic on all cited occurrences from the 11 references, not whole-record
    or scientific validation. Network source lookup disabled. DOI cache names normalized
    only in the temporary fixture to the native fetcher spelling.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  evidence_ids:
  - snippet-audit
- check_id: focused-suite
  name: Focused cache, source-text and writer tests
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/communitymech-1994-uv-cache
    .venv/bin/python -m pytest tests/test_article_supplement_boundaries.py tests/test_cache_supplements.py
    tests/test_reference_validator_actually_validates.py tests/test_cache_is_source_text_not_notes.py
    tests/test_no_paywalled_text_in_repo.py tests/test_writers_leave_a_trace.py -q
    --no-cov
  exit_code: 0
  expected_exit_code: 0
  summary: 80 passed; 12 existing dependency deprecation warnings.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  evidence_ids:
  - regression
- check_id: lint
  name: Maintained lint checks
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/communitymech-1994-uv-cache
    just lint
  exit_code: 0
  expected_exit_code: 0
  summary: Black passed 386 files, Ruff passed, mypy passed 49 source files. Existing
    gtdb_ground.py noqa warning is unrelated.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  evidence_ids:
  - regression
- check_id: receipt-reproduction
  name: Historical control reproduces the receipt
  status: passed
  required: true
  command: .venv/bin/python reports/reference_cache_separation/20261013-1994/audit.py
    --repo-root /private/tmp/communitymech-1994-baseline-20261013 --output-dir /private/tmp/communitymech-1994-reproduction-20261013
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh historical worktree reproduced the final manifest, input hashes,
    targets, counts and all 284 native-validation rows exactly; only run timestamps
    differ.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  evidence_ids:
  - snippet-audit
- check_id: historical-byte-verification
  name: Final bytes against historical Git inputs
  status: passed
  required: true
  command: .venv/bin/python reports/reference_cache_separation/20261013-1994/verify.py
    --output reports/reference_cache_separation/20261013-1994/verification.json
  exit_code: 0
  expected_exit_code: 0
  summary: All 11 article outputs verified against the historical source plus one
    explicit separator LF removal each; ten sidecars unchanged, one extracted exactly,
    11 curated records unchanged, no mixed article caches.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  evidence_ids:
  - cache-1
  - cache-2
  - cache-3
  - cache-4
  - cache-5
  - cache-6
  - cache-7
  - cache-8
  - cache-9
  - cache-10
  - cache-11
evidence:
- evidence_id: cache-1
  kind: record_content
  reference: references_cache/PMID_41634815.txt
  locator: Original supplementary boundary line 89; manifest entry 0
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 89545 bytes; appended
    section is 53816 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-2
  kind: record_content
  reference: references_cache/PMID_42099455.txt
  locator: Original supplementary boundary line 148; manifest entry 1
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 30600 bytes; appended
    section is 30878 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-3
  kind: record_content
  reference: references_cache/PMID_42305112.txt
  locator: Original supplementary boundary line 811; manifest entry 2
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 75397 bytes; appended
    section is 16294 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-4
  kind: record_content
  reference: references_cache/PMID_42307251.txt
  locator: Original supplementary boundary line 227; manifest entry 3
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 41623 bytes; appended
    section is 13713 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-5
  kind: record_content
  reference: references_cache/PMID_42364169.txt
  locator: Original supplementary boundary line 277; manifest entry 4
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 67827 bytes; appended
    section is 102240 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-6
  kind: record_content
  reference: references_cache/PMID_42482240.txt
  locator: Original supplementary boundary line 25; manifest entry 5
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: same source body; retain existing retrieval header. Article prefix is 3999
    bytes; appended section is 1664 bytes. Input/output SHA-256 digests and preserved
    payload offset are recorded in manifest.json.
- evidence_id: cache-7
  kind: record_content
  reference: references_cache/PMID_42511722.txt
  locator: Original supplementary boundary line 476; manifest entry 6
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 61450 bytes; appended
    section is 10372 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-8
  kind: record_content
  reference: references_cache/PMID_42549325.txt
  locator: Original supplementary boundary line 370; manifest entry 7
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 86562 bytes; appended
    section is 2995412 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-9
  kind: record_content
  reference: references_cache/PMID_42602126.txt
  locator: Original supplementary boundary line 443; manifest entry 8
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: extract appended bytes to missing sidecar. Article prefix is 94715 bytes;
    appended section is 7260961 bytes. Input/output SHA-256 digests and preserved
    payload offset are recorded in manifest.json.
- evidence_id: cache-10
  kind: record_content
  reference: references_cache/PMID_42604006.txt
  locator: Original supplementary boundary line 70; manifest entry 9
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 85802 bytes; appended
    section is 8115 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-11
  kind: record_content
  reference: references_cache/doi_10.64898_2026.03.16.712028.md
  locator: Original supplementary boundary line 133; manifest entry 10
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: Table S2 preserved in larger sidecar with Tables S1-S4. Article prefix
    is 85613 bytes; appended section is 1616 bytes. Input/output SHA-256 digests and
    preserved payload offset are recorded in manifest.json.
- evidence_id: snippet-audit
  kind: validation
  reference: reports/reference_cache_separation/20261013-1994/snippet-audit.json
  accessed_at: '2026-10-13T04:42:52Z'
  support: context_only
  summary: 'Offline native 0.1.7 plugin examined all 284 occurrences in 11 canonical
    records: 0 failures before, 79 after article separation. All 79 have case/whitespace-normalized
    verbatim locations in separate supplements and pass its explicitly selected supplement
    matcher. This is not a normal CLI pass. 203 occurrences match article text with
    whitespace/case folding, and two additional article matches require native punctuation
    normalization.'
- evidence_id: policy
  kind: record_content
  reference: references_cache/README.md
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: Repository policy requires supplementary text to remain separate from article
    caches.
- evidence_id: regression
  kind: validation
  reference: tests/test_article_supplement_boundaries.py
  accessed_at: '2026-10-13T04:42:52Z'
  support: supports
  summary: 'After repair: the boundary gate and hash-bound migration tests pass. The
    before arm specifically identified the 11 mixed article files.'
assessments:
- assessment_id: boundary-1
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:41634815
  evidence_ids:
  - cache-1
  - snippet-audit
- assessment_id: boundary-2
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:42099455
  evidence_ids:
  - cache-2
  - snippet-audit
- assessment_id: boundary-3
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:42305112
  evidence_ids:
  - cache-3
  - snippet-audit
- assessment_id: boundary-4
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:42307251
  evidence_ids:
  - cache-4
  - snippet-audit
- assessment_id: boundary-5
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:42364169
  evidence_ids:
  - cache-5
  - snippet-audit
- assessment_id: boundary-6
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. same source body; retain existing retrieval header.
  target_ids:
  - PMID:42482240
  evidence_ids:
  - cache-6
  - snippet-audit
- assessment_id: boundary-7
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:42511722
  evidence_ids:
  - cache-7
  - snippet-audit
- assessment_id: boundary-8
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:42549325
  evidence_ids:
  - cache-8
  - snippet-audit
- assessment_id: boundary-9
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. extract appended bytes to missing sidecar.
  target_ids:
  - PMID:42602126
  evidence_ids:
  - cache-9
  - snippet-audit
- assessment_id: boundary-10
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. byte-identical sidecar retained.
  target_ids:
  - PMID:42604006
  evidence_ids:
  - cache-10
  - snippet-audit
- assessment_id: boundary-11
  area: provenance
  topic: Article and supplementary source separation
  outcome: supported
  summary: Article text preserved byte-for-byte except for removal of one append-separator
    LF; supplement source body preserved separately without overwriting an existing
    sidecar. Table S2 preserved in larger sidecar with Tables S1-S4.
  target_ids:
  - doi:10.64898/2026.03.16.712028
  evidence_ids:
  - cache-11
  - snippet-audit
findings:
- finding_id: mixed-article-caches
  issue_key: 1994-mixed-article-supplements
  category: provenance
  severity: major
  status: resolved
  certainty: confirmed
  title: Supplementary text embedded in 11 article caches
  description: The legacy append path merged independently stored supplement source
    text into article caches, violating the source-boundary policy and masking supplement-only
    native reference failures.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42307251
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - PMID:42602126
  - PMID:42604006
  - doi:10.64898/2026.03.16.712028
  field_paths:
  - article-cache supplementary boundary
  evidence_ids:
  - policy
  - regression
  - snippet-audit
  - cache-1
  - cache-2
  - cache-3
  - cache-4
  - cache-5
  - cache-6
  - cache-7
  - cache-8
  - cache-9
  - cache-10
  - cache-11
  rule_id: source-boundary
  native_severity: P2
  normalization_reason: A systematic source/provenance error across 11 article caches;
    no finding that the scientific claims themselves are false.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_41634815.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_41634815.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42099455.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42099455.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42305112.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42305112.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42307251.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42307251.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42364169.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42364169.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42482240.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42482240.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42511722.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42511722.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42549325.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42549325.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42602126.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42602126.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42604006.txt
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_42604006.supplement.md
    role: separate supplementary source
  - repository: CultureBotAI/CommunityMech
    path: references_cache/doi_10.64898_2026.03.16.712028.md
    role: article cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/doi_10.64898_2026.03.16.712028.supplement.md
    role: separate supplementary source
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1994
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261013T043255Z-1994-source-boundaries-before
    finding_id: mixed-article-caches
  disposition_reason: 'All 11 article outputs and retained/extracted sidecars match
    the reviewed SHA-256 receipts. The final plan removes exactly one append-separator
    LF per article (recorded as 0a and both prefix/output hashes) to avoid new blank
    lines at EOF; the initial pre-repair plan retained that separator. No source text
    or existing sidecar bytes were altered. No supplement marker remains in article
    caches; canonical record bytes are unchanged. Native supplement-only failures
    remain explicitly open under #1996, not waived.'
- finding_id: supplement-routing
  issue_key: 1996-explicit-supplement-routing
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: 79 separately supported snippets remain native article-only validation failures
  description: The pinned validator ignores separate supplement caches. These 79 occurrences
    have retained source locations, but the normal validator still reports failures.
    A source-specific routing design is a separate task, not grounds to re-append
    sources or remove supported claims.
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - doi:10.64898/2026.03.16.712028
  field_paths:
  - snippet-audit.json rows where native_article_after is nonempty
  evidence_ids:
  - snippet-audit
  rule_id: explicit-supplement-location
  native_severity: P3
  normalization_reason: Bounded tooling/provenance limitation with the cited supplement
    source text retained; not an assertion of unsupported scientific claims or a release
    waiver.
  ownership_note: Future maintained schema/validator integration coordinated with
    upstream linkml-reference-validator; no such code is changed here.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1996
actions:
- action_id: route-supplement
  description: 'Resolve #1996 with explicit source-specific locations and end-to-end
    validation, preserving the current reported failures until then.'
  finding_ids:
  - supplement-routing
  target_ids:
  - PMID:41634815
  - PMID:42099455
  - PMID:42305112
  - PMID:42364169
  - PMID:42482240
  - PMID:42511722
  - PMID:42549325
  - doi:10.64898/2026.03.16.712028
  ownership_note: Maintained schema and upstream validator integration, outside this
    byte-separation fix.
  acceptance_checks:
  - No article/supplement concatenation, union/fallback, or threshold waiver.
  - Wrong or missing source locations must fail in end-to-end control/mutation/restoration
    tests.
limitations:
- Self-review, not independent approval or scientific endorsement.
- No publication figures, underlying spreadsheets/PDFs, experimental mechanisms, or
  external licenses were re-assessed.
- 'Normal reference validation does not read supplement sidecars; #1996 remains open.
  Separate-source matching is diagnostic only.'
- 'Two pre-existing snippets require native punctuation normalization: Lut versus
  (Lut) in PMID42604006 and co-inoculated versus the source Unicode hyphen in PMID42099455.
  They are not literal whitespace-only matches; neither was changed.'
- No curated record, schema, validator, curation history or generated community page
  is changed; source-only repair does not create a record-level curation event.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1994
- https://github.com/CultureBotAI/CommunityMech/issues/1996
```
