"""Pin the completed Wetland471 identity/mapping chain, #2898/#2899, 2026-11-15.

The intermediate is the actual maintained integration commit. The existing
fixed guard enforces both transitions; no additional target is admitted.
"""

import wetland_identity_gtdb_successor as guard

TARGET = guard.TARGET
BEFORE = guard.BEFORE
MAINTAINED_INTERMEDIATE = "faad27a2d22971ab0e50594ff4cb4fdf6f63d8c7"
ALLOWANCES = {
    TARGET: {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-wetland-mapping-20261115/471-production-composite-001.json",
            "sha256": "eed9e903b5c1e9934394b984e2206dc6586a01df643239a880bb1b5994c261e5",
        },
    },
}


def admit_wetland_successor(root, path, predecessor_sha256, *, current=None):
    return guard.admit(root, path, predecessor_sha256, ALLOWANCES, current=current)
