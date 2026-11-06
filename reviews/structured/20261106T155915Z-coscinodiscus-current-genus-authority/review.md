# Coscinodiscus CS4 review correction: current NCBI genus authority

- Review: 20261106T155915Z-coscinodiscus-current-genus-authority
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T15:52:26.966553Z
- Finished UTC: 2026-11-06T15:59:15.240151Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Withdraw the original unqualified current-genus approval: fresh NCBI resolves taxid 1434019 to genus 74032 Antarctobacter, with Mameliella as synonym. Preserve the source alias Mameliella sp. CS4, historical GTDB snapshot and all four original scientific finding heads/five actions. Add only the minor authority follow-up #2572. The known three reference-cache misses remain; no full-paper or SI reassessment is claimed.

## Scope And Provenance

Current NCBI alias/accepted-genus relationship, four exact maintained descriptor locations, prior review assertion and focused deterministic checks only.

Selection: Exactly CommunityMech:000020 in PR #2058; bounded correction for #2571 and canonical action #2572.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 08bcc178e09ebc040839ec76151efaaef889154c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000020 | kb/communities/Coscinodiscus_Synthetic_Community.yaml | maintained | Coscinodiscus Synthetic Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000020 | Fresh exit 0. |
| strict | passed | True | CommunityMech:000020 | Fresh exit 0. |
| terms | passed | True | CommunityMech:000020 | Fresh exit 0. |
| references | failed | True | CommunityMech:000020 | Fresh exit 1: three pre-existing article-cache snippet misses; no validator was weakened. |
| gtdb | passed | True | CommunityMech:000020 | Fresh exit 0. |
| gtdb-domain | passed | True | CommunityMech:000020 | Fresh exit 0. |
| history | passed | True | CommunityMech:000020 | Fresh exit 0. |
| original-review-validate | passed | True | CommunityMech:000020 | Fresh exit 0. |
| Direct read of fresh public NCBI genus response | passed | True | CommunityMech:000020 | Returned TaxId 74032 is genus Antarctobacter, synonym Mameliella, with AkaTaxIds 1434019; all four exact record descriptor paths were enumerated. |

## Scientific And Domain Assessments

### Current accepted genus versus source alias and local historical snapshots

grounding: concern. Targets: CommunityMech:000020.

Current NCBI authority resolves the old Mameliella taxid to Antarctobacter 74032.

Correct only the current-authority implication in 20261022T012643Z-coscinodiscus-record-review assessments identity, grounding and taxonomy: a local ontology-cache match is not a current NCBI accepted-name certificate. Retain the source designation Mameliella sp. CS4 explicitly. This genus-level relationship does not identify a species, a collection strain, a biological reassignment of the isolate, or the date of a taxonomic merge. The old g__Mameliella 3/3 result remains a historical crosswalk snapshot, not a mapping automatically transferable to 74032.

### Existing scientific findings and native metrics

provenance: unknown. Targets: CommunityMech:000020.

All four original finding heads and all five actions remain untouched.

No previous_occurrences is emitted for cm-000020-cultivation, cm-000020-non-graph-scope, cm-000020-gtdb-provenance or cm-000020-resources. Their action acceptance, source-access limits, five-node/two-arrow qualifiers and historical completeness/validation-quality metrics remain in the original. Those whole-record scores are not recomputed or promoted by this bounded authority observation; literature and supplementary support are outside its scope.

### Actual checks and complete local input pins

provenance: concern. Targets: CommunityMech:000020.

Native deterministic checks retain the known reference-cache failure and current input attestation.

Schema, strict, terms, GTDB shape/domain, history and original-review validation pass. Explained-reference checking fails for interaction indices 0, 1 and 3 against the selected abstract cache. The independent reviewer separately reports these as genuine main-text excerpts; this observation does not certify their primary-source reading. The actual failure is retained, completion is partial, and scientific_review is false. Source/check artifacts, earlier inspect and author helper are frozen; the final inspection and later save checks are outputs, avoiding recursive input hashes.

## Findings

### current-genus-authority: Reconcile the Mameliella source alias with current NCBI genus authority

minor / open / confirmed; issue key: cm-000020-current-genus-authority.

The four maintained descriptors still pair NCBITaxon:1434019 with Mameliella, while fresh NCBI resolves that alias to accepted genus Antarctobacter 74032. Reconcile the maintained identifier/label consistently, preserve the paper's Mameliella sp. CS4 designation, and keep any new GTDB route separate from the old 3/3 snapshot. Canonical follow-up is #2572; no record curation is performed here.

## Recommended Actions And Acceptance Checks

### reconcile-current-genus-authority

Apply the separately tracked #2572 authority correction without changing source identity or retiring unrelated curation.

- Inspect the current authoritative alias/accepted-genus relationship, then reconcile the canonical NCBITaxon identifier and label consistently across taxonomy and repeated interaction participants. Preserve the source designation Mameliella sp. CS4 explicitly.
- Do not infer an exact species, collection strain or biological reassignment from the genus relationship. UpdateDate alone is not the date of a merge event.
- Re-evaluate GTDB for the chosen maintained ID using the pinned crosswalk and actual route. Preserve the prior Mameliella 3/3 result as a historical snapshot; do not silently carry it to a changed ID or force a replacement.
- Keep existing biological findings, graph directions and evidence tiers. Run native schema, strict, term, reference, GTDB, domain and history checks after separately authorized curation, append history and regenerate the affected page.
- Keep #1359 and other 000020 curation scopes open until their own acceptance checks are met. No kb record is edited by PR #2058.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| authority | .temp/pr2058/independent-secondary/sources/ncbi-taxonomy.xml; TaxaSet/Taxon[TaxId=74032]: ScientificName, Rank, OtherNames/Synonym, AkaTaxIds | supports | The fresh NCBI response to a request including 1434019 returns genus 74032 Antarctobacter, Mameliella as a synonym, and AkaTaxIds 1434019. UpdateDate is not a merge-event date. |
| retrieval | .temp/pr2058/independent-secondary/sources/fresh-authority-receipt.json; Entry for ncbi-taxonomy.xml, retrieved 2026-11-06T15:40:47.759488+00:00 | supports | Independent reviewer retrieved the public NCBI bytes; this author directly read the relevant returned genus entry. Shared retrieval does not make this an independent author approval. |
| record | kb/communities/Coscinodiscus_Synthetic_Community.yaml; taxonomy[1].taxon_term and ecological_interactions[1,2,4].participating_taxa | supports | Four descriptors use NCBITaxon:1434019 / Mameliella. The source isolate alias CS4 remains distinct from current genus authority. No canonical bytes are changed. |
| prior | reviews/structured/20261022T012643Z-coscinodiscus-record-review/review.yaml; assessments[identity].details; assessments[grounding].summary; assessments[taxonomy].summary; findings and actions | supports | The original unqualified current-grounding approval needs this narrow correction. Its four open scientific finding heads and five actions are not superseded or reissued. |
| checks | .temp/pr2058/020-author/focused-checks.json; Eight fresh focused commands and their separately pinned stdout/stderr | supports | Seven checks pass. Explained-reference checking fails with the same three interaction snippet cache misses; a local term pass does not establish current live NCBI authority. |
| secondary-context | .temp/pr2058/independent-secondary/independent-science-three-records.json; scientific_assessments.000020; focused_checks; inspection_limits | supports | The separate independent reviewer reports main-text corroboration of the three cache-missed snippets and original scientific findings. This author observation does not repeat or certify that whole-paper/SI pass. |
| issue | .temp/pr2058/020-author/issue2572-current.json; Issue #2572 body: stable key and five acceptance checks | supports | Current canonical follow-up acceptance preserves source alias, historical GTDB provenance and all existing scientific scopes. Its corrected single-ID URL/hash pair is separate from the author's independently paired combined-response XML/retrieval input; the earlier issue snapshot is retained only as historical context. |

## Limits And Additional Notes

- Literature, supplementary sources, biological mechanisms, graph support, cultivation and resource conclusions are not scientifically reassessed by this authority-only author pass.
- Seven focused checks pass and explained-reference checking retains three existing cache misses. Passing local term checks do not override fresh NCBI accepted-name evidence.
- The old four finding heads/five actions remain independent and open; no prior occurrence or grouped review is superseded. Whole-record scores are not recomputed for this bounded observation.
- No new GTDB replay, exact species/strain assignment or merge-event dating is performed. The historical Mameliella 3/3 mapping cannot be silently transferred to a changed ID.
- Remediates review-bundle issue #2571 through an immutable observation. Canonical authority issue #2572 remains open; no kb, cache, history or generated product was edited.
- All actual local author inputs are captured via native inspection. The new inspection manifest cannot hash itself; candidate and post-save checks are later outputs. The JSON helper introduces no YAML writer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T155915Z-coscinodiscus-current-genus-authority
kind: record
repository: CultureBotAI/CommunityMech
title: 'Coscinodiscus CS4 review correction: current NCBI genus authority'
started_at: '2026-11-06T15:52:26.966553Z'
finished_at: '2026-11-06T15:59:15.240151Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Author of this bounded authority correction. Separate agents
    perform independent re-review; shared source retrieval is explicitly attributed.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'Withdraw the original unqualified current-genus approval: fresh NCBI resolves
  taxid 1434019 to genus 74032 Antarctobacter, with Mameliella as synonym. Preserve
  the source alias Mameliella sp. CS4, historical GTDB snapshot and all four original
  scientific finding heads/five actions. Add only the minor authority follow-up #2572.
  The known three reference-cache misses remain; no full-paper or SI reassessment
  is claimed.'
source:
  git_revision: 08bcc178e09ebc040839ec76151efaaef889154c
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/review-communities/reference/metrics-and-reports.md
    sha256: 2647416ac98a8f9569e0afbd826a0d1229bb4262639934848639ce536b0974fc
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 1005e1b9eb7f83306a1f88a6d22ec7954a54c2bf2e2fc15923fdaaa1111a3d2b
    role: context
  - path: .temp/pr2058/020-author/descriptor-locations.json
    sha256: 74cfb288a6dc59f23ab7a69648f1a8e8a2210b20489904e05af61abacae5e911
    role: context
  - path: .temp/pr2058/020-author/focused-checks.json
    sha256: c2e00e1ee7dc000fa8482b832039e296b6ddfa6adf34ae48244d9713aea3e876
    role: context
  - path: .temp/pr2058/020-author/format-final.json
    sha256: 20e153c63ebdc35c9fc796861d6d7b7e17de0201eba015e0217d0cde553008bb
    role: context
  - path: .temp/pr2058/020-author/format-final.stderr
    sha256: c78d4bc341e5cfb6cba20095bbb680bc8471adaac200271c9ee2cc1424564efe
    role: context
  - path: .temp/pr2058/020-author/format-final.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/format.json
    sha256: 52205d58f21e35c2f6e2a3d15c9246c4a0364063ff304a771d5a092c8a6db442
    role: context
  - path: .temp/pr2058/020-author/format.stderr
    sha256: 9762b61aab9fc22f79e44f92d6920a7a9babe3cc4f6b62c4cc6dd26797108e4e
    role: context
  - path: .temp/pr2058/020-author/format.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/full-lint.json
    sha256: d17eed87fb6dadb1ceebadd5edde5542df789a0171344fe85a49db7a69cb2ea6
    role: context
  - path: .temp/pr2058/020-author/full-lint.stderr
    sha256: 36ae6af3a1862febabe13f175ae987b587bc6551764556ee28a28594693b61b9
    role: context
  - path: .temp/pr2058/020-author/full-lint.stdout
    sha256: 1cffccf768da50ca84db43e973c69c47f795b57101ebfc1825d52472c790ab4d
    role: context
  - path: .temp/pr2058/020-author/gtdb-domain.stderr
    sha256: f9936702df665382a776479a8d7611ea0d0d0fc3125f533a1621b893f0bf23e1
    role: context
  - path: .temp/pr2058/020-author/gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2058/020-author/gtdb.stderr
    sha256: bbb5af9b0304164c6eb29550d4a0184c749111cd144e4c595cea21e056a2c456
    role: context
  - path: .temp/pr2058/020-author/gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2058/020-author/initial-inspect-receipt.json
    sha256: 323f15107623ee2dd587e1393f79ef3fe24f9bf7d1241ec2594c52406bce6267
    role: context
  - path: .temp/pr2058/020-author/initial-inspect.json
    sha256: ec493912bfe9acfc077653ccbf620e8acef623ee2ce88b60927e635653a725ea
    role: context
  - path: .temp/pr2058/020-author/input-paths.json
    sha256: beb15bfdd7a1c78522b5877ab5edf810876848b957d0fde4725da357edfcde52
    role: context
  - path: .temp/pr2058/020-author/issue2572-current.json
    sha256: b6dc7c3540361bd05035ff2d358d21f058fd62e08b23183571b79b34d91fc5d8
    role: context
  - path: .temp/pr2058/020-author/original-review-validate.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: .temp/pr2058/020-author/original-review-validate.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: .temp/pr2058/020-author/original-review.json
    sha256: c9e9366f18b66db6f34e899c182fab241e8d0af324858a9b0d6c62a4237ad3b7
    role: context
  - path: .temp/pr2058/020-author/references.stderr
    sha256: fdf7bcaf480dc41d6ddb001291d2e1479abcd14818c3683d046c1d14f980b1fc
    role: context
  - path: .temp/pr2058/020-author/references.stdout
    sha256: 04d194d37b80c5a7dbf15bddb09821a2f34511439e8dc731dd5c20d6a46f4e96
    role: context
  - path: .temp/pr2058/020-author/ruff-final.json
    sha256: 57926aa5e42306231eb2f2368c55447591816ed8f37b87071a238eee1e2ad3d5
    role: context
  - path: .temp/pr2058/020-author/ruff-final.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/ruff-final.stdout
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: .temp/pr2058/020-author/ruff-fix.json
    sha256: d0060f2b3c92b37fc3859520ea6e940df85afc4e23032878e9a525e990dc8225
    role: context
  - path: .temp/pr2058/020-author/ruff-fix.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/ruff-fix.stdout
    sha256: a13139480d1098b0e0425180b05c717b5f9742ebbc220c27144deb5eec66d774
    role: context
  - path: .temp/pr2058/020-author/ruff.json
    sha256: 1022412f4f0a5231573a29bc2b28389f1b0ce2066bf6aa3d9a0137219cc4acb5
    role: context
  - path: .temp/pr2058/020-author/ruff.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/ruff.stdout
    sha256: 62d971d7e0ae9beda5be02fc5dfd7a5ef293517007aacc6069fe9943076fef6c
    role: context
  - path: .temp/pr2058/020-author/strict.stderr
    sha256: ae70288de4761301d30eefb0693f4407944a33d01b2f3db575ecaae0b3e9505a
    role: context
  - path: .temp/pr2058/020-author/strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/020-author/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2058/020-author/targets.json
    sha256: b98ea45ea1753b2fed84ab29e79bce2afb01eaea0c63cab275b2da2ae68b8c59
    role: context
  - path: .temp/pr2058/020-author/terms.stderr
    sha256: 7a11ed344ed0236edc7d04fe14d4fdcb8a98347ab5c13563af8acf59eb05ae74
    role: context
  - path: .temp/pr2058/020-author/terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2058/020-author/validate.stderr
    sha256: c8cbc4a6ac8b774174bd574a25b58ad2d324f79c56df4d674ca4206f1e8bb9a9
    role: context
  - path: .temp/pr2058/020-author/validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2058/294-author/focused-checks.json
    sha256: ebd167d9a7a13c948783c0243061be28aa465150dc4251584b51d2005f5e4509
    role: context
  - path: .temp/pr2058/independent-secondary/independent-science-three-records.json
    sha256: b7cd8e4c121e52818e848dd2706d67cb0bb007db0f2e9eda2ac1c009c1f92f15
    role: context
  - path: .temp/pr2058/independent-secondary/sources/fresh-authority-receipt.json
    sha256: 5eca5ba7939fb205fc313af2aeda2d15ecf596f0d82f9c2a4a2dde55616246d5
    role: context
  - path: .temp/pr2058/independent-secondary/sources/ncbi-taxonomy.xml
    sha256: f84b4bbfefbd5ad827adc412e9cb6ff24da5480ba951f70960dff3fd66edf931
    role: context
  - path: .temp/pr2058/independent-third/issue2572.json
    sha256: 6ad86a3b5370ccfa30b4f093d528ed2bd36cb2f5aad4dc6cdcf89d8f12e1adf3
    role: context
  - path: AGENTS.md
    sha256: 7c35deb79ce874239f1080c2f575756ff47d1985483030878eaeb07df02d7529
    role: context
  - path: conf/record_review.yaml
    sha256: c4ad25505a87a040c57eb93f1ee9673a09389a474c6d4e1136781456ff190fc8
    role: context
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/Coscinodiscus_Synthetic_Community/2026-10-06T025228Z-codex-c5e0cf.yaml
    sha256: 7ba654d2e2a36240fc53caaf313e26a5c1ac928171dfbfb29fb9a94bee64a625
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Coscinodiscus_Synthetic_Community.yaml
    sha256: 96bf155c9e47de5f8934bbf367f392bfcee5073098125c841db171fd0b9dda1a
    role: target
  - path: references_cache/PMID_36300970.md
    sha256: 27c42cb32ffce7ca994a115959fbb6aa13ef7d2d64fc9c6179ab588a0007daad
    role: context
  - path: reviews/structured/20261022T012643Z-coscinodiscus-record-review/review.yaml
    sha256: 7f8832f3229680d086377984e7d72a0d8db22eb803f6ee7f9c260a1538d7f32c
    role: context
  - path: reviews/structured/20261106T062035Z-pr2043-kefir-state-action-correction/review.yaml
    sha256: bcdfa90b626b1230789a09c10c69746faf922cc64e7f82b1eee0a16517e404bb
    role: context
  - path: reviews/structured/20261106T154646Z-corynebacterium-shewanella-current-main/review.yaml
    sha256: d5e7bde90d611a885de16627ea55ad889b859b7e7a0d8afd59a8ebb8274c3088
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2058_020_authority_observation.py
    sha256: d662a31de67991a503f019f97c8e17f365dd1a7df11866e894d0e3059938777c
    role: context
  - path: scripts/adhoc/pr2058_294_refresh.py
    sha256: 9736f264aaf98ad1b14310160e25f293a3ba5e838a3b889338a295db7e92523b
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: 24fc4f6d5b786a15f38194ed902e9b7941e30c17f001532598e20e2898f595a0
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000020
  path: kb/communities/Coscinodiscus_Synthetic_Community.yaml
  label: Coscinodiscus Synthetic Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Coscinodiscus_Synthetic_Community.yaml
    role: canonical_record
scope:
  description: Current NCBI alias/accepted-genus relationship, four exact maintained
    descriptor locations, prior review assertion and focused deterministic checks
    only.
  selection: 'Exactly CommunityMech:000020 in PR #2058; bounded correction for #2571
    and canonical action #2572.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000020
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Fresh exit 0.
  target_ids:
  - CommunityMech:000020
  command: just --no-dotenv validate kb/communities/Coscinodiscus_Synthetic_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Fresh exit 0.
  target_ids:
  - CommunityMech:000020
  command: just --no-dotenv validate-strict kb/communities/Coscinodiscus_Synthetic_Community.yaml
    --out .temp/pr2058/020-author/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: terms
  name: terms
  status: passed
  required: true
  summary: Fresh exit 0.
  target_ids:
  - CommunityMech:000020
  command: just --no-dotenv validate-terms kb/communities/Coscinodiscus_Synthetic_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: references
  name: references
  status: failed
  required: true
  summary: 'Fresh exit 1: three pre-existing article-cache snippet misses; no validator
    was weakened.'
  target_ids:
  - CommunityMech:000020
  command: just --no-dotenv validate-references-explained kb/communities/Coscinodiscus_Synthetic_Community.yaml
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: gtdb
  name: gtdb
  status: passed
  required: true
  summary: Fresh exit 0.
  target_ids:
  - CommunityMech:000020
  command: just --no-dotenv validate-gtdb kb/communities/Coscinodiscus_Synthetic_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: gtdb-domain
  name: gtdb-domain
  status: passed
  required: true
  summary: Fresh exit 0.
  target_ids:
  - CommunityMech:000020
  command: just --no-dotenv validate-gtdb-domain kb/communities/Coscinodiscus_Synthetic_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: history
  name: history
  status: passed
  required: true
  summary: Fresh exit 0.
  target_ids:
  - CommunityMech:000020
  command: just --no-dotenv validate-history history/records/Coscinodiscus_Synthetic_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: original-review-validate
  name: original-review-validate
  status: passed
  required: true
  summary: Fresh exit 0.
  target_ids:
  - CommunityMech:000020
  command: uv run python scripts/record_review.py validate reviews/structured/20261022T012643Z-coscinodiscus-record-review/review.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current author run; these checks do not certify full source coverage
    or live authority labels.
- check_id: fresh-authority-read
  name: Direct read of fresh public NCBI genus response
  status: passed
  required: true
  summary: Returned TaxId 74032 is genus Antarctobacter, synonym Mameliella, with
    AkaTaxIds 1434019; all four exact record descriptor paths were enumerated.
  target_ids:
  - CommunityMech:000020
  evidence_ids:
  - authority
  - retrieval
  - record
evidence:
- evidence_id: authority
  kind: authority
  reference: .temp/pr2058/independent-secondary/sources/ncbi-taxonomy.xml
  locator: 'TaxaSet/Taxon[TaxId=74032]: ScientificName, Rank, OtherNames/Synonym,
    AkaTaxIds'
  summary: The fresh NCBI response to a request including 1434019 returns genus 74032
    Antarctobacter, Mameliella as a synonym, and AkaTaxIds 1434019. UpdateDate is
    not a merge-event date.
  support: supports
  accessed_at: '2026-11-06T15:59:15.240151Z'
  snapshot_sha256: f84b4bbfefbd5ad827adc412e9cb6ff24da5480ba951f70960dff3fd66edf931
- evidence_id: retrieval
  kind: validation
  reference: .temp/pr2058/independent-secondary/sources/fresh-authority-receipt.json
  locator: Entry for ncbi-taxonomy.xml, retrieved 2026-11-06T15:40:47.759488+00:00
  summary: Independent reviewer retrieved the public NCBI bytes; this author directly
    read the relevant returned genus entry. Shared retrieval does not make this an
    independent author approval.
  support: supports
  accessed_at: '2026-11-06T15:59:15.240151Z'
  snapshot_sha256: 5eca5ba7939fb205fc313af2aeda2d15ecf596f0d82f9c2a4a2dde55616246d5
- evidence_id: record
  kind: record_content
  reference: kb/communities/Coscinodiscus_Synthetic_Community.yaml
  locator: taxonomy[1].taxon_term and ecological_interactions[1,2,4].participating_taxa
  summary: Four descriptors use NCBITaxon:1434019 / Mameliella. The source isolate
    alias CS4 remains distinct from current genus authority. No canonical bytes are
    changed.
  support: supports
  accessed_at: '2026-11-06T15:59:15.240151Z'
  snapshot_sha256: 96bf155c9e47de5f8934bbf367f392bfcee5073098125c841db171fd0b9dda1a
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261022T012643Z-coscinodiscus-record-review/review.yaml
  locator: assessments[identity].details; assessments[grounding].summary; assessments[taxonomy].summary;
    findings and actions
  summary: The original unqualified current-grounding approval needs this narrow correction.
    Its four open scientific finding heads and five actions are not superseded or
    reissued.
  support: supports
  accessed_at: '2026-11-06T15:59:15.240151Z'
  snapshot_sha256: 7f8832f3229680d086377984e7d72a0d8db22eb803f6ee7f9c260a1538d7f32c
- evidence_id: checks
  kind: validation
  reference: .temp/pr2058/020-author/focused-checks.json
  locator: Eight fresh focused commands and their separately pinned stdout/stderr
  summary: Seven checks pass. Explained-reference checking fails with the same three
    interaction snippet cache misses; a local term pass does not establish current
    live NCBI authority.
  support: supports
  accessed_at: '2026-11-06T15:59:15.240151Z'
  snapshot_sha256: c2e00e1ee7dc000fa8482b832039e296b6ddfa6adf34ae48244d9713aea3e876
- evidence_id: secondary-context
  kind: prior_review
  reference: .temp/pr2058/independent-secondary/independent-science-three-records.json
  locator: scientific_assessments.000020; focused_checks; inspection_limits
  summary: The separate independent reviewer reports main-text corroboration of the
    three cache-missed snippets and original scientific findings. This author observation
    does not repeat or certify that whole-paper/SI pass.
  support: supports
  accessed_at: '2026-11-06T15:59:15.240151Z'
  snapshot_sha256: b7cd8e4c121e52818e848dd2706d67cb0bb007db0f2e9eda2ac1c009c1f92f15
- evidence_id: issue
  kind: record_content
  reference: .temp/pr2058/020-author/issue2572-current.json
  locator: 'Issue #2572 body: stable key and five acceptance checks'
  summary: Current canonical follow-up acceptance preserves source alias, historical
    GTDB provenance and all existing scientific scopes. Its corrected single-ID URL/hash
    pair is separate from the author's independently paired combined-response XML/retrieval
    input; the earlier issue snapshot is retained only as historical context.
  support: supports
  accessed_at: '2026-11-06T15:59:15.240151Z'
  snapshot_sha256: b6dc7c3540361bd05035ff2d358d21f058fd62e08b23183571b79b34d91fc5d8
assessments:
- assessment_id: bounded-authority-correction
  area: grounding
  topic: Current accepted genus versus source alias and local historical snapshots
  outcome: concern
  summary: Current NCBI authority resolves the old Mameliella taxid to Antarctobacter
    74032.
  target_ids:
  - CommunityMech:000020
  evidence_ids:
  - authority
  - retrieval
  - record
  - prior
  - checks
  details: 'Correct only the current-authority implication in 20261022T012643Z-coscinodiscus-record-review
    assessments identity, grounding and taxonomy: a local ontology-cache match is
    not a current NCBI accepted-name certificate. Retain the source designation Mameliella
    sp. CS4 explicitly. This genus-level relationship does not identify a species,
    a collection strain, a biological reassignment of the isolate, or the date of
    a taxonomic merge. The old g__Mameliella 3/3 result remains a historical crosswalk
    snapshot, not a mapping automatically transferable to 74032.'
  dimensions:
  - name: authority_rank
    value: genus
    definition: Resolution supported by the returned NCBI entry; no species or strain
      inferred
    evidence_ids:
    - authority
  - name: source_alias
    value: Mameliella sp. CS4
    definition: Source designation to retain separately from current accepted genus
    evidence_ids:
    - record
    - prior
  - name: review_scope
    value: authority/provenance only
    definition: No new full-paper, SI, mechanism, graph, abundance or cultivation
      reassessment
    evidence_ids:
    - prior
    - secondary-context
- assessment_id: unmodified-scientific-lineage
  area: provenance
  topic: Existing scientific findings and native metrics
  outcome: unknown
  summary: All four original finding heads and all five actions remain untouched.
  target_ids:
  - CommunityMech:000020
  evidence_ids:
  - prior
  - secondary-context
  details: No previous_occurrences is emitted for cm-000020-cultivation, cm-000020-non-graph-scope,
    cm-000020-gtdb-provenance or cm-000020-resources. Their action acceptance, source-access
    limits, five-node/two-arrow qualifiers and historical completeness/validation-quality
    metrics remain in the original. Those whole-record scores are not recomputed or
    promoted by this bounded authority observation; literature and supplementary support
    are outside its scope.
- assessment_id: current-validation-limits
  area: provenance
  topic: Actual checks and complete local input pins
  outcome: concern
  summary: Native deterministic checks retain the known reference-cache failure and
    current input attestation.
  target_ids:
  - CommunityMech:000020
  evidence_ids:
  - checks
  - secondary-context
  - authority
  details: Schema, strict, terms, GTDB shape/domain, history and original-review validation
    pass. Explained-reference checking fails for interaction indices 0, 1 and 3 against
    the selected abstract cache. The independent reviewer separately reports these
    as genuine main-text excerpts; this observation does not certify their primary-source
    reading. The actual failure is retained, completion is partial, and scientific_review
    is false. Source/check artifacts, earlier inspect and author helper are frozen;
    the final inspection and later save checks are outputs, avoiding recursive input
    hashes.
findings:
- finding_id: current-genus-authority
  issue_key: cm-000020-current-genus-authority
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Bounded authority/provenance reconciliation preserves the
    same source isolate and does not invalidate the community or infer a different
    species.
  rule_id: review-checklist.current-authority-and-source-alias
  status: open
  certainty: confirmed
  title: Reconcile the Mameliella source alias with current NCBI genus authority
  description: 'The four maintained descriptors still pair NCBITaxon:1434019 with
    Mameliella, while fresh NCBI resolves that alias to accepted genus Antarctobacter
    74032. Reconcile the maintained identifier/label consistently, preserve the paper''s
    Mameliella sp. CS4 designation, and keep any new GTDB route separate from the
    old 3/3 snapshot. Canonical follow-up is #2572; no record curation is performed
    here.'
  target_ids:
  - CommunityMech:000020
  field_paths:
  - taxonomy[1].taxon_term.term
  - ecological_interactions[1].participating_taxa[0].term
  - ecological_interactions[2].participating_taxa[1].term
  - ecological_interactions[4].participating_taxa[1].term
  evidence_ids:
  - authority
  - retrieval
  - record
  - prior
  - issue
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Coscinodiscus_Synthetic_Community.yaml
    role: canonical_record
actions:
- action_id: reconcile-current-genus-authority
  description: 'Apply the separately tracked #2572 authority correction without changing
    source identity or retiring unrelated curation.'
  finding_ids:
  - current-genus-authority
  target_ids:
  - CommunityMech:000020
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Coscinodiscus_Synthetic_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Inspect the current authoritative alias/accepted-genus relationship, then reconcile
    the canonical NCBITaxon identifier and label consistently across taxonomy and
    repeated interaction participants. Preserve the source designation Mameliella
    sp. CS4 explicitly.
  - Do not infer an exact species, collection strain or biological reassignment from
    the genus relationship. UpdateDate alone is not the date of a merge event.
  - Re-evaluate GTDB for the chosen maintained ID using the pinned crosswalk and actual
    route. Preserve the prior Mameliella 3/3 result as a historical snapshot; do not
    silently carry it to a changed ID or force a replacement.
  - Keep existing biological findings, graph directions and evidence tiers. Run native
    schema, strict, term, reference, GTDB, domain and history checks after separately
    authorized curation, append history and regenerate the affected page.
  - 'Keep #1359 and other 000020 curation scopes open until their own acceptance checks
    are met. No kb record is edited by PR #2058.'
limitations:
- Literature, supplementary sources, biological mechanisms, graph support, cultivation
  and resource conclusions are not scientifically reassessed by this authority-only
  author pass.
- Seven focused checks pass and explained-reference checking retains three existing
  cache misses. Passing local term checks do not override fresh NCBI accepted-name
  evidence.
- The old four finding heads/five actions remain independent and open; no prior occurrence
  or grouped review is superseded. Whole-record scores are not recomputed for this
  bounded observation.
- No new GTDB replay, exact species/strain assignment or merge-event dating is performed.
  The historical Mameliella 3/3 mapping cannot be silently transferred to a changed
  ID.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261022T012643Z-coscinodiscus-record-review
  relationship: Append-only correction of current-authority implications in identity,
    grounding and taxonomy assessments only; all four scientific finding heads and
    five actions remain untouched.
notes:
- 'Remediates review-bundle issue #2571 through an immutable observation. Canonical
  authority issue #2572 remains open; no kb, cache, history or generated product was
  edited.'
- All actual local author inputs are captured via native inspection. The new inspection
  manifest cannot hash itself; candidate and post-save checks are later outputs. The
  JSON helper introduces no YAML writer.
tags:
- pr2058
- authority-correction
- bounded-observation
- no-scientific-supersession
```
