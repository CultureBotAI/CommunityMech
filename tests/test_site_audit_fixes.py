"""Regression contracts for public links, scientific scope, and mobile controls."""

import json
import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

from communitymech.render import CommunityRenderer, reference_link, reference_url

ROOT = Path(__file__).resolve().parents[1]


def test_reference_resolvers_preserve_pinned_github_paths_and_identifiers():
    github = "GITHUB:owner/repository/blob/abc123/script.py"
    assert reference_url(github) == "https://github.com/owner/repository/blob/abc123/script.py"
    assert (
        reference_url("doi:10.21203/rs.3.rs-7812930/v1")
        == "https://doi.org/10.21203/rs.3.rs-7812930/v1"
    )
    assert reference_url("PMID:38515239") == "https://pubmed.ncbi.nlm.nih.gov/38515239/"
    assert reference_url("CultureMech:003277").endswith("/pages/normalized/003277.html")
    assert reference_url("CultureMech:uncertain") == ""
    assert "href=" not in reference_link("javascript:alert(1)")
    assert "<script>" not in reference_link("<script>")


def test_rendered_record_exposes_distinct_curated_and_ontology_names_and_source_links():
    renderer = CommunityRenderer()
    html = renderer.render_community(
        ROOT / "kb/communities/ANME_SRB_Marine_Methane_Seep_Consortium.yaml"
    )
    assert "anaerobic methanotrophic archaea" in html
    assert "ontology label: Archaea" in html and "ontology label: sediment" in html
    html = renderer.render_community(ROOT / "kb/communities/Copper_Biomining_Heap_Leach.yaml")
    assert "CultureMech/pages/normalized/003277.html" in html
    assert "CultureMech/tree/main/kb/media/" not in html
    html = renderer.render_community(ROOT / "kb/communities/SPRUCE_Peatland_Warming_Community.yaml")
    assert "https://pubmed.ncbi.nlm.nih.gov/38515239/" in html
    html = renderer.render_community(
        ROOT / "kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml"
    )
    assert "https://github.com/Xinming9606/lignin_SynCom_proteomics/blob/" in html


def test_community_level_scope_never_infers_edges_from_membership():
    html = CommunityRenderer().render_community(
        ROOT / "kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml"
    )
    assert "membership alone does not imply an interaction" in html
    assert "No participant links are asserted" in html
    assert "The network could not be loaded" in html
    # This record has no participant assertions; a UI fix must not manufacture them.
    assert "links.push(" not in html


def test_browser_sort_is_case_insensitive_with_deterministic_ties(tmp_path):
    paths = []
    for i, name in enumerate(["Zymomonas", "hCom2", "mCAFEs", "HCOM2"]):
        p = tmp_path / f"{i}.yaml"
        p.write_text(yaml.safe_dump({"id": str(i), "name": name}))
        paths.append(p)
    CommunityRenderer()._generate_index(paths, tmp_path / "docs/communities")
    html = (tmp_path / "docs/browser.html").read_text()
    names = re.findall(r'class="community-card"[\s\S]*?<h2>([^<]+)</h2>', html)
    assert names == ["hCom2", "HCOM2", "mCAFEs", "Zymomonas"]
    assert html.index('id="results-count"') > html.index('class="content-area"')


def test_retained_map_fallback_is_initialized_before_plot_dependency():
    template = Environment(
        loader=FileSystemLoader(ROOT / "src/communitymech/templates"), autoescape=True
    ).get_template("community_umap.html")
    html = template.render(
        community_data_json=json.dumps(
            [{"id": "one", "name": "One", "url": "communities/One.html"}]
        ),
        num_communities=1,
        projection_label="PaCMAP",
    )
    assert (
        html.index("function buildDataTable")
        < html.index("if (typeof d3 === 'undefined')")
        < html.index("d3.symbolCircle")
    )
    assert '<label for="search">Search communities</label>' in html
    assert 'href="https://culturebotai.github.io/mechs/"' in html
    assert "complete plotted dataset in the table" in html
