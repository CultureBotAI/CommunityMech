"""Explicit higher-rank technical successors, #2848, 2026-11-15.

Only immutable per-record public proofs enter this registry. Admission delegates
to the shared core; every unknown changed record remains an error. Historical
scientific ledgers and biological predicates retain their original meaning.
"""

from scoped_gtdb_successor import admit

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
ALLOWANCES = {
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
