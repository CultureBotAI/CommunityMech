"""Refresh retained map wrappers without recomputing or changing scientific points.

Run from the repository root: python scripts/refresh_retained_map_pages.py
New embedding builds use the same community_umap.html template through
communitymech.visualization.umap_generator. This command updates both committed
historic maps when only their wrapper changes.
"""

import json
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    env = Environment(
        loader=FileSystemLoader(ROOT / "src/communitymech/templates"), autoescape=True
    )
    for name, label in [("community_umap.html", "PaCMAP"), ("community_graph.html", "Layout")]:
        path = ROOT / "docs" / name
        text = path.read_text()
        match = re.search(r"const communityData\s*=\s*", text)
        if match is None:
            raise ValueError(f"No retained point data in {path}")
        data, _ = json.JSONDecoder().raw_decode(text[match.end() :])
        rendered = env.get_template("community_umap.html").render(
            community_data_json=json.dumps(data, indent=2),
            num_communities=len(data),
            projection_label=label,
        )
        if label == "Layout":
            rendered = rendered.replace(
                "Community Embedding Space", "Community Graph Layout"
            ).replace("2D projection of", "Retained graph layout of")
        # Template uses |safe for embedded JSON. Verify exact payload before write.
        marker = re.search(r"const communityData\s*=\s*", rendered)
        if marker is None or json.JSONDecoder().raw_decode(rendered[marker.end() :])[0] != data:
            raise ValueError(f"Point data changed while refreshing {path}")
        path.write_text(rendered)
        print(f"{path.relative_to(ROOT)}: preserved {len(data)} points")


if __name__ == "__main__":
    main()
