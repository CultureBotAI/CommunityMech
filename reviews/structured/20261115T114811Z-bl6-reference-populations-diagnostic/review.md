# Chicken BL6 reference mappings and ambiguity with study-genome limits preserved

- Review: 20261115T114811Z-bl6-reference-populations-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T11:48:11.547303Z
- Finished UTC: 2026-11-15T11:48:11.677531Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Two actual guarded M5 transitions clarify the CMLH109/CMLH110 ANI notes, then retain complete salivarius/johnsonii reference ambiguity and store two exact species-ID correspondences. NCBITaxon47770 gives1123 reference genomes/fraction1.0; NCBITaxon52242 gives38/fraction0.92. Neither result independently places the experimental stock genome. All six stocks, two unselected blocks, corrected notes and existing biology remain unchanged.

## Scope And Provenance

CommunityMech:000346 taxonomy[4/5] source notes and taxonomy[1/3/4/5] GTDB fields, actual two-transition provenance, source stock/genome distinctions and eight final-byte native checks. Partial technical and source-provenance assessment, not complete scientific review.

Selection: One source-held whole record. Actual note execution3573 changed originalc4534293 to65f331a4. Real maintained ROOT2139fa42fe538c110f2b91a6e85872e9a30b472b contains that intermediate. A separate M5 checkout at849247f9c3bef1ddeb817327f6b777e291207f10 applied final313ebed0 and ran the eight checks below.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 849247f9c3bef1ddeb817327f6b777e291207f10.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000346 | kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml # taxonomy[1].taxon_term.gtdb_grounding_status; taxonomy[1].taxon_term.gtdb_candidates; taxonomy[3].taxon_term.gtdb_grounding_status; taxonomy[3].taxon_term.gtdb_candidates; taxonomy[4].taxon_term.notes; taxonomy[4].taxon_term.gtdb_classification; taxonomy[4].taxon_term.gtdb_grounding_status; taxonomy[5].taxon_term.notes; taxonomy[5].taxon_term.gtdb_classification; taxonomy[5].taxon_term.gtdb_grounding_status | maintained | Four descriptor routes with source stock, ANI and population distinctions |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000346 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Source-reported study genomes remain distinct from reference mappings

grounding: supported. Targets: CommunityMech:000346.

Corrected notes preserve the source's WGS and ANI comparisons while avoiding independent study-stock GTDB placement. All six stocks, current names, genus-only CMLH124 and source-reference distinctions remain unchanged.

### Complete two-way and three-way species-name ambiguity

grounding: supported. Targets: CommunityMech:000346.

Indices1/3 retain all two and three native alternatives with AMBIGUOUS status. No cluster is selected for CMLH112 or CMLH106, and no unsupported reference denominator or stock probability is inferred.

### Two exact species-ID reference blocks

grounding: supported. Targets: CommunityMech:000346.

Indices4/5 store crispatus1123/1.0 and gallinarum38/0.92 with native lineages and GROUNDED statuses. GROUNDED concerns the encoded descriptor correspondence, not a verified experimental assembly. Corrected notes and unselected0/2 blocks remain exact.

### Two actual transitions with distinct final-byte checks

provenance: supported. Targets: CommunityMech:000346.

Both actual application chains and sidecars are captured. Eight final-byte native commands passed separately from the note-only checks. Maintained2139 and actual8492 have distinct roles. Composite controls, generated products and combined QC remain subsequent work; prior biological findings and immutable history are preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000346-schema | .temp/gtdb-source-holds-20261115/bl6346-mapping-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-strict | .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-gtdb | .temp/gtdb-source-holds-20261115/bl6346-mapping-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-domain | .temp/gtdb-source-holds-20261115/bl6346-mapping-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-scalars | .temp/gtdb-source-holds-20261115/bl6346-mapping-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-history | .temp/gtdb-source-holds-20261115/bl6346-mapping-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-new-history | .temp/gtdb-source-holds-20261115/bl6346-mapping-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-terms | .temp/gtdb-source-holds-20261115/bl6346-mapping-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000346-primary | PMID:42351244; Retained primary Methods genome sequencing, stock roster and Table1 ANI comparisons and caption; data availability; exact source metadata primary_locators | supports | The source identifies all six CMLH stocks and reports CMLH109/CMLH110 genome ANI97.91/98.05percent to species type-strain references. This pass does not independently verify their study assemblies or equate those references with GTDB stock assignments. |
| 000346-native | reports/gtdb-source-holds-20261115/bl6346-final-source-evidence-001.json; Selected taxonomy1/3/4/5 full native_result, classify_status, local authority and captured source populations | supports | Native ncbi_name1624 returns salivarius/sp945923665, and ncbi_name33959 returns johnsonii/sp945980025/sp947171515. Exact47770 gives crispatus1123/fraction1.0 and exact52242 gallinarum38/fraction0.92. These are descriptor-reference populations; pre-application NOT_ATTEMPTED for missing stored blocks did not mean absent database correspondence. |
| 000346-note-transition | reports/gtdb-source-holds-20261115/bl6346-note-checkpoint-001.json; Actual note plan/stage/apply/before bytes, native104614Z sidecar and56-input checkpoint | supports | The first actual transition changed exactly notes4/5 and appended one native event,c4534293 to65f331a4. Eight note-only checks passed. Real maintained2139 preserves that intermediate separately from actual execution3573. |
| 000346-mapping-transition | .temp/gtdb-source-holds-20261115/bl6346-mapping-applied-m5-001/receipt.json; Actual applied/before/after/source inputs and independently accepted candidate313ebed0 | supports | Native ground-and-status persisted65f331a4 to313ebed0: two complete ambiguity sets, two reference blocks and four statuses plus two native events. Corrected notes, unselected blocks0/2, all six stock identities, evidence and biology remain exact. |
| 000346-prior | reviews/structured/20261021T172345Z-chicken-bl6-record/review.yaml; Findings phenotype-abundance, culture-context, evidence-placement and gtdb-completeness; immutable batch11 ledger and current caller | context_only | The current mappings address the narrow prior request to recover two exact-ID descriptor blocks, without revising that historical review or closing its other three scientific finding groups. Current source and biological predicates remain required; strict composite admission follows the complete saved-input checkpoint. |

## Limits And Additional Notes

- Partial diagnostic scientific_review:false. Native validity and reference correspondence do not establish whole-record scientific approval, corpus QC, release clearance or automatic closure of earlier findings.
- The complete canonical record, retained prior review and selected primary Methods, stock roster, genome/ANI Table1 and data-availability passages were inspected. No new figure-pixel, supplementary-file, sequence, study-assembly or full-paper review was performed. Earlier full-review observations remain historical inputs.
- The paper reports sequencing all six isolates and ANI97.91/98.05 percent for CMLH109/CMLH110 against species type-strain references. These are source-reported genome comparisons, not independently verified GTDB placement of those study assemblies. Data available on request is not proof that public assemblies are absent.
- The salivarius1624 and johnsonii33959 native routes use species-name lookup and return two and three alternatives respectively. All alternatives remain unselected; the source stock names do not resolve them. No ambiguity-route genome denominator, identity probability or new nomenclatural assignment is inferred.
- The exact47770 population1123/fraction1.0 and exact52242 population38/fraction0.92 describe reference populations. Rounded0.92 is not unanimity or a recoverable exact numerator. These counts are not six-member inoculum counts, abundance, identity probabilities or evidence of stock-specific genome placement.
- The pinned761 crosswalk's upstream release remains unestablished; file mtime does not identify a release. Local and M5 NCBI file-stat observations are separate execution provenance, not a full database checksum or certified ontology version.
- Keep all six stocks, source-preferred names, CMLH124 genus-level identity and its source-reported93.27percent ANI distinction, the two unselected mapping blocks at0/2, the one community-level node and zero arrows. Chicken host and Salmonella challenge are not community members. Preserving unselected fields does not newly certify their biological or mapping claims.
- The prior review's phenotype-abundance, culture-context and evidence-placement findings remain outside this correction. In particular, host markers do not establish broader barrier/liver function, DOMINANT is not measured strain persistence, isolation recipes do not establish final propagation, membership snippets do not by themselves establish antagonist roles, and the existing ANI evidence-source tag and historical unread-figure wording are unchanged.
- The note-only intermediate had its own eight checks and56-input checkpoint. The eight required checks below are distinct actual commands on final mapping bytes, with a separate native sidecar. Actual execution3573/8492 is separate from the maintained2139 intermediate.
- The original batch11 ledger and current biological assertions remain required. Exact two-transition composite admission, its mutation controls, generated products, reference-snippet validation and combined QC are subsequent work. No general note exemption or rewritten historical scientific assessment is introduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T114811Z-bl6-reference-populations-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: Chicken BL6 reference mappings and ambiguity with study-genome limits preserved
started_at: '2026-11-15T11:48:11.547303Z'
finished_at: '2026-11-15T11:48:11.677531Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored bounded database and provenance assessment. The parent
    independently read both source plans, the complete note and mapping candidates,
    their captured inputs and the actual note checkpoint. Shared native writer, engine,
    checker and builder were independently reviewed previously. This assessment is
    self-review, not independent whole-record scientific approval.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Two actual guarded M5 transitions clarify the CMLH109/CMLH110 ANI notes,
  then retain complete salivarius/johnsonii reference ambiguity and store two exact
  species-ID correspondences. NCBITaxon47770 gives1123 reference genomes/fraction1.0;
  NCBITaxon52242 gives38/fraction0.92. Neither result independently places the experimental
  stock genome. All six stocks, two unselected blocks, corrected notes and existing
  biology remain unchanged.
source:
  git_revision: 849247f9c3bef1ddeb817327f6b777e291207f10
  state: working_tree
  inputs:
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-applied-m5-001/before.yaml
    sha256: 65f331a490b1101f9ffaa421d863bbb078f32ea75a4fb55fc4f10c861be29cf4
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-applied-m5-001/receipt.json
    sha256: b46444f1e80802f9cf2b55101e9b352da63a39f0b19a20322dcd24f09d10ac4a
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-domain-001/native.log
    sha256: 436366dd22ab8a27a3cd442c88e850e1954ca7f167ceb665fdecd1c70e06d82e
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-domain-001/receipt.json
    sha256: a6b09053f553ba57b375c53d410cb0c51de9e086dd7268f830f1248c53504164
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-domain-001/start.json
    sha256: 1769133236b49f7177aff6f1807f15c76eca2495aba9a2703abaf85fc0da9b0a
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-gtdb-001/native.log
    sha256: 0b84f10ccfd223dea4f5cfe86c01c13fa3815ec40f1b812cbbd39b32b9fe5a8b
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-gtdb-001/receipt.json
    sha256: be5f627841195cec6267ea1204e7db02781360ca90b49082104b452eb4b76117
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-gtdb-001/start.json
    sha256: 862b6b2272fb7e7cc989a650f30d947a1d592d1f1efdb18ffdbdc879224e347d
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-history-001/receipt.json
    sha256: 45dd6d4bda9f6e7c905585b13ff6ca0f84032547daa4d965eb397b18db54b1c4
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-history-001/start.json
    sha256: 2137e05dca41f629e679eda43a458a88eab664a50b19c87e37726bac00f7226b
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-new-history-001/native.log
    sha256: 663e8f4e896e3571164ba66ef2de25ebcdb1161543850f8581eaa770f07c44f9
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-new-history-001/receipt.json
    sha256: edfe48dcc73ca67e7201cfc2820ccb48bac23c7055ace1f8f3e11f6bbde8956f
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-new-history-001/start.json
    sha256: 7530b81eef389c50d9dbb06a53c7425e370cbdbf822dc5038f64834d41f4e306
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-scalars-001/native.log
    sha256: 70cb23b1c83393ed2be9d355599615e95b2d9d523b083e95fb399e112145b32b
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-scalars-001/receipt.json
    sha256: 441dcd7a05daaa192100e9e92c01f98c351ae6151025dde43d8a4467e50f09f1
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-scalars-001/start.json
    sha256: 294b4b462589cb76e5527a783ac1b3e6786552ccaab58237e3c364b3ab7dffc9
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-schema-001/native.log
    sha256: 3e151d91ef2c5d1d25559fbddd123b652bac4b71bb2ef3c16ca6429b3411c5e1
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-schema-001/receipt.json
    sha256: 9c44c53f6b45d85281666ad95ae22b7176ca8dbabdc52a13f24d5b29d7a9c134
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-schema-001/start.json
    sha256: e856f3a90c72d4e10fb3f8342453fa1256507f86050d131712e254ae54ce0bcd
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-stage-m5-001/Chicken_BL6_AntiSalmonella_SynCom.yaml
    sha256: 313ebed02de92edf0ced54c3909c6dc5bcf451782aa264ac1f4ef140e4530658
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-stage-m5-001/receipt.json
    sha256: 314e38098026a765b48ebdc8b11c7325b55a61e2050de7113b12c165980e9dae
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/native.log
    sha256: a1adbd90bef8db9beb2b517cbbd16a34631c2890255c242f59def5afbd32a93d
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/receipt.json
    sha256: e4391ae3689b9ea7d4e04d4572f26f032273cb3a59f0a6e7a34cb324a025c84d
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/start.json
    sha256: 3a5b29460c3c77b5e70e2b6c5ac54a9568e3006b576c6d86416d1eae7c853522
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-terms-001/native.log
    sha256: 0ddddd2edabc43bf48b79ee72de2bcb83de6a97e1d05a71b591b67dcfde3f1e1
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-terms-001/receipt.json
    sha256: c580c290729a34cf09839b0de15a31d158bc9e4c5ba83def068a16dba89a8d51
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-mapping-terms-001/start.json
    sha256: 6155b67ae93242eb01a8f62282eb8e80b1318b3f88c69828a855d1777011996f
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-note-applied-m5-001/before.yaml
    sha256: c45342937de0702f02ed9029b7580823f25e2a59f9cdb75f83c4de6e9177ff1c
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-note-applied-m5-001/receipt.json
    sha256: 4903fe21bf72e9643302f24a94ec95552af2642772ee7fbf7b4da244c35e0868
    role: context
  - path: .temp/gtdb-source-holds-20261115/bl6346-note-stage-m5-001/receipt.json
    sha256: d4c1669ba592ce8360fcb8b5b548931ceabc0af3adfe878af428e8465c688c41
    role: context
  - path: .temp/gtdb-source-holds-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/phase2-schema-20261115/bl6346-after-note-native-route-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/bl6346-after-note-native-route-001.json
    sha256: 1f95ab63f59ad55c58f5a8dd6e516325a203c6817dc73601512cb496ef82b2e6
    role: context
  - path: .temp/phase2-schema-20261115/bl6346-after-note-native-route-001.log
    sha256: 3eaa5f13908e6c3c6f05643a796622bb19587353d82fc9db83a211dffeb915c3
    role: context
  - path: .temp/phase2-schema-20261115/bl6346-mapping-binder-m5-001.log
    sha256: 552af1f41233cd968d681a898ea0eca23392c03da62fe9294bf74910e50fc2b5
    role: context
  - path: .temp/phase2-schema-20261115/bl6346-native-route-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/bl6346-native-route-001.json
    sha256: 1949cdc3ac39234250f983af20ca62bf29f7bce86cc052f4d599b2402cc5d245
    role: context
  - path: .temp/phase2-schema-20261115/bl6346-native-route-001.log
    sha256: 558634db5eeaf4ee1b31721361c4b76139732128a5a58e9184f6700894a2ac23
    role: context
  - path: history/records/Chicken_BL6_AntiSalmonella_SynCom/2026-09-11T131435Z-codex-423512.yaml
    sha256: 9d18000986aa84025c54b0cfbeb0298f717488467e964a5d7a5af6cf9c9319c0
    role: context
  - path: history/records/Chicken_BL6_AntiSalmonella_SynCom/2026-10-05T184624Z-codex-beb2ba.yaml
    sha256: 6d4b436344b5753846c4baf635da03d4d2cceda5fbe73085ddea0670babcf16d
    role: context
  - path: history/records/Chicken_BL6_AntiSalmonella_SynCom/2026-11-15T104614Z-codex-1f1c12.yaml
    sha256: d85f859e4d6578b226bc59d4d2a06f43890b32361693dfbcfd564f13560a0d08
    role: context
  - path: history/records/Chicken_BL6_AntiSalmonella_SynCom/2026-11-15T114206Z-codex-a3ef11.yaml
    sha256: 5464b1e439c1ad88ed89593ca9545e96ac81ee3007b1a69fc84dbf78b11257e3
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
    sha256: 313ebed02de92edf0ced54c3909c6dc5bcf451782aa264ac1f4ef140e4530658
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42351244.txt
    sha256: c423fe3294e328c8f7b06affbc394b606249e5cf63ba8a5350f433d949b344e3
    role: context
  - path: reports/causal_graph_review/decisions/20261005-four-records-batch11.yaml
    sha256: f8d8ca3b5c79a2d255f82bff689ed3bb726539e781a836aedbeef0cdde6d13c4
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-final-review-config-001.json
    sha256: ab58de3401b45411a732644da4f8daa7b2d6e65acb9d1215f3267d32a1641c4c
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-final-source-evidence-001.json
    sha256: a7b348acd04ecb670aa42a2ef063e824c2443fbb5ab06fd185d1c8f6efce4738
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-mapping-check-config-001.json
    sha256: 133e600b99d5b981aa856666dc61f66a2335648f2ddf68862b71b211093762b3
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-mapping-route-plan-001.json
    sha256: b0281c974fc4d83e091b18e6168049eb4bfb419335a54ba5d0f771073aacba25
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-mapping-source-config-001.json
    sha256: 90324a9f054c3e02275878647adc49e124376f0b84121fd7c9ac41b63d1da6b8
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-note-apply-001.raw.json
    sha256: 4903fe21bf72e9643302f24a94ec95552af2642772ee7fbf7b4da244c35e0868
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-note-check-config-001.json
    sha256: ddb7946a38ef1b245ddeeda3ebce18fb2e84b9a890043da408a5f60f3d630541
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-note-checkpoint-001.json
    sha256: 03cfb152704b63e8ea5a9e2b5c89630a3c76053af3741a36603f650e37a3ab6a
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-note-intermediate-001.md
    sha256: 9eb4eac7ff8ad7d5dfcfd23ef019508c4e82542503a797d71588d526190da0e3
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-note-plan-001.json
    sha256: 013155da7a94e0ec0899e57f113b1ccfa7a9b9ef98db013497fbdcc580c6c277
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-note-stage-001.raw.json
    sha256: d4c1669ba592ce8360fcb8b5b548931ceabc0af3adfe878af428e8465c688c41
    role: context
  - path: reports/gtdb-source-holds-20261115/bl6346-route-plan-001.json
    sha256: af6e6d5edc4aa5d6e45622d61211af81b9e68ce31bc5fe4c9d865b0264f3d1dc
    role: context
  - path: reports/phase2-completion-20261115/pine-bl6-two-source-context-001.yaml
    sha256: e9268260e3a356c65046b7d3741ab0a1cdb4b06a9f6d5e106e09dd03b10c8aeb
    role: context
  - path: reviews/structured/20261021T172345Z-chicken-bl6-record/review.yaml
    sha256: 812eee6da27ced8de7165f573884f2b5dc0a34ac466a5004128991ec88d5bee9
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
  - path: scripts/adhoc/curate_gtdb_source_notes_20261115.py
    sha256: 77ff86d185c6b04634c1bd83531463e42e5ece9f116873bf1d81c7af1de80380
    role: context
  - path: scripts/adhoc/export_m5_technical_evidence_20261114.py
    sha256: a0f43f617e8921443e660d262d28713f40b4c23770b684203c37b65330cc4a5d
    role: context
  - path: scripts/adhoc/gtdb_batch_curation_20261115.py
    sha256: 867e974e9c55325fb1b7e32f81dcf6b7a65b6720941fd303040f5570e46ba232
    role: context
  - path: scripts/adhoc/inspect_gtdb_note_checkpoint_20261115.py
    sha256: b7e0af9dc1834582a16b7cc2dfefb54a1131e706f12b300a6cd75d603089e134
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
  - path: tests/source_note_gtdb_successor.py
    sha256: f343d60ebcb1fb68e2139ff689004aeadd2a5826cbd0e806db809ef25c5d02ef
    role: context
  - path: tests/test_causal_review_batch11.py
    sha256: d8d23becf561096ff16bc2ccf9f0dca1f7502be8940c4c34a046f8bb1cf754c0
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000346
  path: kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
  selector: taxonomy[1].taxon_term.gtdb_grounding_status; taxonomy[1].taxon_term.gtdb_candidates;
    taxonomy[3].taxon_term.gtdb_grounding_status; taxonomy[3].taxon_term.gtdb_candidates;
    taxonomy[4].taxon_term.notes; taxonomy[4].taxon_term.gtdb_classification; taxonomy[4].taxon_term.gtdb_grounding_status;
    taxonomy[5].taxon_term.notes; taxonomy[5].taxon_term.gtdb_classification; taxonomy[5].taxon_term.gtdb_grounding_status
  label: Four descriptor routes with source stock, ANI and population distinctions
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: CommunityMech:000346 taxonomy[4/5] source notes and taxonomy[1/3/4/5]
    GTDB fields, actual two-transition provenance, source stock/genome distinctions
    and eight final-byte native checks. Partial technical and source-provenance assessment,
    not complete scientific review.
  selection: One source-held whole record. Actual note execution3573 changed originalc4534293
    to65f331a4. Real maintained ROOT2139fa42fe538c110f2b91a6e85872e9a30b472b contains
    that intermediate. A separate M5 checkout at849247f9c3bef1ddeb817327f6b777e291207f10
    applied final313ebed0 and ran the eight checks below.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000346
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000346-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never validate kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000346-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
    --out .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000346-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000346-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000346-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000346-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never validate-history history/records/Chicken_BL6_AntiSalmonella_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000346-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Chicken_BL6_AntiSalmonella_SynCom --target-root kb/communities --event EDIT --outcome
    changed --sections taxonomy,curation_history --actor-name codex --model gpt-6
    --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Retain BL6 descriptor ambiguity and add two source-qualified reference
    mappings' --details 'Applied the accepted native ground-and-status transition
    to indices1/3/4/5 after the actual two-note intermediate. Ligilactobacillus salivarius
    and Lactobacillus johnsonii retain all two and three native species-name alternatives;
    no experimental stock option is selected. Exact NCBITaxon47770 and52242 reference
    populations give1123/fraction1.0 and38/fraction0.92 respectively. The corrected
    notes preserve source-reported CMLH109/CMLH110 genome ANI97.91/98.05 percent to
    type-strain references while distinguishing it from independent stock placement
    in GTDB. Crosswalk release remains unestablished. Both existing index0/2 blocks,
    all six stock identities, source quotations, biological content and old history
    remain unchanged. Prior phenotype/abundance, culture-context and evidence-placement
    findings remain outside this diagnostic. Final strict two-transition admission
    uses real maintained ROOT2139fa42fe538c110f2b91a6e85872e9a30b472b; actual note
    execution3573 and final execution8492 are distinct metadata. No whole-record scientific
    approval or corpus QC is claimed. Actual apply receipt .temp/gtdb-source-holds-20261115/bl6346-mapping-applied-m5-001/receipt.json
    sha256:b46444f1e80802f9cf2b55101e9b352da63a39f0b19a20322dcd24f09d10ac4a.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000346-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000346
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Chicken_BL6_AntiSalmonella_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000346-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000346-schema
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-schema-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-strict
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-strict-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-gtdb
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-gtdb-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-domain
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-domain-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-scalars
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-scalars-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-history
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-history-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-new-history
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-new-history-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-terms
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-terms-001/native.log
  accessed_at: '2026-11-15T11:48:11.547303Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000346-primary
  kind: primary_source
  reference: PMID:42351244
  locator: Retained primary Methods genome sequencing, stock roster and Table1 ANI
    comparisons and caption; data availability; exact source metadata primary_locators
  support: supports
  summary: The source identifies all six CMLH stocks and reports CMLH109/CMLH110 genome
    ANI97.91/98.05percent to species type-strain references. This pass does not independently
    verify their study assemblies or equate those references with GTDB stock assignments.
  accessed_at: '2026-11-15T11:48:11.547303Z'
- evidence_id: 000346-native
  kind: database
  reference: reports/gtdb-source-holds-20261115/bl6346-final-source-evidence-001.json
  locator: Selected taxonomy1/3/4/5 full native_result, classify_status, local authority
    and captured source populations
  support: supports
  summary: Native ncbi_name1624 returns salivarius/sp945923665, and ncbi_name33959
    returns johnsonii/sp945980025/sp947171515. Exact47770 gives crispatus1123/fraction1.0
    and exact52242 gallinarum38/fraction0.92. These are descriptor-reference populations;
    pre-application NOT_ATTEMPTED for missing stored blocks did not mean absent database
    correspondence.
  accessed_at: '2026-11-15T11:48:11.547303Z'
- evidence_id: 000346-note-transition
  kind: record_content
  reference: reports/gtdb-source-holds-20261115/bl6346-note-checkpoint-001.json
  locator: Actual note plan/stage/apply/before bytes, native104614Z sidecar and56-input
    checkpoint
  support: supports
  summary: The first actual transition changed exactly notes4/5 and appended one native
    event,c4534293 to65f331a4. Eight note-only checks passed. Real maintained2139
    preserves that intermediate separately from actual execution3573.
  accessed_at: '2026-11-15T11:48:11.547303Z'
- evidence_id: 000346-mapping-transition
  kind: record_content
  reference: .temp/gtdb-source-holds-20261115/bl6346-mapping-applied-m5-001/receipt.json
  locator: Actual applied/before/after/source inputs and independently accepted candidate313ebed0
  support: supports
  summary: 'Native ground-and-status persisted65f331a4 to313ebed0: two complete ambiguity
    sets, two reference blocks and four statuses plus two native events. Corrected
    notes, unselected blocks0/2, all six stock identities, evidence and biology remain
    exact.'
  accessed_at: '2026-11-15T11:48:11.547303Z'
- evidence_id: 000346-prior
  kind: prior_review
  reference: reviews/structured/20261021T172345Z-chicken-bl6-record/review.yaml
  locator: Findings phenotype-abundance, culture-context, evidence-placement and gtdb-completeness;
    immutable batch11 ledger and current caller
  support: context_only
  summary: The current mappings address the narrow prior request to recover two exact-ID
    descriptor blocks, without revising that historical review or closing its other
    three scientific finding groups. Current source and biological predicates remain
    required; strict composite admission follows the complete saved-input checkpoint.
  accessed_at: '2026-11-15T11:48:11.547303Z'
assessments:
- assessment_id: 000346-stock-ani
  area: grounding
  topic: Source-reported study genomes remain distinct from reference mappings
  outcome: supported
  target_ids:
  - CommunityMech:000346
  evidence_ids:
  - 000346-primary
  - 000346-note-transition
  - 000346-native
  - 000346-terms
  summary: Corrected notes preserve the source's WGS and ANI comparisons while avoiding
    independent study-stock GTDB placement. All six stocks, current names, genus-only
    CMLH124 and source-reference distinctions remain unchanged.
- assessment_id: 000346-ambiguity
  area: grounding
  topic: Complete two-way and three-way species-name ambiguity
  outcome: supported
  target_ids:
  - CommunityMech:000346
  evidence_ids:
  - 000346-native
  - 000346-mapping-transition
  - 000346-gtdb
  summary: Indices1/3 retain all two and three native alternatives with AMBIGUOUS
    status. No cluster is selected for CMLH112 or CMLH106, and no unsupported reference
    denominator or stock probability is inferred.
- assessment_id: 000346-exact-reference
  area: grounding
  topic: Two exact species-ID reference blocks
  outcome: supported
  target_ids:
  - CommunityMech:000346
  evidence_ids:
  - 000346-native
  - 000346-mapping-transition
  - 000346-gtdb
  - 000346-domain
  summary: Indices4/5 store crispatus1123/1.0 and gallinarum38/0.92 with native lineages
    and GROUNDED statuses. GROUNDED concerns the encoded descriptor correspondence,
    not a verified experimental assembly. Corrected notes and unselected0/2 blocks
    remain exact.
- assessment_id: 000346-two-transitions
  area: provenance
  topic: Two actual transitions with distinct final-byte checks
  outcome: supported
  target_ids:
  - CommunityMech:000346
  evidence_ids:
  - 000346-note-transition
  - 000346-mapping-transition
  - 000346-prior
  - 000346-schema
  - 000346-strict
  - 000346-scalars
  - 000346-history
  - 000346-new-history
  summary: Both actual application chains and sidecars are captured. Eight final-byte
    native commands passed separately from the note-only checks. Maintained2139 and
    actual8492 have distinct roles. Composite controls, generated products and combined
    QC remain subsequent work; prior biological findings and immutable history are
    preserved.
findings: []
actions: []
limitations:
- Partial diagnostic scientific_review:false. Native validity and reference correspondence
  do not establish whole-record scientific approval, corpus QC, release clearance
  or automatic closure of earlier findings.
- The complete canonical record, retained prior review and selected primary Methods,
  stock roster, genome/ANI Table1 and data-availability passages were inspected. No
  new figure-pixel, supplementary-file, sequence, study-assembly or full-paper review
  was performed. Earlier full-review observations remain historical inputs.
- The paper reports sequencing all six isolates and ANI97.91/98.05 percent for CMLH109/CMLH110
  against species type-strain references. These are source-reported genome comparisons,
  not independently verified GTDB placement of those study assemblies. Data available
  on request is not proof that public assemblies are absent.
- The salivarius1624 and johnsonii33959 native routes use species-name lookup and
  return two and three alternatives respectively. All alternatives remain unselected;
  the source stock names do not resolve them. No ambiguity-route genome denominator,
  identity probability or new nomenclatural assignment is inferred.
- The exact47770 population1123/fraction1.0 and exact52242 population38/fraction0.92
  describe reference populations. Rounded0.92 is not unanimity or a recoverable exact
  numerator. These counts are not six-member inoculum counts, abundance, identity
  probabilities or evidence of stock-specific genome placement.
- The pinned761 crosswalk's upstream release remains unestablished; file mtime does
  not identify a release. Local and M5 NCBI file-stat observations are separate execution
  provenance, not a full database checksum or certified ontology version.
- Keep all six stocks, source-preferred names, CMLH124 genus-level identity and its
  source-reported93.27percent ANI distinction, the two unselected mapping blocks at0/2,
  the one community-level node and zero arrows. Chicken host and Salmonella challenge
  are not community members. Preserving unselected fields does not newly certify their
  biological or mapping claims.
- The prior review's phenotype-abundance, culture-context and evidence-placement findings
  remain outside this correction. In particular, host markers do not establish broader
  barrier/liver function, DOMINANT is not measured strain persistence, isolation recipes
  do not establish final propagation, membership snippets do not by themselves establish
  antagonist roles, and the existing ANI evidence-source tag and historical unread-figure
  wording are unchanged.
- The note-only intermediate had its own eight checks and56-input checkpoint. The
  eight required checks below are distinct actual commands on final mapping bytes,
  with a separate native sidecar. Actual execution3573/8492 is separate from the maintained2139
  intermediate.
- The original batch11 ledger and current biological assertions remain required. Exact
  two-transition composite admission, its mutation controls, generated products, reference-snippet
  validation and combined QC are subsequent work. No general note exemption or rewritten
  historical scientific assessment is introduced.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/pull/2804
```
