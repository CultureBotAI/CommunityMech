#!/usr/bin/env python3
"""
CLI wrapper for UniProt reference proteome strain coverage checks.

Usage:
    uv run python scripts/check_uniprot_reference_proteomes.py kb/communities
"""

from communitymech.uniprot_reference_proteomes import main


if __name__ == "__main__":
    raise SystemExit(main())
