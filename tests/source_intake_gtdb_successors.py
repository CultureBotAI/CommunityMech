"""Explicit source-intake taxonomy admissions, #2848, 2026-11-15.

Only pinned actual native proofs are admitted. The shared core preserves all
other biology and old history; no source or scientific finding is waived.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
KZ_PATH = "kb/communities/Klebsiella_Arthrobacter_KZ_Phenanthrene_Cadmium_SynCom.yaml"
T1_PATH = "kb/communities/Cyantraniliprole_Consortium_T1.yaml"
T4_PATH = "kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml"
C6_PATH = "kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml"
BEFORE = {
    KZ_PATH: "65275177a514ceb42276f4f416da7b727e5200b3a8f79fb1510cf6c49bbd083c",
    T1_PATH: "9ebd2f07ce536e4e92569e93b36f69ac1c3f8efce458c1520a5879000cbb2c90",
    T4_PATH: "0ecd37ff8b4675764844c6d704c634832fecd8635b80e6f9c5759c217345595c",
    C6_PATH: "275243762d5d3c3032178fcc68b9005177a5d0f1924ff6ef01e3aeaf114e8d08",
}
ALLOWANCES = {
    KZ_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-source-intake-four-20261115/344-001-successor.json",
            "sha256": "a2bffc7b22041ee8df2b0437f5a78443f09320d14cdaf4a80ffae299a8406486",
        },
    },
    T1_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-source-intake-four-20261115/498-001-successor.json",
            "sha256": "83f32c5a294dbbf7e99beed4706206627945a132658ab4717a54ecd02e9c5ab8",
        },
    },
    T4_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-source-intake-four-20261115/369-001-successor.json",
            "sha256": "6503713995e2be8907f152c579cd9bceeeaf981a01bb73da2f6e836f1bcef452",
        },
    },
    C6_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-source-intake-four-20261115/405-001-successor.json",
            "sha256": "c53dccbb03dd4d5ee31f24581fefa18820d0c70fb81b9f6766ef8e4c9b835353",
        },
    },
}


def admit_source_intake_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
