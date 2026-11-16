"""Explicit completed final-four GTDB proof admissions, #2848, 2026-11-15.

Only pinned native units are admitted by the unchanged shared core. Historical
biology, stock identities and scientific limitations remain protected.
"""

import scoped_gtdb_successor as successor

BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
SORGHUM_PATH = "kb/communities/Sorghum_SRC2v4_Root_Colonization_SynCom.yaml"
TRANSWELL_PATH = "kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml"
NASAL_PATH = "kb/communities/Nasal_SynCom_C_Bioreactor.yaml"
RUMEN_PATH = "kb/communities/Optimized_Rumen_Fiber_Degrading_SynCom3.yaml"
BEFORE = {
    SORGHUM_PATH: "e67c57dbf77a55bc484285c5d4fe879e83c556034452104ab61e2d188e29c91c",
    TRANSWELL_PATH: "51bf55d56342aa28864c0dd458a172209f9ef1e14e51a0cd210bb46521a17f47",
    NASAL_PATH: "4bd66811333c6960ebab5553e7ce71c8a4f92aa1d81f0fc2c9e2b4f6b75dac2e",
    RUMEN_PATH: "ee1333388f5d7353daf7713abf744220accf40a855bdbe8b66389f9b7c5031c6",
}
ALLOWANCES = {
    SORGHUM_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-final-four-20261115/348-001-successor.json",
            "sha256": "dae0e0282f6b8abef2a36a44a485799778765a0053af55b06b3fc5af2eeef74d",
        },
    },
    TRANSWELL_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-final-four-20261115/091-001-successor.json",
            "sha256": "acc4ef8ccc5a81b2e7fbe6cdef606bf0ed2a6f56bd65bbb336cc4c9e9269070a",
        },
    },
    NASAL_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-final-four-20261115/395-001-successor.json",
            "sha256": "c61d31cce2a289926e1f24702e7aca2f5fba26d10ba35def1206e8fe92a708b5",
        },
    },
    RUMEN_PATH: {
        "baseline_revision": BASE,
        "manifest": {
            "path": "reports/gtdb-final-four-20261115/398-001-successor.json",
            "sha256": "cc2ee66fc53f0e2405f1d051251138ac001484213c67bfbd7fe938d82ca470e6",
        },
    },
}


def admit_final_four_successor(root, path, before_sha256, *, current=None):
    return successor.admit(root, path, before_sha256, ALLOWANCES, current=current)
