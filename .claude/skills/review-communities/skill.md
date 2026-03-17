---
name: review-communities
description: Quality assurance and validation for ontology-mapped microbial communities using OAK, reference validation, and network integrity checks
version: 1.0.0
tags: [validation, quality-assurance, ontology, oak, ncbitaxon, envo, go, chebi, references, evidence]
author: CommunityMech Team
created: 2026-03-16
---

# Review Communities Skill

## Overview

The **Review Communities** skill provides comprehensive quality assurance and validation for ontology-mapped microbial communities in CommunityMech. It systematically verifies that:

1. **Taxonomy is correctly mapped** - NCBITaxon IDs exist, labels match, roles appropriate
2. **Evidence is properly cited** - PMID/DOI references valid, snippets match abstracts
3. **Ontology terms are valid** - ENVO (environment), GO (processes), CHEBI (metabolites)
4. **Network integrity maintained** - Interaction partners exist, directions valid
5. **Growth media linked** - CultureMech/MediaIngredientMech IDs valid
6. **Metadata is complete** - Required fields populated, enums valid

**Technology Stack:**
- **LinkML Schema**: Validate YAML structure and field constraints
- **OAK (Ontology Access Kit)**: Verify terms exist in NCBITaxon/ENVO/GO/CHEBI ontologies
- **Reference Validator**: Check PubMed/CrossRef citations and snippet matching
- **Network Auditor**: Verify ecological interaction integrity
- **Media Linker**: Validate CultureMech/MediaIngredientMech cross-references

**Current Dataset:** 78 communities
- 60 original curated communities
- 18 BioModels synthetic communities
- 100% validated against schema
- ~95% with validated ontology terms

---

## When to Use This Skill

| Scenario | Workflow | Priority |
|----------|----------|----------|
| **Post-curation QA** | Validate newly curated community before committing | High |
| **Batch validation** | Review all 78 communities | High |
| **Pre-export check** | Ensure KG export quality before KG-Microbe ingestion | Critical |
| **Periodic maintenance** | Monthly validation after ontology updates | Medium |
| **Evidence verification** | Cross-check snippets with PubMed abstracts | High |
| **Network validation** | Check interaction partner references | High |
| **Media linkage check** | Validate CultureMech/MediaIngredientMech IDs | Medium |

**Decision Table:**

```
IF newly curated community → Use interactive review
IF full dataset check → Use batch validation (just qc)
IF evidence issues → Use validate-references
IF network issues → Use audit-network
IF media linkage → Use link-media-dry
IF ontology terms → Use validate-terms
```

---

## Review Workflows

### 1. Schema Validation

**Use case:** Validate YAML structure against LinkML schema

```bash
# Validate single community
just validate kb/communities/Richmond_Mine_AMD_Biofilm.yaml

# Validate all communities
just validate-all
```

**Checks:**
- Required fields present
- Field types correct (strings, lists, enums)
- Enum values valid (e.g., ecological_state, community_category)
- Nested structure correct (taxonomy, interactions, evidence)

### 2. Ontology Term Validation

**Use case:** Verify all ontology terms exist and labels match

```bash
# Validate terms in single community
just validate-terms kb/communities/Richmond_Mine_AMD_Biofilm.yaml

# Validate terms in all communities
just validate-terms-all

# Validate schema-level term meanings
just validate-schema-terms
```

**Checks:**
- NCBITaxon IDs exist and labels match
- ENVO environment terms valid
- GO biological process terms valid
- CHEBI chemical/metabolite terms valid
- OAK adapters configured correctly

### 3. Evidence Reference Validation

**Use case:** Verify PMID/DOI citations and snippet accuracy

```bash
# Validate references in single community
just validate-references kb/communities/Richmond_Mine_AMD_Biofilm.yaml

# Validate references in all communities
just validate-references-all

# Repair references with suggested fixes (dry-run)
just repair-references kb/communities/Richmond_Mine_AMD_Biofilm.yaml
```

**Checks:**
- PMID/DOI references are valid and accessible
- Snippets fuzzy-match cited abstracts (≥70% similarity)
- Evidence items have all required fields
- Support level appropriate (SUPPORT, REFUTE, NEUTRAL)
- Evidence sources valid (EXPERIMENTAL, COMPUTATIONAL, REVIEW)

### 4. Network Integrity Audit

**Use case:** Validate ecological interaction network structure

```bash
# Audit network integrity for all communities
just audit-network

# Audit with JSON output
just audit-network-json

# Check network quality (CI mode - exits with error if issues)
just check-network-quality

# Audit and write report to file
just audit-network-report network_audit.txt
```

**Checks:**
- Interaction partners reference existing taxa
- Directionality is valid (e.g., predator → prey)
- No orphaned taxa (taxa without interactions in STABLE communities)
- No self-loops (taxon interacting with itself)
- Functional roles consistent with interactions

### 5. Growth Media Linkage Validation

**Use case:** Verify CultureMech and MediaIngredientMech cross-references

```bash
# Validate media linkages (dry-run)
just link-media-dry

# Generate media mapping reports
just link-media-report
```

**Checks:**
- CultureMech IDs exist in recipe index
- MediaIngredientMech IDs exist in ingredient index
- URLs properly formatted
- Composition ingredients have valid mappings
- Source attribution correct (CultureMech vs community_curated)

### 6. Full Quality Control

**Use case:** Run all validation checks in sequence

```bash
# Full QC: validate + lint + test
just qc
```

**Runs:**
1. `validate-all` - Schema validation
2. `validate-terms-all` - Ontology term validation
3. `validate-references-all` - Evidence reference validation
4. `lint` - Code quality checks
5. `test` - Unit tests

---

## Validation Rule Catalog

### Priority Levels

| Level | Description | Action Required | Count Target |
|-------|-------------|-----------------|--------------|
| **P1** | Critical errors blocking KG export | Fix immediately | 0 |
| **P2** | High-priority warnings needing review | Manual review | < 5% |
| **P3** | Medium-priority enrichment opportunities | Auto-correct when possible | < 20% |
| **P4** | Low-priority info/suggestions | Optional improvements | Any |

### Rule Definitions

#### P1 - Critical Errors

**Rule P1.1: Ontology Term Existence**
```yaml
id: P1.1
description: Ontology term does not exist (404 from OAK)
check: OAK lookup returns None for term ID
impact: Broken link in knowledge graph
fix: Re-map to correct term or update to current ID
tools: just validate-terms FILE
```

**Rule P1.2: Invalid CURIE Format**
```yaml
id: P1.2
description: Ontology ID not valid CURIE (e.g., "NCBITaxon:562" vs "562")
check: Regex ^[A-Z]+:\d+$ for ontology IDs
impact: Parser failures in downstream systems
fix: Correct to valid CURIE format
tools: Schema validation catches this
```

**Rule P1.3: Schema Validation Failure**
```yaml
id: P1.3
description: YAML does not validate against LinkML schema
check: linkml-validate returns errors
impact: Cannot load community into datamodel
fix: Correct YAML structure to match schema
tools: just validate FILE
```

**Rule P1.4: Evidence Reference Invalid**
```yaml
id: P1.4
description: PMID/DOI reference does not exist or is inaccessible
check: PubMed/CrossRef API returns 404
impact: Citation cannot be verified
fix: Correct reference ID or remove if invalid
tools: just validate-references FILE
```

**Rule P1.5: Network Integrity Violation**
```yaml
id: P1.5
description: Interaction references non-existent taxon
check: Partner taxon ID not in community taxonomy
impact: Orphaned network edges in KG
fix: Add missing taxon or correct partner reference
tools: just audit-network
```

#### P2 - High-Priority Warnings

**Rule P2.1: Ontology Label Mismatch**
```yaml
id: P2.1
description: Term label doesn't match ontology (e.g., "E. coli" vs "Escherichia coli")
check: Compare label to OAK-fetched preferred label
impact: Confusing discrepancies, potential wrong mapping
fix: Update label to match ontology or verify mapping
tools: just validate-terms FILE
```

**Rule P2.2: Snippet Fuzzy Match Low**
```yaml
id: P2.2
description: Evidence snippet similarity < 70% with abstract
check: Fuzzy match score below threshold
impact: Citation may not support claim
fix: Update snippet or verify correct reference
tools: just validate-references FILE
```

**Rule P2.3: Missing Required Metadata**
```yaml
id: P2.3
description: Optional but important fields missing (e.g., description, environment_term)
check: Field is None or empty string
impact: Reduced discoverability and context
fix: Populate from literature or domain knowledge
tools: Manual curation
```

**Rule P2.4: Functional Role Mismatch**
```yaml
id: P2.4
description: Taxon's functional role inconsistent with interactions
check: E.g., PRIMARY_PRODUCER with no cross-feeding interactions
impact: Metadata doesn't reflect actual ecology
fix: Correct role or add missing interactions
tools: just audit-network
```

#### P3 - Medium-Priority Enrichment

**Rule P3.1: Growth Media Not Linked**
```yaml
id: P3.1
description: Growth media lacks CultureMech/MediaIngredientMech IDs
check: culturemech_id or media_ingredient_mech_id missing
impact: Reduced linkage to external resources
fix: Run media linking script
tools: just link-media
```

**Rule P3.2: Limited Evidence**
```yaml
id: P3.2
description: Community has < 3 evidence items
check: Count evidence items across all fields
impact: Less robust support for claims
fix: Add citations from literature
tools: Manual curation + literature search
```

**Rule P3.3: Synonyms Missing**
```yaml
id: P3.3
description: Taxon has no synonyms (common names, strains)
check: taxon_term.synonyms empty or None
impact: Reduced search/discovery
fix: Add from NCBI Taxonomy or literature
tools: Manual enrichment
```

**Rule P3.4: Environmental Factors Sparse**
```yaml
id: P3.4
description: < 3 environmental factors for non-minimal communities
check: Count environmental_factors list
impact: Incomplete environmental context
fix: Add pH, temperature, salinity from literature
tools: Manual curation
```

#### P4 - Low-Priority Suggestions

**Rule P4.1: External Resources Missing**
```yaml
id: P4.1
description: No external_resources links (GenBank, NCBI BioProject, etc.)
check: external_resources empty
impact: Less connected to external databases
fix: Add dataset links opportunistically
tools: Manual enrichment
```

**Rule P4.2: Metabolic Pathways Not Detailed**
```yaml
id: P4.2
description: Interactions lack detailed metabolite exchange info
check: Metabolites field empty in interaction
impact: Less mechanistic detail
fix: Add CHEBI-mapped metabolites from literature
tools: Manual curation
```

**Rule P4.3: Temporal Dynamics Missing**
```yaml
id: P4.3
description: No temporal information for dynamic communities
check: No time-series or succession data
impact: Static view of potentially dynamic system
fix: Add temporal metadata if available
tools: Future enhancement
```

---

## Claude Code-Assisted Review

**Use case:** Interactive validation with Claude's assistance

```bash
# Use this skill
/review-communities

# Or invoke with specific community
/review-communities Richmond_Mine_AMD_Biofilm
```

**Claude will:**
1. Load community YAML file
2. Run all validation workflows:
   - Schema validation (`just validate`)
   - Term validation (`just validate-terms`)
   - Reference validation (`just validate-references`)
   - Network audit (`just audit-network`)
3. Explain issues in plain language
4. Propose corrections with rationale
5. Apply fixes if user approves
6. Commit changes with appropriate message

---

## Execution Protocol

When this skill is invoked, follow this protocol:

### Step 1: Identify Community

```python
# Parse user input
if args:
    community_identifier = args.strip()
else:
    # Show list of communities and ask user to choose
    communities = glob("kb/communities/*.yaml")
    show_communities_list(communities)
    community_identifier = ask_user_to_choose()

# Find community file
if community_identifier.endswith('.yaml'):
    community_file = Path(community_identifier)
elif '/' in community_identifier:
    community_file = Path(community_identifier)
else:
    # Assume it's a community name/stem
    community_file = Path(f"kb/communities/{community_identifier}.yaml")
    if not community_file.exists():
        # Try fuzzy match
        community_file = fuzzy_match_community(community_identifier)
```

### Step 2: Run Validation Suite

```bash
# Schema validation
just validate {community_file}

# Ontology terms
just validate-terms {community_file}

# Evidence references
just validate-references {community_file}

# Network integrity (full audit includes this community)
just audit-network
```

### Step 3: Parse and Categorize Issues

```python
issues = {
    'P1': [],  # Critical errors
    'P2': [],  # High-priority warnings
    'P3': [],  # Medium-priority enrichment
    'P4': []   # Low-priority suggestions
}

# Parse validation output
for line in validation_output:
    if '[ERROR]' in line or 'FAILED' in line:
        issues['P1'].append(parse_issue(line))
    elif '[WARNING]' in line:
        # Classify as P2 or P3 based on message
        if 'label mismatch' in line.lower() or 'snippet' in line.lower():
            issues['P2'].append(parse_issue(line))
        else:
            issues['P3'].append(parse_issue(line))
```

### Step 4: Report Issues to User

```markdown
## Validation Report: {community_name}

### Summary
- **P1 Critical**: {count_p1} issues
- **P2 High**: {count_p2} issues
- **P3 Medium**: {count_p3} issues
- **P4 Low**: {count_p4} issues

### P1 - Critical Errors (Fix Immediately)
{for issue in issues['P1']}
- **{issue.rule_id}**: {issue.description}
  - Location: {issue.location}
  - Current: {issue.current_value}
  - Fix: {issue.suggested_fix}
{endfor}

### P2 - High-Priority Warnings
{similar format}

### P3 - Medium-Priority Enrichment
{similar format}

### P4 - Low-Priority Suggestions
{similar format}
```

### Step 5: Propose Fixes

```markdown
## Suggested Corrections

I found {total_issues} issues. Here are the corrections I can apply:

### Auto-correctable (safe to apply automatically):
1. **Fix CURIE format** (P1.2)
   - Change `NCBITaxon562` → `NCBITaxon:562`
   - Locations: taxonomy[2].taxon_term.term.id

2. **Update ontology labels** (P2.1)
   - Change "E. coli" → "Escherichia coli"
   - Reason: Match NCBITaxon:562 preferred label

### Manual review required:
1. **Evidence snippet mismatch** (P2.2)
   - Snippet similarity: 62% (threshold: 70%)
   - Reference: PMID:12345678
   - Suggestion: Verify reference supports claim or update snippet

Would you like me to:
- [ ] Apply all auto-correctable fixes
- [ ] Apply specific fixes (specify which)
- [ ] Show detailed fix preview first
- [ ] Skip and generate report only
```

### Step 6: Apply Approved Fixes

```python
def apply_fixes(community_file, approved_fixes):
    # Load YAML
    with open(community_file) as f:
        data = yaml.safe_load(f)

    # Apply each fix
    for fix in approved_fixes:
        if fix.type == 'curie_format':
            apply_curie_fix(data, fix)
        elif fix.type == 'label_update':
            apply_label_fix(data, fix)
        elif fix.type == 'add_metadata':
            apply_metadata_fix(data, fix)

    # Write back with proper formatting
    with open(community_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False,
                  sort_keys=False, width=100, allow_unicode=True)

    # Validate again to ensure no regressions
    run_validation(community_file)
```

### Step 7: Document Changes

```python
# Add to curation history
curation_entry = {
    'date': datetime.now().isoformat(),
    'curator': 'Claude Opus 4.6',
    'action': 'validation_review',
    'changes_applied': [fix.summary() for fix in approved_fixes],
    'validation_status': 'PASSED' if no_p1_issues else 'NEEDS_REVIEW'
}

# Commit with detailed message
git_commit_message = f"""
Review and fix validation issues in {community_name}

Applied fixes:
{for fix in approved_fixes}
- {fix.rule_id}: {fix.summary}
{endfor}

Validation status: {P1: 0, P2: X, P3: Y, P4: Z}

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
"""
```

---

## Quality Metrics

### Completeness Score

```python
def calculate_completeness(community_data):
    """
    Calculate completeness score (0-100)

    Required fields (50 points):
    - id, name, description
    - taxonomy with roles
    - ecological_state, community_category

    Recommended fields (30 points):
    - environment_term
    - environmental_factors (≥3)
    - ecological_interactions (≥3)
    - external_resources (≥1)

    Enrichment fields (20 points):
    - growth_media with linkages
    - associated_datasets
    - metabolic_pathways
    - temporal_dynamics
    """
    score = 0

    # Required fields
    if all_required_fields_present(community_data):
        score += 50

    # Recommended fields
    if community_data.get('environment_term'):
        score += 5
    if len(community_data.get('environmental_factors', [])) >= 3:
        score += 10
    if len(community_data.get('ecological_interactions', [])) >= 3:
        score += 10
    if community_data.get('external_resources'):
        score += 5

    # Enrichment
    if community_data.get('growth_media'):
        score += 10
    if community_data.get('associated_datasets'):
        score += 5
    if any('metabolites' in i for i in community_data.get('ecological_interactions', [])):
        score += 5

    return min(100, score)
```

### Validation Quality Score

```python
def calculate_validation_score(validation_summary):
    """
    Calculate validation quality score (0-100)

    Weights:
      - P1 errors: -50 points each (blocking)
      - P2 warnings: -10 points each
      - P3 warnings: -2 points each
      - Evidence coverage: +20 points
      - Network completeness: +15 points
    """
    base_score = 100

    base_score -= validation_summary['P1'] * 50
    base_score -= validation_summary['P2'] * 10
    base_score -= validation_summary['P3'] * 2

    # Evidence coverage bonus
    avg_evidence_per_interaction = validation_summary.get('avg_evidence', 0)
    base_score += min(avg_evidence_per_interaction / 2, 1.0) * 20

    # Network completeness bonus
    if validation_summary.get('network_integrity') == 'COMPLETE':
        base_score += 15

    return max(0, min(100, base_score))
```

---

## Validation Reports

### Text Report Format

```markdown
# CommunityMech Validation Report
**Generated:** 2026-03-16 14:23:45
**Communities Validated:** 78

## Summary

| Metric | Value |
|--------|-------|
| Total Communities | 78 |
| Passed All Checks | 72 (92.3%) |
| P1 Critical Errors | 0 |
| P2 High Warnings | 12 |
| P3 Medium Warnings | 45 |
| P4 Low Suggestions | 89 |
| Avg Completeness Score | 87.3 |
| Avg Validation Score | 92.1 |

## P1 Critical Errors (0)

✅ No critical errors found!

## P2 High-Priority Warnings (12)

### Ontology Label Mismatches (8)
- `Richmond_Mine_AMD_Biofilm.yaml`: "Leptospirillum ferriphilum" → "Leptospirillum ferrooxidans" (NCBITaxon:178)
- `Geobacter_Methanosarcina_DIET.yaml`: "Methanosarcina barkeri" label mismatch
- ...

### Evidence Snippet Mismatches (4)
- `Dangl_SynComm_35.yaml`: interaction[2].evidence[0] snippet similarity 65%
- ...

## P3 Medium-Priority Enrichment (45)

### Growth Media Not Linked (21)
- Communities missing CultureMech linkages
- Run: `just link-media` to auto-link

### Limited Evidence (15)
- Communities with < 3 evidence items
- Recommend adding citations

...

## Recommendations

1. **Immediate**: Fix 0 P1 errors (none found!)
2. **This Week**: Review 12 P2 warnings, prioritize label mismatches
3. **This Month**: Auto-enrich 21 communities with media linkages
4. **Ongoing**: Add evidence to 15 under-cited communities
```

### JSON Report Format

```json
{
  "metadata": {
    "generated_at": "2026-03-16T14:23:45Z",
    "generator": "CommunityMech Review Skill v1.0.0",
    "communities_validated": 78
  },
  "summary": {
    "total_communities": 78,
    "passed_all_checks": 72,
    "P1_critical": 0,
    "P2_high": 12,
    "P3_medium": 45,
    "P4_low": 89,
    "avg_completeness_score": 87.3,
    "avg_validation_score": 92.1
  },
  "issues_by_priority": {
    "P1": [],
    "P2": [
      {
        "rule_id": "P2.1",
        "community": "Richmond_Mine_AMD_Biofilm",
        "description": "Ontology label mismatch",
        "location": "taxonomy[1].taxon_term.term.label",
        "current": "Leptospirillum ferriphilum",
        "expected": "Leptospirillum ferrooxidans",
        "ontology_id": "NCBITaxon:178",
        "suggested_fix": "Update label to match NCBITaxon preferred term",
        "auto_correctable": true
      }
    ],
    "P3": [...],
    "P4": [...]
  },
  "communities": [
    {
      "id": "CommunityMech:000001",
      "file": "Richmond_Mine_AMD_Biofilm.yaml",
      "name": "Richmond Mine Acid Mine Drainage Biofilm",
      "completeness_score": 95,
      "validation_score": 88,
      "issues": {
        "P1": 0,
        "P2": 1,
        "P3": 2,
        "P4": 5
      }
    }
  ]
}
```

---

## Integration with Justfile

The skill integrates with existing `just` commands:

```makefile
# Quality control (includes validation)
qc: validate-all validate-terms-all validate-references-all lint test

# Validation commands
validate FILE           # Schema validation
validate-all           # All communities
validate-terms FILE    # Ontology terms
validate-terms-all     # All communities
validate-references FILE  # Evidence citations
validate-references-all   # All communities

# Network integrity
audit-network          # Interaction network audit
check-network-quality  # CI mode (exits on error)

# Growth media
link-media-dry         # Dry-run linkage
link-media             # Apply linkage
link-media-report      # Generate reports
```

---

## Advanced Features

### 1. Automated Evidence Repair

**Idea:** Use LLM to suggest evidence snippet corrections

```python
from anthropic import Anthropic

def suggest_evidence_fix(reference_id, current_snippet, abstract):
    """Use Claude to suggest corrected snippet from abstract."""
    client = Anthropic()

    prompt = f"""
    Extract a snippet from this abstract that supports the claim implied by the current snippet.

    Current snippet: {current_snippet}

    Abstract: {abstract}

    Return ONLY the corrected snippet (no explanation).
    """

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text.strip()
```

### 2. Cross-Community Consistency Checks

**Idea:** Detect conflicting information across communities

```python
def check_cross_community_consistency():
    """Find taxa mapped to different environments across communities."""
    taxon_environments = defaultdict(set)

    for community in load_all_communities():
        for taxon in community.taxonomy:
            taxon_id = taxon.taxon_term.term.id
            env = community.environment_term.term.id if community.environment_term else None
            if env:
                taxon_environments[taxon_id].add(env)

    # Report taxa in >3 different environments
    for taxon_id, envs in taxon_environments.items():
        if len(envs) > 3:
            print(f"⚠️  {taxon_id} found in {len(envs)} environments: {envs}")
```

### 3. Interaction Type Inference

**Idea:** Suggest interaction types based on functional roles

```python
def infer_interaction_type(taxon_a_role, taxon_b_role):
    """Suggest interaction types based on functional roles."""
    inference_rules = {
        ('PRIMARY_PRODUCER', 'CROSS_FEEDER'): 'COMMENSALISM',
        ('PREDATOR', 'PREY'): 'PREDATION',
        ('SYNTROPHIC_PARTNER', 'SYNTROPHIC_PARTNER'): 'SYNTROPHY',
        ('N_FIXER', 'HOST'): 'MUTUALISM',
    }

    return inference_rules.get((taxon_a_role, taxon_b_role), 'UNKNOWN')
```

### 4. Literature Mining for Evidence

**Idea:** Automatically find supporting citations for interactions

```python
from Bio import Entrez

def find_supporting_literature(taxa_pair, interaction_type):
    """Search PubMed for papers about interaction."""
    taxon_a, taxon_b = taxa_pair
    query = f'("{taxon_a.label}" AND "{taxon_b.label}" AND "{interaction_type}")'

    Entrez.email = "your@email.com"
    handle = Entrez.esearch(db="pubmed", term=query, retmax=5)
    record = Entrez.read(handle)

    return [f"PMID:{pmid}" for pmid in record["IdList"]]
```

---

## Conclusion

The **Review Communities** skill provides comprehensive quality assurance for CommunityMech's ontology-mapped microbial communities. By integrating LinkML validation, OAK, reference validation, and network integrity checks, it ensures:

- **Zero critical errors** (P1) before KG export
- **High-quality ontology mappings** with validated labels and terms
- **Evidence-backed claims** with verified citations and snippets
- **Network integrity** with valid interaction references
- **External linkages** to CultureMech and MediaIngredientMech
- **Audit trail** via validation reports and git history

**Next Steps:**
1. Use `/review-communities` to validate specific communities
2. Run `just qc` for full dataset validation
3. Fix any P1 critical errors immediately
4. Review P2 warnings for manual correction
5. Auto-enrich P3 issues (media linkages, etc.)
6. Integrate into ongoing curation workflow

**Estimated Impact:**
- **Time saved**: 70% reduction in manual QA (automated validation)
- **Error prevention**: 100% P1 error detection before export
- **Data enrichment**: 90%+ communities with validated terms
- **Citation quality**: 95%+ evidence items with verified snippets
