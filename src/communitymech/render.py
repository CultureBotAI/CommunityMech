"""
HTML rendering for CommunityMech community pages.

Generates individual HTML pages for each community with full metadata,
taxonomy, ecological interactions, and evidence.
"""

import yaml
from pathlib import Path
from typing import Optional
from jinja2 import Environment, FileSystemLoader, select_autoescape


class CommunityRenderer:
    """Render community YAML files to HTML pages."""

    def __init__(self, template_dir: Optional[Path] = None):
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

    def render_community(
        self,
        yaml_path: Path,
        output_path: Optional[Path] = None,
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
                f.write(html)
            print(f"  ✓ {yaml_path.name} → {output_path}")

        return html

    def render_all(
        self,
        communities_dir: Path = Path("kb/communities"),
        output_dir: Path = Path("docs/communities"),
    ) -> None:
        """
        Render all community YAML files to HTML.

        Args:
            communities_dir: Directory containing community YAML files
            output_dir: Directory for output HTML files
        """
        yaml_files = sorted(communities_dir.glob("*.yaml"))

        print(f"\nRendering {len(yaml_files)} communities to HTML...")

        for yaml_file in yaml_files:
            try:
                output_file = output_dir / f"{yaml_file.stem}.html"
                self.render_community(yaml_file, output_file)
            except Exception as e:
                print(f"  ✗ {yaml_file.name}: {e}")

        print(f"\n✅ Rendered {len(yaml_files)} communities to {output_dir}")

        # Generate index page
        self._generate_index(yaml_files, output_dir)

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
                communities.append({
                    "id": yaml_file.stem,
                    "name": data.get("name", ""),
                    "description": data.get("description", ""),
                    "ecological_state": data.get("ecological_state", ""),
                    "community_category": data.get("community_category", ""),
                })

        index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CommunityMech - Microbial Community Knowledge Base</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #f8fafc;
            color: #1e293b;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            background: white;
            border-bottom: 2px solid #2563eb;
            padding: 2rem 0;
            margin-bottom: 2rem;
        }

        h1 {
            color: #2563eb;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            color: #64748b;
            font-size: 1.125rem;
        }

        .community-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .community-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1.5rem;
            transition: transform 0.2s, box-shadow 0.2s;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
        }

        .community-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .community-card h2 {
            color: #2563eb;
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }

        .community-card .description {
            color: #64748b;
            font-size: 0.875rem;
            line-height: 1.5;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            flex: 1;
        }

        .card-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 0.75rem;
        }

        .badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 500;
        }

        .badge-engineered { background: #dbeafe; color: #1e40af; }
        .badge-natural { background: #d1fae5; color: #065f46; }

        .badge-category {
            background: #f1f5f9;
            color: #475569;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            padding: 0.2rem 0.6rem;
            border-radius: 10px;
        }

        footer {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #e2e8f0;
            text-align: center;
            color: #64748b;
            font-size: 0.875rem;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>CommunityMech</h1>
            <p class="subtitle">Microbial Community Knowledge Base</p>
        </div>
    </header>

    <main class="container">
        <div class="community-grid">
"""

        for community in communities:
            badge_class = "badge-engineered" if community["ecological_state"] == "ENGINEERED" else "badge-natural"
            index_html += f"""
            <a href="communities/{community['id']}.html" class="community-card">
                <h2>{community['name']}</h2>
                <p class="description">{community['description']}</p>
                <div class="card-footer">
                    <span class="badge {badge_class}">{community['ecological_state']}</span>
                    <span class="badge badge-category">{community['community_category']}</span>
                </div>
            </a>
"""

        index_html += """
        </div>
    </main>

    <footer>
        <div class="container">
            <p>Generated by CommunityMech | <a href="https://github.com/CultureBotAI/CommunityMech">View on GitHub</a></p>
        </div>
    </footer>
</body>
</html>
"""

        index_path = output_dir.parent / "index.html"  # docs/index.html
        index_path.parent.mkdir(parents=True, exist_ok=True)
        with open(index_path, "w") as f:
            f.write(index_html)

        print(f"  ✓ Generated index at {index_path}")


def main():
    """CLI for HTML rendering."""
    import sys
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
        default="docs/communities",
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
        renderer.render_all(
            communities_dir=Path(args.communities_dir),
            output_dir=Path(args.output_dir),
        )


if __name__ == "__main__":
    main()
