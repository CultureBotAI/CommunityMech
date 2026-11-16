"""Explicit completed final-four GTDB proof admissions, #2848, 2026-11-15.

Only pinned native units are admitted by the unchanged shared core. Historical
biology, stock identities and scientific limitations remain protected.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
SORGHUM_PATH = "kb/communities/Sorghum_SRC2v4_Root_Colonization_SynCom.yaml"
BEFORE = {
    SORGHUM_PATH: "e67c57dbf77a55bc484285c5d4fe879e83c556034452104ab61e2d188e29c91c",
}
ALLOWANCES = {
    SORGHUM_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-final-four-20261115/348-001-successor.json",
            "sha256": "dae0e0282f6b8abef2a36a44a485799778765a0053af55b06b3fc5af2eeef74d",
        },
    },
}


def admit_final_four_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
