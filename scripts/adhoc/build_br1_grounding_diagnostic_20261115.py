"""Build a scoped BR1 native diagnostic from actual M5 evidence, #2849, 2026-11-15.

Inputs: exact applied record, authority snapshots, native gates and actual history.
Outputs: exclusive private inspection/review candidate and native route JSON.
No canonical/source writes; the native review validator/saver remains separate.
"""

import argparse
import hashlib
import importlib.util
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from check_br1_grounding_20261115 import (  # noqa: E402
    AFTER,
    BEFORE,
    HISTORY,
    RECIPES,
    STATE,
    TARGET,
)
from curate_br1_grounding_20261115 import REPORT, assert_scope  # noqa: E402

IDENTITY = "CommunityMech:000531"
LEDGER = "reports/causal_graph_review/decisions/20261108-stage2-five-records-batch144.yaml"
TABLE = STATE / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path, data):
    with path.open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", required=True)
    parser.add_argument("--gate-attempt", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--applied-receipt", type=Path, required=True)
    parser.add_argument("--expected-receipt-sha256", required=True)
    parser.add_argument("--staging-receipt", type=Path, required=True)
    args = parser.parse_args()
    if not args.attempt.isdigit() or not args.gate_attempt.isdigit():
        raise ValueError("numeric exclusive attempts required")
    output = STATE / ("diagnostic-" + args.attempt)
    if output.exists():
        raise ValueError("prior diagnostic must remain immutable")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if revision != args.expected_revision:
        raise ValueError("exact actual M5 revision required")
    applied_path, staged_path = args.applied_receipt.resolve(), args.staging_receipt.resolve()
    if any(not path.is_relative_to(STATE) for path in (applied_path, staged_path)):
        raise ValueError("retained private receipts required")
    if sha(applied_path) != args.expected_receipt_sha256 or sha(ROOT / TARGET) != AFTER:
        raise ValueError("actual accepted application differs")
    applied = json.loads(applied_path.read_bytes())
    if (
        applied["applied"] is not True
        or applied["execution_revision"] != revision
        or applied["target"] != TARGET
        or applied["before_sha256"] != BEFORE
        or applied["after_sha256"] != AFTER
        or sha(staged_path) != applied["reviewed_staging_receipt_sha256"]
    ):
        raise ValueError("actual reviewed application chain differs")
    before_path = applied_path.with_name("before.yaml")
    if sha(before_path) != BEFORE or sha(staged_path.with_name("candidate.yaml")) != AFTER:
        raise ValueError("actual predecessor/candidate differs")
    assert_scope(
        yaml.safe_load(before_path.read_bytes()), yaml.safe_load((ROOT / TARGET).read_bytes())
    )
    paths = {
        ROOT / TARGET,
        applied_path,
        before_path,
        staged_path,
        staged_path.with_name("candidate.yaml"),
        ROOT / LEDGER,
        Path(__file__),
        ROOT / "scripts/adhoc/check_br1_grounding_20261115.py",
        TABLE,
    }
    for name, expected in applied["inputs"].items():
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT) or sha(path) != expected:
            raise ValueError("reviewed source changed: " + name)
        paths.add(path)
    checks, evidence, sidecars = [], [], {}
    started = now()
    for gate, recipe in RECIPES.items():
        directory = STATE / f"canary-run-{gate}-{args.gate_attempt}"
        proof = json.loads((directory / "receipt.json").read_bytes())
        log = directory / "native.log"
        if (
            proof["revision"] != revision
            or proof["plan"] is not False
            or proof["exit_code"] != 0
            or (directory / "native.exit").read_text().strip() != "0"
            or proof["log_sha256"] != sha(log)
            or proof["log_bytes"] != log.stat().st_size
            or not log.stat().st_size
            or proof["execution_inputs_unchanged"] is not True
            or proof["inputs"].get(str(ROOT / TARGET)) != AFTER
        ):
            raise ValueError("required actual native gate did not pass: " + gate)
        command = ["just", "--verbose", "--no-dotenv", "--color", "never", recipe]
        if gate == "new-history":
            if proof["command"][:6] != command or len(proof["new_history_sidecars"]) != 1:
                raise ValueError("actual native sidecar generation differs")
            sidecars = proof["new_history_sidecars"]
        else:
            command.append(HISTORY if gate == "history" else TARGET)
            if gate == "strict":
                command.extend(["--out", str((directory / "strict.tsv").relative_to(ROOT))])
            if proof["command"] != command:
                raise ValueError("native command scope differs")
        for name, expected in proof["inputs"].items():
            path = Path(name)
            if sha(path) != expected:
                raise ValueError("gate input changed: " + name)
            if path.is_relative_to(ROOT):
                paths.add(path)
        paths.update(directory.iterdir())
        evidence.append(
            {
                "evidence_id": gate,
                "kind": "validation",
                "reference": str(log.relative_to(ROOT)),
                "accessed_at": started,
                "support": "supports",
                "summary": "Actual native M5 command completed with exit 0 on the exact corrected record; retained nonempty hash-bound output.",
            }
        )
        checks.append(
            {
                "check_id": gate,
                "name": recipe,
                "status": "passed",
                "required": True,
                "summary": evidence[-1]["summary"],
                "target_ids": [IDENTITY],
                "command": shlex.join(proof["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [gate],
                "scope_note": "One record only; native new-history creates the sidecar. No corpus or full scientific approval.",
            }
        )
    for name, expected in sidecars.items():
        path = ROOT / name
        if not name.startswith(HISTORY + "/") or sha(path) != expected:
            raise ValueError("native history sidecar differs")
        paths.add(path)
    if sha(TABLE) != TABLE_SHA:
        raise ValueError("exact retained crosswalk required")
    native_path = ROOT / "scripts/gtdb_ground.py"
    spec = importlib.util.spec_from_file_location("br1_native_gtdb", native_path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    rows = native.collect_rows(
        TABLE, {"1070896"}, set(native.lookup_keys("Microbacterium sp. BR1")), set()
    )
    measured = native.resolve_target("1070896", "Microbacterium sp. BR1", *rows)
    if measured is not None:
        raise ValueError("native BR1 route changed; reassessment required")
    output.mkdir()
    write_json(
        output / "native-route.json",
        {
            "revision": revision,
            "target": TARGET,
            "record_sha256": AFTER,
            "classifier_sha256": sha(native_path),
            "crosswalk_sha256": sha(TABLE),
            "native_result": measured,
            "curated": True,
            "basis": "Exact NCBI BR1 assembly/BioSample identity and explicit GTDB R220 genome history, independently verified in the bound source proof.",
            "majority_fraction_asserted": False,
            "total_genomes_asserted": False,
            "scope": "Native absence alone is not evidence of the chosen species; the independent exact-genome authority chain supplies that evidence.",
        },
    )
    paths.update({native_path, output / "native-route.json"})
    targets = [
        {
            "target_id": IDENTITY,
            "path": TARGET,
            "selector": "taxonomy[0].taxon_term.gtdb_classification; description GTDB identifier",
            "label": "BR1 exact-genome GTDB grounding and matching description identifier",
            "kind": "maintained",
            "ownership_note": "CommunityMech owns the BR1 record. This review is scoped to the corrected stock/genome correspondence and actual application, not full-record scientific claims.",
        }
    ]
    write_json(output / "targets.json", {"targets": targets})
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(output / "targets.json"),
    ]
    for path in sorted(paths):
        command.extend(["--input", str(path.relative_to(ROOT))])
    captured = subprocess.check_output(command, cwd=ROOT)
    inspection = json.loads(captured)
    if inspection["source"]["git_revision"] != revision:
        raise ValueError("native inspection revision differs")
    (output / "inspection.json").write_bytes(captured)
    extra = [
        (
            "assembly",
            "database",
            "https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_002812725.1/dataset_report",
            "reports[0].accession/paired_accession/organism/assembly_info.biosample",
            "supports",
            "The exact assembly pair GCF_002812725.1 / GCA_002812725.1 binds NCBITaxon:1070896, strain BR1 and SAMN07351343.",
        ),
        (
            "history-r220",
            "database",
            "https://gtdb-api.ecogenomic.org/genome/GCF_002812725.1/taxon-history",
            "release=R220; d,p,c,o,f,g,s",
            "supports",
            "Explicit R220 history assigns this same assembly to Microbacterium sp002812725 and the retained full lineage. The current GTDB card independently agrees; software version is not treated as a release.",
        ),
        (
            "source-proof",
            "database",
            REPORT,
            "assembly/r220_lineage/crosswalk/recommendation",
            "supports",
            "Hash-bound source inspection preserves exact authority snapshots and primary paper identity. The CJ77 crosswalk population and GTDB cluster count are not BR1 mapping denominators; both optional count fields are omitted.",
        ),
        (
            "native-route",
            "validation",
            str((output / "native-route.json").relative_to(ROOT)),
            "native_result=null/curated/basis",
            "context_only",
            "The same exact761 crosswalk and unchanged native resolver still return no BR1 mapping. The independently supported genome classification is explicitly curated; a native None alone does not establish its species.",
        ),
        (
            "application",
            "record_content",
            str(applied_path.relative_to(ROOT)),
            "applied/before_sha256/after_sha256/inputs",
            "supports",
            "Actual guarded M5 replacement persisted only the accepted GTDB block, exact description token and native inline event; sidecar provenance and all before/after inputs are bound.",
        ),
        (
            "prior",
            "prior_review",
            LEDGER,
            "records[id=CommunityMech:000531]",
            "context_only",
            "The original batch144 phenotype, one-node/zero-edge and discussion assessment is preserved as historical evidence; this correction does not repeat or upgrade that scientific review.",
        ),
        (
            "paper",
            "primary_source",
            "https://europepmc.org/articles/PMC13472149",
            "Introduction refs7,8,11; Methods stock identities",
            "supports",
            "The inspected source distinguishes the separately cited Microbacterium lacus soil isolate from BR1 and identifies BR1 in the experiment. It does not itself supply a GTDB species assignment.",
        ),
    ]
    for identifier, kind, reference, locator, support, summary in extra:
        evidence.append(
            {
                "evidence_id": identifier,
                "kind": kind,
                "reference": reference,
                "locator": locator,
                "accessed_at": started,
                "support": support,
                "summary": summary,
            }
        )
    assessments = [
        (
            "stock-genome",
            "grounding",
            "Exact BR1 assembly and release-specific lineage",
            ["assembly", "history-r220", "source-proof", "gtdb", "paper"],
            "Correct Microbacterium lacus to the explicit R220 GTDB placeholder Microbacterium sp002812725 through exact assembly, strain, NCBI taxon and BioSample identity. Preserve the NCBI stock; label difference is not a claim of formal species renaming.",
        ),
        (
            "population",
            "grounding",
            "Independent curated mapping and omitted crosswalk counts",
            ["source-proof", "native-route", "gtdb", "domain"],
            "No exact BR1 crosswalk row exists in the inspected table. The chosen classification is justified by independent exact-genome authorities, not by bypassing native None. Do not infer majority_fraction or total_genomes from the card cluster size, CJ77 rows or a single assembly.",
        ),
        (
            "bounded-application",
            "provenance",
            "Actual application and immutable predecessor",
            ["application", "new-history", "history", "strict", "prior"],
            "Only the reviewed GTDB block, one exact opening-description identifier and one appended inline event differ. Native append-only sidecar and actual seven validation gates are retained; all biological claims, notes, quotations, graph and prior history are preserved.",
        ),
    ]
    doc = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-br1-gtdb-diagnostic",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "BR1 exact-genome GTDB grounding: scoped M5 diagnostic",
        "started_at": started,
        "finished_at": now(),
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored the source proof and correction; parent independently reviewed actual authority bytes, candidate semantics and guarded writer before application.",
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": False,
        "summary": "Scoped stock/genome correspondence and actual application assessment only. Exact BR1 assembly identity plus explicit GTDB R220 history support the corrected placeholder species; native absence and unrelated population counts are not substituted for that source evidence. No full-record scientific approval is claimed.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "One GTDB block, matching description identifier, source identity and bounded application/provenance.",
            "selection": "BR1 is one of three actual stored-block discrepancies under issue2849; its independent exact-genome route was reviewed before the isolated one-record canary.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [IDENTITY],
            "exclusions": [
                {
                    "target": "All BR1 experimental claims, graph and discussion; other records and corpus",
                    "reason": "Preserved existing claims were not newly reviewed; separate retained batch144 review and corpus checks have their own scope.",
                }
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": ident,
                "area": area,
                "topic": topic,
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ids,
                "summary": summary,
            }
            for ident, area, topic, ids, summary in assessments
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "This is a scoped technical/provenance assessment with scientific_review:false, not a new whole-record scientific review or closure of the broader issue2849.",
            "The GTDB release assertion is from the explicit R220 API taxon-history entry, not an independently downloaded release taxonomy file or a recomputed ANI analysis.",
            "No crosswalk population counts are asserted for BR1. The placeholder species is a genome classification, not a formal nomenclatural renaming.",
            "Seven native scoped validation commands and one history scaffolder ran on this corrected record. No corpus QC, claim-level reference comparison, generated documentation or full-record quality metric is certified by this diagnostic.",
            "All previous biological content remains unchanged except the exact GTDB identifier in the opening description; historical scientific findings remain their original assessments.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/issues/2849",
            "https://github.com/CultureBotAI/CommunityMech/pull/2856",
        ],
    }
    write_json(output / "review.json", doc)
    print(
        json.dumps(
            {
                "review": str((output / "review.json").relative_to(ROOT)),
                "sha256": sha(output / "review.json"),
                "source_inputs": len(doc["source"]["inputs"]),
            }
        )
    )


if __name__ == "__main__":
    main()
