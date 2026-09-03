"""Landing-page statistics navigate to the views that explain them."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_every_landing_stat_is_a_link_to_a_matching_view():
    template = (ROOT / "src" / "communitymech" / "templates" / "landing.html").read_text(
        encoding="utf-8"
    )

    assert '<div class="stat">' not in template
    assert '<a class="stat" href="browser.html">' in template
    assert '<a class="stat" href="browser.html#category-facet">' in template
    assert '<a class="stat" href="community_umap.html">' in template
    assert "a.stat:focus-visible" in template
