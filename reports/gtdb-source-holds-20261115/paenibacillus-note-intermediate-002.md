# Paenibacillus source-note intermediate

CommunityMech:000393 now distinguishes the pinned native `ncbi_name` correspondence,
the verified R226 GTDB-name population, and the separate R226 NCBI-defined population.
The experimental isolate's GTDB species remains unresolved. This checkpoint changes
only `taxonomy[2].taxon_term.notes` and appends one native inline event and one sidecar.
All five existing GTDB alternatives remain unchanged. The subsequent mapping change,
immutable partial diagnostic assessment, composite historical admission and final QC
are pending; this is not a completed record or scientific review.

The accepted [source plan](paenibacillus-note-plan-002.json) binds the primary cache,
the three distinct source-population reports and the [additive R226 verification](../gtdb-ambiguity-20261115/r226-retained-verification-001.json).
The native correspondence has no exact NCBITaxon:1406 row and resolves by name to
three alternatives. The separate R226 name query has 193 genomes in five bins;
the R226 NCBI correspondence has 128 genomes across six taxa. Neither population
assigns the experimental root isolate to a GTDB species.

The actual isolated M5 application ran at `ce4c9361ab22a5af0893f61feedb66d81b3a166e`.
Its preserved [stage receipt](paenibacillus-note-stage-002.raw.json) and
[application receipt](paenibacillus-note-apply-002.raw.json) are byte-identical copies
of the private native artifacts. The original record SHA-256 is
`2003158329c3f2113f6239f65b1e6a1b85bd3c19204f7aaf9d90be7f1f5c68f0`;
the applied note-only SHA-256 is
`9be68fed356b0d26be6773c51a71de5b519886945b44aae641fc7ff3471e30d4`.
The new [native sidecar](../../history/records/Calcium_Tomato_Bacterial_Wilt_SynCom/2026-11-15T081105Z-codex-81603f.yaml)
links the actual raw application receipt and hash; the three original sidecars are
unchanged.

All eight native commands passed through the unchanged shared checker: schema,
strict, GTDB structure, bacterial domain, scalars, history creation, history
validation and ontology terms. The [checkpoint metadata](paenibacillus-note-checkpoint-002.json)
retains each command's recipe, revision, times, exit and raw receipt/log/exit hashes.
These gates do not establish exact agreement with the native candidate set; the
known five-versus-three mismatch remains until the next transition. No corpus QC,
reference-validation sweep or full scientific review was run for this intermediate.

The [read-only checkpoint inspector](../../scripts/adhoc/inspect_gtdb_note_checkpoint_20261115.py)
verified the exact stage/application chain, native event reconstruction, source
anchors, eight gate receipts and local copies of their checkout inputs. Its actual
passing output is copied verbatim to the public metadata above (SHA-256
`ec073d5aaab44e8fcc6104fff2d7ab20dc9000b6e337f8b489e6add9f568c9b2`).
It captured 53 local files and rechecked them before emitting output. The external
Claw history source remains bound by the native receipt; the local inspector does
not claim to have reread that external checkout. Native M5 receipts report Python
3.13.2; the local inspection is a separate execution.

The first local inspection refused a prototype field-name mismatch (`after_sha256`
versus the stage receipt's `candidate_sha256`); its original helper, log and exit
remain private. The corrected reader passed. An earlier validate-history launch
also correctly refused an already-used outer launcher name before execution;
the successful command used a distinct name, preserving the prior history receipt.
The first local stage and actual M5 stage are both retained.

The note-only source commit must be integrated into the maintained branch before
the mapping transition. The strict composite will bind that real intermediate
Git revision and the original historical record separately from execution metadata,
as required by [#2874](https://github.com/CultureBotAI/CommunityMech/issues/2874).
The later immutable assessment will bind both actual transitions and sidecars.
