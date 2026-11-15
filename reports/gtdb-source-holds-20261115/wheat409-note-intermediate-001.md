# Wheat inoculant source-note intermediate

CommunityMech:000409 now distinguishes the primary study's 16S-based FN0603 and
FWP1205 identifications from GTDB reference-population correspondence. Only the
two taxonomy notes and one appended native inline event changed. Both unresolved
statuses, all existing candidate sets, all five stock identities and the other
scientific content remain unchanged. This is a note-only intermediate; the native
mapping transition, immutable partial diagnostic assessment, composite historical
admission and final QC remain pending.

The accepted [source plan](wheat409-note-plan-001.json) binds the retained primary
Methods 2.1 and the fresh whole-record native route. The pinned correspondence
table has no exact NCBITaxon:158836 row; the native name route returns three
descriptor alternatives. The exact NCBITaxon:299767 row supplies a 296-genome
reference population with stored majority fraction 0.95. Neither result establishes
an assembly-grounded classification of the experimental stock, and the table's
GTDB release is not established. Existing treatment, yield, abundance and
supplementary-evidence concerns in [#1952](https://github.com/CultureBotAI/CommunityMech/issues/1952)
remain outside this bounded correction.

The actual isolated M5 application ran at
`c5f0f16de5a5d3292048b68ef1185fd8a5c9da67`. Its preserved
[stage receipt](wheat409-note-stage-001.raw.json) and
[application receipt](wheat409-note-apply-001.raw.json) are byte-identical copies
of the private native artifacts. The original record SHA-256 is
`613f8b97efa732c213fae320935a4f8cafa8cb899718e6c18a7c1f47f9ba0420`;
the applied note-only SHA-256 is
`94c92ec7ce237ef2d9f7646e695fc1ff3e39eb6ef7bcd9241a1059fcaa90768b`.
The new [native sidecar](../../history/records/Wheat_SynCom_SASW01_Drought_Inoculant/2026-11-15T085528Z-codex-60d280.yaml)
links the actual application receipt and hash. The two original sidecars remain
unchanged. The first local stage and timestamp-only M5 stage are both preserved.

All eight native commands passed on the actual M5 intermediate through the
unchanged shared checker: schema, strict, GTDB structure, bacterial domain,
scalars, history creation, history validation and ontology terms. The
[checkpoint metadata](wheat409-note-checkpoint-001.json) preserves each recipe,
revision, execution times, exit and raw receipt/log/exit hashes. The native GTDB
structural check does not establish agreement with the proposed final mapping;
the two stored statuses remain unresolved at this step. No corpus QC, reference
sweep or full-record scientific review was run for this intermediate.

The unchanged [checkpoint inspector](../../scripts/adhoc/inspect_gtdb_note_checkpoint_20261115.py)
ran on the isolated M5 checkout, verified the exact stage/application chain,
reconstructed native event, source anchors and eight completed gate receipts,
and captured and rechecked 54 inputs. Its passing stdout is copied byte-for-byte
to the public checkpoint JSON. Native gates report Python 3.13.2. External Claw
history source hashes and revision are bound by the native history receipt; the
inspector does not claim to reread that external checkout. The completed raw
gate artifacts, original record and actual application evidence are retained on
M5 and mirrored locally; no source bodies are published in this checkpoint.

This note-only commit must be integrated into the maintained branch before the
mapping transition. The final composite will separately bind that real
intermediate Git revision, the original historical record and the original
execution metadata, preserving the unchanged mapping-only engine and all
current batch122 biological predicates.
