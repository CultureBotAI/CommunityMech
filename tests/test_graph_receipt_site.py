"""Exercise the deployment command with complete receipts and damaged artifacts."""

import gzip
import json
import runpy
import shutil
import subprocess
import sys
from fnmatch import fnmatchcase
from pathlib import Path

import pytest
import yaml

from communitymech import graph_embedding_receipts as receipts

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_graph_receipts.py"
CHECKER = runpy.run_path(str(SCRIPT))


@pytest.fixture
def graph_site(tmp_path):
    corpus = tmp_path / CHECKER["CORPUS_RELATIVE"]
    corpus.mkdir(parents=True)
    record = corpus / "fixture.yaml"
    record.write_text("id: fixture\n")
    source = tmp_path / "fixture-source.tsv.gz"
    source.write_bytes(gzip.compress(b"node\td1\td2\nCHEBI:1\t1\t2\nCHEBI:2\t2\t3\n"))
    reader = receipts.GraphSource(source, ["CHEBI"])
    vectors = dict(reader)
    for relative, methods in CHECKER["RECEIPTS"]:
        metadata = tmp_path / relative
        metadata.parent.mkdir(parents=True, exist_ok=True)
        basename = metadata.name.removesuffix(".metadata.json")
        method = methods[0]
        projection = {
            "method": method,
            "implementation": "graphviz.sfdp" if method == "sfdp" else "pacmap.PaCMAP",
            "normalization": "l2",
            "parameters": {},
            "library_versions": {"fixture": "1"},
            "effective_pairs": {"neighbors": 1, "mid_near": 0, "further": 1},
            "graph": {
                "construction": "symmetric_union_knn",
                "dot_sha256": "a" * 64,
                "graphviz_version": "fixture",
                "arguments": ["-Tplain"],
                "effective_k": 1,
                "edges": 1,
            },
        }
        receipt = receipts.make_receipt(
            source=reader.receipt,
            corpus=receipts.corpus_receipt([record], corpus),
            ledger=[
                {"identifier": name, "source_nodes": [name], "status": "projected"}
                for name in vectors
            ],
            matrix=receipts.matrix_receipt(vectors.values(), vectors),
            projection=projection,
            coverage={"eligible": 2, "projected": 2},
        )
        staged_html = tmp_path / "staged.html"
        staged_html.write_text("<p>Fixture graph</p>")
        staged_points = tmp_path / "staged.json"
        staged_points.write_text(
            json.dumps(
                [
                    {CHECKER["POINT_ID"]: name, "umap_x": index, "umap_y": -index}
                    for index, name in enumerate(vectors)
                ]
            )
        )
        receipts.publish_artifacts(
            {
                metadata.parent / (basename + ".html"): staged_html,
                metadata.parent / (basename + ".points.json"): staged_points,
            },
            metadata,
            receipt,
        )
    source.unlink()  # Deployment must work without the source vectors being present.
    return tmp_path


def run_checker(root):
    # -S removes site-packages: the actual deployment entry point is stdlib-only.
    return subprocess.run(
        [sys.executable, "-S", str(SCRIPT), "--root", str(root)], capture_output=True, text=True
    )


def test_actual_deployment_command_accepts_complete_current_graphs_without_vectors(graph_site):
    result = run_checker(graph_site)
    assert result.returncode == 0, result.stdout + result.stderr
    assert len(json.loads(result.stdout)["verified_graphs"]) == len(CHECKER["RECEIPTS"])


def test_committed_graphs_match_the_actual_corpus():
    result = run_checker(ROOT)
    assert result.returncode == 0, result.stdout + result.stderr


def test_committed_graph_gate_rejects_corpus_mutation_and_accepts_restoration(tmp_path):
    # Copy only publication inputs: no model, embedding source, or vector cache.
    corpus = tmp_path / CHECKER["CORPUS_RELATIVE"]
    shutil.copytree(ROOT / CHECKER["CORPUS_RELATIVE"], corpus)
    for relative, _ in CHECKER["RECEIPTS"]:
        metadata = ROOT / relative
        basename = metadata.name.removesuffix(".metadata.json")
        for name in (metadata.name, basename + ".html", basename + ".points.json"):
            destination = tmp_path / metadata.parent.relative_to(ROOT) / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(metadata.parent / name, destination)
    result = run_checker(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    record = next(corpus.glob("*.yaml"))
    original = record.read_bytes()
    record.write_bytes(original + b"\n# corpus mutation control\n")
    changed = run_checker(tmp_path)
    assert changed.returncode != 0
    assert "graph corpus changed since generation" in changed.stderr
    record.write_bytes(original)
    restored = run_checker(tmp_path)
    assert restored.returncode == 0, restored.stdout + restored.stderr


def test_required_validation_runs_real_graph_check_for_pr_and_merge_group():
    workflow = yaml.safe_load((ROOT / ".github/workflows/validate-strict.yaml").read_text())
    triggers = workflow.get("on", workflow.get(True))
    for event in ("pull_request", "merge_group"):
        assert event in triggers
        assert not (triggers[event] or {}).get("paths")
        assert not (triggers[event] or {}).get("paths-ignore")
    job = workflow["jobs"]["validate-strict"]
    assert not job.get("if")
    assert not job.get("continue-on-error", False)
    step = next(
        s for s in job["steps"] if s.get("run") == "python -S scripts/check_graph_receipts.py"
    )
    assert not step.get("if")
    assert not step.get("continue-on-error", False)


@pytest.mark.parametrize("damage", ["missing_receipt", "html", "points", "corpus"])
def test_actual_deployment_command_rejects_damaged_or_stale_graphs(graph_site, damage):
    metadata = graph_site / CHECKER["RECEIPTS"][0][0]
    basename = metadata.name.removesuffix(".metadata.json")
    if damage == "missing_receipt":
        metadata.unlink()
    elif damage == "corpus":
        (graph_site / CHECKER["CORPUS_RELATIVE"] / "fixture.yaml").write_text("id: changed\n")
    else:
        suffix = ".html" if damage == "html" else ".points.json"
        path = metadata.parent / (basename + suffix)
        path.write_text(path.read_text() + " ")
    result = run_checker(graph_site)
    assert result.returncode != 0, result.stdout
    assert "graph publication refused" in result.stderr


def test_pages_workflow_checks_graphs_before_staging_or_upload():
    workflow = yaml.safe_load((ROOT / ".github/workflows/generate-pages.yaml").read_text())
    steps = workflow["jobs"]["deploy"]["steps"]
    check = next(
        index
        for index, step in enumerate(steps)
        if "python scripts/check_graph_receipts.py" in step.get("run", "")
    )
    publication = next(
        index for index, step in enumerate(steps) if step.get("name") == "Upload docs/ artifact"
    )
    assert check < publication


def test_pages_workflow_runs_for_each_graph_validation_dependency():
    workflow = yaml.safe_load((ROOT / ".github/workflows/generate-pages.yaml").read_text())
    triggers = workflow.get("on", workflow.get(True))
    patterns = triggers["push"]["paths"]
    for changed in (
        "scripts/check_graph_receipts.py",
        "src/communitymech/graph_embedding_receipts.py",
    ):
        matches = False
        for pattern in patterns:
            if fnmatchcase(changed, pattern.removeprefix("!")):
                matches = not pattern.startswith("!")
        assert matches, f"Pages does not run when {changed} changes"
