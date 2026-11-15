"""Explicit PPCP420 mixed fungal admission, #2904, 2026-11-15.

Only this completed actual proof is admitted; unknown changes still refuse.
The reviewed fungal core and every previous mapping-only core stay unchanged.
"""

from scoped_gtdb_fungal_successor import admit

TARGET = "kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml"
BEFORE = "1ec35a19be4bccd263fd578dffe22ebe67642fa9f7a16d8f845176b0afb354b6"
ALLOWANCES = {
    TARGET: {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-ppcp420-domain-20261115/420-001-successor.json",
            "sha256": "8bc196c251d2dc5500a65392b1c35189deb8a42b4d783cba63edd030e160c177",
        },
    }
}


def admit_ppcp_successor(root, path, predecessor_sha256, *, current=None):
    return admit(root, path, predecessor_sha256, ALLOWANCES, current=current)
