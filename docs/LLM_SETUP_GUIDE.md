# LLM Setup Guide

This guide explains how to set up and use the LLM-assisted network repair features in CommunityMech.

## Prerequisites

- Python 3.10+
- `uv` package manager
- Anthropic API key (for Claude)

## Installation

### 1. Install Dependencies

```bash
# Install all dependencies including LLM support
uv sync --all-extras

# Or install anthropic separately
pip install anthropic>=0.39.0
```

### 2. Get Anthropic API Key

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-ant-...`)

### 3. Configure API Key

**Option A: Environment Variable (Recommended)**

```bash
# Linux/macOS
export ANTHROPIC_API_KEY=sk-ant-your-api-key-here

# Add to your shell profile for persistence
echo 'export ANTHROPIC_API_KEY=sk-ant-your-api-key-here' >> ~/.bashrc
source ~/.bashrc
```

**Option B: .env File**

```bash
# Copy example file
cp .env.example .env

# Edit .env and add your key
# ANTHROPIC_API_KEY=sk-ant-your-api-key-here

# Load .env (if using python-dotenv or direnv)
```

**Security Note**: Never commit API keys to version control. The `.env` file is already in `.gitignore`.

### 4. Verify Setup

```bash
# Test API key validation
uv run python -c "
from communitymech.llm.anthropic_client import AnthropicClient
client = AnthropicClient()
print('✅ API key valid' if client.validate_api_key() else '❌ Invalid')
"
```

## Configuration

### LLM Settings

Edit `conf/llm_config.yaml` to customize LLM behavior:

```yaml
llm:
  provider: anthropic
  model: claude-opus-4-6  # or claude-sonnet-4-6, claude-haiku-4-5
  temperature: 0.1  # Lower = more deterministic
  max_tokens: 4096

repair:
  auto_approve_threshold: 0.95  # Confidence for auto-approval
  max_suggestions_per_taxon: 2
  require_evidence_validation: true

limits:
  max_api_calls_per_run: 100
  rate_limit_per_minute: 10
  track_costs: true
  max_cost_per_run: 10.0  # USD
```

### Model Selection

**Claude Opus 4.6** (Recommended for quality):
- Best quality and biological reasoning
- $15/1M input tokens, $75/1M output tokens
- ~$0.08 per suggestion

**Claude Sonnet 4.6** (Recommended for cost):
- Good quality, faster, cheaper
- $3/1M input tokens, $15/1M output tokens
- ~$0.02 per suggestion

**Claude Haiku 4.5** (Fast and cheap):
- Basic quality, very fast
- $0.25/1M input tokens, $1.25/1M output tokens
- ~$0.003 per suggestion

## Usage

### Basic Workflow

```bash
# 1. Audit network to find issues
just audit-network

# 2. Generate LLM repair suggestion (coming in Phase 3-4)
communitymech repair-network kb/communities/Test.yaml

# 3. Review and approve suggestions
# (Interactive CLI will show suggestions with validation)

# 4. Verify repairs
just audit-network
```

### Cost Management

```bash
# Check estimated cost before running
# (Will be added in Phase 5)

# Set cost limits in conf/llm_config.yaml
limits:
  max_cost_per_run: 10.0  # Stop if cost exceeds $10

# Track costs during session
# Cost summary shown at end of repair session
```

## Python API

### Basic Usage

```python
from communitymech.llm.anthropic_client import AnthropicClient
from communitymech.llm.prompts import DISCONNECTED_TAXON_PROMPT

# Initialize client
client = AnthropicClient()

# Generate suggestion
context = {
    "community_name": "AMD Community",
    "environment": "Acid mine drainage",
    "environmental_context": "pH: 2.0, Temp: 40°C",
    "taxon_name": "Ferroplasma acidarmanus",
    "taxon_id": "NCBITaxon:55206",
    "taxon_context": "Iron reducer",
    "connected_taxa": "Leptospirillum (NCBITaxon:1228)",
    "interaction_summary": "5 mutualistic interactions",
}

suggestion = client.generate_suggestion(
    prompt=DISCONNECTED_TAXON_PROMPT,
    context=context,
    temperature=0.1
)

print(suggestion)
```

### Context Building

```python
from pathlib import Path
from communitymech.llm.context_builder import ContextBuilder

# Build rich context from community file
builder = ContextBuilder(Path("kb/communities/Test.yaml"))

context = builder.build_disconnected_taxon_context(
    taxon_name="ARMAN",
    taxon_id="NCBITaxon:123456"
)

# Use context with LLM
suggestion = client.generate_suggestion(
    prompt=DISCONNECTED_TAXON_PROMPT,
    context=context
)
```

### Cost Tracking

```python
# Generate multiple suggestions
for taxon in disconnected_taxa:
    suggestion = client.generate_suggestion(prompt, context)

# Get cost estimate
cost = client.get_cost_estimate()
print(f"Total cost: ${cost['total_cost_usd']:.4f}")
print(f"API calls: {cost['api_calls']}")
print(f"Total tokens: {cost['total_tokens']:,}")

# Reset tracking
client.reset_cost_tracking()
```

## Troubleshooting

### "API key not found"

**Problem**: Environment variable not set

**Solution**:
```bash
export ANTHROPIC_API_KEY=sk-ant-your-key
# Or add to .env file
```

### "anthropic package not installed"

**Problem**: Missing dependency

**Solution**:
```bash
uv sync --all-extras
# Or: pip install anthropic>=0.39.0
```

### "API call limit reached"

**Problem**: Hit max_api_calls_per_run limit

**Solution**: Increase limit in `conf/llm_config.yaml`:
```yaml
limits:
  max_api_calls_per_run: 200  # Increase as needed
```

### "Rate limit reached"

**Problem**: Too many requests per minute

**Solution**: The client automatically handles rate limiting. Wait or increase limit:
```yaml
limits:
  rate_limit_per_minute: 20  # Increase if needed
```

### "Failed to parse YAML"

**Problem**: LLM returned invalid YAML

**Solution**:
- Check prompt template formatting
- Try lower temperature (more deterministic)
- Use Opus model for better structured output
- Review and improve prompt if needed

### High Costs

**Problem**: API costs too high

**Solutions**:
1. Use Sonnet instead of Opus (5x cheaper)
2. Reduce max_tokens in config
3. Set max_cost_per_run limit
4. Use batch mode and review before applying
5. Enable context caching (reduces repeat costs)

## Security Best Practices

### 1. Never Commit API Keys

```bash
# Check .gitignore includes:
.env
*.env
.env.local
```

### 2. Use Environment Variables

```bash
# Good: Environment variable
export ANTHROPIC_API_KEY=sk-ant-...

# Bad: Hardcoded in code
api_key = "sk-ant-..."  # NEVER DO THIS
```

### 3. Rotate Keys Regularly

- Rotate API keys every 90 days
- Immediately rotate if compromised
- Use separate keys for dev/prod

### 4. Limit API Key Permissions

- Use least-privilege API keys
- Set spending limits in Anthropic console
- Monitor usage regularly

### 5. Secure Storage

- Store keys in password manager
- Use secrets management for CI/CD
- Never share keys via chat/email

## GitHub Actions / CI/CD

### Setup

Add API key as repository secret:

1. Go to repository Settings → Secrets → Actions
2. Click "New repository secret"
3. Name: `ANTHROPIC_API_KEY`
4. Value: `sk-ant-your-key`
5. Click "Add secret"

### Workflow Configuration

The workflow is already configured in `.github/workflows/network-quality.yml`:

```yaml
suggest-repairs:
  runs-on: ubuntu-latest
  steps:
    - name: Generate LLM repair suggestions
      env:
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      run: |
        uv run communitymech repair-network-batch --report-only
```

## Cost Estimates

### Typical Workflow

**Scenario**: Fix 10 disconnected taxa across 5 communities

With **Claude Sonnet 4.6**:
- Context: ~2,000 tokens/suggestion
- Prompt: ~1,000 tokens/suggestion
- Output: ~800 tokens/suggestion
- Total: ~3,800 tokens/suggestion
- Cost: ~$0.02/suggestion
- **Total: ~$0.20 for 10 suggestions**

With **Claude Opus 4.6**:
- Same token counts
- Cost: ~$0.08/suggestion
- **Total: ~$0.80 for 10 suggestions**

### Cost Optimization

1. **Use Sonnet**: 5x cheaper than Opus
2. **Batch processing**: Review offline, apply in bulk
3. **Context caching**: Reduces repeat costs by ~90%
4. **Selective repair**: Only fix critical issues
5. **Set limits**: Prevent runaway costs

## Support

- **Documentation**: [docs/NETWORK_QUALITY_GUIDE.md](NETWORK_QUALITY_GUIDE.md)
- **API Docs**: https://docs.anthropic.com/
- **Issues**: https://github.com/CultureBotAI/CommunityMech/issues

## Next Steps

- Review [NETWORK_QUALITY_GUIDE.md](NETWORK_QUALITY_GUIDE.md) for usage
- Check [LLM_REPAIR_ROADMAP.md](LLM_REPAIR_ROADMAP.md) for upcoming features
- Try generating suggestions with test communities
