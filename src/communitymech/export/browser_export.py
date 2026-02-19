"""
Browser export for CommunityMech faceted search.

Generates app/data.js with searchable community data for web interface.
"""

import json
import yaml
from pathlib import Path
from typing import List, Dict, Any, Set


class BrowserExporter:
    """Export community YAMLs to browser-ready JSON."""

    def __init__(self, communities_dir: Path = Path("kb/communities")):
        self.communities_dir = communities_dir
        self.communities: List[Dict[str, Any]] = []

    def export_all(self, output_path: Path = Path("docs/data.js")) -> None:
        """
        Export all community files to browser JSON.

        Args:
            output_path: Path to output JavaScript file
        """
        # Collect all community files
        yaml_files = sorted(self.communities_dir.glob("*.yaml"))

        print(f"\nExporting {len(yaml_files)} communities to browser format...")

        for yaml_file in yaml_files:
            try:
                community_data = self._process_community(yaml_file)
                self.communities.append(community_data)
                print(f"  ✓ {yaml_file.name}")
            except Exception as e:
                print(f"  ✗ {yaml_file.name}: {e}")

        # Generate facets from aggregated data
        facets = self._generate_facets()

        # Write JavaScript file
        self._write_js_file(output_path, facets)

        print(f"\n✅ Exported {len(self.communities)} communities to {output_path}")

    def _process_community(self, yaml_path: Path) -> Dict[str, Any]:
        """Process a single community YAML into browser-friendly format."""
        with open(yaml_path) as f:
            data = yaml.safe_load(f)

        # Extract searchable fields
        community = {
            "id": yaml_path.stem,
            "name": data.get("name", ""),
            "ecological_state": data.get("ecological_state", ""),
            "community_origin": data.get("community_origin", ""),
            "community_category": data.get("community_category", ""),
            "environment": self._extract_environment(data),
            "taxa": self._extract_taxa(data),
            "metabolites": self._extract_metabolites(data),
            "biological_processes": self._extract_processes(data),
            "interaction_types": self._extract_interaction_types(data),
            "functional_roles": self._extract_functional_roles(data),
            "datasets": self._extract_datasets(data),
            "description": data.get("description", ""),
            "source_file": yaml_path.name,
        }

        # Add search text (combines all searchable fields)
        community["search_text"] = self._build_search_text(community)

        return community

    def _extract_environment(self, data: dict) -> Dict[str, str]:
        """Extract environment term and label."""
        env = data.get("environment_term", {})
        if isinstance(env, dict) and "term" in env:
            term = env["term"]
            return {
                "id": term.get("id", ""),
                "label": term.get("label", ""),
                "preferred": env.get("preferred_term", ""),
            }
        return {}

    def _extract_taxa(self, data: dict) -> List[Dict[str, str]]:
        """Extract all taxa from taxonomy section."""
        taxa = []
        for taxon_item in data.get("taxonomy", []):
            if "taxon_term" in taxon_item:
                taxon_term = taxon_item["taxon_term"]
                term = taxon_term.get("term", {})
                taxa.append({
                    "id": term.get("id", ""),
                    "label": term.get("label", ""),
                    "preferred": taxon_term.get("preferred_term", ""),
                    "roles": taxon_item.get("functional_role", []),
                })
        return taxa

    def _extract_metabolites(self, data: dict) -> List[Dict[str, str]]:
        """Extract all metabolites from ecological interactions."""
        metabolites = []
        seen = set()

        for interaction in data.get("ecological_interactions", []):
            for metabolite in interaction.get("metabolites", []):
                if "term" in metabolite:
                    term = metabolite["term"]
                    term_id = term.get("id", "")
                    if term_id and term_id not in seen:
                        metabolites.append({
                            "id": term_id,
                            "label": term.get("label", ""),
                            "preferred": metabolite.get("preferred_term", ""),
                        })
                        seen.add(term_id)

        return metabolites

    def _extract_processes(self, data: dict) -> List[Dict[str, str]]:
        """Extract biological processes from ecological interactions."""
        processes = []
        seen = set()

        for interaction in data.get("ecological_interactions", []):
            for process in interaction.get("biological_processes", []):
                if "term" in process:
                    term = process["term"]
                    term_id = term.get("id", "")
                    if term_id and term_id not in seen:
                        processes.append({
                            "id": term_id,
                            "label": term.get("label", ""),
                            "preferred": process.get("preferred_term", ""),
                        })
                        seen.add(term_id)

        return processes

    def _extract_interaction_types(self, data: dict) -> List[str]:
        """Extract unique interaction types."""
        types = set()
        for interaction in data.get("ecological_interactions", []):
            itype = interaction.get("interaction_type")
            if itype:
                types.add(itype)
        return sorted(types)

    def _extract_functional_roles(self, data: dict) -> List[str]:
        """Extract unique functional roles from taxonomy."""
        roles = set()
        for taxon_item in data.get("taxonomy", []):
            for role in taxon_item.get("functional_role", []):
                roles.add(role)
        return sorted(roles)

    def _extract_datasets(self, data: dict) -> List[Dict[str, str]]:
        """Extract associated datasets."""
        datasets = []
        for ds in data.get("associated_datasets", []):
            datasets.append({
                "name": ds.get("name", ""),
                "dataset_type": ds.get("dataset_type", ""),
                "repository": ds.get("repository", ""),
                "accession": ds.get("accession", ""),
                "url": ds.get("url", ""),
            })
        return datasets

    def _build_search_text(self, community: dict) -> str:
        """Build combined search text from all fields."""
        parts = [
            community["name"],
            community["description"],
            community["ecological_state"],
            community["environment"].get("label", ""),
            community["environment"].get("preferred", ""),
        ]

        # Add taxa labels
        for taxon in community["taxa"]:
            parts.extend([taxon["label"], taxon["preferred"]])

        # Add metabolite labels
        for metabolite in community["metabolites"]:
            parts.extend([metabolite["label"], metabolite["preferred"]])

        # Add process labels
        for process in community["biological_processes"]:
            parts.extend([process["label"], process["preferred"]])

        # Add interaction types and roles
        parts.extend(community["interaction_types"])
        parts.extend(community["functional_roles"])

        # Add dataset names and types
        for ds in community["datasets"]:
            parts.extend([ds["name"], ds["dataset_type"], ds["repository"], ds["accession"]])

        # Combine and clean
        text = " ".join(str(p) for p in parts if p)
        return " ".join(text.split())  # Normalize whitespace

    def _generate_facets(self) -> Dict[str, Any]:
        """Generate facet data from all communities."""
        ecological_states: Set[str] = set()
        community_origins: Set[str] = set()
        community_categories: Set[str] = set()
        environments: Set[str] = set()
        taxa: Set[str] = set()
        metabolites: Set[str] = set()
        interaction_types: Set[str] = set()
        functional_roles: Set[str] = set()
        dataset_types: Set[str] = set()
        dataset_repositories: Set[str] = set()

        for community in self.communities:
            if community["ecological_state"]:
                ecological_states.add(community["ecological_state"])

            if community["community_origin"]:
                community_origins.add(community["community_origin"])

            if community["community_category"]:
                community_categories.add(community["community_category"])

            if community["environment"].get("label"):
                environments.add(community["environment"]["label"])

            for taxon in community["taxa"]:
                if taxon["label"]:
                    taxa.add(taxon["label"])

            for metabolite in community["metabolites"]:
                if metabolite["label"]:
                    metabolites.add(metabolite["label"])

            interaction_types.update(community["interaction_types"])
            functional_roles.update(community["functional_roles"])

            for ds in community["datasets"]:
                if ds["dataset_type"]:
                    dataset_types.add(ds["dataset_type"])
                if ds["repository"]:
                    dataset_repositories.add(ds["repository"])

        return {
            "ecological_states": sorted(ecological_states),
            "community_origins": sorted(community_origins),
            "community_categories": sorted(community_categories),
            "environments": sorted(environments),
            "taxa": sorted(taxa)[:50],  # Limit to top 50 most common
            "metabolites": sorted(metabolites)[:50],
            "interaction_types": sorted(interaction_types),
            "functional_roles": sorted(functional_roles),
            "dataset_types": sorted(dataset_types),
            "dataset_repositories": sorted(dataset_repositories),
        }

    def _write_js_file(self, output_path: Path, facets: Dict[str, Any]) -> None:
        """Write JavaScript file with data and facets."""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            f.write("// CommunityMech Browser Data\n")
            f.write("// Auto-generated by src/communitymech/export/browser_export.py\n\n")

            # Write search data
            f.write("window.communityData = ")
            f.write(json.dumps(self.communities, indent=2))
            f.write(";\n\n")

            # Write facets
            f.write("window.facets = ")
            f.write(json.dumps(facets, indent=2))
            f.write(";\n")


def main():
    """CLI for browser export."""
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Export communities to browser JSON")
    parser.add_argument(
        "--communities-dir",
        default="kb/communities",
        help="Directory containing community YAML files",
    )
    parser.add_argument(
        "--output",
        default="docs/data.js",
        help="Output JavaScript file path",
    )

    args = parser.parse_args()

    exporter = BrowserExporter(communities_dir=Path(args.communities_dir))
    exporter.export_all(output_path=Path(args.output))


if __name__ == "__main__":
    main()
