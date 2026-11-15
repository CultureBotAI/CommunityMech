"""Copy accepted source judgments into bounded binder inputs, #2848, 2026-11-15.

Inputs: two hash-pinned authored YAML plans and an actual native route triplet.
Output: exclusive JSON config for one selected unit or the eight-record group.
No new scientific judgments, route computation, network access or record edits.
Every input is parsed and hashed from one snapshot, then rechecked (#2879).
"""

import argparse
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = "reports/phase2-completion-20261115/"
PLANS = {
    BASE
    + "status-biofilm-pesticide-three-source-context-001.yaml": "3162568ddcec885e34ef838ab2264e0f48009a40c246c3f0f6b2ae47f72d2a7e",
    BASE
    + "hexamine-five-source-context-001.yaml": "9aed96ecfb1b93875c75ea1a130150b09bb49b97230ae96104a956e435d3b299",
}
EXPECTED_IDS = {"400", "499", "500", "505", "506", "507", "508", "509"}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def local(name):
    path = ROOT / name
    if Path(name).is_absolute() or ".." in Path(name).parts or path.resolve() != path.absolute():
        raise ValueError("ordinary repository-relative path required")
    return path


class CapturedInputs:
    def __init__(self):
        self.raw = {}

    def read(self, name):
        path = local(name)
        if name not in self.raw:
            self.raw[name] = path.read_bytes()
        return self.raw[name]

    def pin(self, name, expected=None):
        value = sha(self.read(name))
        if expected is not None and value != expected:
            raise ValueError("accepted input differs: " + name)
        return {"path": name, "sha256": value}

    def verify(self):
        for name, raw in self.raw.items():
            if local(name).read_bytes() != raw:
                raise ValueError("captured input changed: " + name)


def prepare(route_name, record_id):
    if not re.fullmatch(r"[a-z0-9-]+", route_name):
        raise ValueError("literal retained recorder name required")
    stem = ".temp/phase2-schema-20261115/" + route_name
    captured = CapturedInputs()
    routes = json.loads(captured.read(stem + ".log"))
    receipt = json.loads(captured.read(stem + ".json"))
    if receipt["exit_code"] != 0 or captured.read(stem + ".exit") != b"0\n":
        raise ValueError("successful actual native route required")
    if receipt["log_sha256"] != sha(captured.read(stem + ".log")):
        raise ValueError("retained route log differs")
    observed = {r["record_id"]: r for r in routes["records"]}
    helper = str(Path(__file__).relative_to(ROOT))
    records = []
    declared = set()
    for plan_name, plan_sha in PLANS.items():
        captured.pin(plan_name, plan_sha)
        plan = yaml.safe_load(captured.read(plan_name))
        for row in plan["records"]:
            declared.add(row["id"].split(":")[1][-3:])
            if record_id and row["id"] != record_id:
                continue
            route = observed[row["id"]]
            if route["record"] != row["path"] or route["before_sha256"] != row["before_sha256"]:
                raise ValueError("accepted record identity differs")
            captured.pin(row["path"], row["before_sha256"])
            source = row.get("primary_source", plan.get("primary_source"))
            captured.pin(source["retained_path"], source["retained_sha256"])
            guard = row.get("historical_guard", plan.get("historical_guard"))
            additional = {plan_name: plan_sha, helper: captured.pin(helper)["sha256"]}
            for key in ("path", "ledger"):
                expected = guard.get("sha256" if key == "path" else "ledger_sha256")
                additional[guard[key]] = captured.pin(guard[key], expected)["sha256"]
            prior = row.get("prior_review", plan.get("prior_assessment"))
            if prior:
                additional[prior["path"]] = captured.pin(prior["path"], prior["sha256"])["sha256"]
            history = plan["historical_mapping_input"]
            additional[history["path"]] = captured.pin(history["path"], history["sha256"])["sha256"]
            preservation = row.get("preservation_contract", [row.get("preservation", "")])
            preservation += plan.get("shared_preservation_contract", [])
            occurrences = []
            for item in row["proposed_occurrences"]:
                match = re.fullmatch(r"taxonomy\[(\d+)\]\.taxon_term", item["selector"])
                if match is None:
                    raise ValueError("explicit taxonomy selector required")
                index = int(match[1])
                claim = item.get("correspondence", item)
                found = [r for r in route["occurrences"] if r["taxonomy_index"] == index]
                if len(found) != 1:
                    raise ValueError("exact native occurrence required")
                native = found[0]
                if native["term"] != claim["descriptor"] or native["strain_name"] != item["stock"]:
                    raise ValueError("accepted stock or descriptor differs")
                if any(
                    native["native_result"].get(k) != v
                    for k, v in claim["historical_expected"].items()
                ):
                    raise ValueError("fresh native route differs from the accepted source plan")
                boundary = claim.get("boundary", " ".join(preservation))
                occurrences.append(
                    {
                        "taxonomy_index": index,
                        "term": native["term"],
                        "strain_name": native["strain_name"],
                        "expected_ncbi_rank": "NCBITaxon:" + claim.get("expected_rank", "species"),
                        "native_result": native["native_result"],
                        "classify_status": native["classify_status"],
                        "source_assessment": source["judgment"] + " " + " ".join(preservation),
                        "population_scope": boundary,
                        "name_scope": boundary,
                    }
                )
            records.append(
                {
                    "record": row["path"],
                    "record_id": row["id"],
                    "before_sha256": row["before_sha256"],
                    "additional_inputs": additional,
                    "occurrences": occurrences,
                    "primary_sources": [
                        {
                            "reference": source["reference"],
                            "path": source["retained_path"],
                            "sha256": source["retained_sha256"],
                            "locator": source["locator"],
                            "coverage": source["coverage"],
                            "identity_tokens": [source["url"].removeprefix("https://doi.org/")],
                            "anchors": [source["exact_short_quote"]],
                        }
                    ],
                    "historical_guard_assessment": guard["note"],
                }
            )
    if declared != EXPECTED_IDS or not records or (record_id and len(records) != 1):
        raise ValueError("bounded accepted record inventory differs")
    result = {
        "route_report": captured.pin(stem + ".log"),
        "route_receipt": captured.pin(stem + ".json"),
        "route_exit": captured.pin(stem + ".exit"),
        "records": records,
    }
    captured.verify()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--route-name", required=True)
    parser.add_argument("--record-id")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = prepare(args.route_name, args.record_id)
    output = local(args.output)
    with output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(
        json.dumps(
            {
                "path": args.output,
                "sha256": sha(output.read_bytes()),
                "records": len(result["records"]),
            }
        )
    )


if __name__ == "__main__":
    main()
