"""Review CommunityMech000516 from primary sources on 2026-11-14.

Inputs: current canonical YAML, Ding primary XML, retained findings and M5 check
receipts. Outputs: ignored source extracts, inspection hashes and a new native
review bundle. Serves completion review and #2710/#2708; never edits the KB.
"""

import argparse
import hashlib
import json
import shlex
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml
from defusedxml.ElementTree import parse

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
TARGET = "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml"
TARGET_ID = "CommunityMech:000516"
XML = STATE / "ecofab-relations/PMC13522444.xml"
HOST = "marcins-MacBook-Pro-3.local"
CHECKS = {
    "schema": ["validate", TARGET],
    "strict": ["validate-strict", TARGET],
    "terms": ["validate-terms", TARGET],
    "references": ["validate-references-explained", TARGET],
    "gtdb": ["validate-gtdb", TARGET],
    "domain": ["validate-gtdb-domain", TARGET],
    "history": [
        "validate-history",
        "history/records/Brachypodium_Natural_Variation_Dopamine_SynCom16",
    ],
}
SOURCES = {
    "supplement.pdf": "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-76211-1/MediaObjects/41467_2026_76211_MOESM1_ESM.pdf",
    "stocks.xlsx": "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-76211-1/MediaObjects/41467_2026_76211_MOESM3_ESM.xlsx",
    "fig2.png": "https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-026-76211-1/MediaObjects/41467_2026_76211_Fig2_HTML.png",
    "fig3.png": "https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-026-76211-1/MediaObjects/41467_2026_76211_Fig3_HTML.png",
}


def fetch(name):
    destination = STATE / "dopamine-syncom-sources"
    destination.mkdir(exist_ok=True)
    path = destination / name
    request = urllib.request.Request(
        SOURCES[name], headers={"User-Agent": "CommunityMech-source-review/1.0"}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
        content_type = response.headers.get("Content-Type")
    if not data or (name.endswith(".pdf") and not data.startswith(b"%PDF")):
        raise ValueError("Empty or unexpected source")
    path.write_bytes(data)
    entry = {
        "url": SOURCES[name],
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "bytes": path.stat().st_size,
        "sha256": digest(path),
        "content_type": content_type,
    }
    path.with_suffix(path.suffix + ".source.json").write_text(json.dumps(entry, indent=2) + "\n")
    if name.endswith(".pdf"):
        subprocess.run(
            ["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], check=True
        )
    elif name.endswith(".xlsx"):
        from verify_ecofab_primary_sources_20261114 import extract_xlsx

        extract_xlsx(path)
    print(json.dumps(entry))


def checks():
    for name, arguments in CHECKS.items():
        if name == "schema":
            continue  # verified live canary already completed
        run = [
            "/usr/bin/python3",
            "scripts/adhoc/m5_completion_checks.py",
            "run",
            "--name",
            "dopamine-syncom-" + name,
            "--arguments",
            *arguments,
        ]
        log = f".temp/m5-completion-20261114/dopamine-syncom-{name}.launch.log"
        command = f"cd {shlex.quote(str(ROOT))} && nohup {shlex.join(run)} > {shlex.quote(log)} 2>&1 < /dev/null &"
        subprocess.run(["ssh", "-o", "BatchMode=yes", HOST, command], check=True)
        print("launched " + name, flush=True)


def collect():
    sources = [
        f"{HOST}:{STATE}/dopamine-syncom-{name}.{ext}"
        for name in CHECKS
        for ext in ("json", "log", "exit")
    ]
    subprocess.run(["scp", "-q", *sources, str(STATE)], check=True)
    for name in CHECKS:
        receipt = json.loads((STATE / f"dopamine-syncom-{name}.json").read_text())
        if "exit_code" not in receipt or receipt["log_sha256"] != digest(
            STATE / f"dopamine-syncom-{name}.log"
        ):
            raise ValueError("Incomplete or inconsistent check " + name)
        print(name, receipt["status"], receipt["exit_code"], receipt["log_bytes"])


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def issue_drafts():
    """Prepare review finding bodies; creation is a separate explicit gh command."""
    issues = {
        "correlation-direction": """Independent primary-source review of CommunityMech:000516 at input SHA256 c9f8d489241eb57dbbe7046d668e15abd7bb0d04a718fe014eac465466ebc735.

Stable finding key: `cm-000516-correlation-direction-scope`. Severity: major (P2).

Owner: `kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`, `ecological_interactions[0:2].host_participation` and `.effect_direction`; related guidance `docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md`, Interaction sign.

The two nodes correctly describe observational Spearman associations across host genotypes (five positive members and OAS925 negative). Their `HOST_IS_SOURCE` and `INCREASES`/`DECREASES` fields nonetheless select directional host-to-member effects. The schema defines HOST_IS_SOURCE as a host factor acting on members and EffectDirectionEnum as what the source does to the response. The native scientific checklist explicitly says association does not establish ecological interaction direction. The documentation currently presents these same correlations as signed edges, so the guidance also needs correction or an explicit noncausal association representation.

Primary evidence inspected: [Ding et al. PMID42660928](https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/), Results/Dopamine is a dominant exometabolite, Figure3a and its legend; unadjusted Spearman n=28. Figure3b tests 0/50/100 micrograms per mL dopamine on separate isolates and supports distinct nodes2/3 only. The study does not manipulate endogenous dopamine within the assembled hydroponic SynCom. Genotype-dependent covariates and relative-abundance associations do not establish that host dopamine increased/decreased those members in situ.

Acceptance: preserve the measured correlation direction, n and unadjusted status in prose. Remove the optional causal host/effect tags from nodes0/1, or implement an explicitly noncausal typed representation with tests before using it. Retain direct isolate-growth direction only on nodes2/3 and do not transplant their in-vitro evidence into plant-associated causality. Align the guidance example. Append curation history and run focused checks.

Evidence: primary XML SHA256 9a58e566488461f6bda24554f2ab3c580e53fff58f5413b74e0957220acbe274; actual Figure3 PNG SHA256 35a1928c8878800b9a2b849ebc07a49aac7ffb228ef32a094593a4563f9b9b3e. Seven fresh M5 focused checks passed; lexical/schema success does not resolve semantic overstatement.

Deduplication: live all-state issue searches for 000516, dopamine correlation and OAP107; known #2710 concerns the separate node4 exudate-decrease/host-target mechanism. Search did not include all issue comments.
""",
        "grounding-provenance": """Independent primary-source review of CommunityMech:000516 at input SHA256 c9f8d489241eb57dbbe7046d668e15abd7bb0d04a718fe014eac465466ebc735.

Stable finding key: `cm-000516-grounding-provenance`. Severity: minor (P3).

Owner: `kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml`, taxonomy[9].taxon_term, ecological_interactions[4].participating_taxa[9].term, and the fourteen populated taxonomy[*].taxon_term.gtdb_classification.mapping_source fields.

The OAP107 placeholder and unsupported GTDB release latest / built 2026-07-25 provenance from #2674 recur in this separate maintained record. #2674 targets only CommunityMech:000025, so this issue records the additional owner.

[Ding primary Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/) and Supplementary Data1 row3 identify Arthrobacter OAP107. The [DSM113524 stock catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-113524) identifies the same stock as Arthrobacter sp. Live NCBI taxonomy distinguishes genus1663 from the unclassified species placeholder1667. Use the supported genus while preserving stock identity and unknown species; do not arbitrarily select a GTDB split genus.

The historical mapping snapshot/release is not established by a passing coherence validator. Record mapping file identity/hash/method; filesystem date is not a GTDB release or build date. Preserve valid mappings, canonical Allobosea/Bosea handling and Paenibacillus ambiguity until independently supported changes are justified.

Acceptance: refine OAP107 consistently in taxonomy and its node4 placement with source-linked rank and reevaluated GTDB status, or document why a placeholder is still required. Replace unverified latest/build metadata with reproducible provenance. Append history and rerun term, GTDB and reference checks.

Evidence: fresh NCBI1663/1667 response SHA256 d217e7c098497ea705cfa51f0d3c2bc36a8ee385ccd832b874ece8302e12169d; Ding stock workbook SHA256 185d64e815b7ef418d51b0cea0e2a42136fc92423836497bfe88ecbf6c4abfa3. Review preserves species uncertainty; this is not a claim of a newly identified species.

Deduplication: live all-state 000516, OAP107 and dopamine-correlation issue searches; #2674 is the matching defect in the distinct EcoFAB record. Search did not include every issue comment.
""",
    }
    for key, body in issues.items():
        path = STATE / f"dopamine-syncom-{key}-issue.md"
        path.write_text(body)
        print(path)


def render():
    for page in (1, 9, 11):
        folder = STATE / "dopamine-syncom-sources"
        subprocess.run(
            [
                "pdftoppm",
                "-f",
                str(page),
                "-l",
                str(page),
                "-scale-to",
                "1800",
                "-png",
                "-singlefile",
                str(folder / "supplement.pdf"),
                str(folder / f"supplement-page-{page}"),
            ],
            check=True,
        )


def prepare():
    target = {
        "target_id": TARGET_ID,
        "path": TARGET,
        "label": "Brachypodium Natural-Variation Dopamine SynCom16",
        "kind": "maintained",
        "record_class": "MicrobialCommunity",
        "owner_paths": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "path": TARGET,
                "role": "canonical community record",
            }
        ],
    }
    targets = STATE / "dopamine-syncom-targets.yaml"
    targets.write_text(yaml.safe_dump({"targets": [target]}, sort_keys=False))
    inputs = [
        TARGET,
        "docs/record-review-profile.md",
        "docs/record-reviews.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
        ".claude/skills/review-communities/reference/validation-rules.md",
        ".claude/skills/review-communities/reference/execution-protocol.md",
        ".claude/skills/review-yaml-record/SKILL.md",
        "references_cache/PMID_42660928.md",
        str(XML.relative_to(ROOT)),
        "src/communitymech/schema/communitymech.yaml",
        "AGENTS.md",
        "justfile",
    ]
    command = [sys.executable, "scripts/record_review.py", "inspect", "--targets", str(targets)]
    for name in inputs:
        command.extend(["--input", name])
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    (STATE / "dopamine-syncom-initial-inspection.json").write_text(result.stdout)
    tree = parse(XML)
    lines = []
    for section in tree.getroot().iter("sec"):
        title = section.find("title")
        name = " ".join("".join(title.itertext()).split()) if title is not None else ""
        for index, paragraph in enumerate(section.findall("p")):
            text = " ".join("".join(paragraph.itertext()).split())
            lines.append(f"[{section.get('id')} {name} paragraph {index}] {text}")
    for element in tree.getroot().iter():
        if element.tag in {"fig", "supplementary-material"}:
            lines.append(
                f"[{element.tag} {element.get('id')}] "
                + " ".join("".join(element.itertext()).split())
            )
    (STATE / "dopamine-syncom-primary.txt").write_text("\n\n".join(lines) + "\n")
    print(
        json.dumps(
            {
                "inspection": str(STATE / "dopamine-syncom-initial-inspection.json"),
                "target_sha256": digest(ROOT / TARGET),
                "source_sha256": digest(XML),
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode", choices=["prepare", "checks", "collect", "fetch", "issue-drafts", "render"]
    )
    parser.add_argument("--source", choices=sorted(SOURCES))
    args = parser.parse_args()
    if args.mode == "fetch":
        fetch(args.source)
    else:
        {
            "prepare": prepare,
            "checks": checks,
            "collect": collect,
            "issue-drafts": issue_drafts,
            "render": render,
        }[args.mode]()
