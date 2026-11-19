"""Exact remaining-four reference proofs, #2848, 2026-11-15.

Only independently reviewed, persisted units enter this registry. The unchanged
shared core preserves all other biology and history; scientific findings remain.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
Q5_PATH = "data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml"
PPHET_PATH = "kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml"
BUTANOL_PATH = "kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml"
ARSENIC_PATH = (
    "kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml"
)
BEFORE = {
    Q5_PATH: "3be922d81b044ad742cd52ae866f3007d2f17141fc7355c4a34ad9f96ca304c4",
    PPHET_PATH: "f11af6a3d089a413d75e3c07203473f02529734a75c90af1c4c5b33ce2c44243",
    BUTANOL_PATH: "6210d91810b668f546c1e2f17c7f2c01ed37bc250d6314f79696ee7e591b063c",
    ARSENIC_PATH: "a16dd88b010ff55a4e1cc7543271b42ba9641f05f070febffa3de96d66d966f9",
}
ALLOWANCES = {
    Q5_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-remaining-four-20261115/492-001-successor.json",
            "sha256": "087eb01b60460383323b267664d29c447c10873edc94b764611378777b83a3bf",
        },
    },
    PPHET_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-remaining-four-20261115/359-001-successor.json",
            "sha256": "338af167a8140c1aa3008b8355f5406bdbf04e15f42cbc9489d498e5429da9ad",
        },
    },
    BUTANOL_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-remaining-four-20261115/497-001-successor.json",
            "sha256": "47822a8cb7f752d8f71fe1423897d9a72c1a35974f9f61c63d8ee5ee8b1bc768",
        },
    },
    ARSENIC_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-remaining-four-20261115/454-001-successor.json",
            "sha256": "c745329f84aab2c6216e1252c6cc331f9322951c8e9bd9175c348a0fc0b0e4c0",
        },
    },
}


def admit_remaining_four_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
