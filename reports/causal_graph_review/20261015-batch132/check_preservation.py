"""Reproduce the identity-only diff and ignored-inclusive canonical preservation."""

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess

import yaml

ROOT = Path(__file__).resolve().parents[3]
BASE = "d8a37b795d75c372af6d75f590b78cefb913b940"
REL = "kb/communities/Phormidium_Alkaline_Consortium.yaml"
OLD = {"id": "NCBITaxon:1807132", "label": "Candidatus Phormidium alkaliphilum"}
NEW = {"id": "NCBITaxon:3723519", "label": "Candidatus Sodalinema alkaliphilum"}


def original(path):
    return subprocess.check_output(["git", "show", BASE + ":" + path], cwd=ROOT)


before = yaml.safe_load(original(REL))
doc = yaml.safe_load((ROOT / REL).read_bytes())
restored = deepcopy(doc)
nodes = restored["ecological_interactions"]
descriptors = [restored["taxonomy"][0]["taxon_term"], nodes[1]["participating_taxa"][0]]
descriptors += [nodes[i]["source_taxon"] for i in (0, 2, 3)]
for descriptor in descriptors:
    assert descriptor["term"] == NEW
    descriptor["term"] = OLD.copy()
restored["taxonomy"][0]["taxon_term"]["notes"] = before["taxonomy"][0]["taxon_term"]["notes"]
added = restored["taxonomy"][0]["evidence"].pop()
assert added["snippet"] == "the most abundant member and the only cyanobacterium in the consortium"
assert restored["curation_history"].pop()["action"] == "CORRECT_CAUSAL_PARTICIPANT_IDENTITY"
assert restored == before, "Unexpected semantic change outside the reviewed identity fields"
config = yaml.safe_load((ROOT / "conf/id_label_targets.yaml").read_text())
baseline = yaml.safe_load(original("conf/id_label_targets.yaml"))
removed = 0
for target in baseline["targets"]:
    exceptions = target.get("exceptions", [])
    matches = [e for e in exceptions if e["id"] == OLD["id"]]
    removed += len(matches)
    if matches:
        target["exceptions"] = [e for e in exceptions if e["id"] != OLD["id"]]
assert removed == 2 and config == baseline
paths = sorted(
    p for root in (ROOT / "kb/communities", ROOT / "data/isolates") for p in root.rglob("*.yaml")
)
changed = [
    str(p.relative_to(ROOT)) for p in paths if p.read_bytes() != original(str(p.relative_to(ROOT)))
]
assert changed == [REL]
cache = "references_cache/doi_10.3389_fmicb.2022.780346.md"
assert (ROOT / cache).read_bytes() == original(cache)
manifest_dir = ROOT / "reports/causal_graph_review/sources/20261015-phormidium-identity-batch132"
manifest = json.loads((manifest_dir / "manifest.json").read_text())
for name, digest in manifest["files"].items():
    assert hashlib.sha256((manifest_dir / name).read_bytes()).hexdigest() == digest
print(
    json.dumps(
        {
            "records_including_hidden_and_ignored": len(paths),
            "changed_records": changed,
            "unchanged_records": len(paths) - 1,
            "corrected_term_objects": len(descriptors),
            "removed_exact_pair_waivers": removed,
            "graph_topology_and_evidence_preserved": True,
            "old_curation_history_semantically_preserved": True,
            "canonical_cache_unchanged": True,
            "public_source_hashes_verified": len(manifest["files"]),
        },
        indent=2,
    )
)
