"""Plan or run one scoped native gate for campaign canary 000296, 2026-11-15.

Uses the unchanged reviewed Phase2 runner, with a single fixed record/source,
new private state and explicit wrapper/launcher provenance. Preparation uses
--plan only; actual gates await the Phase2 technical handoff. No curation,
provider acquisition, earlier private-checkpoint copy or batch is implemented.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
import check_phase2_linked_records_20261115 as native  # noqa: E402

TARGET = "kb/communities/Ecoli_Bifidobacterium_bifidum_Infant_gut_HMO_Mutualism_Coculture.yaml"
CACHE = "references_cache/PMID_42020426.md"
STATE = ROOT / ".temp/campaign-resume-20261115"
LAUNCHER = "scripts/adhoc/run_campaign_hmo_canary_20261115.sh"
GATES = (
    "schema",
    "strict",
    "terms",
    "references",
    "gtdb",
    "domain",
    "history",
    "scalars",
    "network",
)


def configure():
    native.STATE = STATE
    native.TARGETS = {"hmo": TARGET}
    native.CACHES = {"PMID:42020426": CACHE}
    original_inputs = native.inputs

    def bound_inputs():
        return {
            **original_inputs(),
            str(Path(__file__).relative_to(ROOT)): native.sha(Path(__file__)),
            LAUNCHER: native.sha(ROOT / LAUNCHER),
            "scripts/reference_assertion_coverage.py": native.sha(
                ROOT / "scripts/reference_assertion_coverage.py"
            ),
        }

    native.inputs = bound_inputs


def preflight(expected_revision):
    actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if actual != expected_revision:
        raise ValueError("expected current full commit required")
    record = yaml.safe_load((ROOT / TARGET).read_bytes())
    if record.get("id") != "CommunityMech:000296":
        raise ValueError("wrong campaign canary record")
    if set(native.references(record)) != {"PMID:42020426"}:
        raise ValueError("source scope changed; inspect before running")
    if not STATE.is_dir():
        raise ValueError("campaign private state must already exist")
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--generation", required=True)
    parser.add_argument("--gate", choices=GATES)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.generation.isdigit():
        raise ValueError("numeric exclusive generation required")
    configure()
    revision = preflight(args.expected_revision)
    if args.plan:
        print(
            json.dumps(
                {
                    "mode": "plan_only",
                    "revision": revision,
                    "target": TARGET,
                    "record_id": "CommunityMech:000296",
                    "inputs": native.inputs(),
                    "native_runner_sha256": native.sha(
                        ROOT / "scripts/adhoc/check_phase2_linked_records_20261115.py"
                    ),
                    "gates": list(GATES),
                    "reference_policy": "Native matching against a verified private article-cache copy; no acquisition or full-text enrichment.",
                    "ontology_adapters_present": {
                        key: path.is_file() for key, path in native.LOCAL_ONTOLOGIES.items()
                    },
                    "coverage_command": [
                        ".venv/bin/python",
                        "scripts/reference_assertion_coverage.py",
                        "--record",
                        TARGET,
                        "--output",
                        f".temp/campaign-resume-20261115/hmo-coverage-{args.generation}",
                    ],
                    "limitations": "No gate, source judgment, immutable review save or corpus batch ran in plan mode.",
                },
                indent=2,
            )
        )
        return
    if args.gate is None:
        raise ValueError("one explicit gate or --plan required")
    sys.argv = [
        str(ROOT / "scripts/adhoc/check_phase2_linked_records_20261115.py"),
        args.gate,
        "--record",
        "hmo",
        "--expected-revision",
        revision,
        "--name",
        f"linked-hmo-{args.gate}-{args.generation}",
    ]
    native.main()


if __name__ == "__main__":
    main()
