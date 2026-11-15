"""Explicit Lupinus/Mangrove/NDC6 proof admissions, #2848, 2026-11-15.

Only completed, pinned native units are admitted by the unchanged shared core.
Historical biology, stock identities and scientific limitations remain protected.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
LUPINUS_PATH = "kb/communities/Lupinus_SC7_Rhizosphere_SynCom.yaml"
MANGROVE_PATH = "kb/communities/Mangrove_Benzene_MFC_Bioanode_Consortium.yaml"
NDC6_PATH = "kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml"
BEFORE = {
    LUPINUS_PATH: "59a83e4d0b1defdc5f3bae63bccb38caa87fa9fd90a6c115e5be6f518998f6ff",
    MANGROVE_PATH: "96166a3b9e1e6298b99bb0930ac0cab6b69018ea5b54788e0e9f65231f9bbb6e",
    NDC6_PATH: "1a1c02d8b33165075608eba9bc482646843cecfe41a7a99c3d47f5ab9bbb5c97",
}
ALLOWANCES = {
    LUPINUS_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-lupinus-mangrove-ndc6-20261115/427-001-successor.json",
            "sha256": "c69ec9a514b2212e7bb1c75eb19aacf1a40ce2966361a5f3e957dc34c8c0a197",
        },
    },
    MANGROVE_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-lupinus-mangrove-ndc6-20261115/442-001-successor.json",
            "sha256": "790b3730d7114cd90e76e4e3b0921ac493cb6b472d6c48c32376828d3a8ecbcb",
        },
    },
    NDC6_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-lupinus-mangrove-ndc6-20261115/463-001-successor.json",
            "sha256": "110f82ebb7539721ccc07cb0bca3991dda632a9918c59194b956a9b2a4991309",
        },
    },
}


def admit_lupinus_mangrove_ndc6_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
