"""Multi-layer validation for LLM-generated network repair suggestions."""

from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from communitymech.literature import LiteratureFetcher


class ValidationError:
    """Represents a validation error."""

    def __init__(self, layer: str, field: str, message: str, severity: str = "error"):
        self.layer = layer
        self.field = field
        self.message = message
        self.severity = severity  # "error" or "warning"

    def __repr__(self) -> str:
        return f"{self.layer}::{self.field}: {self.message} [{self.severity}]"

    def to_dict(self) -> dict[str, str]:
        return {
            "layer": self.layer,
            "field": self.field,
            "message": self.message,
            "severity": self.severity,
        }


class SuggestionValidator:
    """Multi-layer validation for LLM-generated repair suggestions."""

    def __init__(
        self,
        schema_path: Path = Path("src/communitymech/schema/communitymech.yaml"),
        validate_evidence: bool = True,
        validate_ontology: bool = True,
        check_plausibility: bool = True,
        min_snippet_match_score: float = 0.95,
    ):
        """
        Initialize suggestion validator.

        Args:
            schema_path: Path to LinkML schema
            validate_evidence: Enable evidence validation
            validate_ontology: Enable ontology validation
            check_plausibility: Enable plausibility checks
            min_snippet_match_score: Minimum fuzzy match score for snippets
        """
        self.schema_path = Path(schema_path)
        self.validate_evidence_enabled = validate_evidence
        self.validate_ontology_enabled = validate_ontology
        self.check_plausibility_enabled = check_plausibility
        self.min_snippet_match_score = min_snippet_match_score

        # Initialize literature fetcher for evidence validation
        if validate_evidence:
            self.literature_fetcher = LiteratureFetcher(cache_dir="references_cache")

    def validate(
        self, suggestion: dict[str, Any], community_data: dict[str, Any]
    ) -> tuple[bool, list[ValidationError]]:
        """
        Perform multi-layer validation on a suggestion.

        Args:
            suggestion: Suggested repair (dict from LLM)
            community_data: Full community YAML data

        Returns:
            Tuple of (is_valid, list of errors)
        """
        errors = []

        # Layer 1: Schema validation
        schema_errors = self.validate_schema(suggestion)
        errors.extend(schema_errors)

        # Layer 2: Ontology validation
        if self.validate_ontology_enabled:
            ontology_errors = self.validate_ontology_terms(suggestion)
            errors.extend(ontology_errors)

        # Layer 3: Evidence validation
        if self.validate_evidence_enabled:
            evidence_errors = self.validate_evidence(suggestion)
            errors.extend(evidence_errors)

        # Layer 4: Biological plausibility
        if self.check_plausibility_enabled:
            plausibility_errors = self.check_biological_plausibility(suggestion, community_data)
            errors.extend(plausibility_errors)

        # Check if any critical errors
        has_errors = any(e.severity == "error" for e in errors)

        return not has_errors, errors

    def validate_schema(self, suggestion: dict[str, Any]) -> list[ValidationError]:
        """
        Layer 1: Validate YAML structure against LinkML schema.

        Args:
            suggestion: Suggested repair

        Returns:
            List of validation errors
        """
        errors = []

        # Check for required top-level key
        if "suggested_interactions" not in suggestion:
            errors.append(
                ValidationError(
                    layer="schema",
                    field="suggested_interactions",
                    message="Missing required field 'suggested_interactions'",
                    severity="error",
                )
            )
            return errors

        # Validate each interaction
        for idx, interaction in enumerate(suggestion.get("suggested_interactions", [])):
            # Required fields for EcologicalInteraction
            required_fields = [
                "name",
                "interaction_type",
                "description",
                "source_taxon",
            ]

            for field in required_fields:
                if field not in interaction:
                    errors.append(
                        ValidationError(
                            layer="schema",
                            field=f"suggested_interactions[{idx}].{field}",
                            message=f"Missing required field '{field}'",
                            severity="error",
                        )
                    )

            # Validate source_taxon structure
            if "source_taxon" in interaction:
                source_errors = self._validate_taxon_term(
                    interaction["source_taxon"],
                    f"suggested_interactions[{idx}].source_taxon",
                )
                errors.extend(source_errors)

            # Validate target_taxon structure (if present)
            if "target_taxon" in interaction:
                target_errors = self._validate_taxon_term(
                    interaction["target_taxon"],
                    f"suggested_interactions[{idx}].target_taxon",
                )
                errors.extend(target_errors)

            # Validate interaction_type is valid enum
            valid_types = [
                "MUTUALISM",
                "SYNTROPHY",
                "COMPETITION",
                "PREDATION",
                "PARASITISM",
                "COMMENSALISM",
                "AMENSALISM",
            ]
            if interaction.get("interaction_type") not in valid_types:
                errors.append(
                    ValidationError(
                        layer="schema",
                        field=f"suggested_interactions[{idx}].interaction_type",
                        message=f"Invalid interaction type. Must be one of: {', '.join(valid_types)}",
                        severity="error",
                    )
                )

            # Validate evidence structure
            if "evidence" in interaction:
                for ev_idx, evidence in enumerate(interaction["evidence"]):
                    evidence_errors = self._validate_evidence_item(
                        evidence, f"suggested_interactions[{idx}].evidence[{ev_idx}]"
                    )
                    errors.extend(evidence_errors)

        return errors

    def _validate_taxon_term(
        self, taxon_term: dict[str, Any], field_path: str
    ) -> list[ValidationError]:
        """Validate TaxonTerm structure."""
        errors = []

        # Check for required fields
        if "preferred_term" not in taxon_term:
            errors.append(
                ValidationError(
                    layer="schema",
                    field=f"{field_path}.preferred_term",
                    message="Missing required field 'preferred_term'",
                    severity="error",
                )
            )

        if "term" not in taxon_term:
            errors.append(
                ValidationError(
                    layer="schema",
                    field=f"{field_path}.term",
                    message="Missing required field 'term'",
                    severity="error",
                )
            )
        else:
            # Validate term structure
            term = taxon_term["term"]
            if "id" not in term:
                errors.append(
                    ValidationError(
                        layer="schema",
                        field=f"{field_path}.term.id",
                        message="Missing required field 'id'",
                        severity="error",
                    )
                )
            if "label" not in term:
                errors.append(
                    ValidationError(
                        layer="schema",
                        field=f"{field_path}.term.label",
                        message="Missing required field 'label'",
                        severity="error",
                    )
                )

        return errors

    def _validate_evidence_item(
        self, evidence: dict[str, Any], field_path: str
    ) -> list[ValidationError]:
        """Validate EvidenceItem structure."""
        errors = []

        # Required fields
        required = ["reference", "supports", "evidence_source", "snippet"]
        for field in required:
            if field not in evidence:
                errors.append(
                    ValidationError(
                        layer="schema",
                        field=f"{field_path}.{field}",
                        message=f"Missing required field '{field}'",
                        severity="error",
                    )
                )

        # Validate enums
        if evidence.get("supports") not in ["SUPPORT", "REFUTE", "NO_EVIDENCE"]:
            errors.append(
                ValidationError(
                    layer="schema",
                    field=f"{field_path}.supports",
                    message="Invalid value for 'supports'",
                    severity="error",
                )
            )

        if evidence.get("evidence_source") not in ["LITERATURE", "DATABASE", "EXPERIMENTAL"]:
            errors.append(
                ValidationError(
                    layer="schema",
                    field=f"{field_path}.evidence_source",
                    message="Invalid value for 'evidence_source'",
                    severity="error",
                )
            )

        return errors

    def validate_ontology_terms(self, suggestion: dict[str, Any]) -> list[ValidationError]:
        """
        Layer 2: Validate ontology term IDs via OAK.

        Args:
            suggestion: Suggested repair

        Returns:
            List of validation errors
        """
        errors = []

        for idx, interaction in enumerate(suggestion.get("suggested_interactions", [])):
            # Validate NCBITaxon IDs
            if "source_taxon" in interaction:
                source_id = interaction["source_taxon"].get("term", {}).get("id")
                if source_id and not self._validate_ncbi_taxon(source_id):
                    errors.append(
                        ValidationError(
                            layer="ontology",
                            field=f"suggested_interactions[{idx}].source_taxon.term.id",
                            message=f"Invalid NCBITaxon ID: {source_id}",
                            severity="error",
                        )
                    )

            if "target_taxon" in interaction:
                target_id = interaction["target_taxon"].get("term", {}).get("id")
                if target_id and not self._validate_ncbi_taxon(target_id):
                    errors.append(
                        ValidationError(
                            layer="ontology",
                            field=f"suggested_interactions[{idx}].target_taxon.term.id",
                            message=f"Invalid NCBITaxon ID: {target_id}",
                            severity="error",
                        )
                    )

            # Validate CHEBI IDs
            for met_idx, metabolite in enumerate(interaction.get("metabolites_exchanged", [])):
                met_id = metabolite.get("metabolite_term", {}).get("id")
                if met_id and not self._validate_chebi_id(met_id):
                    errors.append(
                        ValidationError(
                            layer="ontology",
                            field=f"suggested_interactions[{idx}].metabolites_exchanged[{met_idx}].metabolite_term.id",
                            message=f"Invalid CHEBI ID: {met_id}",
                            severity="warning",  # Warning only for now
                        )
                    )

            # Validate GO IDs
            for proc_idx, process in enumerate(interaction.get("biological_processes", [])):
                proc_id = process.get("id")
                if proc_id and not self._validate_go_id(proc_id):
                    errors.append(
                        ValidationError(
                            layer="ontology",
                            field=f"suggested_interactions[{idx}].biological_processes[{proc_idx}].id",
                            message=f"Invalid GO ID: {proc_id}",
                            severity="warning",  # Warning only for now
                        )
                    )

        return errors

    def _validate_ncbi_taxon(self, taxon_id: str) -> bool:
        """Validate NCBITaxon ID format."""
        # Basic format check: NCBITaxon:NNNNN
        if not taxon_id.startswith("NCBITaxon:"):
            return False
        try:
            int(taxon_id.split(":")[1])
            return True
        except (ValueError, IndexError):
            return False

    def _validate_chebi_id(self, chebi_id: str) -> bool:
        """Validate CHEBI ID format."""
        # Basic format check: CHEBI:NNNNN
        if not chebi_id.startswith("CHEBI:"):
            return False
        try:
            int(chebi_id.split(":")[1])
            return True
        except (ValueError, IndexError):
            return False

    def _validate_go_id(self, go_id: str) -> bool:
        """Validate GO ID format."""
        # Basic format check: GO:NNNNNNN
        if not go_id.startswith("GO:"):
            return False
        try:
            int(go_id.split(":")[1])
            return True
        except (ValueError, IndexError):
            return False

    def validate_evidence(self, suggestion: dict[str, Any]) -> list[ValidationError]:
        """
        Layer 3: Validate evidence snippets match abstracts.

        Args:
            suggestion: Suggested repair

        Returns:
            List of validation errors
        """
        errors = []

        for idx, interaction in enumerate(suggestion.get("suggested_interactions", [])):
            for ev_idx, evidence in enumerate(interaction.get("evidence", [])):
                reference = evidence.get("reference")
                snippet = evidence.get("snippet")

                if not reference or not snippet:
                    continue  # Skip if missing (schema validation will catch)

                # Fetch abstract
                try:
                    abstract, _ = self.literature_fetcher.fetch_paper(reference)

                    if not abstract:
                        errors.append(
                            ValidationError(
                                layer="evidence",
                                field=f"suggested_interactions[{idx}].evidence[{ev_idx}].reference",
                                message=f"Could not fetch abstract for {reference}",
                                severity="warning",
                            )
                        )
                        continue

                    # Validate snippet match
                    is_valid = self._validate_snippet_match(snippet, abstract)

                    if not is_valid:
                        errors.append(
                            ValidationError(
                                layer="evidence",
                                field=f"suggested_interactions[{idx}].evidence[{ev_idx}].snippet",
                                message=f"Snippet does not match abstract (< {self.min_snippet_match_score*100}% similarity)",
                                severity="error",
                            )
                        )

                except Exception as e:
                    errors.append(
                        ValidationError(
                            layer="evidence",
                            field=f"suggested_interactions[{idx}].evidence[{ev_idx}].reference",
                            message=f"Error validating evidence: {e}",
                            severity="warning",
                        )
                    )

        return errors

    def _validate_snippet_match(self, snippet: str, abstract: str) -> bool:
        """
        Check if snippet matches abstract with fuzzy matching.

        Args:
            snippet: Quoted snippet from YAML
            abstract: Full abstract text

        Returns:
            True if snippet found in abstract with >= min_snippet_match_score similarity
        """
        if not abstract or not snippet:
            return False

        # Normalize whitespace
        snippet_normalized = " ".join(snippet.split())
        abstract_normalized = " ".join(abstract.split())

        # Check for exact match (case-insensitive)
        if snippet_normalized.lower() in abstract_normalized.lower():
            return True

        # Check for fuzzy match
        ratio = SequenceMatcher(
            None, snippet_normalized.lower(), abstract_normalized.lower()
        ).ratio()

        return ratio >= self.min_snippet_match_score

    def check_biological_plausibility(
        self, suggestion: dict[str, Any], community_data: dict[str, Any]
    ) -> list[ValidationError]:
        """
        Layer 4: Check biological plausibility of suggestions.

        Args:
            suggestion: Suggested repair
            community_data: Full community YAML data

        Returns:
            List of validation errors (warnings)
        """
        errors = []

        # Build taxonomy lookup
        taxonomy_by_term = {}
        for taxon in community_data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            if preferred:
                taxonomy_by_term[preferred] = taxon

        for idx, interaction in enumerate(suggestion.get("suggested_interactions", [])):
            # Check 1: Taxa should exist in taxonomy
            source_term = interaction.get("source_taxon", {}).get("preferred_term")
            target_term = interaction.get("target_taxon", {}).get("preferred_term")

            if source_term and source_term not in taxonomy_by_term:
                errors.append(
                    ValidationError(
                        layer="plausibility",
                        field=f"suggested_interactions[{idx}].source_taxon",
                        message=f"Source taxon '{source_term}' not found in community taxonomy",
                        severity="error",
                    )
                )

            if target_term and target_term not in taxonomy_by_term:
                errors.append(
                    ValidationError(
                        layer="plausibility",
                        field=f"suggested_interactions[{idx}].target_taxon",
                        message=f"Target taxon '{target_term}' not found in community taxonomy",
                        severity="error",
                    )
                )

            # Check 2: Warn about unusual interaction types
            interaction_type = interaction.get("interaction_type")
            metabolites = interaction.get("metabolites_exchanged", [])

            if interaction_type in ["MUTUALISM", "SYNTROPHY"] and not metabolites:
                errors.append(
                    ValidationError(
                        layer="plausibility",
                        field=f"suggested_interactions[{idx}].metabolites_exchanged",
                        message=f"{interaction_type} interaction typically involves metabolite exchange",
                        severity="warning",
                    )
                )

            # Check 3: Warn if evidence is weak
            evidence_items = interaction.get("evidence", [])
            if not evidence_items:
                errors.append(
                    ValidationError(
                        layer="plausibility",
                        field=f"suggested_interactions[{idx}].evidence",
                        message="No evidence provided for interaction",
                        severity="warning",
                    )
                )

        return errors
