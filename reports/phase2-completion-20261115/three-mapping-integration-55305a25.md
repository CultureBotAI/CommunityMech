# Mangrove, NDC6 and arsenic integration checkpoint

The independently reviewed Mangrove/NDC6 leaf `db8a62242a2aa09bf8c07854e448511a87b5502b`
and arsenic leaf `5e27ca33c19e09b16c2cc44f988fadab02a221e9` are integrated without
conflicts. Their combined revision is `55305a25311905ebe79a673adc665c998d5d9073`.
The source branches remain published in draft PRs 2928 and 2920. No merge to
main is claimed or authorized.

The [Mangrove/NDC6 outcome](../gtdb-lupinus-mangrove-ndc6-20261115/two-record-outcome-001.md)
preserves frozen M5 execution at `90986ee8`, sixteen native checks, a partial
immutable diagnostic, complete 131-file checkpoints on both hosts and 54
verified public artifacts. Four genus correspondences for Mangrove and six
reference correspondences for NDC6 preserve stock identities and all scientific
claims. Mangrove's endpoint/role findings and NDC6's abstract-only source and
assay limits remain explicit.

The [arsenic outcome](../gtdb-remaining-four-20261115/454-outcome-001.md) retains
frozen M5 execution at `bfef6b2a`, eight native checks, a partial immutable
diagnostic, complete 84-file checkpoints on both hosts and 27 verified public
artifacts. One Chelatococcus reference block does not identify the experimental
stock's genome. The cyanobacterial null result, direct carbon-transfer evidence,
two scientific discussions and existing biological graph remain unchanged.

All three diagnostics retain `scientific_review: false`. Their historical
admissions authenticate the original records, applications, source metadata,
native checks, saved reviews and append-only history before admitting only the
bounded taxonomy changes. Current biological predicates remain in force.

These checks ran on the clean combined revision `55305a25`:

| Recorder in `.temp/phase2-schema-20261115/` | Actual result | Raw log SHA256 |
| --- | --- | --- |
| `integration-three-mapping-proofs-001` | 167 passed, 12 warnings, 102.71 s | `458641396efcfefd4ed2e65262237c6ebc6396328ab079ed7597665288360d66` |
| `integration-three-mapping-lint-001` | Black 794 files, Ruff and mypy 52 sources passed | `fabb5b51b5afe4e1e872d137489a3c133362ba6aec627321940f9a2657a63847` |

The composed test run covers both actual-proof registries, batches 64/68/76/120
and participant checks. Separate leaf integrity results were 351 declared-scope
reviews for Mangrove/NDC6 and 349 for the arsenic branch; those counts refer to
their recorded branches and are not whole-corpus scientific approval.

The captured inventory
`.temp/phase2-schema-20261115/assignment-progress-55305a25-001.json` has SHA256
`0d86407089776119e77f5902c898305985dea7bf977d7f3b5a5fd4013fb71a90`.
It reports 111 changed and 15 unchanged records among the historical 126
assignments. This is a byte inventory excluding pending worktrees, not a
completion count. The approved Sorghum and Shrimp lanes continue with one
actual canary each before their remaining records. Earlier eight-input genus
and 40-input ambiguity transfers still await their separate permissions.

The isolated supplement-adoption branch has its own reviewed schema/model,
exact runtime pin and consumer checks. None is included in this integration
yet. Claw PR 1283 and the owned validator draft remain separate; the validator's
full native suite retains an inherited live-network failure reproduced on its
pristine base. The shared-schema PR also retains its current CI setup failure
for investigation. No unresolved check is being relabeled as a pass.

Current generated products, final combined M5 QC, measured references and
scientific-finding dispositions remain required. Later aggregate stages remain
not run. The all-record scientific campaign has not resumed.
