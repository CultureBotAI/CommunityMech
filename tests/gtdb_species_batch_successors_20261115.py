"""Explicit reviewed species-route proof pins; admission stays in the shared core.

#2848, 2026-11-15. Historical callers supply their exact ledger predecessor hash.
Only persisted, independently reviewed technical proofs may be added here. This
registry neither changes historical biology predicates nor approves science.
"""

from scoped_gtdb_successor import admit

ALLOWANCES = {
    "kb/communities/Phenol_Carboxylation_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000053-001-successor.json",
            "sha256": "5b4fe44ecaf71d7484f41dca5392dbfaea2e8770ba7adeecf6955cdbd345afa1",
        },
    },
    "kb/communities/Chlorella_Keystone_Taxa_Antifungal_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000313-001-successor.json",
            "sha256": "c7c401aa9c4ac9d4bb67ba359297b896ffe8afeee99ee30ab555f5027f4c8833",
        },
    },
    "kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-nine-347-003-successor.json",
            "sha256": "7d04740e4d7804b150dd8bd1fbd3ece154c434dc62cefffc17e52d5fa18afb7a",
        },
    },
    "kb/communities/Sphingobium_Nitrososphaera_Phenanthrene_Carbon_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000362-001-successor.json",
            "sha256": "d07edbe7ba53df5dde0801733e5ae6441dd46e7cb54854604d399c90f02726d2",
        },
    },
    "kb/communities/Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/next-ten-388-001-successor.json",
            "sha256": "b810a33b29abba9f4c5e511ec7d946f5b9e0ce1679253373377925cafb726454",
        },
    },
    "kb/communities/Clostridial_isoDCA_Mini_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000396-001-successor.json",
            "sha256": "4c5fa7cddcbdaa3b02656a58d11f4beddcc12c074dc44e542e6024476719c682",
        },
    },
    "kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000397-001-successor.json",
            "sha256": "53f446d5d40639d1dd5fefacbe4b16dd12b1af60243736bba0ca450facaa5634",
        },
    },
    "kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000426-001-successor.json",
            "sha256": "6f6738417f680bce1019877fae3c9b4c8264cf2fa4cca2b68d99f35b8f19839f",
        },
    },
    "kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000431-001-successor.json",
            "sha256": "97842ce3e4880d1dfad63e2e5924c87a5e6cf9603375e0659f35c676d5bbd8df",
        },
    },
    "kb/communities/Parmigiano_NWS_Set1_LAB_Triculture.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000517-001-successor.json",
            "sha256": "41b9afc6e0945a752223593297131a059d6fd8720359b938aff9e35439a201f8",
        },
    },
    "kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/remaining-nine-000522-001-successor.json",
            "sha256": "13791f9a8bcf6cc5a9bc2cc1c557d86bc5f0b9debf15ce4d598161f86109f5aa",
        },
    },
}


def admission(root, path, predecessor_sha256):
    return admit(root, path, predecessor_sha256, ALLOWANCES)
