# LBNL Switchgrass review receipt and later mapping evidence

The full scientific assessment is saved in
[authoritative YAML](../../reviews/structured/20261114T213343Z-m5-lbnl-switchgrass-completion/review.yaml)
and [rendered Markdown](../../reviews/structured/20261114T213343Z-m5-lbnl-switchgrass-completion/review.md).
Native validation and saving passed; both artifacts are nonempty (50,359 and
75,345 bytes). All seven focused M5 checks passed. The review assesses all three
nodes and zero downstream edges and retains two major findings under existing
[issue1548](https://github.com/CultureBotAI/CommunityMech/issues/1548): the missing
final16 strain representation and pooled non-graph assay scope. The other two
records in that issue remain outside this assessment.

The immutable YAML SHA256 is
`a57f38689acbcc47844d8ccd7545dd06511d5d2cb0f8d487824dd86f569d1a44`;
Markdown SHA256 is
`1d41b5cdb77e277682bb808a1df1cad305533358549a8da42271d4ae226128d6`.
The local post-save corpus check was interrupted with SIGTERM after identifying
its own process; the root coordinator already runs the shared full check and
will report its result. This interruption is not a successful corpus check.

After the review was saved, the newly recovered crosswalk was inspected with
`scripts/adhoc/verify_completion_mapping_20261114.py`. The
[mapping receipt](lbnl-mapping-comparison.json) has SHA256
`0da35ea386597a8b3f6c804ff9732e919ea46f2f9bbda37e4717550ab82d0f92`.
It reproduces the stored domain grounding exactly: NCBITaxon2 maps to
GTDB:d__Bacteria, with 1,603,049 supporting and total genomes and fraction1.0.
The crosswalk SHA256 is
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
the native grounding script SHA256 is
`0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175`.
The comparison uses the native aggregate denominator with unnamed species
excluded. The unchanged canonical input SHA256 is
`58bb996c6056821c2e5bf3d3494108826b3f836c79fc95f0c07db967e65b04e4`.

This later numerical result narrows the saved review's limitation about an
unreconstructed mapping. Its earlier ignore-independent search preceded this
crosswalk recovery. The historical `latest` release and claimed build date are
still not certified. Numerical agreement at domain rank supplies neither the
sixteen individual stock identities nor their functions, so both scientific
findings remain open. No prior review, canonical record, cache or history was
rewritten. This supplement is a technical reproduction receipt, not a second
full scientific review or a terminal disposition of issue1548.

Provenance helpers for the full assessment are
`scripts/adhoc/run_lbnl_review_checks_20261114.py`,
`scripts/adhoc/inspect_lbnl_primary_20261114.py`,
`scripts/adhoc/prepare_lbnl_review_context_20261114.py`, and
`scripts/adhoc/build_lbnl_completion_review_20261114.py`.
