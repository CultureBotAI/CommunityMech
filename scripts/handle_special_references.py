#!/usr/bin/env python3
"""
Handle Special Reference Types

Identifies and helps fix non-standard references:
- bioproject:PRJNA... → Find associated publications
- PMC only → Convert to PMID or find DOI
- ResearchGate/MDPI/etc → Find proper citation
"""

import yaml
import re
import requests
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import time


def identify_special_references(yaml_path: Path) -> List[Dict]:
    """Find all non-standard references"""

    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    special_refs = []

    # Check all evidence
    for section in ['taxonomy', 'ecological_interactions', 'environmental_factors']:
        if section not in data:
            continue

        items = data[section]
        for item in items:
            if 'evidence' not in item:
                continue

            for ev in item['evidence']:
                ref = ev.get('reference', '')

                # Categorize special references
                if ref.startswith('bioproject:'):
                    special_refs.append({
                        'file': yaml_path.name,
                        'type': 'bioproject',
                        'reference': ref,
                        'bioproject_id': ref.split(':')[1],
                        'context': section
                    })

                elif ref.startswith('PMID:PMC') or ref.startswith('PMC'):
                    # PMC without PMID
                    pmc_id = ref.replace('PMID:', '').replace('PMC', '')
                    special_refs.append({
                        'file': yaml_path.name,
                        'type': 'pmc_only',
                        'reference': ref,
                        'pmc_id': pmc_id,
                        'context': section
                    })

                elif 'researchgate' in ref.lower():
                    special_refs.append({
                        'file': yaml_path.name,
                        'type': 'researchgate',
                        'reference': ref,
                        'context': section
                    })

                elif ref in ['MDPI', 'PMC articles']:
                    special_refs.append({
                        'file': yaml_path.name,
                        'type': 'incomplete',
                        'reference': ref,
                        'context': section
                    })

    return special_refs


def convert_pmc_to_pmid(pmc_id: str) -> Optional[str]:
    """Convert PMC ID to PMID using NCBI API"""

    try:
        url = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
        params = {
            'ids': f'PMC{pmc_id}',
            'format': 'json',
            'tool': 'communitymech',
            'email': 'noreply@example.com'
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'records' in data and len(data['records']) > 0:
            record = data['records'][0]
            pmid = record.get('pmid')
            doi = record.get('doi')

            if pmid:
                return f"PMID:{pmid}"
            elif doi:
                return f"doi:{doi}"

        return None

    except Exception as e:
        print(f"  Error converting PMC{pmc_id}: {e}")
        return None


def lookup_bioproject_publications(bioproject_id: str) -> List[str]:
    """Find publications associated with a BioProject"""

    # Try PubMed search for BioProject ID
    try:
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            'db': 'pubmed',
            'term': bioproject_id,
            'retmode': 'json',
            'retmax': 5
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'esearchresult' in data and 'idlist' in data['esearchresult']:
            pmids = data['esearchresult']['idlist']
            return [f"PMID:{pmid}" for pmid in pmids]

        return []

    except Exception as e:
        print(f"  Error looking up {bioproject_id}: {e}")
        return []


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Handle special reference types")
    parser.add_argument('--convert-pmc', action='store_true', help="Convert PMC to PMID/DOI")
    parser.add_argument('--lookup-bioproject', action='store_true', help="Lookup BioProject publications")
    args = parser.parse_args()

    kb_dir = Path('kb/communities')
    yaml_files = sorted(kb_dir.glob('*.yaml'))

    print("Special Reference Handler")
    print("=" * 80)
    print()

    all_special = []

    for yaml_path in yaml_files:
        special = identify_special_references(yaml_path)
        if special:
            all_special.extend(special)

    # Group by type
    by_type = defaultdict(list)
    for item in all_special:
        by_type[item['type']].append(item)

    print("Summary:")
    for ref_type, items in sorted(by_type.items()):
        print(f"  {ref_type}: {len(items)}")

    print()
    print("=" * 80)

    # Generate report
    with open('special_references_report.txt', 'w') as f:
        f.write("SPECIAL REFERENCES REPORT\n")
        f.write("=" * 80 + "\n\n")

        # PMC conversions
        if 'pmc_only' in by_type:
            f.write(f"PMC-ONLY REFERENCES ({len(by_type['pmc_only'])})\n")
            f.write("-" * 80 + "\n\n")

            if args.convert_pmc:
                print("\nConverting PMC to PMID...")

                for item in by_type['pmc_only']:
                    f.write(f"{item['file']}: {item['reference']}\n")

                    converted = convert_pmc_to_pmid(item['pmc_id'])
                    if converted:
                        f.write(f"  → {converted}\n\n")
                    else:
                        f.write(f"  → Could not convert\n\n")

                    time.sleep(0.5)  # Rate limit
            else:
                for item in by_type['pmc_only'][:10]:
                    f.write(f"{item['file']}: {item['reference']}\n")
                f.write(f"\n(Run with --convert-pmc to get PMID conversions)\n\n")

        # BioProject references
        if 'bioproject' in by_type:
            f.write(f"\nBIOPROJECT REFERENCES ({len(by_type['bioproject'])})\n")
            f.write("-" * 80 + "\n\n")

            if args.lookup_bioproject:
                print("\nLooking up BioProject publications...")

                for item in by_type['bioproject']:
                    f.write(f"{item['file']}: {item['reference']}\n")

                    pubs = lookup_bioproject_publications(item['bioproject_id'])
                    if pubs:
                        f.write("  Associated publications:\n")
                        for pub in pubs:
                            f.write(f"    - {pub}\n")
                    else:
                        f.write("  → No publications found\n")
                    f.write("\n")

                    time.sleep(0.5)  # Rate limit
            else:
                for item in by_type['bioproject'][:10]:
                    f.write(f"{item['file']}: {item['reference']}\n")
                f.write(f"\n(Run with --lookup-bioproject to find publications)\n\n")

        # Other special types
        for ref_type in ['researchgate', 'incomplete']:
            if ref_type in by_type:
                f.write(f"\n{ref_type.upper()} REFERENCES ({len(by_type[ref_type])})\n")
                f.write("-" * 80 + "\n\n")

                for item in by_type[ref_type]:
                    f.write(f"{item['file']}: {item['reference']}\n")

                f.write("\n(Manual review needed - find proper citations)\n\n")

    print()
    print("✓ Report written: special_references_report.txt")
    print()

    print("Usage:")
    print("  # Convert PMC to PMID/DOI:")
    print("  python scripts/handle_special_references.py --convert-pmc")
    print()
    print("  # Find BioProject publications:")
    print("  python scripts/handle_special_references.py --lookup-bioproject")


if __name__ == '__main__':
    main()
