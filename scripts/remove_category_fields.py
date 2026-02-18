#!/usr/bin/env python3
"""
Remove community_origin and community_category fields from community YAML files.
This is a helper script to clean up before re-running the add script.
"""

import re
from pathlib import Path


def remove_fields(file_path: Path) -> bool:
    """Remove community_origin and community_category fields from a YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the two fields
        content = re.sub(r'^community_origin:.*\n', '', content, flags=re.MULTILINE)
        content = re.sub(r'^community_category:.*\n', '', content, flags=re.MULTILINE)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False


def main():
    script_dir = Path(__file__).parent
    communities_dir = script_dir.parent / 'kb' / 'communities'

    yaml_files = sorted(communities_dir.glob('*.yaml'))

    for yaml_file in yaml_files:
        remove_fields(yaml_file)

    print(f"Removed fields from {len(yaml_files)} files")


if __name__ == '__main__':
    main()
