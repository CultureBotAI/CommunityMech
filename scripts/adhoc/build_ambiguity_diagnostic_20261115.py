"""Build the actual M5 ambiguity canary diagnostic, #2848, 2026-11-15.

Inputs: exact application, primary article, historical ledger and eight native
receipts. Outputs: exclusive private native inspection/recomputation/review draft.
Native validate/save is separate. No canonical changes or scientific approval.
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

import apply_ambiguity_status_canary_20261115 as apply_guard
import check_ambiguity_canary_20261115 as check
import stage_ambiguity_status_canary_20261115 as stage
import yaml
from defusedxml import ElementTree as SafeET

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-ambiguity-20261115"
IDENTITY = "CommunityMech:000546"
SIDECAR = check.HISTORY + "/2026-11-15T060616Z-codex-7ba0d3.yaml"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path, data):
    with path.open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


def inspect_captured(captures, command, output):
    """Bind native inspection to every assessed repository byte snapshot."""
    inspection_raw = subprocess.check_output(command, cwd=ROOT)
    (output / "inspection.json").write_bytes(inspection_raw)
    inspection = json.loads(inspection_raw)
    if inspection["source"]["git_revision"] != check.REVISION:
        raise ValueError("native inspection revision differs")
    expected = {
        str(path.relative_to(ROOT)): digest(raw)
        for path, raw in captures.items()
        if path.is_relative_to(ROOT)
    }
    rows = inspection["source"]["inputs"]
    observed = {row["path"]: row["sha256"] for row in rows}
    if len(rows) != len(observed) or observed != expected:
        raise ValueError("native inspection differs from captured assessment inputs")
    return inspection


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", required=True)
    args = parser.parse_args()
    if not args.attempt.isdigit() or check.head() != check.REVISION:
        raise ValueError("numeric attempt and actual M5 execution revision required")
    output = STATE / f"ambiguity-diagnostic-{args.attempt}"
    if output.exists() or output.is_symlink():
        raise ValueError("preserve earlier diagnostic drafts")
    started = now()
    captures = {}

    def capture(path, expected=None):
        path = Path(path)
        if path not in captures:
            captures[path] = path.read_bytes()
        raw = captures[path]
        if expected is not None and digest(raw) != expected:
            raise ValueError("source hash differs: " + str(path))
        return raw

    after_raw = capture(ROOT / check.TARGET, check.AFTER)
    before_raw = capture(check.APPLIED.with_name("before.yaml"), check.BEFORE)
    applied = json.loads(capture(check.APPLIED, check.APPLIED_SHA))
    if (
        applied["applied"] is not True
        or applied["execution_revision"] != check.REVISION
        or applied["before_sha256"] != check.BEFORE
        or applied["after_sha256"] != check.AFTER
    ):
        raise ValueError("actual accepted application required")
    for relative, expected in applied["inputs"].items():
        if relative == check.TARGET:
            if expected != check.BEFORE:
                raise ValueError("pre-application canonical binding differs")
            continue
        path = (ROOT / relative).resolve()
        path.relative_to(ROOT)
        capture(path, expected)
    candidate = ROOT / applied["candidate_path"]
    capture(candidate, check.AFTER)
    staged = json.loads(
        capture(candidate.with_name("receipt.json"), applied["staging_receipt_sha256"])
    )
    before, after = yaml.safe_load(before_raw), yaml.safe_load(after_raw)
    apply_guard.verify_candidate(before, after, staged)
    ledger_raw = capture(ROOT / stage.LEDGER)
    old_row = next(row for row in yaml.safe_load(ledger_raw)["records"] if row["id"] == IDENTITY)
    if old_row["record_sha256"] != check.BEFORE:
        raise ValueError("historical scientific ledger differs")
    capture(ROOT / SIDECAR)
    for path in (
        Path(__file__),
        Path(check.__file__),
        Path(stage.__file__),
        Path(apply_guard.__file__),
    ):
        capture(path)
    evidence, checks = [], []
    for gate, recipe in check.RECIPES.items():
        prefix = STATE / f"ambiguity-canary-run-{gate}-001"
        receipt = json.loads(capture(prefix / "receipt.json"))
        log = capture(prefix / "native.log", receipt["log_sha256"])
        if (
            receipt["revision"] != check.REVISION
            or receipt["plan"] is not False
            or receipt["exit_code"] != 0
            or capture(prefix / "native.exit") != b"0\n"
            or receipt["log_bytes"] != len(log)
            or not log
        ):
            raise ValueError("required actual native gate did not pass: " + gate)
        command = ["just", "--verbose", "--no-dotenv", "--color", "never", recipe]
        if gate == "new-history":
            if (
                receipt["command"][:6] != command
                or receipt["history_created"] != {SIDECAR: digest(captures[ROOT / SIDECAR])}
                or SIDECAR not in log.decode()
            ):
                raise ValueError("actual single native sidecar differs")
        else:
            command.append(check.HISTORY if gate == "history" else check.TARGET)
            if gate == "strict":
                command.extend(["--out", str((prefix / "strict.tsv").relative_to(ROOT))])
            if receipt["command"] != command:
                raise ValueError("native gate scope differs")
        if receipt["inputs"].get(str(ROOT / check.TARGET)) != check.AFTER:
            raise ValueError("gate did not bind actual corrected record")
        for name, expected in receipt["inputs"].items():
            capture(Path(name), expected)
        for path in prefix.iterdir():
            if path.is_file():
                capture(path)
        evidence.append(
            {
                "evidence_id": gate,
                "kind": "validation",
                "reference": str((prefix / "native.log").relative_to(ROOT)),
                "accessed_at": started,
                "support": "supports",
                "summary": "Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record.",
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
                "command": shlex.join(receipt["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [gate],
                "scope_note": "One record; history validates its complete sidecar directory. Not corpus QC or scientific evidence validation.",
            }
        )
    capture(stage.TABLE, stage.TABLE_SHA)
    capture(stage.NATIVE, stage.NATIVE_SHA)
    spec = importlib.util.spec_from_file_location("ambiguity_native_recompute", stage.NATIVE)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    term = after["taxonomy"][0]["taxon_term"]
    label, identifier = term["term"]["label"], term["term"]["id"]
    rows = native.collect_rows(stage.TABLE, {"853"}, set(native.lookup_keys(label)), set())
    result = native.resolve_target("853", label, *rows)
    status, options = native.classify_status(
        Path(check.TARGET).name,
        identifier,
        label,
        False,
        *rows,
        preferred=term.get("preferred_term"),
    )
    if (
        result is None
        or result.get("ambiguous") is not True
        or result["gtdb_options"] != stage.OPTIONS
        or status != "AMBIGUOUS"
        or options != stage.OPTIONS
        or term["gtdb_grounding_status"] != status
        or term["gtdb_candidates"] != options
    ):
        raise ValueError("native recomputation does not reproduce complete ambiguity")
    article = SafeET.fromstring(capture(stage.ARTICLE, stage.ARTICLE_SHA))
    methods = article.find(".//sec[@id='sec2dot1-microorganisms-14-01812']")
    if methods is None or "Faecalibacterium prausnitzii A2-165 (JCM31915)" not in "".join(
        methods.itertext()
    ):
        raise ValueError("inspected primary study-stock identity differs")
    output.mkdir()
    write_json(
        output / "native-route.json",
        {
            "execution_revision": check.REVISION,
            "target": check.TARGET,
            "record_sha256": check.AFTER,
            "classifier_sha256": stage.NATIVE_SHA,
            "crosswalk_sha256": stage.TABLE_SHA,
            "descriptor": term["term"],
            "result": result,
            "status": status,
            "candidates": options,
            "matches_stored_state": True,
            "scope": "Existing NCBI species descriptor only; alternatives are not inferred identities of A2-165/JCM31915. No strain/genome nomenclature resolution.",
        },
    )
    capture(output / "native-route.json")
    targets = [
        {
            "target_id": IDENTITY,
            "path": check.TARGET,
            "selector": "taxonomy[0].taxon_term.gtdb_grounding_status; taxonomy[0].taxon_term.gtdb_candidates",
            "label": "A2-165 monoculture existing-species-descriptor ambiguity",
            "kind": "maintained",
            "ownership_note": "CommunityMech owns the stored status/candidate fields; the unchanged native classifier computes the full ambiguity set for the existing NCBI853 descriptor. Exact study-strain species/genome identity is not inferred.",
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
    for path in sorted(captures):
        if path.is_relative_to(ROOT):
            command.extend(["--input", str(path.relative_to(ROOT))])
    inspection = inspect_captured(captures, command, output)
    for identifier, kind, reference, locator, support, summary in (
        (
            "native-route",
            "database",
            str((output / "native-route.json").relative_to(ROOT)),
            "result/status/candidates",
            "supports",
            "Actual native recomputation against exact761 returns AMBIGUOUS and all three GTDB alternatives for NCBI853/Faecalibacterium prausnitzii. The stored list matches in full; no candidate is selected as a strain identity.",
        ),
        (
            "primary-stock",
            "primary_source",
            "https://doi.org/10.3390/microorganisms14081812",
            "Methods2.1, sec2dot1-microorganisms-14-01812; retained PMC13515949 XML",
            "context_only",
            "The inspected primary Methods names 'Faecalibacterium prausnitzii A2-165 (JCM31915)'. This supports retaining the source stock and name, not choosing a GTDB species. The bibliography also cites a2024 paper naming A2-165 Faecalibacterium duncaniae; independent stock/genome nomenclature adjudication is outside this correction.",
        ),
        (
            "actual-application",
            "record_content",
            str(check.APPLIED.relative_to(ROOT)),
            "applied/before_sha256/after_sha256/inputs",
            "supports",
            "One actual M5 guarded apply persisted the exact independently accepted candidate. Captured pre-apply canonical bytes remain in before.yaml; the current canonical hash is separately bound to the accepted after state.",
        ),
        (
            "historical-science",
            "prior_review",
            stage.LEDGER,
            "records[id=CommunityMech:000546], node_decisions/source_backed_gaps",
            "context_only",
            "The original batch146 ledger remains unchanged. Its one-node/zero-arrow monoculture assessment,5 graph evidence snippets and unresolved metabolic-flux gap are preserved, not newly certified. Its historical UNRESOLVED wording describes the predecessor state.",
        ),
    ):
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
    doc = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-faecalibacterium-ambiguity-diagnostic",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "A2-165 monoculture: native species-descriptor ambiguity diagnostic",
        "started_at": started,
        "finished_at": now(),
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored the scoped correction; root independently reviewed primary-source scope, local and exact M5 candidates, guarded application and native gate wrapper before execution.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": False,
        "summary": "One existing species descriptor now records AMBIGUOUS and all three native GTDB alternatives. Actual guarded M5 application, append-only history and eight required native commands are bound to their evidence. No GTDB species is assigned to A2-165/JCM31915 and no whole-record scientific approval is claimed.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "Status/candidate computability and actual application provenance only.",
            "selection": "First end-to-end canary for the15 pure ambiguous records within the30-record assigned ambiguity lane; other records have not been applied by this canary.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [IDENTITY],
            "exclusions": [
                {
                    "target": "Study-strain species/genome identity and all experimental, ecological, cultivation or mechanism claims",
                    "reason": "Existing content is preserved; independent full scientific and nomenclature reassessment is outside this diagnostic.",
                },
                {
                    "target": "Other29 assigned records and corpus",
                    "reason": "Metadata intake is not a current classifier result, application, or scientific review.",
                },
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "native-ambiguity",
                "area": "grounding",
                "topic": "Complete ambiguity on the unchanged species descriptor",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["native-route", "gtdb", "primary-stock"],
                "summary": "NCBI853 remains the declared descriptor. Native761 yields three alternatives; AMBIGUOUS plus the complete list reproduces that result without a grounding block or a selected stock species.",
            },
            {
                "assessment_id": "actual-provenance",
                "area": "provenance",
                "topic": "Actual guarded write and append-only history",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": [
                    "actual-application",
                    "new-history",
                    "history",
                    "strict",
                    "historical-science",
                ],
                "summary": "The accepted after bytes persist on M5. Full native inline event reconstruction, captured source checks and the validated writer guarded replacement. Existing sidecars and the immutable historical ledger remain unchanged; exactly one new sidecar records the bounded correction.",
            },
            {
                "assessment_id": "stock-boundary",
                "area": "scope",
                "topic": "Species-descriptor alternatives do not resolve study-stock nomenclature",
                "outcome": "supported",
                "target_ids": [IDENTITY],
                "evidence_ids": ["primary-stock", "historical-science", "native-route"],
                "summary": "The study's A2-165/JCM31915 designation, biological content and quotations are preserved. Alternative species names from a species-level crosswalk do not identify this stock; the duncaniae naming question remains outside the correction. Historical assay conclusions and knowledge gaps are not newly certified.",
            },
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Diagnostic-only partial scope. No full scientific review, study-strain assembly analysis, selected GTDB species, higher-priority issue closure or campaign completion is claimed.",
            "The exact crosswalk SHA761 is pinned; file time does not establish release/build provenance. Native results describe the existing species-level input, not strain-level classification.",
            "Eight native scoped commands passed on M5 Python3.13.2 at4a5999d5, including seven validation gates and one sidecar creation. References, corpus QC and generated pages are not claimed passed by this diagnostic.",
            "Full-record completeness/quality scores are not recomputed for this narrow status/provenance assessment. Deterministic validation does not establish scientific correctness.",
            "The original local301 stage001 and M5 stage001 remain preserved. A fresh M5 stage002 used the same published4a5999d5 launcher and avoided overwriting the local predecessor evidence namespace.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/issues/2848",
            "https://github.com/CultureBotAI/CommunityMech/issues/2861",
            "https://github.com/CultureBotAI/CommunityMech/issues/2865",
            "https://github.com/CultureBotAI/CommunityMech/issues/2864",
            "https://github.com/CultureBotAI/CommunityMech/pull/2804",
        ],
    }
    if check.head() != check.REVISION or any(
        path.read_bytes() != raw for path, raw in captures.items()
    ):
        raise ValueError("source changed before diagnostic publication")
    write_json(output / "review.json", doc)
    print(
        json.dumps(
            {
                "review": str((output / "review.json").relative_to(ROOT)),
                "sha256": digest((output / "review.json").read_bytes()),
                "source_inputs": len(doc["source"]["inputs"]),
            }
        )
    )


if __name__ == "__main__":
    main()
