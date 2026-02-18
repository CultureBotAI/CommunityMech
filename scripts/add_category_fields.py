#!/usr/bin/env python3
"""
Add community_origin and community_category fields to community YAML files.

This script reads each YAML file in kb/communities/, determines the appropriate
community_origin (based on ecological_state) and community_category (based on
keywords in name/description), and adds these fields after ecological_state.
"""

import os
import re
from pathlib import Path
from typing import Dict, Tuple


def determine_community_origin(ecological_state: str) -> str:
    """
    Determine community_origin based on ecological_state.

    Args:
        ecological_state: The ecological state from the YAML file

    Returns:
        Either 'NATURAL' or 'ENGINEERED'
    """
    if ecological_state in ['STABLE', 'PERTURBED']:
        return 'NATURAL'
    elif ecological_state in ['ENGINEERED', 'TRANSIENT']:
        return 'ENGINEERED'
    else:
        # Default to NATURAL if unknown
        return 'NATURAL'


def determine_community_category(name: str, description: str) -> str:
    """
    Determine community_category based on keywords in name and description.

    Args:
        name: Community name
        description: Community description

    Returns:
        One of the defined community categories
    """
    # Combine name and description for keyword matching (case-insensitive)
    text = (name + ' ' + description).lower()

    # Check patterns in priority order
    # Note: Specific AMD sites (Richmond Mine, Tinto River) are checked first
    # Note: DIET is checked before SYNTROPHY because DIET is a specific type of syntrophy
    if any(keyword in text for keyword in ['richmond mine', 'tinto river', 'acid mine drainage', 'amd']):
        return 'AMD'

    if any(keyword in text for keyword in ['biomining', 'bioleaching', 'heap leach']):
        return 'BIOMINING'

    if any(keyword in text for keyword in ['direct interspecies electron transfer']):
        return 'DIET'

    if any(keyword in text for keyword in ['syntrophy', 'syntrophic']):
        return 'SYNTROPHY'

    if any(keyword in text for keyword in ['algae', 'diatom', 'chlamydomonas', 'phytoplankton', 'chlorella', 'coscinodiscus']):
        return 'PHYTOPLANKTON'

    if any(keyword in text for keyword in ['rhizosphere', 'root', 'arabidopsis', 'wheat', 'sorghum', 'maize', 'lotus']):
        return 'RHIZOSPHERE'

    if any(keyword in text for keyword in ['lignocellulose', 'cellulose']):
        return 'LIGNOCELLULOSE'

    if any(keyword in text for keyword in ['methano', 'methanogen']):
        return 'METHANOGENESIS'

    if any(keyword in text for keyword in ['metal reduction', 'uranium reducing', 'iron reducing', 'chromium', 'sulfur reduction']):
        return 'METAL_REDUCTION'

    if any(keyword in text for keyword in ['bioremediation', 'oil-degrading', 'pollutant', 'degradation', 'benzoate', 'cinnamate']):
        return 'BIOREMEDIATION'

    if any(keyword in text for keyword in ['carbon sequestration', 'co2 capture']):
        return 'CARBON_SEQUESTRATION'

    if any(keyword in text for keyword in ['extreme', 'thermophilic', 'halophilic', 'deep subsurface', 'acidophil']):
        return 'EXTREME_ENVIRONMENT'

    if any(keyword in text for keyword in ['industrial', 'reactor', 'e-waste', 'catalyst', 'recovery', 'pgm', 'rare earth', 'ree', 'indium', 'gold', 'uranium', 'lead', 'zinc', 'polymetallic']):
        return 'BIOTECHNOLOGY'

    # Default category
    return 'OTHER'


def process_yaml_file(file_path: Path) -> Tuple[bool, str]:
    """
    Process a single YAML file to add community_origin and community_category.

    Args:
        file_path: Path to the YAML file

    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract name
        name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
        if not name_match:
            return False, f"No 'name' field found in {file_path.name}"
        name = name_match.group(1).strip()

        # Extract description
        desc_match = re.search(r'^description:\s*>(.+?)(?=^[a-z_]+:)', content, re.MULTILINE | re.DOTALL)
        if not desc_match:
            return False, f"No 'description' field found in {file_path.name}"
        description = desc_match.group(1).strip()

        # Extract ecological_state
        state_match = re.search(r'^ecological_state:\s*(\w+)$', content, re.MULTILINE)
        if not state_match:
            return False, f"No 'ecological_state' field found in {file_path.name}"
        ecological_state = state_match.group(1).strip()

        # Check if fields already exist
        if re.search(r'^community_origin:', content, re.MULTILINE):
            return False, f"'community_origin' already exists in {file_path.name}"
        if re.search(r'^community_category:', content, re.MULTILINE):
            return False, f"'community_category' already exists in {file_path.name}"

        # Determine the values
        origin = determine_community_origin(ecological_state)
        category = determine_community_category(name, description)

        # Find the position to insert (after ecological_state line)
        lines = content.split('\n')
        new_lines = []
        inserted = False

        for i, line in enumerate(lines):
            new_lines.append(line)
            if not inserted and re.match(r'^ecological_state:\s*\w+$', line):
                # Insert the new fields after ecological_state
                new_lines.append(f'community_origin: {origin}')
                new_lines.append(f'community_category: {category}')
                inserted = True

        if not inserted:
            return False, f"Could not find insertion point in {file_path.name}"

        # Write back to file
        new_content = '\n'.join(new_lines)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, f"✓ {file_path.name}: origin={origin}, category={category}"

    except Exception as e:
        return False, f"Error processing {file_path.name}: {str(e)}"


def main():
    """Main function to process all YAML files."""
    # Get the script directory and construct path to communities directory
    script_dir = Path(__file__).parent
    communities_dir = script_dir.parent / 'kb' / 'communities'

    if not communities_dir.exists():
        print(f"Error: Communities directory not found at {communities_dir}")
        return 1

    # Find all YAML files
    yaml_files = sorted(communities_dir.glob('*.yaml'))

    if not yaml_files:
        print(f"Error: No YAML files found in {communities_dir}")
        return 1

    print(f"Found {len(yaml_files)} YAML files to process\n")

    # Process each file
    success_count = 0
    error_count = 0

    for yaml_file in yaml_files:
        success, message = process_yaml_file(yaml_file)
        print(message)
        if success:
            success_count += 1
        else:
            error_count += 1

    # Print summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Successfully processed: {success_count}")
    print(f"  Errors/Skipped: {error_count}")
    print(f"  Total: {len(yaml_files)}")
    print(f"{'='*60}")

    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    exit(main())
