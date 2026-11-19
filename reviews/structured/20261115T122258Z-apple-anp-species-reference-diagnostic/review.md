# Apple A+N+P: eight species-reference correspondences and complete Paenibacillus ambiguity

- Review: 20261115T122258Z-apple-anp-species-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T12:22:58.716738Z
- Finished UTC: 2026-11-15T12:22:58.857144Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The Apple A+N+P record now retains eight native species-reference GTDB correspondences, all three ordered Paenibacillus polymyxa alternatives and nine grounding statuses. Nine source stocks, original NCBI identifiers, biological claims, source quotations and earlier history remain unchanged. The actual guarded M5 application, two native inline events, one native history sidecar and eight scoped native commands are bound. The 03SUJ4/TAH1 alias and the prior member-role, alias, media-linkage and dataset-source findings remain unresolved by this diagnostic.

## Scope And Provenance

Nine selected taxonomy descriptors' GTDB correspondence/status/options, source-stock versus reference-population boundaries, and actual application/history/check provenance. Existing scientific claims are preserved without a new approval judgment.

Selection: CommunityMech:000377 is the single end-to-end application canary for the three eligible whole records 377, 428 and 459. The other two records remain unchanged during this canary. Record 471 is excluded and held separately under issues 2898 and 2899.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24f0185a869377f74ecad1425756cb5413d9aa72.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000377 | kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml # taxonomy[0,2,3,4,5,6,7,8].taxon_term.gtdb_classification; taxonomy[0,1,2,3,4,5,6,7,8].taxon_term.gtdb_grounding_status; taxonomy[1].taxon_term.gtdb_candidates | maintained | Apple A+N+P eight reference correspondences and one complete ambiguity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000377 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Preserved nine-stock source scope and unresolved alias

grounding: supported. Targets: CommunityMech:000377.

Preserve nine source stocks, their NCBI species identities and separate tissue/plant/exudate contexts. The 03SUJ4/TAH1 equivalence remains unresolved and no study assembly is newly classified. Prior member-role, alias, media and dataset findings remain outside this technical correction.

### Eight native reference populations and complete Paenibacillus alternatives

grounding: supported. Targets: CommunityMech:000377.

The exact pinned crosswalk and native resolver support the eight stored reference classifications and all three ordered Paenibacillus candidates. Preserve the rounded 0.93 and reference-population boundaries, original NCBI/stock names and unknown upstream release. Database label differences do not establish formal renaming or resolve stock identity.

### Actual bounded application, native history and technical checks

provenance: supported. Targets: CommunityMech:000377.

The actual guarded before-to-after receipt, two native inline events, one new native sidecar and eight scoped commands bind the accepted current bytes. Existing source quotations, biology and historical records are preserved. Strict successor admission, source-snippet comparison, derived products, combined QC and the prior scientific findings remain separate requirements.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000377-schema | .temp/gtdb-species-fifth-batch-20261115/377-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-strict | .temp/gtdb-species-fifth-batch-20261115/377-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-gtdb | .temp/gtdb-species-fifth-batch-20261115/377-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-domain | .temp/gtdb-species-fifth-batch-20261115/377-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-scalars | .temp/gtdb-species-fifth-batch-20261115/377-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-history | .temp/gtdb-species-fifth-batch-20261115/377-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-new-history | .temp/gtdb-species-fifth-batch-20261115/377-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-terms | .temp/gtdb-species-fifth-batch-20261115/377-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000377-paper | references_cache/PMID_40223277.txt; Retained Methods at line 46/character 9273 and Table 1 at lines 288-306; source proof explicitly binds 03SUJ4, AF6313 and AB23 rows at offsets 59335, 59398 and 59452. | supports | The construction study identifies nine distinct A/N/P stocks and their source design groups. Its tissue and plant endpoints are retained with the ANP-versus-P distinction. Stock names and source genome descriptions do not directly establish the new GTDB reference classifications. |
| 000377-followup | references_cache/PMID_40468884.txt; Retained Methods/roster at line 48: TAH1 offset 11493, NBRC101365 offset 11922, OD600 0.5 group-mixing protocol offset 15995. | context_only | The follow-up supplies genome and flower-exudate competition context while naming Terriglobus TAH1. It does not resolve the 03SUJ4 alias or turn downloaded/PacBio genome descriptions into direct GTDB assignments in this diagnostic. Equal group mixing and pathogen-density effects remain distinct from tissue disease and member reciprocal benefit. |
| 000377-database | reports/gtdb-species-fifth-batch-20261115/377-source-evidence-001.json; All nine selected occurrences, complete native_result/classify_status, exact-ID/name lookup rows, local NCBI identity rows and captured source/table hashes. | supports | Eight exact species-ID routes support reference populations 3/1, 2/1, 3/1, 3/1, 3/1, 2/1, 11/1 and 127/0.93 in index order 0,2,3,4,5,6,7,8. The name route for index 1 retains all three Paenibacillus alternatives. Species rank and reference populations do not identify study assemblies or resolve stock aliases. |
| 000377-application | .temp/gtdb-species-fifth-batch-20261115/377-applied-001/receipt.json; Actual applied flag, execution revision, before/after digests, reviewed stage receipt and captured source inputs; exact native sidecar bound separately. | supports | The guarded M5 writer at 24f0185a persisted exact 9c99bb51 after independent candidate/input review. Only eight GTDB blocks, nine statuses, one complete ambiguity list and two native inline events changed. The native EDIT sidecar separately names the exact raw application receipt; all stock, source and biological fields remain intact. |
| 000377-prior | reviews/structured/20261021T064512Z-apple-fire-blight-anp-record/review.yaml; Four findings: cm-000377-member-role-evidence, cm-000377-alias-qualification, cm-000377-media-linkage and cm-000377-dataset-evidence-source; needs_curation verdict. | context_only | The full prior scientific assessment and its four findings remain immutable. This database correction neither retires their findings nor certifies the affected role, alias, media or dataset claims. |
| 000377-history-boundary | reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml; Immutable CommunityMech:000377 row and original/current historical record hashes; current participant guard in tests/test_participating_taxa.py. | context_only | The prior two-node, zero-arrow decision and current all-nine participant boundary remain unchanged. New strict proof must admit only this bounded GTDB/history successor; no direct named batch-4 hash caller was found in the ignore-inclusive current tests search. |

## Limits And Additional Notes

- Partial technical diagnostic with scientific_review:false. Native validator success is not full scientific approval, source-snippet certification, aggregate QC completion or closure of prior findings.
- Primary coverage is the retained roster and selected Methods/assay context in PMID:40223277 and PMID:40468884. This pass did not reacquire either article, inspect figure pixels or sequence archives, classify individual study assemblies, or exhaustively reassess every scientific claim.
- The eight reference populations have 3, 2, 3, 3, 3, 2, 11 and 127 genomes at taxonomy indices 0, 2, 3, 4, 5, 6, 7 and 8. The first seven fractions are 1.0; the last is rounded 0.93. These are reference-taxon observations, not study-stock genome assignments, mixture abundances or an inferred numerator for the rounded fraction.
- Paenibacillus polymyxa AF2927 retains all three ordered native alternatives: Paenibacillus polymyxa, polymyxa_B and polymyxa_C. No alternative is selected. Streptomyces recifensis/griseoluteus, Kitasatospora papulosa/Streptomyces papulosus and Pseudomonas/Pseudomonas_E differences are database correspondences, not formal nomenclatural rulings or stock reidentifications.
- The construction paper names Terriglobus aquaticus 03SUJ4 and the follow-up reports TAH1. Their stock equivalence remains unresolved. The species-ID correspondence does not establish that equivalence; the current stock field and qualification remain unchanged.
- Preserve the two community-level nodes and zero causal arrows. Tissue disease endpoints, whole-plant ANP 33.4% versus P-only 5.4%, and flower-exudate pathogen-density assays remain distinct. Equal within-group and between-group mixing does not establish equal representation of all nine members, viable persistence or reciprocal microbial benefit.
- The prior full review's member-role evidence, alias-qualification, media-linkage and dataset-evidence-source findings are retained. This diagnostic does not supersede that scientific review, clear its needs_curation verdict or recertify inherited member-role/abundance claims.
- Crosswalk SHA256 761d5537 binds the exact bytes; its upstream release and chronology are unestablished. Native mapping_source records file mtime only. Local NCBI authority rows retain file-stat provenance rather than a full database hash or release certification.
- Local source preparation ran at 320b21d5 with Python 3.13.12. Actual M5 staging/application/checks ran at 24f0185a869377f74ecad1425756cb5413d9aa72 with Python 3.13.2. The independently reviewed local/M5 candidate difference was only two native event timestamps. Each execution retains its actual revision and runtime.
- The eight required commands comprise native history scaffolding and seven scoped validators. Source-snippet comparison, generated products, strict successor admission and combined QC are separate requirements. An ignore-inclusive search of current tests found the Apple participant guard, but no direct named batch-4 hash caller; the immutable batch-4 decision row remains untouched. New strict production admission is still required before integration.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T122258Z-apple-anp-species-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Apple A+N+P: eight species-reference correspondences and complete Paenibacillus
  ambiguity'
started_at: '2026-11-15T12:22:58.716738Z'
finished_at: '2026-11-15T12:22:58.857144Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The full current record, retained primary roster and Methods
    passages, prior scientific review and historical guard scope were read before
    staging. A peer independently read the Apple source context and all captured source
    inputs; the parent independently read both the local and actual M5 candidate diffs
    and rehashed the exact stage inputs. The shared stage/apply/check/builder machinery
    was independently reviewed and previously exercised end to end. This authored
    assessment is a partial technical diagnostic, not a new full scientific review.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The Apple A+N+P record now retains eight native species-reference GTDB correspondences,
  all three ordered Paenibacillus polymyxa alternatives and nine grounding statuses.
  Nine source stocks, original NCBI identifiers, biological claims, source quotations
  and earlier history remain unchanged. The actual guarded M5 application, two native
  inline events, one native history sidecar and eight scoped native commands are bound.
  The 03SUJ4/TAH1 alias and the prior member-role, alias, media-linkage and dataset-source
  findings remain unresolved by this diagnostic.
source:
  git_revision: 24f0185a869377f74ecad1425756cb5413d9aa72
  state: working_tree
  inputs:
  - path: .temp/gtdb-species-fifth-batch-20261115/377-applied-001/before.yaml
    sha256: 1f2e836d0bcd5ff68622188aa5eff6d82b0d7c30d9c1a0b6191ea52f0a8e0a94
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-applied-001/receipt.json
    sha256: 9422782e75d484a3edf43c9705b27a0cbef02fc7a31f702efa760f4b23a73b38
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-domain-001/native.log
    sha256: a1e376eeff8f0d1296b8aae95850c3a86cfbbc238041f9264a6d95e87ba2dd91
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-domain-001/receipt.json
    sha256: 4d7d58642aed71d0bcfd5910071a10877d50b721e60c1d1a95eceb3ee2104e3a
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-domain-001/start.json
    sha256: 80f750cc997277bd8f874a0c090c4f31a98d5061d513c3a7d80db8b44cdfa004
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-gtdb-001/native.log
    sha256: df932eafa19ea375625067f087d9bccef3607fc1cf38ee66c3b9825d878f839b
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-gtdb-001/receipt.json
    sha256: b95365db07c34b5e1855d3a425a9a9be36495fd5b6bbf8b8971bb9e3547fbd23
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-gtdb-001/start.json
    sha256: 2428decdcdb3591412598d45015d13a4e6718be49130b430cae54d9b2b8ce3d4
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-history-001/receipt.json
    sha256: d1e31b4a5e07bd809ca06771e9223dd745a92c2b9f6bab837d6b03e1ae6ba382
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-history-001/start.json
    sha256: ed9712bea21f87e9b3e3751057cb4b9a9851175f246ade2a4ec255aaecb530d1
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-m5-candidate-001/Apple_Fire_Blight_ANP_SynCom.yaml
    sha256: 9c99bb5106378c324d3fc54e96399291a7b408abdef6827f98ac59801f555b0f
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-m5-candidate-001/receipt.json
    sha256: a4acee28e961c75c335d24979d8e5740ae8903f02ee24b63d90d0ebfe02997b7
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-new-history-001/native.log
    sha256: 9060ffdfea5ac6af20a545175d9183bcb97c4ef8e65bfa86eba27d46efd55332
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-new-history-001/receipt.json
    sha256: c00f1bc0be48e054dd6c771dfeeb210c70f2ad4888143a20ffeff7dc12e5e2a4
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-new-history-001/start.json
    sha256: b6d5cc992ceb4be66234ed13c602afe010f5f6cacbe79eabb25ee2d95da392f3
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-scalars-001/native.log
    sha256: 243cd34e7aa0061b871aaaff07445f70b9a134dfbef63208bacc86820df89ce7
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-scalars-001/receipt.json
    sha256: 0157abf5419c5e32cf48dcdf141ff5a453931ab35f4b075de82d33aef4ce6c2b
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-scalars-001/start.json
    sha256: dfc7363e00a80a3119ad043d8a4c6184266ff486e4a42f15efcd8b6c7acd634f
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-schema-001/native.log
    sha256: 749be10aadc31c321fdef410c09c16d5d70f1fc9114cebada3f403b60a298869
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-schema-001/receipt.json
    sha256: 73d05bee9de2af628d2cdf642f6541db4e891aef3c5508a22a4c3583be2ab5c0
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-schema-001/start.json
    sha256: 8cdf17e3e7b8ef3c335b3b0ae3d40feb97b48cff8943c018f90c0f3ccc2c7a3e
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-strict-001/native.log
    sha256: e843916670b3d4ac725e43d6d93d94217baa93a3f3b1a9e620c96fb8c22993ef
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-strict-001/receipt.json
    sha256: a9bbc94cead2c0a002f7a384e4078a2ff0723568da4e7d48dec13c2e06ea3858
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-strict-001/start.json
    sha256: 059a971b7ee5beeb20aafd9cdf3ef93b46ad332f29a1ab8117d530e60c66a156
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-terms-001/native.log
    sha256: 995a36b6fd272a61ec9ce07fae258c8650572d064b016a6ce677e44606c2cec5
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-terms-001/receipt.json
    sha256: 9ae2f265a5fde3e1d76025b1be6837b4059b62ecf1b8fd55ddb52e48ff63194a
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/377-terms-001/start.json
    sha256: 794fc20c9df0ca0943f9af8aa9cd21cd334deb43aebdfe008f9d7a3920a3372c
    role: context
  - path: .temp/gtdb-species-fifth-batch-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/phase2-schema-20261115/species-fifth-route-four-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/species-fifth-route-four-001.json
    sha256: e5e8a432ba80f10cfb0758c626dfa56b0ab457ba7d5d4f31848407daffffa81f
    role: context
  - path: .temp/phase2-schema-20261115/species-fifth-route-four-001.log
    sha256: 1da181dcf27eb2e535156b91651576980b5a29ca98091d26d8cb4002748b7762
    role: context
  - path: .temp/phase2-schema-20261115/species-fifth-three-source-binding-001.log
    sha256: 05943f65d92cc8a41af2d49632da1592efacb636583a728dafc31c0199643499
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-09-14T214500Z-codex-apple-fire-blight-anp-syncom.yaml
    sha256: 90cff7f1166dcfd260e3450cffadcc72564bb030690a3d8af6c573be6a6ca344
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-09-14T215800Z-codex-review.yaml
    sha256: 8faf51de812d3678e62b2e147e914febf5374e756d179d51f9e267af5e942e0a
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-10-02T055533Z-codex-afb402.yaml
    sha256: a0fadad8dc11d6ef38d9b62b8c984284b3f00a0e5373272e3b6d84e8b93e4da3
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-10-05T084242Z-codex-4f54a1.yaml
    sha256: 070a6795214a7a1f935e84f230b2c4fd11e057587c25417453455920ea604591
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-11-15T121735Z-codex-6b5bd6.yaml
    sha256: 99a692780fae3ceeb399aa7aa8ab915b0c43d04bad86e02069d52c473ba341b4
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    sha256: 9c99bb5106378c324d3fc54e96399291a7b408abdef6827f98ac59801f555b0f
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_40223277.txt
    sha256: 6da021c7eb122c88477dd4283bcc25f8fb06c31864bb59870bf9ca20d9310e5f
    role: context
  - path: references_cache/PMID_40468884.txt
    sha256: e8c83245e26f3c46555f7b1fc6bf144a343002e791e3321c06c1e2f56d0532aa
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
    sha256: e21a355f676730e8e7e6de6ea663017c9b09e05a824ff383a272ab9f1399fd70
    role: context
  - path: reports/gtdb-species-fifth-batch-20261115/377-check-config-001.json
    sha256: 2a6a11a137d3e4016f5d675ecc4e914b7e25d5c9827eec94a8ab4fce97ebbc9b
    role: context
  - path: reports/gtdb-species-fifth-batch-20261115/377-review-config-001.json
    sha256: fff5cc7b292f316d80031b7a261e3f8b95d7f13ecf42f5ea3fffe633b8373b41
    role: context
  - path: reports/gtdb-species-fifth-batch-20261115/377-source-evidence-001.json
    sha256: 821eae5039bdd7a4c61570c196e7b5120fd7feef29105de2f676498d8845d9c0
    role: context
  - path: reports/gtdb-species-fifth-batch-20261115/four-route-plan-001.json
    sha256: cbed9a6ca53931e3017c140adb0d3ff3d769daa121860dee7241078642008879
    role: context
  - path: reports/gtdb-species-fifth-batch-20261115/three-authored-source-context-001.json
    sha256: ebeef6f4a613190730e3047f465842c05c777543a315f45fb0058ba725be7b4c
    role: context
  - path: reports/gtdb-species-fifth-batch-20261115/three-source-config-001.json
    sha256: f9bb6b2d4668d5ca3ea0b8933fb4f31b93b59bad970ffc893c2226f2ad572ae7
    role: context
  - path: reviews/structured/20261021T064512Z-apple-fire-blight-anp-record/review.yaml
    sha256: 15e9b349f112b6daf4fcccd051f6a9c1418e0ebdf7949e727d3e8078ef72920d
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/bind_gtdb_batch_source_context_20261115.py
    sha256: 6cdeb82122c130cd5b2e7e73bbe66bc5123fc951892f9f87edb589fb4929aac3
    role: context
  - path: scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py
    sha256: c6bf0d09dc3d01797ab5d956a4f7458a9a153a8704508f50e656729e4ee1b860
    role: context
  - path: scripts/adhoc/check_gtdb_batch_unit_20261115.py
    sha256: 723047d1ec66fa752d6cedddbb6d399b18fa7f5b7a0e27fc435c76abfeb10493
    role: context
  - path: scripts/adhoc/compose_gtdb_source_config_20261115.jq
    sha256: 45f228d7cbd89ac7b39ff0f470d6a7602e822b866133d2f9a1b462ce38f9d5a5
    role: context
  - path: scripts/adhoc/export_m5_technical_evidence_20261114.py
    sha256: a0f43f617e8921443e660d262d28713f40b4c23770b684203c37b65330cc4a5d
    role: context
  - path: scripts/adhoc/gtdb_batch_curation_20261115.py
    sha256: bc488158440416db558133cfc0609111d96f46123b66c22efbafcfef1934d144
    role: context
  - path: scripts/adhoc/report_gtdb_batch_routes_20261115.py
    sha256: 2d4732edafccba24741b728b9e672ca7fada5e50d8220162a9ccf3c5d8d875ef
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/__init__.py
    sha256: c003d906fef500e765c59c8f15ee821054e26c43e59a1be70dbc23c33f8aae66
    role: context
  - path: src/communitymech/curate/__init__.py
    sha256: a591b57cbf73ef2ddb0da6d0b7be0dd784258115ae20cf4883f6f379bcad9324
    role: context
  - path: src/communitymech/curate/curation_event.py
    sha256: 58ebdb58ac39d7a319156ec735db9ef2e9afb4c7350613039ad9dc49d65a5afc
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: 7e0a621831b28ac0f718a29c22af8052f93e006012fff77e11d92849e4852c45
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c6f6e4a5cf42e450cf55d8fcb12817591c736198e24bcd217142b4f86712b4c3
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11
    role: context
  - path: src/communitymech/validation/write_validated.py
    sha256: d19dd3b1e46856b4de67ecc17fc856aaa1034a9a97259cab3bbd54c3891fb019
    role: context
  - path: src/communitymech/validators/__init__.py
    sha256: 975d33a39c8e7173d25aa0de711f25a19158228ecfd837908c829b3f9f14cf93
    role: context
  - path: src/communitymech/validators/ncbi_domain.py
    sha256: b1e7ffc3c35c237e36c2c19fab42f1d42a14161397de9c5e726ed85897f1e262
    role: context
  - path: tests/test_participating_taxa.py
    sha256: 0bad0a41fa227759454f6cb84cd72586b654cd8600ff3efd83b1892d93724c8d
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000377
  path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  selector: taxonomy[0,2,3,4,5,6,7,8].taxon_term.gtdb_classification; taxonomy[0,1,2,3,4,5,6,7,8].taxon_term.gtdb_grounding_status;
    taxonomy[1].taxon_term.gtdb_candidates
  label: Apple A+N+P eight reference correspondences and one complete ambiguity
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: Nine selected taxonomy descriptors' GTDB correspondence/status/options,
    source-stock versus reference-population boundaries, and actual application/history/check
    provenance. Existing scientific claims are preserved without a new approval judgment.
  selection: CommunityMech:000377 is the single end-to-end application canary for
    the three eligible whole records 377, 428 and 459. The other two records remain
    unchanged during this canary. Record 471 is excluded and held separately under
    issues 2898 and 2899.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000377
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000377-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never validate kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000377-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    --out .temp/gtdb-species-fifth-batch-20261115/377-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000377-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000377-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000377-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000377-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never validate-history history/records/Apple_Fire_Blight_ANP_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000377-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Apple_Fire_Blight_ANP_SynCom --target-root kb/communities --event EDIT --outcome
    changed --sections taxonomy,curation_history --actor-name codex --model gpt-6
    --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Record eight species-reference GTDB correspondences and complete Paenibacillus
    ambiguity for the Apple ANP descriptors.' --details 'The exact pinned crosswalk
    supports eight reference-species mappings and all three ordered Paenibacillus
    polymyxa alternatives. Preserve all nine study stocks and NCBI identifiers, historical
    crosswalk-unavailability notes, exact source quotations, tissue versus flower-exudate
    assays and every biological field. Reference genome populations do not directly
    classify the study assemblies or establish study abundance; rounded0.93 is not
    an exact numerator. The Terriglobus 03SUJ4/TAH1 stock alias remains unresolved.
    Prior member-role, alias-qualification, media-linkage and dataset-source findings
    remain explicit and are not cleared by these technical checks. GTDB label differences
    are database correspondences, not formal renaming. Only eight blocks, nine statuses,
    one ambiguity list and two native inline events changed. The crosswalk release
    and chronology are unestablished. This partial technical correction does not complete
    scientific review or corpus QC. Actual apply receipt .temp/gtdb-species-fifth-batch-20261115/377-applied-001/receipt.json
    sha256:9422782e75d484a3edf43c9705b27a0cbef02fc7a31f702efa760f4b23a73b38.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000377-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000377
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000377-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000377-schema
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-schema-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-strict
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-strict-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-gtdb
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-gtdb-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-domain
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-domain-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-scalars
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-scalars-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-history
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-history-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-new-history
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-new-history-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-terms
  kind: validation
  reference: .temp/gtdb-species-fifth-batch-20261115/377-terms-001/native.log
  accessed_at: '2026-11-15T12:22:58.716738Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000377-paper
  kind: primary_source
  reference: references_cache/PMID_40223277.txt
  locator: Retained Methods at line 46/character 9273 and Table 1 at lines 288-306;
    source proof explicitly binds 03SUJ4, AF6313 and AB23 rows at offsets 59335, 59398
    and 59452.
  support: supports
  summary: The construction study identifies nine distinct A/N/P stocks and their
    source design groups. Its tissue and plant endpoints are retained with the ANP-versus-P
    distinction. Stock names and source genome descriptions do not directly establish
    the new GTDB reference classifications.
  accessed_at: '2026-11-15T12:22:58.716738Z'
- evidence_id: 000377-followup
  kind: primary_source
  reference: references_cache/PMID_40468884.txt
  locator: 'Retained Methods/roster at line 48: TAH1 offset 11493, NBRC101365 offset
    11922, OD600 0.5 group-mixing protocol offset 15995.'
  support: context_only
  summary: The follow-up supplies genome and flower-exudate competition context while
    naming Terriglobus TAH1. It does not resolve the 03SUJ4 alias or turn downloaded/PacBio
    genome descriptions into direct GTDB assignments in this diagnostic. Equal group
    mixing and pathogen-density effects remain distinct from tissue disease and member
    reciprocal benefit.
  accessed_at: '2026-11-15T12:22:58.716738Z'
- evidence_id: 000377-database
  kind: database
  reference: reports/gtdb-species-fifth-batch-20261115/377-source-evidence-001.json
  locator: All nine selected occurrences, complete native_result/classify_status,
    exact-ID/name lookup rows, local NCBI identity rows and captured source/table
    hashes.
  support: supports
  summary: Eight exact species-ID routes support reference populations 3/1, 2/1, 3/1,
    3/1, 3/1, 2/1, 11/1 and 127/0.93 in index order 0,2,3,4,5,6,7,8. The name route
    for index 1 retains all three Paenibacillus alternatives. Species rank and reference
    populations do not identify study assemblies or resolve stock aliases.
  accessed_at: '2026-11-15T12:22:58.716738Z'
- evidence_id: 000377-application
  kind: record_content
  reference: .temp/gtdb-species-fifth-batch-20261115/377-applied-001/receipt.json
  locator: Actual applied flag, execution revision, before/after digests, reviewed
    stage receipt and captured source inputs; exact native sidecar bound separately.
  support: supports
  summary: The guarded M5 writer at 24f0185a persisted exact 9c99bb51 after independent
    candidate/input review. Only eight GTDB blocks, nine statuses, one complete ambiguity
    list and two native inline events changed. The native EDIT sidecar separately
    names the exact raw application receipt; all stock, source and biological fields
    remain intact.
  accessed_at: '2026-11-15T12:22:58.716738Z'
- evidence_id: 000377-prior
  kind: prior_review
  reference: reviews/structured/20261021T064512Z-apple-fire-blight-anp-record/review.yaml
  locator: 'Four findings: cm-000377-member-role-evidence, cm-000377-alias-qualification,
    cm-000377-media-linkage and cm-000377-dataset-evidence-source; needs_curation
    verdict.'
  support: context_only
  summary: The full prior scientific assessment and its four findings remain immutable.
    This database correction neither retires their findings nor certifies the affected
    role, alias, media or dataset claims.
  accessed_at: '2026-11-15T12:22:58.716738Z'
- evidence_id: 000377-history-boundary
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
  locator: Immutable CommunityMech:000377 row and original/current historical record
    hashes; current participant guard in tests/test_participating_taxa.py.
  support: context_only
  summary: The prior two-node, zero-arrow decision and current all-nine participant
    boundary remain unchanged. New strict proof must admit only this bounded GTDB/history
    successor; no direct named batch-4 hash caller was found in the ignore-inclusive
    current tests search.
  accessed_at: '2026-11-15T12:22:58.716738Z'
assessments:
- assessment_id: 000377-source
  area: grounding
  topic: Preserved nine-stock source scope and unresolved alias
  outcome: supported
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - 000377-paper
  - 000377-followup
  - 000377-database
  - 000377-terms
  - 000377-prior
  summary: Preserve nine source stocks, their NCBI species identities and separate
    tissue/plant/exudate contexts. The 03SUJ4/TAH1 equivalence remains unresolved
    and no study assembly is newly classified. Prior member-role, alias, media and
    dataset findings remain outside this technical correction.
- assessment_id: 000377-population
  area: grounding
  topic: Eight native reference populations and complete Paenibacillus alternatives
  outcome: supported
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - 000377-database
  - 000377-gtdb
  - 000377-domain
  summary: The exact pinned crosswalk and native resolver support the eight stored
    reference classifications and all three ordered Paenibacillus candidates. Preserve
    the rounded 0.93 and reference-population boundaries, original NCBI/stock names
    and unknown upstream release. Database label differences do not establish formal
    renaming or resolve stock identity.
- assessment_id: 000377-provenance
  area: provenance
  topic: Actual bounded application, native history and technical checks
  outcome: supported
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - 000377-application
  - 000377-schema
  - 000377-strict
  - 000377-scalars
  - 000377-new-history
  - 000377-history
  - 000377-prior
  - 000377-history-boundary
  summary: The actual guarded before-to-after receipt, two native inline events, one
    new native sidecar and eight scoped commands bind the accepted current bytes.
    Existing source quotations, biology and historical records are preserved. Strict
    successor admission, source-snippet comparison, derived products, combined QC
    and the prior scientific findings remain separate requirements.
findings: []
actions: []
limitations:
- Partial technical diagnostic with scientific_review:false. Native validator success
  is not full scientific approval, source-snippet certification, aggregate QC completion
  or closure of prior findings.
- Primary coverage is the retained roster and selected Methods/assay context in PMID:40223277
  and PMID:40468884. This pass did not reacquire either article, inspect figure pixels
  or sequence archives, classify individual study assemblies, or exhaustively reassess
  every scientific claim.
- The eight reference populations have 3, 2, 3, 3, 3, 2, 11 and 127 genomes at taxonomy
  indices 0, 2, 3, 4, 5, 6, 7 and 8. The first seven fractions are 1.0; the last is
  rounded 0.93. These are reference-taxon observations, not study-stock genome assignments,
  mixture abundances or an inferred numerator for the rounded fraction.
- 'Paenibacillus polymyxa AF2927 retains all three ordered native alternatives: Paenibacillus
  polymyxa, polymyxa_B and polymyxa_C. No alternative is selected. Streptomyces recifensis/griseoluteus,
  Kitasatospora papulosa/Streptomyces papulosus and Pseudomonas/Pseudomonas_E differences
  are database correspondences, not formal nomenclatural rulings or stock reidentifications.'
- The construction paper names Terriglobus aquaticus 03SUJ4 and the follow-up reports
  TAH1. Their stock equivalence remains unresolved. The species-ID correspondence
  does not establish that equivalence; the current stock field and qualification remain
  unchanged.
- Preserve the two community-level nodes and zero causal arrows. Tissue disease endpoints,
  whole-plant ANP 33.4% versus P-only 5.4%, and flower-exudate pathogen-density assays
  remain distinct. Equal within-group and between-group mixing does not establish
  equal representation of all nine members, viable persistence or reciprocal microbial
  benefit.
- The prior full review's member-role evidence, alias-qualification, media-linkage
  and dataset-evidence-source findings are retained. This diagnostic does not supersede
  that scientific review, clear its needs_curation verdict or recertify inherited
  member-role/abundance claims.
- Crosswalk SHA256 761d5537 binds the exact bytes; its upstream release and chronology
  are unestablished. Native mapping_source records file mtime only. Local NCBI authority
  rows retain file-stat provenance rather than a full database hash or release certification.
- Local source preparation ran at 320b21d5 with Python 3.13.12. Actual M5 staging/application/checks
  ran at 24f0185a869377f74ecad1425756cb5413d9aa72 with Python 3.13.2. The independently
  reviewed local/M5 candidate difference was only two native event timestamps. Each
  execution retains its actual revision and runtime.
- The eight required commands comprise native history scaffolding and seven scoped
  validators. Source-snippet comparison, generated products, strict successor admission
  and combined QC are separate requirements. An ignore-inclusive search of current
  tests found the Apple participant guard, but no direct named batch-4 hash caller;
  the immutable batch-4 decision row remains untouched. New strict production admission
  is still required before integration.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/2898
- https://github.com/CultureBotAI/CommunityMech/issues/2899
- https://github.com/CultureBotAI/CommunityMech/pull/2900
```
