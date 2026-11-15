"""Explicit environmental-record taxonomy admissions, #2848, 2026-11-15.

Only pinned actual native proofs are admitted. The shared core preserves all
other biology and old history; no source or scientific finding is waived.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
DICLOFENAC = "kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml"
BEFORE = {
    DICLOFENAC: "d8e197f2bb938229e5e6cb3424a509aad5c4f62e45022ae2e1a7860eaac5a1b1",
}
ALLOWANCES = {
    DICLOFENAC: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-environment-four-20261115/379-001-successor.json",
            "sha256": "7add3185305e5540113efbf0a695eff1a629f680b487eaef3d6c68c76a6ed58f",
        },
    },
}


def admit_environment_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
