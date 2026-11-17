"""Apply bounded, reviewed M5 completion corrections, 2026-11-14.

Inputs: exact baseline bytes and one named correction supported by the saved
scientific reviews. Outputs: one canonical record or cache and an immutable
before/after receipt. Serves #2772/#2709/#2710/#2708/#2676/#2778. Record edits pass
the native closed-schema writer, then require semantic equality of the narrow
text-preserving candidate before atomic replacement. No historical edits.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from record_review import load_document  # noqa: E402

from communitymech.curate.curation_event import (  # noqa: E402
    append_curation_event_text,
    record_curation_event,
)
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

BASE = "76aa644cd6803ea2c9545d4c704276ede219d354"
STATE = ROOT / ".temp/m5-completion-20261114/curation"
MAP = "kg-microbe NCBI2GTDB.tsv.gz sha256:761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd; aggregate denominator, named species only"
RECORDS = {
    "ecofab-relation": ("EcoFAB_Ring_Trial_SynCom17", "000025", 2772),
    "yolo-provenance": ("Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm", "000515", 2709),
    "syncom-mechanism": ("Brachypodium_Natural_Variation_Dopamine_SynCom16", "000516", 2710),
    "syncom-endpoint": ("Brachypodium_Natural_Variation_Dopamine_SynCom16", "000516", 2778),
}
CACHES = {
    "cache-ecofab": ("PMID_40920748.md", "PMC12416739", 2676),
    "cache-nitrogen": ("doi_10.1126_sciadv.adg7888.md", "PMC10776018", 2676),
    "cache-dopamine": ("PMID_42660928.md", "PMC13522444", 2708),
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError("expected exactly one correction anchor")
    return text.replace(old, new, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=[*RECORDS, *CACHES])
    parser.add_argument("--apply", action="store_true", help="default is plan only")
    args = parser.parse_args()
    action = args.action
    if action in RECORDS:
        slug, ident, issue = RECORDS[action]
        path = Path("kb/communities") / (slug + ".yaml")
    else:
        filename, marker, issue = CACHES[action]
        path = Path("references_cache") / filename
    canonical = ROOT / path
    original = canonical.read_bytes()
    if action == "syncom-endpoint":
        prior_receipt = json.loads((STATE / "syncom-mechanism.json").read_text())
        if digest(original) != prior_receipt["after_sha256"]:
            raise ValueError("source differs from independently reviewed first correction")
        baseline_ref = "curation/syncom-mechanism.json:after_sha256"
    else:
        baseline = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
        if original != baseline:
            raise ValueError("source no longer equals assessed baseline; re-review before applying")
        baseline_ref = BASE
    text = original.decode()
    if action == "ecofab-relation":
        text = replace_once(
            text,
            "SynCom17 plus Bradyrhizobium OAE829 is the dopamine-study 16-strain SynCom's superset.",
            "SynCom17 is the dopamine-study 16-strain SynCom plus Bradyrhizobium OAE829.",
        )
        summary = "Corrected the dopamine-study subset description: SynCom17 already includes OAE829; typed relation and stocks unchanged. Primary Methods and ring S2 independently verified; resolves #2772. Other EcoFAB scientific findings remain open."
    elif action == "yolo-provenance":
        replacement = (
            "The source reports Thaumarchaeota in the control soil's 16S composition. "
            "The native rank-for-rank crosswalk assigns NCBITaxon:651137 to the broader "
            "Thermoproteota (631/631 genome support). A separate class-level count of its "
            "65 named-species rows gives Nitrososphaeria 552 genomes across 57 rows and "
            "Nitrososphaeria_A 79 genomes across 8 rows. This curated entry retains the "
            "unsuffixed class at 552/631 (0.875), preserving the mapping's uncertainty. "
            "These taxonomic votes do not establish amoA activity or ammonia oxidation "
            "in this soil experiment. Reproduced from the hash-identified crosswalk "
            "with an aggregate denominator and unnamed species excluded."
        )
        block = (
            "      curation_note: >-\n"
            + textwrap.fill(
                replacement, width=106, initial_indent="        ", subsequent_indent="        "
            )
            + "\n"
        )
        text, count = re.subn(
            r"(?ms)^      curation_note:.*?(?=^      gtdb_id:)", lambda _: block, text
        )
        if count != 1:
            raise ValueError("expected one reviewed mapping note")
        old_map = "kg-microbe NCBI2GTDB.tsv.gz; GTDB release latest (built 2026-07-25)"
        if text.count(old_map) != 5:
            raise ValueError("unexpected mapping provenance count")
        text = text.replace(old_map, MAP)
        text = replace_once(
            text, "kg-microbe NCBI2GTDB.tsv.gz sha256:761d5537a7edb4b0 (file mtime 2026-09-13)", MAP
        )
        summary = "Removed copied record-specific amoA mechanism rationale and pinned the recovered crosswalk hash/method instead of an unsupported latest/build date. Reproduced and preserved all six numerical cores, including curated Nitrososphaeria552/631. Primary soil evidence and treatment effects unchanged; #2709."
    elif action == "syncom-mechanism":
        text = replace_once(
            text, "  host_participation: HOST_IS_SOURCE\n  effect_direction: INCREASES\n", ""
        )
        text = replace_once(
            text, "  host_participation: HOST_IS_SOURCE\n  effect_direction: DECREASES\n", ""
        )
        text = replace_once(text, "  host_participation: HOST_IS_TARGET\n", "")
        summary = "Removed causal host/source effect tags from correlation-only nodes0/1 (#2773), and removed the unsupported host-target assertion from the lower-exudate-dopamine observation (#2710). Preserved all five nodes, source snippets, isolated-culture growth effects and the unresolved microbial-utilization versus altered-host-production explanation."
    elif action == "syncom-endpoint":
        anchor = "- name: SynCom Colonization Lowers Exudate Dopamine\n"
        if text.count(anchor) != 1:
            raise ValueError("expected one reviewed endpoint node")
        prefix, tail = text.split(anchor, 1)
        node, suffix = tail.split("\nenvironmental_factors:\n", 1)
        node = replace_once(node, "  effect_direction: DECREASES\n", "")
        text = prefix + anchor + node + "\nenvironmental_factors:\n" + suffix
        summary = "Removed the residual effect_direction from the lower-exudate-dopamine observation (#2778): the measured endpoint is extracellular dopamine after SynCom inoculation, whereas this schema direction would encode a dopamine effect on participating taxa. Preserved the measured decrease in prose, both quotations, and the unresolved host-versus-microbial explanation; isolate growth directions remain intact."
    else:
        if marker not in text or text.count("content_type: abstract_only") != 1:
            raise ValueError("expected one inaccurate header and existing full-main boundary")
        text = replace_once(
            text, "content_type: abstract_only", "content_type: abstract_and_full_text"
        )
        summary = "Corrected content declaration for the already appended main article; abstract/full-main boundary, PMID/DOI/PMCID, source text and supplementary boundaries unchanged."
    receipt = {
        "action": action,
        "path": str(path),
        "issue": issue,
        "baseline": baseline_ref,
        "before_sha256": digest(original),
        "summary": summary,
        "applied": args.apply,
    }
    if action in RECORDS:
        before = load_document(original)
        candidate = load_document(text)
        if candidate["id"] != "CommunityMech:" + ident:
            raise ValueError("unexpected record identity/history placement")
        if candidate["curation_history"] != before["curation_history"]:
            raise ValueError("existing history changed")
        event = record_curation_event(
            candidate, curator="codex", action="EDIT", changes=summary, llm_assisted=True
        )
        text = append_curation_event_text(
            text,
            curator="codex",
            action="EDIT",
            changes=summary,
            timestamp=event["timestamp"],
            width=110,
        )
        unmarked = {key: value for key, value in event.items() if key != "llm_assisted"}
        text = replace_once(
            text,
            yaml.safe_dump([unmarked], sort_keys=False, allow_unicode=True, width=110).rstrip(),
            yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=110).rstrip(),
        )
        if load_document(text) != candidate:
            raise ValueError("text preservation changed candidate semantics")
        receipt["event"] = event
    else:
        candidate = None
    if not args.apply:
        print(json.dumps(receipt, indent=2))
        return
    STATE.mkdir(parents=True, exist_ok=True)
    receipt_path = STATE / (action + ".json")
    if receipt_path.exists():
        raise ValueError("correction receipt already exists")
    staged = STATE / (action + ".yaml")
    if candidate is not None:
        write_validated_community(candidate, staged)
        if load_document(staged.read_bytes()) != load_document(text):
            raise ValueError("candidate differs from native validated document")
    if canonical.read_bytes() != original:
        raise ValueError("concurrent source change")
    staged.write_text(text)
    staged.replace(canonical)
    receipt["after_sha256"] = digest(canonical.read_bytes())
    if candidate is not None and load_document(canonical.read_bytes()) != candidate:
        raise ValueError("persisted document differs")
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
