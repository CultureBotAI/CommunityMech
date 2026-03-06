"""Build rich context for LLM prompts from community data."""

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import yaml


class ContextBuilder:
    """Build rich context for LLM prompts from community YAML data."""

    def __init__(self, community_path: Path):
        """
        Initialize context builder.

        Args:
            community_path: Path to community YAML file
        """
        self.community_path = Path(community_path)
        with open(self.community_path) as f:
            self.data = yaml.safe_load(f)

    def build_disconnected_taxon_context(
        self, taxon_name: str, taxon_id: str
    ) -> Dict[str, Any]:
        """
        Build context for repairing a disconnected taxon.

        Args:
            taxon_name: Name of disconnected taxon
            taxon_id: NCBITaxon ID of disconnected taxon

        Returns:
            Context dictionary for prompt formatting
        """
        # Basic community info
        context = {
            "community_name": self.data.get("name", "Unknown"),
            "taxon_name": taxon_name,
            "taxon_id": taxon_id,
        }

        # Environmental context
        env_context = self._build_environmental_context()
        context.update(env_context)

        # Taxon-specific context
        taxon_context = self._build_taxon_context(taxon_name)
        context["taxon_context"] = taxon_context

        # Connected taxa (for interaction partners)
        connected_taxa = self._build_connected_taxa_list()
        context["connected_taxa"] = connected_taxa

        # Interaction summary
        interaction_summary = self._build_interaction_summary()
        context["interaction_summary"] = interaction_summary

        return context

    def _build_environmental_context(self) -> Dict[str, str]:
        """Build environmental context from community data."""
        env_factors = self.data.get("environmental_factors", {})

        # Extract key environmental parameters
        environment_type = "Unknown environment"
        env_params = []

        # Get habitat/environment terms
        if "habitat" in env_factors:
            habitats = env_factors["habitat"]
            if habitats:
                habitat_labels = [h.get("label", "") for h in habitats]
                environment_type = ", ".join(habitat_labels)

        # Get physical parameters
        if "physical_parameters" in env_factors:
            for param in env_factors["physical_parameters"]:
                param_type = param.get("parameter_type", "")
                value = param.get("value", "")
                unit = param.get("unit", "")

                if param_type and value:
                    env_params.append(f"{param_type}: {value} {unit}".strip())

        # Get chemical parameters
        if "chemical_parameters" in env_factors:
            for param in env_factors["chemical_parameters"]:
                param_type = param.get("parameter_type", "")
                value = param.get("value", "")
                unit = param.get("unit", "")

                if param_type and value:
                    env_params.append(f"{param_type}: {value} {unit}".strip())

        environmental_context = "\n".join(f"- {p}" for p in env_params) if env_params else ""

        return {
            "environment": environment_type,
            "environmental_context": environmental_context or "No specific parameters provided",
        }

    def _build_taxon_context(self, taxon_name: str) -> str:
        """
        Build context about the specific taxon.

        Args:
            taxon_name: Name of the taxon

        Returns:
            Formatted context string
        """
        # Find taxon in taxonomy
        taxon_data = None
        for taxon in self.data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            if preferred == taxon_name:
                taxon_data = taxon
                break

        if not taxon_data:
            return "No additional information available"

        context_parts = []

        # Functional roles
        if "functional_roles" in taxon_data:
            roles = taxon_data["functional_roles"]
            if roles:
                role_labels = [r.get("label", "") for r in roles]
                context_parts.append(f"Functional Roles: {', '.join(role_labels)}")

        # Abundance
        if "abundance" in taxon_data:
            abundance = taxon_data["abundance"]
            if "relative_abundance" in abundance:
                rel_ab = abundance["relative_abundance"]
                context_parts.append(f"Relative Abundance: {rel_ab}")
            if "abundance_category" in abundance:
                cat = abundance["abundance_category"]
                context_parts.append(f"Abundance Category: {cat}")

        # Metabolic capabilities (if available)
        if "metabolic_capabilities" in taxon_data:
            capabilities = taxon_data["metabolic_capabilities"]
            if capabilities:
                cap_list = [c.get("label", "") for c in capabilities]
                context_parts.append(f"Metabolic Capabilities: {', '.join(cap_list)}")

        return "\n".join(f"- {p}" for p in context_parts) if context_parts else "No additional information available"

    def _build_connected_taxa_list(self) -> str:
        """
        Build list of taxa that are already connected in the network.

        Returns:
            Formatted list of connected taxa with IDs
        """
        # Get all taxa involved in interactions
        connected = set()
        interactions = self.data.get("ecological_interactions", [])

        for interaction in interactions:
            source = interaction.get("source_taxon", {})
            target = interaction.get("target_taxon", {})

            if source:
                source_term = source.get("preferred_term") or source.get("term", {}).get("label")
                source_id = source.get("term", {}).get("id")
                if source_term and source_id:
                    connected.add((source_term, source_id))

            if target:
                target_term = target.get("preferred_term") or target.get("term", {}).get("label")
                target_id = target.get("term", {}).get("id")
                if target_term and target_id:
                    connected.add((target_term, target_id))

        if not connected:
            return "No connected taxa (no interactions yet)"

        # Format as list
        taxa_list = [f"- {name} ({taxon_id})" for name, taxon_id in sorted(connected)]
        return "\n".join(taxa_list)

    def _build_interaction_summary(self) -> str:
        """
        Build summary of existing interactions in the community.

        Returns:
            Formatted summary of interaction types and patterns
        """
        interactions = self.data.get("ecological_interactions", [])

        if not interactions:
            return "No interactions yet"

        summary_parts = []

        # Count interaction types
        interaction_types = Counter()
        metabolites_used = set()
        processes_involved = set()

        for interaction in interactions:
            # Interaction type
            int_type = interaction.get("interaction_type", "Unknown")
            interaction_types[int_type] += 1

            # Metabolites
            for metabolite in interaction.get("metabolites_exchanged", []):
                met_term = metabolite.get("metabolite_term", {})
                met_label = met_term.get("label", "")
                if met_label:
                    metabolites_used.add(met_label)

            # Processes
            for process in interaction.get("biological_processes", []):
                proc_label = process.get("label", "")
                if proc_label:
                    processes_involved.add(proc_label)

        # Format summary
        summary_parts.append(f"Total interactions: {len(interactions)}")

        if interaction_types:
            types_str = ", ".join(f"{t}: {c}" for t, c in interaction_types.most_common())
            summary_parts.append(f"Interaction types: {types_str}")

        if metabolites_used:
            met_list = ", ".join(sorted(metabolites_used)[:10])
            if len(metabolites_used) > 10:
                met_list += f", ... ({len(metabolites_used)} total)"
            summary_parts.append(f"Key metabolites: {met_list}")

        if processes_involved:
            proc_list = ", ".join(sorted(processes_involved)[:5])
            if len(processes_involved) > 5:
                proc_list += f", ... ({len(processes_involved)} total)"
            summary_parts.append(f"Biological processes: {proc_list}")

        return "\n".join(f"- {p}" for p in summary_parts)

    def build_missing_source_context(
        self, interaction_name: str, interaction_index: int
    ) -> Dict[str, Any]:
        """
        Build context for identifying missing source_taxon.

        Args:
            interaction_name: Name of the interaction
            interaction_index: Index of interaction in list

        Returns:
            Context dictionary for prompt formatting
        """
        interactions = self.data.get("ecological_interactions", [])
        if interaction_index >= len(interactions):
            raise ValueError(f"Interaction index {interaction_index} out of range")

        interaction = interactions[interaction_index]

        context = {
            "community_name": self.data.get("name", "Unknown"),
            "interaction_name": interaction_name,
            "interaction_description": interaction.get("description", "No description"),
        }

        # Build available taxa list
        taxonomy = self.data.get("taxonomy", [])
        available_taxa = []
        for taxon in taxonomy:
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            taxon_id = term.get("term", {}).get("id")
            if preferred and taxon_id:
                available_taxa.append(f"- {preferred} ({taxon_id})")

        context["available_taxa"] = "\n".join(available_taxa) if available_taxa else "No taxa available"

        # Interaction details
        details = []
        if "interaction_type" in interaction:
            details.append(f"Type: {interaction['interaction_type']}")
        if "target_taxon" in interaction:
            target = interaction["target_taxon"]
            target_term = target.get("preferred_term") or target.get("term", {}).get("label")
            if target_term:
                details.append(f"Target: {target_term}")

        context["interaction_details"] = "\n".join(f"- {d}" for d in details) if details else "No details"

        return context

    def build_unknown_target_context(
        self, interaction_name: str, unknown_target: str
    ) -> Dict[str, Any]:
        """
        Build context for resolving unknown target taxon.

        Args:
            interaction_name: Name of the interaction
            unknown_target: Name of the unknown target taxon

        Returns:
            Context dictionary for prompt formatting
        """
        context = {
            "community_name": self.data.get("name", "Unknown"),
            "interaction_name": interaction_name,
            "unknown_target": unknown_target,
        }

        # Build available taxa list
        taxonomy = self.data.get("taxonomy", [])
        available_taxa = []
        for taxon in taxonomy:
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            taxon_id = term.get("term", {}).get("id")
            if preferred and taxon_id:
                available_taxa.append(f"- {preferred} ({taxon_id})")

        context["available_taxa"] = "\n".join(available_taxa) if available_taxa else "No taxa available"

        return context

    def get_all_taxa(self) -> List[Dict[str, str]]:
        """
        Get list of all taxa in the community.

        Returns:
            List of dicts with 'name' and 'id' keys
        """
        taxa = []
        for taxon in self.data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            taxon_id = term.get("term", {}).get("id")
            if preferred and taxon_id:
                taxa.append({"name": preferred, "id": taxon_id})
        return taxa

    def get_connected_taxa(self) -> Set[str]:
        """
        Get set of taxon names that are connected in the network.

        Returns:
            Set of taxon names
        """
        connected = set()
        for interaction in self.data.get("ecological_interactions", []):
            source = interaction.get("source_taxon", {})
            target = interaction.get("target_taxon", {})

            if source:
                source_term = source.get("preferred_term") or source.get("term", {}).get("label")
                if source_term:
                    connected.add(source_term)

            if target:
                target_term = target.get("preferred_term") or target.get("term", {}).get("label")
                if target_term:
                    connected.add(target_term)

        return connected
