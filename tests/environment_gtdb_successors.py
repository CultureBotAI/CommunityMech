"""Explicit environmental-record taxonomy admissions, #2848, 2026-11-15.

Only pinned actual native proofs are admitted. The shared core preserves all
other biology and old history; no source or scientific finding is waived.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
DICLOFENAC = "kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml"
TCP = "kb/communities/TCP_NonDehalogenimonas_Groundwater_Consortium.yaml"
WHEAT_DT = "kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml"
BEFORE = {
    DICLOFENAC: "d8e197f2bb938229e5e6cb3424a509aad5c4f62e45022ae2e1a7860eaac5a1b1",
    TCP: "ab6b0b9201bc3d3ca9c7b2cbd5395404b1ed071c064d2efb36351e4d72d6d02b",
    WHEAT_DT: "ee5b482655aeb0d187e29cfe8b18016b247b355f3d63dbba2db3b591c84f05ef",
}
ALLOWANCES = {
    DICLOFENAC: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-environment-four-20261115/379-001-successor.json",
            "sha256": "7add3185305e5540113efbf0a695eff1a629f680b487eaef3d6c68c76a6ed58f",
        },
    },
    TCP: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-environment-four-20261115/437-001-successor.json",
            "sha256": "51ba6ae78d58bfb8fa12f6693918ab928a49e842a38be0e71219fd2948da70f3",
        },
    },
    WHEAT_DT: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-environment-four-20261115/429-001-successor.json",
            "sha256": "14c2e9c85d0115efc800469190455fdf9d3d98b6ba61757239084af7f2490481",
        },
    },
}


def admit_environment_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
