# PES two-genus correspondence canary

CommunityMech:000340 now records the native genus-reference correspondences
for Pelagerythrobacter N7 (16/16 filtered reference genomes) and Salinicola A11
(46/46). The existing stock names, genus terms, scientific content and old
history are unchanged. These denominators describe database reference
populations, not sequenced study stocks or exact species assignments.

The actual guarded application and eight scoped commands ran on M5 with
Python 3.13.2 at `23d84a2d5567559a9693303c3ac9c07ff498e037`. Source binding
and candidate staging ran locally with Python 3.13.12; the native route report
retains its earlier `52c740b6` revision. The canonical SHA changed from
`c3ce655c53db89daeab6cf8ee8ca02ab7eb3bf597d6fe0dd7171ba33194dde1a` to
`fd80ffd72ba9e2e1909a4d1f165d642af2dda9e5f04e91128a63a7903fef27b8`.
The mapping file SHA is
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
its recorded mtime is not a database release.

The [public successor proof](pes-001-successor.json), SHA
`b44e7040e1bdeacedc63cdb8f45ab4546c30327e357e8c58a0758acfa790c47f`,
binds the actual application receipt, source evidence, native history sidecar,
saved diagnostic and eight check triplets. All eight commands exited zero:
schema, strict, GTDB coherence, GTDB domain, scalar checks, native history
creation, history validation and ontology terms. Strict output contains a
34-byte header and zero error rows. Terms reported “Validation passed” without
an assertion denominator. The publisher persisted 27 artifacts and verified
the saved review's 77 input hashes and exact native Markdown.

The immutable [partial diagnostic](../../reviews/structured/20261115T070439Z-pes-two-genus-reference-diagnostic/review.yaml)
has YAML SHA `046b1ecb9ea249cf79b30c182911fe3c9e20725fee7dd2fc94491d67e94954d9`
and [Markdown](../../reviews/structured/20261115T070439Z-pes-two-genus-reference-diagnostic/review.md)
SHA `74af25d182b52f64c793523f0ea8b7438b0159a85a98f5a9f43450cc215a31f1`.
Independent local and M5 audits verified all 77 inputs (4,920,982 bytes),
native validation, exact rendered Markdown and unchanged captured bytes.
Complete private checkpoints preserve 79 files (4,990,803 bytes) on each
machine, including the saved pair:

| Checkpoint | Repository-relative location | Manifest SHA-256 |
| --- | --- | --- |
| Local | `.temp/gtdb-code006-20261115/pes-input-checkpoint-local-001/manifest.json` | `1b964cf1c63c932dfb8a4cca5878d65e56698666a2445355292aa724c0d6f2aa` |
| M5 | `.temp/gtdb-code006-20261115/pes-input-checkpoint-m5-001/manifest.json` | `50f52755ee2489b0640f3e8e30454169fc0ee2533a1e8f8c5fe2a9ead96778dd` |

Those checkpoints retain the assessed batch83 caller bytes before the caller
was extended to admit this exact successor. Current biological assertions and
the separate 000052 remediation remain intact. The original historical caller
failed at its old last-event assertion; its new strict proof admission and the
actual 554/340 mutation/restoration controls passed with the population guards:
82 tests, 12 pre-existing deprecation warnings. The retained test log is
`.temp/phase2-schema-20261115/pes-actual-successor-controls-001.log`, SHA
`cf903a530b15c62ef6d525b19d7fcc5554f2ce22b3a904811c156bdd0b0ae432`.

This is a scoped technical assessment with `scientific_review: false`.
The hphtC-5 assignment, metabolite handoff, emulsifier contribution and
reciprocal-fitness questions retain their prior qualifications. Removal is
not promoted to mineralization. Source-snippet validation, generated-page
integration and final corpus QC are separate; this canary does not close
[the taxonomy repair issue](https://github.com/CultureBotAI/CommunityMech/issues/2848)
or replace the old scientific review.
