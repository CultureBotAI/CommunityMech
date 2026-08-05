# CommunityMech Network Repair - Quick Start

## 5-Minute Setup

```bash
# 1. Install
just install

# 2. Set API key (get from: https://console.anthropic.com/)
export ANTHROPIC_API_KEY=sk-ant-your-key

# 3. Test
uv run pytest tests/ -v
```

## Common Commands

### Audit Network

```bash
# Check all communities for issues
just audit-network

# CI mode (exits with error if issues found)
just check-network-quality
```

### Interactive Repair (Single Community)

```bash
# Repair one community with interactive prompts
just repair-network kb/communities/YourCommunity.yaml

# Controls: [A]pprove [E]dit [R]eject [S]kip [Q]uit

# Dry-run (no changes)
just repair-network-dry kb/communities/YourCommunity.yaml
```

### Batch Repair (Multiple Communities)

```bash
# 1. Generate suggestions report
just suggest-network-repairs

# 2. Review offline
vim reports/network_repair_suggestions.yaml
# Set approved: true for suggestions to apply

# 3. Apply approved
just apply-batch-repairs reports/network_repair_suggestions.yaml
```

## Costs

| Model | Per Suggestion | 76 Communities |
|-------|----------------|----------------|
| Haiku 4.5 (fast) | $0.002 | $0.30 |
| **Sonnet 4.6 (recommended)** | **$0.02** | **$3.00** |
| Opus 4.6 (best) | $0.08 | $12.00 |

## Documentation

- **Full User Guide**: `docs/NETWORK_REPAIR_USER_GUIDE.md` (865 lines)
- **Setup Guide**: `docs/LLM_SETUP_GUIDE.md`
- **Project Summary**: `PROJECT_COMPLETION_SUMMARY.md`
- **Phase Completion Reports**: `PHASE_1-5_COMPLETION.md` files

## Workflows

### Workflow 1: Quick Fix

```bash
just audit-network                      # Find issues
just repair-network FILE                # Fix interactively
just validate FILE                      # Verify
```

### Workflow 2: Production Batch

```bash
just suggest-network-repairs            # Generate ($3-12)
# Review offline, set approved: true
just apply-batch-repairs REPORT         # Apply
just qc                                 # lint + tests + offline validators
```

### Workflow 3: Testing

```bash
just suggest-network-repairs-limited 5  # Small batch
# Review, approve, apply
just apply-batch-repairs REPORT
```

## Validation

Every suggestion passes 4 layers:

1. ✅ **Schema**: LinkML validation
2. ✅ **Ontology**: NCBITaxon, CHEBI, GO via OAK
3. ✅ **Evidence**: 95%+ snippet match to abstract
4. ✅ **Plausibility**: Biological coherence checks

## Safety

- Human approval required (default)
- Automatic backups before changes
- Multi-layer validation
- Dry-run mode available
- Git integration
- Cost limits configurable

## Performance

- **Parallel Processing**: 4x speedup (default enabled)
- **Context Caching**: 60% cost reduction
- **Rate Limiting**: Prevents API throttling

**Benchmark**: 76 communities in 1m 35s (vs 6m 20s sequential)

## Troubleshooting

**API Key Error**:
```bash
export ANTHROPIC_API_KEY=sk-ant-your-key
echo $ANTHROPIC_API_KEY  # Verify
```

**Rate Limit**:
```yaml
# conf/llm_config.yaml
limits:
  rate_limit_per_minute: 5  # Reduce from 10
```

**Validation Failed**:
- LLM hallucinated evidence
- Reject and regenerate
- Or edit suggestion manually

## Support

- **Documentation**: `docs/` directory
- **Tests**: `tests/test_e2e_repair.py` for examples
- **Configuration**: `conf/llm_config.yaml`

---

**Version**: 1.0.0
**Status**: Production Ready ✅
**Last Updated**: March 6, 2026
