"""Admit explicitly pinned technical GTDB successors without revising science.

#2848, 2026-11-15. Callers own an exact target -> baseline/manifest-hash allowlist.
Inputs are immutable Git predecessor bytes and public saved-review/application/
source/gate artifacts. No writes, acquisition, fresh taxonomy classification or
scientific approval. Existing fixed 552/553/555 contracts remain independent.
"""

import copy
import hashlib
import json
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.record_review import render_markdown, validate_review  # noqa: E402

NATIVE = "scripts/gtdb_ground.py"
NATIVE_SHA = "0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175"
ENGINE = "scripts/adhoc/gtdb_batch_curation_20261115.py"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "scalars": "validate-scalars",
    "history": "validate-history",
    "new-history": "new-history",
    "terms": "validate-terms",
}
FIELDS = ("gtdb_classification", "gtdb_grounding_status", "gtdb_candidates")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class Admission:
    current_sha256: str
    historical_bytes: bytes
    changed: bool


class Artifacts:
    def __init__(self, root):
        self.root = root.resolve()
        self.captured = {}

    def read(self, item):
        name = item["path"]
        relative = Path(name)
        path = (self.root / relative).resolve()
        require(
            not relative.is_absolute()
            and ".." not in relative.parts
            and path.is_relative_to(self.root)
            and not (self.root / relative).is_symlink(),
            "unsafe proof artifact path",
        )
        require(re.fullmatch(r"[0-9a-f]{64}", item["sha256"]), "exact SHA256 required")
        if path not in self.captured:
            self.captured[path] = path.read_bytes()
        raw = self.captured[path]
        require(digest(raw) == item["sha256"], "proof artifact hash differs: " + name)
        return raw

    def verify(self):
        require(
            all(path.read_bytes() == raw for path, raw in self.captured.items()),
            "proof artifact changed during admission",
        )


def bound(review, name, expected):
    rows = [item for item in review["source"]["inputs"] if item["path"] == name]
    require(len(rows) == 1 and rows[0]["sha256"] == expected, "saved input differs: " + name)


def verify_population(review):
    """The shared workflow admits one record or a bounded batch, never wider scope."""
    targets = review["targets"]
    identities = [row["target_id"] for row in targets]
    paths = [row["path"] for row in targets]
    count = len(targets)
    require(
        1 <= count <= 10
        and len(set(identities)) == len(set(paths)) == count
        and review["kind"] == ("record" if count == 1 else "batch")
        and type(review["scope"]["population_size"]) is int
        and review["scope"]["population_size"] == count
        and review["scope"]["reviewed_target_ids"] == identities,
        "exact one-record or at-most-ten-record review population required",
    )


def expected_block(result, actual_mapping_source):
    """Check native serialization only; classification stays in the bound source proof."""
    match = re.match(
        r"^(kg-microbe NCBI2GTDB\.tsv\.gz sha256:761d5537a7edb4b0 "
        r"\(file mtime \d{4}-\d{2}-\d{2}\))",
        actual_mapping_source,
    )
    require(match is not None, "exact crosswalk provenance required")
    source = match.group(1)
    route = result.get("via", "")
    if route.startswith("ncbi_rank_"):
        rank = route.removeprefix("ncbi_rank_")
        require(rank in {"g", "f", "o", "c", "p", "d"}, "unsupported higher rank")
        source += (
            f" [grounded at {rank}__ rank; {result.get('n_alt', 1)} GTDB taxa under the NCBI taxon]"
        )
    elif route == "ncbi_name":
        source += " [mapped via NCBI species name — no species-level NCBI id in table]"
    else:
        require(route == "ncbi_id", "unsupported native route")
    block = {
        key: result[key]
        for key in (
            "gtdb_id",
            "gtdb_taxon",
            "gtdb_lineage",
            "ncbi_source_id",
            "majority_fraction",
            "is_reclassified",
        )
    }
    block.update(
        (key, result[key])
        for key in ("support_genomes", "total_genomes")
        if result.get(key) is not None
    )
    return {**block, "mapping_source": source}


def verify_projection(before, after, source, indices):
    expected = copy.deepcopy(before)
    occurrences = source["occurrences"]
    selected = [item["taxonomy_index"] for item in occurrences]
    require(
        selected
        and all(type(index) is int and index >= 0 for index in selected)
        and all(type(index) is int and index >= 0 for index in indices)
        and len(set(selected)) == len(selected)
        and len(set(indices)) == len(indices)
        and sorted(selected) == sorted(indices),
        "exact unique mutable taxonomy occurrences required",
    )
    grounded = statuses = 0
    for occurrence in occurrences:
        index = occurrence["taxonomy_index"]
        member = expected["taxonomy"][index]
        term = member["taxon_term"]
        require(term == occurrence["existing_descriptor"], "original descriptor differs")
        require(term["term"] == occurrence["term"], "source term differs")
        require(
            member.get("strain_designation", {}).get("strain_name") == occurrence["strain_name"],
            "source stock differs",
        )
        require(
            "gtdb_classification" not in term
            and term.get("gtdb_grounding_status") not in {"WITHHELD", "NO_GTDB_EQUIVALENT"},
            "add-only successor cannot refresh or override a withheld grounding",
        )
        prior = copy.deepcopy(term)
        result = occurrence["native_result"]
        require(result is None or isinstance(result, dict), "unsupported source result")
        if result is None:
            require(
                occurrence.get("classify_status") == {"status": "UNRESOLVED", "candidates": []}
                and term["term"]["id"].startswith("NCBITaxon:")
                and "manual_curated_reason" in occurrence
                and "manual_withheld_reason" in occurrence
                and occurrence["manual_curated_reason"] is None
                and occurrence["manual_withheld_reason"] is None,
                "explicit unheld native-null UNRESOLVED observation required",
            )
            term["gtdb_grounding_status"] = "UNRESOLVED"
            term.pop("gtdb_candidates", None)
        elif result.get("ambiguous") is True:
            require(result.get("ncbi_source_id") == term["term"]["id"], "source result misrouted")
            options = result.get("gtdb_options")
            require(
                isinstance(options, list)
                and options
                and len(set(options)) == len(options)
                and result.get("n_alt", len(options)) == len(options)
                and all(isinstance(value, str) and value.startswith("GTDB:") for value in options),
                "complete unselected ambiguity options required",
            )
            term["gtdb_grounding_status"] = "AMBIGUOUS"
            term["gtdb_candidates"] = options
        else:
            require(result.get("ncbi_source_id") == term["term"]["id"], "source result misrouted")
            require(result.get("gtdb_id"), "native grounded or ambiguous result required")
            actual_block = after["taxonomy"][index]["taxon_term"]["gtdb_classification"]
            term["gtdb_classification"] = expected_block(result, actual_block["mapping_source"])
            term["gtdb_grounding_status"] = "GROUNDED"
            term.pop("gtdb_candidates", None)
            grounded += 1
        statuses += any(prior.get(key) != term.get(key) for key in FIELDS[1:])
    prior_history = expected.get("curation_history", [])
    events = after.get("curation_history", [])[len(prior_history) :]
    actions = []
    if grounded:
        actions.append(
            (
                "GTDB_GROUND",
                f"Added {grounded} gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395).",
            )
        )
    if statuses:
        actions.append(
            (
                "GTDB_SET_STATUS",
                f"Wrote gtdb_grounding_status on {statuses} taxonomy entries (#294, #395).",
            )
        )
    require(actions and len(events) == len(actions), "exact substantive native events required")
    for event, (action, changes) in zip(events, actions, strict=True):
        require(
            isinstance(event.get("timestamp"), str)
            and re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", event["timestamp"])
            and event
            == {
                "timestamp": event["timestamp"],
                "curator": "gtdb_ground.py",
                "action": action,
                "changes": changes,
            },
            "native appended event differs",
        )
    expected["curation_history"] = prior_history + events
    require(after == expected, "scientific content, stock identity or historical events changed")


def verify_gate(artifacts, review, proof, gate, item):
    matching = [row for row in review["checks"] if row["check_id"] == item["check_id"]]
    require(len(matching) == 1, "unique saved native check required")
    check = matching[0]
    require(
        check["required"] is True
        and check["status"] == "passed"
        and check["exit_code"] == 0
        and check["target_ids"] == [proof["target_id"]],
        "required scoped native check failed",
    )
    receipt = json.loads(artifacts.read(item["receipt"]))
    log, exit_raw = artifacts.read(item["log"]), artifacts.read(item["exit"])
    public = receipt["public_evidence"]
    for key, metadata in (
        ("receipt", "raw_receipt_sha256"),
        ("log", "raw_log_sha256"),
        ("exit", "raw_exit_sha256"),
    ):
        require(item[key]["raw_sha256"] == public[metadata], "raw publication mapping differs")
        bound(review, item[key]["raw_path"], item[key]["raw_sha256"])
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    require(
        any(evidence[key]["reference"] == item["log"]["raw_path"] for key in check["evidence_ids"]),
        "saved gate evidence differs",
    )
    require(
        log
        and digest(log) == public["public_log_sha256"]
        and digest(exit_raw) == public["raw_exit_sha256"]
        and exit_raw.strip() == b"0"
        and receipt["log_sha256"] == public["raw_log_sha256"]
        and receipt["revision"] == proof["execution_revision"]
        and receipt["plan"] is False
        and receipt["exit_code"] == 0
        and receipt.get("finished_at")
        and receipt["execution_inputs_unchanged"] is True,
        "native persisted gate evidence differs",
    )
    target_hashes = [
        value for name, value in receipt["inputs"].items() if name.endswith("/" + proof["target"])
    ]
    require(target_hashes == [proof["after_sha256"]], "gate tested another record snapshot")
    command = receipt["command"]
    require(
        command[:6] == ["just", "--verbose", "--no-dotenv", "--color", "never", RECIPES[gate]],
        "native command differs",
    )
    # Saved commands are relative and therefore survive public path redaction.
    require(shlex.split(check["command"]) == command, "saved and actual commands differ")
    if gate == "new-history":
        require(
            receipt["new_history_sidecars"]
            == {proof["history_sidecar"]["path"]: proof["history_sidecar"]["sha256"]},
            "native sidecar persistence differs",
        )
    else:
        expected = (
            "history/records/" + Path(proof["target"]).stem
            if gate == "history"
            else proof["target"]
        )
        require(command[6] == expected, "native gate target differs")
        require(
            (
                len(command) == 7
                if gate != "strict"
                else len(command) == 9 and command[7] == "--out" and command[8].startswith(".temp/")
            ),
            "native gate arguments differ",
        )


def admit(root, path, predecessor_sha256, allowances, *, current=None):
    """Return a protected historical view only after exact successor proof succeeds."""
    root = Path(root).resolve()
    relative = Path(path)
    require(
        not relative.is_absolute()
        and ".." not in relative.parts
        and (root / path).resolve().is_relative_to(root),
        "safe canonical target required",
    )
    supplied_current = current is not None
    current = (root / path).read_bytes() if current is None else current
    actual = digest(current)
    if actual == predecessor_sha256:
        return Admission(actual, current, False)
    require(path in allowances, "unknown changed record has no successor allowance")
    allowed = allowances[path]
    revision = allowed["baseline_revision"]
    require(re.fullmatch(r"[0-9a-f]{40}", revision), "immutable predecessor revision required")
    original = subprocess.check_output(["git", "show", f"{revision}:{path}"], cwd=root)
    require(digest(original) == predecessor_sha256, "immutable predecessor bytes differ")
    artifacts = Artifacts(root)
    if not supplied_current:
        artifacts.captured[(root / path).resolve()] = current
    proof = json.loads(artifacts.read(allowed["manifest"]))
    require(
        proof["target"] == path
        and proof["before_sha256"] == predecessor_sha256
        and proof["after_sha256"] == actual
        and proof["scientific_review"] is False,
        "exact target successor differs",
    )
    before, after = yaml.safe_load(original), yaml.safe_load(current)
    require(before["id"] == after["id"] == proof["target_id"], "record identity differs")
    review = yaml.safe_load(artifacts.read(proof["diagnostic_review"]))
    validate_review(review)
    verify_population(review)
    require(
        review["repository"] == "CultureBotAI/CommunityMech"
        and review["source"]["git_revision"] == proof["execution_revision"]
        and review["completion"] == "completed"
        and review["scientific_review"] is False
        and review["verdict"] == "pass_with_limitations"
        and review["scope"]["coverage"] == "partial",
        "completed partial technical review required",
    )
    target = [row for row in review["targets"] if row["target_id"] == proof["target_id"]]
    require(len(target) == 1 and target[0]["path"] == path, "saved target differs")
    bound(review, path, actual)
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    require(
        any(
            row["area"] == "grounding"
            and row["outcome"] == "supported"
            and proof["target_id"] in row["target_ids"]
            and any(evidence[key]["kind"] == "database" for key in row["evidence_ids"])
            for row in review["assessments"]
        ),
        "supported database correspondence or status assessment required",
    )
    application = proof["application_receipt"]
    require(application["sha256"] == application["raw_sha256"], "actual application bytes required")
    bound(review, application["raw_path"], application["raw_sha256"])
    applied = json.loads(artifacts.read(application))
    require(
        applied["applied"] is True
        and applied["target"] == path
        and applied["target_id"] == proof["target_id"]
        and applied["before_sha256"] == predecessor_sha256
        and applied["after_sha256"] == actual
        and applied["execution_revision"] == proof["execution_revision"]
        and applied["scientific_review"] is False,
        "actual application chain differs",
    )
    bound(review, str(Path(application["raw_path"]).with_name("before.yaml")), predecessor_sha256)
    for name, expected in applied["inputs"].items():
        if name == path:
            require(expected == predecessor_sha256, "application input baseline differs")
        bound(review, name, actual if name == path else expected)
    require(applied["inputs"].get(path) == predecessor_sha256, "application target input absent")
    bound(review, ENGINE, applied["helper_sha256"])
    bound(review, NATIVE, NATIVE_SHA)
    stage = [
        row
        for row in review["source"]["inputs"]
        if row["sha256"] == applied["reviewed_receipt_sha256"]
        and row["path"].endswith("/receipt.json")
    ]
    require(len(stage) == 1, "exact reviewed stage receipt required")
    route = proof["native_recomputation"]
    require(route["sha256"] == route["raw_sha256"], "exact source metadata bytes required")
    bound(review, route["raw_path"], route["sha256"])
    source_raw = artifacts.read(route)
    source = json.loads(source_raw)
    source_item = proof["grounding_evidence"]
    require(
        source_item["path"] == route["raw_path"] and source_item["sha256"] == route["sha256"],
        "source metadata linkage differs",
    )
    require(
        source["record"] == path
        and source["record_id"] == proof["target_id"]
        and source["scientific_review"] is False,
        "source target differs",
    )
    require(
        source["source_inspection_sha256"] == applied["source_proof"]["sha256"],
        "source inspection differs",
    )
    bound(review, applied["source_proof"]["path"], source["source_inspection_sha256"])
    for name, expected in source["source_inputs"].items():
        if name == path:
            require(expected == predecessor_sha256, "source input baseline differs")
        bound(review, name, actual if name == path else expected)
    require(source["source_inputs"].get(path) == predecessor_sha256, "source target input absent")
    if any(item["native_result"] is None for item in source["occurrences"]):
        require(
            applied.get("native_operations") == ["--apply-status"],
            "native-null correction requires actual status-only application",
        )
    tables = [
        (name, value)
        for name, value in source["source_inputs"].items()
        if name.endswith("/NCBI2GTDB.tsv.gz")
    ]
    require(len(tables) == 1 and tables[0][1] == TABLE_SHA, "exact source crosswalk required")
    verify_projection(before, after, source, proof["mutable_taxonomy_indices"])
    sidecar = proof["history_sidecar"]
    bound(review, sidecar["path"], sidecar["sha256"])
    history_raw = artifacts.read(sidecar)
    history = yaml.safe_load(history_raw)
    require(
        history["target"]["kind"] == "record"
        and history["target"]["path"] == path
        and history["events"],
        "actual native history binding differs",
    )
    # The native scaffold binds the actual applied receipt; that receipt above
    # already binds the exact before/after bytes. The record hash need not be
    # duplicated as free text in the sidecar (#2867).
    history_links = [
        pair
        for event in history["events"]
        if event.get("type") == "EDIT"
        and event.get("outcome") == "changed"
        and {"taxonomy", "curation_history"}.issubset(event.get("sections", []))
        for pair in re.findall(
            r"Actual apply receipt (\S+)\s+sha256:([0-9a-f]{64})(?:\.|\s|$)",
            event.get("details", ""),
        )
    ]
    require(
        history_links == [(application["raw_path"], application["raw_sha256"])],
        "native history receipt link differs",
    )
    require(
        set(proof["required_checks"]) == set(RECIPES) == set(proof["check_evidence"]),
        "all eight scoped native gates required",
    )
    check_ids = {item["check_id"] for item in proof["check_evidence"].values()}
    required = {
        row["check_id"]
        for row in review["checks"]
        if row["required"] and proof["target_id"] in row["target_ids"]
    }
    require(len(check_ids) == 8 and required == check_ids, "saved required gate coverage differs")
    for gate, item in proof["check_evidence"].items():
        verify_gate(artifacts, review, proof, gate, item)
    require(
        artifacts.read(proof["review_markdown"]).decode() == render_markdown(review),
        "derived Markdown differs",
    )
    artifacts.verify()
    return Admission(actual, original, True)


def current_record_sha256(root, path, predecessor_sha256, allowances, *, current=None):
    return admit(root, path, predecessor_sha256, allowances, current=current).current_sha256


def historical_document(root, path, predecessor_sha256, allowances, *, current=None):
    return yaml.safe_load(
        admit(root, path, predecessor_sha256, allowances, current=current).historical_bytes
    )
