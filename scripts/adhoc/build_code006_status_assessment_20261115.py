"""Build the bounded000434 diagnostic assessment from real M5 evidence, #2848.

2026-11-15. Inputs: applied candidate002, actual receipt/sidecar, six native
gates and preserved scientific review. Outputs: exclusive private native
inspection/target JSON plus review JSON stdout; no canonical or review save.
"""

import argparse
import hashlib
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
TARGET = "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
IDENTITY = "CommunityMech:000434"
PREVIOUS = "20261105T223042Z-pr2035-acidic-nitrification-successor"
SIDECAR = (
    "history/records/Acidic_Nitrification_Minimal_Consortium/2026-11-15T045124Z-codex-aa564b.yaml"
)
REVISION = "956d00c6143020810ef7a60a6298e67fb0ee0caf"
GATES = ("schema", "strict", "gtdb", "domain", "scalars", "history")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive assessment attempt required")
    if (STATE / f"assessment-inspection-{args.attempt}.json").exists():
        raise ValueError("exclusive assessment inspection required")
    if sha(ROOT / TARGET) != "d58669e049476d801fa68cdb50184e6ac9c21c07cdbc2517ef32579f75acb7f8":
        raise ValueError("wrong applied candidate")
    applied_path = STATE / "applied-001/receipt.json"
    if sha(applied_path) != "39bac49ad4dc868eb2423d94ce1eaac64cef0bdd23595f233d81a75ac1fe853b":
        raise ValueError("wrong actual application receipt")
    applied = json.loads(applied_path.read_bytes())
    if applied["applied"] is not True or applied["execution_revision"] != REVISION:
        raise ValueError("application provenance differs")
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", "HEAD"], cwd=ROOT, text=True
    ).splitlines()
    if changed != [TARGET]:
        raise ValueError("unexpected tracked execution inputs changed")
    staged_path = STATE / "status-candidate-002/receipt.json"
    if sha(staged_path) != applied["reviewed_receipt_sha256"]:
        raise ValueError("reviewed staging receipt differs")
    staged = json.loads(staged_path.read_bytes())
    for name, expected in staged["inputs"].items():
        if name != TARGET and sha(ROOT / name) != expected:
            raise ValueError("reviewed classifier/source input changed")
    if sha(ROOT / SIDECAR) != "7c496a4563e76ecb8c6da0261d25bca8d247786b82269425f239bb47ddc1669d":
        raise ValueError("actual native sidecar changed")
    paths = [
        applied_path,
        STATE / "applied-001/before.yaml",
        STATE / "status-candidate-002/receipt.json",
        STATE / "status-candidate-002" / Path(TARGET).name,
        STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz",
        STATE / "native-source-provenance-001.txt",
        ROOT / SIDECAR,
        ROOT / "scripts/gtdb_ground.py",
        ROOT / "uv.lock",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "scripts/adhoc/apply_code006_gtdb_status_20261115.py",
        ROOT / "scripts/adhoc/check_code006_gtdb_canary_20261115.sh",
        Path(__file__),
        ROOT / "reviews/structured" / PREVIOUS / "review.yaml",
        ROOT / "reviews/structured" / PREVIOUS / "review.md",
    ]
    paths.extend(ROOT / name for name in staged["inputs"] if name != TARGET)
    paths.append(STATE / "strict-001.tsv")
    completion_prefix = STATE / "canary-completion-001"
    completion_paths = [
        Path(str(completion_prefix) + suffix)
        for suffix in (".command.txt", ".head.txt", ".log", ".exit")
    ]
    if (
        completion_paths[1].read_text().strip() != REVISION
        or completion_paths[3].read_text().strip() != "1"
        or sha(completion_paths[2])
        != "fe98dd5ac01f22ec3febff9fe5e6253100d6d02992c0aa6978bcc4882bb4f938"
    ):
        raise ValueError("actual outstanding-grounding diagnostic differs")
    paths.extend(completion_paths)
    checks, evidence = [], []
    accessed = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    for gate in GATES:
        prefix = STATE / f"canary-run-{gate}-001"
        artifacts = [
            Path(str(prefix) + suffix)
            for suffix in (
                ".command.txt",
                ".log",
                ".exit",
                ".start.txt",
                ".finished.txt",
                ".log.sha256",
            )
        ]
        if artifacts[2].read_text().strip() != "0" or not artifacts[1].stat().st_size:
            raise ValueError("required native gate did not pass with retained output")
        if artifacts[5].read_text().split()[0] != sha(artifacts[1]):
            raise ValueError("native gate log hash differs")
        expected_recipe = {
            "schema": "validate",
            "strict": "validate-strict",
            "gtdb": "validate-gtdb",
            "domain": "validate-gtdb-domain",
            "scalars": "validate-scalars",
            "history": "validate-history",
        }[gate]
        expected_target = (
            "history/records/Acidic_Nitrification_Minimal_Consortium"
            if gate == "history"
            else TARGET
        )
        expected_command = [
            "just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            expected_recipe,
            expected_target,
        ]
        if gate == "strict":
            expected_command.extend(["--out", ".temp/gtdb-code006-20261115/strict-001.tsv"])
        if shlex.split(artifacts[0].read_text()) != expected_command:
            raise ValueError("native gate command scope differs")
        if artifacts[3].read_text().splitlines()[:2] != [REVISION, "Python 3.13.2"]:
            raise ValueError("native gate runtime/revision differs")
        paths.extend(artifacts)
        checks.append(
            {
                "check_id": gate,
                "name": gate,
                "status": "passed",
                "required": True,
                "summary": "Actual native M5 command completed with exit0 and nonempty retained log.",
                "target_ids": [IDENTITY],
                "command": artifacts[0].read_text().strip(),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [gate],
                "scope_note": "One record; history gate validates its append-only history directory. This is not corpus QC or scientific evidence validation.",
            }
        )
        evidence.append(
            {
                "evidence_id": gate,
                "kind": "validation",
                "reference": str(artifacts[1].relative_to(ROOT)),
                "accessed_at": accessed,
                "support": "supports",
                "summary": checks[-1]["summary"],
            }
        )
    checks.append(
        {
            "check_id": "completion",
            "name": "Native outstanding-grounding guards",
            "status": "failed",
            "required": True,
            "summary": "Both native guards fail on the single new NOT_ATTEMPTED Mycobacterium entry; status correction alone is not a complete QC repair.",
            "target_ids": [IDENTITY],
            "command": completion_paths[0].read_text().strip(),
            "exit_code": 1,
            "expected_exit_code": 0,
            "evidence_ids": ["completion"],
            "scope_note": "Two actual corpus-level tests; their retained failures specifically identify this canary's single outstanding entry.",
        }
    )
    evidence.append(
        {
            "evidence_id": "completion",
            "kind": "validation",
            "reference": str(completion_paths[2].relative_to(ROOT)),
            "accessed_at": accessed,
            "support": "refutes",
            "summary": checks[-1]["summary"],
        }
    )
    targets = [
        {
            "target_id": IDENTITY,
            "path": TARGET,
            "selector": "taxonomy[1].taxon_term.gtdb_grounding_status",
            "label": "Current crosswalk computability at the existing Mycobacterium genus",
            "kind": "maintained",
            "ownership_note": "CommunityMech owns record status; native gtdb_ground.py owns classifier semantics; pinned kg-microbe crosswalk supplies mapping rows.",
        }
    ]
    target_file = STATE / f"assessment-targets-{args.attempt}.json"
    with target_file.open("x") as stream:
        json.dump({"targets": targets}, stream, indent=2)
    command = [sys.executable, "scripts/record_review.py", "inspect", "--targets", str(target_file)]
    for path in paths:
        command.extend(("--input", str(path.relative_to(ROOT))))
    capture = subprocess.check_output(command, cwd=ROOT)
    inspection = json.loads(capture)
    if inspection["source"]["git_revision"] != REVISION:
        raise ValueError("unexpected native inspection revision")
    with (STATE / f"assessment-inspection-{args.attempt}.json").open("xb") as stream:
        stream.write(capture)
    for identifier, kind, path, summary in (
        (
            "application",
            "record_content",
            applied_path.relative_to(ROOT).as_posix(),
            "Exact reviewed one-status candidate was natively validated and persisted on M5; raw receipt binds before/after bytes.",
        ),
        (
            "mapping",
            "database",
            str((STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz").relative_to(ROOT)),
            "Exact761 crosswalk supports current computability at the already-declared genus. It does not identify the paper's species or genome.",
        ),
        (
            "previous",
            "prior_review",
            f"reviews/structured/{PREVIOUS}/review.yaml",
            "Preserved November5 full scientific review and its unknown-species/genome, source-access and mechanism limits. No finding is closed by this diagnostic.",
        ),
    ):
        evidence.append(
            {
                "evidence_id": identifier,
                "kind": kind,
                "reference": path,
                "accessed_at": accessed,
                "support": "context_only",
                "summary": summary,
            }
        )
    finished = datetime.now(timezone.utc)
    doc = {
        "schema_version": "1.0.0",
        "review_id": finished.strftime("%Y%m%dT%H%M%SZ") + "-gtdb-status-000434-canary",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "One-record diagnostic canary: current Mycobacterium GTDB computability",
        "started_at": applied["created_at"].replace("+00:00", "Z"),
        "finished_at": finished.isoformat().replace("+00:00", "Z"),
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored diagnosis and application; separate root read-only review accepted the candidate, guard and source boundary before application.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": False,
        "summary": "One status now describes current native resolver computability, with exact reviewed bytes, actual application receipt, native sidecar and six passing scoped gates. The two native outstanding-grounding tests still fail; this diagnostic is not a complete QC repair. No GTDB block or biological identity changed. Historical scientific uncertainty and the wider2848/2849 backlog remain unresolved.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "Only current status computability and its guarded application/provenance were assessed; not the full biological record.",
            "selection": "First named status discrepancy, independently accepted one-record canary; not a random sample.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [IDENTITY],
            "exclusions": [
                {
                    "target": "Other548records and all biological claims of000434",
                    "reason": "No broader scientific or corpus reproducibility assessment is claimed by this diagnostic canary.",
                }
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "computability",
                "area": "grounding",
                "topic": "Current status at fixed genus identity",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["mapping", "application", "gtdb"],
                "summary": "NOT_ATTEMPTED means the current native resolver can produce a genus block that is absent. It does not mean no curator historically tried, or that a source species/genome is resolved. The candidate contains no added GTDB classification.",
            },
            {
                "assessment_id": "preservation",
                "area": "provenance",
                "topic": "Unchanged biological payload and immutable review",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["application", "previous", "history", "strict"],
                "summary": "Exact bounded application changes one status and appends one native inline event. The prior source organism/strain, mechanisms, quotations and saved scientific review remain unchanged; the new external native sidecar records the scope and actual receipt.",
            },
        ],
        "findings": [
            {
                "finding_id": "outstanding-genus-grounding",
                "issue_key": "gtdb-status-2848",
                "category": "grounding",
                "severity": "major",
                "status": "open",
                "certainty": "confirmed",
                "title": "Current computability still requires a grounded or evidence-backed held disposition",
                "description": "The native resolver can produce a same-genus Mycobacterium correspondence, but this diagnostic added no block. Both maintained completion tests reject the resulting single NOT_ATTEMPTED entry. A separately reviewed database correspondence must preserve the historical unknown species/genome and mechanism limits; no arbitrary hold or changed test baseline is justified.",
                "target_ids": [IDENTITY],
                "field_paths": ["taxonomy[1].taxon_term"],
                "evidence_ids": ["completion", "mapping", "previous"],
                "ownership_note": "CommunityMech owns current grounding metadata; issue2848 retains the broader status/classifier discrepancy work.",
                "external_issues": ["https://github.com/CultureBotAI/CommunityMech/issues/2848"],
            }
        ],
        "actions": [
            {
                "action_id": "review-genus-correspondence",
                "finding_ids": ["outstanding-genus-grounding"],
                "target_ids": [IDENTITY],
                "description": "Stage one actual native genus correspondence with the exact pinned source and original scientific limits for independent review before application.",
                "ownership_note": "CommunityMech owns the single target taxonomy block and its native grounding writer; no upstream source or historical review change is proposed.",
                "acceptance_checks": [
                    "Same-genus correspondence is source-backed without a species/genome claim.",
                    "Native completion and scoped validation gates pass after a separately guarded application, with actual receipt and append-only history.",
                ],
            }
        ],
        "limitations": [
            "Diagnostic-only assessment; no new primary-paper review, source acquisition, reference sweep, ontology relabelling or scientific approval.",
            "Six scoped gates and this one-record canary do not establish passing full QC or resolve the original125-file status/candidate findings and three stored-block findings.",
            "Executed on the isolated M5 checkout with native Python3.13.2 at committed956d00c6 plus the explicitly retained untracked wrapper/builder hashes; classifier/source revision remains c9-equivalent.",
            "No existing issue or historical scientific finding is closed; subsequent batch inclusion must preserve manual withholding and prior scientific limits.",
        ],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": PREVIOUS,
                "relationship": "Preserved historical scientific assessment; this is only an additive current-status/provenance diagnostic.",
            }
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/issues/2848",
            "https://github.com/CultureBotAI/CommunityMech/issues/2849",
            "https://github.com/CultureBotAI/CommunityMech/pull/2853",
        ],
    }
    print(json.dumps(doc, indent=2))


if __name__ == "__main__":
    main()
