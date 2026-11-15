"""Explicit completed note-plus-mapping admissions; no inferred targets (#2869).

2026-11-15: immutable original and real ROOT intermediate bytes are both required.
The exact composite delegates its final leg to the unchanged mapping-only core.
"""

from source_note_gtdb_successor import admit

TARGET = "kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml"
BEFORE = {TARGET: "2003158329c3f2113f6239f65b1e6a1b85bd3c19204f7aaf9d90be7f1f5c68f0"}
ALLOWANCES = {
    TARGET: {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-source-holds-20261115/paenibacillus-composite-successor-001.json",
            "sha256": "0e62d5ee554abde28a513814ada7e9e35330941bcc8fbc83a9cce318340a6f95",
        },
    }
}


def admit_note_mapping_successor(root, path, predecessor_sha256, *, current=None):
    return admit(root, path, predecessor_sha256, ALLOWANCES, current=current)
