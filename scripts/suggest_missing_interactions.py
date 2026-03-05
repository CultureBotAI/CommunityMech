#!/usr/bin/env python3
"""
Generate interaction suggestions for disconnected taxa based on their functional roles.

Analyzes disconnected taxa and suggests appropriate interactions to connect them
to the network based on their:
- Functional roles (PRIMARY_DEGRADER, CROSS_FEEDER, etc.)
- Taxonomic identity
- Existing interactions in the community
"""

import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple


# Interaction templates based on functional role pairs
INTERACTION_TEMPLATES = {
    ("PRIMARY_DEGRADER", "CROSS_FEEDER"): {
        "type": "CROSS_FEEDING",
        "name_template": "Organic Matter Exchange: {source} to {target}",
        "description_template": "{source} degrades complex substrates and releases metabolic intermediates that support {target} growth through cross-feeding.",
    },
    ("PRIMARY_PRODUCER", "CROSS_FEEDER"): {
        "type": "CROSS_FEEDING",
        "name_template": "Primary Production Supporting {target}",
        "description_template": "{source} produces organic compounds through primary metabolism that are utilized by heterotrophic {target}.",
    },
    ("CROSS_FEEDER", "CROSS_FEEDER"): {
        "type": "CROSS_FEEDING",
        "name_template": "Metabolite Exchange",
        "description_template": "{source} and {target} exchange metabolic intermediates supporting mutual growth.",
    },
    ("SYNTROPHIC_PARTNER", "SYNTROPHIC_PARTNER"): {
        "type": "SYNTROPHY",
        "name_template": "Syntrophic Partnership",
        "description_template": "{source} and {target} cooperate through syntrophic metabolism with thermodynamically coupled reactions.",
    },
}


class InteractionSuggester:
    def __init__(self, communities_dir: Path = Path("kb/communities")):
        self.communities_dir = communities_dir

    def suggest_all(self):
        """Generate interaction suggestions for all communities."""
        yaml_files = sorted(self.communities_dir.glob("*.yaml"))

        print(f"\n💡 Suggesting interactions for disconnected taxa in {len(yaml_files)} communities...\n")

        communities_with_suggestions = 0
        total_suggestions = 0

        for yaml_file in yaml_files:
            suggestions = self.suggest_for_community(yaml_file)
            if suggestions:
                communities_with_suggestions += 1
                total_suggestions += len(suggestions)
                self.print_suggestions(yaml_file.stem, suggestions)

        print(f"\n{'='*80}")
        print(f"Summary:")
        print(f"  Communities with suggestions: {communities_with_suggestions}")
        print(f"  Total interaction suggestions: {total_suggestions}")
        print(f"{'='*80}\n")

    def suggest_for_community(self, yaml_path: Path) -> List[Dict]:
        """Suggest interactions for disconnected taxa in a community."""
        with open(yaml_path) as f:
            data = yaml.safe_load(f)

        # Build taxonomy info
        taxonomy_info = {}
        for taxon in data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            roles = taxon.get("functional_role", [])
            abundance = taxon.get("abundance_level")

            if preferred:
                taxonomy_info[preferred] = {
                    "roles": roles,
                    "abundance": abundance,
                    "taxon": taxon,
                }

        # Find connected taxa
        connected_taxa = set()
        for interaction in data.get("ecological_interactions", []):
            source = interaction.get("source_taxon")
            if source:
                source_term = source.get("preferred_term") or source.get("term", {}).get("label")
                if source_term:
                    connected_taxa.add(source_term)

            target = interaction.get("target_taxon")
            if target:
                target_term = target.get("preferred_term") or target.get("term", {}).get("label")
                if target_term:
                    connected_taxa.add(target_term)

        # Find disconnected taxa
        all_taxa = set(taxonomy_info.keys())
        disconnected = all_taxa - connected_taxa

        if not disconnected:
            return []

        # Generate suggestions
        suggestions = []
        for disc_taxon in sorted(disconnected):
            disc_info = taxonomy_info[disc_taxon]
            disc_roles = disc_info["roles"]

            # Skip if it's a host organism (often not in interaction network)
            if "host" in disc_taxon.lower() or any("host" in str(r).lower() for r in disc_roles):
                continue

            # Find potential interaction partners among connected taxa
            for conn_taxon in connected_taxa:
                if conn_taxon not in taxonomy_info:
                    continue

                conn_info = taxonomy_info[conn_taxon]
                conn_roles = conn_info["roles"]

                # Try to match functional role pairs
                for disc_role in disc_roles if disc_roles else ["UNKNOWN"]:
                    for conn_role in conn_roles if conn_roles else ["UNKNOWN"]:
                        template_key = (disc_role, conn_role)
                        reverse_key = (conn_role, disc_role)

                        template = INTERACTION_TEMPLATES.get(template_key) or INTERACTION_TEMPLATES.get(reverse_key)

                        if template:
                            # Generate suggestion
                            suggestion = {
                                "disconnected_taxon": disc_taxon,
                                "partner_taxon": conn_taxon,
                                "interaction_type": template["type"],
                                "source_role": disc_role,
                                "target_role": conn_role,
                                "confidence": "medium",
                                "rationale": f"Both taxa have compatible functional roles: {disc_role} and {conn_role}",
                            }
                            suggestions.append(suggestion)
                            break
                    if suggestions and suggestions[-1]["disconnected_taxon"] == disc_taxon:
                        break

            # If no role-based match, suggest based on abundance
            if not any(s["disconnected_taxon"] == disc_taxon for s in suggestions):
                # Connect to most abundant taxon
                abundant_taxa = [
                    (t, info) for t, info in taxonomy_info.items()
                    if t in connected_taxa and info.get("abundance") == "DOMINANT"
                ]

                if abundant_taxa:
                    partner = abundant_taxa[0][0]
                    suggestions.append({
                        "disconnected_taxon": disc_taxon,
                        "partner_taxon": partner,
                        "interaction_type": "CROSS_FEEDING",
                        "source_role": "UNKNOWN",
                        "target_role": "UNKNOWN",
                        "confidence": "low",
                        "rationale": f"Connecting to dominant community member {partner}",
                    })

        return suggestions

    def print_suggestions(self, community_name: str, suggestions: List[Dict]):
        """Print interaction suggestions for a community."""
        print(f"\n{'─'*80}")
        print(f"💡 {community_name}")
        print(f"{'─'*80}")

        for i, sugg in enumerate(suggestions, 1):
            print(f"\n  {i}. {sugg['disconnected_taxon']} ↔ {sugg['partner_taxon']}")
            print(f"     Type: {sugg['interaction_type']}")
            print(f"     Confidence: {sugg['confidence']}")
            print(f"     Rationale: {sugg['rationale']}")

        print(f"\n  Total suggestions: {len(suggestions)}")


def main():
    suggester = InteractionSuggester()
    suggester.suggest_all()


if __name__ == "__main__":
    main()
