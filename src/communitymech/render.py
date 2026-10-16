"""
HTML rendering for CommunityMech community pages.

Generates individual HTML pages for each community with full metadata,
taxonomy, ecological interactions, and evidence.
"""

import json
import re
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

from communitymech.paths import DOCS


@lru_cache(maxsize=1)
def culturemech_links() -> dict[str, str]:
    return json.loads(Path(__file__).with_name("culturemech-record-links.json").read_text())[
        "links"
    ]


def reference_url(reference: str | None) -> str:
    value = str(reference or "")
    if value.startswith(("https://", "http://")):
        return value
    if re.fullmatch(r"CultureMech:\d{6}", value):
        return culturemech_links().get(value, "")
    if value.startswith("PMID:") and value[5:].isdigit():
        return "https://pubmed.ncbi.nlm.nih.gov/" + value[5:] + "/"
    if re.match(r"(?i)^doi:10\.\d{4,9}/", value):
        return "https://doi.org/" + quote(value.split(":", 1)[1], safe="/():;._-")
    if re.match(r"^GITHUB:[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*(?:/|$)", value):
        return "https://github.com/" + quote(value[7:], safe="/")
    return ""


def reference_link(reference: str | None) -> Markup:
    url = reference_url(reference)
    if url:
        return Markup('<a href="{}" rel="noreferrer">{}</a>').format(url, reference or "")
    if str(reference or "").startswith("CultureMech:"):
        return Markup('{} <span class="muted">(record link unresolved)</span>').format(reference)
    return Markup("{}").format(reference or "")


def _strip_trailing_whitespace(html: str) -> str:
    return "\n".join(line.rstrip() for line in html.split("\n"))


class CommunityRenderer:
    """Render community YAML files to HTML pages."""

    def __init__(self, template_dir: Path | None = None):
        """
        Initialize renderer with Jinja2 environment.

        Args:
            template_dir: Path to templates directory (default: src/communitymech/templates)
        """
        if template_dir is None:
            # Default to templates directory relative to this file
            template_dir = Path(__file__).parent / "templates"

        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(["html", "xml"]),
        )
        self.env.filters["reference_link"] = reference_link
        self.env.globals["reference_url"] = reference_url

    def render_community(
        self,
        yaml_path: Path,
        output_path: Path | None = None,
    ) -> str:
        """
        Render a single community YAML to HTML.

        Args:
            yaml_path: Path to community YAML file
            output_path: Path to output HTML file (optional)

        Returns:
            Rendered HTML string
        """
        # Load community data
        with open(yaml_path) as f:
            community = yaml.safe_load(f)

        # Load template
        template = self.env.get_template("community.html")

        # Render
        html = template.render(
            community=community,
            source_file=yaml_path.name,
        )

        # Write to file if output path provided
        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(_strip_trailing_whitespace(html))
            print(f"  ✓ {yaml_path.name} → {output_path}")

        return html

    def render_all(
        self,
        communities_dir: Path = Path("kb/communities"),
        output_dir: Path | None = None,
    ) -> list[str]:
        """
        Render all community YAML files to HTML.

        Args:
            communities_dir: Directory containing community YAML files
            output_dir: Directory for output HTML files. Defaults to the repo's
                `docs/communities`, which is git-tracked — a cwd-relative default
                wrote a stray tree wherever the process ran (#407).

        Returns:
            The names of records that failed to render. Their pages are left as
            they were, so a caller that ignores this cannot tell a current tree
            from a stale one.
        """
        output_dir = output_dir if output_dir is not None else DOCS / "communities"
        yaml_files = sorted(communities_dir.glob("*.yaml"))

        print(f"\nRendering {len(yaml_files)} communities to HTML...")

        failed: list[str] = []
        for yaml_file in yaml_files:
            try:
                output_file = output_dir / f"{yaml_file.stem}.html"
                self.render_community(yaml_file, output_file)
            except Exception as e:
                print(f"  ✗ {yaml_file.name}: {e}")
                failed.append(yaml_file.name)

        # A swallowed failure used to leave the previous page in place and still
        # print "✅ Rendered 312", so `check-docs-current` saw no diff and
        # reported the tree current — green precisely when the regeneration it
        # gates on had not happened (#442 review). Report the real count and
        # exit non-zero.
        rendered = len(yaml_files) - len(failed)
        print(f"\n✅ Rendered {rendered} communities to {output_dir}")
        if failed:
            print(f"❌ {len(failed)} failed to render, so their pages are STALE: {failed}")

        # Generate index page
        self._generate_index(yaml_files, output_dir)

        return failed

    def _generate_index(
        self,
        yaml_files: list[Path],
        output_dir: Path,
    ) -> None:
        """Generate index.html listing all communities."""
        communities = []
        for yaml_file in yaml_files:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

                # Compute member count from taxonomy
                member_count = len(data.get("taxonomy", []))

                # Extract metal/REE data
                metals = data.get("metals_present", [])
                ree = data.get("rare_earth_elements_present", [])
                metal_relevance = data.get("metal_relevance", "NOT_APPLICABLE")

                communities.append(
                    {
                        "id": yaml_file.stem,
                        "name": data.get("name", ""),
                        "description": data.get("description", ""),
                        "ecological_state": data.get("ecological_state", ""),
                        "community_category": data.get("community_category", ""),
                        "member_count": member_count,
                        "metals_present": metals,
                        "rare_earth_elements_present": ree,
                        "metal_relevance": metal_relevance,
                    }
                )

        communities.sort(key=lambda row: (row["name"].casefold(), row["id"]))

        # Render the faceted browser (templates/index.html) to docs/browser.html
        browser_template = self.env.get_template("index.html")
        browser_html = browser_template.render(communities=communities)

        browser_path = output_dir.parent / "browser.html"  # docs/browser.html
        browser_path.parent.mkdir(parents=True, exist_ok=True)
        with open(browser_path, "w") as f:
            f.write(_strip_trailing_whitespace(browser_html))

        print(f"  ✓ Generated browser at {browser_path}")

        # Render the landing page (templates/landing.html) to docs/index.html
        landing_template = self.env.get_template("landing.html")
        landing_html = landing_template.render(
            num_communities=len(communities),
            num_categories=len(
                {c["community_category"] for c in communities if c["community_category"]}
            ),
        )

        index_path = output_dir.parent / "index.html"  # docs/index.html
        with open(index_path, "w") as f:
            f.write(_strip_trailing_whitespace(landing_html))

        print(f"  ✓ Generated landing at {index_path}")

        self._generate_downloads(communities, output_dir.parent)
        self._generate_schema_and_404(len(communities), output_dir.parent)
        self._generate_embedding_maps(yaml_files, output_dir)

    def _generate_downloads(
        self,
        communities: list[dict],
        docs_dir: Path,
    ) -> None:
        """Write docs/communities.json and docs/communities.tsv."""
        import csv

        json_path = docs_dir / "communities.json"
        json_path.write_text(
            json.dumps(communities, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        tsv_path = docs_dir / "communities.tsv"
        fieldnames = [
            "id",
            "name",
            "community_category",
            "ecological_state",
            "member_count",
            "metal_relevance",
            "metals_present",
            "rare_earth_elements_present",
            "description",
        ]
        with open(tsv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter="\t", lineterminator="\n")
            writer.writerow(fieldnames)
            for row in communities:
                writer.writerow(
                    [
                        row.get("id", ""),
                        row.get("name", ""),
                        row.get("community_category", ""),
                        row.get("ecological_state", ""),
                        row.get("member_count", 0),
                        row.get("metal_relevance", ""),
                        ";".join(str(x) for x in (row.get("metals_present") or [])),
                        ";".join(str(x) for x in (row.get("rare_earth_elements_present") or [])),
                        str(row.get("description", "")).replace("\t", " ").replace("\n", " ").strip(),
                    ]
                )
        print(f"  ✓ Generated bulk exports at {json_path} and {tsv_path}")

    def _generate_schema_and_404(
        self,
        num_communities: int,
        docs_dir: Path,
    ) -> None:
        """Generate docs/schema.html and docs/404.html."""
        from html import escape

        schema_yaml_path = Path(__file__).parent / "schema" / "communitymech.yaml"
        schema_data = yaml.safe_load(schema_yaml_path.read_text(encoding="utf-8"))
        schema_uri = str(schema_data.get("id", "https://w3id.org/communitymech"))
        schema_name = str(schema_data.get("name", "communitymech"))
        schema_desc = str(schema_data.get("description", "")).strip()

        classes = schema_data.get("classes") or {}
        slots = schema_data.get("slots") or {}
        enums = schema_data.get("enums") or {}

        class_rows = []
        for cname, cdef in sorted(classes.items()):
            cdef = cdef or {}
            cdesc = escape(str(cdef.get("description", "")).strip())
            cattrs = ", ".join(sorted((cdef.get("attributes") or {}).keys()))
            class_rows.append(
                f"<tr><th scope='row'><code>{escape(cname)}</code></th>"
                f"<td>{cdesc}</td>"
                f"<td><code>{escape(cattrs)}</code></td></tr>"
            )

        slot_rows = []
        for sname, sdef in sorted(slots.items()):
            sdef = sdef or {}
            sdesc = escape(str(sdef.get("description", "")).strip())
            srange = escape(str(sdef.get("range", "string")))
            slot_rows.append(
                f"<tr><th scope='row'><code>{escape(sname)}</code></th>"
                f"<td><code>{srange}</code></td>"
                f"<td>{sdesc}</td></tr>"
            )
        for cname, cdef in sorted(classes.items()):
            for aname, adef in sorted(((cdef or {}).get("attributes") or {}).items()):
                adef = adef or {}
                adesc = escape(str(adef.get("description", "")).strip())
                arange = escape(str(adef.get("range", "string")))
                slot_rows.append(
                    f"<tr><th scope='row'><code>{escape(cname)}.{escape(aname)}</code></th>"
                    f"<td><code>{arange}</code></td>"
                    f"<td>{adesc}</td></tr>"
                )

        enum_rows = []
        for ename, edef in sorted(enums.items()):
            edef = edef or {}
            edesc = escape(str(edef.get("description", "")).strip())
            pvs = ", ".join(sorted((edef.get("permissible_values") or {}).keys()))
            enum_rows.append(
                f"<tr><th scope='row'><code>{escape(ename)}</code></th>"
                f"<td>{edesc}</td>"
                f"<td><code>{escape(pvs)}</code></td></tr>"
            )

        schema_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CommunityMech — LinkML Schema Documentation</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; background: var(--bg-page); color: var(--text-primary); line-height: 1.6; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem 1.5rem; }}
        header {{ background: var(--bg-card); padding: 1.5rem 2rem; border-radius: 8px; border: 1px solid var(--border); margin-bottom: 1.5rem; }}
        nav a {{ color: var(--accent); text-decoration: none; margin-right: 1rem; font-weight: 600; }}
        section {{ background: var(--bg-card); padding: 1.5rem 2rem; border-radius: 8px; border: 1px solid var(--border); margin-bottom: 1.5rem; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 0.75rem; font-size: 0.9rem; }}
        caption {{ text-align: left; font-weight: 600; margin-bottom: 0.5rem; color: var(--text-secondary); }}
        th, td {{ text-align: left; padding: 0.6rem 0.75rem; border-bottom: 1px solid var(--border); vertical-align: top; }}
        thead th {{ background: var(--bg-chip); font-weight: 600; }}
        code {{ background: var(--bg-chip); padding: 0.12rem 0.35rem; border-radius: 4px; font-size: 0.85em; }}
        footer {{ text-align: center; color: var(--text-muted); font-size: 0.85rem; padding: 1.5rem 0; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <nav aria-label="Primary">
                <a href="index.html">Home</a>
                <a href="browser.html">Browse</a>
                <a href="text_map.html">Text Map</a>
                <a href="community_umap.html">Taxonomic UMAP</a>
                <a href="sequence_map.html">Sequence Map</a>
                <a href="community_graph.html">Network</a>
                <a href="schema.html" aria-current="page">Schema</a>
                <a href="https://culturebotai.github.io/mechs/">All Mech projects</a>
            </nav>
            <h1>CommunityMech LinkML Schema Documentation</h1>
            <p>{escape(schema_desc)}</p>
            <p><strong>Schema URI:</strong> <code>{escape(schema_uri)}</code> &bull; <strong>Name:</strong> <code>{escape(schema_name)}</code> &bull; <a href="https://github.com/CultureBotAI/CommunityMech/blob/main/src/communitymech/schema/communitymech.yaml">View LinkML YAML source</a></p>
        </header>
        <main>
            <section>
                <h2>Classes ({len(classes)})</h2>
                <table>
                    <caption>LinkML classes defined in the CommunityMech schema</caption>
                    <thead>
                        <tr><th scope="col">Class</th><th scope="col">Description</th><th scope="col">Attributes</th></tr>
                    </thead>
                    <tbody>
                        {"".join(class_rows)}
                    </tbody>
                </table>
            </section>
            <section>
                <h2>Slots &amp; Class Attributes ({len(slot_rows)})</h2>
                <table>
                    <caption>LinkML slots and class attributes in CommunityMech</caption>
                    <thead>
                        <tr><th scope="col">Slot / Attribute</th><th scope="col">Range</th><th scope="col">Description</th></tr>
                    </thead>
                    <tbody>
                        {"".join(slot_rows)}
                    </tbody>
                </table>
            </section>
            <section>
                <h2>Enumerations ({len(enums)})</h2>
                <table>
                    <caption>Controlled vocabulary enumerations in CommunityMech</caption>
                    <thead>
                        <tr><th scope="col">Enumeration</th><th scope="col">Description</th><th scope="col">Permissible Values</th></tr>
                    </thead>
                    <tbody>
                        {"".join(enum_rows)}
                    </tbody>
                </table>
            </section>
        </main>
        <footer>
            <p>CommunityMech Knowledge Base ({num_communities} communities) &bull; Schema: <a href="schema.html"><code>{escape(schema_uri)}</code></a> &bull; Source: <a href="https://github.com/CultureBotAI/CommunityMech">kb/communities/</a> &bull; License: BSD-3-Clause</p>
        </footer>
    </div>
    <script src="theme-toggle.js"></script>
</body>
</html>
"""
        schema_path = docs_dir / "schema.html"
        schema_path.write_text(_strip_trailing_whitespace(schema_html), encoding="utf-8")
        print(f"  ✓ Generated schema docs at {schema_path}")

        not_found_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found — CommunityMech</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; background: var(--bg-page); color: var(--text-primary); line-height: 1.6; }}
        .container {{ max-width: 800px; margin: 3rem auto; padding: 2rem 1.5rem; }}
        .card {{ background: var(--bg-card); padding: 2rem; border-radius: 10px; border: 1px solid var(--border); }}
        nav a {{ color: var(--accent); text-decoration: none; margin-right: 1rem; font-weight: 600; }}
        .search-form {{ display: flex; gap: 0.5rem; margin: 1.25rem 0; }}
        .search-form input {{ flex: 1; padding: 0.65rem 0.9rem; border: 1px solid var(--border-strong); border-radius: 6px; font-size: 1rem; background: var(--bg-input); color: var(--text-primary); }}
        .search-form button {{ padding: 0.65rem 1.2rem; border-radius: 6px; border: 1px solid var(--accent); background: var(--accent); color: var(--accent-contrast); font-weight: 600; cursor: pointer; }}
        footer {{ text-align: center; color: var(--text-muted); font-size: 0.85rem; padding: 1.5rem 0; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <nav aria-label="Primary">
                <a href="index.html">Home</a>
                <a href="browser.html">Browse</a>
                <a href="text_map.html">Text Map</a>
                <a href="community_umap.html">Taxonomic UMAP</a>
                <a href="sequence_map.html">Sequence Map</a>
                <a href="community_graph.html">Network</a>
                <a href="schema.html">Schema</a>
            </nav>
            <h1>Page Not Found (404)</h1>
            <p>The requested CommunityMech page could not be found. Search the curated microbial community knowledge base below or navigate to one of the main views:</p>
            <form class="search-form" action="browser.html" method="get" role="search">
                <label for="q404" style="position:absolute;left:-9999px;">Search communities</label>
                <input type="search" id="q404" name="q" placeholder="Search communities by name, taxon, metabolite, or habitat...">
                <button type="submit">Search</button>
            </form>
            <h2>Explore CommunityMech</h2>
            <ul>
                <li><a href="index.html">Landing Page &amp; Overview</a></li>
                <li><a href="browser.html">Interactive Community Browser ({num_communities} communities)</a></li>
                <li><a href="text_map.html">Community Text Embedding Map</a></li>
                <li><a href="community_umap.html">Taxonomic UMAP Embedding</a></li>
                <li><a href="sequence_map.html">ESM-2 Protein Sequence Map</a></li>
                <li><a href="community_graph.html">Community Network Graph</a></li>
                <li><a href="schema.html">LinkML Schema Documentation</a></li>
                <li><a href="communities.json">Download All Communities (JSON)</a> &bull; <a href="communities.tsv">TSV</a></li>
            </ul>
        </div>
        <footer>
            <p>CommunityMech Knowledge Base ({num_communities} communities) &bull; Schema: <a href="schema.html"><code>{escape(schema_uri)}</code></a> &bull; Source: <a href="https://github.com/CultureBotAI/CommunityMech">kb/communities/</a> &bull; License: BSD-3-Clause</p>
        </footer>
    </div>
    <script src="theme-toggle.js"></script>
</body>
</html>
"""
        not_found_path = docs_dir / "404.html"
        not_found_path.write_text(_strip_trailing_whitespace(not_found_html), encoding="utf-8")
        print(f"  ✓ Generated 404 recovery page at {not_found_path}")

    def _generate_embedding_maps(
        self,
        yaml_files: list[Path],
        output_dir: Path,
    ) -> None:
        """Render text_map.html, sequence_map.html, and community_umap.html."""
        repo_root = Path(__file__).resolve().parents[2]
        valid_stems = {p.stem for p in yaml_files}

        umap_path = output_dir.parent / "community_umap.html"
        if umap_path.exists():
            existing_umap = umap_path.read_text(encoding="utf-8")
            m = re.search(r"const communityData = (\[.*?\]);", existing_umap, re.DOTALL)
            if m:
                umap_rows = [
                    row for row in json.loads(m.group(1)) if row.get("id") in valid_stems
                ]
                umap_template = self.env.get_template("community_umap.html")
                umap_html = umap_template.render(
                    num_communities=len(umap_rows),
                    community_data_json=json.dumps(umap_rows, indent=2, ensure_ascii=False),
                )
                umap_path.write_text(_strip_trailing_whitespace(umap_html) + "\n", encoding="utf-8")
                print(f"  ✓ Generated taxonomic UMAP at {umap_path}")

        corpus_json_path = repo_root / "data" / "embeddings" / "corpus_map.json"
        if corpus_json_path.exists():
            corpus_data = json.loads(corpus_json_path.read_text(encoding="utf-8"))
            points = [
                {
                    **pt,
                    "neighbors": [
                        nn for nn in (pt.get("neighbors") or []) if nn.get("id") in valid_stems
                    ],
                }
                for pt in (corpus_data.get("points") or [])
                if pt.get("id") in valid_stems
            ]
            corpus_payload = {
                **corpus_data,
                "count": len(points),
                "points": points,
            }
            text_map_template = self.env.get_template("text_map.html")
            text_map_html = text_map_template.render(
                corpus_map=corpus_payload,
                corpus_map_json=json.dumps(corpus_payload, ensure_ascii=False),
            )
            text_map_path = output_dir.parent / "text_map.html"
            text_map_path.write_text(_strip_trailing_whitespace(text_map_html), encoding="utf-8")
            print(f"  ✓ Generated text embedding map at {text_map_path}")

        seq_json_path = repo_root / "data" / "embeddings" / "sequence_map.json"
        if seq_json_path.exists():
            seq_data = json.loads(seq_json_path.read_text(encoding="utf-8"))
            records = []
            for rec in seq_data.get("records") or []:
                comms = [
                    c for c in (rec.get("communities") or []) if c.get("id") in valid_stems
                ]
                records.append({
                    **rec,
                    "communities": comms,
                    "n_communities": len(comms),
                })
            seq_payload = {
                **seq_data,
                "count": len(records),
                "records": records,
            }
            seq_map_template = self.env.get_template("sequence_map.html")
            seq_map_html = seq_map_template.render(
                sequence_map=seq_payload,
                sequence_map_json=json.dumps(seq_payload, ensure_ascii=False),
            )
            seq_map_path = output_dir.parent / "sequence_map.html"
            seq_map_path.write_text(_strip_trailing_whitespace(seq_map_html), encoding="utf-8")
            print(f"  ✓ Generated sequence embedding map at {seq_map_path}")


def main():
    """CLI for HTML rendering."""
    import argparse

    parser = argparse.ArgumentParser(description="Render community YAML files to HTML")
    parser.add_argument(
        "yaml_file",
        nargs="?",
        help="Path to single community YAML file (optional)",
    )
    parser.add_argument(
        "--communities-dir",
        default="kb/communities",
        help="Directory containing community YAML files",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DOCS / "communities"),
        help="Output directory for HTML files",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Render all communities",
    )

    args = parser.parse_args()

    renderer = CommunityRenderer()

    if args.yaml_file:
        # Render single file
        yaml_path = Path(args.yaml_file)
        output_path = Path(args.output_dir) / f"{yaml_path.stem}.html"
        renderer.render_community(yaml_path, output_path)
    else:
        # Render all files
        failed = renderer.render_all(
            communities_dir=Path(args.communities_dir),
            output_dir=Path(args.output_dir),
        )
        if failed:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
