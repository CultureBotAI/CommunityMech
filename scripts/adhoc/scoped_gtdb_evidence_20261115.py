"""Audit immutable scoped GTDB reviews and publish captured evidence, 2026-11-15.

Inputs: exact review hash and all retained inspected inputs (#2848/#2860).
Audit emits JSON stdout only; callers may publish exclusive metadata through
the captured-byte guard. No canonical, cache, history or review mutation.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import record_review as native_review  # noqa: E402


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class FrozenSchema:
    """Native validation/rendering consumes the same captured schema bytes."""

    def __init__(self, raw):
        self.raw = raw

    def read_text(self, encoding="utf-8"):
        return self.raw.decode(encoding)


def capture_inputs(review_path, expected_sha):
    review_path = Path(review_path).resolve()
    if not review_path.is_relative_to(ROOT / "reviews/structured"):
        raise ValueError("native saved review path required")
    captured = {review_path: review_path.read_bytes()}
    if digest(captured[review_path]) != expected_sha:
        raise ValueError("immutable accepted review bytes differ")
    review = yaml.safe_load(captured[review_path])
    seen = set()
    for item in review["source"]["inputs"]:
        name = item["path"]
        path = (ROOT / name).resolve()
        if Path(name).is_absolute() or not path.is_relative_to(ROOT) or path in seen:
            raise ValueError("unsafe or duplicate saved input")
        seen.add(path)
        if path not in captured:
            captured[path] = path.read_bytes()
        if digest(captured[path]) != item["sha256"]:
            raise ValueError("saved diagnostic input differs: " + name)
    for path in (review_path.with_name("review.md"), ROOT / "schema/record_review.yaml"):
        if path not in captured:
            captured[path] = path.read_bytes()
    return review, captured


def verify_captured(captured):
    for path, raw in captured.items():
        if path.read_bytes() != raw:
            raise ValueError("captured input changed before publication: " + str(path))


def artifact(path, captured):
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(captured[path])}


def bound(review, path, captured):
    item = artifact(path, captured)
    found = [row for row in review["source"]["inputs"] if row["path"] == item["path"]]
    if len(found) != 1 or found[0]["sha256"] != item["sha256"]:
        raise ValueError("artifact absent from saved review inputs")
    return item


def validate_pair(review_path, expected_sha):
    review, captured = capture_inputs(review_path, expected_sha)
    schema = FrozenSchema(captured[ROOT / "schema/record_review.yaml"])
    native_review.validate_review(review, schema_path=schema)
    if (
        native_review.render_markdown(review, schema_path=schema).encode()
        != captured[review_path.with_name("review.md")]
    ):
        raise ValueError("saved Markdown differs from native derivation")
    verify_captured(captured)
    return review, captured


def publish(captured, pending):
    if any(path.exists() or path.is_symlink() for path in pending):
        raise ValueError("public evidence must use new exclusive paths")
    if any(not path.resolve().is_relative_to(ROOT / "reports") for path in pending):
        raise ValueError("public evidence belongs under repository reports")
    verify_captured(captured)
    for path, raw in pending.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(raw)
        if path.read_bytes() != raw:
            raise ValueError("persisted public evidence differs")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--expected-review-sha256", required=True)
    args = parser.parse_args()
    review_path = (ROOT / args.review).resolve()
    review, captured = validate_pair(review_path, args.expected_review_sha256)
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "review": artifact(review_path, captured),
                "markdown": artifact(review_path.with_name("review.md"), captured),
                "review_inputs_verified": len(review["source"]["inputs"]),
                "input_bytes": sum(
                    len(captured[ROOT / row["path"]]) for row in review["source"]["inputs"]
                ),
                "native_validation_passed": True,
                "native_markdown_verified": True,
                "captured_inputs_unchanged": True,
                "scope": "Exact retained input-byte and native-pair audit only; no fresh scientific assessment or corpus QC.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
