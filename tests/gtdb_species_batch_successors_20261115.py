"""Explicit reviewed species-route proof pins; admission stays in the shared core.

#2848, 2026-11-15. Historical callers supply their exact ledger predecessor hash.
Only persisted, independently reviewed technical proofs may be added here. This
registry neither changes historical biology predicates nor approves science.
"""

from scoped_gtdb_successor import admit

ALLOWANCES = {
    "kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-339-001-successor.json"
            ),
            "sha256": "eb258d2c17a5f4fd9fd69df0d7d29fc6b027f3d5f587232423604aad1a46d5f9",
        },
    },
    "kb/communities/TwoStep_PCB_Copper_Gold_Bioleaching_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-491-001-successor.json"
            ),
            "sha256": "f235a13393645008c245dbd4e4d4a0c2dd6163153d4c859476b8ed4375486be4",
        },
    },
    "kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-414-001-successor.json"
            ),
            "sha256": "e11b6ba308c4e6d51b9efa4f217dcc1e98da943bc71df877250674a8d212c5ec",
        },
    },
    "kb/communities/Wheat_CrownRot_TB_CrossKingdom_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-391-001-successor.json"
            ),
            "sha256": "857ffe01920e24f8a00331ea0ee923abd2a164e4ce0fbd5d0b918334ac10ce6b",
        },
    },
    "kb/communities/Bacillus_A1_A3_Naphthalene_Biofilm_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-358-001-successor.json"
            ),
            "sha256": "86b14cbad1df841082a7f08352c004848ed63ef6f2504467cf6b22d611b0d48a",
        },
    },
    "kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-502-001-successor.json"
            ),
            "sha256": "d75be094da229f35e6b408a19276b94cf45fff4f804cd781aae1833343932542",
        },
    },
    "kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-503-001-successor.json"
            ),
            "sha256": "b6735798d328a013b5581ef0750665b8a460ab03bb0b7cf925466f712f8bd96a",
        },
    },
    "kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-504-001-successor.json"
            ),
            "sha256": "98d15e91afbcc6a95a8531634442adbb143addcbbdaf0a1da6421718600dd708",
        },
    },
    "data/isolates/Bacillus_Paranthracis_A1_PAH_Biofilm_Isolate_Baseline.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": (
                "reports/gtdb-species-third-batch-20261115/" "remaining-nine-550-001-successor.json"
            ),
            "sha256": "74438fa2ad00d085867c574d9b4efd119efe56a114a82624356e1b90e8ef5dda",
        },
    },
    "kb/communities/Endophytic_SynCom_NS_Brassica_Cadmium_Phytoextraction_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-fourth-batch-20261115/476-001-successor.json",
            "sha256": "b70d2a46be03564960011eed981535735b7e459d1f73d460c567211a5c61a1df",
        },
    },
    "data/isolates/Bacillus_Paramycoides_B81_PAH_Biodegradation_Isolate_Baseline.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-third-batch-20261115/549-001-successor.json",
            "sha256": "e23162ae95ef3cf54651ccd8efe9fcc703de2cfde3004e1391a5e2ffadaffdff",
        },
    },
    "kb/communities/Priestia_Pseudomonas_Rice_Arsenic_Stress_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-341-002-successor.json",
            "sha256": "52894ec26d55326c0fecb23270f8846055a9d9110b45a3fdb3947dd7b63a31dd",
        },
    },
    "kb/communities/RH1_Glyphosate_Streptomyces_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-361-002-successor.json",
            "sha256": "a365837d0d94bd1c3c96a2e1f94f4458e873b3f160ef0c09bc8e1cbd92b596fc",
        },
    },
    "kb/communities/Soy_Sauce_Temporal_SevenSpecies_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-378-002-successor.json",
            "sha256": "b0713cdd3fd3d1cf5ffb4723a585fc8273cf59e8d65a379452a4acca65ac1a88",
        },
    },
    "kb/communities/Viili_Fungus_Bacterium_EPS_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-408-002-successor.json",
            "sha256": "3827783f9181c59fe309c5613ef277d000a9dd99a814b39b95e49eeeefe59c83",
        },
    },
    "kb/communities/Glutamicibacter_S11_Aquaculture_Nitrogen_Removal_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-411-002-successor.json",
            "sha256": "3d0ffedf7b53b0e05bd870a9a31996164c97c93b8f25f93ad42105494a21f652",
        },
    },
    "kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-432-002-successor.json",
            "sha256": "789c3775293092370320eab31865f29c2bd541ca5c6918a7c2fb55aaec424101",
        },
    },
    "kb/communities/Halobacillus_Black_Gram_Halophilic_PGPR_Consortium.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-472-002-successor.json",
            "sha256": "3d54e977e68846620cbe3eb9e4c52c941c64cb3496eb453913cc0a4f26efb235",
        },
    },
    "kb/communities/Delftia_Klebsiella_Light_Driven_Hydrogen_Denitrifying_Coculture.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/second-eight-481-002-successor.json",
            "sha256": "f6090d8246213328f979e2a50a96bdc80b9e3a29eb0a9089540a771a60fd3dbf",
        },
    },
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
