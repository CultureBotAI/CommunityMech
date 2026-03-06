"""Network integrity checking and repair for CommunityMech.

This module provides tools for auditing, validating, and repairing
network integrity issues in microbial community YAML files.
"""

from communitymech.network.auditor import NetworkIntegrityAuditor
from communitymech.network.batch_reporter import BatchReporter
from communitymech.network.llm_repair import LLMNetworkRepairer
from communitymech.network.repair_strategies import (
    DisconnectedTaxonStrategy,
    MissingSourceStrategy,
    RepairStrategy,
    StrategySelector,
    UnknownSourceStrategy,
    UnknownTargetStrategy,
)
from communitymech.network.validators import SuggestionValidator, ValidationError

__all__ = [
    "NetworkIntegrityAuditor",
    "LLMNetworkRepairer",
    "BatchReporter",
    "SuggestionValidator",
    "ValidationError",
    "RepairStrategy",
    "DisconnectedTaxonStrategy",
    "MissingSourceStrategy",
    "UnknownTargetStrategy",
    "UnknownSourceStrategy",
    "StrategySelector",
]
