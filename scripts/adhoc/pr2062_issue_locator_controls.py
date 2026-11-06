"""Check issue preparation against the real batch and a forbidden-text control.

Only scratch issue drafts and a new control receipt are written. No GitHub,
canonical record, or immutable review mutations are performed.
"""

import copy
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import yaml

HELPER = Path("scripts/adhoc/batch_review_issues.py")
INVENTORY = Path(".temp/pr2062/review-inventory.json")
OUT = Path(".temp/pr2062/issue-locator-controls")


def main():
    if OUT.exists():
        raise ValueError(f"Refusing to overwrite control outputs: {OUT}")
    spec = importlib.util.spec_from_file_location("issue_helper", HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    inventory = json.loads(INVENTORY.read_text())
    count = 0
    originals = {}
    for row in inventory:
        source = Path(row["review"])
        originals[str(source)] = hashlib.sha256(source.read_bytes()).hexdigest()
        review = yaml.safe_load(source.read_text())
        args = SimpleNamespace(pr=2062, review=source, revision=revision, output=OUT / "valid")
        helper.prepare(args)
        plan = json.loads((args.output / f"{row['target_id'].split(':')[1]}-plan.json").read_text())
        for item in plan:
            finding = next(f for f in review["findings"] if f["finding_id"] == item["finding_id"])
            body = Path(item["body_file"]).read_text()
            assert chr(64) not in body
            assert finding["description"] in body
            assert source.as_posix() in body
            for action in review["actions"]:
                if finding["finding_id"] in action["finding_ids"]:
                    assert all(check in body for check in action["acceptance_checks"])
            count += 1
    assert count == 35
    original = Path(inventory[0]["review"])
    altered = copy.deepcopy(yaml.safe_load(original.read_text()))
    altered["findings"][0]["description"] += " " + chr(64) + "mention-control"
    args = SimpleNamespace(pr=2062, review=original, revision=revision, output=OUT / "rejected")
    with patch.object(helper.yaml, "safe_load", return_value=altered):
        try:
            helper.prepare(args)
        except AssertionError as exc:
            assert "mentions are prohibited" in str(exc)
        else:
            raise AssertionError("Forbidden mention was accepted")
    assert not list(args.output.iterdir())
    # A location without explanatory prose must still fail the same guard.
    selector = "XPath //*[" + chr(64) + 'id="source"]/p[1]'
    assert helper.publication_locator(selector) == selector
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == h for p, h in originals.items())
    receipt = {
        "prepared_findings": count,
        "all_descriptions_and_acceptance_checks_preserved": True,
        "ordinary_mentions_rejected_before_any_issue_file": True,
        "selector_only_locator_not_silently_erased": True,
        "original_reviews_unchanged": originals,
        "helper_sha256": hashlib.sha256(HELPER.read_bytes()).hexdigest(),
        "scope": "Issue prose only; exact source selectors remain in immutable review bundles.",
    }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
