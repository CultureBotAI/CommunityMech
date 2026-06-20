# Minting IDs, Adding Records & Batch Assignment (all collection types)

*Reference for the **manage-identifiers** skill — see [`../skill.md`](../skill.md) for the CommunityMech overview and core workflow.*

---

## Minting New IDs

Once you know the highest ID, minting a new ID is straightforward.

### Basic ID Generation

**Python function**:
```python
def generate_xmech_id(prefix: str, number: int) -> str:
    """Generate formatted X-Mech ID.

    Args:
        prefix: Repository name (e.g., "MediaIngredientMech")
        number: Sequential number (1-999999)

    Returns:
        Formatted ID (e.g., "MediaIngredientMech:000001")

    Examples:
        >>> generate_xmech_id("MediaIngredientMech", 1)
        'MediaIngredientMech:000001'

        >>> generate_xmech_id("CultureMech", 15431)
        'CultureMech:015431'
    """
    return f"{prefix}:{number:06d}"

# Usage
new_id = generate_xmech_id("MediaIngredientMech", 113)
print(new_id)  # Output: MediaIngredientMech:000113
```

### Complete Minting Workflow

**Generic mint function**:
```python
from pathlib import Path

def mint_next_id(
    source: Path,
    prefix: str,
    collection_type: str = "single_file",
    collection_key: str = "ingredients"
) -> str:
    """Mint next available ID for a collection.

    Args:
        source: Path to YAML file or directory
        prefix: ID prefix (repo name)
        collection_type: "single_file" or "multi_file"
        collection_key: Collection key name (for single_file type)

    Returns:
        Next available ID string

    Examples:
        >>> # Single-file collection
        >>> mint_next_id(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech',
        ...     'single_file',
        ...     'ingredients'
        ... )
        'MediaIngredientMech:000113'

        >>> # Multi-file collection
        >>> mint_next_id(
        ...     Path('kb/communities'),
        ...     'CommunityMech',
        ...     'multi_file'
        ... )
        'CommunityMech:000079'
    """
    if collection_type == "single_file":
        highest = find_highest_id_single_file(source, prefix, collection_key)
    elif collection_type == "multi_file":
        highest = find_highest_id_multi_file(source, prefix)
    else:
        raise ValueError(f"Unknown collection_type: {collection_type}")

    next_number = highest + 1
    return generate_xmech_id(prefix, next_number)
```

### Quick Mint Examples

**MediaIngredientMech** (single-file):
```python
from pathlib import Path

yaml_path = Path('data/curated/unmapped_ingredients.yaml')
highest = find_highest_id_single_file(yaml_path, 'MediaIngredientMech')
next_id = generate_xmech_id('MediaIngredientMech', highest + 1)
print(f"Next ID: {next_id}")  # MediaIngredientMech:000113
```

**CommunityMech** (multi-file):
```python
from pathlib import Path

communities_dir = Path('kb/communities')
highest = find_highest_id_multi_file(communities_dir, 'CommunityMech')
next_id = generate_xmech_id('CommunityMech', highest + 1)
print(f"Next ID: {next_id}")  # CommunityMech:000079
```

**CultureMech** (multi-file + registry):
```python
from pathlib import Path

registry_path = Path('data/culturemech_id_registry.tsv')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)
print(f"Next ID: {next_id}")  # CultureMech:015432
```

## Adding New Records

### Workflow 1: Single-File Collection (MediaIngredientMech)

**Step-by-step process**:

```python
import yaml
from pathlib import Path
from datetime import datetime, timezone

# Step 1: Load existing data
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
with open(yaml_path) as f:
    data = yaml.safe_load(f)

# Step 2: Find next ID
highest = find_highest_id_single_file(yaml_path, 'MediaIngredientMech', 'ingredients')
next_id = generate_xmech_id('MediaIngredientMech', highest + 1)

# Step 3: Create new record
new_record = {
    'id': next_id,  # ALWAYS first field
    'identifier': f'UNMAPPED_{(highest + 1):04d}',
    'preferred_term': 'New Ingredient Name',
    'synonyms': [],
    'mapping_status': 'UNMAPPED',
    'occurrence_statistics': {
        'total_occurrences': 1,
        'media_count': 1
    },
    'curation_history': [
        {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'curator': 'manual_addition',
            'action': 'CREATED',
            'changes': 'New ingredient added manually',
            'new_status': 'UNMAPPED',
            'llm_assisted': False
        }
    ],
    'notes': 'Added manually via identifier management workflow'
}

# Step 4: Append to collection
data['ingredients'].append(new_record)

# Step 5: Update metadata
data['total_count'] = len(data['ingredients'])
data['generation_date'] = datetime.now(timezone.utc).isoformat()

# Step 6: Save (preserves order with sort_keys=False)
with open(yaml_path, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

print(f"✓ Added {next_id}: {new_record['preferred_term']}")
```

**Key points**:
- ✓ `id` field ALWAYS comes first
- ✓ Update `total_count` metadata
- ✓ Update `generation_date` metadata
- ✓ Use `sort_keys=False` to preserve field order
- ✓ Include curation history for audit trail

### Workflow 2: Multi-File Collection (CommunityMech)

**Step-by-step process**:

```python
import yaml
from pathlib import Path
from datetime import datetime, timezone

# Step 1: Find next ID
communities_dir = Path('kb/communities')
highest = find_highest_id_multi_file(communities_dir, 'CommunityMech')
next_id = generate_xmech_id('CommunityMech', highest + 1)

# Step 2: Create new record
new_community = {
    'id': next_id,  # ALWAYS first field
    'name': 'New Community Name',
    'description': 'Description of the microbial community',
    'environment': 'Environmental context',
    'members': [],
    'metadata': {
        'created_date': datetime.now(timezone.utc).isoformat(),
        'curator': 'manual_addition'
    }
}

# Step 3: Generate filename (sanitize name for filesystem)
safe_name = new_community['name'].replace(' ', '_').replace('/', '_')
output_path = communities_dir / f"{safe_name}.yaml"

# Step 4: Save to new file
with open(output_path, 'w') as f:
    yaml.dump(
        new_community,
        f,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        width=100
    )

print(f"✓ Created {next_id} → {output_path.name}")
```

**Key points**:
- ✓ Create separate file for each record
- ✓ Use sanitized filename (no special chars)
- ✓ `id` field ALWAYS first
- ✓ No metadata update needed (each file is independent)

### Workflow 3: Multi-File + Registry (CultureMech)

**Step-by-step process**:

```python
import yaml
import pandas as pd
from pathlib import Path
from datetime import datetime, timezone

# Step 1: Find next ID from registry
registry_path = Path('data/culturemech_id_registry.tsv')
registry = pd.read_csv(registry_path, sep='\t')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)

# Step 2: Create new record
new_medium = {
    'id': next_id,  # ALWAYS first field
    'name': 'New Medium Name',
    'category': 'bacterial',  # bacterial, algae, fungi, etc.
    'description': 'Medium description',
    'ingredients': [],
    'metadata': {
        'created_date': datetime.now(timezone.utc).isoformat(),
        'curator': 'manual_addition'
    }
}

# Step 3: Determine output path (based on category)
category = new_medium['category']
safe_name = new_medium['name'].replace(' ', '_').replace('/', '_')
output_path = Path(f'data/normalized_yaml/{category}/{safe_name}.yaml')

# Ensure category directory exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# Step 4: Save to new file
with open(output_path, 'w') as f:
    yaml.dump(
        new_medium,
        f,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True
    )

# Step 5: Update registry
new_entry = pd.DataFrame({
    'culturemech_id': [next_id],
    'file_path': [str(output_path)]
})
registry = pd.concat([registry, new_entry], ignore_index=True)
registry.to_csv(registry_path, sep='\t', index=False)

print(f"✓ Created {next_id} → {output_path}")
print(f"✓ Updated registry: {registry_path}")
```

**Key points**:
- ✓ Read registry to find highest ID
- ✓ Create file in category-specific directory
- ✓ Update registry with new ID and path
- ✓ Registry columns: `culturemech_id`, `file_path`

## Batch ID Assignment

For bulk operations, use the existing repository-specific scripts.

### MediaIngredientMech Batch Assignment

**Script**: `scripts/add_mediaingredientmech_ids.py`

**Usage**:
```bash
# Preview changes (dry-run)
python scripts/add_mediaingredientmech_ids.py --dry-run

# Execute assignment
python scripts/add_mediaingredientmech_ids.py

# Custom options
python scripts/add_mediaingredientmech_ids.py \
  --data-path data/curated/unmapped_ingredients.yaml \
  --start-index 1 \
  --show-samples 20
```

**Features**:
- ✓ Skips records that already have IDs
- ✓ Sequential assignment starting from specified index
- ✓ Rich table output showing sample records
- ✓ Statistics on IDs added/skipped
- ✓ `--force-overwrite` option (use with caution)

### CultureMech Batch Assignment

**Script**: `scripts/assign_culturemech_ids.py`

**Usage**:
```bash
# Preview changes (dry-run)
python scripts/assign_culturemech_ids.py --dry-run

# Execute assignment
python scripts/assign_culturemech_ids.py

# Custom start ID
python scripts/assign_culturemech_ids.py --start-id 15432
```

**Features**:
- ✓ Scans all YAML files recursively
- ✓ Finds highest existing ID automatically
- ✓ Assigns IDs to files without them
- ✓ Generates ID registry TSV
- ✓ Sorted processing for deterministic ordering

### CommunityMech Batch Assignment

**Script**: `scripts/add_community_ids.py`

**Usage**:
```bash
# Execute assignment (no dry-run option in simple version)
python scripts/add_community_ids.py
```

**Features**:
- ✓ Simple sequential assignment
- ✓ Processes files in sorted order
- ✓ Updates YAML with ID as first field
- ✓ Progress output for each file

