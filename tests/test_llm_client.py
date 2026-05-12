"""Tests for LLM client integration."""

import os
from unittest.mock import MagicMock, patch

import pytest

# Try to import anthropic, but don't fail if not installed
try:
    from communitymech.llm.anthropic_client import AnthropicClient

    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

from communitymech.llm.prompts import DISCONNECTED_TAXON_PROMPT


@pytest.fixture
def mock_config():
    """Create mock configuration."""
    return {
        "llm": {
            "provider": "anthropic",
            "model": "claude-opus-4-6",
            "api_key_env": "ANTHROPIC_API_KEY",
            "temperature": 0.1,
            "max_tokens": 4096,
            "timeout": 60,
        },
        "repair": {
            "auto_approve_threshold": 0.95,
            "max_suggestions_per_taxon": 2,
            "require_evidence_validation": True,
            "backup_before_apply": True,
        },
        "limits": {
            "max_api_calls_per_run": 100,
            "rate_limit_per_minute": 10,
            "track_costs": True,
            "max_cost_per_run": 10.0,
        },
    }


@pytest.fixture
def mock_api_response():
    """Create mock API response."""
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="""Here's a suggested interaction:

```yaml
suggested_interactions:
  - name: "Iron Cycling Partnership"
    interaction_type: "MUTUALISM"
    description: "Ferroplasma reduces Fe(III) which Leptospirillum oxidizes"
    source_taxon:
      preferred_term: "Ferroplasma acidarmanus"
      term:
        id: "NCBITaxon:55206"
        label: "Ferroplasma acidarmanus"
    target_taxon:
      preferred_term: "Leptospirillum group II"
      term:
        id: "NCBITaxon:1228"
        label: "Leptospirillum group II"
    metabolites_exchanged:
      - metabolite_term:
          id: "CHEBI:29033"
          label: "iron(2+)"
        direction: "source_to_target"
    biological_processes:
      - id: "GO:0055114"
        label: "oxidation-reduction process"
    evidence:
      - reference: "PMID:15066799"
        supports: "SUPPORT"
        evidence_source: "LITERATURE"
        snippet: "Ferroplasma acidarmanus was capable of growing by reduction of Fe(III)"
```
""")]
    mock_response.usage = MagicMock()
    mock_response.usage.input_tokens = 2500
    mock_response.usage.output_tokens = 800
    return mock_response


@pytest.mark.skipif(not ANTHROPIC_AVAILABLE, reason="anthropic package not installed")
class TestAnthropicClient:
    """Tests for Anthropic client."""

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_client_initialization(self, mock_anthropic_class, mock_config):
        """Test client initializes correctly."""
        client = AnthropicClient(config=mock_config)

        assert client.model == "claude-opus-4-6"
        assert client.max_tokens == 4096
        assert client.api_calls == 0
        assert client.total_input_tokens == 0
        assert client.total_output_tokens == 0

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_api_key_raises(self, mock_config):
        """Test that missing API key raises ValueError."""
        with pytest.raises(ValueError, match="API key not found"):
            AnthropicClient(config=mock_config)

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_validate_api_key(self, mock_anthropic_class, mock_config):
        """Test API key validation."""
        # Setup mock
        mock_client = MagicMock()
        mock_anthropic_class.return_value = mock_client
        mock_client.messages.create.return_value = MagicMock()

        client = AnthropicClient(config=mock_config)
        is_valid = client.validate_api_key()

        assert is_valid is True
        mock_client.messages.create.assert_called_once()

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_generate_suggestion(self, mock_anthropic_class, mock_config, mock_api_response):
        """Test suggestion generation."""
        # Setup mock
        mock_client = MagicMock()
        mock_anthropic_class.return_value = mock_client
        mock_client.messages.create.return_value = mock_api_response

        client = AnthropicClient(config=mock_config)

        # Generate suggestion
        context = {
            "community_name": "Test Community",
            "environment": "Acid mine drainage",
            "environmental_context": "pH: 2.0\nTemp: 40°C",
            "taxon_name": "Ferroplasma acidarmanus",
            "taxon_id": "NCBITaxon:55206",
            "taxon_context": "Functional roles: Iron reducer",
            "connected_taxa": "Leptospirillum group II (NCBITaxon:1228)",
            "interaction_summary": "Interactions: 5\nTypes: MUTUALISM",
        }

        suggestion = client.generate_suggestion(
            prompt=DISCONNECTED_TAXON_PROMPT, context=context, temperature=0.1
        )

        # Verify API was called
        mock_client.messages.create.assert_called_once()

        # Verify suggestion structure
        assert "suggested_interactions" in suggestion
        assert len(suggestion["suggested_interactions"]) == 1

        interaction = suggestion["suggested_interactions"][0]
        assert interaction["name"] == "Iron Cycling Partnership"
        assert interaction["interaction_type"] == "MUTUALISM"
        assert "source_taxon" in interaction
        assert "target_taxon" in interaction
        assert "metabolites_exchanged" in interaction
        assert "evidence" in interaction

        # Verify cost tracking
        assert client.api_calls == 1
        assert client.total_input_tokens == 2500
        assert client.total_output_tokens == 800

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_cost_estimation(self, mock_anthropic_class, mock_config, mock_api_response):
        """Test cost estimation."""
        # Setup mock
        mock_client = MagicMock()
        mock_anthropic_class.return_value = mock_client
        mock_client.messages.create.return_value = mock_api_response

        client = AnthropicClient(config=mock_config)

        # Manually set usage for testing
        client.api_calls = 5
        client.total_input_tokens = 10000
        client.total_output_tokens = 4000

        cost = client.get_cost_estimate()

        assert cost["model"] == "claude-opus-4-6"
        assert cost["api_calls"] == 5
        assert cost["input_tokens"] == 10000
        assert cost["output_tokens"] == 4000
        assert cost["total_tokens"] == 14000

        # Opus pricing: $15/1M input, $75/1M output
        expected_input_cost = (10000 / 1_000_000) * 15.0
        expected_output_cost = (4000 / 1_000_000) * 75.0
        expected_total = expected_input_cost + expected_output_cost

        assert abs(cost["input_cost_usd"] - expected_input_cost) < 0.001
        assert abs(cost["output_cost_usd"] - expected_output_cost) < 0.001
        assert abs(cost["total_cost_usd"] - expected_total) < 0.001

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_parse_yaml_response(self, mock_anthropic_class, mock_config):
        """Test YAML parsing from LLM response."""
        client = AnthropicClient(config=mock_config)

        # Test with YAML code block
        response_with_yaml = """Here's the suggestion:

```yaml
suggested_interactions:
  - name: "Test Interaction"
    interaction_type: "MUTUALISM"
```

This should work well."""

        parsed = client._parse_yaml_response(response_with_yaml)
        assert "suggested_interactions" in parsed
        assert parsed["suggested_interactions"][0]["name"] == "Test Interaction"

        # Test with generic code block
        response_with_generic = """
```
key: value
another: 123
```
"""
        parsed = client._parse_yaml_response(response_with_generic)
        assert parsed["key"] == "value"
        assert parsed["another"] == 123

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_api_call_limit(self, mock_anthropic_class, mock_config):
        """Test that API call limit is enforced."""
        # Set low limit for testing
        mock_config["limits"]["max_api_calls_per_run"] = 2

        mock_client = MagicMock()
        mock_anthropic_class.return_value = mock_client
        mock_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="```yaml\nkey: value\n```")],
            usage=MagicMock(input_tokens=100, output_tokens=50),
        )

        client = AnthropicClient(config=mock_config)

        # First call should work
        client.generate_suggestion(prompt="test: {key}", context={"key": "value"}, temperature=0.1)
        assert client.api_calls == 1

        # Second call should work
        client.generate_suggestion(prompt="test: {key}", context={"key": "value"}, temperature=0.1)
        assert client.api_calls == 2

        # Third call should raise
        with pytest.raises(RuntimeError, match="API call limit reached"):
            client.generate_suggestion(
                prompt="test: {key}", context={"key": "value"}, temperature=0.1
            )

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_missing_context_key_raises(self, mock_anthropic_class, mock_config):
        """Test that missing context key raises ValueError."""
        client = AnthropicClient(config=mock_config)

        with pytest.raises(ValueError, match="Missing context key"):
            client.generate_suggestion(prompt="Hello {missing_key}", context={}, temperature=0.1)

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "sk-ant-test-key"})
    @patch("communitymech.llm.anthropic_client.anthropic.Anthropic")
    def test_reset_cost_tracking(self, mock_anthropic_class, mock_config):
        """Test resetting cost tracking."""
        client = AnthropicClient(config=mock_config)

        # Set some values
        client.api_calls = 10
        client.total_input_tokens = 5000
        client.total_output_tokens = 2000

        # Reset
        client.reset_cost_tracking()

        assert client.api_calls == 0
        assert client.total_input_tokens == 0
        assert client.total_output_tokens == 0


def test_import_without_anthropic():
    """Test that module can be imported without anthropic package."""
    # This test just verifies the import doesn't fail
    from communitymech.llm import ContextBuilder, LLMClient

    assert ContextBuilder is not None
    assert LLMClient is not None
