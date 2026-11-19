# Governed SupportingReference adoption checkpoint

The isolated Phase 2 branch adopted the reviewed Claw annotation repair from
published commit `fde0154a8f2d56514a738c4800657348391c2b66`, tracked in
[Claw PR #1219](https://github.com/CultureBotAI/culturebotai-claw/pull/1219) and
[CommunityMech #476](https://github.com/CultureBotAI/CommunityMech/issues/476).
Neither PR has been merged by this session. No other consumer or live checkout
was changed.

The native synchronizer applied exactly its five reviewed paths: the shared
schema, canonical pin, current backlog prompt, record-review guide and merge
admission helper. The last three are existing canonical updates required by the
new pin. The admission change rejects malformed paths before constructing a
set; the documentation changes retain durable session state and publication
rules. No merge helper was executed. Python-model regeneration changed only its
generated timestamp.

The [retained adoption procedure](../../scripts/adhoc/adopt_supporting_reference_schema_20261115.py)
uses explicit RepositorySettings identity checks, LockManager, the native
transactional synchronizer, exclusive before-state backups and a native
post-write check. Review finding #2810 added lock-time checks of both revisions,
cleanliness and the exact plan before dispatch. Three race controls failed
before the repair; all four controls passed afterward. A process ignoring
repository locks is outside the cooperating-writer guarantee.

The actual apply receipt is retained at
`.temp/phase2-integration-20261115/governed-adoption-apply-001/receipt.json`,
SHA-256 `d7e17be004c09386e938c27493aef4d371f4c871fd6d66aaf63302f07f68ff81`.
Shared-schema bytes now have SHA-256
`cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11`, matching
the published canonical manifest. Both original no-write plans remain retained.

## Actual downstream comparisons

The maintained [coverage instrument](../../scripts/reference_assertion_coverage.py)
ran against exact committed CommunityMech revision
`f4590dc775259c75ea1cbf5583ffdc363b028b42`. Acquisition, enrichment, source writes
and supplement fallback were disabled. All captured inputs remained unchanged.

| Native record control | Snippets | Actual comparisons | SupportingReference comparisons | Native exit | Meaning |
|---|---:|---:|---:|---:|---|
| Original 000087 switchgrass record | 14 | 14 | 0 | 0 | Ordinary EvidenceItem control; did not exercise the repaired shared class |
| Achromobacter SL8 isolate baseline | 17 | 17 | 4 | 0 | Three dataset snippets and one discussion snippet were actually compared |

The earlier corpus measurement recorded 13 comparisons and four unannotated
snippets for the unchanged SL8 record. The new control reaches those four
SupportingReference assertions through the native matcher. All 17 matched
cached source text. This is a lexical coverage result, not a scientific verdict.

The SL8 run is retained under
`.temp/phase2-integration-20261115/discussion-canary-002/`:

| Artifact | SHA-256 |
|---|---|
| `receipt.json` | `a69a5ed722eec0e87239f9a09a08b7a559f15faed2ba8e2908131c4e7f83c1e2` |
| `measurement.json` | `4974b9a51519ccc2afbce4d4ba65e9d7173fa60c33ecc0eafbed3f8a7891762f` |
| `measurement.log` | `82ceb8bd8c304893b6c3149e0cfcabfb2cb6614de64918eea2d802126f7ed6e3` |

The first control receipt has SHA-256
`7b6b1174acfccabde23f79b55c50a9cac98b2632564c80d9972372740a5fe00d`.
It remains a valid ordinary-reference control and is not counted as proof of
SupportingReference traversal. Claw separately retains positive, fabricated and
restored native controls for both shared containers, with exits 0/1/0.

This checkpoint does not declare all 522 historical omissions repaired in a
measured corpus, clear source-specific mismatch blockers or complete scientific
review. A new full M5 measurement is required after the final canonical changes.
