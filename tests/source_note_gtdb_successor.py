"""Compose exact native note and mapping transitions without widening either (#2869).

2026-11-15: one reviewed original -> real committed note-only intermediate ->
ordinary mapping-only successor. This module reads proof artifacts only. The
caller must explicitly pin a composite manifest; no record is admitted by default.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import scoped_gtdb_successor as mapping
import yaml

from communitymech.curate.curation_event import record_curation_event

NOTE_HELPER = "scripts/adhoc/curate_gtdb_source_notes_20261115.py"


def historical_bytes(root, revision, path):
    mapping.require(re.fullmatch(r"[0-9a-f]{40}", revision), "exact real Git revision required")
    return subprocess.check_output(["git", "show", f"{revision}:{path}"], cwd=root)


def verify_note_transition(original, intermediate, plan, applied, stage):
    """Reconstruct every allowed note and native event; all other content must agree."""
    mapping.require(
        plan["scope"] == applied["scope"] == stage["scope"] == "taxonomy-notes-only"
        and plan["scientific_review"] is applied["scientific_review"] is False
        and applied["applied"] is True
        and stage["canonical_apply"] is False
        and stage["source_inputs_unchanged"] is True,
        "actual bounded note transition required",
    )
    before_sha, after_sha = mapping.digest(original), mapping.digest(intermediate)
    mapping.require(
        plan["target"] == applied["target"] == stage["target"]
        and plan["target_id"] == applied["target_id"] == stage["target_id"]
        and plan["before_sha256"]
        == applied["before_sha256"]
        == stage["before_sha256"]
        == before_sha
        and applied["after_sha256"] == stage["candidate_sha256"] == after_sha
        and applied["execution_revision"] == stage["execution_revision"],
        "exact original and real intermediate chain required",
    )
    before, expected = yaml.safe_load(original), yaml.safe_load(original)
    actual = yaml.safe_load(intermediate)
    mapping.require(before["id"] == actual["id"] == plan["target_id"], "note identity differs")
    seen = set()
    for change in plan["notes"]:
        index = change["taxonomy_index"]
        mapping.require(
            type(index) is int and index >= 0 and index not in seen, "unique note index"
        )
        seen.add(index)
        member = expected["taxonomy"][index]
        mapping.require(
            member["taxon_term"] == change["existing_descriptor"]
            and member.get("strain_designation") == change["existing_stock"]
            and member["taxon_term"].get("notes") == change["before"]
            and isinstance(change["after"], str)
            and change["after"].strip()
            and change["after"] != change["before"],
            "known old note, descriptor and stock required",
        )
        member["taxon_term"]["notes"] = change["after"]
    mapping.require(seen, "substantive note transition required")
    added = actual["curation_history"][len(before["curation_history"]) :]
    mapping.require(len(added) == 1, "one native note event required")
    timestamp = added[0].get("timestamp", "")
    mapping.require(
        re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", timestamp), "native event timestamp"
    )
    event = record_curation_event(
        expected,
        curator="Codex",
        action="CLARIFY_GTDB_SOURCE_SCOPE",
        changes=plan["event_changes"],
        llm_assisted=True,
        timestamp=timestamp,
    )
    mapping.require(
        actual == expected
        and event == stage["appended_native_inline_history"]
        and event == applied["appended_native_inline_history"],
        "note transition changed undeclared content or history",
    )


def admit(root, path, predecessor_sha256, allowances, *, current=None):
    root = Path(root).resolve()
    relative = Path(path)
    mapping.require(
        not relative.is_absolute()
        and ".." not in relative.parts
        and (root / relative).resolve().is_relative_to(root),
        "safe canonical target required",
    )
    supplied = current is not None
    current = (root / path).read_bytes() if current is None else current
    current_sha = mapping.digest(current)
    if current_sha == predecessor_sha256:
        return mapping.Admission(current_sha, current, False)
    mapping.require(path in allowances, "unknown changed record has no composite proof")
    artifacts = mapping.Artifacts(root)
    if not supplied:
        artifacts.captured[(root / path).resolve()] = current
    entry = allowances[path]
    proof = json.loads(artifacts.read(entry["manifest"]))
    original = historical_bytes(root, entry["baseline_revision"], path)
    mapping.require(mapping.digest(original) == predecessor_sha256, "historical bytes differ")
    intermediate = historical_bytes(root, proof["intermediate_revision"], path)
    mapping.require(
        proof["target"] == path
        and proof["before_sha256"] == predecessor_sha256
        and proof["intermediate_sha256"] == mapping.digest(intermediate)
        and proof["after_sha256"] == current_sha
        and proof["mapping_allowance"]["baseline_revision"] == proof["intermediate_revision"],
        "exact composite chain required",
    )
    final_manifest = json.loads(artifacts.read(proof["mapping_allowance"]["manifest"]))
    # Execution revisions remain exact receipt/review metadata. They need not
    # be ancestors of cherry-picked integration commits or available objects
    # after branch cleanup (#2874). Only the two actual byte baselines above
    # are Git dependencies, with explicit historical-CI retrieval.
    admitted = mapping.admit(
        root,
        path,
        proof["intermediate_sha256"],
        {path: proof["mapping_allowance"]},
        current=current,
    )
    mapping.require(
        admitted.changed and admitted.historical_bytes == intermediate, "final leg differs"
    )
    review = yaml.safe_load(artifacts.read(final_manifest["diagnostic_review"]))
    note = proof["note_transition"]
    loaded = {}
    for key in ("source_plan", "application_receipt", "stage_receipt"):
        item = note[key]
        mapping.require(item["sha256"] == item["raw_sha256"], "exact raw note artifact required")
        mapping.bound(review, item["raw_path"], item["raw_sha256"])
        loaded[key] = json.loads(artifacts.read(item))
    plan, applied, stage = (
        loaded[key] for key in ("source_plan", "application_receipt", "stage_receipt")
    )
    mapping.require(plan["target"] == path, "note plan target differs")
    mapping.require(
        applied["source_plan"]
        == stage["source_plan"]
        == {"path": note["source_plan"]["raw_path"], "sha256": note["source_plan"]["raw_sha256"]}
        and applied["reviewed_receipt"]
        == {
            "path": note["stage_receipt"]["raw_path"],
            "sha256": note["stage_receipt"]["raw_sha256"],
        },
        "actual note receipt links differ",
    )
    mapping.require(
        re.fullmatch(r"[0-9a-f]{40}", applied["execution_revision"]),
        "exact note execution metadata required",
    )
    mapping.bound(
        review,
        str(Path(note["application_receipt"]["raw_path"]).with_name("before.yaml")),
        predecessor_sha256,
    )
    mapping.require(applied["inputs"] == stage["inputs"], "note application inputs differ")
    mapping.require(applied["inputs"].get(path) == predecessor_sha256, "note target input missing")
    for name, digest in applied["inputs"].items():
        mapping.bound(review, name, current_sha if name == path else digest)
    for name, digest in plan["inputs"].items():
        mapping.require(applied["inputs"].get(name) == digest, "note source input omitted")
    mapping.require(
        applied["inputs"].get(NOTE_HELPER) == applied["helper_sha256"],
        "note helper binding differs",
    )
    verify_note_transition(original, intermediate, plan, applied, stage)
    sidecar = note["history_sidecar"]
    mapping.bound(review, sidecar["path"], sidecar["sha256"])
    history = yaml.safe_load(artifacts.read(sidecar))
    links = [
        pair
        for event in history.get("events", [])
        if event.get("type") == "EDIT"
        and event.get("outcome") == "changed"
        and {"taxonomy", "curation_history"}.issubset(event.get("sections", []))
        for pair in re.findall(
            r"Actual apply receipt (\S+)\s+sha256:([0-9a-f]{64})(?:\.|\s|$)",
            event.get("details", ""),
        )
    ]
    mapping.require(
        history["target"]["kind"] == "record"
        and history["target"]["path"] == path
        and history["target"]["slug"] == Path(path).stem
        and links
        == [(note["application_receipt"]["raw_path"], note["application_receipt"]["raw_sha256"])],
        "native note history receipt link differs",
    )
    artifacts.verify()
    return mapping.Admission(current_sha, original, True)
