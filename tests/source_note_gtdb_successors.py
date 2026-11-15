"""Explicit completed note-plus-mapping admissions; no inferred targets (#2869).

2026-11-15: immutable original and real ROOT intermediate bytes are both required.
The exact composite delegates its final leg to the unchanged mapping-only core.
"""

from source_note_gtdb_successor import admit

TARGET = "kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml"
WHEAT = "kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml"
CARAGANA = "kb/communities/Caragana_Korshinskii_CrossKingdom_Forage_SynCom.yaml"
MULBERRY = "kb/communities/Mulberry_Distillers_Grains_Feed_Consortium.yaml"
BEFORE = {
    TARGET: "2003158329c3f2113f6239f65b1e6a1b85bd3c19204f7aaf9d90be7f1f5c68f0",
    WHEAT: "613f8b97efa732c213fae320935a4f8cafa8cb899718e6c18a7c1f47f9ba0420",
    CARAGANA: "c25facb4d904532aae4c45fe2b63c08a48983c4ce86cb46b4298a30e4847ab06",
    MULBERRY: "db5dd094bbd49fba2952851b1d8394c3b30d04cb08440f850ae04cc77614137d",
}
ALLOWANCES = {
    TARGET: {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-source-holds-20261115/paenibacillus-composite-successor-001.json",
            "sha256": "0e62d5ee554abde28a513814ada7e9e35330941bcc8fbc83a9cce318340a6f95",
        },
    },
    WHEAT: {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-source-holds-20261115/wheat409-composite-successor-001.json",
            "sha256": "5add0f48c79d681d565d61118ba7f817ad9e1fae7e774f0aba8e8a3878922867",
        },
    },
    CARAGANA: {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-source-holds-20261115/caragana338-composite-successor-001.json",
            "sha256": "c771f37e06feb597751c40acc7c0d7f76058773e7023ab1b5de47d2983d57b18",
        },
    },
    MULBERRY: {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-source-holds-20261115/mulberry435-composite-successor-001.json",
            "sha256": "55b887854e5f4b23bf1206cdbb9252ca8bce061756b76b4d6d054101a1185c74",
        },
    },
}


def admit_note_mapping_successor(root, path, predecessor_sha256, *, current=None):
    return admit(root, path, predecessor_sha256, ALLOWANCES, current=current)
