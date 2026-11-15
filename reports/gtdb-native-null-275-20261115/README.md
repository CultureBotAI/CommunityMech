# Native-null rumen status correction preparation

Issue [2888](https://github.com/CultureBotAI/CommunityMech/issues/2888) records
the guarded workflow gap for CommunityMech:000275. The existing native resolver
returns no correspondence for the encoded NCBITaxon:971 descriptor, and its
classifier reports `UNRESOLVED` with no candidates. The old three-candidate
ambiguity is not reproduced by that route. No canonical application has occurred.

The reviewed code extension accepts this status-only case only with explicit
null correspondence, `UNRESOLVED`/empty candidates, no existing grounding,
no stored withholding/domain-exclusion status and explicit absence of both
manual exceptions. It rechecks the unchanged native classifier in the offline
staging context. Strict successor proof additionally requires the actual
status-only operation and preserves every unselected descriptor, scientific
field and earlier history event. Existing frozen proofs remain reproducible;
the native resolver and classifier are unchanged.

## Recorded local checks

All commands below ran at `85d582fa0dcbb3faea2f92ca2ebfb7a33e79998e` with
the disclosed working-tree changes. These are guard and proof controls, not
actual M5 curation or full-record scientific approval.

| Run | Result | Raw log SHA-256 |
|---|---|---|
| `native-null275-controls-001` | 33 passed; first null controls plus existing application guards | `6cc638936443e0cad5d7114f5fe9403ab9623e752a491259fd93d926ba9d8716` |
| `native-null275-controls-002` | 17 final null controls passed after fixture repair and two additional controls | `a1f90e8dd79bcff3fdc14a069408c94dc876afe3ffab7fe4939d782d7e01882c` |
| `native-null275-existing-proofs-001` | 64 existing actual proof and rehashed-mutation controls passed | `ef59d658a9b73063b4b01321cecfc19c740ac2b9d98e2c835105b49d0d46d78b` |
| `native-null275-lint-001` | Black753, Ruff and mypy52 passed | `1307548163a70e3088850b3328099113969dfbd932c1234d0aa83a7acb3813e0` |

Each pytest run retained 12 existing dependency warnings. Counts overlap and
are not summed. Independent review recorded the initial short-commit fixture
dependency [under 2888](https://github.com/CultureBotAI/CommunityMech/issues/2888#issuecomment-6893198010).
The test now uses full retained revision
`68699871415fda3c9eebf20382a315f9f3c7b17a`, whose record bytes are identical.
The final delta and passing evidence received a separate read-only review.

## Source and authority boundary

The [accepted primary-source plan](../phase2-completion-20261115/rumen275-source-context-001.yaml)
records abstract-only coverage and preserves the pairwise/model/triple
distinctions, unknown enzyme denominator, absent exact stock identifiers,
current ontology labels and existing scientific findings. The prospective
[source configuration](rumen275-source-config-001.json) selects only taxonomy
index1 and does not permit a synonym-driven ontology rollback.

The fresh unchanged reporter passed as `rumen275-null-support-route-001`,
with a nonempty 12,466-byte report, SHA-256
`559e799029733908dfd530d24debbb37108eeaa0e0bc7ef5662af56b0a2ade9d`.
The first unchanged binder refused the local authority label mismatch before
staging: `rumen275-null-source-bind-001`, exit1, log
`eb51550d62d0d825f8942891f5146e1df3443fe14043a631143d23699a644280`.
This refusal is retained, not credited as a successful source inspection.

The local SQLite row still uses *Selenomonas ruminantium*, parent970. A separate
read-only query on M5 reports *Pseudoselenomonas ruminantium*, parent3713899,
species rank and the earlier name as a synonym; its saved stdout is
`rumen275-m5-ncbi-identity-001.log`, SHA-256
`b714051bb996a446bdec6e0b2e5c1069d3c2d9342752005754feabaee7b6ebc5`.
The [retained SQL](../../scripts/adhoc/inspect_rumen275_ncbi_identity_20261115.sql)
documents the query. Neither database was modified. Current
[LPSN](https://lpsn.dsmz.de/species/pseudoselenomonas-ruminantium) independently
identifies the newer combination and the older homotypic synonym. Differently
cached NCBI browser responses disagree, so they were not used to override the
record or bypass the source guard.

The intended next step is unchanged source binding against M5's current local
authority. Until that succeeds and its exact output is reviewed, native staging
and application remain pending. Then one actual end-to-end M5 canary must pass,
including saved partial YAML/Markdown review, all eight native checks, immutable
input checkpoint and strict historical admission. This preparation supplies
none of those completion claims. Full Phase 2 QC, reference comparisons and
the broader scientific campaign remain separate.
