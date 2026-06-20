# Finding the Highest ID (all collection types)

*Reference for the **manage-identifiers** skill — see [`../skill.md`](../skill.md) for the CommunityMech overview and core workflow.*

---

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

