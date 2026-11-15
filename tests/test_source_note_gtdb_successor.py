"""Exercise note-chain admission with real isolated Git history (#2869).

The already-tested mapping core is a spy in these outer-contract controls;
real final mapping artifacts will receive the shared actual-proof matrix after
the first end-to-end record is saved. No synthetic artifact is published.
"""

import copy
import json
import shutil
import subprocess
from pathlib import Path

import pytest
import source_note_gtdb_successor as composite
import yaml
from test_gtdb_source_note_guard import PLAN, case  # noqa: F401


def git(root, *args):
    return subprocess.check_output(
        [
            "git",
            "-c",
            "user.name=Codex",
            "-c",
            "user.email=codex@users.noreply.github.com",
            "-c",
            "commit.gpgsign=false",
            "-c",
            "core.hooksPath=/dev/null",
            *args,
        ],
        cwd=root,
        text=True,
    ).strip()


@pytest.fixture
def chain(request, monkeypatch):
    notes, plan, original, _ = request.getfixturevalue("case")
    root = notes.ROOT
    git(root, "init", "-q", "--initial-branch=proof-control")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "actual historical fixture")
    baseline = git(root, "rev-parse", "HEAD")
    cherry_picked = bool(getattr(request, "param", False))
    if cherry_picked:
        git(root, "commit", "-q", "--allow-empty", "-m", "feature helper execution")
    execution = git(root, "rev-parse", "HEAD")
    monkeypatch.setattr(notes, "head", lambda: git(root, "rev-parse", "HEAD"))
    stage = notes.stage(PLAN, notes.sha((root / PLAN).read_bytes()), ".temp/note-stage", execution)
    stage_raw = (root / ".temp/note-stage/receipt.json").read_bytes()
    applied = notes.apply(
        ".temp/note-stage",
        stage["candidate_sha256"],
        notes.sha(stage_raw),
        ".temp/note-applied",
        execution,
    )
    target = plan["target"]
    intermediate = (root / target).read_bytes()
    apply_raw = (root / ".temp/note-applied/receipt.json").read_bytes()
    sidecar_name = "history/records/" + Path(target).stem + "/note.yaml"
    sidecar = {
        "target": {"kind": "record", "path": target, "slug": Path(target).stem},
        "events": [
            {
                "type": "EDIT",
                "outcome": "changed",
                "sections": ["taxonomy", "curation_history"],
                "details": "Actual apply receipt .temp/note-applied/receipt.json sha256:"
                + notes.sha(apply_raw)
                + ".",
            }
        ],
    }
    (root / sidecar_name).parent.mkdir(parents=True)
    (root / sidecar_name).write_text(yaml.safe_dump(sidecar))
    git(root, "add", target, sidecar_name)
    git(root, "commit", "-q", "-m", "real note-only intermediate")
    intermediate_revision = git(root, "rev-parse", "HEAD")
    final_doc = yaml.safe_load(intermediate)
    final_doc["taxonomy"][2]["taxon_term"]["gtdb_candidates"] = final_doc["taxonomy"][2][
        "taxon_term"
    ]["gtdb_candidates"][:3]
    final_doc["curation_history"].append({"action": "GTDB_SET_STATUS", "fixture_only": True})
    current = yaml.safe_dump(final_doc, sort_keys=False).encode()
    (root / target).write_bytes(current)
    git(root, "add", target)
    git(root, "commit", "-q", "-m", "separate mapping fixture transition")
    final_revision = git(root, "rev-parse", "HEAD")
    if cherry_picked:
        source_intermediate = intermediate_revision
        git(root, "switch", "-q", "-c", "root-integration", baseline)
        git(root, "cherry-pick", source_intermediate)
        intermediate_revision = git(root, "rev-parse", "HEAD")
        git(root, "cherry-pick", final_revision)
        assert intermediate_revision != source_intermediate
        assert (root / target).read_bytes() == current

    def artifact(name, raw, raw_path=None):
        location = root / name
        location.parent.mkdir(parents=True, exist_ok=True)
        location.write_bytes(raw)
        result = {"path": name, "sha256": notes.sha(raw)}
        if raw_path is not None:
            result.update(raw_path=raw_path, raw_sha256=notes.sha(raw))
        return result

    note = {
        "source_plan": artifact(PLAN, (root / PLAN).read_bytes(), PLAN),
        "stage_receipt": artifact(
            "reports/note-stage.raw.json", stage_raw, ".temp/note-stage/receipt.json"
        ),
        "application_receipt": artifact(
            "reports/note-apply.raw.json", apply_raw, ".temp/note-applied/receipt.json"
        ),
        "history_sidecar": artifact(sidecar_name, (root / sidecar_name).read_bytes()),
    }
    bound_inputs = dict(applied["inputs"])
    bound_inputs[target] = notes.sha(current)
    bound_inputs[".temp/note-applied/before.yaml"] = notes.sha(original)
    for key in ("source_plan", "stage_receipt", "application_receipt"):
        bound_inputs[note[key]["raw_path"]] = note[key]["raw_sha256"]
    bound_inputs[sidecar_name] = note["history_sidecar"]["sha256"]
    review = {
        "source": {
            "inputs": [{"path": name, "sha256": value} for name, value in bound_inputs.items()]
        }
    }
    review_item = artifact("reviews/fixture.yaml", yaml.safe_dump(review).encode())
    final = {"execution_revision": final_revision, "diagnostic_review": review_item}
    final_item = artifact("reports/mapping.json", json.dumps(final).encode())
    proof = {
        "target": target,
        "before_sha256": notes.sha(original),
        "intermediate_revision": intermediate_revision,
        "intermediate_sha256": notes.sha(intermediate),
        "after_sha256": notes.sha(current),
        "mapping_allowance": {"baseline_revision": intermediate_revision, "manifest": final_item},
        "note_transition": note,
    }
    allowed = {
        target: {
            "baseline_revision": baseline,
            "manifest": artifact("reports/composite.json", json.dumps(proof).encode()),
        }
    }
    calls = []

    def mapping_spy(actual_root, path, predecessor, allowance, *, current):
        assert actual_root == root and path == target
        assert predecessor == notes.sha(intermediate)
        assert allowance[path] == proof["mapping_allowance"]
        calls.append((predecessor, current))
        return composite.mapping.Admission(notes.sha(current), intermediate, True)

    monkeypatch.setattr(composite.mapping, "admit", mapping_spy)
    return {
        "root": root,
        "target": target,
        "original": original,
        "intermediate": intermediate,
        "current": current,
        "plan": plan,
        "applied": applied,
        "stage": stage,
        "proof": proof,
        "allowed": allowed,
        "artifact": artifact,
        "calls": calls,
        "execution": execution,
        "final_execution": final_revision,
        "intermediate_revision": intermediate_revision,
    }


def admit(chain):
    return composite.admit(
        chain["root"],
        chain["target"],
        composite.mapping.digest(chain["original"]),
        chain["allowed"],
    )


def repin(chain):
    chain["allowed"][chain["target"]]["manifest"] = chain["artifact"](
        "reports/composite.json", json.dumps(chain["proof"]).encode()
    )


def test_real_git_intermediate_is_passed_to_unchanged_mapping_core(chain):
    result = admit(chain)
    assert result.historical_bytes == chain["original"] and result.changed
    assert result.current_sha256 == composite.mapping.digest(chain["current"])
    assert chain["calls"] == [(composite.mapping.digest(chain["intermediate"]), chain["current"])]


@pytest.mark.parametrize("chain", [True], indirect=True)
def test_cherry_picked_execution_metadata_does_not_require_ancestry(chain):
    assert admit(chain).historical_bytes == chain["original"]


@pytest.mark.parametrize("chain", [True], indirect=True)
def test_fresh_clone_needs_baselines_not_feature_execution_objects(chain, monkeypatch):
    source = chain["root"]
    clone = source.parent / (source.name + "-fresh-clone")
    subprocess.run(
        [
            "git",
            "clone",
            "--quiet",
            "--no-local",
            "--single-branch",
            "--branch",
            "root-integration",
            source.as_uri(),
            str(clone),
        ],
        check=True,
    )
    for revision in (chain["execution"], chain["final_execution"]):
        assert (
            subprocess.run(
                ["git", "cat-file", "-e", revision], cwd=clone, capture_output=True
            ).returncode
            != 0
        )
    assert (
        composite.historical_bytes(clone, chain["intermediate_revision"], chain["target"])
        == chain["intermediate"]
    )
    shutil.copytree(source / "reports", clone / "reports", dirs_exist_ok=True)
    shutil.copytree(source / "reviews", clone / "reviews", dirs_exist_ok=True)

    def mapping_spy(root, path, predecessor, allowance, *, current):
        assert root == clone and path == chain["target"]
        assert predecessor == composite.mapping.digest(chain["intermediate"])
        assert allowance[path]["baseline_revision"] == chain["intermediate_revision"]
        return composite.mapping.Admission(
            composite.mapping.digest(current), chain["intermediate"], True
        )

    monkeypatch.setattr(composite.mapping, "admit", mapping_spy)
    chain["root"] = clone
    assert admit(chain).historical_bytes == chain["original"]


@pytest.mark.parametrize("field", ["before", "after", "existing_stock", "existing_descriptor"])
def test_wrong_note_or_identity_projection_is_rejected_and_restored(chain, field):
    modified = copy.deepcopy(chain["plan"])
    modified["notes"][0][field] = "unreviewed"
    with pytest.raises(AssertionError, match="known old|undeclared content"):
        composite.verify_note_transition(
            chain["original"], chain["intermediate"], modified, chain["applied"], chain["stage"]
        )
    composite.verify_note_transition(
        chain["original"], chain["intermediate"], chain["plan"], chain["applied"], chain["stage"]
    )


@pytest.mark.parametrize(
    "key", ["source_plan", "application_receipt", "stage_receipt", "history_sidecar"]
)
def test_rehashed_note_artifact_still_requires_saved_review_binding(chain, key):
    item = chain["proof"]["note_transition"][key]
    location = chain["root"] / item["path"]
    original = location.read_bytes()
    prior_item = copy.deepcopy(item)
    location.write_bytes(original + b"\n ")
    item["sha256"] = composite.mapping.digest(location.read_bytes())
    if "raw_sha256" in item:
        item["raw_sha256"] = item["sha256"]
    repin(chain)
    with pytest.raises(AssertionError, match="saved input differs"):
        admit(chain)
    location.write_bytes(original)
    chain["proof"]["note_transition"][key] = prior_item
    repin(chain)
    assert admit(chain).changed


def test_nonexistent_and_wrong_real_intermediate_refuse(chain):
    saved = copy.deepcopy(chain["proof"])
    for revision in ("f" * 40, chain["allowed"][chain["target"]]["baseline_revision"]):
        chain["proof"]["intermediate_revision"] = revision
        chain["proof"]["mapping_allowance"]["baseline_revision"] = revision
        repin(chain)
        with pytest.raises((AssertionError, subprocess.CalledProcessError)):
            admit(chain)
    chain["proof"].clear()
    chain["proof"].update(saved)
    repin(chain)
    assert admit(chain).changed


def test_unrelated_current_biology_and_unknown_target_refuse(chain):
    location = chain["root"] / chain["target"]
    changed = yaml.safe_load(chain["current"])
    changed["description"] += " Invented protection."
    location.write_text(yaml.safe_dump(changed))
    with pytest.raises(AssertionError, match="composite chain"):
        admit(chain)
    location.write_bytes(chain["current"])
    with pytest.raises(AssertionError, match="unknown changed record"):
        composite.admit(
            chain["root"], chain["target"], composite.mapping.digest(chain["original"]), {}
        )
    assert admit(chain).changed
