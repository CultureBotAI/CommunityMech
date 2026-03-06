"""LLM integration for network repair suggestions.

This module provides abstracted LLM clients for generating biologically
plausible network repair suggestions with evidence validation.
"""

from communitymech.llm.client import LLMClient
from communitymech.llm.context_builder import ContextBuilder

try:
    from communitymech.llm.anthropic_client import AnthropicClient

    __all__ = ["LLMClient", "AnthropicClient", "ContextBuilder"]
except ImportError:
    # anthropic package not installed
    __all__ = ["LLMClient", "ContextBuilder"]
