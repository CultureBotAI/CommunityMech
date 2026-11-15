"""Explicit source-intake taxonomy admissions, #2848, 2026-11-15.

Only pinned actual native proofs are admitted. The shared core preserves all
other biology and old history; no source or scientific finding is waived.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
KZ_PATH = "kb/communities/Klebsiella_Arthrobacter_KZ_Phenanthrene_Cadmium_SynCom.yaml"
BEFORE = {
    KZ_PATH: "65275177a514ceb42276f4f416da7b727e5200b3a8f79fb1510cf6c49bbd083c",
}
ALLOWANCES = {
    KZ_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-source-intake-four-20261115/344-001-successor.json",
            "sha256": "a2bffc7b22041ee8df2b0437f5a78443f09320d14cdaf4a80ffae299a8406486",
        },
    },
}


def admit_source_intake_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
