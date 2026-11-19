"""Prepare one native-check config from a reviewed M5 application, 2026-11-15.

Inputs: one of seven fixed record IDs and its retained stage/application receipts.
Output: one exclusive JSON config for the unchanged native checker, #2848/PR2881.
This does not apply records, run checks, change policies or certify science.
"""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIVATE = ".temp/gtdb-ambiguity-eight-20261115"
PUBLIC = "reports/gtdb-ambiguity-eight-20261115"
REVISION = "ee9930cb145805101cc87b0a9ba188616cbf7ab8"
TABLE = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
SOURCE = "efc851cec1476ecfd204bf5f6e0ce5e898a247a4b6feab62498039b777b2667f"
REVIEWED = {
    "400": (
        "431b4abfb1e55b3a3410cdbb26c055c7d713250f14bb9443b1924516a41b69f1",
        "9763ae81a1d772f4513b2ff4f53c684be6f80f34d34bf2ddd3b348d900b97b04",
    ),
    "499": (
        "a050977eb02d61cdbb027ebec0c1209d4550addfc71de5c109233e1a5475d104",
        "f40d3e671cf3f043148f306dca35515346e0b9f7a62e63922caa6749ff79d423",
    ),
    "500": (
        "0ce651c369c0c4a0403ccbf7e9a0bee9bb4043c4759af951b8e275792debf6a1",
        "2f20197cc0b61bab650b1c82396823814010b343401d25260f347647ac8e61ed",
    ),
    "506": (
        "3486aeded8af49715e065e14c0fe8cc2868ea0eba4fbcc0568ac725ad50291b0",
        "fc1d71fb8e9c33b2ae0c69ad83470785ff7cff674b0572479496737be38dc09e",
    ),
    "507": (
        "390813890b2c68feedc5c0896312a27cee4191063dcfb04ab0d5f9d9e0914744",
        "b74f5a2dc0a11b32a754c193108134a1027fe0b89f525b0e19cc50b40d2c5481",
    ),
    "508": (
        "fcb1b6a31b958130163813c5ca859649a027a53da5234817bbccef0847246baf",
        "33c0c21508c48cf7af08400104faff45ccf3d8d4d3908119b696b369f8d72d56",
    ),
    "509": (
        "ca7c7518979b0f8bcb732da4878a57f9f92cf5be5e236f3e1ef46f3a1a955247",
        "fc1f5a5ce3f48bd7d606636af3ae613f69353ae62691d6e454fe06f79941ad22",
    ),
}
DETAILS = {
    "400": "Retain all eleven native Stenotrophomonas alternatives for the PMSX X descriptor. Preserve PRJEB18431 and the source's earlier Xanthomonas name, the other three members, spatial and substrate observations, source quotations and all biological fields. No alternative is selected or study genome reclassified.",
    "499": "Retain all eight native Serratia alternatives separately for the Bo1 and Bo2 descriptors. Preserve their distinct MALDI-TOF best matches and scores; a database best-match name does not establish stock identity or an assembly. Other T2 members, formulations, endpoints and inferred-enzyme limitations remain unchanged.",
    "500": "Retain both native Bacillus halotolerans and Bacillus mojavensis alternatives for the Ht3 descriptor. Preserve its MALDI-TOF best match and score, all other T3 members and biological claims. Do not reinterpret the source isolate as either reference species or an identified genome.",
    "506": "Preserve C2 stocks SRCHD03, SRCHD05 and genus-only SRCHD06. Retain all three Brevundimonas and all three Ochrobactrum alternatives; the Brucella pseudintermedia descriptor receives its native 18-genome, fraction-1.0 Ochrobactrum pseudintermedium reference correspondence. Partial-16S identification, formulation, isolate kinetics and bulk endpoints remain distinct.",
    "507": "Preserve C3 stocks SRCHD04, SRCHD05 and genus-only SRCHD06; SRCHD04 is not SRCHD03. Retain all three Brevundimonas and all three Ochrobactrum alternatives; the Brucella pseudintermedia descriptor receives its native 18-genome, fraction-1.0 Ochrobactrum pseudintermedium reference correspondence. Preserve all source and biological claims.",
    "508": "Preserve C4 stocks SRCHD05, genus-only SRCHD06 and the separate SRCHD07. Both Brucella pseudintermedia descriptors receive the native 18-genome, fraction-1.0 Ochrobactrum pseudintermedium reference correspondence; SRCHD06 retains all three genus alternatives. Shared reference correspondence does not merge study stocks or alter isolate kinetics and bulk endpoints.",
    "509": "Preserve all five C5 stocks SRCHD03-SRCHD07. The two Brevundimonas stocks retain all three alternatives separately, the two Brucella pseudintermedia descriptors receive the native 18-genome, fraction-1.0 Ochrobactrum pseudintermedium reference correspondence, and genus-only SRCHD06 retains all three alternatives. Preserve every formulation, kinetic and bulk-endpoint distinction, including the separate C6 experiments.",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepare(record_id):
    stage_dir = ROOT / PRIVATE / f"{record_id}-candidate-001"
    stage_bytes = (stage_dir / "receipt.json").read_bytes()
    expected_stage, expected_after = REVIEWED[record_id]
    if digest(stage_bytes) != expected_stage:
        raise ValueError("stage receipt differs from independently reviewed bytes")
    stage = json.loads(stage_bytes)
    application_name = f"{PRIVATE}/{record_id}-applied-001/receipt.json"
    application_bytes = (ROOT / application_name).read_bytes()
    application = json.loads(application_bytes)
    expected_id = f"CommunityMech:{int(record_id):06d}"
    if (
        application["applied"] is not True
        or application["execution_revision"] != REVISION
        or stage["code_revision"] != REVISION
        or application["target_id"] != expected_id
        or stage["target_id"] != expected_id
        or application["target"] != stage["target"]
        or application["before_sha256"] != stage["before_sha256"]
        or application["after_sha256"] != expected_after
        or stage["candidate_sha256"] != expected_after
        or application["reviewed_receipt_sha256"] != expected_stage
        or application["source_proof"] != stage["source_proof"]
        or application["source_proof"]["sha256"] != SOURCE
        or digest((stage_dir / Path(stage["target"]).name).read_bytes()) != expected_after
    ):
        raise ValueError("actual application differs from accepted candidate/provenance")
    config = {
        "target": stage["target"],
        "before_sha256": stage["before_sha256"],
        "after_sha256": expected_after,
        "application_receipt": application_name,
        "application_receipt_sha256": digest(application_bytes),
        "crosswalk": f"{PRIVATE}/kg-microbe/data/raw/NCBI2GTDB.tsv.gz",
        "crosswalk_sha256": TABLE,
        "history_scaffolder_revision": "23899092a4a2aedf53ff4435c0bdc03ebd79e6be",
        "issue": "https://github.com/CultureBotAI/CommunityMech/issues/2848",
        "history_summary": "Record complete native ambiguity options and scoped reference correspondence for "
        + expected_id
        + ".",
        "history_details": DETAILS[record_id]
        + " Reference populations do not identify experimental stock assemblies. The pinned table has no verified upstream release label. All old events remain unchanged. This bounded technical change and its validators do not complete scientific review.",
    }
    output = ROOT / PUBLIC / f"{record_id}-check-config-001.json"
    with output.open("x") as handle:
        handle.write(json.dumps(config, indent=2) + "\n")
    print(
        json.dumps({"path": str(output.relative_to(ROOT)), "sha256": digest(output.read_bytes())})
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record_id", choices=REVIEWED)
    prepare(parser.parse_args().record_id)
