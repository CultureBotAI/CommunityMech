#!/usr/bin/env python3
"""Verify bounded canonical deltas after coordinator freezes writes, 2026-11-14.

Inputs: reviewed base76aa644c, current three records/caches/guidance, and the
native original history. Output: ignored mechanical delta receipt only; no
scientific status or canonical mutation. Serves the post-curation batch review.
Run only after native initial inspect and the all-writes-complete notification.
"""

import copy
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = "76aa644cd6803ea2c9545d4c704276ede219d354"
STATE = ROOT / ".temp/m5-completion-20261114"
SLUGS = {
    "CommunityMech:000025": "EcoFAB_Ring_Trial_SynCom17",
    "CommunityMech:000515": "Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm",
    "CommunityMech:000516": "Brachypodium_Natural_Variation_Dopamine_SynCom16",
}
CACHES = ("PMID_40920748.md", "doi_10.1126_sciadv.adg7888.md", "PMID_42660928.md")
MAP = "kg-microbe NCBI2GTDB.tsv.gz sha256:761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd; aggregate denominator, named species only"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def baseline(path):
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)


def semantic_diff(before, after, path=""):
    if isinstance(before, dict) and isinstance(after, dict):
        output = []
        for key in sorted(set(before) | set(after)):
            child = f"{path}.{key}" if path else key
            if key not in before or key not in after:
                output.append(child)
            else:
                output.extend(semantic_diff(before[key], after[key], child))
        return output
    if isinstance(before, list) and isinstance(after, list) and len(before) == len(after):
        return [
            item
            for index, (old, new) in enumerate(zip(before, after, strict=True))
            for item in semantic_diff(old, new, f"{path}[{index}]")
        ]
    return [] if before == after else [path]


def main():
    if not (STATE / "postcuration-initial-inspection.json").exists():
        raise ValueError("Capture native initial inspection before delta verification")
    results = []
    for identifier, slug in SLUGS.items():
        path = f"kb/communities/{slug}.yaml"
        old_raw, new_raw = baseline(path), (ROOT / path).read_bytes()
        old = yaml.load(old_raw, Loader=yaml.CSafeLoader)
        new = yaml.load(new_raw, Loader=yaml.CSafeLoader)
        expected = copy.deepcopy(old)
        if new["id"] != identifier:
            raise ValueError("Identity changed")
        if identifier == "CommunityMech:000025":
            expected["related_communities"][0][
                "description"
            ] = "SynCom17 is the dopamine-study 16-strain SynCom plus Bradyrhizobium OAE829."
        elif identifier == "CommunityMech:000515":
            for index in range(6):
                mapping = expected["taxonomy"][index]["taxon_term"]["gtdb_classification"]
                source = mapping["mapping_source"]
                prefix = source.split(" [grounded", 1)[0]
                mapping["mapping_source"] = source.replace(prefix, MAP, 1)
            expected["taxonomy"][4]["taxon_term"]["gtdb_classification"]["curation_note"] = new[
                "taxonomy"
            ][4]["taxon_term"]["gtdb_classification"]["curation_note"]
            # Its scientific wording needs a separate human/agent assessment.
        else:
            for index in (0, 1):
                del expected["ecological_interactions"][index]["host_participation"]
                del expected["ecological_interactions"][index]["effect_direction"]
            del expected["ecological_interactions"][4]["host_participation"]
            del expected["ecological_interactions"][4]["effect_direction"]
        old_history, new_history = old["curation_history"], new["curation_history"]
        expected_events = 2 if identifier == "CommunityMech:000516" else 1
        if (
            new_history[:-expected_events] != old_history
            or len(new_history) != len(old_history) + expected_events
        ):
            raise ValueError("History must append exactly the reviewed events")
        appended = new_history[len(old_history) :]
        if any(
            event.get("llm_assisted") is not True or event.get("curator") != "codex"
            for event in appended
        ):
            raise ValueError("New inline event lacks truthful actor/LLM provenance")
        expected["curation_history"] = new_history
        if expected != new:
            raise ValueError(
                f"Unexpected semantic change in {path}: {semantic_diff(expected, new)}"
            )
        results.append(
            {
                "target_id": identifier,
                "path": path,
                "before_sha256": sha(old_raw),
                "after_sha256": sha(new_raw),
                "bounded_semantics_match": True,
                "changed_selectors": semantic_diff(old, new),
                "new_inline_events": appended,
            }
        )
    for filename in CACHES:
        path = f"references_cache/{filename}"
        old, new = baseline(path), (ROOT / path).read_bytes()
        anchor = b"content_type: abstract_only"
        if old.count(anchor) != 1 or new != old.replace(
            anchor, b"content_type: abstract_and_full_text", 1
        ):
            raise ValueError(f"Cache has unexpected changes: {path}")
        results.append(
            {
                "path": path,
                "before_sha256": sha(old),
                "after_sha256": sha(new),
                "only_content_type_changed": True,
            }
        )
    history_roots = [f"history/records/{slug}" for slug in SLUGS.values()]
    tracked = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BASE, *history_roots], cwd=ROOT, text=True
    ).splitlines()
    for path in tracked:
        if (ROOT / path).read_bytes() != baseline(path):
            raise ValueError("Previously committed history changed: " + path)
    receipt = {
        "base": BASE,
        "status": "bounded_delta_passed_not_scientific_approval",
        "results": results,
        "prior_history_files_unchanged": len(tracked),
        "prior_history_search_roots": history_roots,
        "guidance_requires_separate_read": "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
        "new_sidecars_require_native_validation": True,
    }
    output = STATE / "postcuration-diff-check.json"
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(output)


if __name__ == "__main__":
    main()
