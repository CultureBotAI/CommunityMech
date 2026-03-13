---
name: manage-identifiers
description: Generic identifier management for X-Mech repositories - finding highest IDs, minting new IDs, and adding records with proper ID placement
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
---

# Identifier Management for X-Mech Repositories

## Overview

**Purpose**: Maintain stable, sequential identifiers across X-Mech repositories (MediaIngredientMech, CultureMech, CommunityMech, and future projects) to ensure data integrity, enable cross-references, and support knowledge graph integration.

**Why**: Identifiers provide persistent references for records, enable semantic linking in knowledge graphs, support data provenance tracking, and maintain consistency across datasets.

**Scope**: All X-Mech repositories that use the standard identifier format `RepoName:NNNNNN` where NNNNNN is a zero-padded 6-digit sequential number.

## When to Use This Skill

Use this skill when:
- Adding new records to any X-Mech repository
- Finding the next available ID for a new record
- Understanding how to mint IDs for different collection types
- Running batch ID assignment operations
- Validating ID sequences and checking for duplicates or gaps
- Setting up a new X-Mech repository with identifier infrastructure
- Troubleshooting ID-related issues (conflicts, formatting, gaps)

## Identifier Format

### Standard Format

```
RepoName:NNNNNN
```

**Components:**
- `RepoName`: Repository name (e.g., MediaIngredientMech, CultureMech, CommunityMech)
- `:`: Separator (colon)
- `NNNNNN`: Zero-padded 6-digit sequential number (000001 to 999999)

**Examples:**
- `MediaIngredientMech:000001` - First ingredient
- `CultureMech:015431` - 15,431st medium
- `CommunityMech:000078` - 78th community

### Why This Format?

1. **Human-readable**: Easy to recognize and parse
2. **Sortable**: Alphabetical sort = numerical sort (due to zero-padding)
3. **Stable**: Never changes once assigned (independent of content)
4. **Unique**: Guaranteed uniqueness within repository
5. **Cross-referenceable**: Easy to link between repositories
6. **KG-compatible**: Works as RDF subject/object in knowledge graphs

## Collection Types

X-Mech repositories use two main patterns for organizing records:

### Type 1: Single-File Collection

**Pattern**: All records stored in one YAML file with a collection key

**Example Repository**: MediaIngredientMech

**Structure**:
```yaml
generation_date: '2026-03-09T06:54:18.022301+00:00'
total_count: 112
mapped_count: 65
unmapped_count: 47
ingredients:  # <-- Collection key
  - id: MediaIngredientMech:000001
    preferred_term: Sodium chloride
    mapping_status: MAPPED
    # ... other fields

  - id: MediaIngredientMech:000002
    preferred_term: Glucose
    mapping_status: MAPPED
    # ... other fields
```

**Characteristics**:
- ✓ Simple to manage (one file)
- ✓ Easy to see all records at once
- ✓ Good for <1000 records
- ✗ Large files can be slow to load/edit
- ✗ Git merge conflicts more likely

**Files**:
- Data: `data/curated/unmapped_ingredients.yaml`
- ID script: `scripts/add_mediaingredientmech_ids.py`

### Type 2: Multi-File Collection

**Pattern**: Each record is a separate YAML file in a directory hierarchy

**Example Repositories**: CultureMech, CommunityMech

**Structure**:
```
data/normalized_yaml/
├── bacterial/
│   ├── LB_Medium.yaml        # id: CultureMech:000001
│   ├── TSA_Medium.yaml       # id: CultureMech:000002
│   └── ...
├── algae/
│   ├── BG11_Medium.yaml      # id: CultureMech:000500
│   └── ...
└── fungi/
    └── PDA_Medium.yaml       # id: CultureMech:001000
```

**Each file contains**:
```yaml
id: CultureMech:000001
name: LB Medium
category: bacterial
# ... other fields
```

**Characteristics**:
- ✓ Scales well (1000s of records)
- ✓ Smaller git diffs (one file per change)
- ✓ Parallel editing easier
- ✗ More complex to manage
- ✗ Need to scan all files to find highest ID

**CultureMech adds**: ID registry file (`data/culturemech_id_registry.tsv`)
```tsv
culturemech_id	file_path
CultureMech:000001	data/normalized_yaml/bacterial/LB_Medium.yaml
CultureMech:000002	data/normalized_yaml/bacterial/TSA_Medium.yaml
```

**Files**:
- Data: `data/normalized_yaml/**/*.yaml`
- ID script: `scripts/assign_culturemech_ids.py` (with registry)
- Registry: `data/culturemech_id_registry.tsv` (CultureMech only)

### Comparison Table

| Feature | Single-File | Multi-File | Multi-File + Registry |
|---------|-------------|------------|----------------------|
| **Repo Example** | MediaIngredientMech | CommunityMech | CultureMech |
| **Record Count** | 112 | 78 | 15,431 |
| **Find Highest ID** | Parse YAML once | Scan all files | Read registry file |
| **Add New Record** | Append to list | Create new file | Create file + update registry |
| **Git Conflicts** | More likely | Rare | Rare |
| **Scalability** | <1000 records | <10,000 records | 10,000+ records |
| **Complexity** | Low | Medium | Medium-High |

## Finding the Highest ID

Before minting a new ID, you need to find the current maximum ID number.

### Method 1: Single-File Collection (MediaIngredientMech)

**Python approach**:
```python
import yaml
import re
from pathlib import Path

def find_highest_id_single_file(
    yaml_path: Path,
    prefix: str = "MediaIngredientMech",
    collection_key: str = "ingredients"
) -> int:
    """Find highest ID in single-file YAML collection.

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix (e.g., "MediaIngredientMech")
        collection_key: YAML key for collection (e.g., "ingredients")

    Returns:
        Highest ID number (0 if none found)
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    max_id = 0
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if match := re.match(rf'{prefix}:(\d+)', id_str):
            max_id = max(max_id, int(match.group(1)))

    return max_id

# Usage
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
highest = find_highest_id_single_file(yaml_path, 'MediaIngredientMech', 'ingredients')
print(f"Highest ID: {highest}")  # Output: 112
```

**Quick bash one-liner**:
```bash
# MediaIngredientMech
grep -o 'MediaIngredientMech:[0-9]\+' data/curated/unmapped_ingredients.yaml | \
  cut -d: -f2 | sort -n | tail -1
```

### Method 2: Multi-File Collection (CommunityMech)

**Python approach**:
```python
import yaml
import re
from pathlib import Path

def find_highest_id_multi_file(
    directory: Path,
    prefix: str = "CommunityMech",
    pattern: str = "*.yaml"
) -> int:
    """Find highest ID across multiple YAML files.

    Args:
        directory: Directory to search
        prefix: ID prefix (e.g., "CommunityMech")
        pattern: Glob pattern for files (default: "*.yaml")

    Returns:
        Highest ID number (0 if none found)
    """
    max_id = 0

    for yaml_file in directory.glob(pattern):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id', '')
            if match := re.match(rf'{prefix}:(\d+)', id_str):
                max_id = max(max_id, int(match.group(1)))
        except Exception as e:
            print(f"Error reading {yaml_file}: {e}")
            continue

    return max_id

# Usage
communities_dir = Path('kb/communities')
highest = find_highest_id_multi_file(communities_dir, 'CommunityMech')
print(f"Highest ID: {highest}")  # Output: 78
```

**Recursive search** (for nested directories):
```python
def find_highest_id_recursive(
    base_dir: Path,
    prefix: str = "CultureMech"
) -> int:
    """Recursively find highest ID in directory tree."""
    max_id = 0

    for yaml_file in base_dir.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id', '')
            if match := re.match(rf'{prefix}:(\d+)', id_str):
                max_id = max(max_id, int(match.group(1)))
        except Exception:
            continue

    return max_id

# Usage for CultureMech with nested dirs
base_dir = Path('data/normalized_yaml')
highest = find_highest_id_recursive(base_dir, 'CultureMech')
print(f"Highest ID: {highest}")  # Output: 15431
```

**Quick bash approach**:
```bash
# CommunityMech (single directory)
grep -rh 'id: CommunityMech:' kb/communities/ | \
  cut -d: -f3 | sort -n | tail -1

# CultureMech (nested directories)
find data/normalized_yaml -name "*.yaml" -exec grep -h 'id: CultureMech:' {} \; | \
  cut -d: -f3 | sort -n | tail -1
```

### Method 3: Using Registry File (CultureMech)

**Python approach**:
```python
import pandas as pd
import re

def find_highest_id_from_registry(
    registry_path: Path,
    prefix: str = "CultureMech"
) -> int:
    """Find highest ID from TSV registry file.

    Args:
        registry_path: Path to registry TSV
        prefix: ID prefix (e.g., "CultureMech")

    Returns:
        Highest ID number (0 if none found)
    """
    registry = pd.read_csv(registry_path, sep='\t')

    max_id = 0
    for id_str in registry['culturemech_id']:
        if match := re.match(rf'{prefix}:(\d+)', id_str):
            max_id = max(max_id, int(match.group(1)))

    return max_id

# Usage
registry_path = Path('data/culturemech_id_registry.tsv')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
print(f"Highest ID: {highest}")  # Output: 15431
```

**Bash approach**:
```bash
# Quick lookup from registry
tail -n +2 data/culturemech_id_registry.tsv | \
  cut -f1 | cut -d: -f2 | sort -n | tail -1
```

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

## Validation and Troubleshooting

### Validating ID Format

**Python validator**:
```python
import re

def validate_id_format(id_string: str, prefix: str) -> bool:
    """Validate ID matches expected format.

    Args:
        id_string: ID to validate (e.g., "MediaIngredientMech:000001")
        prefix: Expected prefix (e.g., "MediaIngredientMech")

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_id_format("MediaIngredientMech:000001", "MediaIngredientMech")
        True

        >>> validate_id_format("MediaIngredientMech:1", "MediaIngredientMech")
        False  # Not zero-padded

        >>> validate_id_format("CultureMech:000001", "MediaIngredientMech")
        False  # Wrong prefix
    """
    pattern = rf'^{re.escape(prefix)}:\d{{6}}$'
    return bool(re.match(pattern, id_string))

# Usage
is_valid = validate_id_format("MediaIngredientMech:000001", "MediaIngredientMech")
print(f"Valid: {is_valid}")  # True
```

### Finding Duplicate IDs

**Single-file collection**:
```python
from collections import Counter

def find_duplicate_ids(yaml_path: Path, collection_key: str = "ingredients") -> list[str]:
    """Find duplicate IDs in single-file collection."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    ids = [record.get('id') for record in data.get(collection_key, [])]
    counts = Counter(ids)

    duplicates = [id_str for id_str, count in counts.items() if count > 1]
    return duplicates

# Usage
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
duplicates = find_duplicate_ids(yaml_path)
if duplicates:
    print(f"⚠️  Duplicate IDs found: {duplicates}")
else:
    print("✓ No duplicates")
```

**Multi-file collection**:
```python
from collections import defaultdict

def find_duplicate_ids_multi_file(directory: Path) -> dict[str, list[Path]]:
    """Find duplicate IDs across multiple files."""
    id_to_files = defaultdict(list)

    for yaml_file in directory.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id')
            if id_str:
                id_to_files[id_str].append(yaml_file)
        except Exception:
            continue

    # Filter to only duplicates
    duplicates = {id_str: files for id_str, files in id_to_files.items() if len(files) > 1}
    return duplicates

# Usage
base_dir = Path('data/normalized_yaml')
duplicates = find_duplicate_ids_multi_file(base_dir)
if duplicates:
    for id_str, files in duplicates.items():
        print(f"⚠️  {id_str} found in {len(files)} files:")
        for file in files:
            print(f"   - {file}")
else:
    print("✓ No duplicates")
```

### Finding Gaps in Sequence

**Check for gaps**:
```python
def find_id_gaps(yaml_path: Path, prefix: str, collection_key: str = "ingredients") -> list[int]:
    """Find gaps in ID sequence for single-file collection."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    ids = []
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if match := re.match(rf'{prefix}:(\d+)', id_str):
            ids.append(int(match.group(1)))

    ids.sort()
    if not ids:
        return []

    # Find gaps
    expected = set(range(ids[0], ids[-1] + 1))
    actual = set(ids)
    gaps = sorted(expected - actual)

    return gaps

# Usage
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
gaps = find_id_gaps(yaml_path, 'MediaIngredientMech')
if gaps:
    print(f"⚠️  Gaps found in sequence: {gaps}")
else:
    print("✓ No gaps (sequential)")
```

### Common Issues and Solutions

#### Issue 1: Duplicate IDs

**Symptom**: Same ID appears in multiple records

**Cause**: Manual editing, script error, or merge conflict

**Solution**:
```python
# Re-run batch assignment with force-overwrite
python scripts/add_mediaingredientmech_ids.py --force-overwrite

# Or manually fix in YAML and re-run without force
```

#### Issue 2: Incorrect Zero-Padding

**Symptom**: IDs like `MediaIngredientMech:1` instead of `MediaIngredientMech:000001`

**Cause**: Manual creation without using `f"{prefix}:{number:06d}"`

**Solution**:
```python
# Fix formatting
def fix_id_padding(id_string: str) -> str:
    """Fix ID zero-padding."""
    parts = id_string.split(':')
    if len(parts) == 2:
        prefix, number = parts
        return f"{prefix}:{int(number):06d}"
    return id_string

# Apply to all records
# (re-run batch script or manual fix)
```

#### Issue 3: Registry Out of Sync (CultureMech)

**Symptom**: Registry missing IDs or has wrong file paths

**Cause**: Manual file moves or registry not updated

**Solution**:
```python
# Rebuild registry from scratch
import pandas as pd
from pathlib import Path

def rebuild_registry(base_dir: Path, output_path: Path):
    """Rebuild CultureMech ID registry from YAML files."""
    records = []

    for yaml_file in base_dir.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id')
            if id_str and id_str.startswith('CultureMech:'):
                records.append({
                    'culturemech_id': id_str,
                    'file_path': str(yaml_file)
                })
        except Exception:
            continue

    df = pd.DataFrame(records).sort_values('culturemech_id')
    df.to_csv(output_path, sep='\t', index=False)
    print(f"✓ Rebuilt registry with {len(df)} entries")

# Usage
rebuild_registry(
    Path('data/normalized_yaml'),
    Path('data/culturemech_id_registry.tsv')
)
```

#### Issue 4: Gaps in Sequence

**Symptom**: Missing IDs (e.g., 1, 2, 4, 5 - missing 3)

**Cause**: Deleted record, manual ID assignment, or migration

**Solution**:
```
This is usually fine! IDs are persistent - once assigned, they should never be reused.
If a record is deleted, its ID should remain unused (tombstone).

To fill gaps (NOT RECOMMENDED):
- Only if absolutely necessary for migration/cleanup
- Re-run batch assignment with sequential ordering
- Document the renumbering in changelog
```

## Best Practices

### DO:
✓ **Always run `--dry-run` first** before batch operations
✓ **Validate after changes** using validation functions
✓ **Use zero-padding** (`{number:06d}`)
✓ **Place `id` field first** in YAML for readability
✓ **Update metadata** (`total_count`, `generation_date`) for single-file collections
✓ **Update registry** when adding/moving files (CultureMech)
✓ **Preserve ID history** - never reuse deleted IDs
✓ **Use existing scripts** for batch operations
✓ **Document manual additions** in curation history or metadata

### DON'T:
✗ **Don't manually assign IDs** without checking highest ID first
✗ **Don't reuse IDs** from deleted records (breaks references)
✗ **Don't use `sort_keys=True`** when saving YAML (breaks field order)
✗ **Don't skip registry updates** (CultureMech)
✗ **Don't force-overwrite** existing IDs unless absolutely necessary
✗ **Don't create gaps intentionally** (sequential is better)
✗ **Don't use non-standard formats** (stick to `Prefix:NNNNNN`)

## Repository-Specific Workflows

### MediaIngredientMech Quick Reference

**Current state**: 112 ingredients (`MediaIngredientMech:000001` to `MediaIngredientMech:000112`)

**Add single ingredient**:
```python
# 1. Find next ID
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
highest = find_highest_id_single_file(yaml_path, 'MediaIngredientMech', 'ingredients')
next_id = generate_xmech_id('MediaIngredientMech', highest + 1)

# 2. Create record (see Workflow 1 above)
# 3. Append to data['ingredients']
# 4. Update data['total_count']
# 5. Save YAML
```

**Batch operation**:
```bash
python scripts/add_mediaingredientmech_ids.py --dry-run
python scripts/add_mediaingredientmech_ids.py
```

### CultureMech Quick Reference

**Current state**: 15,431 media (`CultureMech:000001` to `CultureMech:015431`)

**Add single medium**:
```python
# 1. Find next ID from registry
registry_path = Path('data/culturemech_id_registry.tsv')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)

# 2. Create record (see Workflow 3 above)
# 3. Save to category directory
# 4. Update registry
```

**Batch operation**:
```bash
python scripts/assign_culturemech_ids.py --dry-run
python scripts/assign_culturemech_ids.py
```

**Rebuild registry**:
```python
rebuild_registry(
    Path('data/normalized_yaml'),
    Path('data/culturemech_id_registry.tsv')
)
```

### CommunityMech Quick Reference

**Current state**: 78 communities (`CommunityMech:000001` to `CommunityMech:000078`)

**Add single community**:
```python
# 1. Find next ID
communities_dir = Path('kb/communities')
highest = find_highest_id_multi_file(communities_dir, 'CommunityMech')
next_id = generate_xmech_id('CommunityMech', highest + 1)

# 2. Create record (see Workflow 2 above)
# 3. Save to communities directory
```

**Batch operation**:
```bash
python scripts/add_community_ids.py
```

## Integration with Other Tools

### Using with IngredientCurator

The `IngredientCurator` class in MediaIngredientMech handles ID preservation automatically:

```python
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

curator = IngredientCurator(yaml_path='data/curated/unmapped_ingredients.yaml')

# IDs are preserved when loading
curator.load()

# When adding new ingredients manually, mint ID first
next_id = mint_next_id(
    Path('data/curated/unmapped_ingredients.yaml'),
    'MediaIngredientMech',
    'single_file',
    'ingredients'
)

# Then create record with ID
new_record = {
    'id': next_id,
    'preferred_term': 'New Ingredient',
    # ... other fields
}

# Curator preserves IDs when saving
curator.save()
```

### Using in Knowledge Graph Export

IDs serve as RDF subjects in KG exports:

```python
# Example KGX export
from kgx import Transformer

# MediaIngredientMech:000001 becomes RDF subject
subject = "MediaIngredientMech:000001"
predicate = "biolink:has_chemical_role"
object = "CHEBI:32599"

# Can be referenced from other entities
edge = {
    "subject": "CultureMech:000001",  # LB Medium
    "predicate": "biolink:has_part",
    "object": "MediaIngredientMech:000001"  # Sodium chloride
}
```

## Future Enhancements

**Not in current scope, but documented for future consideration**:

1. **Centralized xmech-common Package**
   - Shared ID utilities across all X-Mech repos
   - Consistent validation and minting logic
   - Cross-repo reference checking

2. **CLI Tool for ID Management**
   ```bash
   xmech-id mint MediaIngredientMech
   xmech-id validate data/curated/unmapped_ingredients.yaml
   xmech-id check-duplicates data/normalized_yaml/
   ```

3. **Automated CI/CD Validation**
   - Pre-commit hooks to validate IDs
   - GitHub Actions to check for duplicates
   - Automatic registry rebuilding

4. **ID Migration Utilities**
   - Safe renumbering with tombstone tracking
   - Cross-reference preservation
   - Migration audit trails

5. **Web UI for ID Management**
   - Visual gap detection
   - Duplicate resolution interface
   - Batch assignment dashboard

## Complete Code Examples

### Utility Module (Copy-Paste Ready)

Save this as `src/mediaingredientmech/utils/id_utils.py` (or equivalent in other repos):

```python
"""Generic ID utilities for X-Mech repositories."""

import re
import yaml
from pathlib import Path
from typing import Optional


def parse_xmech_id(id_string: str, expected_prefix: str) -> Optional[int]:
    """Parse X-Mech ID and return number part.

    Args:
        id_string: ID to parse (e.g., "MediaIngredientMech:000001")
        expected_prefix: Expected prefix (e.g., "MediaIngredientMech")

    Returns:
        ID number (e.g., 1) or None if invalid
    """
    if not id_string or not id_string.startswith(f"{expected_prefix}:"):
        return None

    try:
        return int(id_string.split(':', 1)[1])
    except (IndexError, ValueError):
        return None


def generate_xmech_id(prefix: str, number: int) -> str:
    """Generate formatted X-Mech ID.

    Args:
        prefix: Repository name
        number: Sequential number (1-999999)

    Returns:
        Formatted ID (e.g., "MediaIngredientMech:000001")
    """
    return f"{prefix}:{number:06d}"


def validate_id_format(id_string: str, prefix: str) -> bool:
    """Validate ID matches expected format.

    Args:
        id_string: ID to validate
        prefix: Expected prefix

    Returns:
        True if valid, False otherwise
    """
    pattern = rf'^{re.escape(prefix)}:\d{{6}}$'
    return bool(re.match(pattern, id_string))


def find_highest_id_single_file(
    yaml_path: Path,
    prefix: str,
    collection_key: str = "ingredients"
) -> int:
    """Find highest ID in single-file YAML collection.

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix
        collection_key: YAML key for collection

    Returns:
        Highest ID number (0 if none found)
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    max_id = 0
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if id_num := parse_xmech_id(id_str, prefix):
            max_id = max(max_id, id_num)

    return max_id


def find_highest_id_multi_file(
    directory: Path,
    prefix: str,
    pattern: str = "*.yaml"
) -> int:
    """Find highest ID across multiple YAML files.

    Args:
        directory: Directory to search (recursive)
        prefix: ID prefix
        pattern: Glob pattern for files

    Returns:
        Highest ID number (0 if none found)
    """
    max_id = 0

    for yaml_file in directory.rglob(pattern):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id', '')
            if id_num := parse_xmech_id(id_str, prefix):
                max_id = max(max_id, id_num)
        except Exception:
            continue

    return max_id


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

    Raises:
        ValueError: If collection_type is invalid
    """
    if collection_type == "single_file":
        highest = find_highest_id_single_file(source, prefix, collection_key)
    elif collection_type == "multi_file":
        highest = find_highest_id_multi_file(source, prefix)
    else:
        raise ValueError(f"Unknown collection_type: {collection_type}")

    return generate_xmech_id(prefix, highest + 1)


# Example usage
if __name__ == "__main__":
    # MediaIngredientMech
    next_id = mint_next_id(
        Path('data/curated/unmapped_ingredients.yaml'),
        'MediaIngredientMech',
        'single_file',
        'ingredients'
    )
    print(f"Next MediaIngredientMech ID: {next_id}")

    # CommunityMech
    next_id = mint_next_id(
        Path('kb/communities'),
        'CommunityMech',
        'multi_file'
    )
    print(f"Next CommunityMech ID: {next_id}")
```

## Summary Decision Tree

```
┌─────────────────────────────────────┐
│ Need to add a new record?           │
└─────────────┬───────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │ What collection type?│
    └──────┬────────┬──────┘
           │        │
    Single │        │ Multi
    File   │        │ File
           ▼        ▼
    ┌──────────┐  ┌──────────┐
    │Find max  │  │Find max  │
    │in YAML   │  │across    │
    │array     │  │files     │
    └─────┬────┘  └─────┬────┘
          │             │
          │             ▼
          │      ┌──────────────┐
          │      │Has registry? │
          │      └───┬──────┬───┘
          │          │Yes   │No
          │          ▼      │
          │      ┌───────┐  │
          │      │Read   │  │
          │      │registry│ │
          │      └───┬───┘  │
          │          │      │
          └──────────┴──────┘
                     │
                     ▼
            ┌────────────────┐
            │Mint next ID:   │
            │max + 1         │
            └────────┬───────┘
                     │
                     ▼
            ┌────────────────┐
            │Create record   │
            │with ID first   │
            └────────┬───────┘
                     │
          ┌──────────┴────────────┐
          │                       │
    Single│                       │Multi
    File  ▼                       ▼
    ┌──────────┐          ┌──────────────┐
    │Append to │          │Create new    │
    │array     │          │YAML file     │
    │          │          │              │
    │Update    │          │Update        │
    │metadata  │          │registry?     │
    └─────┬────┘          └──────┬───────┘
          │                      │
          │                      │
          └──────────┬───────────┘
                     │
                     ▼
            ┌────────────────┐
            │Save changes    │
            └────────────────┘
```

## Conclusion

This skill provides complete coverage of identifier management across X-Mech repositories. Use the provided code examples, best practices, and workflows to maintain stable, sequential IDs that support data integrity and knowledge graph integration.

For repository-specific details, see the Quick Reference sections. For troubleshooting, see the Validation and Troubleshooting section. For future enhancements, see the Future Enhancements section.

**Remember**: IDs are persistent references - treat them with care, validate before committing, and never reuse deleted IDs.
