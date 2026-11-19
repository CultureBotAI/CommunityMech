# Cold-seep ANME/SRB record: bounded Methanocomedenaceae family correspondence

- Review: 20261115T103337Z-cold-seep-family-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T10:33:37.592140Z
- Finished UTC: 2026-11-15T10:33:37.715163Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The existing Candidatus Methanocomedenaceae family descriptor now carries its native 2/2 filtered-reference correspondence and matching GROUNDED status. Its broad family scope, absent stock identity, existing bacterial phylum mapping, biological claims, source quotations and old history remain unchanged. This technical correction does not revise or close the prior scientific assessment.

## Scope And Provenance

One declared family correspondence block and status, two native inline events, and actual source/application/history/gate provenance for CommunityMech:000475. No new biological, mechanistic or study-genome identification claim is assessed as established.

Selection: One whole-record family-rank canary, selected separately after the completed mixed-rank units. The reviewed population is exactly one record; other prepared records and higher-rank groups are excluded.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 832b981208364ffd3f77e317dd0ff70fd400c941.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000475 | kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml # taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Methanocomedenaceae family reference correspondence without study-MAG identification |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000475 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Family authority and source-compatible scope

grounding: supported. Targets: CommunityMech:000475.

The existing broad Methanocomedenaceae family anchor retains its authority label, rank, ANME notes and absent stock fields. No focal genus, species or experimental assembly is newly identified.

### Two-reference family population without mechanistic promotion

grounding: supported. Targets: CommunityMech:000475.

The native family route supports the exact 2/2 reference correspondence while preserving the separate bacterial phylum block. The population is not experimental replication, study abundance or proof of exclusive ANME-to-SRB electron transfer.

### Guarded actual transition with historical science intact

provenance: supported. Targets: CommunityMech:000475.

The reviewed family candidate was applied with exact external hashes and unchanged captured sources, followed by eight native scoped commands and an appended sidecar. The prior needs_curation scientific assessment and other biological findings remain unchanged; strict successor and composed integration checks remain separate.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000475-schema | .temp/gtdb-code006-20261115/genus-family-475-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-strict | .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-gtdb | .temp/gtdb-code006-20261115/genus-family-475-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-domain | .temp/gtdb-code006-20261115/genus-family-475-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-scalars | .temp/gtdb-code006-20261115/genus-family-475-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-history | .temp/gtdb-code006-20261115/genus-family-475-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-new-history | .temp/gtdb-code006-20261115/genus-family-475-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-terms | .temp/gtdb-code006-20261115/genus-family-475-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000475-paper | https://pubmed.ncbi.nlm.nih.gov/41980960/; Retained PMC13079720 lineage sections and activity/alternative-SRB passages; exact source metadata primary_locators | supports | The source identifies multiple ANME lineages in natural sediments, with a focal Methanomarinus ANME-2b population. It distinguishes sulfate-associated activity, sulfate-free archaeal methanogenesis and possible direct SRB CO respiration. These observations do not identify either crosswalk reference genome as a study MAG. |
| 000475-database | reports/gtdb-code006-20261115/genus-family-475-source-evidence-001.json; occurrences[taxonomy_index=0], native_result, exact selector and ncbi_identity_rows | supports | The existing NCBITaxon:3386223 descriptor remains family rank and resolves via ncbi_rank_f to GTDB:f__Methanocomedenaceae with support_genomes 2, total_genomes 2, fraction 1.0 and one alternative. This is a family-level database correspondence, not species assignment or study-stock evidence. |
| 000475-application | .temp/gtdb-code006-20261115/genus-family-475-applied-001/receipt.json; actual before/after and source input binding, two native events and appended sidecar | supports | The exact independently reviewed candidate was persisted on isolated M5. Only the selected family block/status and two native inline events change semantically; the existing phylum mapping and provenance, current biology, quotations and old history are preserved. |
| 000475-prior | reviews/structured/20261021T235431Z-cold-seep-co-consortium-record-review/review.yaml; family-grounding assessment and resolve-family-gtdb finding, with all other scientific findings retained | context_only | The immutable prior review requested the available family correspondence while retaining broader needs_curation findings. This limited technical successor neither rewrites that review nor approves its other disputed roles, mechanistic claims, culture omissions or missing links. |

## Limits And Additional Notes

- Partial technical assessment with scientific_review:false. The completed diagnostic and eight native gates do not establish a new full scientific review, source-assertion comparison, final corpus QC, generated-page integration or campaign completion.
- Two filtered crosswalk reference genomes support the family correspondence. They are not two study stocks, all members of the family, the focal ANME-2b MAG, relative abundance observations or an identity probability. No genus/species promotion or assembly match is inferred.
- The natural sediment source includes several ANME populations and SRB. The canonical broad family and phylum anchors, original ANME notes and absent stock fields are retained. This correction does not recast the sediment consortium as an isolated two-stock culture.
- Source examination for this unit was limited to selected retained main-text lineage, activity and alternative-mechanism passages plus the immutable prior full assessment. No new complete paper, supplement, image, workbook or study-assembly reanalysis was performed.
- The prior needs_curation assessment remains immutable, including issues 2595-2599 and its unsupported complex-substrate role, mechanistic confidence, culture-detail and data-link findings. The available family correspondence is addressed technically without an issue-state closure or new scientific clearance.
- Direct bacterial CO oxidation remains a source-supported alternative. Sulfate-free archaeal methanogenesis and sulfate-associated joint activity remain separate conditions. Mapping concordance does not prove exclusive ANME-to-SRB electron transfer or resolve maintenance versus growth interpretation.
- The source route and binding ran locally at 834ee86f with the recorded working-tree state. Actual M5 staging, application and native gates ran at frozen 832b981208364ffd3f77e317dd0ff70fd400c941 with native Python 3.13.2. Post-application receipts truthfully contain the accepted target modification and later sidecar.
- The mapping table is pinned by SHA-256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. Its file mtime is not a release identifier. Native local NCBI label/rank observations are stat-bound rather than a fresh full-database checksum claim.
- Native term validation reports its literal output without an assertion denominator. Strict successor admission and historical caller checks are separate follow-up controls; validators do not measure scientific truth.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T103337Z-cold-seep-family-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Cold-seep ANME/SRB record: bounded Methanocomedenaceae family correspondence'
started_at: '2026-11-15T10:33:37.592140Z'
finished_at: '2026-11-15T10:33:37.715163Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: A peer independently read the authored source configuration
    and retained primary context. Parent independently read the exact actual M5 candidate,
    source proof and application hashes before the guarded write. Shared native staging,
    application, gate and review machinery has separate code reviews and mutation
    controls. This is self-review of the resulting partial technical correction.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The existing Candidatus Methanocomedenaceae family descriptor now carries
  its native 2/2 filtered-reference correspondence and matching GROUNDED status. Its
  broad family scope, absent stock identity, existing bacterial phylum mapping, biological
  claims, source quotations and old history remain unchanged. This technical correction
  does not revise or close the prior scientific assessment.
source:
  git_revision: 832b981208364ffd3f77e317dd0ff70fd400c941
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/genus-family-475-applied-001/before.yaml
    sha256: aa71bf0755e21633808d22d5e88a4da0fcb79f3a2c4f84b8037a2065155e1518
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-applied-001/receipt.json
    sha256: 3090c34069ca640bb26c44f178054b25cecb1995f294bd7e24176de11d738842
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-candidate-001/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
    sha256: 9d39b50e7049f5b122c0d29fc6726f739a2013b1f1491c2ac299178f76cd9c57
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-candidate-001/receipt.json
    sha256: ca725137ff50abd1d20c342293f9607a2271b699534841b0e10df9df3ae38ce6
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-check-config-001.json
    sha256: 4a9299bc7f0396852f60d1d1de0c66ffd45beec6ae4a31fc10c5e66e6c95e7cc
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-route-plan-001.json
    sha256: 256fef7ad567ab403432d1ee7410a99c728a23a937ad38dc6e701b01deeeec39
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-domain-001/native.log
    sha256: a1c0cbe629947e97aeda69521018be413b48960012502b367ae3d6d2f554f845
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-domain-001/receipt.json
    sha256: 0400bdc06e0462cbdedf3b6f251d4f2e4c5b504114aa5bb5af8e86ed21e221ee
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-domain-001/start.json
    sha256: 67c8017b59510e3a91a80af206050202b0275fd175691152e18178ca0888e141
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-gtdb-001/native.log
    sha256: 11d0056ac944a9619ccf4e583c5fe3c6f320f735d175f3ec4fc316c1d31c493f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-gtdb-001/receipt.json
    sha256: a9faa285173e3c6a791b1fdcf3b76ed70da710dcdfd7127b1dd2c7b2a78588fb
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-gtdb-001/start.json
    sha256: 4a8b4eac6cbfcffa28cb72cea03356bb3822056bc238c651ef14b65b1cbc98dc
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-history-001/receipt.json
    sha256: 7c5f66bc02bd67ac4a53f3a4db017bc1ad763a9a68aa45a200f40d340b1991f4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-history-001/start.json
    sha256: 16d12eb04b2ad8e39ac08f6213ca4ee7e2f51ab13f7174f9ab3d56866e64a1c0
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-new-history-001/native.log
    sha256: 282e60544faea2a79ef1d1b9e84077d31032fd5008eb48b9f512d66ce465c784
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-new-history-001/receipt.json
    sha256: 6845c5309c30f5d925868a0d95ef4c7ce15fdf17a39ae3816b144a2b9ff25a09
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-new-history-001/start.json
    sha256: 2bb957545b4268bd80a91c4163bd4dc1e5070598163b01793d2404c9f9456c09
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-scalars-001/native.log
    sha256: 358bbddb4328326a25f39b93c8290bab72e641444d4ddae7df6770e23984c555
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-scalars-001/receipt.json
    sha256: c61d832d14edb5d1a083869bddf5058493c0efc97acabcbc2a100527469eb644
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-scalars-001/start.json
    sha256: fc9a86f2399abb2a7685599d82a8ec7066eabf0fedaca7bc7f3250170612df94
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-schema-001/native.log
    sha256: 796fbe33c0ea681105c78641da3ea4371e69c1fb8c495f4f6e30d19313efad67
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-schema-001/receipt.json
    sha256: a547dbeb1286cc86b85690a1073e59cd8915be8ffc18d81b9c48fd68fe33b777
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-schema-001/start.json
    sha256: eae0ee982a5ab93c7c836b6ad2d8d6cb1b2c075ac34d6fb778119492d644f27c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/native.log
    sha256: 915313ee066a99f750cba5ca81a59466f78ea099344d1ee71804b4ad96aa42ca
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/receipt.json
    sha256: afc71f9dd0ab59477dac83ddcd0609317d38cfd0dfca46ce3dc9af100d81f6ef
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/start.json
    sha256: 5cc932de834fffc681a92c49397039e252fc7545361aa84ae66b9d04034f4a6f
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-terms-001/native.log
    sha256: f9be59af822612495d2ffc24568e79e41a92350e775ebfcb920c3ea63602e41b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-terms-001/receipt.json
    sha256: e80724b1f644c610f4554e583a24c0069c31be8247fec0c646ebfaca0603abab
    role: context
  - path: .temp/gtdb-code006-20261115/genus-family-475-run-terms-001/start.json
    sha256: a13f0b39471569d7073c99ff148e81219c24c328d774a225f22a559c63563de6
    role: context
  - path: .temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/phase2-schema-20261115/genus-family-475-binding-001.log
    sha256: 209be302f62db495b7f51acfb1079f064fde7f5a8cc840970c123bb0a9eebcef
    role: context
  - path: .temp/phase2-schema-20261115/genus-family-475-route-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/genus-family-475-route-001.json
    sha256: 80e01a1ef250847e304d6056e4d252ec9b11387f6eb7ad2dfdc15fcb323c053a
    role: context
  - path: .temp/phase2-schema-20261115/genus-family-475-route-001.log
    sha256: 0bedd43ff10c1f3ae07302d680e5c432753d8232c05651f6e0f33f332350a4a8
    role: context
  - path: history/records/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium/2026-10-19T053000Z-antigravity-61e7.yaml
    sha256: 5f75965f850e329e99ac7433cbbb33988450515379d69aae49f3eb34357605ab
    role: context
  - path: history/records/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium/2026-10-20T041800Z-antigravity-aa71bf.yaml
    sha256: 0669ca9cb06f8d96a6f590b5321a17394b75c0b530a89462de6af03087278dc6
    role: context
  - path: history/records/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium/2026-11-15T103155Z-codex-a70f34.yaml
    sha256: b3103a3c2a3e33e930aabb0e180adbf798e278204fd33781af73dca2c5cb960f
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
    sha256: 9d39b50e7049f5b122c0d29fc6726f739a2013b1f1491c2ac299178f76cd9c57
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_41980960.txt
    sha256: d14f05c6e4269f5bc044cda18faf1f7d05e5392af4473e0df08a45269ed5ed6b
    role: context
  - path: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
    sha256: e9ded35a2333f9994869573f9f952b3af3191ab55528813a7f2c03639a362d3f
    role: context
  - path: reports/gtdb-code006-20261115/genus-family-475-authored-source-context-001.json
    sha256: 392eeb940b395335adec95d1aa76ec99b00a341aff4f806f6ec765c789e59e52
    role: context
  - path: reports/gtdb-code006-20261115/genus-family-475-review-config-001.json
    sha256: 14d23de8b70d175d5c31339b1189bf8740bb9ae7c5973dbcb207fb81e7503921
    role: context
  - path: reports/gtdb-code006-20261115/genus-family-475-source-config-001.json
    sha256: 8139dfc89c327bf4ac700786a0ba2a4d19acd19445ffcb02ddad4a96c6b0d4be
    role: context
  - path: reports/gtdb-code006-20261115/genus-family-475-source-evidence-001.json
    sha256: eb3db13bb8287c66de51415a9ded2cf15d868bc64dfedcd9c04eee54d5924230
    role: context
  - path: reports/phase2-completion-20261115/higher-rank-enrichment-three-source-context-001.yaml
    sha256: 0265a09b58e8e6b7b93948a37bdd2030753b6863b2ed1c006131437d5056ff91
    role: context
  - path: reviews/structured/20261021T235431Z-cold-seep-co-consortium-record-review/review.yaml
    sha256: c57635b2700c772e118e54cd05e0ee2862c5b6b907c84e4f511f493b94611207
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
    sha256: 867e974e9c55325fb1b7e32f81dcf6b7a65b6720941fd303040f5570e46ba232
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
  - path: tests/test_causal_review_batch133.py
    sha256: e55164a53b2ceb2fb4bdb7155b44492e69a829993871f7a4fcdd8de60537a295
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000475
  path: kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
  selector: taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Methanocomedenaceae family reference correspondence without study-MAG identification
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: One declared family correspondence block and status, two native inline
    events, and actual source/application/history/gate provenance for CommunityMech:000475.
    No new biological, mechanistic or study-genome identification claim is assessed
    as established.
  selection: One whole-record family-rank canary, selected separately after the completed
    mixed-rank units. The reviewed population is exactly one record; other prepared
    records and higher-rank groups are excluded.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000475
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000475-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never validate kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000475-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
    --out .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000475-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000475-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000475-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000475-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never validate-history history/records/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000475-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add the bounded Methanocomedenaceae family reference correspondence'
    --details 'The independently reviewed native candidate adds the existing Candidatus
    Methanocomedenaceae descriptor'"'"'s family correspondence (2/2 filtered reference
    genomes), matching GROUNDED status and two native inline events. Preserve family
    rank, both original taxon labels and notes, absent stock fields, the unchanged
    bacterial phylum mapping and its provenance, every biological claim, source quotation
    and old history. These reference genomes do not identify a focal Methanomarinus
    ANME-2b MAG or two study stocks. Direct SRB CO oxidation remains a source-supported
    alternative; sulfate-free archaeal methanogenesis and sulfate-associated joint
    activity remain distinct conditions. The prior full scientific assessment and
    issues 2595-2599 are not rewritten or closed. Source reporting and binding ran
    locally at 834ee86f; actual M5 staging/application ran at published 832b9812 with
    the same captured source bytes. The mapping table'"'"'s file mtime is not its
    release. This is partial database-correspondence work, not a full scientific review.
    Actual apply receipt .temp/gtdb-code006-20261115/genus-family-475-applied-001/receipt.json
    sha256:3090c34069ca640bb26c44f178054b25cecb1995f294bd7e24176de11d738842.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000475-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000475
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000475-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000475-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-schema-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-strict-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-gtdb-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-domain-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-scalars-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-history-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-new-history-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-family-475-run-terms-001/native.log
  accessed_at: '2026-11-15T10:33:37.592140Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000475-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/41980960/
  locator: Retained PMC13079720 lineage sections and activity/alternative-SRB passages;
    exact source metadata primary_locators
  support: supports
  summary: The source identifies multiple ANME lineages in natural sediments, with
    a focal Methanomarinus ANME-2b population. It distinguishes sulfate-associated
    activity, sulfate-free archaeal methanogenesis and possible direct SRB CO respiration.
    These observations do not identify either crosswalk reference genome as a study
    MAG.
  accessed_at: '2026-11-15T10:33:37.592140Z'
- evidence_id: 000475-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-family-475-source-evidence-001.json
  locator: occurrences[taxonomy_index=0], native_result, exact selector and ncbi_identity_rows
  support: supports
  summary: The existing NCBITaxon:3386223 descriptor remains family rank and resolves
    via ncbi_rank_f to GTDB:f__Methanocomedenaceae with support_genomes 2, total_genomes
    2, fraction 1.0 and one alternative. This is a family-level database correspondence,
    not species assignment or study-stock evidence.
  accessed_at: '2026-11-15T10:33:37.592140Z'
- evidence_id: 000475-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-family-475-applied-001/receipt.json
  locator: actual before/after and source input binding, two native events and appended
    sidecar
  support: supports
  summary: The exact independently reviewed candidate was persisted on isolated M5.
    Only the selected family block/status and two native inline events change semantically;
    the existing phylum mapping and provenance, current biology, quotations and old
    history are preserved.
  accessed_at: '2026-11-15T10:33:37.592140Z'
- evidence_id: 000475-prior
  kind: prior_review
  reference: reviews/structured/20261021T235431Z-cold-seep-co-consortium-record-review/review.yaml
  locator: family-grounding assessment and resolve-family-gtdb finding, with all other
    scientific findings retained
  support: context_only
  summary: The immutable prior review requested the available family correspondence
    while retaining broader needs_curation findings. This limited technical successor
    neither rewrites that review nor approves its other disputed roles, mechanistic
    claims, culture omissions or missing links.
  accessed_at: '2026-11-15T10:33:37.592140Z'
assessments:
- assessment_id: 000475-identity
  area: grounding
  topic: Family authority and source-compatible scope
  outcome: supported
  target_ids:
  - CommunityMech:000475
  evidence_ids:
  - 000475-paper
  - 000475-database
  - 000475-terms
  summary: The existing broad Methanocomedenaceae family anchor retains its authority
    label, rank, ANME notes and absent stock fields. No focal genus, species or experimental
    assembly is newly identified.
- assessment_id: 000475-population
  area: grounding
  topic: Two-reference family population without mechanistic promotion
  outcome: supported
  target_ids:
  - CommunityMech:000475
  evidence_ids:
  - 000475-database
  - 000475-gtdb
  - 000475-domain
  - 000475-prior
  summary: The native family route supports the exact 2/2 reference correspondence
    while preserving the separate bacterial phylum block. The population is not experimental
    replication, study abundance or proof of exclusive ANME-to-SRB electron transfer.
- assessment_id: 000475-provenance
  area: provenance
  topic: Guarded actual transition with historical science intact
  outcome: supported
  target_ids:
  - CommunityMech:000475
  evidence_ids:
  - 000475-application
  - 000475-prior
  - 000475-schema
  - 000475-strict
  - 000475-scalars
  - 000475-new-history
  - 000475-history
  summary: The reviewed family candidate was applied with exact external hashes and
    unchanged captured sources, followed by eight native scoped commands and an appended
    sidecar. The prior needs_curation scientific assessment and other biological findings
    remain unchanged; strict successor and composed integration checks remain separate.
findings: []
actions: []
limitations:
- Partial technical assessment with scientific_review:false. The completed diagnostic
  and eight native gates do not establish a new full scientific review, source-assertion
  comparison, final corpus QC, generated-page integration or campaign completion.
- Two filtered crosswalk reference genomes support the family correspondence. They
  are not two study stocks, all members of the family, the focal ANME-2b MAG, relative
  abundance observations or an identity probability. No genus/species promotion or
  assembly match is inferred.
- The natural sediment source includes several ANME populations and SRB. The canonical
  broad family and phylum anchors, original ANME notes and absent stock fields are
  retained. This correction does not recast the sediment consortium as an isolated
  two-stock culture.
- Source examination for this unit was limited to selected retained main-text lineage,
  activity and alternative-mechanism passages plus the immutable prior full assessment.
  No new complete paper, supplement, image, workbook or study-assembly reanalysis
  was performed.
- The prior needs_curation assessment remains immutable, including issues 2595-2599
  and its unsupported complex-substrate role, mechanistic confidence, culture-detail
  and data-link findings. The available family correspondence is addressed technically
  without an issue-state closure or new scientific clearance.
- Direct bacterial CO oxidation remains a source-supported alternative. Sulfate-free
  archaeal methanogenesis and sulfate-associated joint activity remain separate conditions.
  Mapping concordance does not prove exclusive ANME-to-SRB electron transfer or resolve
  maintenance versus growth interpretation.
- The source route and binding ran locally at 834ee86f with the recorded working-tree
  state. Actual M5 staging, application and native gates ran at frozen 832b981208364ffd3f77e317dd0ff70fd400c941
  with native Python 3.13.2. Post-application receipts truthfully contain the accepted
  target modification and later sidecar.
- The mapping table is pinned by SHA-256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd.
  Its file mtime is not a release identifier. Native local NCBI label/rank observations
  are stat-bound rather than a fresh full-database checksum claim.
- Native term validation reports its literal output without an assertion denominator.
  Strict successor admission and historical caller checks are separate follow-up controls;
  validators do not measure scientific truth.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/2595
- https://github.com/CultureBotAI/CommunityMech/issues/2596
- https://github.com/CultureBotAI/CommunityMech/issues/2597
- https://github.com/CultureBotAI/CommunityMech/issues/2598
- https://github.com/CultureBotAI/CommunityMech/issues/2599
- https://github.com/CultureBotAI/CommunityMech/pull/2853
```
