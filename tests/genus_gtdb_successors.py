"""Explicit higher-rank technical successors, #2848, 2026-11-15.

Only immutable per-record public proofs enter this registry. Admission delegates
to the shared core; every unknown changed record remains an error. Historical
scientific ledgers and biological predicates retain their original meaning.
"""

from scoped_gtdb_successor import admit

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
ALLOWANCES = {
    "kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/phage-pair-467-001-successor.json",
            "sha256": "6e46a3c754bf766546669c4abfb28bad36cc00fbd19f89dc634ebd2887ab1c76",
        },
    },
    "kb/communities/Cold_Seep_ANME_SRB_Carbon_Monoxide_Syntrophic_Consortium.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-family-475-001-successor.json",
            "sha256": "7c370366c098ea0c61d0e268604f43ca7dd29fef4702c77c97255fad975d65dd",
        },
    },
    "kb/communities/High_Ammonia_Biogas_0B_Butyrate_Oxidizing_Enrichment.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-mixed-four-350-001-successor.json",
            "sha256": "5f2ebfd59361d99c4e7d968e960e32ecc5072842d39fbaaae62aa0e1004b6baf",
        },
    },
    "kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-mixed-four-364-001-successor.json",
            "sha256": "eae3a9fd00f8552e6c834e7c8a929d5dc178dc585d96eb70b6394bfe8e40cde3",
        },
    },
    "kb/communities/Alfalfa_Stress_Adapted_Bacterial_SynCom.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-mixed-four-458-001-successor.json",
            "sha256": "6612d430644712b57b1444532b8a49c6d732a50a1cd0fdfafdb9befd007bfed4",
        },
    },
    "kb/communities/Caragana_Wheat_Drought_SynCom15.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-mixed-four-456-001-successor.json",
            "sha256": "610e7ef69a190344cdf68b7e7c66a873333e9915c0d03c1c2a797a093e587c2c",
        },
    },
    "kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-mixed-384-001-successor.json",
            "sha256": "bd8fd08c99cf2bf97298e93cc67719d4bdabd6266fb4e995f6e563878a55ad8e",
        },
    },
    "kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-415-001-successor.json",
            "sha256": "72d85fec7d9736b3b875ec60002167728f1b5c7bd69b89e9b71272dd2f4d196a",
        },
    },
    "kb/communities/Cucumber_Low_Phosphorus_Cross_Kingdom_Biocontrol_SynCom.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-477-001-successor.json",
            "sha256": "6a5b0d311f52bd87842f5999edc1342d233fab504126b9ff415c2bb1f303f67c",
        },
    },
    "kb/communities/Hualgayoc_Acidic_Sulfate_Reducing_AMD_Consortium.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-353-001-successor.json",
            "sha256": "b7b6d72527ec7916c063ae9e77873700ea96a242d44fb75b0e48b677f13bdf25",
        },
    },
    "kb/communities/Electrostimulated_Toluene_Methanogenic_Microbiota.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-440-001-successor.json",
            "sha256": "df840b3bc6342b1ed238b5d7d5fc48a1bfc1bbf62c0cf6f505884655ce6849e3",
        },
    },
    "kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-447-001-successor.json",
            "sha256": "6947116cc5dc62c57eb7ce55c0bb4de6ecc93454ee11bdd60ad0a86fd1c47460",
        },
    },
    "kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-433-001-successor.json",
            "sha256": "1ca7c686eab74369baeeb16cf3c04f253ff76c5294d5773a5ce11f754d1fdc68",
        },
    },
    "kb/communities/Whale_Fall_Vallitalea_Trichloromonas_Chitin_EET_Consortium.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-474-001-successor.json",
            "sha256": "85f585400852a55caeb1950273f4f3bcffad3cfd2457c6e5a3fb226735293299",
        },
    },
    "kb/communities/Choysum_SynLAV_DEHP_Rhizobacterial_SynCom.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-403-001-successor.json",
            "sha256": "d7eb240067b72f9f1b26d3ed52bbeba0deeb4e5e9bac1aecf68597e5a781216f",
        },
    },
    "kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-nine-410-001-successor.json",
            "sha256": "a1b18aba24732dc079afcd37a745c3a7a78b352ed1f8971174fd275b522b7251",
        },
    },
    "kb/communities/Pseudomonas_Klebsiella_Alcaligenes_FeII_Nitrogen_Removal_SynCom.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-next-three-372-001-successor.json",
            "sha256": "e42825733412ec112ac507502e6a02a8adb8c5426083f17f3ea53ede7ff5d541",
        },
    },
    "kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-next-three-349-001-successor.json",
            "sha256": "6aabe1afc6fde3be1228191ade21d69dd07e506efa4cb68d8b83952cee443b09",
        },
    },
    "kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-next-three-424-001-successor.json",
            "sha256": "e6974eccb2ff5e55b7519b88208733d6c2d6dfd14b1b983c1c3cc58ad66ad68b",
        },
    },
    "kb/communities/Nitratireductor_Gordonia_Z123_LDPE_Degradation_SynCom.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-three-342-001-successor.json",
            "sha256": "ebd654e13f0d50704b6df613ecf3f70e2be0e737e1de3993576aead436a9f7ea",
        },
    },
    "kb/communities/Microalgae_Cyanobacteria_Bioactive_Peptide_Consortia.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-three-390-001-successor.json",
            "sha256": "eccb05d97e0090aa425305e50d08889b9d713a37fb96112eac58010c8b1a3fa0",
        },
    },
    "kb/communities/Meghalaya_Bacillus_Consortia_A22ED9.yaml": {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-code006-20261115/genus-three-406-001-successor.json",
            "sha256": "543cb76351719c0eb378f5ef7c214f2731f491fd6a6a8c32c20fc637976749be",
        },
    },
}


def admit_genus_successor(root, path, predecessor_sha256, *, current=None):
    return admit(root, path, predecessor_sha256, ALLOWANCES, current=current)
