"""Repair strategies for different types of network integrity issues."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Tuple

from communitymech.llm.context_builder import ContextBuilder
from communitymech.llm.prompts import (
    DISCONNECTED_TAXON_PROMPT,
    MISSING_SOURCE_PROMPT,
    UNKNOWN_TARGET_PROMPT,
)
from communitymech.network.auditor import IssueType
from communitymech.network.validators import SuggestionValidator


class RepairStrategy(ABC):
    """Abstract base class for repair strategies."""

    def __init__(self, community_path: Path, validator: SuggestionValidator):
        """
        Initialize repair strategy.

        Args:
            community_path: Path to community YAML file
            validator: Suggestion validator instance
        """
        self.community_path = Path(community_path)
        self.validator = validator
        self.context_builder = ContextBuilder(community_path)

    @abstractmethod
    def can_handle(self, issue: Dict[str, Any]) -> bool:
        """
        Check if this strategy can handle the given issue.

        Args:
            issue: Issue dict from auditor

        Returns:
            True if this strategy can handle the issue
        """
        pass

    @abstractmethod
    def build_context(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build LLM context for this issue.

        Args:
            issue: Issue dict from auditor

        Returns:
            Context dict for prompt formatting
        """
        pass

    @abstractmethod
    def get_prompt_template(self) -> str:
        """
        Get prompt template for this strategy.

        Returns:
            Prompt template string
        """
        pass

    def validate_suggestion(
        self, suggestion: Dict[str, Any], community_data: Dict[str, Any]
    ) -> Tuple[bool, List]:
        """
        Validate LLM suggestion using multi-layer validation.

        Args:
            suggestion: Suggested repair from LLM
            community_data: Full community YAML data

        Returns:
            Tuple of (is_valid, list of errors)
        """
        return self.validator.validate(suggestion, community_data)

    def get_issue_summary(self, issue: Dict[str, Any]) -> str:
        """
        Get human-readable summary of the issue.

        Args:
            issue: Issue dict from auditor

        Returns:
            Summary string
        """
        return issue.get("message", "Unknown issue")


class DisconnectedTaxonStrategy(RepairStrategy):
    """Strategy for repairing disconnected taxa."""

    def can_handle(self, issue: Dict[str, Any]) -> bool:
        """Check if this is a DISCONNECTED issue."""
        return issue.get("type") == IssueType.DISCONNECTED

    def build_context(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build context for disconnected taxon repair.

        Args:
            issue: Issue dict with 'taxon' and 'taxon_id'

        Returns:
            Context dict for DISCONNECTED_TAXON_PROMPT
        """
        taxon_name = issue.get("taxon")
        taxon_id = issue.get("taxon_id")

        if not taxon_name or not taxon_id:
            raise ValueError(
                f"Issue missing required fields 'taxon' or 'taxon_id': {issue}"
            )

        return self.context_builder.build_disconnected_taxon_context(
            taxon_name=taxon_name, taxon_id=taxon_id
        )

    def get_prompt_template(self) -> str:
        """Get DISCONNECTED_TAXON_PROMPT."""
        return DISCONNECTED_TAXON_PROMPT

    def get_issue_summary(self, issue: Dict[str, Any]) -> str:
        """Get summary for disconnected taxon."""
        taxon = issue.get("taxon", "Unknown")
        taxon_id = issue.get("taxon_id", "Unknown")
        return f"Disconnected: {taxon} ({taxon_id})"


class MissingSourceStrategy(RepairStrategy):
    """Strategy for identifying missing source_taxon."""

    def can_handle(self, issue: Dict[str, Any]) -> bool:
        """Check if this is a MISSING_SOURCE issue."""
        return issue.get("type") == IssueType.MISSING_SOURCE

    def build_context(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build context for missing source repair.

        Args:
            issue: Issue dict with 'interaction' and 'interaction_index'

        Returns:
            Context dict for MISSING_SOURCE_PROMPT
        """
        interaction_name = issue.get("interaction", "Unknown")
        interaction_index = issue.get("interaction_index")

        if interaction_index is None:
            raise ValueError(
                f"Issue missing required field 'interaction_index': {issue}"
            )

        return self.context_builder.build_missing_source_context(
            interaction_name=interaction_name, interaction_index=interaction_index
        )

    def get_prompt_template(self) -> str:
        """Get MISSING_SOURCE_PROMPT."""
        return MISSING_SOURCE_PROMPT

    def get_issue_summary(self, issue: Dict[str, Any]) -> str:
        """Get summary for missing source."""
        interaction = issue.get("interaction", "Unknown")
        return f"Missing source: {interaction}"


class UnknownTargetStrategy(RepairStrategy):
    """Strategy for resolving unknown target taxon references."""

    def can_handle(self, issue: Dict[str, Any]) -> bool:
        """Check if this is an UNKNOWN_TARGET issue."""
        return issue.get("type") == IssueType.UNKNOWN_TARGET

    def build_context(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build context for unknown target resolution.

        Args:
            issue: Issue dict with 'interaction' and 'taxon'

        Returns:
            Context dict for UNKNOWN_TARGET_PROMPT
        """
        interaction_name = issue.get("interaction", "Unknown")
        unknown_target = issue.get("taxon")

        if not unknown_target:
            raise ValueError(f"Issue missing required field 'taxon': {issue}")

        return self.context_builder.build_unknown_target_context(
            interaction_name=interaction_name, unknown_target=unknown_target
        )

    def get_prompt_template(self) -> str:
        """Get UNKNOWN_TARGET_PROMPT."""
        return UNKNOWN_TARGET_PROMPT

    def get_issue_summary(self, issue: Dict[str, Any]) -> str:
        """Get summary for unknown target."""
        interaction = issue.get("interaction", "Unknown")
        taxon = issue.get("taxon", "Unknown")
        return f"Unknown target in {interaction}: {taxon}"


class UnknownSourceStrategy(RepairStrategy):
    """Strategy for resolving unknown source taxon references."""

    def can_handle(self, issue: Dict[str, Any]) -> bool:
        """Check if this is an UNKNOWN_SOURCE issue."""
        return issue.get("type") == IssueType.UNKNOWN_SOURCE

    def build_context(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build context for unknown source resolution.

        Note: Uses same prompt as unknown target resolution.

        Args:
            issue: Issue dict with 'interaction' and 'taxon'

        Returns:
            Context dict for UNKNOWN_TARGET_PROMPT
        """
        interaction_name = issue.get("interaction", "Unknown")
        unknown_source = issue.get("taxon")

        if not unknown_source:
            raise ValueError(f"Issue missing required field 'taxon': {issue}")

        # Reuse unknown target context builder and prompt
        return self.context_builder.build_unknown_target_context(
            interaction_name=interaction_name, unknown_target=unknown_source
        )

    def get_prompt_template(self) -> str:
        """Get UNKNOWN_TARGET_PROMPT (reused for source)."""
        return UNKNOWN_TARGET_PROMPT

    def get_issue_summary(self, issue: Dict[str, Any]) -> str:
        """Get summary for unknown source."""
        interaction = issue.get("interaction", "Unknown")
        taxon = issue.get("taxon", "Unknown")
        return f"Unknown source in {interaction}: {taxon}"


class StrategySelector:
    """Select appropriate repair strategy for an issue."""

    def __init__(self, community_path: Path, validator: SuggestionValidator):
        """
        Initialize strategy selector.

        Args:
            community_path: Path to community YAML file
            validator: Suggestion validator instance
        """
        self.community_path = Path(community_path)
        self.validator = validator

        # Initialize all strategies
        self.strategies = [
            DisconnectedTaxonStrategy(community_path, validator),
            MissingSourceStrategy(community_path, validator),
            UnknownTargetStrategy(community_path, validator),
            UnknownSourceStrategy(community_path, validator),
        ]

    def select_strategy(self, issue: Dict[str, Any]) -> RepairStrategy:
        """
        Select appropriate strategy for the given issue.

        Args:
            issue: Issue dict from auditor

        Returns:
            RepairStrategy instance

        Raises:
            ValueError: If no strategy can handle the issue
        """
        for strategy in self.strategies:
            if strategy.can_handle(issue):
                return strategy

        raise ValueError(f"No strategy found for issue type: {issue.get('type')}")

    def can_repair(self, issue: Dict[str, Any]) -> bool:
        """
        Check if any strategy can repair this issue.

        Args:
            issue: Issue dict from auditor

        Returns:
            True if a strategy exists for this issue type
        """
        try:
            self.select_strategy(issue)
            return True
        except ValueError:
            return False

    def get_repairable_issue_types(self) -> List[str]:
        """
        Get list of issue types that can be repaired.

        Returns:
            List of IssueType values
        """
        return [
            IssueType.DISCONNECTED,
            IssueType.MISSING_SOURCE,
            IssueType.UNKNOWN_TARGET,
            IssueType.UNKNOWN_SOURCE,
        ]
