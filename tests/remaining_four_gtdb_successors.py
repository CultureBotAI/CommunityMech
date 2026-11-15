"""Exact remaining-four reference proofs, #2848, 2026-11-15.

Only independently reviewed, persisted units enter this registry. The unchanged
shared core preserves all other biology and history; scientific findings remain.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
Q5_PATH = "data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml"
BEFORE = {
    Q5_PATH: "3be922d81b044ad742cd52ae866f3007d2f17141fc7355c4a34ad9f96ca304c4",
}
ALLOWANCES = {
    Q5_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-remaining-four-20261115/492-001-successor.json",
            "sha256": "087eb01b60460383323b267664d29c447c10873edc94b764611378777b83a3bf",
        },
    },
}


def admit_remaining_four_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
