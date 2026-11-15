# Terrabacter 2APm3 reference-genus correction

CommunityMech:000532 now preserves its exact NCBI stock identity while recording
an explicitly curated reference-genus correspondence. The primary study names
DSMZ 28514 in Methods; DSMZ BacDive identifies that deposit as 2APm3, and NCBI
Taxonomy 1472881 places the stock under genus 53355, Terrabacter. The old ancestor
37948 assertion was incorrect. The [source proof](terrabacter-source-proof-001.json)
binds the actual article XML, catalogue capture, NCBI XML and retained crosswalk.
Sources: [primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13472149/),
[DSMZ BacDive](https://bacdive.dsmz.de/strain/157986),
[NCBI stock](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1472881).

The exact stock ID/name has no result in the retained crosswalk. A separate
native query for the verified genus reproduces GTDB Terrabacter under
Actinomycetales/Dermatophilaceae, support 12 / total 12 / fraction 1. These are
the native **named-species-filtered reference-genome counts**, not 12 genomes or
strains of 2APm3; 18 raw genus rows were inspected. The curated flag and note
document this supported manual ancestor route. They do not assert a stock
assembly or GTDB species. No GTDB release or build date is inferred from the
crosswalk file timestamp.

Execution used published code `75c079352fbb823d6fefb5ccb5d0e712eea28676` and
Python 3.13.2 in a new isolated M5 checkout. The independently reviewed local
candidate002 and M5 candidate001 differ only in the native inline event
timestamp. One guarded M5 apply persisted the exact reviewed bytes:

| Artifact | SHA256 |
| --- | --- |
| Original record | `81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e` |
| Applied record | `068a38e5be07ab6756b1fe32683c166d8562e8405fae7bc4429575a33e2578ec` |
| [Actual application receipt](terrabacter-apply-001.raw.json) | `1de5702ca3382b2d6cc5b84552abf169280a17dbb646a420bd2ed6ae340b8f03` |
| [Post-apply native recomputation](terrabacter-native-recomputation-001.json) | `2f5db2759aef9d3f01bfe2e0b25e7d506ba3c10580b8fa46586aa3ad11e50cc2` |

Only the GTDB block and one appended inline event changed. All other scientific
content, the exact stock label and quotations remain unchanged. Native
`just new-history` created one sidecar; both existing sidecar hashes remained
unchanged. The actual M5 canonical bytes, new sidecar and immutable review were
then mirrored locally, without a second curation application.

| Native check | Result | Receipt |
| --- | --- | --- |
| Schema | exit 0 | [receipt](terrabacter-schema-001.receipt.json) |
| Strict | exit 0 | [receipt](terrabacter-strict-001.receipt.json) |
| GTDB coherence | exit 0 | [receipt](terrabacter-gtdb-001.receipt.json) |
| GTDB/NCBI domain | exit 0 | [receipt](terrabacter-domain-001.receipt.json) |
| YAML scalars | exit 0 | [receipt](terrabacter-scalars-001.receipt.json) |
| Complete target history directory | exit 0 | [receipt](terrabacter-history-001.receipt.json) |
| Native sidecar creation | exit 0 | [receipt](terrabacter-new-history-001.receipt.json) |

Every receipt has adjacent `.log.txt` and `.exit.txt` artifacts. Public derivatives
sanitize private paths and retain raw hashes; raw metadata proofs are byte-identical
to their saved review inputs. The native GTDB gate alone does not prove a curated
manual mapping: the independent post-apply genus recomputation provides that
bounded check here. Original raw evidence remains on M5 and in the verified local
mirror. No paper bodies or ontology databases are published.

The scoped diagnostic is saved as
[native YAML](../../reviews/structured/20261115T053046Z-terrabacter-gtdb-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T053046Z-terrabacter-gtdb-diagnostic/review.md).
YAML: 27,156 bytes, SHA256 `0bf6ed4a8d533e77b3ea7140ac530bc7bec062951f999f45761c069a64a8cf1e`.
Markdown: 36,915 bytes, SHA256 `96f91171a3a7325508649dedda461dc34d2ebb8da12c7dc5976f9c0862443503`.
Both M5 and local persistence audits verified 56/56 input hashes and exact native
Markdown. The assessment remains partial, `scientific_review: false`, and
`pass_with_limitations`; it does not certify the complete biological record.

The [one-record successor proof](terrabacter-successor-001.json) binds the actual
application, native diagnostic, sidecar and recomputation to the immutable
batch144 baseline. Thirteen focused successor/guard controls passed, including
changed biological prose/graph/stock identity, rewritten history, rehashed
unreviewed receipts/sidecars/recomputation, missing provenance, altered Markdown
and a source mutation during validation followed by a restored positive control.
The original batch144 module's exact-hash assertion failed on this corrected
Terrabacter record before successor integration (one failure, one pass).
The [combined BR1/Terrabacter proof](batch144-successors-001.json) verifies both
actual chains against their unchanged historical records. BR1 alone replaces
one exact obsolete GTDB identifier in its opening description; all other
biological fields and the original ledger remain equal. Its separate
[source-backed canary](../br1-source-review-20261115/canary-outcome.md) retains
its own execution revision, eight native checks and scoped assessment.
The full batch144 module, both mapping/provenance controls, both writer guards,
both export snapshot controls and writer inventory passed together: 51 tests,
12 existing Pydantic warnings, 26.84 seconds. Actual BR1 source-proof, native
route, raw receipt and description mutations all fail before restored positives
pass. The retained combined log is
`.temp/gtdb-source-routes-2849-20261115/batch144-combined-controls-001.log`,
SHA256 `0dc5d9c3a13e0176875e47aa16297999c2ad17555d9003829889642abd578608`.

The initial public001 export preceded the captured-byte publication repair in
[issue 2860](https://github.com/CultureBotAI/CommunityMech/issues/2860).
Its artifacts were not rewritten. The corrected exporter captured each review
input once, then separately [verified all 24 existing public artifacts](terrabacter-export-verification-002.json)
with unchanged bytes and modification times. The new attestation explicitly
does not claim the earlier exporter used the fix. Actual old-helper controls
failed to reject three mid-preparation mutations; the corrected implementation
rejects canonical, review and native-exit mutations and passes restored controls.

Generated-page integration and a separate native whole-corpus uncurated-mapping
check remain later steps at this checkpoint. No whole-corpus or docs pass is
claimed here.

Subsequent checkpoint: the unchanged native
[whole-corpus stored-mapping module passed on M5](CORPUS-CHECK.md) after both
BR1 and Terrabacter were integrated. Generated-page integration remains separate.

This work addresses the Terrabacter discrepancy in
[issue 2849](https://github.com/CultureBotAI/CommunityMech/issues/2849).
References, ontology labels, full corpus QC and all remaining scientific concerns
are outside this diagnostic. The historical batch144 ledger and its biological
assertions have not been rewritten.
