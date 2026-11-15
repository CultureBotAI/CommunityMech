"""Admit explicit native taxonomy successors through shared proof, #2848, 2026-11-15.

No scientific exemption or recomputation. Old ledgers remain immutable; the
shared core proves current biology and old history are unchanged.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
TOBACCO_PATH = "kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml"
BAIJIU_PATH = "kb/communities/Baijiu_Pit_Mud_Hexanoic_Acid_SynCom_G4.yaml"
AT_PATH = "kb/communities/At_RSPHERE_SynCom.yaml"
C1_PATH = "kb/communities/Hexamine_Formaldehyde_Consortium_C1.yaml"
BEFORE = {
    C1_PATH: "1183b1f4762087ed7d8adf1b9960dc38beda73f5d23a8c378fdf8fd0a23e0a2a",
    TOBACCO_PATH: "c9f62a78e6ca7a6c6fc3f3886a77fb9d7e0583f3ce931dd474aeefa2217a1e9d",
    BAIJIU_PATH: "a284ede66ef1dee551a8ba37b94d2a0dd0e63578f7b4bb6899792dd08d53a74a",
    AT_PATH: "b615c84fa2415eecbf9eb3964ee830fdb3bc573508fbc42ce601fb340f3500c0",
}
ALLOWANCES = {
    C1_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/505-002-successor.json",
            "sha256": "3eea836214e4bb5184c3e459296bc0c4d599e28c3f00f8787cb346903f011b4e",
        },
    },
    TOBACCO_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-20261115/status373-001-successor.json",
            "sha256": "4c60b0c85928889507dd3cb867f6a4b1777912918b31395b198593806f6e07e4",
        },
    },
    BAIJIU_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-20261115/status365-001-successor.json",
            "sha256": "34e329bb2d142bfb9581be4f991f06da6c269097dbafbb4e384fa7a3d5d53d1c",
        },
    },
    AT_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-20261115/status003-001-successor.json",
            "sha256": "24d934f509c8a2ad78b6f76464ee388ca8de63e90859d3b49ff8bf081687136d",
        },
    },
}


def admit_status_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
