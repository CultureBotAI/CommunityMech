"""
HTML rendering for CommunityMech community pages.

Generates individual HTML pages for each community with full metadata,
taxonomy, ecological interactions, and evidence.
"""

from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from communitymech.paths import DOCS, REPO_ROOT
from communitymech.text_map_site import prepare_text_map


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

    def render_isolates(self, isolates_dir: Path, output_dir: Path) -> list[str]:
        """Render isolate detail pages without changing the community browser population."""
        if not isolates_dir.is_dir():
            raise ValueError(f"missing isolate corpus: {isolates_dir}")
        failed = []
        for yaml_path in sorted(isolates_dir.glob("*.yaml")):
            try:
                self.render_community(yaml_path, output_dir / f"{yaml_path.stem}.html")
            except Exception as error:
                print(f"  ✗ {yaml_path.name}: {error}")
                failed.append(yaml_path.name)
        return failed

    def render_all(
        self,
        communities_dir: Path = Path("kb/communities"),
        output_dir: Path | None = None,
    ) -> list[str]:
        """Preflight and stage the common map before any generated page changes."""
        output_dir = output_dir if output_dir is not None else DOCS / "communities"
        with prepare_text_map(REPO_ROOT) as text_map:
            if text_map is not None:
                text_map.stage(output_dir.parent)
            self.env.globals["text_map_enabled"] = text_map is not None
            return self._render_all(communities_dir, output_dir)

    def _render_all(
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
        landing_html = landing_template.render(num_communities=len(communities))

        index_path = output_dir.parent / "index.html"  # docs/index.html
        with open(index_path, "w") as f:
            f.write(_strip_trailing_whitespace(landing_html))

        print(f"  ✓ Generated landing at {index_path}")


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
        "--isolates-dir",
        default="data/isolates",
        help="Isolate detail records, published separately from the community browser",
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
        failed.extend(
            renderer.render_isolates(
                Path(args.isolates_dir), Path(args.output_dir).parent / "isolates"
            )
        )
        if failed:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
