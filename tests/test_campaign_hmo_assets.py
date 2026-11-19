"""Offline guards for the #1428/#2828/#2843 primary-asset capture, 2026-11-15."""

import importlib.util
import io
from pathlib import Path

import pytest
from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/adhoc/fetch_campaign_hmo_assets_20261115.py"
SPEC = importlib.util.spec_from_file_location("hmo_assets", SCRIPT)
assert SPEC and SPEC.loader
assets = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(assets)


def test_only_exact_retained_primary_routes_are_admitted(monkeypatch):
    payload = b"""<article xmlns:xlink="http://www.w3.org/1999/xlink"><body><fig id="Fig4">
    <alternatives><graphic content-type="image" xlink:href="41467_2026_71764_Fig4_HTML.jpg">
    <?cloudpmc-path blobs/be48/13103366/3cf711379ff3/41467_2026_71764_Fig4_HTML.jpg?>
    <?original-width 1988?><?original-height 1189?>
    <?scaled-width 795?><?scaled-height 475?></graphic>
    </alternatives></fig></body></article>"""
    monkeypatch.setattr(assets, "ARTICLE_SHA", assets.sha(payload))
    plan = assets.asset_plan(payload, "Fig4")
    assert (
        plan["url"]
        == "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/be48/13103366/3cf711379ff3/41467_2026_71764_Fig4_HTML.jpg"
    )
    assert plan["expected_dimensions"] == [1988, 1189]
    assert plan["expected_scaled_dimensions"] == [795, 475]
    with pytest.raises(ValueError, match="wrong retained"):
        assets.asset_plan(payload + b" ", "Fig4")
    mutated = payload.replace(b"blobs/be48/13103366", b"blobs/be48/99999999")
    monkeypatch.setattr(assets, "ARTICLE_SHA", assets.sha(mutated))
    with pytest.raises(ValueError, match="primary figure route"):
        assets.asset_plan(mutated, "Fig4")


@pytest.mark.parametrize(
    "url",
    [
        "http://cdn.ncbi.nlm.nih.gov/pmc/x.jpg",
        "https://example.com/x.jpg",
        "https://cdn.ncbi.nlm.nih.gov/pmc/x.jpg?token=secret",
        "https://person:password@cdn.ncbi.nlm.nih.gov/pmc/x.jpg",
    ],
)
def test_external_or_credential_bearing_redirects_refuse(url):
    with pytest.raises(ValueError, match="fixed anonymous"):
        assets.checked_url(url)


def test_actual_image_control_rejects_html_size_and_dimension_mismatches():
    stream = io.BytesIO()
    Image.new("RGB", (10, 12), "white").save(stream, format="JPEG")
    raw = stream.getvalue()
    plan = {"filename": "figure.jpg", "expected_bytes": len(raw), "expected_dimensions": [10, 12]}
    assert assets.inspect_format(raw, plan, "image/jpeg")[0]["dimensions"] == [10, 12]
    with pytest.raises(ValueError, match="text response"):
        assets.inspect_format(b"<html>challenge</html>", plan, "text/html")
    with pytest.raises(ValueError, match="byte count"):
        assets.inspect_format(raw[:-1], plan, "image/jpeg")
    with pytest.raises(ValueError, match="dimensions"):
        assets.inspect_format(raw, {**plan, "expected_dimensions": [11, 12]}, "image/jpeg")
    assert assets.inspect_format(raw, plan, "image/jpeg")[0]["format"] == "JPEG"


def test_only_explicit_original_or_scaled_dimensions_are_accepted():
    plan = {
        "filename": "figure.jpg",
        "expected_bytes": None,
        "expected_dimensions": [10, 12],
        "expected_scaled_dimensions": [5, 6],
    }
    for size, rendition in [((10, 12), "original"), ((5, 6), "scaled")]:
        stream = io.BytesIO()
        Image.new("RGB", size, "white").save(stream, format="JPEG")
        assert (
            assets.inspect_format(stream.getvalue(), plan, "image/jpeg")[0]["rendition"]
            == rendition
        )
    raw = stream.getvalue()
    with pytest.raises(ValueError, match="dimensions"):
        assets.inspect_format(raw, {**plan, "expected_scaled_dimensions": [7, 8]}, "image/jpeg")
    with pytest.raises(ValueError, match="dimensions"):
        assets.inspect_format(raw, {**plan, "expected_scaled_dimensions": None}, "image/jpeg")
    assert assets.inspect_format(raw, plan, "image/jpeg")[0]["rendition"] == "scaled"
