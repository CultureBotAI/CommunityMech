"""The active page template must retain causal explanations and uncertainty (#1238)."""

from html import escape

import pytest
import yaml

from communitymech.render import CommunityRenderer


def render(tmp_path, descriptions=True):
    source = {"name": "Source process", "downstream": [{"target": "Target process"}]}
    target = {"name": "Target process"}
    if descriptions:
        source["description"] = "PARTIAL - source process remains <uncertain> & unisolated."
        source["downstream"][0][
            "description"
        ] = "HYPOTHESIZED - this arrow is not a measured <transfer>."
        target["description"] = "Observed endpoint without an isolated causal mechanism."
    path = tmp_path / "community.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "id": "CommunityMech:999999",
                "name": "Causal publication fixture",
                "taxonomy": [],
                "ecological_interactions": [source, target],
            }
        )
    )
    return CommunityRenderer().render_community(path), source, target


def test_node_descriptions_stay_with_their_interactions(tmp_path):
    html, source, target = render(tmp_path)
    cards = html.split('<div class="interaction-card">')[1:]
    assert len(cards) == 2
    for card, node in zip(cards, (source, target), strict=True):
        assert escape(node["description"]) in card
    assert escape(target["description"]) not in cards[0]


def test_edge_description_is_visible_with_its_target(tmp_path):
    html, source, _ = render(tmp_path)
    flow = html.split('<div class="flow-item">', 1)[1].split("</div>", 1)[0]
    assert "Target process" in flow
    assert escape(source["downstream"][0]["description"]) in flow
    assert "<transfer>" not in html


def test_absent_descriptions_do_not_render_empty_paragraphs(tmp_path):
    html, _, _ = render(tmp_path, descriptions=False)
    assert "<h3>Source process</h3>" in html
    assert 'class="prewrap interaction-description"' not in html
    assert 'class="prewrap causal-description"' not in html
    assert "Undefined" not in html


@pytest.mark.parametrize("field", ["description", "downstream"])
def test_description_html_is_escaped(tmp_path, field):
    html, _, _ = render(tmp_path)
    expected = "&lt;uncertain&gt; &amp;" if field == "description" else "&lt;transfer&gt;"
    assert expected in html
