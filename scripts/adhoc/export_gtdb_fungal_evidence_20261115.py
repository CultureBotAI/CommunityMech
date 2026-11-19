"""Publish the additional fungal-domain artifact, #2904, 2026-11-15.

Inputs: the existing export config and complete saved mixed-domain review.
Outputs: existing captured public artifacts plus one byte-identical domain
observation and explicit contract in each manifest. No matching or curation.
"""

import argparse
import json
from pathlib import Path

import export_scoped_gtdb_evidence_20261115 as base
import gtdb_fungal_domain_contract_20261115 as contract


def verify_domain_export(review, captured, proof, applied, source):
    if (
        applied.get("contract") != contract.CONTRACT
        or source.get("contract") != contract.CONTRACT
        or applied.get("native_operations") != ["--apply", "--apply-status"]
        or applied.get("domain_proof") != source.get("domain_proof")
    ):
        raise ValueError("mixed fungal export contract differs")
    item = applied["domain_proof"]
    location = base.safe_path(item["path"])
    base.audit.bound(review, location, captured)
    raw = captured[location]
    if base.audit.digest(raw) != item["sha256"]:
        raise ValueError("domain artifact differs from actual application")
    document = json.loads(raw)
    if document != source["domain_observation"]:
        raise ValueError("source and actual domain observation differ")
    contract.verify_document(
        {**source, "before_sha256": proof["before_sha256"]},
        document,
        applied["source_proof"],
        applied["inputs"],
    )
    for name in (contract.ENGINE, contract.HELPER, contract.DOMAIN, contract.ADAPTER):
        path = base.safe_path(name)
        base.audit.bound(review, path, captured)
        if base.audit.digest(captured[path]) != applied["inputs"][name]:
            raise ValueError("domain implementation differs from actual application")
    return location


def prepare(config_path, expected_config_sha):
    captured, pending, result = base.prepare(config_path, expected_config_sha)
    review = base.yaml.safe_load(captured[base.safe_path(result["review"])])
    base.capture_additional(captured, (Path(__file__).resolve(), Path(contract.__file__).resolve()))
    for name in result["manifests"]:
        manifest_path = base.safe_path(name)
        proof = json.loads(pending[manifest_path])
        applied = json.loads(pending[base.safe_path(proof["application_receipt"]["path"])])
        source = json.loads(pending[base.safe_path(proof["native_recomputation"]["path"])])
        location = verify_domain_export(review, captured, proof, applied, source)
        destination = manifest_path.with_name(
            manifest_path.name.removesuffix("-successor.json") + "-domain.raw.json"
        )
        if destination.exists() or destination in pending:
            raise ValueError("exclusive fungal domain artifact required")
        raw, artifact = base.raw_metadata(review, location, destination, captured)
        pending[destination] = raw
        proof.update(contract=contract.CONTRACT, domain_observation=artifact)
        pending[manifest_path] = (json.dumps(proof, indent=2) + "\n").encode()
    base.audit.verify_captured(captured)
    result["contract"] = contract.CONTRACT
    result["implementation"].update(
        {
            str(path.relative_to(base.ROOT)): base.audit.digest(captured[path])
            for path in (Path(__file__).resolve(), Path(contract.__file__).resolve())
        }
    )
    result["artifacts"] = [
        {"path": str(path.relative_to(base.ROOT)), "sha256": base.audit.digest(raw)}
        for path, raw in sorted(pending.items())
    ]
    return captured, pending, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--expected-config-sha256", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    captured, pending, result = prepare(args.config, args.expected_config_sha256)
    if not args.plan:
        base.audit.publish(captured, pending)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
