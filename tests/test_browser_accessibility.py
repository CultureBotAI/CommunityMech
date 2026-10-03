from html.parser import HTMLParser
from pathlib import Path


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.items = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.items.append((tag, dict(attrs)))

    def find(self, tag=None, **attrs):
        return [
            a
            for t, a in self.items
            if (tag is None or t == tag)
            and all(a.get(k.rstrip("_").replace("_", "-")) == v for k, v in attrs.items())
        ]


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = "https://culturebotai.github.io/mechs/"


def test_browser_has_keyboard_disclosures_labels_and_result_status():
    from communitymech.render import CommunityRenderer

    html = CommunityRenderer().env.get_template("index.html").render(communities=[])
    dom = Elements(html)
    assert dom.find("label", for_="search")  # explicit persistent search name
    assert dom.find(role="status", aria_live="polite", aria_atomic="true")
    disclosures = [a for tag, a in dom.items if "aria-controls" in a]
    assert len(disclosures) == 5
    for control in disclosures:
        assert dom.find("button", aria_controls=control["aria-controls"])
        assert control["aria-expanded"] in {"true", "false"}
        assert dom.find(id=control["aria-controls"])
    assert dom.find("a", href=DIRECTORY)


def test_category_stat_uses_the_same_input_population_as_the_browser(tmp_path):
    import yaml

    from communitymech.render import CommunityRenderer

    records = []
    for i, category in enumerate(["AMD", "AMD", "OTHER", ""]):
        path = tmp_path / f"community-{i}.yaml"
        path.write_text(
            yaml.safe_dump({"id": str(i), "name": str(i), "community_category": category})
        )
        records.append(path)
    CommunityRenderer()._generate_index(records, tmp_path / "docs" / "communities")
    landing = (tmp_path / "docs" / "index.html").read_text()
    assert "<b>2</b><span>categories</span>" in landing
    assert "<b>4</b>" in landing
    assert DIRECTORY in landing


def test_browser_javascript_parses(tmp_path):
    import re
    import shutil
    import subprocess

    import pytest

    from communitymech.render import CommunityRenderer

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser JavaScript syntax check")
    html = CommunityRenderer().env.get_template("index.html").render(communities=[])
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL)
    assert scripts
    for number, script in enumerate(scripts):
        source = tmp_path / f"inline-{number}.js"
        source.write_text(script)
        checked = subprocess.run([node, "--check", str(source)], capture_output=True, text=True)
        assert checked.returncode == 0, checked.stderr
