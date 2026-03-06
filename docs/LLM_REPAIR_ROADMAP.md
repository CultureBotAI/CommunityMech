# LLM-Assisted Network Repair Roadmap

## Overview

This document outlines the implementation roadmap for LLM-assisted network quality checking and repair infrastructure. Phase 1 (Foundation) is complete. This roadmap details Phases 2-5.

**Status**: Phase 1 ✅ Complete | Phases 2-5 📋 Planned

---

## Phase 1: Foundation ✅ COMPLETE

**Timeline**: Week 1 (Completed March 5, 2026)

### Deliverables
- [x] Module structure (`network/`, `llm/`)
- [x] Refactored auditor with CLI modes
- [x] Basic CLI with commands
- [x] Unit tests (9/9 passing)
- [x] CI/CD workflow
- [x] Configuration files
- [x] Documentation

### Files Created
- `src/communitymech/network/auditor.py`
- `src/communitymech/llm/client.py` (abstract base)
- `src/communitymech/llm/prompts.py` (templates)
- `src/communitymech/cli.py`
- `conf/llm_config.yaml`
- `.github/workflows/network-quality.yml`
- `tests/test_network_auditor.py`

**See**: [PHASE_1_COMPLETION.md](../PHASE_1_COMPLETION.md)

---

## Phase 2: LLM Integration 📋 PLANNED

**Timeline**: Week 2 (Estimated 5-7 days)

### Goals
- Integrate Anthropic Claude API
- Build context builder for rich prompts
- Implement suggestion generation
- Add comprehensive testing with mocks

### Tasks

#### 2.1 Anthropic Client Implementation
**File**: `src/communitymech/llm/anthropic_client.py`

```python
class AnthropicClient(LLMClient):
    """Claude API integration with caching and rate limiting."""

    def __init__(self, config: dict):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.cache = {}
        self.rate_limiter = RateLimiter(...)

    def generate_suggestion(self, prompt, context, temperature=0.1):
        # Use context caching for efficiency
        # Parse structured YAML output
        # Validate response format
        # Handle API errors gracefully
```

**Dependencies**:
- `anthropic>=0.39.0` ✅ (already in pyproject.toml)
- API key via `ANTHROPIC_API_KEY` environment variable

**Testing**:
- Mock API responses
- Test error handling
- Test rate limiting
- Test cost tracking

#### 2.2 Context Builder
**File**: `src/communitymech/llm/context_builder.py`

```python
class ContextBuilder:
    """Build rich context for LLM prompts from community data."""

    def build_disconnected_taxon_context(self, community_data, disconnected_taxon):
        """Extract relevant context for disconnected taxon repair."""
        return {
            "community_name": ...,
            "environment": ...,
            "environmental_context": ...,  # pH, temp, etc.
            "taxon_name": ...,
            "taxon_id": ...,
            "taxon_context": ...,  # functional roles, abundance
            "connected_taxa": ...,  # list with IDs
            "interaction_summary": ...,  # types, metabolites, patterns
        }
```

**Features**:
- Extract environmental factors
- Build taxonomy summary
- Summarize existing interactions
- Identify metabolic capabilities
- Format for prompt injection

#### 2.3 Integration Tests
**File**: `tests/test_llm_client.py`

- Test with mocked API responses
- Test YAML parsing from LLM output
- Test error handling (API failures, rate limits)
- Test context building
- Test prompt formatting

#### 2.4 Environment Setup
- Document API key setup process
- Add `.env.example` template
- Update documentation with API costs
- Add API key validation

### Deliverables
- [x] Working Anthropic client
- [x] Context builder with rich prompt data
- [x] Integration tests with mocks
- [x] API key handling
- [x] Cost estimation

### Acceptance Criteria
```bash
# Can generate suggestions with mocked API
uv run pytest tests/test_llm_client.py -v

# Can validate API key
export ANTHROPIC_API_KEY=sk-ant-...
uv run python -c "from communitymech.llm.anthropic_client import AnthropicClient; \
                   client = AnthropicClient(); \
                   print('✅ API key valid' if client.validate_api_key() else '❌ Invalid')"
```

---

## Phase 3: Repair Strategies 📋 PLANNED

**Timeline**: Week 3 (Estimated 7-10 days)

### Goals
- Implement repair strategy pattern
- Add multi-layer validation
- Enable evidence snippet validation
- Handle different issue types

### Tasks

#### 3.1 Strategy Pattern
**File**: `src/communitymech/network/repair_strategies.py`

```python
class RepairStrategy(ABC):
    """Abstract base for repair strategies."""

    @abstractmethod
    def build_context(self, issue, community_data) -> dict:
        """Build LLM context for this issue type."""

    @abstractmethod
    def get_prompt_template(self) -> str:
        """Get prompt template for this issue type."""

    @abstractmethod
    def validate_suggestion(self, suggestion, community_data) -> tuple[bool, list[str]]:
        """Validate LLM suggestion."""


class DisconnectedTaxonStrategy(RepairStrategy):
    """Strategy for connecting disconnected taxa."""

    def build_context(self, issue, community_data):
        builder = ContextBuilder()
        return builder.build_disconnected_taxon_context(
            community_data, issue["taxon"]
        )

    def get_prompt_template(self):
        return DISCONNECTED_TAXON_PROMPT

    def validate_suggestion(self, suggestion, community_data):
        # Multi-layer validation
        errors = []
        errors.extend(self._validate_schema(suggestion))
        errors.extend(self._validate_ontology_terms(suggestion))
        errors.extend(self._validate_evidence(suggestion))
        errors.extend(self._validate_biological_plausibility(suggestion))
        return len(errors) == 0, errors
```

**Strategies to Implement**:
1. `DisconnectedTaxonStrategy` - Most common issue type
2. `MissingSourceStrategy` - Identify missing source from context
3. `UnknownTargetStrategy` - Resolve unknown target references

#### 3.2 Multi-Layer Validation
**File**: `src/communitymech/network/validators.py`

```python
class SuggestionValidator:
    """Multi-layer validation for LLM suggestions."""

    def validate_schema(self, suggestion: dict) -> list[str]:
        """Layer 1: LinkML schema validation."""
        # Use linkml-validate

    def validate_ontology_terms(self, suggestion: dict) -> list[str]:
        """Layer 2: Ontology term validation via OAK."""
        # Validate NCBITaxon, CHEBI, GO IDs

    def validate_evidence(self, suggestion: dict) -> list[str]:
        """Layer 3: Evidence snippet validation."""
        # Fetch abstracts, fuzzy match snippets (95%+)

    def validate_biological_plausibility(
        self, suggestion: dict, community_data: dict
    ) -> list[str]:
        """Layer 4: Biological plausibility checks."""
        # Check metabolic compatibility
        # Verify environmental constraints
        # Check interaction type makes sense
```

**Validation Layers**:
1. **Schema**: YAML structure matches LinkML schema
2. **Ontology**: All NCBITaxon, CHEBI, GO IDs exist
3. **Evidence**: Snippets match abstracts (95%+ similarity)
4. **Plausibility**: Metabolically and ecologically sound

#### 3.3 Evidence Validation
**Integration**: Use existing `literature.py` patterns

```python
from communitymech.literature import LiteratureFetcher

fetcher = LiteratureFetcher(cache_dir="references_cache")
abstract, _ = fetcher.fetch_paper(reference)
is_valid = fetcher.validate_evidence_snippet(snippet, abstract)
```

#### 3.4 End-to-End Repair Flow
**File**: `src/communitymech/network/llm_repair.py`

```python
class LLMNetworkRepairer:
    """Main orchestrator for LLM-assisted network repair."""

    def repair_community(self, yaml_path: Path, dry_run: bool = True):
        # 1. Audit to find issues
        issues = self.auditor.audit_community(yaml_path)

        # 2. For each issue, select strategy
        for issue in issues:
            strategy = self._select_strategy(issue["type"])

            # 3. Build context
            context = strategy.build_context(issue, community_data)

            # 4. Generate suggestion with LLM
            suggestion = self.llm_client.generate_suggestion(
                prompt=strategy.get_prompt_template(),
                context=context
            )

            # 5. Validate suggestion
            is_valid, errors = strategy.validate_suggestion(suggestion, community_data)

            # 6. Present to user for approval
            if dry_run:
                self._display_suggestion(suggestion, is_valid, errors)
            else:
                if self._get_user_approval(suggestion):
                    self._apply_suggestion(yaml_path, suggestion)
```

### Deliverables
- [x] Strategy pattern implementation
- [x] Multi-layer validators
- [x] Evidence snippet validation
- [x] End-to-end repair flow
- [x] Tests for all strategies

### Acceptance Criteria
```bash
# Can generate and validate suggestions
uv run pytest tests/test_repair_strategies.py -v
uv run pytest tests/test_validators.py -v

# End-to-end test with real API
export ANTHROPIC_API_KEY=sk-ant-...
uv run pytest tests/test_llm_repair_e2e.py -v
```

---

## Phase 4: User Interface 📋 PLANNED

**Timeline**: Week 4 (Estimated 5-7 days)

### Goals
- Build beautiful interactive CLI with `rich`
- Implement batch report mode
- Add backup/restore functionality
- Polish user experience

### Tasks

#### 4.1 Interactive CLI with Rich
**Enhancement**: `src/communitymech/cli.py`

```python
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.table import Table
from rich.syntax import Syntax

@cli.command()
def repair_network(file: Path, auto_approve: bool, dry_run: bool):
    console = Console()

    # Show progress
    with console.status("[bold green]Auditing network..."):
        issues = auditor.audit_community(file)

    # Display issues
    table = Table(title="Network Integrity Issues")
    table.add_column("Type", style="cyan")
    table.add_column("Details", style="magenta")
    for issue in issues:
        table.add_row(issue["type"], issue["message"])
    console.print(table)

    # For each issue
    for i, issue in enumerate(issues):
        console.print(f"\n[bold]Issue {i+1}/{len(issues)}[/bold]")

        # Generate suggestion
        with console.status("[bold yellow]Generating LLM suggestion..."):
            suggestion = repairer.generate_suggestion(issue)

        # Display suggestion with syntax highlighting
        yaml_code = yaml.dump(suggestion)
        syntax = Syntax(yaml_code, "yaml", theme="monokai")
        console.print(Panel(syntax, title="Suggested Fix"))

        # Validation status
        is_valid, errors = validator.validate(suggestion)
        if is_valid:
            console.print("✅ Validation: [green]PASSED[/green]")
        else:
            console.print("❌ Validation: [red]FAILED[/red]")
            for error in errors:
                console.print(f"  • {error}")

        # User approval
        if not dry_run and is_valid:
            if auto_approve or Confirm.ask("Apply this fix?"):
                repairer.apply_suggestion(file, suggestion)
                console.print("[green]✓ Applied[/green]")
```

#### 4.2 Batch Report Mode
**File**: `src/communitymech/network/batch_reporter.py`

```python
class BatchReporter:
    """Generate repair suggestions report for offline review."""

    def generate_report(self, output_path: Path = Path("reports/repair_suggestions.yaml")):
        """Generate YAML report with all suggestions."""

        report = {
            "generated_at": datetime.now().isoformat(),
            "communities": []
        }

        for yaml_file in self.communities_dir.glob("*.yaml"):
            issues = self.auditor.audit_community(yaml_file)
            if not issues:
                continue

            suggestions = []
            for issue in issues:
                suggestion = self.repairer.generate_suggestion(issue)
                is_valid, errors = self.validator.validate(suggestion)

                suggestions.append({
                    "issue": issue,
                    "suggestion": suggestion,
                    "validation": {
                        "passed": is_valid,
                        "errors": errors
                    },
                    "approved": False  # User will edit this
                })

            report["communities"].append({
                "file": str(yaml_file),
                "issues_count": len(issues),
                "suggestions": suggestions
            })

        with open(output_path, "w") as f:
            yaml.dump(report, f, sort_keys=False)
```

**Workflow**:
1. Generate report: `just suggest-network-repairs`
2. Human reviews and edits `reports/repair_suggestions.yaml`
3. Sets `approved: true` for suggestions to apply
4. Applies approved: `just repair-network-batch --apply-from reports/repair_suggestions.yaml`

#### 4.3 Backup and Restore
**File**: `src/communitymech/network/backup.py`

```python
class BackupManager:
    """Manage backups before applying repairs."""

    def create_backup(self, yaml_path: Path) -> Path:
        """Create timestamped backup."""
        backup_dir = Path(".backups")
        backup_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"{yaml_path.stem}_{timestamp}.yaml"

        shutil.copy(yaml_path, backup_path)
        return backup_path

    def restore_backup(self, backup_path: Path, target_path: Path):
        """Restore from backup."""
        shutil.copy(backup_path, target_path)

    def list_backups(self, yaml_path: Path) -> list[Path]:
        """List available backups for a file."""
        backup_dir = Path(".backups")
        pattern = f"{yaml_path.stem}_*.yaml"
        return sorted(backup_dir.glob(pattern), reverse=True)
```

### Deliverables
- [x] Beautiful interactive CLI with rich
- [x] Batch report generation
- [x] Backup/restore functionality
- [x] Progress indicators and syntax highlighting
- [x] User-friendly prompts

### Acceptance Criteria
```bash
# Interactive mode works
communitymech repair-network kb/communities/Test.yaml

# Batch mode generates report
communitymech repair-network-batch --report-only

# Backup created before apply
ls .backups/Test_20260305_*.yaml
```

---

## Phase 5: Integration & Polish 📋 PLANNED

**Timeline**: Week 5 (Estimated 5-7 days)

### Goals
- End-to-end testing with real communities
- Performance optimization
- Documentation and examples
- CI/CD integration for LLM suggestions

### Tasks

#### 5.1 End-to-End Testing
- Test with real community files
- Validate suggestions against schema
- Verify evidence snippets
- Test all issue types

#### 5.2 Performance Optimization
- Implement parallel suggestion generation
- Optimize context caching
- Add request batching
- Minimize API calls

#### 5.3 Cost Tracking
**File**: `src/communitymech/llm/cost_tracker.py`

```python
class CostTracker:
    """Track API usage and estimated costs."""

    PRICING = {
        "claude-opus-4-6": {"input": 15.0, "output": 75.0},  # per 1M tokens
        "claude-sonnet-4-6": {"input": 3.0, "output": 15.0},
    }

    def estimate_cost(self, model: str, input_tokens: int, output_tokens: int) -> float:
        """Calculate estimated cost in USD."""

    def log_request(self, model: str, input_tokens: int, output_tokens: int):
        """Log API request for cost tracking."""

    def get_total_cost(self) -> float:
        """Get total estimated cost for session."""
```

#### 5.4 Documentation
- Complete user guide
- Add examples for each issue type
- Document API costs and limits
- Create troubleshooting guide

#### 5.5 CI/CD Enhancement
**Update**: `.github/workflows/network-quality.yml`

Uncomment LLM repair suggestions job:
```yaml
suggest-repairs:
  runs-on: ubuntu-latest
  needs: audit-network
  if: failure()

  steps:
    - name: Generate LLM repair suggestions
      env:
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      run: |
        uv run communitymech repair-network-batch --report-only

    - name: Upload suggestions
      uses: actions/upload-artifact@v4
      with:
        name: network-repair-suggestions
        path: reports/repair_suggestions.yaml
```

### Deliverables
- [x] E2E tests with real communities
- [x] Performance optimizations
- [x] Cost tracking
- [x] Complete documentation
- [x] Enhanced CI/CD with LLM suggestions

### Acceptance Criteria
```bash
# Full E2E workflow
just audit-network
# (artificially introduce issue)
communitymech repair-network kb/communities/Test.yaml
# (approve suggestion)
just audit-network  # Should show 0 issues

# CI/CD generates suggestions on failure
# (push PR with network issue)
# → GitHub Actions uploads repair suggestions as artifact

# Cost tracking works
export ANTHROPIC_API_KEY=sk-ant-...
communitymech repair-network-batch --report-only
# → Displays: "Estimated cost: $2.45 (45 API calls)"
```

---

## Timeline Summary

| Phase | Duration | Status | Deliverable |
|-------|----------|--------|-------------|
| Phase 1: Foundation | Week 1 | ✅ Complete | Repeatable audit with CI |
| Phase 2: LLM Integration | Week 2 | 📋 Planned | Working LLM client |
| Phase 3: Repair Strategies | Week 3 | 📋 Planned | Validated repair flow |
| Phase 4: User Interface | Week 4 | 📋 Planned | Interactive + batch modes |
| Phase 5: Integration & Polish | Week 5 | 📋 Planned | Production-ready system |

**Total Timeline**: 5 weeks from foundation to production

---

## Cost Estimates

### Anthropic Claude Pricing
- **Opus 4.6**: $15/1M input tokens, $75/1M output tokens
- **Sonnet 4.6**: $3/1M input tokens, $15/1M output tokens (recommended)

### Per-Community Repair
- Context: ~2,000 tokens
- Prompt: ~1,000 tokens
- Output: ~800 tokens
- **Cost per suggestion**: ~$0.08 (Opus) or ~$0.02 (Sonnet)

### For 60 Communities (avg 3 issues each)
- Total suggestions: 180
- **Estimated cost**:
  - Opus: ~$14 (without caching), ~$5-7 (with caching)
  - Sonnet: ~$4 (without caching), ~$2-3 (with caching)

**Recommendation**: Use Sonnet 4.6 for cost efficiency, Opus 4.6 for highest quality

---

## Success Criteria (Overall)

- [x] **Phase 1**: Repeatable audit command with CI
- [ ] **Phase 2**: LLM generates valid YAML suggestions
- [ ] **Phase 3**: Multi-layer validation catches errors
- [ ] **Phase 4**: Interactive CLI enables human-in-loop
- [ ] **Phase 5**: System deployed to production with CI/CD

**Key Innovation**: Combines LLM reasoning power with ontology-grounded, evidence-based curation to scale knowledge base maintenance.

---

## Next Steps

### To Start Phase 2:
1. Set up Anthropic API key: `export ANTHROPIC_API_KEY=sk-ant-...`
2. Implement `anthropic_client.py`
3. Implement `context_builder.py`
4. Write integration tests with mocks
5. Test with real API

### Prerequisites:
- ✅ Phase 1 complete
- Anthropic API key (get from https://console.anthropic.com/)
- Review prompt templates in `llm/prompts.py`
- Decide on model (Sonnet vs Opus)

**Ready to proceed with Phase 2!**
