"""Existing local discussion previews link to actual record sections."""

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def test_every_discussion_preview_link_resolves_to_a_published_record_section():
    source = (ROOT / "app/discussions/data.js").read_text()
    records = json.loads(
        re.search(r"window.searchData = (.*?);\nwindow.searchMetrics", source, re.S).group(1)
    )
    assert records
    for record in records:
        url = urlsplit(record["page_url"])
        target = (ROOT / "app/discussions" / url.path).resolve()
        assert target.is_relative_to(ROOT / "docs/communities")
        assert url.fragment == "discussions"
        assert 'id="discussions"' in target.read_text()
