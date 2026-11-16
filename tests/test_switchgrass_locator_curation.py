"""Private staging/application mutation controls, #1996, 2026-11-15.

Real original record and native writer; synthetic local proof fixtures are
explicitly test data, never actual consumer validation evidence. No canonical
workspace file, provider, runtime matcher or native writer is patched.
"""

import importlib.util
import inspect
import json
import subprocess
from copy import deepcopy
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import pytest
import yaml
from linkml_reference_validator.etl.source_locator import extract_docx_tables

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "scripts/adhoc/curate_switchgrass_source_locators_20261115.py"
spec = importlib.util.spec_from_file_location("switchgrass_locator_curation", HELPER)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
BASE = "b5cb827fa8dfac6e00f824f7d91de3ba74b123b8"


def frozen_original(repository=ROOT, revision=BASE):
    """Load the explicit predecessor independently of current canonical bytes."""
    raw = subprocess.check_output(["git", "-C", str(repository), "show", f"{revision}:{M.TARGET}"])
    assert M.sha(raw) == M.BEFORE
    return raw


ORIGINAL = frozen_original()


def write(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return M.sha(raw)


def test_frozen_predecessor_survives_current_locator_curation(tmp_path):
    """A real Git predecessor stays usable after a private current record changes."""
    source = tmp_path / "current-source"
    source.mkdir()
    target = source / M.TARGET
    write(target, ORIGINAL)
    subprocess.run(["git", "init", "-q", str(source)], check=True)
    subprocess.run(["git", "-C", str(source), "add", M.TARGET], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(source),
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "exact predecessor",
        ],
        check=True,
    )
    revision = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    assert frozen_original(source, revision) == ORIGINAL
    candidate, _, _ = M.render_candidate(
        ORIGINAL, {"controls": {"selected": {"sha256": "1" * 64}}}, "2026-11-16T00:00:00Z"
    )
    target.write_bytes(candidate)
    assert target.read_bytes() != ORIGINAL
    with pytest.raises(ValueError, match="exact Switchgrass original required"):
        M.selection(target.read_bytes())
    assert frozen_original(source, revision) == ORIGINAL
    target.write_bytes(ORIGINAL)
    assert frozen_original(source, revision) == ORIGINAL


def docx_fixture():
    cells = [["fixture" for _ in range(3)] for _ in range(19)]
    cells[11][0:2] = ["Methylobacterium", "OAE516"]
    cells[17][0:2] = ["Bacillus", "OAE603"]
    rows = "".join(
        "<w:tr>"
        + "".join(f"<w:tc><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:tc>" for text in row)
        + "</w:tr>"
        for row in cells
    )
    raw = BytesIO()
    with ZipFile(raw, "w") as archive:
        archive.writestr(
            "word/document.xml",
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:tbl>'
            + rows
            + "</w:tbl></w:body></w:document>",
        )
    return raw.getvalue()


def synthetic_report(mode, record, paths, catalog_raw, projection):
    """Construct explicit synthetic evidence so guards can be mutated locally."""
    failures = {
        "selected": set(),
        "restored": set(),
        "article-only": {paths[0], paths[2]},
        "wrong-cell": {paths[1]},
        "wrong-parent": {paths[0]},
    }[mode]
    evidence = next(d for d in record["discussions"] if d["discussion_id"] == M.DISCUSSION)[
        "evidence"
    ]
    source = json.loads(catalog_raw)["sources"][0]
    events = []
    for path, text, reference in M.surfaces(record):
        selection_error = mode == "wrong-parent" and path == paths[0]
        identity = None
        if path in paths and mode != "article-only" and not selection_error:
            entry = (2, 3, 4)[paths.index(path)]
            locator = evidence[entry]["source_locator"]
            cell = projection["tables"][locator["table"] - 1][locator["row"] - 1][
                locator["cell"] - 1
            ]
            identity = {
                "reference": source["reference"],
                "asset_id": source["asset_id"],
                "version": source["version"],
                "asset_sha256": source["asset_sha256"],
                "extraction_sha256": source["extraction_sha256"],
                "catalog_sha256": M.sha(catalog_raw),
                "extractor": projection["format"],
                "locator": locator,
                "selected_sha256": M.sha(cell["text"].encode()),
            }
        events.append(
            {
                "path": path,
                "reference": reference,
                "text_sha256": M.sha(text.encode()),
                "is_valid": path not in failures,
                "matched": None if selection_error else path not in failures,
                "severity": "ERROR" if path in failures else "INFO",
                "source_identity": identity,
                "message": (
                    "Source selection failed: synthetic wrong parent"
                    if selection_error
                    else "synthetic comparison"
                ),
            }
        )
    return {
        "mode": "selected" if mode == "restored" else mode,
        "control_passed": True,
        "errors": [],
        "changed_inputs": [],
        "network_attempts": [],
        "validator_revision": M.VALIDATOR,
        "runtime_python_members": 49,
        "independent_snippet_surfaces": 37,
        "native_exit_code": int(bool(failures)),
        "native_failures": len(failures),
        "comparisons": events,
        "established_source_identities": sum(e["source_identity"] is not None for e in events),
        **dict(zip(M.COUNT_KEYS, M.COUNTS[mode], strict=True)),
        "executable": "/synthetic-test/python",
        "installed_package": "/synthetic-test/package",
        "dependencies": {"synthetic_test_fixture": "not-an-actual-consumer-run"},
    }


@pytest.fixture
def unit(tmp_path, monkeypatch):
    root = tmp_path / "private-repository"
    root.mkdir()
    for name in M.REQUIRED:
        write(root / name, ORIGINAL if name == M.TARGET else (ROOT / name).read_bytes())
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "--allow-empty",
            "-qm",
            "synthetic fixture",
        ],
        check=True,
    )
    monkeypatch.setattr(M, "ROOT", root)
    revision = M.head()
    monkeypatch.setattr(M, "VALIDATOR", revision)
    source_package = root / "src/linkml_reference_validator"
    installed_package = root / ".temp/installed/linkml_reference_validator"
    runtime_inputs = {}
    for package in (source_package, installed_package):
        for name in ("__init__.py", *(f"member_{i}.py" for i in range(47))):
            runtime_inputs[str(package / name)] = write(
                package / name, b"# synthetic package member\n"
            )
        runtime_inputs[str(package / "etl/source_locator.py")] = write(
            package / "etl/source_locator.py",
            Path(inspect.getfile(extract_docx_tables)).read_bytes(),
        )
    asset = docx_fixture()
    monkeypatch.setattr(M, "ASSET_SHA", M.sha(asset))
    projection = extract_docx_tables(asset)
    projection_raw = M.encoded(projection)
    catalog_raw = M.encoded(
        {
            "version": 1,
            "sources": [
                {
                    "reference": "PMID:36472419",
                    "asset_id": M.ASSET,
                    "version": "published",
                    "asset_path": f"assets/{M.ASSET}",
                    "asset_sha256": M.ASSET_SHA,
                    "extraction_path": "extractions/table-s1.json",
                    "extraction_sha256": M.sha(projection_raw),
                }
            ],
        }
    )
    _, selected, _, paths = M.selection(ORIGINAL)
    prepared = root / ".temp/prepared"
    inputs = {str(root / name): M.sha((root / name).read_bytes()) for name in M.REQUIRED}
    outputs = {
        "original.yaml": ORIGINAL,
        "selected.json": M.encoded(selected),
        "catalog.json": catalog_raw,
        "extractions/table-s1.json": projection_raw,
        f"assets/{M.ASSET}": asset,
        "schema/communitymech.yaml": (
            ROOT / "src/communitymech/schema/communitymech.yaml"
        ).read_bytes(),
        "schema/mech_shared.yaml": (
            ROOT / "src/communitymech/schema/mech_shared.yaml"
        ).read_bytes(),
        "config.json": b"{}\n",
    }
    preparation = {
        "plan": False,
        "schema_bytes_unchanged": True,
        "record_content_unchanged_except_three_locators": True,
        "selected_paths": paths,
        "asset_sha256": M.ASSET_SHA,
        "inputs": inputs,
        "outputs": {name: write(prepared / name, raw) for name, raw in outputs.items()},
    }
    prep_sha = write(prepared / "preparation.json", M.encoded(preparation))
    plan = {
        "scope": M.SCOPE,
        "target": M.TARGET,
        "before_sha256": M.BEFORE,
        "preparation": {"path": ".temp/prepared/preparation.json", "sha256": prep_sha},
        "inputs": {name: M.sha((root / name).read_bytes()) for name in M.REQUIRED},
        "controls": {},
    }
    for mode in M.COUNTS:
        directory = root / ".temp" / mode
        record, _, _ = M.control_record(ORIGINAL, mode)
        report = synthetic_report(mode, record, paths, catalog_raw, projection)
        report["installed_package"] = str(installed_package)
        report["inputs"] = {
            **inputs,
            **runtime_inputs,
            **{str(prepared / name): digest for name, digest in preparation["outputs"].items()},
            str(prepared / "preparation.json"): prep_sha,
            str(directory / "record.json"): write(directory / "record.json", M.encoded(record)),
        }
        report["native_argv"] = [
            "data",
            str(directory / "record.json"),
            "--schema",
            str(prepared / "schema/communitymech.yaml"),
            "--target-class",
            "MicrobialCommunity",
            "--config",
            str(prepared / "config.json"),
            "--no-full-text",
        ]
        report["log_sha256"] = write(
            directory / "native.log", b"Synthetic unit-test evidence only.\n"
        )
        write(directory / "native.exit", f"{report['native_exit_code']}\n".encode())
        plan["controls"][mode] = {
            "path": f".temp/{mode}/receipt.json",
            "sha256": write(directory / "receipt.json", M.encoded(report)),
        }
    plan_name = ".temp/plan.json"
    plan_sha = write(root / plan_name, M.encoded(plan))
    return root, revision, plan_name, plan_sha, plan


def test_private_stage_apply_and_exact_backup(unit):
    root, revision, name, digest, plan = unit
    assert M.stage(name, digest, ".temp/planned", revision, plan_only=True)["plan"]
    assert not (root / ".temp/planned").exists()
    staged = M.stage(name, digest, ".temp/stage", revision)
    assert (root / M.TARGET).read_bytes() == ORIGINAL
    candidate = (root / ".temp/stage" / Path(M.TARGET).name).read_bytes()
    expected, event = M.verify_candidate(ORIGINAL, candidate, plan)
    assert list(M.surfaces(expected)) == list(M.surfaces(yaml.safe_load(ORIGINAL)))
    assert event["llm_assisted"] is True
    assert expected["curation_history"][:-1] == yaml.safe_load(ORIGINAL)["curation_history"]
    receipt_sha = M.sha((root / ".temp/stage/receipt.json").read_bytes())
    assert M.apply(
        ".temp/stage",
        staged["candidate_sha256"],
        receipt_sha,
        ".temp/apply-plan",
        revision,
        plan_only=True,
    )["plan"]
    assert not (root / ".temp/apply-plan").exists()
    applied = M.apply(
        ".temp/stage", staged["candidate_sha256"], receipt_sha, ".temp/applied", revision
    )
    assert applied["applied"] and (root / M.TARGET).read_bytes() == candidate
    assert (root / ".temp/applied/before.yaml").read_bytes() == ORIGINAL
    assert yaml.safe_load((root / ".temp/applied/validated.yaml").read_bytes()) == expected
    with pytest.raises(ValueError, match="exclusive"):
        M.apply(".temp/stage", staged["candidate_sha256"], receipt_sha, ".temp/applied", revision)


@pytest.mark.parametrize(
    "mutation", ["locator", "quotation", "reference", "biology", "old-history", "event"]
)
def test_rehashed_candidate_mutation_refuses_then_restores(unit, mutation):
    root, revision, name, digest, plan = unit
    staged = M.stage(name, digest, ".temp/stage", revision)
    target = root / ".temp/stage" / Path(M.TARGET).name
    original = target.read_bytes()
    altered = yaml.safe_load(original)
    _, _, index, _ = M.selection(ORIGINAL)
    item = altered["discussions"][index]["evidence"][2]
    if mutation == "locator":
        item["source_locator"]["row"] = 18
    elif mutation == "quotation":
        item["snippet"] = "OAE515"
    elif mutation == "reference":
        item["reference"] = "PMID:12345"
    elif mutation == "biology":
        altered["name"] += " changed"
    elif mutation == "old-history":
        altered["curation_history"][0]["changes"] += " altered"
    else:
        altered["curation_history"][-1]["llm_assisted"] = False
    changed = yaml.safe_dump(altered, sort_keys=False).encode()
    assert changed != original
    with pytest.raises(ValueError, match="candidate bytes or native event differ"):
        M.verify_candidate(ORIGINAL, changed, plan)
    M.verify_candidate(ORIGINAL, original, plan)
    assert (root / M.TARGET).read_bytes() == ORIGINAL
    assert staged["candidate_sha256"] == M.sha(original)


@pytest.mark.parametrize(
    "mutation",
    [
        "counts",
        "identity",
        "comparison",
        "duplicate",
        "soft-parent",
        "capture",
        "runtime-member",
        "log",
    ],
)
def test_consistently_rehashed_control_mutations_refuse_then_restore(unit, mutation):
    root, revision, name, digest, plan = unit
    M.prepare(name, digest, revision)
    mode = "wrong-parent" if mutation == "soft-parent" else "selected"
    receipt_path = root / plan["controls"][mode]["path"]
    raw = receipt_path.read_bytes()
    report = json.loads(raw)
    if mutation == "counts":
        report["native_comparisons"] = 36
    elif mutation == "identity":
        next(e for e in report["comparisons"] if e["source_identity"])["source_identity"][
            "asset_id"
        ] = "wrong.docx"
    elif mutation == "comparison":
        report["comparisons"][0]["matched"] = None
    elif mutation == "duplicate":
        report["comparisons"][0] = deepcopy(report["comparisons"][1])
    elif mutation == "soft-parent":
        next(e for e in report["comparisons"] if e["matched"] is None)["severity"] = "WARNING"
    elif mutation == "capture":
        del report["inputs"][str(root / M.TARGET)]
    elif mutation == "runtime-member":
        del report["inputs"][str(root / "src/linkml_reference_validator/member_0.py")]
    else:
        report["log_sha256"] = "0" * 64
    changed = M.encoded(report)
    assert changed != raw
    mutated = deepcopy(plan)
    mutated["controls"][mode]["sha256"] = write(receipt_path, changed)
    mutated_sha = write(root / ".temp/mutated.json", M.encoded(mutated))
    try:
        with pytest.raises(ValueError):
            M.stage(".temp/mutated.json", mutated_sha, ".temp/refused", revision)
        assert not (root / ".temp/refused/receipt.json").exists()
        assert (root / M.TARGET).read_bytes() == ORIGINAL
    finally:
        receipt_path.write_bytes(raw)
    M.prepare(name, digest, revision)


@pytest.mark.parametrize("mutation", ["missing", "extra"])
def test_rehashed_stage_capture_coverage_refuses_then_restores(unit, mutation):
    root, revision, name, digest, _ = unit
    staged = M.stage(name, digest, ".temp/stage", revision)
    receipt_path = root / ".temp/stage/receipt.json"
    raw = receipt_path.read_bytes()
    receipt = json.loads(raw)
    if mutation == "missing":
        receipt["inputs"].pop(next(iter(receipt["inputs"])))
    else:
        receipt["inputs"][str(root / "extra")] = "1" * 64
    changed_sha = write(receipt_path, M.encoded(receipt))
    try:
        with pytest.raises(ValueError, match="stage captured-input coverage differs"):
            M.apply(
                ".temp/stage", staged["candidate_sha256"], changed_sha, ".temp/refused", revision
            )
        assert not (root / ".temp/refused").exists()
        assert (root / M.TARGET).read_bytes() == ORIGINAL
    finally:
        receipt_path.write_bytes(raw)
    M.admitted_stage(".temp/stage", staged["candidate_sha256"], M.sha(raw), revision)


def test_real_source_drift_after_validation_refuses_then_restores(unit, monkeypatch):
    root, revision, name, digest, _ = unit
    M.stage(name, digest, ".temp/positive-before", revision)
    target = root / "uv.lock"
    original = target.read_bytes()
    native_writer = M.write_validated_community

    def write_then_mutate(document, destination):
        native_writer(document, destination)
        target.write_bytes(original + b"\n# real drift control\n")

    with monkeypatch.context() as injection:
        injection.setattr(M, "write_validated_community", write_then_mutate)
        try:
            with pytest.raises(ValueError, match="captured input or revision changed"):
                M.stage(name, digest, ".temp/refused", revision)
            assert target.read_bytes() != original
            assert not (root / ".temp/refused/receipt.json").exists()
            assert (root / M.TARGET).read_bytes() == ORIGINAL
        finally:
            target.write_bytes(original)
    M.stage(name, digest, ".temp/positive-after", revision)


@pytest.mark.parametrize(
    "mutation", ["missing-control", "reused-restoration", "planned-preparation"]
)
def test_incomplete_actual_control_chain_refuses_then_restores(unit, mutation):
    root, revision, name, digest, plan = unit
    M.prepare(name, digest, revision)
    changed = deepcopy(plan)
    prep_path = root / plan["preparation"]["path"]
    prep_raw = prep_path.read_bytes()
    if mutation == "missing-control":
        del changed["controls"]["wrong-cell"]
    elif mutation == "reused-restoration":
        changed["controls"]["restored"] = deepcopy(changed["controls"]["selected"])
    else:
        prep = json.loads(prep_raw)
        prep["plan"] = True
        changed["preparation"]["sha256"] = write(prep_path, M.encoded(prep))
    changed_sha = write(root / ".temp/incomplete.json", M.encoded(changed))
    try:
        with pytest.raises(ValueError):
            M.stage(".temp/incomplete.json", changed_sha, ".temp/refused", revision)
        assert not (root / ".temp/refused/receipt.json").exists()
        assert (root / M.TARGET).read_bytes() == ORIGINAL
    finally:
        prep_path.write_bytes(prep_raw)
    M.prepare(name, digest, revision)


def test_captured_overlap_and_revision_drift_refuse_then_restore(unit):
    root, revision, name, digest, _ = unit
    _, _, captured = M.prepare(name, digest, revision)
    lock = root / "uv.lock"
    original = lock.read_bytes()
    lock.write_bytes(original + b"\n# captured-input mutation\n")
    try:
        with pytest.raises(ValueError, match="pinned input differs"):
            M.capture(captured, lock, M.sha(lock.read_bytes()))
        with pytest.raises(ValueError, match="captured input or revision changed"):
            M.unchanged(captured, revision)
    finally:
        lock.write_bytes(original)
    M.unchanged(captured, revision)
    with pytest.raises(ValueError, match="exact current revision required"):
        M.prepare(name, digest, "0" * 40)
    M.prepare(name, digest, revision)


@pytest.mark.parametrize("which", ["source", "installed"])
def test_runtime_membership_drift_after_capture_refuses_then_restores(unit, monkeypatch, which):
    root, revision, name, digest, _ = unit
    M.stage(name, digest, ".temp/positive-before", revision)
    package = root / (
        "src/linkml_reference_validator"
        if which == "source"
        else ".temp/installed/linkml_reference_validator"
    )
    extra = package / "unexpected.py"
    native_writer = M.write_validated_community

    def write_then_add(document, destination):
        native_writer(document, destination)
        extra.write_bytes(b"# actual unaccounted runtime member\n")

    with monkeypatch.context() as injection:
        injection.setattr(M, "write_validated_community", write_then_add)
        try:
            with pytest.raises(ValueError, match="captured runtime membership changed"):
                M.stage(name, digest, ".temp/refused", revision)
            assert extra.is_file()
            assert not (root / ".temp/refused/receipt.json").exists()
            assert (root / M.TARGET).read_bytes() == ORIGINAL
        finally:
            extra.unlink()
    M.stage(name, digest, ".temp/positive-after", revision)
