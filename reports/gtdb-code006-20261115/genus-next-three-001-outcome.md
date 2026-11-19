# Three additional genus-reference corrections

Six selected taxonomy occurrences in records000372,000349 and000424 now have
source-compatible native genus-reference correspondences and grounding statuses.
Only those fields and six appended native inline events changed. This is a partial
technical diagnostic with `scientific_review:false`; prior scientific findings,
unselected mappings/candidates, source text and biological assertions remain intact.

| Record | Bounded correspondence | Preserved limitation | Immutable proof |
|---|---|---|---|
|000372, nitrogen-removal consortium|Klebsiella44527/44529; Alcaligenes36/36|Rounded Klebsiella1.0 is not unanimity; unknown stocks, Stutzerimonas/Pseudomonas alternatives, nitrogen endpoints and mechanisms stay qualified.|[372 successor](genus-next-three-372-001-successor.json)|
|000349, GAC-dependent enrichment|Methanosarcina301/301; Lentimicrobium3/3; Desulforhopalus6/6|Reference populations do not identify study MAG assemblies; study R214 provenance differs from this crosswalk; proposed auxiliary/electron-transfer roles remain qualified.|[349 successor](genus-next-three-349-001-successor.json)|
|000424, QY2S1|Dehalogenimonas17/17|No species/assembly or intermember-transfer inference; Clostridium alternatives, c13s5 remediation and supplementary-reference issues remain intact.|[424 successor](genus-next-three-424-001-successor.json)|

The route report ran locally at`1d5bfe5ad58c0321fa988646d049cc810ba292b2`;
source binding and staging ran at`295c7d2b13fcd26ff8ab17c44ab43d2c20d94440`.
Actual guarded writes, eight native commands per record and native review save
ran on the isolated M5 checkout at`23d84a2d5567559a9693303c3ac9c07ff498e037`
with Python3.13.2. Local proof tests used Python3.13.12 at`0e826fcf2f90cda930a39bb108f1c508f1922015`
plus the recorded working-tree diff. These were not clean-tree post-application runs.
The crosswalk SHA remains`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
its file mtime does not identify a GTDB release.

The first372 unit completed its actual write, schema/strict/GTDB/domain/scalar/
history/term checks and append-only history scaffold before349 and424 followed
serially through the same launcher and environment. All24 commands exited0;
each strict TSV persisted as a34-byte header-only file. The actual canonical
and sidecar hashes were checked. Term validation reports “Validation passed”
without an assertion denominator. These commands do not include source-snippet
validation, page generation or final corpus QC.

The immutable [native YAML](../../reviews/structured/20261115T080026Z-nitrogen-gac-qy2s1-genus-reference-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T080026Z-nitrogen-gac-qy2s1-genus-reference-diagnostic/review.md)
contain nine assessments and the24 command bindings. Native validation, exact
Markdown derivation and all172 captured inputs (60,369,478 bytes) passed on both
machines and in the parent's independent audit. The retained source scope is
abstract-only for372 and selected main-text passages for349/424; no new full-paper,
supplement, figure or assembly audit is claimed.

Before historical caller changes, complete174-file checkpoints (60,536,989 bytes,
including the saved pair) were created and verified. Both namespaces are now
present on both machines, with reciprocal verification:

| Private checkpoint manifest | SHA256 |
|---|---|
|`.temp/gtdb-code006-20261115/genus-next-three-input-checkpoint-local-001/manifest.json`|`8adb3b8523a7ef3341c58b3dc7ba3ad4d5e5af84a546e279e3b4e85159049b74`|
|`.temp/gtdb-code006-20261115/genus-next-three-input-checkpoint-m5-001/manifest.json`|`73512f582b64d447ddf6068a476ff55a39ccf8ddc32e1149e06adcd9e66b1604`|

The unchanged shared exporter produced81 public metadata/log/exit artifacts;
all returned SHA256 values were checked against persisted bytes. Public receipts
retain exact raw input digests and distinguish any derived log transformation.
Raw private evidence remains preserved. The saved pair hashes are
`c11e29429520992a483cf42ce6523704983860e9bf7fe8e489d7b9022c1ae3a4`
(YAML) and`1489e7728a747d3a90e7ef95a65c44ea60d3d5698fed04574b3d044f31655c74`
(Markdown).

The explicit genus registry admits only the exact public proofs. Batch89 and92
retain all current biological predicates and old ledgers, projecting the admitted
predecessor only for historical hash/last-event assertions. The331 and c13s5
chains remain intact. Batch8 is unchanged;349 is checked through its explicit
registry and the complete shared actual-proof controls.

| Verification | Result | Retained log SHA256 |
|---|---|---|
|Actual372 positive/tampering/registry canary|17 passed,12 warnings;17.29s|`583743c44c3656f0eac185b6a7642b49cf04b1292768749c95ecc05a47cb518a`|
|Actual349/424 controls after canary|34 passed,12 warnings;34.35s|`8474a746a5732f3d62845f86197daff1f1e1920e13d5cc350a0673a322d1b299`|
|Historical89/92/8 restoration|27 passed,12 warnings;6.84s|`f2b51d110936900d0cb145ce6908d6a9f4835e13a5d4c6a1e45e1ea941b89f67`|
|Native lint|Black675 files, Ruff and mypy52 sources passed|`9a97bb8cb5227fa9b2688478f631612583c3d6f1d5143b73a97e32ff490e529c`|

Raw triplets use `.temp/phase2-schema-20261115/genus-next-three-` with suffixes
`actual-372-canary-001`, `actual-remainder-001`, `historical-after-001` and
`lint-001`. The prior `historical-before-001` remains a real5-failure/22-pass
run: four old hash/history assertions plus one absent historical Git object.
The exact CI-listed object`5fb1fb3d8fa26c4f424be17f7a380e3f9c0eaee6` was fetched
and verified under`historical-prerequisite-001`; no baseline or source assertion
was waived. The12 warnings are existing Pydantic deprecations.

This checkpoint advances the bounded repairs owned by[2848](https://github.com/CultureBotAI/CommunityMech/issues/2848).
It neither closes scientific issues nor resolves[1996](https://github.com/CultureBotAI/CommunityMech/issues/1996).
Generated pages and composed integration checks are recorded separately by the
integration owner.
