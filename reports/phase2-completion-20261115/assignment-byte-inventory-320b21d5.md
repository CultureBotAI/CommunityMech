# Assignment byte inventory at 320b21d5

The pinned historical 126-record assignment ledger was compared with actual
canonical files in working tree `320b21d5a40a5493dd1dd26a74a8a29b5ec0ae54`.
There were **79 changed files and 47 unchanged files**. This is a byte inventory,
not a completed-review count or a new resolver measurement. In particular, the
existing BL6 note-only intermediate is changed but its final mapping was not
yet integrated at this revision. The separate completion ledger therefore
still records 78 completed corrections in this historical partition.

The initial inventory001 remains unchanged under `.temp/phase2-integration-20261115/`.
Independent review found that its helper did not recheck captured bytes or HEAD
before publishing; [issue2897](https://github.com/CultureBotAI/CommunityMech/issues/2897)
records that finding. No actual drift was observed. The corrected
[helper](../../scripts/adhoc/inspect_gtdb_assignment_progress_20261115.py)
captures the ledger and canonical bytes, rechecks every capture and HEAD,
explicitly labels working-tree state, then writes exclusively. It is a
cooperative guard, not a filesystem lock against unrelated writers.

The corrected actual inventory002 reproduced79/47, with SHA-256
`27b19db231c3b6b311765831de7bbbb4f09cbdc09a106ca5560f0cc7a1c12631`.
Its path is `.temp/phase2-integration-20261115/gtdb-assignment-bytes-320b21d5-002.json`;
the helper SHA-256 is `7260a44b96f0c6986889743011e790091727c6b38f6293ab1131d31b3e3323f1`.
Both files were verified nonempty. No canonical data changed in either scan.

The [two refusal/restoration controls](../../tests/test_gtdb_assignment_inventory_snapshot.py)
run an unchanged positive arm, inject a real file write or actual Git commit
during the scan, require the specific refusal with no output, restore the file
or original revision in the isolated synthetic repository, then pass another
positive arm. Run `assignment-inventory-drift-controls-001` passed both cases
in0.81s. Its retained raw log hash is
`e0f99c009e3f0cb266186091c50ea73692ee91d8e6be128e02c71a43032856ce`.
Black and Ruff passed for the helper and controls. These tests exercise inventory
integrity only; they do not establish taxonomy correctness or scientific review.
