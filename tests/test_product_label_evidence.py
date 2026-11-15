"""Product evidence rejects changed retained bytes and incomplete native gates."""

import importlib.util
import json
from pathlib import Path

import pytest


@pytest.fixture
def staged(tmp_path, monkeypatch):
    helpers = Path(__file__).resolve().parents[1] / "scripts/adhoc"
    monkeypatch.syspath_prepend(str(helpers))
    spec = importlib.util.spec_from_file_location(
        "product_evidence", helpers / "export_product_label_evidence_20261115.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repo"
    state = root / ".temp/product-labels-20261115"
    run = state / "canary-001"
    run.mkdir(parents=True)
    products = state / "canary-001-products"
    products.mkdir()
    python = "/private/test/.venv/bin/python"
    commands = [
        [python, "-m", "communitymech.render", "kb/communities/" + module.CANARY],
        [
            python,
            "-m",
            "communitymech.export",
            "--kb",
            "kb/communities",
            "--output",
            "output/kgx",
            "--record",
            module.CANARY,
        ],
        [python, "-m", "communitymech.export.validate_kgx", "--strict"],
        [
            "/opt/homebrew/bin/just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            "validate-products",
        ],
    ]
    receipt = {
        "mode": "canary",
        "validate_labels": True,
        "revision": module.PIN,
        "started_at": "2026-11-15T00:00:00+00:00",
        "finished_at": "2026-11-15T00:01:00+00:00",
        "exit_code": 0,
        "implementation": {},
        "products": {},
        "commands": [
            {"name": n, "argv": c, "exit_code": 0}
            for n, c in zip(module.NAMES, commands, strict=True)
        ],
    }
    for name in module.PRODUCTS:
        raw = name.encode()
        (products / Path(name).name).write_bytes(raw)
        receipt["products"][name] = {"sha256": module.digest(raw), "bytes": len(raw)}
    for name in module.NAMES:
        (run / (name + ".log.txt")).write_text("All id↔label pairs correspond.\n")
    (run / "receipt.json").write_text(json.dumps(receipt))

    def bind():
        paths = sorted([*run.iterdir(), *products.iterdir()])
        (state / "m5-raw-checksums-001.txt").write_text(
            "".join(f"{module.digest(p.read_bytes())}  {p.relative_to(root)}\n" for p in paths)
        )

    bind()
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "STATE", state)
    return module, run, products, bind


def test_changed_product_refused_even_with_new_host_checksum(staged):
    module, _run, products, bind = staged
    assert len(module.prepare("canary-001")) == 5
    product = products / "nodes.tsv"
    original = product.read_bytes()
    product.write_bytes(b"changed product")
    with pytest.raises(ValueError, match="execution-host evidence"):
        module.prepare("canary-001")
    bind()
    with pytest.raises(ValueError, match="product does not match"):
        module.prepare("canary-001")
    product.write_bytes(original)
    bind()
    assert len(module.prepare("canary-001")) == 5


def test_native_skip_is_not_success_even_with_zero_exit(staged):
    module, run, _products, bind = staged
    path = run / "validate-labels.log.txt"
    original = path.read_bytes()
    assert len(module.prepare("canary-001")) == 5
    path.write_text("SKIPPED, NOT PASSED\nAll id↔label pairs correspond.\n")
    bind()
    with pytest.raises(ValueError, match="not completed successfully"):
        module.prepare("canary-001")
    path.write_bytes(original)
    bind()
    assert len(module.prepare("canary-001")) == 5
