"""Explicit completed units in the last genus lane, #2848, 2026-11-16.

Only pinned actual native proofs enter this registry. Enforcement stays in the
shared successor core; source preparation never admits a changed record.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
DOLICHOSPERMUM = "kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml"
BEFORE = {
    DOLICHOSPERMUM: "d4da92fc50e4b006fcaaf2d830d5c668e1e2671cea3b00655909a97a8c5e4bd1",
}
ALLOWANCES = {
    DOLICHOSPERMUM: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-genus-last-four-20261115/441-001-successor.json",
            "sha256": "b473194da537ffccae554c2e308de9e2c11062b8cd7ae29bb54a46613f369292",
        },
    },
}


def admit_genus_last_four_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
