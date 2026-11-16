"""Explicit Shrimp-lane taxonomy admissions, #2848, 2026-11-15.

Only pinned actual native proofs enter this registry. The shared core preserves
all other biology and old history; historical scientific ledgers stay immutable.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
SHRIMP_PATH = "kb/communities/Shrimp_Vibrio_Resistance_Gut_Enrichment_SynCom_Panel.yaml"
BEFORE = {
    SHRIMP_PATH: "f23b26c7b39205a716e77e5149c06e2c4e4c618dec523a3e5245c65370ec7c0e",
}
ALLOWANCES = {
    SHRIMP_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-shrimp-thermophilic-sahara-20261115/436-001-successor.json",
            "sha256": "f08c08480c9af4b71c844d0daf9299f43c703111064f9f73062f7c50f16647fb",
        },
    },
}


def admit_shrimp_lane_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
