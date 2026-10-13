# Issue 1994 bounded source-provenance review: before

- Review: 20261013T043255Z-1994-source-boundaries-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-13T04:32:55Z
- Finished UTC: 2026-10-13T04:32:55Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Eleven mixed caches require byte-preserving separation.

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
| Article/supplement boundary regression | failed | True | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | The corpus guard reproduces all 11 offenders; 13 synthetic tests pass. |
| Native article-only reference validation | passed | False | PMID:41634815, PMID:42099455, PMID:42305112, PMID:42307251, PMID:42364169, PMID:42482240, PMID:42511722, PMID:42549325, PMID:42602126, PMID:42604006, doi:10.64898/2026.03.16.712028 | Receipt generator completed successfully; native plugin had 0 pre-separation and 79 post-separation failures. Generator exit 0 is not a reference-validation pass. |

## Scientific And Domain Assessments

### Article and supplementary source separation

provenance: concern. Targets: PMID:41634815.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42099455.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42305112.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42307251.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42364169.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42482240.

Supplement text is still embedded in the article evidence surface. same source body; retain existing retrieval header.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42511722.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42549325.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42602126.

Supplement text is still embedded in the article evidence surface. extract appended bytes to missing sidecar.

### Article and supplementary source separation

provenance: concern. Targets: PMID:42604006.

Supplement text is still embedded in the article evidence surface. byte-identical sidecar retained.

### Article and supplementary source separation

provenance: concern. Targets: doi:10.64898/2026.03.16.712028.

Supplement text is still embedded in the article evidence surface. Table S2 preserved in larger sidecar with Tables S1-S4.

## Findings

### mixed-article-caches: Supplementary text embedded in 11 article caches

major / open / confirmed; issue key: 1994-mixed-article-supplements.

The legacy append path merged independently stored supplement source text into article caches, violating the source-boundary policy and masking supplement-only native reference failures.

## Recommended Actions And Acceptance Checks

### separate

Apply the reviewed hash-bound separation without rewriting curated YAML or losing supplementary source text.

- Preserve every article prefix and all existing sidecar bytes.
- Extract the missing Lupinus sidecar byte-for-byte.
- Record every affected snippet and native-validator outcome without adding a fallback.
- Run control/mutation/restore regression tests and protected CI.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cache-1 | references_cache/PMID_41634815.txt; Original supplementary boundary line 89; manifest entry 0 | supports | byte-identical sidecar retained. Article prefix is 89546 bytes; appended section is 53816 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-2 | references_cache/PMID_42099455.txt; Original supplementary boundary line 148; manifest entry 1 | supports | byte-identical sidecar retained. Article prefix is 30601 bytes; appended section is 30878 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-3 | references_cache/PMID_42305112.txt; Original supplementary boundary line 811; manifest entry 2 | supports | byte-identical sidecar retained. Article prefix is 75398 bytes; appended section is 16294 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-4 | references_cache/PMID_42307251.txt; Original supplementary boundary line 227; manifest entry 3 | supports | byte-identical sidecar retained. Article prefix is 41624 bytes; appended section is 13713 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-5 | references_cache/PMID_42364169.txt; Original supplementary boundary line 277; manifest entry 4 | supports | byte-identical sidecar retained. Article prefix is 67828 bytes; appended section is 102240 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-6 | references_cache/PMID_42482240.txt; Original supplementary boundary line 25; manifest entry 5 | supports | same source body; retain existing retrieval header. Article prefix is 4000 bytes; appended section is 1664 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-7 | references_cache/PMID_42511722.txt; Original supplementary boundary line 476; manifest entry 6 | supports | byte-identical sidecar retained. Article prefix is 61451 bytes; appended section is 10372 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-8 | references_cache/PMID_42549325.txt; Original supplementary boundary line 370; manifest entry 7 | supports | byte-identical sidecar retained. Article prefix is 86563 bytes; appended section is 2995412 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-9 | references_cache/PMID_42602126.txt; Original supplementary boundary line 443; manifest entry 8 | supports | extract appended bytes to missing sidecar. Article prefix is 94716 bytes; appended section is 7260961 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-10 | references_cache/PMID_42604006.txt; Original supplementary boundary line 70; manifest entry 9 | supports | byte-identical sidecar retained. Article prefix is 85803 bytes; appended section is 8115 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| cache-11 | references_cache/doi_10.64898_2026.03.16.712028.md; Original supplementary boundary line 133; manifest entry 10 | supports | Table S2 preserved in larger sidecar with Tables S1-S4. Article prefix is 85614 bytes; appended section is 1616 bytes. Input/output SHA-256 digests and preserved payload offset are recorded in manifest.json. |
| snippet-audit | reports/reference_cache_separation/20261013-1994/snippet-audit.json | context_only | Offline native 0.1.7 plugin examined all 284 occurrences in 11 canonical records: 0 failures before, 79 after article separation. All 79 have case/whitespace-normalized verbatim locations in separate supplements and pass its explicitly selected supplement matcher. This is not a normal CLI pass. 203 occurrences match article text with whitespace/case folding, and two additional article matches require native punctuation normalization. |
| policy | references_cache/README.md | supports | Repository policy requires supplementary text to remain separate from article caches. |
| regression | tests/test_article_supplement_boundaries.py | supports | Before repair: one corpus-gate failure identifying all 11 mixed caches, 13 tests passed. The tests include control, applied mutation, restoration, byte preservation and fail-closed manifest checks. |

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
review_id: 20261013T043255Z-1994-source-boundaries-before
kind: repository
repository: CultureBotAI/CommunityMech
title: 'Issue 1994 bounded source-provenance review: before'
started_at: '2026-10-13T04:32:55Z'
finished_at: '2026-10-13T04:32:55Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent implements and reviews this repair; not independent
    approval.
skill: pr-adversarial-review
completion: completed
verdict: needs_curation
scientific_review: false
summary: Eleven mixed caches require byte-preserving separation.
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
    sha256: e0d6273fc07f1ae3ff6c8378978592949d5764e1c830735a3a7bacc9ba3f277f
    role: target
  - path: references_cache/PMID_42099455.supplement.md
    sha256: 65ecfb230839593cded3ad746a58d0274dc2b2441fdf2f500aa80b8b61398144
    role: context
  - path: references_cache/PMID_42099455.txt
    sha256: b94e222a0aea5e54f856ab247d4682ef0238739bf8daafd9f8da411294577344
    role: target
  - path: references_cache/PMID_42305112.supplement.md
    sha256: 7a67c97aa2aead8294100ba895a393e1259010c9d14553273d2fc46facba197b
    role: context
  - path: references_cache/PMID_42305112.txt
    sha256: c6e6e9b34234a6d58c0a632592a9ab866670ec676395028808509f439c4d02f6
    role: target
  - path: references_cache/PMID_42307251.supplement.md
    sha256: 292f06d875760cea5d5ca2c659dae6a0f637d8cd98d297db2aaa635fdb3042b2
    role: context
  - path: references_cache/PMID_42307251.txt
    sha256: bcb8882683d12da58c0a37f0fa64f85d3ab74b0fdebeb0c5deecdc961dcdb6be
    role: target
  - path: references_cache/PMID_42364169.supplement.md
    sha256: baca59f4f9ac9c772f51d4c28be1ad8244ee94b016a70e5b464694c0e3590a7f
    role: context
  - path: references_cache/PMID_42364169.txt
    sha256: 7362a45c8a1264c55c00552b3ff87f4340bebd228d7031971b793be17e9c1eb5
    role: target
  - path: references_cache/PMID_42482240.supplement.md
    sha256: 45614f71bd112451ce0a5bb4b11f201c4e80278cb56c2cc591d5fc9bd0fcc726
    role: context
  - path: references_cache/PMID_42482240.txt
    sha256: c911bd4adb229d1912726c8b7cc847ea2a57a9399eb4d0a56e912fd4f88ab335
    role: target
  - path: references_cache/PMID_42511722.supplement.md
    sha256: 6ddcbad463b48ca43da2a266f2f81e2e696c65ee54b7b4cc56b7adcd838df757
    role: context
  - path: references_cache/PMID_42511722.txt
    sha256: 80c07a0370ed3e2d22408aa0d36a57799b0cefb9300702d3e9b88222f472ec4a
    role: target
  - path: references_cache/PMID_42549325.supplement.md
    sha256: 4b30395e5db1c46bfb2f87a8737c55f825dfb80394485a5315736b006ec9f50e
    role: context
  - path: references_cache/PMID_42549325.txt
    sha256: a89202a5efcabd780b32998d1adff83552c725b9145e8f25d40280bd89510191
    role: target
  - path: references_cache/PMID_42602126.txt
    sha256: c37d35419d8479f813eeefd9539b3774999064492d90ea152126a7224a9ade70
    role: target
  - path: references_cache/PMID_42604006.supplement.md
    sha256: caa01b17167192dbcc5804e7179c5de549208d36213ae120952d3639996f2ef0
    role: context
  - path: references_cache/PMID_42604006.txt
    sha256: 242ded4c628a18d5e9744d71122478b5f08116ab9f90e5f88251eb3eef1b85e1
    role: target
  - path: references_cache/README.md
    sha256: c0f60b3c368123c29dcbe9bd7685b417f3ff1297e945afce48bb265ed68f5602
    role: context
  - path: references_cache/doi_10.64898_2026.03.16.712028.md
    sha256: 46a337ff25e4f9f16f874d9d305a212c9a437bdb96305d753827450e06e4be6d
    role: target
  - path: references_cache/doi_10.64898_2026.03.16.712028.supplement.md
    sha256: 90b71bdcf0f071f2b99b53174601664edf903690f1bc4e61cda1b282ee85e23e
    role: context
  - path: reports/reference_cache_separation/20261013-1994/audit.py
    sha256: ebf1e82e69d7fd9828e251b3147736c81765c99b384221fb69673b012799dd28
    role: context
  - path: reports/reference_cache_separation/20261013-1994/before-inputs.json
    sha256: 0afaefa0d8372509d8efc70946d3fbdee3b6ca9424f9bba29dd94fb3fad064be
    role: context
  - path: reports/reference_cache_separation/20261013-1994/manifest.json
    sha256: ae73ebec25c85078de8b81489ff203be069733cf4bd740dcc8902da214560872
    role: context
  - path: reports/reference_cache_separation/20261013-1994/snippet-audit.json
    sha256: 6245aedba15fb31d1a8080c94cd77b6ddf40e869df2a0eb96e71bbcd8ee3c1d4
    role: context
  - path: reports/reference_cache_separation/20261013-1994/targets.json
    sha256: 0035919f15928db32f3fcab8e73ee86eff84e0e1c13939f30b32c02bfcaada39
    role: context
  - path: scripts/separate_legacy_supplements.py
    sha256: b01f91643512b8defb1773018d8acaf02ef127bd87f1fd03415ca947e510a567
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_article_supplement_boundaries.py
    sha256: 0d4213f874e363d63e100e023448ead7e7fc3945859e81761535a3dfeb9de7b2
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
  status: failed
  required: true
  command: .venv/bin/python -m pytest tests/test_article_supplement_boundaries.py
    -q --no-cov
  exit_code: 1
  expected_exit_code: 0
  summary: The corpus guard reproduces all 11 offenders; 13 synthetic tests pass.
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
  status: passed
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
evidence:
- evidence_id: cache-1
  kind: record_content
  reference: references_cache/PMID_41634815.txt
  locator: Original supplementary boundary line 89; manifest entry 0
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 89546 bytes; appended
    section is 53816 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-2
  kind: record_content
  reference: references_cache/PMID_42099455.txt
  locator: Original supplementary boundary line 148; manifest entry 1
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 30601 bytes; appended
    section is 30878 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-3
  kind: record_content
  reference: references_cache/PMID_42305112.txt
  locator: Original supplementary boundary line 811; manifest entry 2
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 75398 bytes; appended
    section is 16294 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-4
  kind: record_content
  reference: references_cache/PMID_42307251.txt
  locator: Original supplementary boundary line 227; manifest entry 3
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 41624 bytes; appended
    section is 13713 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-5
  kind: record_content
  reference: references_cache/PMID_42364169.txt
  locator: Original supplementary boundary line 277; manifest entry 4
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 67828 bytes; appended
    section is 102240 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-6
  kind: record_content
  reference: references_cache/PMID_42482240.txt
  locator: Original supplementary boundary line 25; manifest entry 5
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: same source body; retain existing retrieval header. Article prefix is 4000
    bytes; appended section is 1664 bytes. Input/output SHA-256 digests and preserved
    payload offset are recorded in manifest.json.
- evidence_id: cache-7
  kind: record_content
  reference: references_cache/PMID_42511722.txt
  locator: Original supplementary boundary line 476; manifest entry 6
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 61451 bytes; appended
    section is 10372 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-8
  kind: record_content
  reference: references_cache/PMID_42549325.txt
  locator: Original supplementary boundary line 370; manifest entry 7
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 86563 bytes; appended
    section is 2995412 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-9
  kind: record_content
  reference: references_cache/PMID_42602126.txt
  locator: Original supplementary boundary line 443; manifest entry 8
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: extract appended bytes to missing sidecar. Article prefix is 94716 bytes;
    appended section is 7260961 bytes. Input/output SHA-256 digests and preserved
    payload offset are recorded in manifest.json.
- evidence_id: cache-10
  kind: record_content
  reference: references_cache/PMID_42604006.txt
  locator: Original supplementary boundary line 70; manifest entry 9
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: byte-identical sidecar retained. Article prefix is 85803 bytes; appended
    section is 8115 bytes. Input/output SHA-256 digests and preserved payload offset
    are recorded in manifest.json.
- evidence_id: cache-11
  kind: record_content
  reference: references_cache/doi_10.64898_2026.03.16.712028.md
  locator: Original supplementary boundary line 133; manifest entry 10
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: Table S2 preserved in larger sidecar with Tables S1-S4. Article prefix
    is 85614 bytes; appended section is 1616 bytes. Input/output SHA-256 digests and
    preserved payload offset are recorded in manifest.json.
- evidence_id: snippet-audit
  kind: validation
  reference: reports/reference_cache_separation/20261013-1994/snippet-audit.json
  accessed_at: '2026-10-13T04:32:55Z'
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
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: Repository policy requires supplementary text to remain separate from article
    caches.
- evidence_id: regression
  kind: validation
  reference: tests/test_article_supplement_boundaries.py
  accessed_at: '2026-10-13T04:32:55Z'
  support: supports
  summary: 'Before repair: one corpus-gate failure identifying all 11 mixed caches,
    13 tests passed. The tests include control, applied mutation, restoration, byte
    preservation and fail-closed manifest checks.'
assessments:
- assessment_id: boundary-1
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:41634815
  evidence_ids:
  - cache-1
  - snippet-audit
- assessment_id: boundary-2
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:42099455
  evidence_ids:
  - cache-2
  - snippet-audit
- assessment_id: boundary-3
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:42305112
  evidence_ids:
  - cache-3
  - snippet-audit
- assessment_id: boundary-4
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:42307251
  evidence_ids:
  - cache-4
  - snippet-audit
- assessment_id: boundary-5
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:42364169
  evidence_ids:
  - cache-5
  - snippet-audit
- assessment_id: boundary-6
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. same
    source body; retain existing retrieval header.
  target_ids:
  - PMID:42482240
  evidence_ids:
  - cache-6
  - snippet-audit
- assessment_id: boundary-7
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:42511722
  evidence_ids:
  - cache-7
  - snippet-audit
- assessment_id: boundary-8
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:42549325
  evidence_ids:
  - cache-8
  - snippet-audit
- assessment_id: boundary-9
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. extract
    appended bytes to missing sidecar.
  target_ids:
  - PMID:42602126
  evidence_ids:
  - cache-9
  - snippet-audit
- assessment_id: boundary-10
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. byte-identical
    sidecar retained.
  target_ids:
  - PMID:42604006
  evidence_ids:
  - cache-10
  - snippet-audit
- assessment_id: boundary-11
  area: provenance
  topic: Article and supplementary source separation
  outcome: concern
  summary: Supplement text is still embedded in the article evidence surface. Table
    S2 preserved in larger sidecar with Tables S1-S4.
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
  status: open
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
actions:
- action_id: separate
  description: Apply the reviewed hash-bound separation without rewriting curated
    YAML or losing supplementary source text.
  finding_ids:
  - mixed-article-caches
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
  ownership_note: Article and separate supplementary caches listed in the finding.
  acceptance_checks:
  - Preserve every article prefix and all existing sidecar bytes.
  - Extract the missing Lupinus sidecar byte-for-byte.
  - Record every affected snippet and native-validator outcome without adding a fallback.
  - Run control/mutation/restore regression tests and protected CI.
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
