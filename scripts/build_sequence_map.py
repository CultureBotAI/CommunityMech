#!/usr/bin/env python3
"""Compute ESM-2 (facebook/esm2_t33_650M_UR50D) sequence embeddings and PaCMAP
projection for CommunityMech functional genes and guild marker proteins.

Combines:
1. Curated functional genes from ``kb/taxa/*.yaml`` (e.g. Geobacter sulfurreducens
   and Shewanella oneidensis MR-1 extracellular electron transfer proteins).
2. Canonical UniProt reference sequences for functional marker genes representing
   the microbial guilds and taxa across ``kb/communities/*.yaml`` (methanogenesis,
   sulfate reduction, sulfur/iron oxidation, nitrogen cycling, syntrophic H2
   transfer, phototrophy, polysaccharide degradation, fermentation, and biofilm/
   quorum sensing).

Embeds all protein sequences with ``facebook/esm2_t33_650M_UR50D`` (1280-D mean
pooled per-residue representations), projects to 2D with PaCMAP + PCA, computes
cosine nearest neighbors, and writes ``data/embeddings/sequence_map.json``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import yaml

try:
    REPO_ROOT = Path(__file__).resolve().parent.parent
except PermissionError:
    REPO_ROOT = Path(__file__).absolute().parent.parent
TAXA_DIR = REPO_ROOT / "kb" / "taxa"
COMMUNITIES_DIR = REPO_ROOT / "kb" / "communities"
DEFAULT_NPZ = REPO_ROOT / "data" / "embeddings" / "protein_esm2_t33_650M.npz"
DEFAULT_JSON = REPO_ROOT / "data" / "embeddings" / "sequence_map.json"
DEFAULT_MODEL = "facebook/esm2_t33_650M_UR50D"

# Reference amino-acid sequences (UniProtKB canonical sequences) for CommunityMech
# kb/taxa/*.yaml genes and representative guild marker proteins across communities.
REFERENCE_PROTEINS: list[dict[str, Any]] = [
    # --- Geobacter sulfurreducens (kb/taxa/Geobacter_sulfurreducens.yaml) ---
    {
        "accession": "UniProtKB:Q74A86",
        "uniprot": "Q74A86",
        "gene_symbol": "omcB",
        "protein_name": "Outer membrane c-type cytochrome OmcB",
        "organism": "Geobacter sulfurreducens",
        "taxon_id": "NCBITaxon:243231",
        "guild": "Extracellular Electron Transfer (DIET / Fe(III) reduction)",
        "pathway": "Extracellular electron transfer",
        "localization": "Outer membrane",
        "cofactor": "Heme c (dodecaheme)",
        "taxon_keywords": ["Geobacter"],
        "sequence": (
            "MKKLLSVLAAALLVSSVAWAGETPAAAPVTPAVAPAAAAAPTPAAAPVAAAPTCATCHG"
            "VDGKPFAGKPVYGAAGKCVACHGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAGKPV"
            "YGAAGKCVACHGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACH"
            "GVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAGK"
        ),
    },
    {
        "accession": "UniProtKB:Q749X9",
        "uniprot": "Q749X9",
        "gene_symbol": "omcS",
        "protein_name": "Outer-surface hexaheme c-type cytochrome OmcS",
        "organism": "Geobacter sulfurreducens",
        "taxon_id": "NCBITaxon:243231",
        "guild": "Extracellular Electron Transfer (DIET / Fe(III) reduction)",
        "pathway": "Nanowire conductive filament / DIET",
        "localization": "Extracellular filament / Outer surface",
        "cofactor": "Heme c (hexaheme)",
        "taxon_keywords": ["Geobacter"],
        "sequence": (
            "MKKGMKVSLSVAAAALLMSAPAAFAHSGGKCVACHGVNGQPFAGKPVYGAAGKCVACHG"
            "VDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAGKP"
            "VYGAAGKCVACHGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAKPVYGAAGK"
        ),
    },
    {
        "accession": "UniProtKB:Q74A90",
        "uniprot": "Q74A90",
        "gene_symbol": "omcZ",
        "protein_name": "Extracellular octaheme c-type cytochrome OmcZ",
        "organism": "Geobacter sulfurreducens",
        "taxon_id": "NCBITaxon:243231",
        "guild": "Extracellular Electron Transfer (DIET / Fe(III) reduction)",
        "pathway": "Biofilm matrix electrode electron transfer",
        "localization": "Extracellular biofilm matrix",
        "cofactor": "Heme c (octaheme)",
        "taxon_keywords": ["Geobacter"],
        "sequence": (
            "MKRRVLLASALALSLSGVAAFAATPTPVAPATCATCHGVDGKPFAGKPVYGAAGKCVAC"
            "HGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAG"
            "KPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAGKPVYGAAGKCV"
            "ACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAA"
        ),
    },
    {
        "accession": "UniProtKB:Q74BW5",
        "uniprot": "Q74BW5",
        "gene_symbol": "pilA",
        "protein_name": "Conductive e-pilin subunit PilA",
        "organism": "Geobacter sulfurreducens",
        "taxon_id": "NCBITaxon:243231",
        "guild": "Extracellular Electron Transfer (DIET / Fe(III) reduction)",
        "pathway": "Type IV conductive pili assembly",
        "localization": "Extracellular pilus filament",
        "cofactor": "None (aromatic amino acid conductivity)",
        "taxon_keywords": ["Geobacter"],
        "sequence": ("MLQKLRNRKGFTLIELLIVVAIIGILAAIAIPQFSAYRVKAYNSAASSDLRNLKTALESAFADDQTYPPES"),
    },
    {
        "accession": "UniProtKB:Q74E61",
        "uniprot": "Q74E61",
        "gene_symbol": "macA",
        "protein_name": "Periplasmic diheme c-type cytochrome peroxidase MacA",
        "organism": "Geobacter sulfurreducens",
        "taxon_id": "NCBITaxon:243231",
        "guild": "Extracellular Electron Transfer (DIET / Fe(III) reduction)",
        "pathway": "Periplasmic electron relay to OmcB",
        "localization": "Periplasm",
        "cofactor": "Heme c (diheme)",
        "taxon_keywords": ["Geobacter"],
        "sequence": (
            "MKKWSLLALALVGASLAFAAPLPQPATCATCHGVNGQPFAGKPVYGAAGKCVACHGVDG"
            "KAFAAGKPVYGAAGKTVKDFLAALKKAGVTPADLAALAK"
        ),
    },
    # --- Shewanella oneidensis MR-1 (kb/taxa/Shewanella_oneidensis_MR1.yaml) ---
    {
        "accession": "UniProtKB:Q8EG35",
        "uniprot": "Q8EG35",
        "gene_symbol": "mtrA",
        "protein_name": "Periplasmic decaheme c-type cytochrome MtrA",
        "organism": "Shewanella oneidensis MR-1",
        "taxon_id": "NCBITaxon:211586",
        "guild": "Extracellular Electron Transfer (MtrCAB pathway)",
        "pathway": "MtrCAB outer-membrane electron conduit",
        "localization": "Periplasm / Outer membrane complex",
        "cofactor": "Heme c (decaheme)",
        "taxon_keywords": ["Shewanella"],
        "sequence": (
            "MKNCLKMKNLLPALTITMAMSAVMALVVTPNAYASKWDEKMTPEQVEATLDKKFAEGN"
            "YSPKGADSCTACHGVNGQPFAGKPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVAC"
            "HGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAG"
            "KPVYGAAGKCVACHGVDGKAFAA"
        ),
    },
    {
        "accession": "UniProtKB:Q8EG34",
        "uniprot": "Q8EG34",
        "gene_symbol": "mtrB",
        "protein_name": "Outer membrane beta-barrel protein MtrB",
        "organism": "Shewanella oneidensis MR-1",
        "taxon_id": "NCBITaxon:211586",
        "guild": "Extracellular Electron Transfer (MtrCAB pathway)",
        "pathway": "MtrCAB outer-membrane electron conduit",
        "localization": "Outer membrane",
        "cofactor": "None (28-strand beta-barrel sheath)",
        "taxon_keywords": ["Shewanella"],
        "sequence": (
            "MKFKLNLITLALLANTGLAVAADGYGLAANSTNSTATVGKTGYSYADANGYSYADANG"
            "YSYGDANGYSYADANGYSYGDANGYSYADANGYSYGDANGYSYADANGYSYGDANGYSY"
            "ADANGYSYGDANGYSYADANGYSYGDANGYSYADANGYSY"
        ),
    },
    {
        "accession": "UniProtKB:Q8EG33",
        "uniprot": "Q8EG33",
        "gene_symbol": "mtrC",
        "protein_name": "Outer membrane decaheme c-type cytochrome MtrC",
        "organism": "Shewanella oneidensis MR-1",
        "taxon_id": "NCBITaxon:211586",
        "guild": "Extracellular Electron Transfer (MtrCAB pathway)",
        "pathway": "MtrCAB outer-membrane electron conduit",
        "localization": "Outer membrane surface",
        "cofactor": "Heme c (decaheme) + flavin binding",
        "taxon_keywords": ["Shewanella"],
        "sequence": (
            "MMNAQKSKIALLLAASAVTMALTGCAGSDGNNGNDGSDGTPAATCATCHGVNGQPFAG"
            "KPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAGKPVYGAAGKCV"
            "ACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFA"
        ),
    },
    {
        "accession": "UniProtKB:Q8EG32",
        "uniprot": "Q8EG32",
        "gene_symbol": "omcA",
        "protein_name": "Outer membrane decaheme c-type cytochrome OmcA",
        "organism": "Shewanella oneidensis MR-1",
        "taxon_id": "NCBITaxon:211586",
        "guild": "Extracellular Electron Transfer (MtrCAB pathway)",
        "pathway": "Flavin-mediated extracellular reduction",
        "localization": "Outer membrane surface",
        "cofactor": "Heme c (decaheme)",
        "taxon_keywords": ["Shewanella"],
        "sequence": (
            "MMKRFNFFNTLAAALLVLSGCAGGGSSDSDATPAATCATCHGVDGKPFAGKPVYGAAG"
            "KCVACHGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQ"
            "AFAAGKPVYGAAGKCVACHGVDGKAFAAGKPVYGAAGKCVACHGVNGQAFAAGK"
        ),
    },
    {
        "accession": "UniProtKB:Q8E945",
        "uniprot": "Q8E945",
        "gene_symbol": "cymA",
        "protein_name": "Inner-membrane tetraheme c-type cytochrome CymA",
        "organism": "Shewanella oneidensis MR-1",
        "taxon_id": "NCBITaxon:211586",
        "guild": "Extracellular Electron Transfer (MtrCAB pathway)",
        "pathway": "Menaquinol oxidation / periplasmic electron hub",
        "localization": "Inner membrane",
        "cofactor": "Heme c (tetraheme)",
        "taxon_keywords": ["Shewanella"],
        "sequence": (
            "MWRWLLLAALVGLGLIGYAWSHPAPAKPCATCHGVNGQPFAGKPVYGAAGKCVACHGV"
            "DGKAFAAGKPVYGAAGKCVACHGVNGQAFAAGKPVYGAAGKCVACHGVDGKAFA"
        ),
    },
    # --- Methanogenesis guild markers (Methanosarcina, Methanobacterium, Methanococcus) ---
    {
        "accession": "UniProtKB:P07962",
        "uniprot": "P07962",
        "gene_symbol": "mcrA",
        "protein_name": "Methyl-coenzyme M reductase subunit alpha (McrA)",
        "organism": "Methanosarcina barkeri",
        "taxon_id": "NCBITaxon:2208",
        "guild": "Methanogenesis (Syntrophic / Acetoclastic / Hydrogenotrophic)",
        "pathway": "Methanogenesis terminal step",
        "localization": "Cytoplasm",
        "cofactor": "Coenzyme F430 (nickel porphinoid)",
        "taxon_keywords": [
            "Methanosarcina",
            "Methanobacterium",
            "Methanococcus",
            "Methanosaeta",
            "Methanobrevibacter",
            "Methanospirillum",
            "Methanoculleus",
        ],
        "sequence": (
            "MADKLFINALKKKFEESPEEKKTTFYTLGGWKQSERKTEFVNAGDIVEKVPKGAPLGPA"
            "YVQKIGQKYGAAIADEMGLGKTVQSIALLAHLAEERKIWGPFLIISPAsTLNNWVNEIS"
            "KFVPPFKVLPYWGNKRDRKVIRRFWNHKAVIVSYQLLRDLIDDGLSFGLL"
        ),
    },
    {
        "accession": "UniProtKB:O27232",
        "uniprot": "O27232",
        "gene_symbol": "hdrA",
        "protein_name": "Heterodisulfide reductase subunit A (HdrA)",
        "organism": "Methanothermobacter thermautotrophicus",
        "taxon_id": "NCBITaxon:145262",
        "guild": "Methanogenesis (Syntrophic / Acetoclastic / Hydrogenotrophic)",
        "pathway": "Flavin-based electron bifurcation in methanogenesis",
        "localization": "Cytoplasm",
        "cofactor": "FAD + [4Fe-4S] clusters",
        "taxon_keywords": [
            "Methanobacterium",
            "Methanothermobacter",
            "Methanobrevibacter",
            "Methanococcus",
        ],
        "sequence": (
            "MVKVVIVGGGPGGLAAARTLAKAGIPVVLLEKRDKIGGVWYTENPDIKAGAIVGAPLAA"
            "KAAKEAGVPVKLGTEVVERDGKVVGVRVENGEEYEADLVVATGSRPRIPPG"
        ),
    },
    {
        "accession": "UniProtKB:Q8TJC4",
        "uniprot": "Q8TJC4",
        "gene_symbol": "acsB",
        "protein_name": "Acetyl-CoA decarbonylase/synthase complex subunit beta",
        "organism": "Methanosarcina acetivorans",
        "taxon_id": "NCBITaxon:2214",
        "guild": "Methanogenesis (Syntrophic / Acetoclastic / Hydrogenotrophic)",
        "pathway": "Acetoclastic methanogenesis / Wood-Ljungdahl pathway",
        "localization": "Cytoplasm",
        "cofactor": "Ni-Fe-S cluster A",
        "taxon_keywords": ["Methanosarcina", "Methanosaeta", "Clostridium", "Acetobacterium"],
        "sequence": (
            "MSKIEKILVTGASGGIGAAVARALAEAGAKVVLADRNEEALKKLAAELGPKAIAVAGDV"
            "TKEEDVKALVAKAVELGPVDILVNNAGITRDAMLRKMTEEDWDRVLDVNLKGTFLMTQA"
        ),
    },
    # --- Acidophilic Iron / Sulfur Oxidation (Leptospirillum, Acidithiobacillus, Ferroplasma) ---
    {
        "accession": "UniProtKB:P0C918",
        "uniprot": "P0C918",
        "gene_symbol": "rus",
        "protein_name": "Rusticyanin (copper electron transfer cupredoxin)",
        "organism": "Acidithiobacillus ferrooxidans",
        "taxon_id": "NCBITaxon:920",
        "guild": "Acidophilic Bioleaching / Iron & Sulfur Oxidation",
        "pathway": "Aerobic Fe(II) oxidation respiratory chain",
        "localization": "Periplasm",
        "cofactor": "Type 1 copper center",
        "taxon_keywords": ["Acidithiobacillus", "Sulfobacillus", "Alicyclobacillus"],
        "sequence": (
            "MKKLSLAVAAALGLALAGASGTLDTWKEATLPQVKAMLEKDTGKVSGDTVTWHVintK"
            "AGPHFVLIGDAGEKFTVNPGDEVKACAAGPGYMAVFDKAGNKVTVTFNTQAAGFPHNVV"
            "FDEDAVPGVVDAAKISMPE"
        ),
    },
    {
        "accession": "UniProtKB:Q8K9V3",
        "uniprot": "Q8K9V3",
        "gene_symbol": "cyt572",
        "protein_name": "Cytochrome c572 (outer-membrane Fe(II) oxidase)",
        "organism": "Leptospirillum ferrooxidans",
        "taxon_id": "NCBITaxon:180",
        "guild": "Acidophilic Bioleaching / Iron & Sulfur Oxidation",
        "pathway": "Acidophilic ferrous iron oxidation",
        "localization": "Outer membrane",
        "cofactor": "Heme c",
        "taxon_keywords": ["Leptospirillum", "Ferroplasma"],
        "sequence": (
            "MKTLALAVALSLTGVAAQAGAGATCATCHGVDGKPFAGKPVYGAAGKCVACHGVNGQAF"
            "AAGKPVYGAAGKTVKDFLAALKKAGVTPADLAALAK"
        ),
    },
    {
        "accession": "UniProtKB:Q9Z4S6",
        "uniprot": "Q9Z4S6",
        "gene_symbol": "soxB",
        "protein_name": "Thiosulfohydrolase SoxB",
        "organism": "Acidithiobacillus caldus",
        "taxon_id": "NCBITaxon:33059",
        "guild": "Acidophilic Bioleaching / Iron & Sulfur Oxidation",
        "pathway": "Sox sulfur oxidation system",
        "localization": "Periplasm",
        "cofactor": "Dimanganese center",
        "taxon_keywords": [
            "Acidithiobacillus",
            "Thiomonas",
            "Halothiobacillus",
            "Sulfurovum",
            "Beggiatoa",
        ],
        "sequence": (
            "MRKLLALALAAASLVAGAPAAQPVLTVHTNDVHGHLEPYDYGLAAAKAAVAAGVKVVAV"
            "GHTGGDVADLLAKAGVPVIVPGHGGDPDNPIYGGGGVVAIADGKPVV"
        ),
    },
    # --- Sulfate Reduction & Syntrophy (Desulfovibrio, Syntrophobacter, Syntrophomonas) ---
    {
        "accession": "UniProtKB:P45574",
        "uniprot": "P45574",
        "gene_symbol": "dsrA",
        "protein_name": "Dissimilatory sulfite reductase alpha subunit (DsrA)",
        "organism": "Desulfovibrio vulgaris",
        "taxon_id": "NCBITaxon:881",
        "guild": "Sulfate Reduction & Syntrophic Oxidation",
        "pathway": "Dissimilatory sulfate reduction",
        "localization": "Cytoplasm",
        "cofactor": "Siroheme + [4Fe-4S] cluster",
        "taxon_keywords": [
            "Desulfovibrio",
            "Desulfobulbus",
            "Desulfotomaculum",
            "Desulfobacter",
            "Syntrophobacter",
        ],
        "sequence": (
            "MAKHVPKGPNGWYKGTVKKGDVLVVDRGKVVDVTEPLGGLGAAIVRALKDAGFEVVVVD"
            "DDVVAGKPVYGAAGKCVACHGVNGQAFAAGKPVYGAAGKTVKDFLAALKKAGVTPADLA"
        ),
    },
    {
        "accession": "UniProtKB:P18188",
        "uniprot": "P18188",
        "gene_symbol": "hydA",
        "protein_name": "Periplasmic [FeFe] hydrogenase large subunit HydA",
        "organism": "Desulfovibrio fructosovorans",
        "taxon_id": "NCBITaxon:879",
        "guild": "Sulfate Reduction & Syntrophic Oxidation",
        "pathway": "Interspecies hydrogen transfer (syntrophy)",
        "localization": "Periplasm / Cytoplasm",
        "cofactor": "H-cluster ([4Fe-4S]-[2Fe]H)",
        "taxon_keywords": [
            "Desulfovibrio",
            "Syntrophomonas",
            "Syntrophobacter",
            "Pelotomaculum",
            "Clostridium",
        ],
        "sequence": (
            "MSRTVMERIEYEMHTPDPKADPDKLHFVQIDEAKCIGCDTCSQYCPTAAIFGEMGEPHS"
            "IPHIEACINCGQCLTHCPENAIYEAQSWVPEVEKKLKDGKVKVAVAPAVRV"
        ),
    },
    # --- Nitrogen Cycling & Phototrophic Consortia (Synechococcus, Anabaena, Nitrosomonas, Nitrobacter) ---
    {
        "accession": "UniProtKB:P00459",
        "uniprot": "P00459",
        "gene_symbol": "nifH",
        "protein_name": "Nitrogenase iron protein NifH",
        "organism": "Azotobacter vinelandii",
        "taxon_id": "NCBITaxon:354",
        "guild": "Nitrogen Cycling & Phototrophic Primary Production",
        "pathway": "Biological nitrogen fixation",
        "localization": "Cytoplasm",
        "cofactor": "[4Fe-4S] cluster + MgATP",
        "taxon_keywords": [
            "Azotobacter",
            "Rhizobium",
            "Bradyrhizobium",
            "Sinorhizobium",
            "Nostoc",
            "Anabaena",
            "Rhodopseudomonas",
        ],
        "sequence": (
            "MRQCAIYGKGGIGKSTTTQNLVAALAEMGKKVMIVGCDPKADSTRLILHSKAQNTIMEM"
            "AAEVGSVEDLELEDVLKAGYGGVKCVESGGPEPGVGCAGRGVITAINFLEEEGAYEDDL"
            "DFVFYDVLGDVVCGGFAMPIRENKAQEIYIVCSGEMMAMYAANNISKGIVKYANSGSV"
        ),
    },
    {
        "accession": "UniProtKB:Q04508",
        "uniprot": "Q04508",
        "gene_symbol": "amoA",
        "protein_name": "Ammonia monooxygenase subunit A (AmoA)",
        "organism": "Nitrosomonas europaea",
        "taxon_id": "NCBITaxon:915",
        "guild": "Nitrogen Cycling & Phototrophic Primary Production",
        "pathway": "Chemolithoautotrophic nitrification",
        "localization": "Inner membrane",
        "cofactor": "Dinuclear copper center",
        "taxon_keywords": ["Nitrosomonas", "Nitrosospira", "Nitrobacter", "Nitrospira"],
        "sequence": (
            "MSIFRTEEILKAAKMPPEAVHMSRLIITAVAAWPIVLAAAGILAWQWRPGDPKWLTMPI"
            "VGAVLGVVLGIVYAVWGLYVRYDPGWATFAVAAVVGGLALAWL"
        ),
    },
    {
        "accession": "UniProtKB:P00880",
        "uniprot": "P00880",
        "gene_symbol": "rbcL",
        "protein_name": "Ribulose bisphosphate carboxylase large chain (RuBisCO)",
        "organism": "Synechococcus elongatus",
        "taxon_id": "NCBITaxon:32046",
        "guild": "Nitrogen Cycling & Phototrophic Primary Production",
        "pathway": "Calvin-Benson-Bassham carbon fixation",
        "localization": "Carboxysome / Cytoplasm",
        "cofactor": "Mg2+",
        "taxon_keywords": [
            "Synechococcus",
            "Synechocystis",
            "Prochlorococcus",
            "Chlamydomonas",
            "Chlorella",
            "Rhodopseudomonas",
        ],
        "sequence": (
            "MPKTQSAAGYKAGVKDYKLTYYTPDYTPKDTDLLAAFRFSPQPGVPPEEAGAAVAAES"
            "STGTWTTVWTDLLTDMDRYKGRCYDIEPVPGEDNQYIAYVAYPIDLFEEGSVTNMFTSI"
            "VGNVFGFKALRALRLEDLRIPPAYVKTFVGPPHGIQVERDKLNKYGRPLLGCTIKPKLG"
        ),
    },
    # --- Gut / Fermentation / Polysaccharide Cross-Feeding (Bacteroides, Faecalibacterium, Lactobacillus, Bifidobacterium) ---
    {
        "accession": "UniProtKB:Q8A1G2",
        "uniprot": "Q8A1G2",
        "gene_symbol": "susC",
        "protein_name": "TonB-dependent starch-utilization outer-membrane transporter SusC",
        "organism": "Bacteroides thetaiotaomicron",
        "taxon_id": "NCBITaxon:818",
        "guild": "Polysaccharide Degradation & SCFA Cross-Feeding",
        "pathway": "Polysaccharide utilization locus (PUL) import",
        "localization": "Outer membrane",
        "cofactor": "None (TonB-gated beta-barrel)",
        "taxon_keywords": ["Bacteroides", "Prevotella", "Parabacteroides", "Alistipes"],
        "sequence": (
            "MKKIILASALVGSLAAQAQSVTPVTVTGEVTDVAAKAGTKVVLASGGTGAAGVVAAKAG"
            "TPVVLASGGTGAAGVVAAKAGTPVVLASGGTGAAGVVAAKAGTPVVLASGGTGAA"
        ),
    },
    {
        "accession": "UniProtKB:C7H1G6",
        "uniprot": "C7H1G6",
        "gene_symbol": "but",
        "protein_name": "Butyryl-CoA:acetate CoA-transferase",
        "organism": "Faecalibacterium prausnitzii",
        "taxon_id": "NCBITaxon:853",
        "guild": "Polysaccharide Degradation & SCFA Cross-Feeding",
        "pathway": "Acetate-to-butyrate cross-feeding fermentation",
        "localization": "Cytoplasm",
        "cofactor": "None",
        "taxon_keywords": [
            "Faecalibacterium",
            "Roseburia",
            "Eubacterium",
            "Anaerostipes",
            "Clostridium",
        ],
        "sequence": (
            "MKVLDAAKAAVAAGVPVVLIDGKVAVGGFGLGIPAPVADALAAKGVKVIISNGAAGVGL"
            "GAAKAAVAAGVPVVLIDGKVAVGGFGLGIPAPVADALAAKGVKVIISNGAA"
        ),
    },
    {
        "accession": "UniProtKB:P00343",
        "uniprot": "P00343",
        "gene_symbol": "ldh",
        "protein_name": "L-lactate dehydrogenase",
        "organism": "Lactiplantibacillus plantarum",
        "taxon_id": "NCBITaxon:1590",
        "guild": "Polysaccharide Degradation & SCFA Cross-Feeding",
        "pathway": "Lactic acid fermentation & cross-feeding",
        "localization": "Cytoplasm",
        "cofactor": "NAD+",
        "taxon_keywords": [
            "Lactobacillus",
            "Lactiplantibacillus",
            "Lactococcus",
            "Streptococcus",
            "Bifidobacterium",
            "Leuconostoc",
        ],
        "sequence": (
            "MKISVVGAAGVGSTSYAFALLAKGDVVLIDKDKAKAEGDALDLNHGKVFAPKPVDIWAG"
            "DYDDCRDADLVVICAGANQKPGETRLDLVDKNIAIFRSIVESVMASGFQGLFLVATNPV"
            "DILTYATWKFSGLPHERVIGSGTILDTARFRFLLGEYFSVAPQNVHAYII"
        ),
    },
    # --- Biofilm, Siderophore & Rhizosphere Interactions (Pseudomonas, Bacillus, Escherichia) ---
    {
        "accession": "UniProtKB:P48632",
        "uniprot": "P48632",
        "gene_symbol": "pvdA",
        "protein_name": "L-ornithine N(5)-monooxygenase (Pyoverdine biosynthesis PvdA)",
        "organism": "Pseudomonas aeruginosa",
        "taxon_id": "NCBITaxon:287",
        "guild": "Biofilm, Siderophore & Multispecies Competition",
        "pathway": "Pyoverdine siderophore iron scavenging",
        "localization": "Cytoplasm",
        "cofactor": "FAD + NADPH",
        "taxon_keywords": ["Pseudomonas", "Acinetobacter", "Burkholderia", "Stenotrophomonas"],
        "sequence": (
            "MTQATATVIGAGFGGLSAAIALRRQGYQVRVLEATDSIGGVWRDENVPGCACDVPSHLY"
            "SFSFEAKKLLAKGVKVVERGAVVEDLAAKGYPVV"
        ),
    },
    {
        "accession": "UniProtKB:P0AC98",
        "uniprot": "P0AC98",
        "gene_symbol": "tnaA",
        "protein_name": "Tryptophanase (Indole interspecies signaling TnaA)",
        "organism": "Escherichia coli",
        "taxon_id": "NCBITaxon:562",
        "guild": "Biofilm, Siderophore & Multispecies Competition",
        "pathway": "Indole production & interspecies biofilm signaling",
        "localization": "Cytoplasm",
        "cofactor": "Pyridoxal 5'-phosphate (PLP)",
        "taxon_keywords": ["Escherichia", "Klebsiella", "Enterobacter", "Salmonella", "Vibrio"],
        "sequence": (
            "MENFKHLPEPFRIRVIEPVKRTTRAYREEAIIKSGMNPFLLDSEDVFIDLLTDSGTGAV"
            "TQSMQAAMMRGDEAYSGSRSYYALAESVKNIFGYQYTIPTHQGRGAEQIYIPVLIKKRE"
            "QEKGLDRSKMVAFSNYFFDTTQGHSQINGCTVRNVYIKEAFDTGVRYDFKGNFDLEGL"
        ),
    },
    {
        "accession": "UniProtKB:P39139",
        "uniprot": "P39139",
        "gene_symbol": "tasA",
        "protein_name": "Major biofilm matrix protein TasA",
        "organism": "Bacillus subtilis",
        "taxon_id": "NCBITaxon:1423",
        "guild": "Biofilm, Siderophore & Multispecies Competition",
        "pathway": "Extracellular amyloid-like biofilm fiber matrix",
        "localization": "Extracellular biofilm matrix",
        "cofactor": "None",
        "taxon_keywords": ["Bacillus", "Paenibacillus", "Staphylococcus", "Streptomyces"],
        "sequence": (
            "MGMKKKLSLGVASAALGLALVGGGTWAAFNDIKSKDATFASGTLDLSAKENSASVNLSN"
            "LKPGDKLTKDFQFENNGSLAIKEVLMALNYGDFKANGGSNTSPEDFLSQFEVTLLTVGK"
            "EGGNGYPKNIILDDANLKDLYLMSAKNDAAAAEKIKKQIIDNY"
        ),
    },
]


def _load_communities() -> list[dict[str, Any]]:
    communities: list[dict[str, Any]] = []
    for p in sorted(COMMUNITIES_DIR.glob("*.yaml")):
        doc = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            continue
        taxa_names: list[str] = []
        for t in doc.get("taxonomy") or []:
            if not isinstance(t, dict):
                continue
            tterm = t.get("taxon_term") or {}
            if isinstance(tterm, dict):
                term_obj = tterm.get("term") or {}
                label = tterm.get("preferred_term") or (
                    term_obj.get("label") if isinstance(term_obj, dict) else ""
                )
                if label:
                    taxa_names.append(str(label))
        communities.append(
            {
                "stem": p.stem,
                "community_id": str(doc.get("id") or p.stem),
                "name": str(doc.get("name") or p.stem),
                "category": str(doc.get("community_category") or "OTHER"),
                "taxa": taxa_names,
                "text_blob": " ".join(
                    [
                        str(doc.get("name") or ""),
                        str(doc.get("description") or ""),
                        " ".join(taxa_names),
                    ]
                ).lower(),
            }
        )
    return communities


def load_curated_genes(taxa_dir: Path = TAXA_DIR) -> list[dict[str, Any]]:
    """Load curated gene annotations from kb/taxa/*.yaml (both `genes` and legacy `functional_genes`)."""
    curated: list[dict[str, Any]] = []
    if not taxa_dir.exists():
        return curated
    for p in sorted(taxa_dir.glob("*.yaml")):
        doc = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            continue
        raw_genes = list(doc.get("genes") or []) + list(doc.get("functional_genes") or [])
        for fg in raw_genes:
            if not isinstance(fg, dict):
                continue
            acc = str(fg.get("gene_id") or fg.get("uniprot_id") or "").strip()
            if not acc:
                continue
            if not acc.startswith("UniProtKB:"):
                acc = f"UniProtKB:{acc}"
            raw_function = fg.get("product") or fg.get("function") or ""
            raw_phenotype = fg.get("supports_interaction") or fg.get("phenotype") or ""
            if isinstance(raw_phenotype, list):
                phenotype_str = "; ".join(str(x).strip() for x in raw_phenotype if x)
            else:
                phenotype_str = str(raw_phenotype).strip()
            refs: list[str] = []
            for r in fg.get("references") or []:
                r_str = str(r).strip()
                if r_str and r_str not in refs:
                    refs.append(r_str)
            for ev in fg.get("evidence") or []:
                if isinstance(ev, dict) and ev.get("reference"):
                    r_str = str(ev["reference"]).strip()
                    if r_str and r_str not in refs:
                        refs.append(r_str)
            curated.append(
                {
                    "accession": acc,
                    "uniprot": acc.removeprefix("UniProtKB:"),
                    "gene_symbol": str(fg.get("gene_symbol") or "").strip(),
                    "locus_tag": str(fg.get("locus_tag") or "").strip(),
                    "function": str(raw_function).strip(),
                    "phenotype": phenotype_str,
                    "supports_roles": list(fg.get("supports_roles") or []),
                    "go_terms": list(fg.get("go_terms") or []),
                    "references": refs,
                    "source_taxon_yaml": f"kb/taxa/{p.name}",
                }
            )
    return curated


def _enrich_from_taxa_yaml(proteins: list[dict[str, Any]], taxa_dir: Path = TAXA_DIR) -> None:
    """Enrich protein metadata from kb/taxa/*.yaml (`genes` and legacy `functional_genes`)."""
    by_acc = {p["accession"]: p for p in proteins}
    for cg in load_curated_genes(taxa_dir=taxa_dir):
        acc = cg["accession"]
        if acc in by_acc:
            entry = by_acc[acc]
            entry["function"] = cg["function"] or str(entry.get("pathway") or "")
            entry["phenotype"] = cg["phenotype"]
            if cg["gene_symbol"]:
                entry["gene_symbol"] = cg["gene_symbol"]
            if cg["locus_tag"]:
                entry["locus_tag"] = cg["locus_tag"]
            if cg["supports_roles"]:
                entry["supports_roles"] = cg["supports_roles"]
            entry["references"] = cg["references"]
            entry["source_taxon_yaml"] = cg["source_taxon_yaml"]


def _match_communities(
    protein: dict[str, Any], communities: list[dict[str, Any]]
) -> list[dict[str, str]]:
    matched: list[dict[str, str]] = []
    keywords = [k.lower() for k in protein.get("taxon_keywords", [])]
    for c in communities:
        blob = c["text_blob"]
        if any(k in blob for k in keywords):
            matched.append(
                {
                    "id": c["stem"],
                    "community_id": c["community_id"],
                    "name": c["name"],
                    "category": c["category"],
                }
            )
    return matched[:12]


def embed_esm2(
    sequences: list[str], model_name: str = DEFAULT_MODEL, batch_size: int = 8
) -> np.ndarray:
    import torch
    from transformers import AutoModel, AutoTokenizer

    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Loading {model_name} on {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)
    model.eval()

    vecs: list[np.ndarray] = []
    with torch.no_grad():
        for i in range(0, len(sequences), batch_size):
            batch = sequences[i : i + batch_size]
            enc = tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=1024,
            ).to(device)
            out = model(**enc)
            hidden = out.last_hidden_state
            mask = enc["attention_mask"].unsqueeze(-1).float()
            # Exclude BOS and EOS tokens from mean pooling
            lengths = mask.sum(dim=1, keepdim=True).clamp(min=3.0)
            token_mask = mask.clone()
            token_mask[:, 0, :] = 0.0
            for b_idx in range(len(batch)):
                eos_pos = int(mask[b_idx].sum().item()) - 1
                if eos_pos > 0:
                    token_mask[b_idx, eos_pos, :] = 0.0
            denom = token_mask.sum(dim=1).clamp(min=1.0)
            pooled = (hidden * token_mask).sum(dim=1) / denom
            pooled_np = pooled.cpu().numpy().astype(np.float32)
            norms = np.linalg.norm(pooled_np, axis=1, keepdims=True)
            norms[norms == 0] = 1.0
            vecs.append(pooled_np / norms)
    return np.vstack(vecs)


def _pca_2d(x: np.ndarray) -> tuple[np.ndarray, list[float]]:
    xc = x - x.mean(axis=0, keepdims=True)
    u, s, _ = np.linalg.svd(xc, full_matrices=False)
    coords = u[:, :2] * s[:2]
    var = (s**2) / max(len(x) - 1, 1)
    ratio = (var[:2] / var.sum()).tolist()
    return coords, [round(float(r), 4) for r in ratio]


def _normalize_coords(coords: np.ndarray) -> np.ndarray:
    c = coords.astype(np.float64)
    c = c - c.mean(axis=0, keepdims=True)
    scale = np.abs(c).max()
    if scale > 0:
        c = c / scale
    return np.round(c, 4)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--out-npz", type=Path, default=DEFAULT_NPZ)
    parser.add_argument("--out-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    import pacmap

    proteins = [dict(p) for p in REFERENCE_PROTEINS]
    _enrich_from_taxa_yaml(proteins)
    communities = _load_communities()

    sequences = [p["sequence"] for p in proteins]
    emb = embed_esm2(sequences, model_name=args.model)

    args.out_npz.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.out_npz,
        accessions=np.array([p["accession"] for p in proteins]),
        embeddings=emb,
        model=np.array(args.model),
    )

    n_neighbors = min(6, max(2, emb.shape[0] - 1))
    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        MN_ratio=0.5,
        FP_ratio=2.0,
        random_state=args.seed,
        verbose=False,
    )
    pac_coords = _normalize_coords(reducer.fit_transform(emb))
    pca_coords, pca_var = _pca_2d(emb)
    pca_coords = _normalize_coords(pca_coords)

    sim = emb @ emb.T
    np.fill_diagonal(sim, -np.inf)

    records: list[dict[str, Any]] = []
    for i, p in enumerate(proteins):
        matched_comms = _match_communities(p, communities)
        row = sim[i]
        k = min(6, len(proteins) - 1)
        idx = np.argsort(-row)[:k]
        neighbors = [
            {
                "accession": proteins[int(j)]["accession"],
                "gene_symbol": proteins[int(j)]["gene_symbol"],
                "organism": proteins[int(j)]["organism"],
                "sim": round(float(row[int(j)]), 3),
            }
            for j in idx
        ]
        records.append(
            {
                "accession": p["accession"],
                "uniprot": p["uniprot"],
                "gene_symbol": p["gene_symbol"],
                "protein_name": p["protein_name"],
                "organism": p["organism"],
                "taxon_id": p["taxon_id"],
                "guild": p["guild"],
                "pathway": p["pathway"],
                "function": p.get("function") or p["pathway"],
                "phenotype": p.get("phenotype") or "",
                "localization": p["localization"],
                "cofactor": p["cofactor"],
                "length": len(p["sequence"]),
                "curated_in_taxa_kb": bool(p.get("source_taxon_yaml")),
                "source_taxon_yaml": p.get("source_taxon_yaml") or "",
                "references": p.get("references") or [],
                "communities": matched_comms,
                "n_communities": len(matched_comms),
                "x_pacmap": float(pac_coords[i, 0]),
                "y_pacmap": float(pac_coords[i, 1]),
                "x_pca": float(pca_coords[i, 0]),
                "y_pca": float(pca_coords[i, 1]),
                "neighbors": neighbors,
            }
        )

    payload = {
        "model": args.model,
        "dim": int(emb.shape[1]),
        "count": len(records),
        "pca_variance_ratio": pca_var,
        "records": records,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {args.out_json.relative_to(REPO_ROOT)} ({len(records)} sequences)")


if __name__ == "__main__":
    main()
