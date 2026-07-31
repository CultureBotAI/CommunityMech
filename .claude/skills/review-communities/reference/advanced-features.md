# Advanced Features

*Reference for the **review-communities** skill — see [`../SKILL.md`](../SKILL.md) for the overview, workflows, and rule summary.*

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

