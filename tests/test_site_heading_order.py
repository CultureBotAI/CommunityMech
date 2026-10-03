"""Keep the browser and existing map facet headings in document order."""

from html.parser import HTMLParser
from itertools import pairwise
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]


class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.levels = []

    def handle_starttag(self, tag, attrs):
        if len(tag) == 2 and tag[0] == "h" and tag[1] in "123456":
            self.levels.append(int(tag[1]))


def assert_heading_order(html):
    parser = HeadingParser()
    parser.feed(html)
    assert parser.levels and parser.levels[0] == 1
    assert all(
        current <= previous + 1 for previous, current in pairwise(parser.levels)
    ), parser.levels


@pytest.mark.parametrize("name", ["browser.html", "community_umap.html", "community_graph.html"])
def test_published_filter_pages_have_no_skipped_heading_levels(name):
    assert_heading_order((ROOT / "docs" / name).read_text())


@pytest.mark.parametrize("name", ["index.html", "community_umap.html"])
def test_filter_templates_render_without_skipped_heading_levels(name):
    env = Environment(
        loader=FileSystemLoader(ROOT / "src/communitymech/templates"), autoescape=True
    )
    html = env.get_template(name).render(
        communities=[], community_data_json="[]", num_communities=0, projection_label="PaCMAP"
    )
    assert_heading_order(html)
