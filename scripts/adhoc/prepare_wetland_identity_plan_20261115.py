"""Author the fixed source-backed Wetland471 identity plan; #2898, 2026-11-15.

Inputs: exact existing record and retained primary cache. Output: JSON stdout for
an exclusive caller-owned plan path. No canonical, source or network writes.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
TARGET = "kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml"
BEFORE = "2191214bbc8d7f8bb6341c6493344e2180eb63fe2098375f44aab9f49d35d199"
SOURCE = "references_cache/PMID_42663479.txt"
SOURCE_SHA = "489eb292cd49275ee0d480727b215360c2101e577aae884a4f52ff68fb7990eb"
ANCHORS = [
    "The “top-down” strategy yielded microbial community Y13.",
    "The 13th transfer was used as the top-down inoculum in this study.",
    "The bottom-up synthetic consortium (M) was rationally constructed following function-based SynCom (synthetic community) design strategies ( 17 , 21 ).",
    "The consortium comprised the obligate organohalide-respiring bacterium Dehalococcoides mccartyi , supported by the corrinoid-provisioning strains Geobacter lovleyi and Sulfurospirillum multivorans ( 9 , 18 ), the fermentative supplier Petrimonas sulfuriphila PET ( 22 ), and seven isolated γ-HCH-degrading strains, several of which harbor cobalamin synthesis genes ( 23 ).",
    "Specifically, Enterococcus avium ATCC 14025 shared an ANI of 98.03 with PseS3 and 98.21 with bin161. Enterococcus thailandicus DSM 21767 exhibited an ANI of 99.35 with R1, 99.31 with R3, and 99.35 with bin381. Similarly, Enterococcus casseliflavus ATCC 49996 shared an ANI of 98.24 with R12 and 98.24 with bin436.",
    "Additionally, it should be noted that the initial consortium was constructed by directly mixing glycerol stocks of individual strains without prior revival and verification of each strain’s viability. The OD 600 data reported here reflect the overall growth of the enrichment culture and do not confirm that all component strains were equally revived.",
    "To further investigate the genomic characteristics of Enterococcus spp., the Enterococcus MAGs (bin161, bin381, and bin436) assembled in this study were compared with whole genomes of Enterococcus spp., including PseS3, R1, R3, R12, and standard strains such as Enterococcus avium ATCC 14025, Enterococcus thailandicus DSM 21767, and Enterococcus casseliflavus ATCC 49996, which were obtained from NCBI.",
]
REPLACEMENTS = [
    (
        ("description",),
        [0, 1, 2, 3, 4, 5],
        "Two anaerobic lindane bioaugmentation treatments in coastal wetland sediment: top-down sediment enrichment Y13 and bottom-up consortium M. M was assembled from Dehalococcoides mccartyi, Geobacter lovleyi (represented here as Trichlorobacter lovleyi), Sulfurospirillum multivorans, Petrimonas sulfuriphila PET and seven isolated gamma-HCH degraders. The five retained taxonomy entries are a partial representation, not a complete shared roster of M and Y13. The Enterococcus casseliflavus entry corresponds to isolate R12; PseS3 is E. avium and R1/R3 are E. thailandicus. Intended inoculum membership does not establish revival or endpoint colonization of every stock. The ecological interaction graph retains separate unresolved mechanism limitations.",
    ),
    (
        ("taxonomy", 0, "taxon_term", "notes"),
        [4, 5, 6],
        "The source ANI comparison identifies isolate R12 as Enterococcus casseliflavus (98.24% ANI to ATCC 49996). Sediment MAG bin436 has the same reported ANI to that reference but is a separate metagenomic reconstruction, not the R12 isolate. PseS3 is E. avium and R1/R3 are E. thailandicus; these other isolates must not be grouped under this E. casseliflavus descriptor. The current five-entry taxonomy is incomplete for consortium M and does not define a complete Y13 roster.",
    ),
    (
        ("taxonomy", 0, "evidence", 0, "explanation"),
        [4, 6],
        "The ANI comparison separately identifies isolate R12 and sediment MAG bin436 as E. casseliflavus relative to ATCC 49996 (98.24% each). It assigns PseS3 to E. avium and R1/R3 to E. thailandicus. Species correspondence does not establish that R12 and bin436 are the same physical strain or genome.",
    ),
    (
        ("taxonomy", 4, "taxon_term", "notes"),
        [2, 3, 5],
        "Obligate organohalide-respiring bacterium included in the bottom-up gamma-HCH-degrading consortium M. Intended inoculum membership does not establish strain-specific revival or endpoint sediment colonization.",
    ),
]


def get(document, keys):
    for key in keys:
        document = document[key]
    return document


def build():
    paths = [
        TARGET,
        SOURCE,
        "tests/test_causal_review_batch133.py",
        "reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml",
        str(Path(__file__).relative_to(ROOT)),
    ]
    captured = {name: (ROOT / name).read_bytes() for name in paths}

    def digest(raw):
        return hashlib.sha256(raw).hexdigest()

    if digest(captured[TARGET]) != BEFORE or digest(captured[SOURCE]) != SOURCE_SHA:
        raise ValueError("fixed record and primary cache required")
    text, document = captured[SOURCE].decode(), yaml.safe_load(captured[TARGET])
    if any(anchor not in text for anchor in ANCHORS):
        raise ValueError("authored source anchor absent")
    discussion = {
        "discussion_id": "wetland-m-y13-stock-and-roster-boundaries",
        "prompt": "Complete the separate M and Y13 membership descriptions without equating inoculated stocks with sediment MAGs or endpoint establishment.",
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "attaches_to": ["taxonomy", "description"],
        "rationale": "Methods identify Y13 as the thirteenth sediment-enrichment transfer and M as a bottom-up mixture of four named partner taxa plus seven isolated degraders. The five current entries therefore represent selected taxa rather than a complete common roster. R12 and bin436 share a species-level ANI assignment but remain an isolate and a sediment MAG, respectively. Bulk revival measurements cannot establish viability of every initial stock.",
        "evidence": [
            {
                "reference": "PMID:42663479",
                "supports": "SUPPORT",
                "evidence_source": "full_text",
                "snippet": ANCHORS[index],
                "explanation": explanation,
            }
            for index, explanation in [
                (0, "Methods assigns the top-down treatment to Y13."),
                (2, "Methods assigns the bottom-up treatment to M."),
                (
                    3,
                    "The reported M composition exceeds the five retained taxonomy entries; no full Table S1 inventory is reconstructed here.",
                ),
                (
                    4,
                    "The ANI paragraph distinguishes three Enterococcus species and separates isolate names from MAG identifiers.",
                ),
                (
                    5,
                    "The authors explicitly limit stock-specific revival inference from bulk OD measurements.",
                ),
                (
                    6,
                    "The comparison treats assembled sediment MAGs and isolate whole genomes as distinct inputs.",
                ),
            ]
        ],
        "posed_by": "Codex",
        "posed_date": "2026-11-15",
        "notes": "Identity corrections are tracked under https://github.com/CultureBotAI/CommunityMech/issues/2898. Full Table S1 membership and strain-specific establishment remain unresolved. Separate mechanism/graph findings under https://github.com/CultureBotAI/CommunityMech/issues/2899 remain open; this correction does not validate the three retained interaction nodes or two causal edges. No taxon, strain accession, genome assignment or experiment-specific participant set is added.",
    }
    result = {
        "scope": "wetland471-source-identity-only",
        "scientific_review": False,
        "target": TARGET,
        "target_id": "CommunityMech:000471",
        "before_sha256": BEFORE,
        "inputs": {name: digest(raw) for name, raw in captured.items()},
        "source_anchors": ANCHORS,
        "changes": [
            {
                "path": list(keys),
                "before": get(document, keys),
                "after": after,
                "source_anchor_indices": indexes,
            }
            for keys, indexes, after in REPLACEMENTS
        ],
        "discussion": discussion,
        "event_changes": "Correct top-down Y13 versus bottom-up M labels and the R12-specific Enterococcus casseliflavus assignment; distinguish R12 isolate from sediment MAG bin436 in notes and evidence explanation. Add an evidence-backed open discussion for partial roster and unverified stock revival. Preserve all taxon terms, existing snippets, GTDB states, functional roles, three interaction nodes, two arrows and earlier history. Issues #2898 and #2899 retain unresolved roster and mechanistic scope; no full scientific approval or mapping correction.",
    }
    if any((ROOT / name).read_bytes() != raw for name, raw in captured.items()):
        raise ValueError("captured input changed")
    return result


if __name__ == "__main__":
    print(json.dumps(build(), indent=2, ensure_ascii=False))
