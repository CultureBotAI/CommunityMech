# Three-record native evidence checkpoint

Records 389, 381 and 482 have accepted M5 applications, all 24 native checks,
one independently reviewed and saved partial diagnostic, complete input
checkpoints on both hosts, and 81 verified public proof artifacts. This is a
durable stopping point for the separate Intel handoff. **Strict registry/caller
adaptations and their tests are NOT RUN. Do not integrate this checkpoint into
the maintained branch yet.** The completed 441 proof remains separate.

The changes cover 31 selected descriptor occurrences: 29 reference blocks,
complete five-option Megasphaera and ten-option Stutzerimonas lists, 31 statuses
and six native inline events. Record 389 retains its separate SILVA bins and
substrate enrichment lines. Record 381 retains all fifteen bacterial stocks,
the separate algal member and unresolved B12 findings. Record 482 is expressly
term-only: Rhodanobacter 15/15 does not settle the four-stock membership hold,
NMC performance attribution or issues 2404–2406. No whole-record scientific
clearance follows from these technical checks.

Actual staging, application, gates, diagnostic build and native save used the
named M5 branch `review/gtdb-genus-last-four-20261115` at frozen
`308081a8cf3f82472c542db87e135a5b96da61be`, Python 3.13.2 and Claw
`23899092a4a2aedf53ff4435c0bdc03ebd79e6be`. These are working-tree executions
containing the accepted applied records. Local mirroring, audits and public
export used the same repository path at publication predecessor
`4f46bb640e0a5ceec646df90527bdfa881a20e12`, Python 3.13.12. No source,
crosswalk, shared engine, checker, builder, exporter or test implementation was
changed for this checkpoint.

The existing [remaining-input transfer report](remaining-binding-transfer-001.md)
retains the nine metadata transfers, exact existing M5 supplement reuse and
earlier sandbox DNS failure. A later read-only check-config verification also
failed safely with sandbox DNS resolution (recorder
`genus-last-four-381-482-check-config-m5-verify-001`, exit 255, raw SHA256
`44166c803ed367c797668ee1b6b5ee10f3289a1649c17322a1a135468df7b20f`).
The same read-only command through normal network authorization succeeded in
`002`, raw `c0e5b2baa93c732bb34ee00ce48ddf38a4b1b06bd4a0e4449f48282f0b9e2184`.
This was not a native validation failure or a waived transfer rejection.

Each unit completed its eight free plans before actual execution. Record 389
ran serially; 381 and 482 used independent per-record input sets, outputs and
history directories, with serial checks within each record. Both actual schema
outputs were verified before their remaining checks. Every actual gate passed
at the frozen revision with unchanged captured inputs; strict validation scanned
one file with zero errors per record. Terms reported `Validation passed` without
an assertion denominator. Fresh M5 rehashes of every captured gate input,
including external Claw files, passed. The independent peer read every actual
log and receipt before the diagnostic builder ran.

The saved native bundle is
[`20261116T024711Z-rumen-prymnesium-black-soil-reference-diagnostic`](../../reviews/structured/20261116T024711Z-rumen-prymnesium-black-soil-reference-diagnostic/review.yaml).
It has nine assessments, 24 checks, 38 evidence entries, partial coverage and
`scientific_review: false`. Its YAML SHA256 is
`b186628bcc4944dc16c077734212a73f0e70da546b92d27eecefc51fecd9a208`; its
Markdown SHA256 is
`35684b9575193db3707e90fe5df6f9ce911dc1948a315dcb4e36b296c96b8602`.
Actual draft `b5090c3f347b5b1e888609d2693ec29464776e40ef6699e8b668cea415f6776f`
and inspection `4a5b65420d2da87c2e526502a8a2ca8c4fffa47c3ddeecb3c600a8aa1c7ea08e`
remain in the private `remaining-three-review-draft-001` directory.

Both native saved-pair audits verified all 179 inputs / 13,313,207 bytes,
native schema validity, exact native Markdown and unchanged captured inputs.
The complete snapshot on each host is
`.temp/gtdb-genus-last-four-20261115/remaining-three-input-checkpoint-001`:
181 files / 13,500,609 bytes. The local manifest is
`dbe1a4fa16650ba3dff75379c2507a77bcbcb9260878473c642fa18f0b37e103`;
the M5 manifest is
`bca9957755c7ce99615cb59a3b6d73d48603cc7e4b9e571d11d3af0ace7c6ec4`.
Both standalone verifiers passed. The independent peer also ran its own native
pair audit and complete local checkpoint verification; see the
[independent handoff](independent-review-handoff-001.md).

The exact export config is
`7a97b9a179664268dcfc213f525681ff7947bb6e857ff8e9cc1e1ebb49a0872b`.
The unchanged exporter first planned, then persisted 81 exclusive artifacts.
Plan and actual stdout are byte-identical, and every exported file rehashes
against that output. Fixed manifests are:

| Record | Manifest SHA256 |
|---|---|
| 389 | `c33fe6ab2fdad1cecf9c6d2a0f7377eb1970c1885168a18ef77274bae6fa874a` |
| 381 | `234e7fe2da9f1a4184bb4973cc6d97ca46f91e76d125bdf8f53687046ed2ba57` |
| 482 | `bb7a3a36f57ee59d76085649f579d235ea385d5c5e9f1ae7241ea02944c7d6e6` |

The following raw logs live under `.temp/phase2-schema-20261115/`, each with
its finalized JSON receipt and `.exit` file. All listed completed commands
returned 0; the raw M5 receipts, rather than local SSH wrapper metadata, bind
the actual native execution.

| Recorder prefix | Raw log SHA256 |
|---|---|
| `genus-last-four-three-build-m5-001` | `6bcf9266d08b39fea073820f0efe3b23461a7b879f0722308b68b793737bf476` |
| `genus-last-four-three-save-m5-001` | `e130e5294ad22e18294f84dc5ff301ce005ae7c3d5ab136c91e3d60875558499` |
| `genus-last-four-three-saved-audit-m5-001` and `-local-001` | `db7c10fcb8eac424a8107f095a17a93a2c7c9d7dc3272bfa65070ecb2cb551c9` |
| `genus-last-four-three-checkpoint-verify-local-001` | `3897e0372169799b9b8af0d00ae49c9b4686e91aa1e0ba6eb67bb38a9b8417d7` |
| `genus-last-four-three-checkpoint-verify-m5-001` | `c2be6e0892d472942dee21562baa731b85054c47d154d9c1fcd4fdbded5bba53` |
| `genus-last-four-three-export-plan-001` and `-actual-001` | `ecdbbe97e915c85ad4d6225aee282e949b09e2ff03cbb5ee04855336cb76cec7` |
| `genus-last-four-three-export-hashes-001` | `ca139e68602cbb9896d78a4afe116886cdbf83ba0ceedacbdaa11bc72b6ffd39` |

No registry entry or historical caller has been modified for these three
records. The actual-proof mutation controls, affected caller/participant
matrix, final lint, declared-scope corpus review check and integration remain
**NOT RUN** for this new checkpoint. Earlier 441 test results do not cover them.
This publication is draft evidence preservation, not a merge recommendation or
a claim that the three records are admitted by current production tests.
The exact remaining work and frozen execution paths are in
[continuation-001.md](continuation-001.md).
