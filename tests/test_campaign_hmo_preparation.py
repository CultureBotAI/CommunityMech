"""Guard source identity and private canary planning without network, 2026-11-15."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "hmo_source_prep", ROOT / "scripts/adhoc/fetch_campaign_hmo_primary_20261115.py"
)
SOURCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOURCE)
GATE_SPEC = importlib.util.spec_from_file_location(
    "hmo_gate_prep", ROOT / "scripts/adhoc/check_campaign_hmo_canary_20261115.py"
)
GATE = importlib.util.module_from_spec(GATE_SPEC)
GATE_SPEC.loader.exec_module(GATE)


def payload(pmid="42020426", doi="10.1038/s41467-026-71764-7", pmc="PMC13103366", body=True):
    middle = (
        '<body><sec id="results"><title>Results</title><p>'
        + "test context " * 1000
        + '</p></sec><sec id="methods"><title>Methods</title><p>Methods.</p></sec></body>'
        if body
        else "<abstract>" + "test context " * 1000 + "</abstract>"
    )
    return (
        '<article><front><article-meta><article-id pub-id-type="pmid">'
        + pmid
        + '</article-id><article-id pub-id-type="doi">'
        + doi
        + '</article-id><article-id pub-id-type="pmc">'
        + pmc
        + "</article-id><title-group><article-title>Fixture article</article-title></title-group>"
        + "</article-meta></front>"
        + middle
        + "</article>"
    ).encode()


def test_expected_primary_identity_and_body():
    result = SOURCE.inspect_primary(payload())
    assert result["identity"]["pmid"] == "42020426"
    assert len(result["paragraphs"]) == 2
    assert result["sections"] == ["Results", "Methods"]


@pytest.mark.parametrize(
    "override", [{"pmid": "1"}, {"doi": "10.0000/wrong"}, {"pmc": "PMC1"}, {"body": False}]
)
def test_wrong_primary_is_rejected(override):
    with pytest.raises(ValueError):
        SOURCE.inspect_primary(payload(**override))


def test_html_is_not_article():
    with pytest.raises(ValueError):
        SOURCE.inspect_primary(b"<html>" + b"challenge " * 2000 + b"</html>")


def test_existing_output_refused_before_network(tmp_path, monkeypatch):
    monkeypatch.setattr(SOURCE, "STATE", tmp_path)
    destination = tmp_path / "existing"
    destination.mkdir()
    marker = destination / "keep"
    marker.write_bytes(b"unchanged")
    monkeypatch.setattr(
        SOURCE.urllib.request, "urlopen", lambda *a, **kw: pytest.fail("network reached")
    )
    with pytest.raises(ValueError, match="exclusive"):
        SOURCE.prepare(destination, "unused", False)
    assert marker.read_bytes() == b"unchanged"


def test_external_output_refused_before_network(tmp_path, monkeypatch):
    monkeypatch.setattr(SOURCE, "STATE", tmp_path / "private")
    monkeypatch.setattr(
        SOURCE.urllib.request, "urlopen", lambda *a, **kw: pytest.fail("network reached")
    )
    with pytest.raises(ValueError, match="exclusive"):
        SOURCE.prepare(tmp_path / "outside", "unused", False)
    assert not (tmp_path / "outside").exists()


@pytest.mark.parametrize("defect", [None, "revision", "identity", "source"])
def test_gate_preflight_binds_one_source_record(tmp_path, monkeypatch, defect):
    monkeypatch.setattr(GATE, "ROOT", tmp_path)
    monkeypatch.setattr(GATE, "STATE", tmp_path)
    monkeypatch.setattr(GATE.subprocess, "check_output", lambda *a, **kw: "a" * 40)
    target = tmp_path / GATE.TARGET
    target.parent.mkdir(parents=True)
    target.write_text(
        "id: "
        + ("CommunityMech:wrong" if defect == "identity" else "CommunityMech:000296")
        + "\nevidence:\n- reference: "
        + ("PMID:1" if defect == "source" else "PMID:42020426")
        + "\n"
    )
    revision = "b" * 40 if defect == "revision" else "a" * 40
    if defect:
        with pytest.raises(ValueError):
            GATE.preflight(revision)
    else:
        assert GATE.preflight(revision) == revision
