# Claude Code-Assisted Review & Execution Protocol

*Reference for the **review-communities** skill — see [`../SKILL.md`](../SKILL.md) for the overview, workflows, and rule summary.*

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

