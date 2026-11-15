"""Admit explicit native taxonomy successors through shared proof, #2848, 2026-11-15.

No scientific exemption or recomputation. Old ledgers remain immutable; the
shared core proves current biology and old history are unchanged.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
RUMEN_PATH = (
    "kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml"
)
TOBACCO_PATH = "kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml"
BAIJIU_PATH = "kb/communities/Baijiu_Pit_Mud_Hexanoic_Acid_SynCom_G4.yaml"
AT_PATH = "kb/communities/At_RSPHERE_SynCom.yaml"
C1_PATH = "kb/communities/Hexamine_Formaldehyde_Consortium_C1.yaml"
PMSX_PATH = "kb/communities/Carbon_Substrate_PMSX_Biofilm_SynCom.yaml"
T2_PATH = "kb/communities/Cyantraniliprole_Consortium_T2.yaml"
T3_PATH = "kb/communities/Cyantraniliprole_Consortium_T3.yaml"
C2_PATH = "kb/communities/Hexamine_Formaldehyde_Consortium_C2.yaml"
C3_PATH = "kb/communities/Hexamine_Formaldehyde_Consortium_C3.yaml"
C4_PATH = "kb/communities/Hexamine_Formaldehyde_Consortium_C4.yaml"
C5_PATH = "kb/communities/Hexamine_Formaldehyde_Consortium_C5.yaml"
BEFORE = {
    RUMEN_PATH: "f9ad860387600c64fa0ba428afdfd9fa4cc0e960097b445b5253eb953ed1336e",
    PMSX_PATH: "8dc5ea53ef9ad6dc4469c8e9b4897a77fd9a0c1c6addb73881891884fb4a6e65",
    T2_PATH: "cd6a38668c90338cf89fe2279e1958fffd8b12da401ea0ad82b4faaa08b526f6",
    T3_PATH: "a09fbcc47c0c084facbf9a501bbef519452bc4c70ad31f0071a383d5db144457",
    C2_PATH: "5a2c59369389c982d1a1f2a54d2a278eee49908493a78e5c54d85af2d575979d",
    C3_PATH: "042454b4b13904fcd05ee42b019346e9940ef68ae6504be8f745266e1d9f2c5f",
    C4_PATH: "63a03e2e8960e287c4637edf7562b97d8c90e9ee25d07a3f77fb8843170488bd",
    C5_PATH: "c80260476fe0975446f9e2415313873060271d7a38240c64bae507ed7055b99e",
    C1_PATH: "1183b1f4762087ed7d8adf1b9960dc38beda73f5d23a8c378fdf8fd0a23e0a2a",
    TOBACCO_PATH: "c9f62a78e6ca7a6c6fc3f3886a77fb9d7e0583f3ce931dd474aeefa2217a1e9d",
    BAIJIU_PATH: "a284ede66ef1dee551a8ba37b94d2a0dd0e63578f7b4bb6899792dd08d53a74a",
    AT_PATH: "b615c84fa2415eecbf9eb3964ee830fdb3bc573508fbc42ce601fb340f3500c0",
}
ALLOWANCES = {
    RUMEN_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-native-null-275-20261115/rumen275-001-successor.json",
            "sha256": "123706faca69aff41a791df1aff42b2b0a12f0d0d1040c0e6f0a2ae973666f77",
        },
    },
    PMSX_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/400-001-successor.json",
            "sha256": "6416793166bd41f0efd47f28447255b1f57b48904fdfe77d937fcc6135668844",
        },
    },
    T2_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/499-001-successor.json",
            "sha256": "3d0ffcc3988a889507ba83fcb0256333ad564665208a813895b74b2b9bd2d8e1",
        },
    },
    T3_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/500-001-successor.json",
            "sha256": "926bc4c078c9738dbd30ce95a035a45d8491fc50b269b6a22b6c3932ae2eaf8b",
        },
    },
    C2_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/506-001-successor.json",
            "sha256": "ce9d9d6aa2e27483eabfb30fa1d3120d344a8232e56858bec32da9915e097cf5",
        },
    },
    C3_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/507-001-successor.json",
            "sha256": "a34cbe212510e1ff24a1aef763580e3730755abc3f1bce42498fb98610c03d64",
        },
    },
    C4_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/508-001-successor.json",
            "sha256": "c8b210dbde99f13b4e3922a1dc908937593078600a729ca4cd6bd8bae42608d0",
        },
    },
    C5_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-ambiguity-eight-20261115/509-001-successor.json",
            "sha256": "960db7d2b4f9e121898c241c78396e3620f2af5faf85c905f5289dbc5cd27edc",
        },
    },
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
