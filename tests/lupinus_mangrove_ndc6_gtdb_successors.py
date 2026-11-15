"""Explicit Lupinus/Mangrove/NDC6 proof admissions, #2848, 2026-11-15.

Only completed, pinned native units are admitted by the unchanged shared core.
Historical biology, stock identities and scientific limitations remain protected.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
LUPINUS_PATH = "kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml"
BEFORE = {
    LUPINUS_PATH: "59a83e4d0b1defdc5f3bae63bccb38caa87fa9fd90a6c115e5be6f518998f6ff",
}
ALLOWANCES = {
    LUPINUS_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-lupinus-mangrove-ndc6-20261115/427-001-successor.json",
            "sha256": "c69ec9a514b2212e7bb1c75eb19aacf1a40ce2966361a5f3e957dc34c8c0a197",
        },
    },
}


def admit_lupinus_mangrove_ndc6_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
