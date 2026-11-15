"""Public rendering regressions from the Phase 2 review (#2705–#2707)."""

import re

import pytest
import yaml

from communitymech.paths import DATA_ISOLATES
from communitymech.render import CommunityRenderer


def render_section(**fields):
    return (
        CommunityRenderer()
        .env.get_template("community.html")
        .render(
            community={"id": "CommunityMech:999999", "name": "Rendering control", **fields},
            source_file="control.yaml",
            related_pages={},
        )
    )


@pytest.mark.parametrize(
    "location, expected",
    [
        ({"place_name": "Field"}, "Field"),
        ({"latitude": 38.5, "place_name": "Field"}, "Field"),
        ({"longitude": -121.5, "place_name": "Field"}, "Field"),
        ({"latitude": None, "longitude": None, "place_name": "Field"}, "Field"),
        ({"latitude": 38.5, "longitude": -121.5}, "(38.5, -121.5)"),
        ({"latitude": 0, "longitude": 0}, "(0, 0)"),
    ],
)
def test_soil_coordinates_require_both_numbers_and_preserve_zero(location, expected):
    html = render_section(soils=[{"preferred_term": "Soil", "location": location}])
    value = re.search(r"<dt>Location</dt><dd>(.*?)</dd>", html, re.S).group(1)
    assert " ".join(value.split()) == expected


@pytest.mark.parametrize("with_term", [False, True])
def test_developmental_stage_qualifier_is_visible_and_escaped(with_term):
    stage = {"preferred_term": "seedling", "description": "Four days <not four weeks>"}
    if with_term:
        stage["term"] = {"id": "PO:0007131", "label": "seedling development stage"}
    html = render_section(host={"preferred_term": "Plant", "developmental_stage": stage})
    assert "Four days &lt;not four weeks&gt;" in html
    assert "<not four weeks>" not in html
    assert ("PO:0007131" in html) == with_term


def test_absent_stage_qualifier_leaves_no_placeholder():
    html = render_section(
        host={"preferred_term": "Plant", "developmental_stage": {"preferred_term": "seedling"}}
    )
    paragraph = re.search(r"<p><strong>Developmental stage:</strong>(.*?)</p>", html, re.S)
    assert " ".join(paragraph.group(1).split()) == "seedling"


def test_links_only_name_pages_in_the_current_render_population(tmp_path, monkeypatch):
    isolate = next(
        path
        for path in DATA_ISOLATES.glob("*.yaml")
        if yaml.safe_load(path.read_text())["id"] == "CommunityMech:000488"
    )
    source = tmp_path / "source"
    source.mkdir()
    output = tmp_path / "fresh" / "communities"
    records = {
        "first": {
            "id": "CommunityMech:999991",
            "name": "First",
            "related_communities": [
                {"identifier": "CommunityMech:999992", "relation": "SAME_STUDY_AS"},
                {"identifier": "CommunityMech:000488", "relation": "SAME_STUDY_AS"},
            ],
        },
        "second": {"id": "CommunityMech:999992", "name": "Second"},
    }
    for stem, record in records.items():
        (source / f"{stem}.yaml").write_text(yaml.safe_dump(record))
    renderer = CommunityRenderer()
    monkeypatch.setattr(renderer, "_generate_index", lambda *args: None)
    assert renderer.render_all(source, output) == []
    html = (output / "first.html").read_text()
    assert 'href="second.html"' in html
    assert "CommunityMech:000488" in html
    assert f'href="{isolate.stem}.html"' not in html
    assert (output / "second.html").stat().st_size > 0
    # A second run with a narrower population must not reuse a cached registry.
    (source / "second.yaml").unlink()
    assert renderer.render_all(source, output) == []
    assert 'href="second.html"' not in (output / "first.html").read_text()
    # A standalone rendering declares no neighboring generated pages.
    assert 'href="second.html"' not in renderer.render_community(source / "first.yaml")
