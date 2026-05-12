"""Abstract base class for LLM clients."""

from abc import ABC, abstractmethod
from typing import Any


class LLMClient(ABC):
    """Abstract base class for LLM integration."""

    @abstractmethod
    def generate_suggestion(
        self, prompt: str, context: dict[str, Any], temperature: float = 0.1
    ) -> dict[str, Any]:
        """
        Generate a repair suggestion using the LLM.

        Args:
            prompt: The prompt template to use
            context: Context dictionary for prompt formatting
            temperature: Sampling temperature (lower = more deterministic)

        Returns:
            Suggestion dictionary with repair details
        """
        pass

    @abstractmethod
    def validate_api_key(self) -> bool:
        """
        Validate that API key is configured and valid.

        Returns:
            True if API key is valid
        """
        pass
