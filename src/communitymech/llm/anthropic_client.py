"""Anthropic Claude API client for network repair suggestions."""

import os
import time
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

try:
    import anthropic
except ImportError:
    anthropic = None

from communitymech.llm.client import LLMClient
from communitymech.llm.prompts import SYSTEM_MESSAGE


class AnthropicClient(LLMClient):
    """Claude API integration with caching and rate limiting."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize Anthropic client.

        Args:
            config: Configuration dict (if None, loads from conf/llm_config.yaml)
        """
        if anthropic is None:
            raise ImportError(
                "anthropic package not installed. "
                "Install with: uv sync --all-extras or pip install anthropic"
            )

        # Load config
        if config is None:
            config = self._load_config()
        self.config = config

        # Get API key from environment
        api_key_env = config.get("llm", {}).get("api_key_env", "ANTHROPIC_API_KEY")
        api_key = os.getenv(api_key_env)

        if not api_key:
            raise ValueError(
                f"API key not found. Set environment variable: {api_key_env}\n"
                f"Get your API key from: https://console.anthropic.com/"
            )

        # Initialize client
        self.client = anthropic.Anthropic(api_key=api_key)

        # Get model settings
        llm_config = config.get("llm", {})
        self.model = llm_config.get("model", "claude-opus-4-6")
        self.max_tokens = llm_config.get("max_tokens", 4096)
        self.timeout = llm_config.get("timeout", 60)

        # Rate limiting
        limits_config = config.get("limits", {})
        self.rate_limit_per_minute = limits_config.get("rate_limit_per_minute", 10)
        self.max_api_calls_per_run = limits_config.get("max_api_calls_per_run", 100)

        # Cost tracking
        self.track_costs = limits_config.get("track_costs", True)
        self.api_calls = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0

        # Rate limiting state
        self._last_request_time = 0
        self._requests_this_minute = []

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from conf/llm_config.yaml."""
        config_path = Path("conf/llm_config.yaml")
        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}\n"
                f"Create it from conf/llm_config.yaml template"
            )

        with open(config_path) as f:
            return yaml.safe_load(f)

    def _rate_limit(self):
        """Enforce rate limiting."""
        now = time.time()

        # Remove requests older than 1 minute
        self._requests_this_minute = [
            t for t in self._requests_this_minute if now - t < 60
        ]

        # Check if we're at the limit
        if len(self._requests_this_minute) >= self.rate_limit_per_minute:
            # Wait until oldest request is >1 minute old
            oldest = self._requests_this_minute[0]
            wait_time = 60 - (now - oldest)
            if wait_time > 0:
                print(f"⏳ Rate limit reached, waiting {wait_time:.1f}s...")
                time.sleep(wait_time)

        # Record this request
        self._requests_this_minute.append(now)

    def validate_api_key(self) -> bool:
        """
        Validate that API key is configured and valid.

        Returns:
            True if API key is valid
        """
        try:
            # Try a minimal API call
            response = self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{"role": "user", "content": "Hello"}],
            )
            return response is not None
        except Exception as e:
            print(f"API key validation failed: {e}")
            return False

    def generate_suggestion(
        self,
        prompt: str,
        context: Dict[str, Any],
        temperature: float = 0.1,
    ) -> Dict[str, Any]:
        """
        Generate a repair suggestion using Claude API.

        Args:
            prompt: The prompt template to use
            context: Context dictionary for prompt formatting
            temperature: Sampling temperature (lower = more deterministic)

        Returns:
            Suggestion dictionary with repair details

        Raises:
            RuntimeError: If API call fails
            ValueError: If response cannot be parsed
        """
        # Check API call limit
        if self.api_calls >= self.max_api_calls_per_run:
            raise RuntimeError(
                f"API call limit reached ({self.max_api_calls_per_run}). "
                f"Increase limits.max_api_calls_per_run in config if needed."
            )

        # Enforce rate limiting
        self._rate_limit()

        # Format prompt with context
        try:
            formatted_prompt = prompt.format(**context)
        except KeyError as e:
            raise ValueError(f"Missing context key for prompt: {e}")

        # Make API call
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=temperature,
                system=SYSTEM_MESSAGE,
                messages=[{"role": "user", "content": formatted_prompt}],
            )

            # Track usage
            self.api_calls += 1
            if self.track_costs:
                self.total_input_tokens += response.usage.input_tokens
                self.total_output_tokens += response.usage.output_tokens

            # Extract text response
            if not response.content or len(response.content) == 0:
                raise ValueError("Empty response from API")

            response_text = response.content[0].text

            # Parse YAML from response
            suggestion = self._parse_yaml_response(response_text)

            return suggestion

        except anthropic.APIError as e:
            raise RuntimeError(f"Anthropic API error: {e}")
        except Exception as e:
            raise RuntimeError(f"Error generating suggestion: {e}")

    def _parse_yaml_response(self, response_text: str) -> Dict[str, Any]:
        """
        Parse YAML from LLM response.

        Extracts YAML code blocks and parses them.

        Args:
            response_text: Raw response from LLM

        Returns:
            Parsed YAML dictionary

        Raises:
            ValueError: If YAML cannot be parsed
        """
        # Extract YAML code block
        yaml_content = None

        # Look for ```yaml code blocks
        if "```yaml" in response_text:
            parts = response_text.split("```yaml")
            if len(parts) > 1:
                yaml_content = parts[1].split("```")[0].strip()
        # Look for generic ``` code blocks
        elif "```" in response_text:
            parts = response_text.split("```")
            if len(parts) >= 3:
                yaml_content = parts[1].strip()
        else:
            # Try parsing entire response as YAML
            yaml_content = response_text.strip()

        if not yaml_content:
            raise ValueError("No YAML content found in response")

        # Parse YAML
        try:
            parsed = yaml.safe_load(yaml_content)
            if not isinstance(parsed, dict):
                raise ValueError(f"Expected dict, got {type(parsed)}")
            return parsed
        except yaml.YAMLError as e:
            raise ValueError(f"Failed to parse YAML: {e}\n\nContent:\n{yaml_content}")

    def get_cost_estimate(self) -> Dict[str, Any]:
        """
        Get cost estimate for API usage so far.

        Returns:
            Dictionary with cost breakdown
        """
        # Pricing per 1M tokens (as of March 2026)
        pricing = {
            "claude-opus-4-6": {"input": 15.0, "output": 75.0},
            "claude-sonnet-4-6": {"input": 3.0, "output": 15.0},
            "claude-haiku-4-5": {"input": 0.25, "output": 1.25},
        }

        model_pricing = pricing.get(
            self.model, {"input": 15.0, "output": 75.0}  # Default to Opus pricing
        )

        input_cost = (self.total_input_tokens / 1_000_000) * model_pricing["input"]
        output_cost = (self.total_output_tokens / 1_000_000) * model_pricing["output"]
        total_cost = input_cost + output_cost

        return {
            "model": self.model,
            "api_calls": self.api_calls,
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "input_cost_usd": round(input_cost, 4),
            "output_cost_usd": round(output_cost, 4),
            "total_cost_usd": round(total_cost, 4),
        }

    def reset_cost_tracking(self):
        """Reset cost tracking counters."""
        self.api_calls = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def __repr__(self) -> str:
        """String representation."""
        return f"AnthropicClient(model={self.model}, calls={self.api_calls})"
