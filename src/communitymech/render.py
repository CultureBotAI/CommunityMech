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

        # Load index template
        template = self.env.get_template("index.html")

        # Render index page
        index_html = template.render(communities=communities)

        # Write to file
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
