"""Explicit reviewed species-route proof pins; admission stays in the shared core.

#2848, 2026-11-15. Historical callers supply their exact ledger predecessor hash.
Only persisted, independently reviewed technical proofs may be added here. This
registry neither changes historical biology predicates nor approves science.
"""

from scoped_gtdb_successor import admit

ALLOWANCES = {
    "kb/communities/Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom.yaml": {
        "baseline_revision": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "manifest": {
            "path": "reports/gtdb-species-status-20261115/next-ten-388-001-successor.json",
            "sha256": "b810a33b29abba9f4c5e511ec7d946f5b9e0ce1679253373377925cafb726454",
        },
    },
}


def admission(root, path, predecessor_sha256):
    return admit(root, path, predecessor_sha256, ALLOWANCES)
