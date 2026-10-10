"""The maintained static detail shell keeps every table keyboard-accessible."""

from html.parser import HTMLParser
from pathlib import Path

import yaml

from communitymech.render import CommunityRenderer


class TableParents(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.divs = []
        self.tables = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.divs.append(dict(attrs))
        elif tag == "table":
            self.tables.append(self.divs[-1] if self.divs else {})

    def handle_endtag(self, tag):
        if tag == "div":
            self.divs.pop()


def test_all_record_table_families_have_named_keyboard_scroll_regions():
    root = Path(__file__).resolve().parents[1]
    community = yaml.safe_load(
        (root / "kb/communities/AMD_Acidophile_Heterotroph_Network.yaml").read_text()
    )
    community["associated_datasets"] = [
        {"title": "Study", "accession": "PRJNA123", "url": "https://example.org/study"}
    ]
    community["external_resources"] = [
        {"name": "Resource", "resource_id": "RESOURCE:123", "url": "https://example.org/source"}
    ]
    community["growth_media"] = [
        {"name": 'Medium "A" <B>', "composition": [{"name": "Glucose", "concentration": 1}]}
    ]
    html = (
        CommunityRenderer()
        .env.get_template("community.html")
        .render(community=community, source_file="fixture.yaml")
    )
    parents = TableParents(html).tables
    assert len(parents) == 5
    assert [p.get("aria-label") for p in parents] == [
        "Taxonomy",
        "Associated Datasets",
        "External Resources",
        "Environmental Factors",
        'Medium "A" <B> composition',
    ]
    for parent in parents:
        assert parent.get("class") == "table-scroll"
        assert parent.get("role") == "region"
        assert parent.get("tabindex") == "0"
    # These remain ordinary populated HTML tables, available without JavaScript.
    for value in ["NCBITaxon:62140", "PRJNA123", "RESOURCE:123", "Glucose"]:
        assert value in html
    assert 'href="https://example.org/study"' in html
    assert 'href="https://example.org/source"' in html
