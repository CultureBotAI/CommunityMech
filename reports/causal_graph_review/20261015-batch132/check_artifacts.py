"""Verify the corrected identity reaches generated HTML and KGX without old-ID links."""

import csv
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[3]
SPECIES = "NCBITaxon:3723519"
OLD = "NCBITaxon:1807132"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.taxa = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        href = dict(attrs).get("href", "")
        parsed = urlparse(href)
        if parsed.netloc == "www.ncbi.nlm.nih.gov" and parsed.path.startswith("/Taxonomy/"):
            self.taxa.extend(parse_qs(parsed.query).get("id", []))


page = ROOT / "docs/communities/Phormidium_Alkaline_Consortium.html"
html = page.read_text()
links = Links()
links.feed(html)
assert "3723519" in links.taxa and "1807132" not in links.taxa
assert 'id: "' + SPECIES + '"' in html
assert 'id: "' + OLD + '"' not in html
assert "Candidatus Phormidium alkaliphilum" in html
with (ROOT / "output/kgx/nodes.tsv").open() as handle:
    nodes = {r["id"]: r for r in csv.DictReader(handle, delimiter="\t")}
assert nodes[SPECIES]["name"] == "Candidatus Sodalinema alkaliphilum"
assert OLD not in nodes
with (ROOT / "output/kgx/edges.tsv").open() as handle:
    edges = list(csv.DictReader(handle, delimiter="\t"))
assert any(e["subject"] == "CommunityMech:000054" and e["object"] == SPECIES for e in edges)
assert not any(OLD in (e["subject"], e["object"]) for e in edges)
print(
    json.dumps(
        {
            "html": str(page.relative_to(ROOT)),
            "taxonomy_link": "3723519",
            "graph_node_id": SPECIES,
            "source_name_retained": True,
            "kgx_name": nodes[SPECIES]["name"],
            "kgx_member_edge_present": True,
            "old_taxon_absent_from_generated_identity_links_nodes_and_edges": True,
            "limit": "Historical notes may name the former identifier; this checks active links and identities, not all text occurrences.",
        },
        indent=2,
    )
)
