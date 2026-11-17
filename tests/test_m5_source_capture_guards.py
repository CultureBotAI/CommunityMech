"""Protect M5 evidence captures cited by immutable reviews (#2780, 2026-11-14).

Inputs: the three one-off fetch helpers and mocked primary-source responses.
Outputs: isolated temporary captures only; no network or repository evidence writes.
"""

import hashlib
import importlib.util
import io
import json
from functools import partial
from pathlib import Path
from unittest.mock import Mock

import pytest

ROOT = Path(__file__).resolve().parents[1]
CASES = ("dopamine", "ecofab", "relations")


def configured_helper(kind, tmp_path, monkeypatch):
    names = {
        "dopamine": "review_dopamine_syncom_20261114",
        "ecofab": "verify_ecofab_primary_sources_20261114",
        "relations": "fetch_ecofab_relation_sources",
    }
    spec = importlib.util.spec_from_file_location(
        "capture_guard_" + kind, ROOT / "scripts/adhoc" / (names[kind] + ".py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if kind == "dopamine":
        monkeypatch.setattr(module, "STATE", tmp_path)
        folder = tmp_path / "dopamine-syncom-sources"
        folder.mkdir()
        files = [
            folder / "supplement.pdf",
            folder / "supplement.pdf.source.json",
            folder / "supplement.txt",
        ]
        invoke = partial(module.fetch, "supplement.pdf")
    elif kind == "ecofab":
        monkeypatch.setattr(module, "DEST", tmp_path)
        monkeypatch.setattr("sys.argv", [names[kind], "ring-main.xml"])
        files = [
            tmp_path / "ring-main.xml",
            tmp_path / "ring-main.xml.source.json",
            tmp_path / "ring-main.txt",
        ]
        invoke = module.main
    else:
        monkeypatch.setattr(module, "OUT", tmp_path)
        monkeypatch.setattr("sys.argv", [names[kind], "PMC13522444"])
        files = [
            tmp_path / "PMC13522444.xml",
            tmp_path / "PMC13522444-paragraphs.json",
            tmp_path / "PMC13522444-retrieval.json",
        ]
        invoke = module.main
    return module, files, invoke


@pytest.mark.parametrize("kind", CASES)
@pytest.mark.parametrize("existing_indices", [(0, 1, 2), (0,), (1,), (2,)])
def test_existing_capture_is_rejected_before_network_without_changes(
    kind, existing_indices, tmp_path, monkeypatch
):
    module, files, invoke = configured_helper(kind, tmp_path, monkeypatch)
    before = {}
    for index in existing_indices:
        path = files[index]
        path.write_bytes(f"retained original evidence {index}\n".encode())
        before[path] = (path.read_bytes(), path.stat().st_mtime_ns)
    network = Mock(side_effect=AssertionError("must reject before network access"))
    monkeypatch.setattr(module.urllib.request, "urlopen", network)

    state = "complete" if len(existing_indices) == len(files) else "partial"
    with pytest.raises(ValueError, match=f"retained {state} source capture"):
        invoke()

    network.assert_not_called()
    for path in files:
        if path in before:
            assert (path.read_bytes(), path.stat().st_mtime_ns) == before[path]
        else:
            assert not path.exists()


@pytest.mark.parametrize("kind", CASES)
def test_new_capture_still_persists_source_and_hash_receipt(kind, tmp_path, monkeypatch):
    module, files, invoke = configured_helper(kind, tmp_path, monkeypatch)
    payload = (
        b"<article><sec><title>Results</title><p>"
        + b"source evidence " * 1000
        + b"</p></sec></article>"
    )
    if kind == "dopamine":
        # A figure exercises the real fetch/save path without invoking a PDF converter.
        files = [files[0].parent / "fig2.png", files[0].parent / "fig2.png.source.json"]
        invoke = partial(module.fetch, "fig2.png")
        payload = b"\x89PNG\r\n\x1a\nmock source figure"
    response = io.BytesIO(payload)
    response.headers = {"Content-Type": "application/octet-stream"}
    response.geturl = lambda: "https://example.org/source"
    network = Mock(return_value=response)
    monkeypatch.setattr(module.urllib.request, "urlopen", network)

    invoke()

    network.assert_called_once()
    assert files[0].read_bytes() == payload
    receipt_path = files[2] if kind == "relations" else files[1]
    receipt = json.loads(receipt_path.read_text())
    assert receipt["sha256"] == hashlib.sha256(payload).hexdigest()
    assert receipt["bytes"] == len(payload)
    assert receipt["retrieved_at"]
    assert all(path.is_file() and path.stat().st_size for path in files)
