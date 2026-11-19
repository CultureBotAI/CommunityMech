# GTDB source-route correction canary — 15 November 2026

One Sulfobacillus mapping in CommunityMech:000035 was corrected on an isolated
M5 checkout. This is the first of three stored-block discrepancies in
[issue 2849](https://github.com/CultureBotAI/CommunityMech/issues/2849).
The other two records have not been changed by this canary.

The retained crosswalk has no NCBITaxon:53633 row. Its two exact species-name
rows, NCBI679936 and 1051632, each report two genomes, fraction 1.0 and
Sulfobacillus_A acidophilus. The native classifier reproduces that correspondence
with total 4 and fraction 1.0. The source NCBI identifier and species name remain
unchanged. The correction removes unsupported latest/build wording and adds no
curated exemption. It does not identify the study's exact strain or resolve the
composite community, biological claims or graph concerns in
[issue 1509](https://github.com/CultureBotAI/CommunityMech/issues/1509).

The public [source-route proof](sulfobacillus-route-001.json) binds the original
record and the retained crosswalk SHA256
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
This hash identifies the inspected bytes; no GTDB release is inferred from a
file modification time. The primary 2014 paper was checked at abstract scope;
the mapping is a database assertion, not a result from that experiment.

Execution used published code `cb642708f04b12d3a30ecdb662854dd26816014c`
and Python 3.13.2 on M5. Independently reviewed local candidate002 and M5
candidate001 differ only in the native inline event timestamp. The exact
reviewed M5 candidate was applied once, through the guarded native writer:

| Artifact | SHA256 |
| --- | --- |
| Original record | `71160959bae2c8e3f0caf63d57452a597e29967f70faea6bec59016752b9aad4` |
| Applied record | `24c55ff3c29b21fa5988c4859fdcccfacc52caf62a1902cb28887b68780f551e` |
| [Actual raw application receipt](sulfobacillus-apply-001.raw.json) | `ee8f6aec6f076b02c80539d3d47fc1a694274d6de97ca68145131910add33066` |
| [Native post-apply recomputation](sulfobacillus-native-recomputation-001.json) | `7d4df488bd3badfd2c3a847e3abc0ae9ab4639881e061c78b408e829992e9f93` |

Only the reviewed GTDB block and one appended inline event changed. Native
`just new-history` created one nonempty append-only sidecar; the old sidecar's
hash remained unchanged. The native history scaffolder's actual source revision
was `23899092a4a2aedf53ff4435c0bdc03ebd79e6be`, with module hashes retained in
the private command receipt. Canonical bytes, sidecar and saved review were
subsequently mirrored locally; this was not a second curation application.

All six native focused checks passed against the corrected M5 bytes:

| Check | Result | Public receipt |
| --- | --- | --- |
| Schema | exit0 | [receipt](sulfobacillus-schema-001.receipt.json) |
| Strict | exit0 | [receipt](sulfobacillus-strict-001.receipt.json) |
| GTDB coherence | exit0 | [receipt](sulfobacillus-gtdb-001.receipt.json) |
| GTDB/NCBI domain | exit0 | [receipt](sulfobacillus-domain-001.receipt.json) |
| YAML scalars | exit0 | [receipt](sulfobacillus-scalars-001.receipt.json) |
| History directory | exit0 | [receipt](sulfobacillus-history-001.receipt.json) |

The [native history creation receipt](sulfobacillus-new-history-001.receipt.json)
also records exit0. Each receipt has an adjacent `.log.txt` and `.exit.txt`;
public derivatives remove private paths and preserve original log/receipt
hashes. The original M5 evidence and verified local copies remain under the
ignored repository work directory. No paper bodies or ontology databases are
published here.

The independently reviewed diagnostic was saved using the native immutable
review writer: [YAML](../../reviews/structured/20261115T050549Z-sulfobacillus-gtdb-diagnostic/review.yaml),
[Markdown](../../reviews/structured/20261115T050549Z-sulfobacillus-gtdb-diagnostic/review.md).
The saved YAML is 24,658 bytes/SHA256 `c2179cce51f334bdf950d1acfc63afeb8cc657f7ae89ecef9d0529bed43ef833`;
Markdown is 33,354 bytes/SHA256 `bcef3fad12e6dc4b93ad52e0d428eaa3dde6012948eb0f64ac91df944bfeb58e`.
The persistence audit verified 53/53 input hashes and exact native Markdown.
Its scope is partial, `scientific_review: false`, with verdict
`pass_with_limitations`. It does not clear previous scientific findings.

The [successor proof](sulfobacillus-successor-001.json) connects the actual
application and diagnostic to the immutable batch53 baseline already fetched by
CI. Existing graph assertions remain in place. The bridge additionally checks
unchanged scientific content outside this one mapping, append-only history,
review-bound raw application and sidecar hashes, native recomputation, and exact
derived Markdown. Other records retain the original exact-hash requirement.

The original batch53 hash assertion failed on the actual corrected record
before the bridge was wired. Afterward, 27 tests passed across the complete
batch53 module, successor controls, guarded writer controls and writer inventory
(12 existing Pydantic deprecation warnings). Negative controls reject changed
graph/scientific content, rewritten old history, another mapping, rehashed
unreviewed receipts/sidecars/recomputation, mismatched Markdown, wrong review
scope and use of this exception for another record. The retained combined log
is `.temp/gtdb-source-routes-2849-20261115/sulfobacillus-combined-controls-001.log`,
SHA256 `96a3b35b6f1f1dfdb63d0ddbd88b2793ae5d22da16142b17171f45f7787f1f18`.
The native renderer regenerated the one record page successfully; its tracked
HTML bytes were unchanged. That one-page render is not the corpus docs gate.

References, ontology labels, full corpus QC and the corpus-wide generated-docs
gate are not claimed passed by this diagnostic. The NCBITaxon label and all
source quotations are unchanged. Later integration checks remain separate from
this bounded M5 canary.

The subsequent independently reviewed [Terrabacter 2APm3 canary](TERRABACTER.md)
has its own source proof, actual M5 application, native checks and immutable
diagnostic. Its evidence does not change the scope or status of this earlier
Sulfobacillus assessment.

After all three corrections were integrated, the unchanged native
[whole-corpus stored-mapping module passed on M5](CORPUS-CHECK.md).
That follow-up does not clear the separate grounding-status or scientific backlog.
