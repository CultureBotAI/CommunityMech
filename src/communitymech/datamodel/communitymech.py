# Auto generated from communitymech.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-08-04T17:44:50
# Schema: communitymech
#
# id: https://w3id.org/communitymech
# description: Schema for modeling microbial community structure, function, and ecological interactions
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Any, ClassVar, Dict, List, Optional, Union

from jsonasobj2 import JsonObj, as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import camelcase, sfx, underscore
from linkml_runtime.utils.metamodelcore import bnode, empty_dict, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_float, extended_int, extended_str
from rdflib import Namespace, URIRef

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
CHEBI = CurieNamespace("CHEBI", "http://purl.obolibrary.org/obo/CHEBI_")
CL = CurieNamespace("CL", "http://purl.obolibrary.org/obo/CL_")
ENVO = CurieNamespace("ENVO", "http://purl.obolibrary.org/obo/ENVO_")
GO = CurieNamespace("GO", "http://purl.obolibrary.org/obo/GO_")
NCBITAXON = CurieNamespace("NCBITaxon", "http://purl.obolibrary.org/obo/NCBITaxon_")
OBI = CurieNamespace("OBI", "http://purl.obolibrary.org/obo/OBI_")
PMID = CurieNamespace("PMID", "http://www.ncbi.nlm.nih.gov/pubmed/")
UBERON = CurieNamespace("UBERON", "http://purl.obolibrary.org/obo/UBERON_")
COMMUNITYMECH = CurieNamespace("communitymech", "https://w3id.org/communitymech/")
DOI = CurieNamespace("doi", "https://doi.org/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
MECH_SHARED = CurieNamespace("mech_shared", "https://w3id.org/kg-microbe/mech-shared/")
RDFS = CurieNamespace("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
XSD = CurieNamespace("xsd", "http://www.w3.org/2001/XMLSchema#")
DEFAULT_ = COMMUNITYMECH


# Types
class PMID(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PMID"
    type_model_uri = COMMUNITYMECH.PMID


# Class references
class MicrobialCommunityId(extended_str):
    pass


class CommonTaxonId(extended_str):
    pass


@dataclass(repr=False)
class Term(YAMLRoot):
    """
    An ontology term with ID and label
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["Term"]
    class_class_curie: ClassVar[str] = "communitymech:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.Term

    id: str = None
    label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceItem(YAMLRoot):
    """
    An evidence item linking a claim to a publication
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EvidenceItem"]
    class_class_curie: ClassVar[str] = "communitymech:EvidenceItem"
    class_name: ClassVar[str] = "EvidenceItem"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EvidenceItem

    reference: str = None
    supports: Union[str, "EvidenceItemSupportEnum"] = None
    evidence_source: Union[str, "EvidenceSourceEnum"] = None
    snippet: str = None
    explanation: Optional[str] = None
    confidence_score: Optional[float] = None
    computational_provenance: Optional[Union[dict, "ComputationalProvenance"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.supports):
            self.MissingRequiredField("supports")
        if not isinstance(self.supports, EvidenceItemSupportEnum):
            self.supports = EvidenceItemSupportEnum(self.supports)

        if self._is_empty(self.evidence_source):
            self.MissingRequiredField("evidence_source")
        if not isinstance(self.evidence_source, EvidenceSourceEnum):
            self.evidence_source = EvidenceSourceEnum(self.evidence_source)

        if self._is_empty(self.snippet):
            self.MissingRequiredField("snippet")
        if not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if self.confidence_score is not None and not isinstance(self.confidence_score, float):
            self.confidence_score = float(self.confidence_score)

        if self.computational_provenance is not None and not isinstance(
            self.computational_provenance, ComputationalProvenance
        ):
            self.computational_provenance = ComputationalProvenance(
                **as_dict(self.computational_provenance)
            )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputationalProvenance(YAMLRoot):
    """
    Provenance for a computationally derived claim — the method category, the tool chain (each with an optional
    version and citation), and the model / inputs / simulated conditions behind a prediction. Attach to an
    EvidenceItem whose evidence_source is COMPUTATIONAL (e.g. cross-feeding predicted from a genome-scale metabolic
    model under flux balance analysis).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["ComputationalProvenance"]
    class_class_curie: ClassVar[str] = "communitymech:ComputationalProvenance"
    class_name: ClassVar[str] = "ComputationalProvenance"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.ComputationalProvenance

    prediction_type: Optional[Union[str, "ComputationalPredictionTypeEnum"]] = None
    tools: Optional[
        Union[Union[dict, "ComputationalTool"], list[Union[dict, "ComputationalTool"]]]
    ] = empty_list()
    model_name: Optional[str] = None
    model_source: Optional[str] = None
    input_accession: Optional[str] = None
    simulated_medium: Optional[str] = None
    parameters: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.prediction_type is not None and not isinstance(
            self.prediction_type, ComputationalPredictionTypeEnum
        ):
            self.prediction_type = ComputationalPredictionTypeEnum(self.prediction_type)

        if not isinstance(self.tools, list):
            self.tools = [self.tools] if self.tools is not None else []
        self.tools = [
            v if isinstance(v, ComputationalTool) else ComputationalTool(**as_dict(v))
            for v in self.tools
        ]

        if self.model_name is not None and not isinstance(self.model_name, str):
            self.model_name = str(self.model_name)

        if self.model_source is not None and not isinstance(self.model_source, str):
            self.model_source = str(self.model_source)

        if self.input_accession is not None and not isinstance(self.input_accession, str):
            self.input_accession = str(self.input_accession)

        if self.simulated_medium is not None and not isinstance(self.simulated_medium, str):
            self.simulated_medium = str(self.simulated_medium)

        if self.parameters is not None and not isinstance(self.parameters, str):
            self.parameters = str(self.parameters)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputationalTool(YAMLRoot):
    """
    A single software tool used in a computational prediction, with optional version and citation.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["ComputationalTool"]
    class_class_curie: ClassVar[str] = "communitymech:ComputationalTool"
    class_name: ClassVar[str] = "ComputationalTool"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.ComputationalTool

    tool_name: str = None
    tool_version: Optional[str] = None
    tool_reference: Optional[str] = None
    role: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.tool_name):
            self.MissingRequiredField("tool_name")
        if not isinstance(self.tool_name, str):
            self.tool_name = str(self.tool_name)

        if self.tool_version is not None and not isinstance(self.tool_version, str):
            self.tool_version = str(self.tool_version)

        if self.tool_reference is not None and not isinstance(self.tool_reference, str):
            self.tool_reference = str(self.tool_reference)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonDescriptor(YAMLRoot):
    """
    Describes an organism with NCBITaxon term
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["TaxonDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:TaxonDescriptor"
    class_name: ClassVar[str] = "TaxonDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.TaxonDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    gtdb_grounding_status: Optional[Union[str, "GtdbGroundingStatusEnum"]] = None
    gtdb_candidates: Optional[Union[str, list[str]]] = empty_list()
    gtdb_classification: Optional[Union[dict, "GtdbClassification"]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.gtdb_grounding_status is not None and not isinstance(
            self.gtdb_grounding_status, GtdbGroundingStatusEnum
        ):
            self.gtdb_grounding_status = GtdbGroundingStatusEnum(self.gtdb_grounding_status)

        if not isinstance(self.gtdb_candidates, list):
            self.gtdb_candidates = (
                [self.gtdb_candidates] if self.gtdb_candidates is not None else []
            )
        self.gtdb_candidates = [v if isinstance(v, str) else str(v) for v in self.gtdb_candidates]

        if self.gtdb_classification is not None and not isinstance(
            self.gtdb_classification, GtdbClassification
        ):
            self.gtdb_classification = GtdbClassification(**as_dict(self.gtdb_classification))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GtdbClassification(YAMLRoot):
    """
    GTDB grounding for a taxon: the canonical GTDB CURIE, its taxon name and full lineage, the NCBITaxon id it was
    mapped from, and the mapping confidence. GTDB CURIEs follow the kg-microbe / Bioregistry scheme
    (GTDB:<rank>__<name-with-underscores>, e.g. GTDB:s__Bacillus_velezensis) and resolve at
    https://gtdb.ecogenomic.org/tree?r={id}. GTDB names are only best-effort stable across releases, so mapping_source
    records the release/provenance. Not an OAK-validated ontology term (no id↔label gate).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["GtdbClassification"]
    class_class_curie: ClassVar[str] = "communitymech:GtdbClassification"
    class_name: ClassVar[str] = "GtdbClassification"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.GtdbClassification

    gtdb_id: Optional[str] = None
    gtdb_taxon: Optional[str] = None
    gtdb_lineage: Optional[str] = None
    ncbi_source_id: Optional[str] = None
    majority_fraction: Optional[float] = None
    support_genomes: Optional[int] = None
    total_genomes: Optional[int] = None
    is_reclassified: Optional[Union[bool, Bool]] = None
    mapping_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.gtdb_id is not None and not isinstance(self.gtdb_id, str):
            self.gtdb_id = str(self.gtdb_id)

        if self.gtdb_taxon is not None and not isinstance(self.gtdb_taxon, str):
            self.gtdb_taxon = str(self.gtdb_taxon)

        if self.gtdb_lineage is not None and not isinstance(self.gtdb_lineage, str):
            self.gtdb_lineage = str(self.gtdb_lineage)

        if self.ncbi_source_id is not None and not isinstance(self.ncbi_source_id, str):
            self.ncbi_source_id = str(self.ncbi_source_id)

        if self.majority_fraction is not None and not isinstance(self.majority_fraction, float):
            self.majority_fraction = float(self.majority_fraction)

        if self.support_genomes is not None and not isinstance(self.support_genomes, int):
            self.support_genomes = int(self.support_genomes)

        if self.total_genomes is not None and not isinstance(self.total_genomes, int):
            self.total_genomes = int(self.total_genomes)

        if self.is_reclassified is not None and not isinstance(self.is_reclassified, Bool):
            self.is_reclassified = Bool(self.is_reclassified)

        if self.mapping_source is not None and not isinstance(self.mapping_source, str):
            self.mapping_source = str(self.mapping_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetaboliteDescriptor(YAMLRoot):
    """
    Describes a metabolite with CHEBI term
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["MetaboliteDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:MetaboliteDescriptor"
    class_name: ClassVar[str] = "MetaboliteDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.MetaboliteDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    concentration: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.concentration is not None and not isinstance(self.concentration, str):
            self.concentration = str(self.concentration)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcessDescriptor(YAMLRoot):
    """
    Describes a biological process with GO term
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["BiologicalProcessDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:BiologicalProcessDescriptor"
    class_name: ClassVar[str] = "BiologicalProcessDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.BiologicalProcessDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentDescriptor(YAMLRoot):
    """
    Describes an environment with ENVO term
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EnvironmentDescriptor"]
    class_class_curie: ClassVar[str] = "communitymech:EnvironmentDescriptor"
    class_name: ClassVar[str] = "EnvironmentDescriptor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EnvironmentDescriptor

    preferred_term: str = None
    term: Union[dict, Term] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self._is_empty(self.term):
            self.MissingRequiredField("term")
        if not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CultureCollectionID(YAMLRoot):
    """
    A culture collection identifier with accession number
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["CultureCollectionID"]
    class_class_curie: ClassVar[str] = "communitymech:CultureCollectionID"
    class_name: ClassVar[str] = "CultureCollectionID"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.CultureCollectionID

    collection: Union[str, "CultureCollectionEnum"] = None
    accession: str = None
    url: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.collection):
            self.MissingRequiredField("collection")
        if not isinstance(self.collection, CultureCollectionEnum):
            self.collection = CultureCollectionEnum(self.collection)

        if self._is_empty(self.accession):
            self.MissingRequiredField("accession")
        if not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StrainDesignation(YAMLRoot):
    """
    Detailed strain-level information for reproducibility
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["StrainDesignation"]
    class_class_curie: ClassVar[str] = "communitymech:StrainDesignation"
    class_name: ClassVar[str] = "StrainDesignation"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.StrainDesignation

    strain_name: Optional[str] = None
    culture_collections: Optional[
        Union[Union[dict, CultureCollectionID], list[Union[dict, CultureCollectionID]]]
    ] = empty_list()
    type_strain: Optional[Union[bool, Bool]] = None
    genome_accession: Optional[str] = None
    genome_url: Optional[str] = None
    genetic_modification: Optional[str] = None
    isolation_source: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.strain_name is not None and not isinstance(self.strain_name, str):
            self.strain_name = str(self.strain_name)

        self._normalize_inlined_as_dict(
            slot_name="culture_collections",
            slot_type=CultureCollectionID,
            key_name="collection",
            keyed=False,
        )

        if self.type_strain is not None and not isinstance(self.type_strain, Bool):
            self.type_strain = Bool(self.type_strain)

        if self.genome_accession is not None and not isinstance(self.genome_accession, str):
            self.genome_accession = str(self.genome_accession)

        if self.genome_url is not None and not isinstance(self.genome_url, str):
            self.genome_url = str(self.genome_url)

        if self.genetic_modification is not None and not isinstance(self.genetic_modification, str):
            self.genetic_modification = str(self.genetic_modification)

        if self.isolation_source is not None and not isinstance(self.isolation_source, str):
            self.isolation_source = str(self.isolation_source)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomicComposition(YAMLRoot):
    """
    A taxon present in the community with abundance and role
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["TaxonomicComposition"]
    class_class_curie: ClassVar[str] = "communitymech:TaxonomicComposition"
    class_name: ClassVar[str] = "TaxonomicComposition"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.TaxonomicComposition

    taxon_term: Union[dict, TaxonDescriptor] = None
    strain_designation: Optional[Union[dict, StrainDesignation]] = None
    abundance_level: Optional[Union[str, "AbundanceEnum"]] = None
    abundance_value: Optional[str] = None
    absolute_abundance: Optional[float] = None
    absolute_abundance_unit: Optional[str] = None
    relative_abundance: Optional[float] = None
    relative_abundance_unit: Optional[str] = None
    common_taxon: Optional[str] = None
    functional_role: Optional[
        Union[Union[str, "FunctionalRoleEnum"], list[Union[str, "FunctionalRoleEnum"]]]
    ] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxon_term):
            self.MissingRequiredField("taxon_term")
        if not isinstance(self.taxon_term, TaxonDescriptor):
            self.taxon_term = TaxonDescriptor(**as_dict(self.taxon_term))

        if self.strain_designation is not None and not isinstance(
            self.strain_designation, StrainDesignation
        ):
            self.strain_designation = StrainDesignation(**as_dict(self.strain_designation))

        if self.abundance_level is not None and not isinstance(self.abundance_level, AbundanceEnum):
            self.abundance_level = AbundanceEnum(self.abundance_level)

        if self.abundance_value is not None and not isinstance(self.abundance_value, str):
            self.abundance_value = str(self.abundance_value)

        if self.absolute_abundance is not None and not isinstance(self.absolute_abundance, float):
            self.absolute_abundance = float(self.absolute_abundance)

        if self.absolute_abundance_unit is not None and not isinstance(
            self.absolute_abundance_unit, str
        ):
            self.absolute_abundance_unit = str(self.absolute_abundance_unit)

        if self.relative_abundance is not None and not isinstance(self.relative_abundance, float):
            self.relative_abundance = float(self.relative_abundance)

        if self.relative_abundance_unit is not None and not isinstance(
            self.relative_abundance_unit, str
        ):
            self.relative_abundance_unit = str(self.relative_abundance_unit)

        if self.common_taxon is not None and not isinstance(self.common_taxon, str):
            self.common_taxon = str(self.common_taxon)

        if not isinstance(self.functional_role, list):
            self.functional_role = (
                [self.functional_role] if self.functional_role is not None else []
            )
        self.functional_role = [
            v if isinstance(v, FunctionalRoleEnum) else FunctionalRoleEnum(v)
            for v in self.functional_role
        ]

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InteractionDownstream(YAMLRoot):
    """
    A downstream target in a causal interaction graph
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["InteractionDownstream"]
    class_class_curie: ClassVar[str] = "communitymech:InteractionDownstream"
    class_name: ClassVar[str] = "InteractionDownstream"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.InteractionDownstream

    target: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EcologicalInteraction(YAMLRoot):
    """
    An interaction between organisms or metabolic processes
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EcologicalInteraction"]
    class_class_curie: ClassVar[str] = "communitymech:EcologicalInteraction"
    class_name: ClassVar[str] = "EcologicalInteraction"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EcologicalInteraction

    name: str = None
    description: Optional[str] = None
    interaction_type: Optional[Union[str, "InteractionTypeEnum"]] = None
    scope: Optional[Union[str, "InteractionScopeEnum"]] = "PAIRWISE"
    source_taxon: Optional[Union[dict, TaxonDescriptor]] = None
    target_taxon: Optional[Union[dict, TaxonDescriptor]] = None
    metabolites: Optional[
        Union[Union[dict, MetaboliteDescriptor], list[Union[dict, MetaboliteDescriptor]]]
    ] = empty_list()
    biological_processes: Optional[
        Union[
            Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]
        ]
    ] = empty_list()
    downstream: Optional[
        Union[Union[dict, InteractionDownstream], list[Union[dict, InteractionDownstream]]]
    ] = empty_list()
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.interaction_type is not None and not isinstance(
            self.interaction_type, InteractionTypeEnum
        ):
            self.interaction_type = InteractionTypeEnum(self.interaction_type)

        if self.scope is not None and not isinstance(self.scope, InteractionScopeEnum):
            self.scope = getattr(InteractionScopeEnum, self.scope)

        if self.source_taxon is not None and not isinstance(self.source_taxon, TaxonDescriptor):
            self.source_taxon = TaxonDescriptor(**as_dict(self.source_taxon))

        if self.target_taxon is not None and not isinstance(self.target_taxon, TaxonDescriptor):
            self.target_taxon = TaxonDescriptor(**as_dict(self.target_taxon))

        self._normalize_inlined_as_dict(
            slot_name="metabolites",
            slot_type=MetaboliteDescriptor,
            key_name="preferred_term",
            keyed=False,
        )

        self._normalize_inlined_as_dict(
            slot_name="biological_processes",
            slot_type=BiologicalProcessDescriptor,
            key_name="preferred_term",
            keyed=False,
        )

        self._normalize_inlined_as_dict(
            slot_name="downstream", slot_type=InteractionDownstream, key_name="target", keyed=False
        )

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalFactor(YAMLRoot):
    """
    An environmental condition or parameter
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["EnvironmentalFactor"]
    class_class_curie: ClassVar[str] = "communitymech:EnvironmentalFactor"
    class_name: ClassVar[str] = "EnvironmentalFactor"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.EnvironmentalFactor

    name: str = None
    value: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GrowthMediaComponent(YAMLRoot):
    """
    A component of growth media (nutrient, salt, buffer, etc.)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["GrowthMediaComponent"]
    class_class_curie: ClassVar[str] = "communitymech:GrowthMediaComponent"
    class_name: ClassVar[str] = "GrowthMediaComponent"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.GrowthMediaComponent

    name: str = None
    media_ingredient_mech_id: Optional[str] = None
    media_ingredient_mech_url: Optional[str] = None
    concentration: Optional[str] = None
    unit: Optional[str] = None
    chebi_term: Optional[Union[dict, MetaboliteDescriptor]] = None
    from_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.media_ingredient_mech_id is not None and not isinstance(
            self.media_ingredient_mech_id, str
        ):
            self.media_ingredient_mech_id = str(self.media_ingredient_mech_id)

        if self.media_ingredient_mech_url is not None and not isinstance(
            self.media_ingredient_mech_url, str
        ):
            self.media_ingredient_mech_url = str(self.media_ingredient_mech_url)

        if self.concentration is not None and not isinstance(self.concentration, str):
            self.concentration = str(self.concentration)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.chebi_term is not None and not isinstance(self.chebi_term, MetaboliteDescriptor):
            self.chebi_term = MetaboliteDescriptor(**as_dict(self.chebi_term))

        if self.from_source is not None and not isinstance(self.from_source, str):
            self.from_source = str(self.from_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GrowthMedia(YAMLRoot):
    """
    Growth media used for cultivation of the community or its members
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["GrowthMedia"]
    class_class_curie: ClassVar[str] = "communitymech:GrowthMedia"
    class_name: ClassVar[str] = "GrowthMedia"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.GrowthMedia

    name: str = None
    culturemech_id: Optional[str] = None
    culturemech_url: Optional[str] = None
    composition: Optional[
        Union[Union[dict, GrowthMediaComponent], list[Union[dict, GrowthMediaComponent]]]
    ] = empty_list()
    ph: Optional[str] = None
    ph_range: Optional[str] = None
    temperature: Optional[str] = None
    temperature_unit: Optional[str] = None
    temperature_range: Optional[str] = None
    atmosphere: Optional[Union[str, "AtmosphereEnum"]] = None
    headspace_gas: Optional[str] = None
    salinity: Optional[str] = None
    salinity_unit: Optional[str] = None
    pressure: Optional[str] = None
    pressure_unit: Optional[str] = None
    light_regime: Optional[str] = None
    light_intensity: Optional[str] = None
    light_intensity_unit: Optional[str] = None
    redox_potential: Optional[str] = None
    redox_potential_unit: Optional[str] = None
    inoculum_source: Optional[str] = None
    inoculum_size: Optional[str] = None
    inoculum_unit: Optional[str] = None
    incubation_time: Optional[str] = None
    incubation_time_unit: Optional[str] = None
    shaking_speed: Optional[str] = None
    shaking_speed_unit: Optional[str] = None
    vessel_type: Optional[str] = None
    preparation_notes: Optional[str] = None
    protocol_url: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.culturemech_id is not None and not isinstance(self.culturemech_id, str):
            self.culturemech_id = str(self.culturemech_id)

        if self.culturemech_url is not None and not isinstance(self.culturemech_url, str):
            self.culturemech_url = str(self.culturemech_url)

        self._normalize_inlined_as_dict(
            slot_name="composition", slot_type=GrowthMediaComponent, key_name="name", keyed=False
        )

        if self.ph is not None and not isinstance(self.ph, str):
            self.ph = str(self.ph)

        if self.ph_range is not None and not isinstance(self.ph_range, str):
            self.ph_range = str(self.ph_range)

        if self.temperature is not None and not isinstance(self.temperature, str):
            self.temperature = str(self.temperature)

        if self.temperature_unit is not None and not isinstance(self.temperature_unit, str):
            self.temperature_unit = str(self.temperature_unit)

        if self.temperature_range is not None and not isinstance(self.temperature_range, str):
            self.temperature_range = str(self.temperature_range)

        if self.atmosphere is not None and not isinstance(self.atmosphere, AtmosphereEnum):
            self.atmosphere = AtmosphereEnum(self.atmosphere)

        if self.headspace_gas is not None and not isinstance(self.headspace_gas, str):
            self.headspace_gas = str(self.headspace_gas)

        if self.salinity is not None and not isinstance(self.salinity, str):
            self.salinity = str(self.salinity)

        if self.salinity_unit is not None and not isinstance(self.salinity_unit, str):
            self.salinity_unit = str(self.salinity_unit)

        if self.pressure is not None and not isinstance(self.pressure, str):
            self.pressure = str(self.pressure)

        if self.pressure_unit is not None and not isinstance(self.pressure_unit, str):
            self.pressure_unit = str(self.pressure_unit)

        if self.light_regime is not None and not isinstance(self.light_regime, str):
            self.light_regime = str(self.light_regime)

        if self.light_intensity is not None and not isinstance(self.light_intensity, str):
            self.light_intensity = str(self.light_intensity)

        if self.light_intensity_unit is not None and not isinstance(self.light_intensity_unit, str):
            self.light_intensity_unit = str(self.light_intensity_unit)

        if self.redox_potential is not None and not isinstance(self.redox_potential, str):
            self.redox_potential = str(self.redox_potential)

        if self.redox_potential_unit is not None and not isinstance(self.redox_potential_unit, str):
            self.redox_potential_unit = str(self.redox_potential_unit)

        if self.inoculum_source is not None and not isinstance(self.inoculum_source, str):
            self.inoculum_source = str(self.inoculum_source)

        if self.inoculum_size is not None and not isinstance(self.inoculum_size, str):
            self.inoculum_size = str(self.inoculum_size)

        if self.inoculum_unit is not None and not isinstance(self.inoculum_unit, str):
            self.inoculum_unit = str(self.inoculum_unit)

        if self.incubation_time is not None and not isinstance(self.incubation_time, str):
            self.incubation_time = str(self.incubation_time)

        if self.incubation_time_unit is not None and not isinstance(self.incubation_time_unit, str):
            self.incubation_time_unit = str(self.incubation_time_unit)

        if self.shaking_speed is not None and not isinstance(self.shaking_speed, str):
            self.shaking_speed = str(self.shaking_speed)

        if self.shaking_speed_unit is not None and not isinstance(self.shaking_speed_unit, str):
            self.shaking_speed_unit = str(self.shaking_speed_unit)

        if self.vessel_type is not None and not isinstance(self.vessel_type, str):
            self.vessel_type = str(self.vessel_type)

        if self.preparation_notes is not None and not isinstance(self.preparation_notes, str):
            self.preparation_notes = str(self.preparation_notes)

        if self.protocol_url is not None and not isinstance(self.protocol_url, str):
            self.protocol_url = str(self.protocol_url)

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedMedia(YAMLRoot):
    """
    A CultureMech medium relevant to this community through shared environment, organism overlap, or study context.
    Complements GrowthMedia (which captures media actually used for cultivation) by enabling environment-based
    discovery of potentially useful media across the CultureMech repository.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["RelatedMedia"]
    class_class_curie: ClassVar[str] = "communitymech:RelatedMedia"
    class_name: ClassVar[str] = "RelatedMedia"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.RelatedMedia

    preferred_term: str = None
    culturemech_id: Optional[str] = None
    relationship_type: Optional[Union[str, "MediaRelationshipEnum"]] = None
    shared_environment_term: Optional[Union[dict, Term]] = None
    relevance_notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.culturemech_id is not None and not isinstance(self.culturemech_id, str):
            self.culturemech_id = str(self.culturemech_id)

        if self.relationship_type is not None and not isinstance(
            self.relationship_type, MediaRelationshipEnum
        ):
            self.relationship_type = MediaRelationshipEnum(self.relationship_type)

        if self.shared_environment_term is not None and not isinstance(
            self.shared_environment_term, Term
        ):
            self.shared_environment_term = Term(**as_dict(self.shared_environment_term))

        if self.relevance_notes is not None and not isinstance(self.relevance_notes, str):
            self.relevance_notes = str(self.relevance_notes)

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedIngredient(YAMLRoot):
    """
    A MediaIngredientMech ingredient relevant to this community's environment or metabolism. Complements
    GrowthMediaComponent (which captures ingredients in actual cultivation media) by linking to environmentally
    significant compounds that may not be in any currently used medium.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["RelatedIngredient"]
    class_class_curie: ClassVar[str] = "communitymech:RelatedIngredient"
    class_name: ClassVar[str] = "RelatedIngredient"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.RelatedIngredient

    preferred_term: str = None
    mediaingredientmech_id: Optional[str] = None
    chebi_term: Optional[Union[dict, Term]] = None
    shared_environment_term: Optional[Union[dict, Term]] = None
    relevance: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_term):
            self.MissingRequiredField("preferred_term")
        if not isinstance(self.preferred_term, str):
            self.preferred_term = str(self.preferred_term)

        if self.mediaingredientmech_id is not None and not isinstance(
            self.mediaingredientmech_id, str
        ):
            self.mediaingredientmech_id = str(self.mediaingredientmech_id)

        if self.chebi_term is not None and not isinstance(self.chebi_term, Term):
            self.chebi_term = Term(**as_dict(self.chebi_term))

        if self.shared_environment_term is not None and not isinstance(
            self.shared_environment_term, Term
        ):
            self.shared_environment_term = Term(**as_dict(self.shared_environment_term))

        if self.relevance is not None and not isinstance(self.relevance, str):
            self.relevance = str(self.relevance)

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalResource(YAMLRoot):
    """
    An external model or narrative resource linked to the community
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["ExternalResource"]
    class_class_curie: ClassVar[str] = "communitymech:ExternalResource"
    class_name: ClassVar[str] = "ExternalResource"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.ExternalResource

    name: str = None
    repository: Union[str, "ExternalResourceRepositoryEnum"] = None
    resource_id: str = None
    url: str = None
    description: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.repository):
            self.MissingRequiredField("repository")
        if not isinstance(self.repository, ExternalResourceRepositoryEnum):
            self.repository = ExternalResourceRepositoryEnum(self.repository)

        if self._is_empty(self.resource_id):
            self.MissingRequiredField("resource_id")
        if not isinstance(self.resource_id, str):
            self.resource_id = str(self.resource_id)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunityEngineeringDesign(YAMLRoot):
    """
    Design intent and implementation details for engineered or synthetic communities
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["CommunityEngineeringDesign"]
    class_class_curie: ClassVar[str] = "communitymech:CommunityEngineeringDesign"
    class_name: ClassVar[str] = "CommunityEngineeringDesign"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.CommunityEngineeringDesign

    objective: Optional[str] = None
    assembly_strategy: Optional[str] = None
    inoculation_strategy: Optional[str] = None
    passaging_regimen: Optional[str] = None
    perturbation_design: Optional[str] = None
    measurement_endpoints: Optional[Union[str, list[str]]] = empty_list()
    protocol_url: Optional[str] = None
    notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        if self.assembly_strategy is not None and not isinstance(self.assembly_strategy, str):
            self.assembly_strategy = str(self.assembly_strategy)

        if self.inoculation_strategy is not None and not isinstance(self.inoculation_strategy, str):
            self.inoculation_strategy = str(self.inoculation_strategy)

        if self.passaging_regimen is not None and not isinstance(self.passaging_regimen, str):
            self.passaging_regimen = str(self.passaging_regimen)

        if self.perturbation_design is not None and not isinstance(self.perturbation_design, str):
            self.perturbation_design = str(self.perturbation_design)

        if not isinstance(self.measurement_endpoints, list):
            self.measurement_endpoints = (
                [self.measurement_endpoints] if self.measurement_endpoints is not None else []
            )
        self.measurement_endpoints = [
            v if isinstance(v, str) else str(v) for v in self.measurement_endpoints
        ]

        if self.protocol_url is not None and not isinstance(self.protocol_url, str):
            self.protocol_url = str(self.protocol_url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CultivationSetup(YAMLRoot):
    """
    Hardware/instrumentation and cultivation mode used to grow or sustain the community. Optional — not all
    communities have a defined setup. Captures both the system (e.g. stirred-tank bioreactor, photobioreactor,
    microbial fuel cell) and the operating approach (batch, fed-batch, continuous, …). Complements GrowthMedia (medium
    composition/conditions); the controlled cultivation_mode/system_type values are the preferred standardized home
    for vessel/reactor information going forward (vs the legacy free-text GrowthMedia.vessel_type).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["CultivationSetup"]
    class_class_curie: ClassVar[str] = "communitymech:CultivationSetup"
    class_name: ClassVar[str] = "CultivationSetup"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.CultivationSetup

    cultivation_mode: Optional[Union[str, "CultivationModeEnum"]] = None
    system_type: Optional[Union[str, "CultivationSystemEnum"]] = None
    instrument_detail: Optional[str] = None
    manufacturer_model: Optional[str] = None
    working_volume: Optional[float] = None
    working_volume_unit: Optional[str] = None
    operating_temperature: Optional[float] = None
    operating_temperature_unit: Optional[str] = None
    feed_or_dilution_rate: Optional[float] = None
    feed_or_dilution_rate_unit: Optional[str] = None
    retention_time: Optional[float] = None
    retention_time_unit: Optional[str] = None
    retention_time_type: Optional[str] = None
    applied_potential: Optional[float] = None
    applied_potential_unit: Optional[str] = None
    electrode_detail: Optional[str] = None
    ph_controlled: Optional[Union[bool, Bool]] = None
    do_controlled: Optional[Union[bool, Bool]] = None
    temperature_controlled: Optional[Union[bool, Bool]] = None
    controls_notes: Optional[str] = None
    protocol_url: Optional[str] = None
    notes: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cultivation_mode is not None and not isinstance(
            self.cultivation_mode, CultivationModeEnum
        ):
            self.cultivation_mode = CultivationModeEnum(self.cultivation_mode)

        if self.system_type is not None and not isinstance(self.system_type, CultivationSystemEnum):
            self.system_type = CultivationSystemEnum(self.system_type)

        if self.instrument_detail is not None and not isinstance(self.instrument_detail, str):
            self.instrument_detail = str(self.instrument_detail)

        if self.manufacturer_model is not None and not isinstance(self.manufacturer_model, str):
            self.manufacturer_model = str(self.manufacturer_model)

        if self.working_volume is not None and not isinstance(self.working_volume, float):
            self.working_volume = float(self.working_volume)

        if self.working_volume_unit is not None and not isinstance(self.working_volume_unit, str):
            self.working_volume_unit = str(self.working_volume_unit)

        if self.operating_temperature is not None and not isinstance(
            self.operating_temperature, float
        ):
            self.operating_temperature = float(self.operating_temperature)

        if self.operating_temperature_unit is not None and not isinstance(
            self.operating_temperature_unit, str
        ):
            self.operating_temperature_unit = str(self.operating_temperature_unit)

        if self.feed_or_dilution_rate is not None and not isinstance(
            self.feed_or_dilution_rate, float
        ):
            self.feed_or_dilution_rate = float(self.feed_or_dilution_rate)

        if self.feed_or_dilution_rate_unit is not None and not isinstance(
            self.feed_or_dilution_rate_unit, str
        ):
            self.feed_or_dilution_rate_unit = str(self.feed_or_dilution_rate_unit)

        if self.retention_time is not None and not isinstance(self.retention_time, float):
            self.retention_time = float(self.retention_time)

        if self.retention_time_unit is not None and not isinstance(self.retention_time_unit, str):
            self.retention_time_unit = str(self.retention_time_unit)

        if self.retention_time_type is not None and not isinstance(self.retention_time_type, str):
            self.retention_time_type = str(self.retention_time_type)

        if self.applied_potential is not None and not isinstance(self.applied_potential, float):
            self.applied_potential = float(self.applied_potential)

        if self.applied_potential_unit is not None and not isinstance(
            self.applied_potential_unit, str
        ):
            self.applied_potential_unit = str(self.applied_potential_unit)

        if self.electrode_detail is not None and not isinstance(self.electrode_detail, str):
            self.electrode_detail = str(self.electrode_detail)

        if self.ph_controlled is not None and not isinstance(self.ph_controlled, Bool):
            self.ph_controlled = Bool(self.ph_controlled)

        if self.do_controlled is not None and not isinstance(self.do_controlled, Bool):
            self.do_controlled = Bool(self.do_controlled)

        if self.temperature_controlled is not None and not isinstance(
            self.temperature_controlled, Bool
        ):
            self.temperature_controlled = Bool(self.temperature_controlled)

        if self.controls_notes is not None and not isinstance(self.controls_notes, str):
            self.controls_notes = str(self.controls_notes)

        if self.protocol_url is not None and not isinstance(self.protocol_url, str):
            self.protocol_url = str(self.protocol_url)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(
            slot_name="evidence", slot_type=EvidenceItem, key_name="reference", keyed=False
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrobialCommunity(YAMLRoot):
    """
    A microbial community with composition and interactions
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["MicrobialCommunity"]
    class_class_curie: ClassVar[str] = "communitymech:MicrobialCommunity"
    class_name: ClassVar[str] = "MicrobialCommunity"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.MicrobialCommunity

    id: Union[str, MicrobialCommunityId] = None
    name: str = None
    description: Optional[str] = None
    ecological_state: Optional[Union[str, "EcologicalStateEnum"]] = None
    community_origin: Optional[Union[str, "CommunityOriginEnum"]] = None
    community_category: Optional[Union[str, "CommunityCategoryEnum"]] = None
    engineering_design: Optional[Union[dict, CommunityEngineeringDesign]] = None
    environment_term: Optional[Union[dict, EnvironmentDescriptor]] = None
    modeled_environment: Optional[
        Union[Union[dict, EnvironmentDescriptor], list[Union[dict, EnvironmentDescriptor]]]
    ] = empty_list()
    taxonomy: Optional[
        Union[Union[dict, TaxonomicComposition], list[Union[dict, TaxonomicComposition]]]
    ] = empty_list()
    ecological_interactions: Optional[
        Union[Union[dict, EcologicalInteraction], list[Union[dict, EcologicalInteraction]]]
    ] = empty_list()
    environmental_factors: Optional[
        Union[Union[dict, EnvironmentalFactor], list[Union[dict, EnvironmentalFactor]]]
    ] = empty_list()
    growth_media: Optional[Union[Union[dict, GrowthMedia], list[Union[dict, GrowthMedia]]]] = (
        empty_list()
    )
    cultivation_setup: Optional[
        Union[Union[dict, CultivationSetup], list[Union[dict, CultivationSetup]]]
    ] = empty_list()
    related_media: Optional[Union[Union[dict, RelatedMedia], list[Union[dict, RelatedMedia]]]] = (
        empty_list()
    )
    related_ingredients: Optional[
        Union[Union[dict, RelatedIngredient], list[Union[dict, RelatedIngredient]]]
    ] = empty_list()
    associated_datasets: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = (
        empty_list()
    )
    external_resources: Optional[
        Union[Union[dict, ExternalResource], list[Union[dict, ExternalResource]]]
    ] = empty_list()
    metals_present: Optional[
        Union[Union[str, "MetalElementEnum"], list[Union[str, "MetalElementEnum"]]]
    ] = empty_list()
    rare_earth_elements_present: Optional[
        Union[Union[str, "RareEarthElementEnum"], list[Union[str, "RareEarthElementEnum"]]]
    ] = empty_list()
    metal_relevance: Optional[Union[str, "MetalRelevanceEnum"]] = None
    metal_notes: Optional[str] = None
    discussions: Optional[Union[Union[dict, "Discussion"], list[Union[dict, "Discussion"]]]] = (
        empty_list()
    )
    curation_history: Optional[
        Union[Union[dict, "CurationEvent"], list[Union[dict, "CurationEvent"]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicrobialCommunityId):
            self.id = MicrobialCommunityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ecological_state is not None and not isinstance(
            self.ecological_state, EcologicalStateEnum
        ):
            self.ecological_state = EcologicalStateEnum(self.ecological_state)

        if self.community_origin is not None and not isinstance(
            self.community_origin, CommunityOriginEnum
        ):
            self.community_origin = CommunityOriginEnum(self.community_origin)

        if self.community_category is not None and not isinstance(
            self.community_category, CommunityCategoryEnum
        ):
            self.community_category = CommunityCategoryEnum(self.community_category)

        if self.engineering_design is not None and not isinstance(
            self.engineering_design, CommunityEngineeringDesign
        ):
            self.engineering_design = CommunityEngineeringDesign(**as_dict(self.engineering_design))

        if self.environment_term is not None and not isinstance(
            self.environment_term, EnvironmentDescriptor
        ):
            self.environment_term = EnvironmentDescriptor(**as_dict(self.environment_term))

        if not isinstance(self.modeled_environment, list):
            self.modeled_environment = (
                [self.modeled_environment] if self.modeled_environment is not None else []
            )
        self.modeled_environment = [
            v if isinstance(v, EnvironmentDescriptor) else EnvironmentDescriptor(**as_dict(v))
            for v in self.modeled_environment
        ]

        self._normalize_inlined_as_dict(
            slot_name="taxonomy", slot_type=TaxonomicComposition, key_name="taxon_term", keyed=False
        )

        self._normalize_inlined_as_dict(
            slot_name="ecological_interactions",
            slot_type=EcologicalInteraction,
            key_name="name",
            keyed=False,
        )

        self._normalize_inlined_as_dict(
            slot_name="environmental_factors",
            slot_type=EnvironmentalFactor,
            key_name="name",
            keyed=False,
        )

        self._normalize_inlined_as_dict(
            slot_name="growth_media", slot_type=GrowthMedia, key_name="name", keyed=False
        )

        if not isinstance(self.cultivation_setup, list):
            self.cultivation_setup = (
                [self.cultivation_setup] if self.cultivation_setup is not None else []
            )
        self.cultivation_setup = [
            v if isinstance(v, CultivationSetup) else CultivationSetup(**as_dict(v))
            for v in self.cultivation_setup
        ]

        if not isinstance(self.related_media, list):
            self.related_media = [self.related_media] if self.related_media is not None else []
        self.related_media = [
            v if isinstance(v, RelatedMedia) else RelatedMedia(**as_dict(v))
            for v in self.related_media
        ]

        if not isinstance(self.related_ingredients, list):
            self.related_ingredients = (
                [self.related_ingredients] if self.related_ingredients is not None else []
            )
        self.related_ingredients = [
            v if isinstance(v, RelatedIngredient) else RelatedIngredient(**as_dict(v))
            for v in self.related_ingredients
        ]

        if not isinstance(self.associated_datasets, list):
            self.associated_datasets = (
                [self.associated_datasets] if self.associated_datasets is not None else []
            )
        self.associated_datasets = [
            v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.associated_datasets
        ]

        self._normalize_inlined_as_dict(
            slot_name="external_resources", slot_type=ExternalResource, key_name="name", keyed=False
        )

        if not isinstance(self.metals_present, list):
            self.metals_present = [self.metals_present] if self.metals_present is not None else []
        self.metals_present = [
            v if isinstance(v, MetalElementEnum) else MetalElementEnum(v)
            for v in self.metals_present
        ]

        if not isinstance(self.rare_earth_elements_present, list):
            self.rare_earth_elements_present = (
                [self.rare_earth_elements_present]
                if self.rare_earth_elements_present is not None
                else []
            )
        self.rare_earth_elements_present = [
            v if isinstance(v, RareEarthElementEnum) else RareEarthElementEnum(v)
            for v in self.rare_earth_elements_present
        ]

        if self.metal_relevance is not None and not isinstance(
            self.metal_relevance, MetalRelevanceEnum
        ):
            self.metal_relevance = MetalRelevanceEnum(self.metal_relevance)

        if self.metal_notes is not None and not isinstance(self.metal_notes, str):
            self.metal_notes = str(self.metal_notes)

        if not isinstance(self.discussions, list):
            self.discussions = [self.discussions] if self.discussions is not None else []
        self.discussions = [
            v if isinstance(v, Discussion) else Discussion(**as_dict(v)) for v in self.discussions
        ]

        if not isinstance(self.curation_history, list):
            self.curation_history = (
                [self.curation_history] if self.curation_history is not None else []
            )
        self.curation_history = [
            v if isinstance(v, CurationEvent) else CurationEvent(**as_dict(v))
            for v in self.curation_history
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CurationEvent(YAMLRoot):
    """
    A timestamped curator action on a MicrobialCommunity. Mirrors the shape used by sibling Mech repos (CultureMech,
    MediaIngredientMech, TraitMech) so cross-repo tooling can read curation events uniformly.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["CurationEvent"]
    class_class_curie: ClassVar[str] = "communitymech:CurationEvent"
    class_name: ClassVar[str] = "CurationEvent"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.CurationEvent

    timestamp: Union[str, XSDDateTime] = None
    curator: str = None
    action: str = None
    changes: Optional[str] = None
    llm_assisted: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, XSDDateTime):
            self.timestamp = XSDDateTime(self.timestamp)

        if self._is_empty(self.curator):
            self.MissingRequiredField("curator")
        if not isinstance(self.curator, str):
            self.curator = str(self.curator)

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, str):
            self.action = str(self.action)

        if self.changes is not None and not isinstance(self.changes, str):
            self.changes = str(self.changes)

        if self.llm_assisted is not None and not isinstance(self.llm_assisted, Bool):
            self.llm_assisted = Bool(self.llm_assisted)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommonTaxon(YAMLRoot):
    """
    A reusable taxon record: an NCBITaxon-grounded organism together with its reference genome(s) and the genes known
    to support its community role(s) or specific ecological interactions. Maintained once and referenced by many
    community records.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["CommonTaxon"]
    class_class_curie: ClassVar[str] = "communitymech:CommonTaxon"
    class_name: ClassVar[str] = "CommonTaxon"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.CommonTaxon

    id: Union[str, CommonTaxonId] = None
    taxon_term: Union[dict, TaxonDescriptor] = None
    genomes: Optional[Union[Union[dict, "GenomeRecord"], list[Union[dict, "GenomeRecord"]]]] = (
        empty_list()
    )
    genes: Optional[Union[Union[dict, "GeneAnnotation"], list[Union[dict, "GeneAnnotation"]]]] = (
        empty_list()
    )
    notes: Optional[str] = None
    curation_history: Optional[
        Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommonTaxonId):
            self.id = CommonTaxonId(self.id)

        if self._is_empty(self.taxon_term):
            self.MissingRequiredField("taxon_term")
        if not isinstance(self.taxon_term, TaxonDescriptor):
            self.taxon_term = TaxonDescriptor(**as_dict(self.taxon_term))

        if not isinstance(self.genomes, list):
            self.genomes = [self.genomes] if self.genomes is not None else []
        self.genomes = [
            v if isinstance(v, GenomeRecord) else GenomeRecord(**as_dict(v)) for v in self.genomes
        ]

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [
            v if isinstance(v, GeneAnnotation) else GeneAnnotation(**as_dict(v)) for v in self.genes
        ]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.curation_history, list):
            self.curation_history = (
                [self.curation_history] if self.curation_history is not None else []
            )
        self.curation_history = [
            v if isinstance(v, CurationEvent) else CurationEvent(**as_dict(v))
            for v in self.curation_history
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenomeRecord(YAMLRoot):
    """
    A reference genome assembly for a taxon.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["GenomeRecord"]
    class_class_curie: ClassVar[str] = "communitymech:GenomeRecord"
    class_name: ClassVar[str] = "GenomeRecord"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.GenomeRecord

    id: str = None
    label: Optional[str] = None
    strain_designation: Optional[Union[dict, StrainDesignation]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.strain_designation is not None and not isinstance(
            self.strain_designation, StrainDesignation
        ):
            self.strain_designation = StrainDesignation(**as_dict(self.strain_designation))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneAnnotation(YAMLRoot):
    """
    A gene that supports a taxon's community role or a specific ecological interaction, with standardized identifiers
    and supporting evidence.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COMMUNITYMECH["GeneAnnotation"]
    class_class_curie: ClassVar[str] = "communitymech:GeneAnnotation"
    class_name: ClassVar[str] = "GeneAnnotation"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.GeneAnnotation

    gene_id: str = None
    gene_symbol: Optional[str] = None
    locus_tag: Optional[str] = None
    product: Optional[str] = None
    genome: Optional[str] = None
    kegg_ortholog: Optional[str] = None
    go_terms: Optional[Union[Union[dict, Term], list[Union[dict, Term]]]] = empty_list()
    supports_roles: Optional[
        Union[Union[str, "FunctionalRoleEnum"], list[Union[str, "FunctionalRoleEnum"]]]
    ] = empty_list()
    supports_interaction: Optional[str] = None
    evidence: Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gene_id):
            self.MissingRequiredField("gene_id")
        if not isinstance(self.gene_id, str):
            self.gene_id = str(self.gene_id)

        if self.gene_symbol is not None and not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self.locus_tag is not None and not isinstance(self.locus_tag, str):
            self.locus_tag = str(self.locus_tag)

        if self.product is not None and not isinstance(self.product, str):
            self.product = str(self.product)

        if self.genome is not None and not isinstance(self.genome, str):
            self.genome = str(self.genome)

        if self.kegg_ortholog is not None and not isinstance(self.kegg_ortholog, str):
            self.kegg_ortholog = str(self.kegg_ortholog)

        if not isinstance(self.go_terms, list):
            self.go_terms = [self.go_terms] if self.go_terms is not None else []
        self.go_terms = [v if isinstance(v, Term) else Term(**as_dict(v)) for v in self.go_terms]

        if not isinstance(self.supports_roles, list):
            self.supports_roles = [self.supports_roles] if self.supports_roles is not None else []
        self.supports_roles = [
            v if isinstance(v, FunctionalRoleEnum) else FunctionalRoleEnum(v)
            for v in self.supports_roles
        ]

        if self.supports_interaction is not None and not isinstance(self.supports_interaction, str):
            self.supports_interaction = str(self.supports_interaction)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [
            v if isinstance(v, EvidenceItem) else EvidenceItem(**as_dict(v)) for v in self.evidence
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingReference(YAMLRoot):
    """
    A lightweight literature/database citation supporting a Discussion or Dataset. Self-contained (so this module has
    no dependency on each repo's EvidenceItem); carries a verbatim `snippet` so the same anti-hallucination
    snippet-vs-cached-abstract check the Mechs already run can validate it.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["SupportingReference"]
    class_class_curie: ClassVar[str] = "mech_shared:SupportingReference"
    class_name: ClassVar[str] = "SupportingReference"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.SupportingReference

    reference: str = None
    reference_title: Optional[str] = None
    supports: Optional[Union[str, "SupportLevelEnum"]] = None
    evidence_source: Optional[str] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self.reference_title is not None and not isinstance(self.reference_title, str):
            self.reference_title = str(self.reference_title)

        if self.supports is not None and not isinstance(self.supports, SupportLevelEnum):
            self.supports = SupportLevelEnum(self.supports)

        if self.evidence_source is not None and not isinstance(self.evidence_source, str):
            self.evidence_source = str(self.evidence_source)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Discussion(YAMLRoot):
    """
    A thread-like record of an open question, controversy, curation todo, emerging hypothesis, knowledge gap, or
    interpretation debate attached to a record or one of its sub-objects. Captures the discourse / knowledge-gap layer
    of curation. External thread links (GitHub issues, forum posts) are cited via the `evidence` block, not a separate
    slot.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["Discussion"]
    class_class_curie: ClassVar[str] = "mech_shared:Discussion"
    class_name: ClassVar[str] = "Discussion"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.Discussion

    discussion_id: str = None
    prompt: str = None
    kind: Optional[Union[str, "DiscussionKindEnum"]] = None
    status: Optional[Union[str, "DiscussionStatusEnum"]] = None
    attaches_to: Optional[Union[str, list[str]]] = empty_list()
    rationale: Optional[str] = None
    proposed_experiments: Optional[
        Union[Union[dict, "ProposedExperiment"], list[Union[dict, "ProposedExperiment"]]]
    ] = empty_list()
    evidence: Optional[
        Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]
    ] = empty_list()
    posed_by: Optional[str] = None
    posed_date: Optional[Union[str, XSDDate]] = None
    resolved_date: Optional[Union[str, XSDDate]] = None
    resolution_note: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.discussion_id):
            self.MissingRequiredField("discussion_id")
        if not isinstance(self.discussion_id, str):
            self.discussion_id = str(self.discussion_id)

        if self._is_empty(self.prompt):
            self.MissingRequiredField("prompt")
        if not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        if self.kind is not None and not isinstance(self.kind, DiscussionKindEnum):
            self.kind = DiscussionKindEnum(self.kind)

        if self.status is not None and not isinstance(self.status, DiscussionStatusEnum):
            self.status = DiscussionStatusEnum(self.status)

        if not isinstance(self.attaches_to, list):
            self.attaches_to = [self.attaches_to] if self.attaches_to is not None else []
        self.attaches_to = [v if isinstance(v, str) else str(v) for v in self.attaches_to]

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if not isinstance(self.proposed_experiments, list):
            self.proposed_experiments = (
                [self.proposed_experiments] if self.proposed_experiments is not None else []
            )
        self.proposed_experiments = [
            v if isinstance(v, ProposedExperiment) else ProposedExperiment(**as_dict(v))
            for v in self.proposed_experiments
        ]

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [
            v if isinstance(v, SupportingReference) else SupportingReference(**as_dict(v))
            for v in self.evidence
        ]

        if self.posed_by is not None and not isinstance(self.posed_by, str):
            self.posed_by = str(self.posed_by)

        if self.posed_date is not None and not isinstance(self.posed_date, XSDDate):
            self.posed_date = XSDDate(self.posed_date)

        if self.resolved_date is not None and not isinstance(self.resolved_date, XSDDate):
            self.resolved_date = XSDDate(self.resolved_date)

        if self.resolution_note is not None and not isinstance(self.resolution_note, str):
            self.resolution_note = str(self.resolution_note)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProposedExperiment(YAMLRoot):
    """
    A lightweight, domain-neutral sketch of an experiment or analysis that could resolve a knowledge gap. Records the
    idea and how its outcome would decide the gap; intentionally simpler than a full study design.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["ProposedExperiment"]
    class_class_curie: ClassVar[str] = "mech_shared:ProposedExperiment"
    class_name: ClassVar[str] = "ProposedExperiment"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.ProposedExperiment

    experiment_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    approach: Optional[str] = None
    model_systems: Optional[Union[str, list[str]]] = empty_list()
    perturbations: Optional[Union[str, list[str]]] = empty_list()
    readouts: Optional[Union[str, list[str]]] = empty_list()
    decision_criterion: Optional[str] = None
    would_support: Optional[str] = None
    would_refute: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.experiment_id is not None and not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.approach is not None and not isinstance(self.approach, str):
            self.approach = str(self.approach)

        if not isinstance(self.model_systems, list):
            self.model_systems = [self.model_systems] if self.model_systems is not None else []
        self.model_systems = [v if isinstance(v, str) else str(v) for v in self.model_systems]

        if not isinstance(self.perturbations, list):
            self.perturbations = [self.perturbations] if self.perturbations is not None else []
        self.perturbations = [v if isinstance(v, str) else str(v) for v in self.perturbations]

        if not isinstance(self.readouts, list):
            self.readouts = [self.readouts] if self.readouts is not None else []
        self.readouts = [v if isinstance(v, str) else str(v) for v in self.readouts]

        if self.decision_criterion is not None and not isinstance(self.decision_criterion, str):
            self.decision_criterion = str(self.decision_criterion)

        if self.would_support is not None and not isinstance(self.would_support, str):
            self.would_support = str(self.would_support)

        if self.would_refute is not None and not isinstance(self.would_refute, str):
            self.would_refute = str(self.would_refute)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A reference to a publicly available dataset (omics, sequence, phenotype) relevant to this record. A lightweight
    repository-accession reference, not a full Datasheets-for-Datasets / DCAT description.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["Dataset"]
    class_class_curie: ClassVar[str] = "mech_shared:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = COMMUNITYMECH.Dataset

    accession: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    organism: Optional[str] = None
    dataset_type: Optional[Union[str, "DatasetTypeEnum"]] = None
    repository: Optional[Union[str, "DatasetRepositoryEnum"]] = None
    sample_types: Optional[Union[str, list[str]]] = empty_list()
    sample_count: Optional[int] = None
    conditions: Optional[Union[str, list[str]]] = empty_list()
    platform: Optional[str] = None
    url: Optional[Union[str, URI]] = None
    publication: Optional[str] = None
    findings: Optional[str] = None
    evidence: Optional[
        Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]
    ] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.dataset_type is not None and not isinstance(self.dataset_type, DatasetTypeEnum):
            self.dataset_type = DatasetTypeEnum(self.dataset_type)

        if self.repository is not None and not isinstance(self.repository, DatasetRepositoryEnum):
            self.repository = DatasetRepositoryEnum(self.repository)

        if not isinstance(self.sample_types, list):
            self.sample_types = [self.sample_types] if self.sample_types is not None else []
        self.sample_types = [v if isinstance(v, str) else str(v) for v in self.sample_types]

        if self.sample_count is not None and not isinstance(self.sample_count, int):
            self.sample_count = int(self.sample_count)

        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, str) else str(v) for v in self.conditions]

        if self.platform is not None and not isinstance(self.platform, str):
            self.platform = str(self.platform)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if self.findings is not None and not isinstance(self.findings, str):
            self.findings = str(self.findings)

        if not isinstance(self.evidence, list):
            self.evidence = [self.evidence] if self.evidence is not None else []
        self.evidence = [
            v if isinstance(v, SupportingReference) else SupportingReference(**as_dict(v))
            for v in self.evidence
        ]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


# Enumerations
class EvidenceItemSupportEnum(EnumDefinitionImpl):
    """
    How the cited reference relates to the curated claim. Distinct from the validity of the claim itself: REFUTE means
    the cited paper actively contradicts the claim, while WRONG_STATEMENT means the cited paper is misattributed (it
    does not address the claim).
    """

    SUPPORT = PermissibleValue(
        text="SUPPORT",
        description="""The cited reference directly supports the claim; the snippet is a substring of the reference and the surrounding context endorses the interaction or property as stated.""",
    )
    REFUTE = PermissibleValue(
        text="REFUTE",
        description="""The cited reference actively contradicts the claim (e.g., reports the opposite effect, or shows the proposed mechanism does not occur under the cited conditions).""",
    )
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="""The cited reference supports part but not all of the claim. Common cases: snippet supports the mechanism but not the specific site, taxa, or quantitative figure asserted; or the reference supports a related but weaker version of the claim.""",
    )
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        description="""The cited reference does not contain a passage that addresses the claim. Used when the paper is on-topic and a reference is required by the schema, but the curator could not locate a supporting (or contradicting) excerpt; the snippet records the closest on-topic excerpt examined. Stronger than WRONG_STATEMENT (which signals misattribution) and weaker than REFUTE.""",
    )
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        description="""The cited reference is misattributed - the paper does not address the curated claim at all (e.g., wrong DOI/PMID, paper about a different system). Distinct from REFUTE, which is reserved for references that actively contradict the claim.""",
    )

    _defn = EnumDefinition(
        name="EvidenceItemSupportEnum",
        description="""How the cited reference relates to the curated claim. Distinct from the validity of the claim itself: REFUTE means the cited paper actively contradicts the claim, while WRONG_STATEMENT means the cited paper is misattributed (it does not address the claim).""",
    )


class EvidenceSourceEnum(EnumDefinitionImpl):
    """
    The provenance/source of the evidence
    """

    IN_VITRO = PermissibleValue(
        text="IN_VITRO", description="In vitro experiments (batch culture, bioreactor, etc.)"
    )
    IN_VIVO = PermissibleValue(
        text="IN_VIVO", description="In vivo experiments (field studies, host-associated, etc.)"
    )
    COMPUTATIONAL = PermissibleValue(
        text="COMPUTATIONAL", description="In silico modeling, simulation, or prediction"
    )
    REVIEW = PermissibleValue(text="REVIEW", description="Review article or meta-analysis")
    OTHER = PermissibleValue(text="OTHER", description="Other evidence type")

    _defn = EnumDefinition(
        name="EvidenceSourceEnum",
        description="The provenance/source of the evidence",
    )


class EcologicalStateEnum(EnumDefinitionImpl):
    """
    The ecological or health state of the community
    """

    STABLE = PermissibleValue(text="STABLE", description="Stable, equilibrium community")
    PERTURBED = PermissibleValue(
        text="PERTURBED", description="Recently perturbed (e.g., antibiotic treatment)"
    )
    ENGINEERED = PermissibleValue(
        text="ENGINEERED", description="Synthetic or engineered community"
    )
    TRANSIENT = PermissibleValue(text="TRANSIENT", description="Transient or developing community")

    _defn = EnumDefinition(
        name="EcologicalStateEnum",
        description="The ecological or health state of the community",
    )


class CommunityOriginEnum(EnumDefinitionImpl):
    """
    The origin or source of the community
    """

    NATURAL = PermissibleValue(
        text="NATURAL", description="Naturally occurring community from environment"
    )
    ENGINEERED = PermissibleValue(
        text="ENGINEERED", description="Deliberately engineered or synthetic community"
    )
    SYNTHETIC = PermissibleValue(
        text="SYNTHETIC", description="Fully synthetic community designed in laboratory"
    )

    _defn = EnumDefinition(
        name="CommunityOriginEnum",
        description="The origin or source of the community",
    )


class MediaRelationshipEnum(EnumDefinitionImpl):
    """
    Type of relationship between a microbial community and a growth medium. Distinguishes actual cultivation media
    from environmentally related media.
    """

    CULTIVATION_MEDIUM = PermissibleValue(
        text="CULTIVATION_MEDIUM",
        description="Medium actually used for cultivation of community members",
    )
    ISOLATION_MEDIUM = PermissibleValue(
        text="ISOLATION_MEDIUM",
        description="Medium used for initial isolation of community members from the environment",
    )
    ENVIRONMENT_ANALOG = PermissibleValue(
        text="ENVIRONMENT_ANALOG",
        description="Medium designed to mimic the community's natural environment",
    )
    REFERENCED_IN_STUDY = PermissibleValue(
        text="REFERENCED_IN_STUDY",
        description="Medium referenced in a study of this community but not necessarily used for cultivation",
    )
    SELECTIVE_ENRICHMENT = PermissibleValue(
        text="SELECTIVE_ENRICHMENT",
        description="Medium used for selective enrichment of specific functional groups within the community",
    )

    _defn = EnumDefinition(
        name="MediaRelationshipEnum",
        description="""Type of relationship between a microbial community and a growth medium. Distinguishes actual cultivation media from environmentally related media.""",
    )


class CommunityCategoryEnum(EnumDefinitionImpl):
    """
    Broad functional/ecological category of the community
    """

    BIOMINING = PermissibleValue(
        text="BIOMINING", description="Metal extraction and bioleaching systems"
    )
    AMD = PermissibleValue(text="AMD", description="Acid mine drainage communities")
    SYNTROPHY = PermissibleValue(text="SYNTROPHY", description="Syntrophic metabolic cooperation")
    PHYTOPLANKTON = PermissibleValue(
        text="PHYTOPLANKTON", description="Algae-bacteria associations"
    )
    RHIZOSPHERE = PermissibleValue(
        text="RHIZOSPHERE", description="Plant root-associated communities"
    )
    ORAL = PermissibleValue(
        text="ORAL", description="Oral microbiome and dental biofilm communities"
    )
    LIGNOCELLULOSE = PermissibleValue(
        text="LIGNOCELLULOSE", description="Lignocellulose degradation systems"
    )
    METHANOGENESIS = PermissibleValue(
        text="METHANOGENESIS", description="Methane-producing communities"
    )
    DIET = PermissibleValue(text="DIET", description="Direct interspecies electron transfer")
    METAL_REDUCTION = PermissibleValue(
        text="METAL_REDUCTION", description="Metal-reducing communities"
    )
    BIOREMEDIATION = PermissibleValue(
        text="BIOREMEDIATION", description="Pollutant degradation and remediation"
    )
    CARBON_SEQUESTRATION = PermissibleValue(
        text="CARBON_SEQUESTRATION", description="Carbon fixation and storage"
    )
    EXTREME_ENVIRONMENT = PermissibleValue(
        text="EXTREME_ENVIRONMENT", description="Communities from extreme conditions"
    )
    BIOTECHNOLOGY = PermissibleValue(
        text="BIOTECHNOLOGY", description="Industrial biotechnology applications"
    )
    OTHER = PermissibleValue(text="OTHER", description="Other or uncategorized communities")

    _defn = EnumDefinition(
        name="CommunityCategoryEnum",
        description="Broad functional/ecological category of the community",
    )


class GtdbGroundingStatusEnum(EnumDefinitionImpl):
    """
    Why a taxon does or does not carry a gtdb_classification. Absence alone cannot say: a virus GTDB will never
    classify, an NCBI taxon GTDB splits with no majority, and a taxon nobody has grounded yet all look identical as a
    missing block (#294). The first is a *final* state and by far the largest — 293 of 1032 taxonomy entries — so
    reading absence as outstanding work overstated the remaining backfill by roughly threefold (#276).
    """

    GROUNDED = PermissibleValue(
        text="GROUNDED",
        description="""A gtdb_classification is present. Redundant with the block's presence by design: a consumer should read a state, not infer one from whether a field exists, which is the defect this enum exists to fix.""",
    )
    NO_GTDB_EQUIVALENT = PermissibleValue(
        text="NO_GTDB_EQUIVALENT",
        description="""GTDB has no counterpart and never will. Viruses and eukaryotes (GTDB is bacteria/archaea only), environmental pseudo-taxa such as \"Stordalen Mire thaw-gradient microbiome\", and strains absent from the NCBI2GTDB mapping. A final state, not a gap.""",
    )
    AMBIGUOUS = PermissibleValue(
        text="AMBIGUOUS",
        description="""GTDB splits the NCBI taxon and no candidate holds a majority, so the tool declines to guess. gtdb_candidates carries the contenders so a curator can choose without re-running anything. Resolvable by curation, unlike NO_GTDB_EQUIVALENT.""",
    )
    WITHHELD = PermissibleValue(
        text="WITHHELD",
        description="""The tool can produce a grounding and a curator has decided it must not be stored — usually because the NCBITaxon id names a different organism, so the derived block would describe the wrong species convincingly (#292, #293). Fix the id and this becomes GROUNDED on the next run.""",
    )
    NOT_ATTEMPTED = PermissibleValue(
        text="NOT_ATTEMPTED",
        description="""No grounding has been derived, and nothing above explains why. The only value here that represents outstanding work.""",
    )

    _defn = EnumDefinition(
        name="GtdbGroundingStatusEnum",
        description="""Why a taxon does or does not carry a gtdb_classification. Absence alone cannot say: a virus GTDB will never classify, an NCBI taxon GTDB splits with no majority, and a taxon nobody has grounded yet all look identical as a missing block (#294). The first is a *final* state and by far the largest — 293 of 1032 taxonomy entries — so reading absence as outstanding work overstated the remaining backfill by roughly threefold (#276).""",
    )


class InteractionTypeEnum(EnumDefinitionImpl):
    """
    Type of ecological interaction between organisms
    """

    MUTUALISM = PermissibleValue(text="MUTUALISM", description="Both organisms benefit (+/+)")
    COMMENSALISM = PermissibleValue(
        text="COMMENSALISM", description="One benefits, other unaffected (+/0)"
    )
    CROSS_FEEDING = PermissibleValue(
        text="CROSS_FEEDING", description="Metabolite exchange between organisms"
    )
    COMPETITION = PermissibleValue(text="COMPETITION", description="Both negatively affected (-/-)")
    PREDATION = PermissibleValue(text="PREDATION", description="One benefits, other harmed (+/-)")
    SYNTROPHY = PermissibleValue(text="SYNTROPHY", description="Obligate metabolic cooperation")
    NICHE_PARTITIONING = PermissibleValue(
        text="NICHE_PARTITIONING",
        description="""Strains/species occupy distinct ecological niches, reducing competition through spatial or temporal separation""",
    )
    STRAIN_COMPETITION = PermissibleValue(
        text="STRAIN_COMPETITION",
        description="Intraspecific competition between closely related strains of the same species",
    )
    COLONIZATION_FACILITATION = PermissibleValue(
        text="COLONIZATION_FACILITATION",
        description="""One organism facilitates the colonization or establishment of another through priority effects or niche modification""",
    )

    _defn = EnumDefinition(
        name="InteractionTypeEnum",
        description="Type of ecological interaction between organisms",
    )


class InteractionScopeEnum(EnumDefinitionImpl):
    """
    Whether an interaction is a pairwise organism-to-organism edge or a community-level phenomenon
    """

    PAIRWISE = PermissibleValue(
        text="PAIRWISE",
        description="""Standard pairwise interaction between a source organism and (usually) a target. Requires source_taxon.""",
    )
    COMMUNITY_LEVEL = PermissibleValue(
        text="COMMUNITY_LEVEL",
        description="""Community-wide or emergent phenomenon (e.g., division of labor, host-microbiota colonization patterns, abiotic-input-driven processes such as electrolysis-supplied H2). source_taxon may be omitted because no single organism is the source.""",
    )

    _defn = EnumDefinition(
        name="InteractionScopeEnum",
        description="Whether an interaction is a pairwise organism-to-organism edge or a community-level phenomenon",
    )


class AbundanceEnum(EnumDefinitionImpl):
    """
    Relative abundance categories
    """

    DOMINANT = PermissibleValue(text="DOMINANT", description="Greater than 1% relative abundance")
    ABUNDANT = PermissibleValue(text="ABUNDANT", description="0.1-1% relative abundance")
    COMMON = PermissibleValue(text="COMMON", description="0.01-0.1% relative abundance")
    RARE = PermissibleValue(text="RARE", description="Less than 0.01% relative abundance")

    _defn = EnumDefinition(
        name="AbundanceEnum",
        description="Relative abundance categories",
    )


class FunctionalRoleEnum(EnumDefinitionImpl):
    """
    Functional role in the community
    """

    PRIMARY_PRODUCER = PermissibleValue(
        text="PRIMARY_PRODUCER", description="Fixes carbon (autotroph)"
    )
    PRIMARY_DEGRADER = PermissibleValue(
        text="PRIMARY_DEGRADER", description="Degrades complex substrates"
    )
    SECONDARY_FERMENTER = PermissibleValue(
        text="SECONDARY_FERMENTER", description="Ferments products from primary degraders"
    )
    SYNTROPHIC_PARTNER = PermissibleValue(
        text="SYNTROPHIC_PARTNER", description="Engages in syntrophic metabolism"
    )
    CROSS_FEEDER = PermissibleValue(
        text="CROSS_FEEDER", description="Utilizes metabolites from other taxa"
    )
    ELECTRON_DONOR = PermissibleValue(
        text="ELECTRON_DONOR",
        description="""Donates electrons in interspecies or extracellular electron transfer (e.g. the electron-donating partner in DIET).""",
    )
    ELECTRON_ACCEPTOR = PermissibleValue(
        text="ELECTRON_ACCEPTOR",
        description="""Accepts electrons in interspecies or extracellular electron transfer (e.g. the electron-accepting methanogen in DIET).""",
    )
    ELECTROGEN = PermissibleValue(
        text="ELECTROGEN",
        description="""Exoelectrogen; transfers electrons to an extracellular solid acceptor such as an anode or a metal (Fe/Mn) oxide.""",
    )
    ELECTROTROPH = PermissibleValue(
        text="ELECTROTROPH",
        description="""Takes up electrons from an extracellular donor such as a cathode (electrotrophy / extracellular electron uptake).""",
    )

    _defn = EnumDefinition(
        name="FunctionalRoleEnum",
        description="Functional role in the community",
    )


class AtmosphereEnum(EnumDefinitionImpl):
    """
    Atmospheric/oxygen requirements for growth
    """

    AEROBIC = PermissibleValue(text="AEROBIC", description="Requires oxygen for growth")
    ANAEROBIC = PermissibleValue(
        text="ANAEROBIC", description="Growth only in absence of oxygen (strict anaerobe)"
    )
    MICROAEROBIC = PermissibleValue(
        text="MICROAEROBIC", description="Requires low oxygen levels (typically 2-10%)"
    )
    FACULTATIVE_ANAEROBIC = PermissibleValue(
        text="FACULTATIVE_ANAEROBIC", description="Can grow with or without oxygen"
    )
    FACULTATIVE_AEROBIC = PermissibleValue(
        text="FACULTATIVE_AEROBIC", description="Preferentially aerobic but can grow anaerobically"
    )
    CAPNOPHILIC = PermissibleValue(text="CAPNOPHILIC", description="Requires elevated CO2 levels")

    _defn = EnumDefinition(
        name="AtmosphereEnum",
        description="Atmospheric/oxygen requirements for growth",
    )


class ExternalResourceRepositoryEnum(EnumDefinitionImpl):
    """
    External repositories and platforms that host community model resources
    """

    BIOMODELS = PermissibleValue(text="BIOMODELS", description="BioModels database")
    KBASE = PermissibleValue(text="KBASE", description="KBase Narrative platform")
    BIGG = PermissibleValue(text="BIGG", description="BiGG Models")
    VMH = PermissibleValue(text="VMH", description="Virtual Metabolic Human")
    MODELSEED = PermissibleValue(text="MODELSEED", description="ModelSEED resources")
    GITHUB = PermissibleValue(text="GITHUB", description="GitHub repository")
    OTHER = PermissibleValue(text="OTHER", description="Other resource repository")

    _defn = EnumDefinition(
        name="ExternalResourceRepositoryEnum",
        description="External repositories and platforms that host community model resources",
    )


class CultureCollectionEnum(EnumDefinitionImpl):
    """
    Major microbial culture collections worldwide
    """

    ATCC = PermissibleValue(text="ATCC", description="American Type Culture Collection (USA)")
    DSM = PermissibleValue(
        text="DSM", description="Deutsche Sammlung von Mikroorganismen (DSMZ, Germany)"
    )
    JCM = PermissibleValue(text="JCM", description="Japan Collection of Microorganisms (Japan)")
    NCTC = PermissibleValue(text="NCTC", description="National Collection of Type Cultures (UK)")
    CCUG = PermissibleValue(
        text="CCUG", description="Culture Collection University of Gothenburg (Sweden)"
    )
    PCC = PermissibleValue(
        text="PCC", description="Pasteur Culture Collection of Cyanobacteria (France)"
    )
    NCIMB = PermissibleValue(
        text="NCIMB", description="National Collection of Industrial Marine Bacteria (UK)"
    )
    LMG = PermissibleValue(text="LMG", description="BCCM/LMG Bacteria Collection (Belgium)")
    KCTC = PermissibleValue(text="KCTC", description="Korean Collection for Type Cultures (Korea)")
    CIP = PermissibleValue(text="CIP", description="Collection de l'Institut Pasteur (France)")
    NBRC = PermissibleValue(text="NBRC", description="NITE Biological Resource Center (Japan)")
    VKM = PermissibleValue(
        text="VKM", description="All-Russian Collection of Microorganisms (Russia)"
    )
    CGMCC = PermissibleValue(
        text="CGMCC", description="China General Microbiological Culture Collection (China)"
    )
    BCRC = PermissibleValue(
        text="BCRC", description="Bioresource Collection and Research Center (Taiwan)"
    )
    CBS = PermissibleValue(
        text="CBS", description="Westerdijk Fungal Biodiversity Institute (Netherlands)"
    )
    OTHER = PermissibleValue(text="OTHER", description="Other culture collection not listed")

    _defn = EnumDefinition(
        name="CultureCollectionEnum",
        description="Major microbial culture collections worldwide",
    )


class MetalElementEnum(EnumDefinitionImpl):
    """
    Metal elements relevant to microbial communities
    """

    COPPER = PermissibleValue(
        text="COPPER", description="Copper(2+) cation", meaning=CHEBI["29036"]
    )
    IRON = PermissibleValue(text="IRON", description="Iron(2+) cation", meaning=CHEBI["29033"])
    ZINC = PermissibleValue(text="ZINC", description="Zinc(2+) cation", meaning=CHEBI["27363"])
    NICKEL = PermissibleValue(
        text="NICKEL", description="Nickel(2+) cation", meaning=CHEBI["49786"]
    )
    COBALT = PermissibleValue(
        text="COBALT", description="Cobalt(2+) cation", meaning=CHEBI["48828"]
    )
    VANADIUM = PermissibleValue(
        text="VANADIUM", description="Vanadium cation", meaning=CHEBI["27698"]
    )
    URANIUM = PermissibleValue(text="URANIUM", description="Uranium atom", meaning=CHEBI["27214"])
    CHROMIUM = PermissibleValue(
        text="CHROMIUM", description="Chromium atom", meaning=CHEBI["28073"]
    )
    LEAD = PermissibleValue(text="LEAD", description="Lead(2+) cation", meaning=CHEBI["25016"])
    LITHIUM = PermissibleValue(
        text="LITHIUM", description="Lithium(1+) cation", meaning=CHEBI["49713"]
    )
    GOLD = PermissibleValue(text="GOLD", description="Gold atom", meaning=CHEBI["29287"])
    SILVER = PermissibleValue(
        text="SILVER", description="Silver(1+) cation", meaning=CHEBI["30512"]
    )
    PALLADIUM = PermissibleValue(
        text="PALLADIUM", description="Palladium atom", meaning=CHEBI["33363"]
    )
    GALLIUM = PermissibleValue(
        text="GALLIUM", description="Gallium(3+) cation", meaning=CHEBI["49631"]
    )
    INDIUM = PermissibleValue(
        text="INDIUM", description="Indium(3+) cation", meaning=CHEBI["49664"]
    )
    TITANIUM = PermissibleValue(
        text="TITANIUM", description="Titanium atom", meaning=CHEBI["33341"]
    )
    MERCURY = PermissibleValue(
        text="MERCURY", description="Mercury(2+) cation", meaning=CHEBI["16793"]
    )

    _defn = EnumDefinition(
        name="MetalElementEnum",
        description="Metal elements relevant to microbial communities",
    )


class RareEarthElementEnum(EnumDefinitionImpl):
    """
    Rare earth elements (lanthanides + Y, Sc)
    """

    LANTHANUM = PermissibleValue(
        text="LANTHANUM", description="Lanthanum(3+) cation", meaning=CHEBI["49701"]
    )
    CERIUM = PermissibleValue(
        text="CERIUM", description="Cerium(3+) cation", meaning=CHEBI["48782"]
    )
    PRASEODYMIUM = PermissibleValue(
        text="PRASEODYMIUM", description="Praseodymium(3+) cation", meaning=CHEBI["229784"]
    )
    NEODYMIUM = PermissibleValue(
        text="NEODYMIUM", description="Neodymium(3+) cation", meaning=CHEBI["229785"]
    )
    SAMARIUM = PermissibleValue(
        text="SAMARIUM", description="Samarium(3+) cation", meaning=CHEBI["49890"]
    )
    EUROPIUM = PermissibleValue(
        text="EUROPIUM", description="Europium(3+) cation", meaning=CHEBI["49591"]
    )
    GADOLINIUM = PermissibleValue(
        text="GADOLINIUM", description="Gadolinium(3+) cation", meaning=CHEBI["49618"]
    )
    TERBIUM = PermissibleValue(
        text="TERBIUM", description="Terbium(3+) cation", meaning=CHEBI["49902"]
    )
    DYSPROSIUM = PermissibleValue(
        text="DYSPROSIUM",
        description="Dysprosium atom (ChEBI has no dysprosium(3+) cation term)",
        meaning=CHEBI["33377"],
    )
    HOLMIUM = PermissibleValue(
        text="HOLMIUM", description="Holmium(3+) cation", meaning=CHEBI["49650"]
    )
    ERBIUM = PermissibleValue(
        text="ERBIUM",
        description="Erbium atom (ChEBI has no erbium(3+) cation term)",
        meaning=CHEBI["33379"],
    )
    THULIUM = PermissibleValue(
        text="THULIUM",
        description="Thulium atom (ChEBI has no thulium(3+) cation term)",
        meaning=CHEBI["33380"],
    )
    YTTERBIUM = PermissibleValue(
        text="YTTERBIUM", description="Ytterbium(3+) cation", meaning=CHEBI["49980"]
    )
    LUTETIUM = PermissibleValue(
        text="LUTETIUM", description="Lutetium(3+) cation", meaning=CHEBI["49746"]
    )
    YTTRIUM = PermissibleValue(
        text="YTTRIUM", description="Yttrium(3+) cation", meaning=CHEBI["49962"]
    )
    SCANDIUM = PermissibleValue(
        text="SCANDIUM", description="Scandium(3+) cation", meaning=CHEBI["231857"]
    )

    _defn = EnumDefinition(
        name="RareEarthElementEnum",
        description="Rare earth elements (lanthanides + Y, Sc)",
    )


class MetalRelevanceEnum(EnumDefinitionImpl):
    """
    Relevance of metals/REE to community function
    """

    PRIMARY = PermissibleValue(
        text="PRIMARY", description="Primary function involves metal/REE extraction or cycling"
    )
    SIGNIFICANT = PermissibleValue(
        text="SIGNIFICANT", description="Significant metal/REE metabolism but not primary function"
    )
    INCIDENTAL = PermissibleValue(text="INCIDENTAL", description="Incidental metal/REE interaction")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE", description="No significant metal/REE relevance"
    )

    _defn = EnumDefinition(
        name="MetalRelevanceEnum",
        description="Relevance of metals/REE to community function",
    )


class CultivationModeEnum(EnumDefinitionImpl):
    """
    Operating mode / approach used to cultivate the community. Standardized terms maintained in
    vocab/cultivation_terms.yaml (kept in sync by tests/test_cultivation_vocab_sync.py) and staged for a METPO
    proposal.
    """

    BATCH = PermissibleValue(
        text="BATCH",
        description="Closed culture with no nutrient addition or removal after inoculation.",
    )
    FED_BATCH = PermissibleValue(
        text="FED_BATCH",
        description="Nutrients fed during the run, with no removal of culture broth.",
    )
    CONTINUOUS = PermissibleValue(
        text="CONTINUOUS",
        description="Fresh medium added and culture withdrawn continuously, typically at steady state.",
    )
    SEMI_CONTINUOUS = PermissibleValue(
        text="SEMI_CONTINUOUS",
        description="Periodic partial harvest and replacement of medium (draw-and-fill).",
    )
    CHEMOSTAT = PermissibleValue(
        text="CHEMOSTAT",
        description="""Continuous culture held at steady state by a fixed dilution rate and a growth-limiting nutrient.""",
    )
    TURBIDOSTAT = PermissibleValue(
        text="TURBIDOSTAT",
        description="Continuous culture controlled to hold constant turbidity / cell density.",
    )
    PERFUSION = PermissibleValue(
        text="PERFUSION",
        description="""Continuous medium exchange with biomass retention (cells retained while spent medium is removed).""",
    )
    SEQUENCING_BATCH = PermissibleValue(
        text="SEQUENCING_BATCH",
        description="Repeated fill / react / settle / draw cycles in a single vessel.",
    )
    RETENTOSTAT = PermissibleValue(
        text="RETENTOSTAT",
        description="Continuous culture with complete biomass retention, approaching near-zero growth rate.",
    )
    OTHER = PermissibleValue(
        text="OTHER", description="Other cultivation mode not covered by the listed values."
    )

    _defn = EnumDefinition(
        name="CultivationModeEnum",
        description="""Operating mode / approach used to cultivate the community. Standardized terms maintained in vocab/cultivation_terms.yaml (kept in sync by tests/test_cultivation_vocab_sync.py) and staged for a METPO proposal.""",
    )


class CultivationSystemEnum(EnumDefinitionImpl):
    """
    Instrumentation / vessel system used to grow the community. Standardized terms maintained in
    vocab/cultivation_terms.yaml (kept in sync by tests/test_cultivation_vocab_sync.py) and staged for a METPO
    proposal.
    """

    STIRRED_TANK_BIOREACTOR = PermissibleValue(
        text="STIRRED_TANK_BIOREACTOR", description="Mechanically stirred tank reactor (CSTR-type)."
    )
    PHOTOBIOREACTOR = PermissibleValue(
        text="PHOTOBIOREACTOR",
        description="Light-driven reactor for cultivating phototrophic organisms.",
    )
    MICROBIAL_FUEL_CELL = PermissibleValue(
        text="MICROBIAL_FUEL_CELL",
        description="Bioelectrochemical system that generates electric current from microbial metabolism.",
    )
    BIOELECTROCHEMICAL_SYSTEM = PermissibleValue(
        text="BIOELECTROCHEMICAL_SYSTEM",
        description="""Electrode-coupled reactor (broader than a microbial fuel cell), e.g. microbial electrolysis or electrosynthesis cells.""",
    )
    CHEMOSTAT_VESSEL = PermissibleValue(
        text="CHEMOSTAT_VESSEL",
        description="A vessel configured for chemostat (dilution-rate-controlled) continuous culture.",
    )
    MEMBRANE_BIOREACTOR = PermissibleValue(
        text="MEMBRANE_BIOREACTOR",
        description="Reactor coupling cultivation with a membrane for biomass/liquid separation.",
    )
    SERUM_BOTTLE = PermissibleValue(
        text="SERUM_BOTTLE",
        description="Sealed serum bottle, commonly used for anaerobic cultivation.",
    )
    FLASK = PermissibleValue(text="FLASK", description="Erlenmeyer / shake flask.")
    GAS_LIFT_REACTOR = PermissibleValue(
        text="GAS_LIFT_REACTOR", description="Pneumatically mixed reactor (airlift / gas-lift)."
    )
    PACKED_BED_REACTOR = PermissibleValue(
        text="PACKED_BED_REACTOR",
        description="Reactor with a fixed packed support matrix for biofilm growth.",
    )
    MICROFLUIDIC_DEVICE = PermissibleValue(
        text="MICROFLUIDIC_DEVICE", description="Microfluidic cultivation chip / device."
    )
    HOLLOW_FIBER_REACTOR = PermissibleValue(
        text="HOLLOW_FIBER_REACTOR", description="Hollow-fiber membrane cultivation system."
    )
    BIOREACTOR_UNSPECIFIED = PermissibleValue(
        text="BIOREACTOR_UNSPECIFIED",
        description="Bioreactor of unspecified type.",
        meaning=OBI["0001046"],
    )
    OTHER = PermissibleValue(
        text="OTHER", description="Other cultivation system not covered by the listed values."
    )

    _defn = EnumDefinition(
        name="CultivationSystemEnum",
        description="""Instrumentation / vessel system used to grow the community. Standardized terms maintained in vocab/cultivation_terms.yaml (kept in sync by tests/test_cultivation_vocab_sync.py) and staged for a METPO proposal.""",
    )


class ComputationalPredictionTypeEnum(EnumDefinitionImpl):
    """
    Category of computational method that produced a predicted claim. Used to make model-derived evidence (e.g.
    cross-feeding predicted from a genome-scale metabolic model) queryable rather than buried in free text. Populate
    ComputationalProvenance.prediction_type when EvidenceItem.evidence_source is COMPUTATIONAL.
    """

    GENOME_SCALE_METABOLIC_MODEL = PermissibleValue(
        text="GENOME_SCALE_METABOLIC_MODEL",
        description="""Prediction derived from a genome-scale metabolic model (GEM), e.g. a draft reconstruction of an organism's metabolic network.""",
    )
    FLUX_BALANCE_ANALYSIS = PermissibleValue(
        text="FLUX_BALANCE_ANALYSIS",
        description="""Constraint-based flux simulation (FBA / community FBA) over a metabolic model, e.g. to identify exchangeable metabolites between members.""",
    )
    METABOLIC_INTERACTION_SIMULATION = PermissibleValue(
        text="METABOLIC_INTERACTION_SIMULATION",
        description="""Community-level metabolic exchange / cross-feeding simulation (e.g. SMETANA, MICOM) that predicts interspecies interactions.""",
    )
    SEQUENCE_HOMOLOGY = PermissibleValue(
        text="SEQUENCE_HOMOLOGY",
        description="Prediction from sequence similarity / homology search (e.g. BLAST, DIAMOND, HMM).",
    )
    PHYLOGENETIC_INFERENCE = PermissibleValue(
        text="PHYLOGENETIC_INFERENCE",
        description="Prediction from phylogenetic placement or comparative genomics.",
    )
    STATISTICAL_INFERENCE = PermissibleValue(
        text="STATISTICAL_INFERENCE",
        description="""Prediction from a statistical model (e.g. co-occurrence, correlation networks, differential abundance).""",
    )
    MACHINE_LEARNING = PermissibleValue(
        text="MACHINE_LEARNING",
        description="Prediction from a trained machine-learning / deep-learning model.",
    )
    THERMODYNAMIC = PermissibleValue(
        text="THERMODYNAMIC", description="Prediction from thermodynamic feasibility analysis."
    )
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other computational prediction method not covered by the listed values.",
    )

    _defn = EnumDefinition(
        name="ComputationalPredictionTypeEnum",
        description="""Category of computational method that produced a predicted claim. Used to make model-derived evidence (e.g. cross-feeding predicted from a genome-scale metabolic model) queryable rather than buried in free text. Populate ComputationalProvenance.prediction_type when EvidenceItem.evidence_source is COMPUTATIONAL.""",
    )


class DiscussionKindEnum(EnumDefinitionImpl):
    """
    Kind of unresolved / in-progress item captured by a Discussion. Knowledge gaps are represented as a discussion
    kind so they reuse the shared pointer, evidence, and lifecycle machinery, while optional proposed experiments
    capture how a gap could be resolved.
    """

    OPEN_QUESTION = PermissibleValue(
        text="OPEN_QUESTION",
        description="An unresolved scientific question posed by curators or experts.",
    )
    KNOWLEDGE_GAP = PermissibleValue(
        text="KNOWLEDGE_GAP",
        description="""A missing causal, evidentiary, model-system, or measurement assertion whose resolution would materially improve the record.""",
    )
    CONTROVERSY = PermissibleValue(
        text="CONTROVERSY",
        description="A live disagreement or competing interpretation between published positions.",
    )
    CURATION_TODO = PermissibleValue(
        text="CURATION_TODO",
        description='A curation task captured inline (e.g. "ingredient needs CHEBI refinement").',
    )
    EMERGING_HYPOTHESIS = PermissibleValue(
        text="EMERGING_HYPOTHESIS",
        description="A recently reported hypothesis under active discussion in the community.",
    )
    INTERPRETATION = PermissibleValue(
        text="INTERPRETATION",
        description="A discussion about how to interpret existing evidence or model an edge.",
    )
    HUMAN_MODEL_MISMATCH = PermissibleValue(
        text="HUMAN_MODEL_MISMATCH",
        description="""A gap where evidence exists in one system but its fidelity to the target context is uncertain (e.g. an in-vitro/model result whose transfer to the in-situ or host-associated setting is unverified).""",
    )

    _defn = EnumDefinition(
        name="DiscussionKindEnum",
        description="""Kind of unresolved / in-progress item captured by a Discussion. Knowledge gaps are represented as a discussion kind so they reuse the shared pointer, evidence, and lifecycle machinery, while optional proposed experiments capture how a gap could be resolved.""",
    )


class DiscussionStatusEnum(EnumDefinitionImpl):
    """
    Lifecycle status for a Discussion.
    """

    OPEN = PermissibleValue(text="OPEN", description="Posed but not yet under active discussion.")
    UNDER_DISCUSSION = PermissibleValue(
        text="UNDER_DISCUSSION",
        description="Actively being discussed in one or more linked venues.",
    )
    RESOLVED = PermissibleValue(
        text="RESOLVED", description="Closed with a documented resolution; kept for provenance."
    )
    ARCHIVED = PermissibleValue(
        text="ARCHIVED",
        description="No longer active and not resolved (deferred, stale, or superseded).",
    )

    _defn = EnumDefinition(
        name="DiscussionStatusEnum",
        description="Lifecycle status for a Discussion.",
    )


class SupportLevelEnum(EnumDefinitionImpl):
    """
    How a SupportingReference bears on the claim it is attached to (mirrors the supports semantics already used in the
    Mech EvidenceItem models).
    """

    SUPPORT = PermissibleValue(text="SUPPORT", description="The source supports the claim.")
    REFUTE = PermissibleValue(text="REFUTE", description="The source contradicts the claim.")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="The source partially supports the claim or supports it with caveats.",
    )
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        description="The source is relevant context but does not directly bear on the claim.",
    )
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        description="The cited statement was found to be incorrect (kept for provenance).",
    )

    _defn = EnumDefinition(
        name="SupportLevelEnum",
        description="""How a SupportingReference bears on the claim it is attached to (mirrors the supports semantics already used in the Mech EvidenceItem models).""",
    )


class DatasetTypeEnum(EnumDefinitionImpl):
    """
    Type of dataset or data resource. Canonical UNION of CultureMech's and CommunityMech's enums plus microbial
    additions. Migration map (old → this): CultureMech values carry over unchanged; CommunityMech GENOME→GENOMICS,
    METAGENOME→METAGENOMICS, METATRANSCRIPTOME→METATRANSCRIPTOMICS, METAPROTEOME→METAPROTEOMICS (AMPLICON_16S /
    AMPLICON_ITS / METABOLOMICS / PHENOTYPE / MULTI_OMICS / OTHER are unchanged).
    """

    GENOMICS = PermissibleValue(
        text="GENOMICS",
        description="Isolate / single-organism genome data. (CultureMech GENOMICS; CommunityMech GENOME)",
    )
    METAGENOMICS = PermissibleValue(
        text="METAGENOMICS", description="Shotgun metagenome sequencing. (CommunityMech METAGENOME)"
    )
    AMPLICON_16S = PermissibleValue(
        text="AMPLICON_16S", description="16S rRNA marker-gene amplicon sequencing."
    )
    AMPLICON_ITS = PermissibleValue(
        text="AMPLICON_ITS", description="ITS marker-gene amplicon sequencing."
    )
    AMPLICON_OTHER = PermissibleValue(
        text="AMPLICON_OTHER",
        description="Marker-gene amplicon sequencing other than 16S/ITS (e.g. 18S, rpoB).",
    )
    TRANSCRIPTOMICS = PermissibleValue(
        text="TRANSCRIPTOMICS", description="Single-organism RNA sequencing / expression."
    )
    METATRANSCRIPTOMICS = PermissibleValue(
        text="METATRANSCRIPTOMICS",
        description="Community-level RNA sequencing. (CommunityMech METATRANSCRIPTOME)",
    )
    PROTEOMICS = PermissibleValue(
        text="PROTEOMICS", description="Single-organism protein expression profiling."
    )
    METAPROTEOMICS = PermissibleValue(
        text="METAPROTEOMICS",
        description="Community-level proteomics. (CommunityMech METAPROTEOME)",
    )
    METABOLOMICS = PermissibleValue(text="METABOLOMICS", description="Metabolite profiling.")
    FLUXOMICS = PermissibleValue(text="FLUXOMICS", description="Metabolic flux profiling.")
    PHENOMICS = PermissibleValue(
        text="PHENOMICS", description="High-throughput phenotype profiling."
    )
    PHENOTYPE = PermissibleValue(
        text="PHENOTYPE",
        description="Phenotype / trait measurement collection (e.g. growth, biochemical).",
    )
    MULTI_OMICS = PermissibleValue(
        text="MULTI_OMICS", description="Integrated multi-omics profiling."
    )
    OTHER = PermissibleValue(text="OTHER", description="A dataset type not covered by the above.")

    _defn = EnumDefinition(
        name="DatasetTypeEnum",
        description="""Type of dataset or data resource. Canonical UNION of CultureMech's and CommunityMech's enums plus microbial additions. Migration map (old → this): CultureMech values carry over unchanged; CommunityMech GENOME→GENOMICS, METAGENOME→METAGENOMICS, METATRANSCRIPTOME→METATRANSCRIPTOMICS, METAPROTEOME→METAPROTEOMICS (AMPLICON_16S / AMPLICON_ITS / METABOLOMICS / PHENOTYPE / MULTI_OMICS / OTHER are unchanged).""",
    )


class DatasetRepositoryEnum(EnumDefinitionImpl):
    """
    Public repository hosting the dataset. Superset of CommunityMech's enum (all values preserved) plus common
    additions; CultureMech datasets have no repository field today and migrate with repository unset / OTHER.
    """

    NCBI_SRA = PermissibleValue(text="NCBI_SRA", description="NCBI Sequence Read Archive.")
    NCBI_BIOPROJECT = PermissibleValue(text="NCBI_BIOPROJECT", description="NCBI BioProject.")
    NCBI_GEO = PermissibleValue(text="NCBI_GEO", description="NCBI Gene Expression Omnibus.")
    NCBI_ASSEMBLY = PermissibleValue(
        text="NCBI_ASSEMBLY", description="NCBI Assembly (genome assemblies)."
    )
    ENA = PermissibleValue(text="ENA", description="European Nucleotide Archive.")
    ARRAYEXPRESS = PermissibleValue(
        text="ARRAYEXPRESS", description="EBI ArrayExpress / BioStudies."
    )
    MGNIFY = PermissibleValue(text="MGNIFY", description="EBI MGnify metagenomics resource.")
    JGI_GOLD = PermissibleValue(text="JGI_GOLD", description="JGI Genomes OnLine Database.")
    JGI_IMG = PermissibleValue(
        text="JGI_IMG", description="JGI Integrated Microbial Genomes & Microbiomes."
    )
    NMDC = PermissibleValue(text="NMDC", description="National Microbiome Data Collaborative.")
    METABOLOMICS_WORKBENCH = PermissibleValue(
        text="METABOLOMICS_WORKBENCH", description="NIH Metabolomics Workbench."
    )
    METABOLIGHTS = PermissibleValue(
        text="METABOLIGHTS", description="EBI MetaboLights metabolomics repository."
    )
    MASSIVE = PermissibleValue(text="MASSIVE", description="MassIVE mass-spectrometry repository.")
    GNPS = PermissibleValue(
        text="GNPS", description="Global Natural Products Social Molecular Networking."
    )
    PRIDE = PermissibleValue(text="PRIDE", description="EBI PRIDE proteomics repository.")
    DBGAP = PermissibleValue(text="DBGAP", description="NCBI database of Genotypes and Phenotypes.")
    GTEX = PermissibleValue(text="GTEX", description="Genotype-Tissue Expression project.")
    FIGSHARE = PermissibleValue(
        text="FIGSHARE", description="Figshare general-purpose research data archive."
    )
    ZENODO = PermissibleValue(
        text="ZENODO", description="Zenodo general-purpose research data archive."
    )
    BIOMODELS = PermissibleValue(
        text="BIOMODELS", description="EBI BioModels repository of computational models."
    )
    KBASE = PermissibleValue(text="KBASE", description="DOE Systems Biology Knowledgebase (KBase).")
    OTHER = PermissibleValue(text="OTHER", description="A repository not covered by the above.")

    _defn = EnumDefinition(
        name="DatasetRepositoryEnum",
        description="""Public repository hosting the dataset. Superset of CommunityMech's enum (all values preserved) plus common additions; CultureMech datasets have no repository field today and migrate with repository unset / OTHER.""",
    )


# Slots
class slots:
    pass


slots.term__id = Slot(
    uri=COMMUNITYMECH.id,
    name="term__id",
    curie=COMMUNITYMECH.curie("id"),
    model_uri=COMMUNITYMECH.term__id,
    domain=None,
    range=str,
)

slots.term__label = Slot(
    uri=RDFS.label,
    name="term__label",
    curie=RDFS.curie("label"),
    model_uri=COMMUNITYMECH.term__label,
    domain=None,
    range=str,
)

slots.evidenceItem__reference = Slot(
    uri=COMMUNITYMECH.reference,
    name="evidenceItem__reference",
    curie=COMMUNITYMECH.curie("reference"),
    model_uri=COMMUNITYMECH.evidenceItem__reference,
    domain=None,
    range=str,
    pattern=re.compile(r"^(PMID:|doi:|bioproject:).*"),
)

slots.evidenceItem__supports = Slot(
    uri=COMMUNITYMECH.supports,
    name="evidenceItem__supports",
    curie=COMMUNITYMECH.curie("supports"),
    model_uri=COMMUNITYMECH.evidenceItem__supports,
    domain=None,
    range=Union[str, "EvidenceItemSupportEnum"],
)

slots.evidenceItem__evidence_source = Slot(
    uri=COMMUNITYMECH.evidence_source,
    name="evidenceItem__evidence_source",
    curie=COMMUNITYMECH.curie("evidence_source"),
    model_uri=COMMUNITYMECH.evidenceItem__evidence_source,
    domain=None,
    range=Union[str, "EvidenceSourceEnum"],
)

slots.evidenceItem__snippet = Slot(
    uri=COMMUNITYMECH.snippet,
    name="evidenceItem__snippet",
    curie=COMMUNITYMECH.curie("snippet"),
    model_uri=COMMUNITYMECH.evidenceItem__snippet,
    domain=None,
    range=str,
)

slots.evidenceItem__explanation = Slot(
    uri=COMMUNITYMECH.explanation,
    name="evidenceItem__explanation",
    curie=COMMUNITYMECH.curie("explanation"),
    model_uri=COMMUNITYMECH.evidenceItem__explanation,
    domain=None,
    range=Optional[str],
)

slots.evidenceItem__confidence_score = Slot(
    uri=COMMUNITYMECH.confidence_score,
    name="evidenceItem__confidence_score",
    curie=COMMUNITYMECH.curie("confidence_score"),
    model_uri=COMMUNITYMECH.evidenceItem__confidence_score,
    domain=None,
    range=Optional[float],
)

slots.evidenceItem__computational_provenance = Slot(
    uri=COMMUNITYMECH.computational_provenance,
    name="evidenceItem__computational_provenance",
    curie=COMMUNITYMECH.curie("computational_provenance"),
    model_uri=COMMUNITYMECH.evidenceItem__computational_provenance,
    domain=None,
    range=Optional[Union[dict, ComputationalProvenance]],
)

slots.computationalProvenance__prediction_type = Slot(
    uri=COMMUNITYMECH.prediction_type,
    name="computationalProvenance__prediction_type",
    curie=COMMUNITYMECH.curie("prediction_type"),
    model_uri=COMMUNITYMECH.computationalProvenance__prediction_type,
    domain=None,
    range=Optional[Union[str, "ComputationalPredictionTypeEnum"]],
)

slots.computationalProvenance__tools = Slot(
    uri=COMMUNITYMECH.tools,
    name="computationalProvenance__tools",
    curie=COMMUNITYMECH.curie("tools"),
    model_uri=COMMUNITYMECH.computationalProvenance__tools,
    domain=None,
    range=Optional[Union[Union[dict, ComputationalTool], list[Union[dict, ComputationalTool]]]],
)

slots.computationalProvenance__model_name = Slot(
    uri=COMMUNITYMECH.model_name,
    name="computationalProvenance__model_name",
    curie=COMMUNITYMECH.curie("model_name"),
    model_uri=COMMUNITYMECH.computationalProvenance__model_name,
    domain=None,
    range=Optional[str],
)

slots.computationalProvenance__model_source = Slot(
    uri=COMMUNITYMECH.model_source,
    name="computationalProvenance__model_source",
    curie=COMMUNITYMECH.curie("model_source"),
    model_uri=COMMUNITYMECH.computationalProvenance__model_source,
    domain=None,
    range=Optional[str],
)

slots.computationalProvenance__input_accession = Slot(
    uri=COMMUNITYMECH.input_accession,
    name="computationalProvenance__input_accession",
    curie=COMMUNITYMECH.curie("input_accession"),
    model_uri=COMMUNITYMECH.computationalProvenance__input_accession,
    domain=None,
    range=Optional[str],
)

slots.computationalProvenance__simulated_medium = Slot(
    uri=COMMUNITYMECH.simulated_medium,
    name="computationalProvenance__simulated_medium",
    curie=COMMUNITYMECH.curie("simulated_medium"),
    model_uri=COMMUNITYMECH.computationalProvenance__simulated_medium,
    domain=None,
    range=Optional[str],
)

slots.computationalProvenance__parameters = Slot(
    uri=COMMUNITYMECH.parameters,
    name="computationalProvenance__parameters",
    curie=COMMUNITYMECH.curie("parameters"),
    model_uri=COMMUNITYMECH.computationalProvenance__parameters,
    domain=None,
    range=Optional[str],
)

slots.computationalTool__tool_name = Slot(
    uri=COMMUNITYMECH.tool_name,
    name="computationalTool__tool_name",
    curie=COMMUNITYMECH.curie("tool_name"),
    model_uri=COMMUNITYMECH.computationalTool__tool_name,
    domain=None,
    range=str,
)

slots.computationalTool__tool_version = Slot(
    uri=COMMUNITYMECH.tool_version,
    name="computationalTool__tool_version",
    curie=COMMUNITYMECH.curie("tool_version"),
    model_uri=COMMUNITYMECH.computationalTool__tool_version,
    domain=None,
    range=Optional[str],
)

slots.computationalTool__tool_reference = Slot(
    uri=COMMUNITYMECH.tool_reference,
    name="computationalTool__tool_reference",
    curie=COMMUNITYMECH.curie("tool_reference"),
    model_uri=COMMUNITYMECH.computationalTool__tool_reference,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^(PMID:|doi:|bioproject:).*"),
)

slots.computationalTool__role = Slot(
    uri=COMMUNITYMECH.role,
    name="computationalTool__role",
    curie=COMMUNITYMECH.curie("role"),
    model_uri=COMMUNITYMECH.computationalTool__role,
    domain=None,
    range=Optional[str],
)

slots.taxonDescriptor__preferred_term = Slot(
    uri=COMMUNITYMECH.preferred_term,
    name="taxonDescriptor__preferred_term",
    curie=COMMUNITYMECH.curie("preferred_term"),
    model_uri=COMMUNITYMECH.taxonDescriptor__preferred_term,
    domain=None,
    range=str,
)

slots.taxonDescriptor__term = Slot(
    uri=COMMUNITYMECH.term,
    name="taxonDescriptor__term",
    curie=COMMUNITYMECH.curie("term"),
    model_uri=COMMUNITYMECH.taxonDescriptor__term,
    domain=None,
    range=Union[dict, Term],
)

slots.taxonDescriptor__gtdb_grounding_status = Slot(
    uri=COMMUNITYMECH.gtdb_grounding_status,
    name="taxonDescriptor__gtdb_grounding_status",
    curie=COMMUNITYMECH.curie("gtdb_grounding_status"),
    model_uri=COMMUNITYMECH.taxonDescriptor__gtdb_grounding_status,
    domain=None,
    range=Optional[Union[str, "GtdbGroundingStatusEnum"]],
)

slots.taxonDescriptor__gtdb_candidates = Slot(
    uri=COMMUNITYMECH.gtdb_candidates,
    name="taxonDescriptor__gtdb_candidates",
    curie=COMMUNITYMECH.curie("gtdb_candidates"),
    model_uri=COMMUNITYMECH.taxonDescriptor__gtdb_candidates,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.taxonDescriptor__gtdb_classification = Slot(
    uri=COMMUNITYMECH.gtdb_classification,
    name="taxonDescriptor__gtdb_classification",
    curie=COMMUNITYMECH.curie("gtdb_classification"),
    model_uri=COMMUNITYMECH.taxonDescriptor__gtdb_classification,
    domain=None,
    range=Optional[Union[dict, GtdbClassification]],
)

slots.taxonDescriptor__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="taxonDescriptor__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.taxonDescriptor__notes,
    domain=None,
    range=Optional[str],
)

slots.gtdbClassification__gtdb_id = Slot(
    uri=COMMUNITYMECH.gtdb_id,
    name="gtdbClassification__gtdb_id",
    curie=COMMUNITYMECH.curie("gtdb_id"),
    model_uri=COMMUNITYMECH.gtdbClassification__gtdb_id,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^GTDB:[cdfgops]__.+"),
)

slots.gtdbClassification__gtdb_taxon = Slot(
    uri=COMMUNITYMECH.gtdb_taxon,
    name="gtdbClassification__gtdb_taxon",
    curie=COMMUNITYMECH.curie("gtdb_taxon"),
    model_uri=COMMUNITYMECH.gtdbClassification__gtdb_taxon,
    domain=None,
    range=Optional[str],
)

slots.gtdbClassification__gtdb_lineage = Slot(
    uri=COMMUNITYMECH.gtdb_lineage,
    name="gtdbClassification__gtdb_lineage",
    curie=COMMUNITYMECH.curie("gtdb_lineage"),
    model_uri=COMMUNITYMECH.gtdbClassification__gtdb_lineage,
    domain=None,
    range=Optional[str],
)

slots.gtdbClassification__ncbi_source_id = Slot(
    uri=COMMUNITYMECH.ncbi_source_id,
    name="gtdbClassification__ncbi_source_id",
    curie=COMMUNITYMECH.curie("ncbi_source_id"),
    model_uri=COMMUNITYMECH.gtdbClassification__ncbi_source_id,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^NCBITaxon:[0-9]+$"),
)

slots.gtdbClassification__majority_fraction = Slot(
    uri=COMMUNITYMECH.majority_fraction,
    name="gtdbClassification__majority_fraction",
    curie=COMMUNITYMECH.curie("majority_fraction"),
    model_uri=COMMUNITYMECH.gtdbClassification__majority_fraction,
    domain=None,
    range=Optional[float],
)

slots.gtdbClassification__support_genomes = Slot(
    uri=COMMUNITYMECH.support_genomes,
    name="gtdbClassification__support_genomes",
    curie=COMMUNITYMECH.curie("support_genomes"),
    model_uri=COMMUNITYMECH.gtdbClassification__support_genomes,
    domain=None,
    range=Optional[int],
)

slots.gtdbClassification__total_genomes = Slot(
    uri=COMMUNITYMECH.total_genomes,
    name="gtdbClassification__total_genomes",
    curie=COMMUNITYMECH.curie("total_genomes"),
    model_uri=COMMUNITYMECH.gtdbClassification__total_genomes,
    domain=None,
    range=Optional[int],
)

slots.gtdbClassification__is_reclassified = Slot(
    uri=COMMUNITYMECH.is_reclassified,
    name="gtdbClassification__is_reclassified",
    curie=COMMUNITYMECH.curie("is_reclassified"),
    model_uri=COMMUNITYMECH.gtdbClassification__is_reclassified,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.gtdbClassification__mapping_source = Slot(
    uri=COMMUNITYMECH.mapping_source,
    name="gtdbClassification__mapping_source",
    curie=COMMUNITYMECH.curie("mapping_source"),
    model_uri=COMMUNITYMECH.gtdbClassification__mapping_source,
    domain=None,
    range=Optional[str],
)

slots.metaboliteDescriptor__preferred_term = Slot(
    uri=COMMUNITYMECH.preferred_term,
    name="metaboliteDescriptor__preferred_term",
    curie=COMMUNITYMECH.curie("preferred_term"),
    model_uri=COMMUNITYMECH.metaboliteDescriptor__preferred_term,
    domain=None,
    range=str,
)

slots.metaboliteDescriptor__term = Slot(
    uri=COMMUNITYMECH.term,
    name="metaboliteDescriptor__term",
    curie=COMMUNITYMECH.curie("term"),
    model_uri=COMMUNITYMECH.metaboliteDescriptor__term,
    domain=None,
    range=Union[dict, Term],
)

slots.metaboliteDescriptor__concentration = Slot(
    uri=COMMUNITYMECH.concentration,
    name="metaboliteDescriptor__concentration",
    curie=COMMUNITYMECH.curie("concentration"),
    model_uri=COMMUNITYMECH.metaboliteDescriptor__concentration,
    domain=None,
    range=Optional[str],
)

slots.metaboliteDescriptor__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="metaboliteDescriptor__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.metaboliteDescriptor__notes,
    domain=None,
    range=Optional[str],
)

slots.biologicalProcessDescriptor__preferred_term = Slot(
    uri=COMMUNITYMECH.preferred_term,
    name="biologicalProcessDescriptor__preferred_term",
    curie=COMMUNITYMECH.curie("preferred_term"),
    model_uri=COMMUNITYMECH.biologicalProcessDescriptor__preferred_term,
    domain=None,
    range=str,
)

slots.biologicalProcessDescriptor__term = Slot(
    uri=COMMUNITYMECH.term,
    name="biologicalProcessDescriptor__term",
    curie=COMMUNITYMECH.curie("term"),
    model_uri=COMMUNITYMECH.biologicalProcessDescriptor__term,
    domain=None,
    range=Union[dict, Term],
)

slots.biologicalProcessDescriptor__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="biologicalProcessDescriptor__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.biologicalProcessDescriptor__notes,
    domain=None,
    range=Optional[str],
)

slots.environmentDescriptor__preferred_term = Slot(
    uri=COMMUNITYMECH.preferred_term,
    name="environmentDescriptor__preferred_term",
    curie=COMMUNITYMECH.curie("preferred_term"),
    model_uri=COMMUNITYMECH.environmentDescriptor__preferred_term,
    domain=None,
    range=str,
)

slots.environmentDescriptor__term = Slot(
    uri=COMMUNITYMECH.term,
    name="environmentDescriptor__term",
    curie=COMMUNITYMECH.curie("term"),
    model_uri=COMMUNITYMECH.environmentDescriptor__term,
    domain=None,
    range=Union[dict, Term],
)

slots.environmentDescriptor__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="environmentDescriptor__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.environmentDescriptor__notes,
    domain=None,
    range=Optional[str],
)

slots.cultureCollectionID__collection = Slot(
    uri=COMMUNITYMECH.collection,
    name="cultureCollectionID__collection",
    curie=COMMUNITYMECH.curie("collection"),
    model_uri=COMMUNITYMECH.cultureCollectionID__collection,
    domain=None,
    range=Union[str, "CultureCollectionEnum"],
)

slots.cultureCollectionID__accession = Slot(
    uri=COMMUNITYMECH.accession,
    name="cultureCollectionID__accession",
    curie=COMMUNITYMECH.curie("accession"),
    model_uri=COMMUNITYMECH.cultureCollectionID__accession,
    domain=None,
    range=str,
)

slots.cultureCollectionID__url = Slot(
    uri=COMMUNITYMECH.url,
    name="cultureCollectionID__url",
    curie=COMMUNITYMECH.curie("url"),
    model_uri=COMMUNITYMECH.cultureCollectionID__url,
    domain=None,
    range=Optional[str],
)

slots.cultureCollectionID__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="cultureCollectionID__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.cultureCollectionID__notes,
    domain=None,
    range=Optional[str],
)

slots.strainDesignation__strain_name = Slot(
    uri=COMMUNITYMECH.strain_name,
    name="strainDesignation__strain_name",
    curie=COMMUNITYMECH.curie("strain_name"),
    model_uri=COMMUNITYMECH.strainDesignation__strain_name,
    domain=None,
    range=Optional[str],
)

slots.strainDesignation__culture_collections = Slot(
    uri=COMMUNITYMECH.culture_collections,
    name="strainDesignation__culture_collections",
    curie=COMMUNITYMECH.curie("culture_collections"),
    model_uri=COMMUNITYMECH.strainDesignation__culture_collections,
    domain=None,
    range=Optional[Union[Union[dict, CultureCollectionID], list[Union[dict, CultureCollectionID]]]],
)

slots.strainDesignation__type_strain = Slot(
    uri=COMMUNITYMECH.type_strain,
    name="strainDesignation__type_strain",
    curie=COMMUNITYMECH.curie("type_strain"),
    model_uri=COMMUNITYMECH.strainDesignation__type_strain,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.strainDesignation__genome_accession = Slot(
    uri=COMMUNITYMECH.genome_accession,
    name="strainDesignation__genome_accession",
    curie=COMMUNITYMECH.curie("genome_accession"),
    model_uri=COMMUNITYMECH.strainDesignation__genome_accession,
    domain=None,
    range=Optional[str],
)

slots.strainDesignation__genome_url = Slot(
    uri=COMMUNITYMECH.genome_url,
    name="strainDesignation__genome_url",
    curie=COMMUNITYMECH.curie("genome_url"),
    model_uri=COMMUNITYMECH.strainDesignation__genome_url,
    domain=None,
    range=Optional[str],
)

slots.strainDesignation__genetic_modification = Slot(
    uri=COMMUNITYMECH.genetic_modification,
    name="strainDesignation__genetic_modification",
    curie=COMMUNITYMECH.curie("genetic_modification"),
    model_uri=COMMUNITYMECH.strainDesignation__genetic_modification,
    domain=None,
    range=Optional[str],
)

slots.strainDesignation__isolation_source = Slot(
    uri=COMMUNITYMECH.isolation_source,
    name="strainDesignation__isolation_source",
    curie=COMMUNITYMECH.curie("isolation_source"),
    model_uri=COMMUNITYMECH.strainDesignation__isolation_source,
    domain=None,
    range=Optional[str],
)

slots.strainDesignation__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="strainDesignation__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.strainDesignation__notes,
    domain=None,
    range=Optional[str],
)

slots.taxonomicComposition__taxon_term = Slot(
    uri=COMMUNITYMECH.taxon_term,
    name="taxonomicComposition__taxon_term",
    curie=COMMUNITYMECH.curie("taxon_term"),
    model_uri=COMMUNITYMECH.taxonomicComposition__taxon_term,
    domain=None,
    range=Union[dict, TaxonDescriptor],
)

slots.taxonomicComposition__strain_designation = Slot(
    uri=COMMUNITYMECH.strain_designation,
    name="taxonomicComposition__strain_designation",
    curie=COMMUNITYMECH.curie("strain_designation"),
    model_uri=COMMUNITYMECH.taxonomicComposition__strain_designation,
    domain=None,
    range=Optional[Union[dict, StrainDesignation]],
)

slots.taxonomicComposition__abundance_level = Slot(
    uri=COMMUNITYMECH.abundance_level,
    name="taxonomicComposition__abundance_level",
    curie=COMMUNITYMECH.curie("abundance_level"),
    model_uri=COMMUNITYMECH.taxonomicComposition__abundance_level,
    domain=None,
    range=Optional[Union[str, "AbundanceEnum"]],
)

slots.taxonomicComposition__abundance_value = Slot(
    uri=COMMUNITYMECH.abundance_value,
    name="taxonomicComposition__abundance_value",
    curie=COMMUNITYMECH.curie("abundance_value"),
    model_uri=COMMUNITYMECH.taxonomicComposition__abundance_value,
    domain=None,
    range=Optional[str],
)

slots.taxonomicComposition__absolute_abundance = Slot(
    uri=COMMUNITYMECH.absolute_abundance,
    name="taxonomicComposition__absolute_abundance",
    curie=COMMUNITYMECH.curie("absolute_abundance"),
    model_uri=COMMUNITYMECH.taxonomicComposition__absolute_abundance,
    domain=None,
    range=Optional[float],
)

slots.taxonomicComposition__absolute_abundance_unit = Slot(
    uri=COMMUNITYMECH.absolute_abundance_unit,
    name="taxonomicComposition__absolute_abundance_unit",
    curie=COMMUNITYMECH.curie("absolute_abundance_unit"),
    model_uri=COMMUNITYMECH.taxonomicComposition__absolute_abundance_unit,
    domain=None,
    range=Optional[str],
)

slots.taxonomicComposition__relative_abundance = Slot(
    uri=COMMUNITYMECH.relative_abundance,
    name="taxonomicComposition__relative_abundance",
    curie=COMMUNITYMECH.curie("relative_abundance"),
    model_uri=COMMUNITYMECH.taxonomicComposition__relative_abundance,
    domain=None,
    range=Optional[float],
)

slots.taxonomicComposition__relative_abundance_unit = Slot(
    uri=COMMUNITYMECH.relative_abundance_unit,
    name="taxonomicComposition__relative_abundance_unit",
    curie=COMMUNITYMECH.curie("relative_abundance_unit"),
    model_uri=COMMUNITYMECH.taxonomicComposition__relative_abundance_unit,
    domain=None,
    range=Optional[str],
)

slots.taxonomicComposition__common_taxon = Slot(
    uri=COMMUNITYMECH.common_taxon,
    name="taxonomicComposition__common_taxon",
    curie=COMMUNITYMECH.curie("common_taxon"),
    model_uri=COMMUNITYMECH.taxonomicComposition__common_taxon,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^CommunityMech:taxon:\d{6}$"),
)

slots.taxonomicComposition__functional_role = Slot(
    uri=COMMUNITYMECH.functional_role,
    name="taxonomicComposition__functional_role",
    curie=COMMUNITYMECH.curie("functional_role"),
    model_uri=COMMUNITYMECH.taxonomicComposition__functional_role,
    domain=None,
    range=Optional[Union[Union[str, "FunctionalRoleEnum"], list[Union[str, "FunctionalRoleEnum"]]]],
)

slots.taxonomicComposition__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="taxonomicComposition__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.taxonomicComposition__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.interactionDownstream__target = Slot(
    uri=COMMUNITYMECH.target,
    name="interactionDownstream__target",
    curie=COMMUNITYMECH.curie("target"),
    model_uri=COMMUNITYMECH.interactionDownstream__target,
    domain=None,
    range=str,
)

slots.interactionDownstream__description = Slot(
    uri=COMMUNITYMECH.description,
    name="interactionDownstream__description",
    curie=COMMUNITYMECH.curie("description"),
    model_uri=COMMUNITYMECH.interactionDownstream__description,
    domain=None,
    range=Optional[str],
)

slots.ecologicalInteraction__name = Slot(
    uri=COMMUNITYMECH.name,
    name="ecologicalInteraction__name",
    curie=COMMUNITYMECH.curie("name"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__name,
    domain=None,
    range=str,
)

slots.ecologicalInteraction__description = Slot(
    uri=COMMUNITYMECH.description,
    name="ecologicalInteraction__description",
    curie=COMMUNITYMECH.curie("description"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__description,
    domain=None,
    range=Optional[str],
)

slots.ecologicalInteraction__interaction_type = Slot(
    uri=COMMUNITYMECH.interaction_type,
    name="ecologicalInteraction__interaction_type",
    curie=COMMUNITYMECH.curie("interaction_type"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__interaction_type,
    domain=None,
    range=Optional[Union[str, "InteractionTypeEnum"]],
)

slots.ecologicalInteraction__scope = Slot(
    uri=COMMUNITYMECH.scope,
    name="ecologicalInteraction__scope",
    curie=COMMUNITYMECH.curie("scope"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__scope,
    domain=None,
    range=Optional[Union[str, "InteractionScopeEnum"]],
)

slots.ecologicalInteraction__source_taxon = Slot(
    uri=COMMUNITYMECH.source_taxon,
    name="ecologicalInteraction__source_taxon",
    curie=COMMUNITYMECH.curie("source_taxon"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__source_taxon,
    domain=None,
    range=Optional[Union[dict, TaxonDescriptor]],
)

slots.ecologicalInteraction__target_taxon = Slot(
    uri=COMMUNITYMECH.target_taxon,
    name="ecologicalInteraction__target_taxon",
    curie=COMMUNITYMECH.curie("target_taxon"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__target_taxon,
    domain=None,
    range=Optional[Union[dict, TaxonDescriptor]],
)

slots.ecologicalInteraction__metabolites = Slot(
    uri=COMMUNITYMECH.metabolites,
    name="ecologicalInteraction__metabolites",
    curie=COMMUNITYMECH.curie("metabolites"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__metabolites,
    domain=None,
    range=Optional[
        Union[Union[dict, MetaboliteDescriptor], list[Union[dict, MetaboliteDescriptor]]]
    ],
)

slots.ecologicalInteraction__biological_processes = Slot(
    uri=COMMUNITYMECH.biological_processes,
    name="ecologicalInteraction__biological_processes",
    curie=COMMUNITYMECH.curie("biological_processes"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__biological_processes,
    domain=None,
    range=Optional[
        Union[
            Union[dict, BiologicalProcessDescriptor], list[Union[dict, BiologicalProcessDescriptor]]
        ]
    ],
)

slots.ecologicalInteraction__downstream = Slot(
    uri=COMMUNITYMECH.downstream,
    name="ecologicalInteraction__downstream",
    curie=COMMUNITYMECH.curie("downstream"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__downstream,
    domain=None,
    range=Optional[
        Union[Union[dict, InteractionDownstream], list[Union[dict, InteractionDownstream]]]
    ],
)

slots.ecologicalInteraction__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="ecologicalInteraction__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.ecologicalInteraction__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.environmentalFactor__name = Slot(
    uri=COMMUNITYMECH.name,
    name="environmentalFactor__name",
    curie=COMMUNITYMECH.curie("name"),
    model_uri=COMMUNITYMECH.environmentalFactor__name,
    domain=None,
    range=str,
)

slots.environmentalFactor__value = Slot(
    uri=COMMUNITYMECH.value,
    name="environmentalFactor__value",
    curie=COMMUNITYMECH.curie("value"),
    model_uri=COMMUNITYMECH.environmentalFactor__value,
    domain=None,
    range=Optional[str],
)

slots.environmentalFactor__unit = Slot(
    uri=COMMUNITYMECH.unit,
    name="environmentalFactor__unit",
    curie=COMMUNITYMECH.curie("unit"),
    model_uri=COMMUNITYMECH.environmentalFactor__unit,
    domain=None,
    range=Optional[str],
)

slots.environmentalFactor__description = Slot(
    uri=COMMUNITYMECH.description,
    name="environmentalFactor__description",
    curie=COMMUNITYMECH.curie("description"),
    model_uri=COMMUNITYMECH.environmentalFactor__description,
    domain=None,
    range=Optional[str],
)

slots.environmentalFactor__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="environmentalFactor__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.environmentalFactor__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.growthMediaComponent__name = Slot(
    uri=COMMUNITYMECH.name,
    name="growthMediaComponent__name",
    curie=COMMUNITYMECH.curie("name"),
    model_uri=COMMUNITYMECH.growthMediaComponent__name,
    domain=None,
    range=str,
)

slots.growthMediaComponent__media_ingredient_mech_id = Slot(
    uri=COMMUNITYMECH.media_ingredient_mech_id,
    name="growthMediaComponent__media_ingredient_mech_id",
    curie=COMMUNITYMECH.curie("media_ingredient_mech_id"),
    model_uri=COMMUNITYMECH.growthMediaComponent__media_ingredient_mech_id,
    domain=None,
    range=Optional[str],
)

slots.growthMediaComponent__media_ingredient_mech_url = Slot(
    uri=COMMUNITYMECH.media_ingredient_mech_url,
    name="growthMediaComponent__media_ingredient_mech_url",
    curie=COMMUNITYMECH.curie("media_ingredient_mech_url"),
    model_uri=COMMUNITYMECH.growthMediaComponent__media_ingredient_mech_url,
    domain=None,
    range=Optional[str],
)

slots.growthMediaComponent__concentration = Slot(
    uri=COMMUNITYMECH.concentration,
    name="growthMediaComponent__concentration",
    curie=COMMUNITYMECH.curie("concentration"),
    model_uri=COMMUNITYMECH.growthMediaComponent__concentration,
    domain=None,
    range=Optional[str],
)

slots.growthMediaComponent__unit = Slot(
    uri=COMMUNITYMECH.unit,
    name="growthMediaComponent__unit",
    curie=COMMUNITYMECH.curie("unit"),
    model_uri=COMMUNITYMECH.growthMediaComponent__unit,
    domain=None,
    range=Optional[str],
)

slots.growthMediaComponent__chebi_term = Slot(
    uri=COMMUNITYMECH.chebi_term,
    name="growthMediaComponent__chebi_term",
    curie=COMMUNITYMECH.curie("chebi_term"),
    model_uri=COMMUNITYMECH.growthMediaComponent__chebi_term,
    domain=None,
    range=Optional[Union[dict, MetaboliteDescriptor]],
)

slots.growthMediaComponent__from_source = Slot(
    uri=COMMUNITYMECH.from_source,
    name="growthMediaComponent__from_source",
    curie=COMMUNITYMECH.curie("from_source"),
    model_uri=COMMUNITYMECH.growthMediaComponent__from_source,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__name = Slot(
    uri=COMMUNITYMECH.name,
    name="growthMedia__name",
    curie=COMMUNITYMECH.curie("name"),
    model_uri=COMMUNITYMECH.growthMedia__name,
    domain=None,
    range=str,
)

slots.growthMedia__culturemech_id = Slot(
    uri=COMMUNITYMECH.culturemech_id,
    name="growthMedia__culturemech_id",
    curie=COMMUNITYMECH.curie("culturemech_id"),
    model_uri=COMMUNITYMECH.growthMedia__culturemech_id,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^CultureMech:\d{6}$"),
)

slots.growthMedia__culturemech_url = Slot(
    uri=COMMUNITYMECH.culturemech_url,
    name="growthMedia__culturemech_url",
    curie=COMMUNITYMECH.curie("culturemech_url"),
    model_uri=COMMUNITYMECH.growthMedia__culturemech_url,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__composition = Slot(
    uri=COMMUNITYMECH.composition,
    name="growthMedia__composition",
    curie=COMMUNITYMECH.curie("composition"),
    model_uri=COMMUNITYMECH.growthMedia__composition,
    domain=None,
    range=Optional[
        Union[Union[dict, GrowthMediaComponent], list[Union[dict, GrowthMediaComponent]]]
    ],
)

slots.growthMedia__ph = Slot(
    uri=COMMUNITYMECH.ph,
    name="growthMedia__ph",
    curie=COMMUNITYMECH.curie("ph"),
    model_uri=COMMUNITYMECH.growthMedia__ph,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__ph_range = Slot(
    uri=COMMUNITYMECH.ph_range,
    name="growthMedia__ph_range",
    curie=COMMUNITYMECH.curie("ph_range"),
    model_uri=COMMUNITYMECH.growthMedia__ph_range,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__temperature = Slot(
    uri=COMMUNITYMECH.temperature,
    name="growthMedia__temperature",
    curie=COMMUNITYMECH.curie("temperature"),
    model_uri=COMMUNITYMECH.growthMedia__temperature,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__temperature_unit = Slot(
    uri=COMMUNITYMECH.temperature_unit,
    name="growthMedia__temperature_unit",
    curie=COMMUNITYMECH.curie("temperature_unit"),
    model_uri=COMMUNITYMECH.growthMedia__temperature_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__temperature_range = Slot(
    uri=COMMUNITYMECH.temperature_range,
    name="growthMedia__temperature_range",
    curie=COMMUNITYMECH.curie("temperature_range"),
    model_uri=COMMUNITYMECH.growthMedia__temperature_range,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__atmosphere = Slot(
    uri=COMMUNITYMECH.atmosphere,
    name="growthMedia__atmosphere",
    curie=COMMUNITYMECH.curie("atmosphere"),
    model_uri=COMMUNITYMECH.growthMedia__atmosphere,
    domain=None,
    range=Optional[Union[str, "AtmosphereEnum"]],
)

slots.growthMedia__headspace_gas = Slot(
    uri=COMMUNITYMECH.headspace_gas,
    name="growthMedia__headspace_gas",
    curie=COMMUNITYMECH.curie("headspace_gas"),
    model_uri=COMMUNITYMECH.growthMedia__headspace_gas,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__salinity = Slot(
    uri=COMMUNITYMECH.salinity,
    name="growthMedia__salinity",
    curie=COMMUNITYMECH.curie("salinity"),
    model_uri=COMMUNITYMECH.growthMedia__salinity,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__salinity_unit = Slot(
    uri=COMMUNITYMECH.salinity_unit,
    name="growthMedia__salinity_unit",
    curie=COMMUNITYMECH.curie("salinity_unit"),
    model_uri=COMMUNITYMECH.growthMedia__salinity_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__pressure = Slot(
    uri=COMMUNITYMECH.pressure,
    name="growthMedia__pressure",
    curie=COMMUNITYMECH.curie("pressure"),
    model_uri=COMMUNITYMECH.growthMedia__pressure,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__pressure_unit = Slot(
    uri=COMMUNITYMECH.pressure_unit,
    name="growthMedia__pressure_unit",
    curie=COMMUNITYMECH.curie("pressure_unit"),
    model_uri=COMMUNITYMECH.growthMedia__pressure_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__light_regime = Slot(
    uri=COMMUNITYMECH.light_regime,
    name="growthMedia__light_regime",
    curie=COMMUNITYMECH.curie("light_regime"),
    model_uri=COMMUNITYMECH.growthMedia__light_regime,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__light_intensity = Slot(
    uri=COMMUNITYMECH.light_intensity,
    name="growthMedia__light_intensity",
    curie=COMMUNITYMECH.curie("light_intensity"),
    model_uri=COMMUNITYMECH.growthMedia__light_intensity,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__light_intensity_unit = Slot(
    uri=COMMUNITYMECH.light_intensity_unit,
    name="growthMedia__light_intensity_unit",
    curie=COMMUNITYMECH.curie("light_intensity_unit"),
    model_uri=COMMUNITYMECH.growthMedia__light_intensity_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__redox_potential = Slot(
    uri=COMMUNITYMECH.redox_potential,
    name="growthMedia__redox_potential",
    curie=COMMUNITYMECH.curie("redox_potential"),
    model_uri=COMMUNITYMECH.growthMedia__redox_potential,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__redox_potential_unit = Slot(
    uri=COMMUNITYMECH.redox_potential_unit,
    name="growthMedia__redox_potential_unit",
    curie=COMMUNITYMECH.curie("redox_potential_unit"),
    model_uri=COMMUNITYMECH.growthMedia__redox_potential_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__inoculum_source = Slot(
    uri=COMMUNITYMECH.inoculum_source,
    name="growthMedia__inoculum_source",
    curie=COMMUNITYMECH.curie("inoculum_source"),
    model_uri=COMMUNITYMECH.growthMedia__inoculum_source,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__inoculum_size = Slot(
    uri=COMMUNITYMECH.inoculum_size,
    name="growthMedia__inoculum_size",
    curie=COMMUNITYMECH.curie("inoculum_size"),
    model_uri=COMMUNITYMECH.growthMedia__inoculum_size,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__inoculum_unit = Slot(
    uri=COMMUNITYMECH.inoculum_unit,
    name="growthMedia__inoculum_unit",
    curie=COMMUNITYMECH.curie("inoculum_unit"),
    model_uri=COMMUNITYMECH.growthMedia__inoculum_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__incubation_time = Slot(
    uri=COMMUNITYMECH.incubation_time,
    name="growthMedia__incubation_time",
    curie=COMMUNITYMECH.curie("incubation_time"),
    model_uri=COMMUNITYMECH.growthMedia__incubation_time,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__incubation_time_unit = Slot(
    uri=COMMUNITYMECH.incubation_time_unit,
    name="growthMedia__incubation_time_unit",
    curie=COMMUNITYMECH.curie("incubation_time_unit"),
    model_uri=COMMUNITYMECH.growthMedia__incubation_time_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__shaking_speed = Slot(
    uri=COMMUNITYMECH.shaking_speed,
    name="growthMedia__shaking_speed",
    curie=COMMUNITYMECH.curie("shaking_speed"),
    model_uri=COMMUNITYMECH.growthMedia__shaking_speed,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__shaking_speed_unit = Slot(
    uri=COMMUNITYMECH.shaking_speed_unit,
    name="growthMedia__shaking_speed_unit",
    curie=COMMUNITYMECH.curie("shaking_speed_unit"),
    model_uri=COMMUNITYMECH.growthMedia__shaking_speed_unit,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__vessel_type = Slot(
    uri=COMMUNITYMECH.vessel_type,
    name="growthMedia__vessel_type",
    curie=COMMUNITYMECH.curie("vessel_type"),
    model_uri=COMMUNITYMECH.growthMedia__vessel_type,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__preparation_notes = Slot(
    uri=COMMUNITYMECH.preparation_notes,
    name="growthMedia__preparation_notes",
    curie=COMMUNITYMECH.curie("preparation_notes"),
    model_uri=COMMUNITYMECH.growthMedia__preparation_notes,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__protocol_url = Slot(
    uri=COMMUNITYMECH.protocol_url,
    name="growthMedia__protocol_url",
    curie=COMMUNITYMECH.curie("protocol_url"),
    model_uri=COMMUNITYMECH.growthMedia__protocol_url,
    domain=None,
    range=Optional[str],
)

slots.growthMedia__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="growthMedia__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.growthMedia__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.relatedMedia__preferred_term = Slot(
    uri=COMMUNITYMECH.preferred_term,
    name="relatedMedia__preferred_term",
    curie=COMMUNITYMECH.curie("preferred_term"),
    model_uri=COMMUNITYMECH.relatedMedia__preferred_term,
    domain=None,
    range=str,
)

slots.relatedMedia__culturemech_id = Slot(
    uri=COMMUNITYMECH.culturemech_id,
    name="relatedMedia__culturemech_id",
    curie=COMMUNITYMECH.curie("culturemech_id"),
    model_uri=COMMUNITYMECH.relatedMedia__culturemech_id,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^CultureMech:\d{6}$"),
)

slots.relatedMedia__relationship_type = Slot(
    uri=COMMUNITYMECH.relationship_type,
    name="relatedMedia__relationship_type",
    curie=COMMUNITYMECH.curie("relationship_type"),
    model_uri=COMMUNITYMECH.relatedMedia__relationship_type,
    domain=None,
    range=Optional[Union[str, "MediaRelationshipEnum"]],
)

slots.relatedMedia__shared_environment_term = Slot(
    uri=COMMUNITYMECH.shared_environment_term,
    name="relatedMedia__shared_environment_term",
    curie=COMMUNITYMECH.curie("shared_environment_term"),
    model_uri=COMMUNITYMECH.relatedMedia__shared_environment_term,
    domain=None,
    range=Optional[Union[dict, Term]],
)

slots.relatedMedia__relevance_notes = Slot(
    uri=COMMUNITYMECH.relevance_notes,
    name="relatedMedia__relevance_notes",
    curie=COMMUNITYMECH.curie("relevance_notes"),
    model_uri=COMMUNITYMECH.relatedMedia__relevance_notes,
    domain=None,
    range=Optional[str],
)

slots.relatedMedia__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="relatedMedia__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.relatedMedia__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.relatedIngredient__preferred_term = Slot(
    uri=COMMUNITYMECH.preferred_term,
    name="relatedIngredient__preferred_term",
    curie=COMMUNITYMECH.curie("preferred_term"),
    model_uri=COMMUNITYMECH.relatedIngredient__preferred_term,
    domain=None,
    range=str,
)

slots.relatedIngredient__mediaingredientmech_id = Slot(
    uri=COMMUNITYMECH.mediaingredientmech_id,
    name="relatedIngredient__mediaingredientmech_id",
    curie=COMMUNITYMECH.curie("mediaingredientmech_id"),
    model_uri=COMMUNITYMECH.relatedIngredient__mediaingredientmech_id,
    domain=None,
    range=Optional[str],
)

slots.relatedIngredient__chebi_term = Slot(
    uri=COMMUNITYMECH.chebi_term,
    name="relatedIngredient__chebi_term",
    curie=COMMUNITYMECH.curie("chebi_term"),
    model_uri=COMMUNITYMECH.relatedIngredient__chebi_term,
    domain=None,
    range=Optional[Union[dict, Term]],
)

slots.relatedIngredient__shared_environment_term = Slot(
    uri=COMMUNITYMECH.shared_environment_term,
    name="relatedIngredient__shared_environment_term",
    curie=COMMUNITYMECH.curie("shared_environment_term"),
    model_uri=COMMUNITYMECH.relatedIngredient__shared_environment_term,
    domain=None,
    range=Optional[Union[dict, Term]],
)

slots.relatedIngredient__relevance = Slot(
    uri=COMMUNITYMECH.relevance,
    name="relatedIngredient__relevance",
    curie=COMMUNITYMECH.curie("relevance"),
    model_uri=COMMUNITYMECH.relatedIngredient__relevance,
    domain=None,
    range=Optional[str],
)

slots.relatedIngredient__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="relatedIngredient__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.relatedIngredient__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.externalResource__name = Slot(
    uri=COMMUNITYMECH.name,
    name="externalResource__name",
    curie=COMMUNITYMECH.curie("name"),
    model_uri=COMMUNITYMECH.externalResource__name,
    domain=None,
    range=str,
)

slots.externalResource__repository = Slot(
    uri=COMMUNITYMECH.repository,
    name="externalResource__repository",
    curie=COMMUNITYMECH.curie("repository"),
    model_uri=COMMUNITYMECH.externalResource__repository,
    domain=None,
    range=Union[str, "ExternalResourceRepositoryEnum"],
)

slots.externalResource__resource_id = Slot(
    uri=COMMUNITYMECH.resource_id,
    name="externalResource__resource_id",
    curie=COMMUNITYMECH.curie("resource_id"),
    model_uri=COMMUNITYMECH.externalResource__resource_id,
    domain=None,
    range=str,
)

slots.externalResource__url = Slot(
    uri=COMMUNITYMECH.url,
    name="externalResource__url",
    curie=COMMUNITYMECH.curie("url"),
    model_uri=COMMUNITYMECH.externalResource__url,
    domain=None,
    range=str,
)

slots.externalResource__description = Slot(
    uri=COMMUNITYMECH.description,
    name="externalResource__description",
    curie=COMMUNITYMECH.curie("description"),
    model_uri=COMMUNITYMECH.externalResource__description,
    domain=None,
    range=Optional[str],
)

slots.externalResource__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="externalResource__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.externalResource__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.communityEngineeringDesign__objective = Slot(
    uri=COMMUNITYMECH.objective,
    name="communityEngineeringDesign__objective",
    curie=COMMUNITYMECH.curie("objective"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__objective,
    domain=None,
    range=Optional[str],
)

slots.communityEngineeringDesign__assembly_strategy = Slot(
    uri=COMMUNITYMECH.assembly_strategy,
    name="communityEngineeringDesign__assembly_strategy",
    curie=COMMUNITYMECH.curie("assembly_strategy"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__assembly_strategy,
    domain=None,
    range=Optional[str],
)

slots.communityEngineeringDesign__inoculation_strategy = Slot(
    uri=COMMUNITYMECH.inoculation_strategy,
    name="communityEngineeringDesign__inoculation_strategy",
    curie=COMMUNITYMECH.curie("inoculation_strategy"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__inoculation_strategy,
    domain=None,
    range=Optional[str],
)

slots.communityEngineeringDesign__passaging_regimen = Slot(
    uri=COMMUNITYMECH.passaging_regimen,
    name="communityEngineeringDesign__passaging_regimen",
    curie=COMMUNITYMECH.curie("passaging_regimen"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__passaging_regimen,
    domain=None,
    range=Optional[str],
)

slots.communityEngineeringDesign__perturbation_design = Slot(
    uri=COMMUNITYMECH.perturbation_design,
    name="communityEngineeringDesign__perturbation_design",
    curie=COMMUNITYMECH.curie("perturbation_design"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__perturbation_design,
    domain=None,
    range=Optional[str],
)

slots.communityEngineeringDesign__measurement_endpoints = Slot(
    uri=COMMUNITYMECH.measurement_endpoints,
    name="communityEngineeringDesign__measurement_endpoints",
    curie=COMMUNITYMECH.curie("measurement_endpoints"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__measurement_endpoints,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.communityEngineeringDesign__protocol_url = Slot(
    uri=COMMUNITYMECH.protocol_url,
    name="communityEngineeringDesign__protocol_url",
    curie=COMMUNITYMECH.curie("protocol_url"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__protocol_url,
    domain=None,
    range=Optional[str],
)

slots.communityEngineeringDesign__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="communityEngineeringDesign__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__notes,
    domain=None,
    range=Optional[str],
)

slots.communityEngineeringDesign__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="communityEngineeringDesign__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.communityEngineeringDesign__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.cultivationSetup__cultivation_mode = Slot(
    uri=COMMUNITYMECH.cultivation_mode,
    name="cultivationSetup__cultivation_mode",
    curie=COMMUNITYMECH.curie("cultivation_mode"),
    model_uri=COMMUNITYMECH.cultivationSetup__cultivation_mode,
    domain=None,
    range=Optional[Union[str, "CultivationModeEnum"]],
)

slots.cultivationSetup__system_type = Slot(
    uri=COMMUNITYMECH.system_type,
    name="cultivationSetup__system_type",
    curie=COMMUNITYMECH.curie("system_type"),
    model_uri=COMMUNITYMECH.cultivationSetup__system_type,
    domain=None,
    range=Optional[Union[str, "CultivationSystemEnum"]],
)

slots.cultivationSetup__instrument_detail = Slot(
    uri=COMMUNITYMECH.instrument_detail,
    name="cultivationSetup__instrument_detail",
    curie=COMMUNITYMECH.curie("instrument_detail"),
    model_uri=COMMUNITYMECH.cultivationSetup__instrument_detail,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__manufacturer_model = Slot(
    uri=COMMUNITYMECH.manufacturer_model,
    name="cultivationSetup__manufacturer_model",
    curie=COMMUNITYMECH.curie("manufacturer_model"),
    model_uri=COMMUNITYMECH.cultivationSetup__manufacturer_model,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__working_volume = Slot(
    uri=COMMUNITYMECH.working_volume,
    name="cultivationSetup__working_volume",
    curie=COMMUNITYMECH.curie("working_volume"),
    model_uri=COMMUNITYMECH.cultivationSetup__working_volume,
    domain=None,
    range=Optional[float],
)

slots.cultivationSetup__working_volume_unit = Slot(
    uri=COMMUNITYMECH.working_volume_unit,
    name="cultivationSetup__working_volume_unit",
    curie=COMMUNITYMECH.curie("working_volume_unit"),
    model_uri=COMMUNITYMECH.cultivationSetup__working_volume_unit,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__operating_temperature = Slot(
    uri=COMMUNITYMECH.operating_temperature,
    name="cultivationSetup__operating_temperature",
    curie=COMMUNITYMECH.curie("operating_temperature"),
    model_uri=COMMUNITYMECH.cultivationSetup__operating_temperature,
    domain=None,
    range=Optional[float],
)

slots.cultivationSetup__operating_temperature_unit = Slot(
    uri=COMMUNITYMECH.operating_temperature_unit,
    name="cultivationSetup__operating_temperature_unit",
    curie=COMMUNITYMECH.curie("operating_temperature_unit"),
    model_uri=COMMUNITYMECH.cultivationSetup__operating_temperature_unit,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__feed_or_dilution_rate = Slot(
    uri=COMMUNITYMECH.feed_or_dilution_rate,
    name="cultivationSetup__feed_or_dilution_rate",
    curie=COMMUNITYMECH.curie("feed_or_dilution_rate"),
    model_uri=COMMUNITYMECH.cultivationSetup__feed_or_dilution_rate,
    domain=None,
    range=Optional[float],
)

slots.cultivationSetup__feed_or_dilution_rate_unit = Slot(
    uri=COMMUNITYMECH.feed_or_dilution_rate_unit,
    name="cultivationSetup__feed_or_dilution_rate_unit",
    curie=COMMUNITYMECH.curie("feed_or_dilution_rate_unit"),
    model_uri=COMMUNITYMECH.cultivationSetup__feed_or_dilution_rate_unit,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__retention_time = Slot(
    uri=COMMUNITYMECH.retention_time,
    name="cultivationSetup__retention_time",
    curie=COMMUNITYMECH.curie("retention_time"),
    model_uri=COMMUNITYMECH.cultivationSetup__retention_time,
    domain=None,
    range=Optional[float],
)

slots.cultivationSetup__retention_time_unit = Slot(
    uri=COMMUNITYMECH.retention_time_unit,
    name="cultivationSetup__retention_time_unit",
    curie=COMMUNITYMECH.curie("retention_time_unit"),
    model_uri=COMMUNITYMECH.cultivationSetup__retention_time_unit,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__retention_time_type = Slot(
    uri=COMMUNITYMECH.retention_time_type,
    name="cultivationSetup__retention_time_type",
    curie=COMMUNITYMECH.curie("retention_time_type"),
    model_uri=COMMUNITYMECH.cultivationSetup__retention_time_type,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__applied_potential = Slot(
    uri=COMMUNITYMECH.applied_potential,
    name="cultivationSetup__applied_potential",
    curie=COMMUNITYMECH.curie("applied_potential"),
    model_uri=COMMUNITYMECH.cultivationSetup__applied_potential,
    domain=None,
    range=Optional[float],
)

slots.cultivationSetup__applied_potential_unit = Slot(
    uri=COMMUNITYMECH.applied_potential_unit,
    name="cultivationSetup__applied_potential_unit",
    curie=COMMUNITYMECH.curie("applied_potential_unit"),
    model_uri=COMMUNITYMECH.cultivationSetup__applied_potential_unit,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__electrode_detail = Slot(
    uri=COMMUNITYMECH.electrode_detail,
    name="cultivationSetup__electrode_detail",
    curie=COMMUNITYMECH.curie("electrode_detail"),
    model_uri=COMMUNITYMECH.cultivationSetup__electrode_detail,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__ph_controlled = Slot(
    uri=COMMUNITYMECH.ph_controlled,
    name="cultivationSetup__ph_controlled",
    curie=COMMUNITYMECH.curie("ph_controlled"),
    model_uri=COMMUNITYMECH.cultivationSetup__ph_controlled,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.cultivationSetup__do_controlled = Slot(
    uri=COMMUNITYMECH.do_controlled,
    name="cultivationSetup__do_controlled",
    curie=COMMUNITYMECH.curie("do_controlled"),
    model_uri=COMMUNITYMECH.cultivationSetup__do_controlled,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.cultivationSetup__temperature_controlled = Slot(
    uri=COMMUNITYMECH.temperature_controlled,
    name="cultivationSetup__temperature_controlled",
    curie=COMMUNITYMECH.curie("temperature_controlled"),
    model_uri=COMMUNITYMECH.cultivationSetup__temperature_controlled,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.cultivationSetup__controls_notes = Slot(
    uri=COMMUNITYMECH.controls_notes,
    name="cultivationSetup__controls_notes",
    curie=COMMUNITYMECH.curie("controls_notes"),
    model_uri=COMMUNITYMECH.cultivationSetup__controls_notes,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__protocol_url = Slot(
    uri=COMMUNITYMECH.protocol_url,
    name="cultivationSetup__protocol_url",
    curie=COMMUNITYMECH.curie("protocol_url"),
    model_uri=COMMUNITYMECH.cultivationSetup__protocol_url,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="cultivationSetup__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.cultivationSetup__notes,
    domain=None,
    range=Optional[str],
)

slots.cultivationSetup__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="cultivationSetup__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.cultivationSetup__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.microbialCommunity__id = Slot(
    uri=COMMUNITYMECH.id,
    name="microbialCommunity__id",
    curie=COMMUNITYMECH.curie("id"),
    model_uri=COMMUNITYMECH.microbialCommunity__id,
    domain=None,
    range=URIRef,
    pattern=re.compile(r"^CommunityMech:\d{6}$"),
)

slots.microbialCommunity__name = Slot(
    uri=COMMUNITYMECH.name,
    name="microbialCommunity__name",
    curie=COMMUNITYMECH.curie("name"),
    model_uri=COMMUNITYMECH.microbialCommunity__name,
    domain=None,
    range=str,
)

slots.microbialCommunity__description = Slot(
    uri=COMMUNITYMECH.description,
    name="microbialCommunity__description",
    curie=COMMUNITYMECH.curie("description"),
    model_uri=COMMUNITYMECH.microbialCommunity__description,
    domain=None,
    range=Optional[str],
)

slots.microbialCommunity__ecological_state = Slot(
    uri=COMMUNITYMECH.ecological_state,
    name="microbialCommunity__ecological_state",
    curie=COMMUNITYMECH.curie("ecological_state"),
    model_uri=COMMUNITYMECH.microbialCommunity__ecological_state,
    domain=None,
    range=Optional[Union[str, "EcologicalStateEnum"]],
)

slots.microbialCommunity__community_origin = Slot(
    uri=COMMUNITYMECH.community_origin,
    name="microbialCommunity__community_origin",
    curie=COMMUNITYMECH.curie("community_origin"),
    model_uri=COMMUNITYMECH.microbialCommunity__community_origin,
    domain=None,
    range=Optional[Union[str, "CommunityOriginEnum"]],
)

slots.microbialCommunity__community_category = Slot(
    uri=COMMUNITYMECH.community_category,
    name="microbialCommunity__community_category",
    curie=COMMUNITYMECH.curie("community_category"),
    model_uri=COMMUNITYMECH.microbialCommunity__community_category,
    domain=None,
    range=Optional[Union[str, "CommunityCategoryEnum"]],
)

slots.microbialCommunity__engineering_design = Slot(
    uri=COMMUNITYMECH.engineering_design,
    name="microbialCommunity__engineering_design",
    curie=COMMUNITYMECH.curie("engineering_design"),
    model_uri=COMMUNITYMECH.microbialCommunity__engineering_design,
    domain=None,
    range=Optional[Union[dict, CommunityEngineeringDesign]],
)

slots.microbialCommunity__environment_term = Slot(
    uri=COMMUNITYMECH.environment_term,
    name="microbialCommunity__environment_term",
    curie=COMMUNITYMECH.curie("environment_term"),
    model_uri=COMMUNITYMECH.microbialCommunity__environment_term,
    domain=None,
    range=Optional[Union[dict, EnvironmentDescriptor]],
)

slots.microbialCommunity__modeled_environment = Slot(
    uri=COMMUNITYMECH.modeled_environment,
    name="microbialCommunity__modeled_environment",
    curie=COMMUNITYMECH.curie("modeled_environment"),
    model_uri=COMMUNITYMECH.microbialCommunity__modeled_environment,
    domain=None,
    range=Optional[
        Union[Union[dict, EnvironmentDescriptor], list[Union[dict, EnvironmentDescriptor]]]
    ],
)

slots.microbialCommunity__taxonomy = Slot(
    uri=COMMUNITYMECH.taxonomy,
    name="microbialCommunity__taxonomy",
    curie=COMMUNITYMECH.curie("taxonomy"),
    model_uri=COMMUNITYMECH.microbialCommunity__taxonomy,
    domain=None,
    range=Optional[
        Union[Union[dict, TaxonomicComposition], list[Union[dict, TaxonomicComposition]]]
    ],
)

slots.microbialCommunity__ecological_interactions = Slot(
    uri=COMMUNITYMECH.ecological_interactions,
    name="microbialCommunity__ecological_interactions",
    curie=COMMUNITYMECH.curie("ecological_interactions"),
    model_uri=COMMUNITYMECH.microbialCommunity__ecological_interactions,
    domain=None,
    range=Optional[
        Union[Union[dict, EcologicalInteraction], list[Union[dict, EcologicalInteraction]]]
    ],
)

slots.microbialCommunity__environmental_factors = Slot(
    uri=COMMUNITYMECH.environmental_factors,
    name="microbialCommunity__environmental_factors",
    curie=COMMUNITYMECH.curie("environmental_factors"),
    model_uri=COMMUNITYMECH.microbialCommunity__environmental_factors,
    domain=None,
    range=Optional[Union[Union[dict, EnvironmentalFactor], list[Union[dict, EnvironmentalFactor]]]],
)

slots.microbialCommunity__growth_media = Slot(
    uri=COMMUNITYMECH.growth_media,
    name="microbialCommunity__growth_media",
    curie=COMMUNITYMECH.curie("growth_media"),
    model_uri=COMMUNITYMECH.microbialCommunity__growth_media,
    domain=None,
    range=Optional[Union[Union[dict, GrowthMedia], list[Union[dict, GrowthMedia]]]],
)

slots.microbialCommunity__cultivation_setup = Slot(
    uri=COMMUNITYMECH.cultivation_setup,
    name="microbialCommunity__cultivation_setup",
    curie=COMMUNITYMECH.curie("cultivation_setup"),
    model_uri=COMMUNITYMECH.microbialCommunity__cultivation_setup,
    domain=None,
    range=Optional[Union[Union[dict, CultivationSetup], list[Union[dict, CultivationSetup]]]],
)

slots.microbialCommunity__related_media = Slot(
    uri=COMMUNITYMECH.related_media,
    name="microbialCommunity__related_media",
    curie=COMMUNITYMECH.curie("related_media"),
    model_uri=COMMUNITYMECH.microbialCommunity__related_media,
    domain=None,
    range=Optional[Union[Union[dict, RelatedMedia], list[Union[dict, RelatedMedia]]]],
)

slots.microbialCommunity__related_ingredients = Slot(
    uri=COMMUNITYMECH.related_ingredients,
    name="microbialCommunity__related_ingredients",
    curie=COMMUNITYMECH.curie("related_ingredients"),
    model_uri=COMMUNITYMECH.microbialCommunity__related_ingredients,
    domain=None,
    range=Optional[Union[Union[dict, RelatedIngredient], list[Union[dict, RelatedIngredient]]]],
)

slots.microbialCommunity__associated_datasets = Slot(
    uri=COMMUNITYMECH.associated_datasets,
    name="microbialCommunity__associated_datasets",
    curie=COMMUNITYMECH.curie("associated_datasets"),
    model_uri=COMMUNITYMECH.microbialCommunity__associated_datasets,
    domain=None,
    range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]],
)

slots.microbialCommunity__external_resources = Slot(
    uri=COMMUNITYMECH.external_resources,
    name="microbialCommunity__external_resources",
    curie=COMMUNITYMECH.curie("external_resources"),
    model_uri=COMMUNITYMECH.microbialCommunity__external_resources,
    domain=None,
    range=Optional[Union[Union[dict, ExternalResource], list[Union[dict, ExternalResource]]]],
)

slots.microbialCommunity__metals_present = Slot(
    uri=COMMUNITYMECH.metals_present,
    name="microbialCommunity__metals_present",
    curie=COMMUNITYMECH.curie("metals_present"),
    model_uri=COMMUNITYMECH.microbialCommunity__metals_present,
    domain=None,
    range=Optional[Union[Union[str, "MetalElementEnum"], list[Union[str, "MetalElementEnum"]]]],
)

slots.microbialCommunity__rare_earth_elements_present = Slot(
    uri=COMMUNITYMECH.rare_earth_elements_present,
    name="microbialCommunity__rare_earth_elements_present",
    curie=COMMUNITYMECH.curie("rare_earth_elements_present"),
    model_uri=COMMUNITYMECH.microbialCommunity__rare_earth_elements_present,
    domain=None,
    range=Optional[
        Union[Union[str, "RareEarthElementEnum"], list[Union[str, "RareEarthElementEnum"]]]
    ],
)

slots.microbialCommunity__metal_relevance = Slot(
    uri=COMMUNITYMECH.metal_relevance,
    name="microbialCommunity__metal_relevance",
    curie=COMMUNITYMECH.curie("metal_relevance"),
    model_uri=COMMUNITYMECH.microbialCommunity__metal_relevance,
    domain=None,
    range=Optional[Union[str, "MetalRelevanceEnum"]],
)

slots.microbialCommunity__metal_notes = Slot(
    uri=COMMUNITYMECH.metal_notes,
    name="microbialCommunity__metal_notes",
    curie=COMMUNITYMECH.curie("metal_notes"),
    model_uri=COMMUNITYMECH.microbialCommunity__metal_notes,
    domain=None,
    range=Optional[str],
)

slots.microbialCommunity__discussions = Slot(
    uri=COMMUNITYMECH.discussions,
    name="microbialCommunity__discussions",
    curie=COMMUNITYMECH.curie("discussions"),
    model_uri=COMMUNITYMECH.microbialCommunity__discussions,
    domain=None,
    range=Optional[Union[Union[dict, Discussion], list[Union[dict, Discussion]]]],
)

slots.microbialCommunity__curation_history = Slot(
    uri=COMMUNITYMECH.curation_history,
    name="microbialCommunity__curation_history",
    curie=COMMUNITYMECH.curie("curation_history"),
    model_uri=COMMUNITYMECH.microbialCommunity__curation_history,
    domain=None,
    range=Optional[Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]],
)

slots.curationEvent__timestamp = Slot(
    uri=COMMUNITYMECH.timestamp,
    name="curationEvent__timestamp",
    curie=COMMUNITYMECH.curie("timestamp"),
    model_uri=COMMUNITYMECH.curationEvent__timestamp,
    domain=None,
    range=Union[str, XSDDateTime],
)

slots.curationEvent__curator = Slot(
    uri=COMMUNITYMECH.curator,
    name="curationEvent__curator",
    curie=COMMUNITYMECH.curie("curator"),
    model_uri=COMMUNITYMECH.curationEvent__curator,
    domain=None,
    range=str,
)

slots.curationEvent__action = Slot(
    uri=COMMUNITYMECH.action,
    name="curationEvent__action",
    curie=COMMUNITYMECH.curie("action"),
    model_uri=COMMUNITYMECH.curationEvent__action,
    domain=None,
    range=str,
    pattern=re.compile(r"^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$"),
)

slots.curationEvent__changes = Slot(
    uri=COMMUNITYMECH.changes,
    name="curationEvent__changes",
    curie=COMMUNITYMECH.curie("changes"),
    model_uri=COMMUNITYMECH.curationEvent__changes,
    domain=None,
    range=Optional[str],
)

slots.curationEvent__llm_assisted = Slot(
    uri=COMMUNITYMECH.llm_assisted,
    name="curationEvent__llm_assisted",
    curie=COMMUNITYMECH.curie("llm_assisted"),
    model_uri=COMMUNITYMECH.curationEvent__llm_assisted,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.commonTaxon__id = Slot(
    uri=COMMUNITYMECH.id,
    name="commonTaxon__id",
    curie=COMMUNITYMECH.curie("id"),
    model_uri=COMMUNITYMECH.commonTaxon__id,
    domain=None,
    range=URIRef,
    pattern=re.compile(r"^CommunityMech:taxon:\d{6}$"),
)

slots.commonTaxon__taxon_term = Slot(
    uri=COMMUNITYMECH.taxon_term,
    name="commonTaxon__taxon_term",
    curie=COMMUNITYMECH.curie("taxon_term"),
    model_uri=COMMUNITYMECH.commonTaxon__taxon_term,
    domain=None,
    range=Union[dict, TaxonDescriptor],
)

slots.commonTaxon__genomes = Slot(
    uri=COMMUNITYMECH.genomes,
    name="commonTaxon__genomes",
    curie=COMMUNITYMECH.curie("genomes"),
    model_uri=COMMUNITYMECH.commonTaxon__genomes,
    domain=None,
    range=Optional[Union[Union[dict, GenomeRecord], list[Union[dict, GenomeRecord]]]],
)

slots.commonTaxon__genes = Slot(
    uri=COMMUNITYMECH.genes,
    name="commonTaxon__genes",
    curie=COMMUNITYMECH.curie("genes"),
    model_uri=COMMUNITYMECH.commonTaxon__genes,
    domain=None,
    range=Optional[Union[Union[dict, GeneAnnotation], list[Union[dict, GeneAnnotation]]]],
)

slots.commonTaxon__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="commonTaxon__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.commonTaxon__notes,
    domain=None,
    range=Optional[str],
)

slots.commonTaxon__curation_history = Slot(
    uri=COMMUNITYMECH.curation_history,
    name="commonTaxon__curation_history",
    curie=COMMUNITYMECH.curie("curation_history"),
    model_uri=COMMUNITYMECH.commonTaxon__curation_history,
    domain=None,
    range=Optional[Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]],
)

slots.genomeRecord__id = Slot(
    uri=COMMUNITYMECH.id,
    name="genomeRecord__id",
    curie=COMMUNITYMECH.curie("id"),
    model_uri=COMMUNITYMECH.genomeRecord__id,
    domain=None,
    range=str,
    pattern=re.compile(r"^GC[AF]_[0-9]{9}\.[0-9]+$"),
)

slots.genomeRecord__label = Slot(
    uri=COMMUNITYMECH.label,
    name="genomeRecord__label",
    curie=COMMUNITYMECH.curie("label"),
    model_uri=COMMUNITYMECH.genomeRecord__label,
    domain=None,
    range=Optional[str],
)

slots.genomeRecord__strain_designation = Slot(
    uri=COMMUNITYMECH.strain_designation,
    name="genomeRecord__strain_designation",
    curie=COMMUNITYMECH.curie("strain_designation"),
    model_uri=COMMUNITYMECH.genomeRecord__strain_designation,
    domain=None,
    range=Optional[Union[dict, StrainDesignation]],
)

slots.genomeRecord__notes = Slot(
    uri=COMMUNITYMECH.notes,
    name="genomeRecord__notes",
    curie=COMMUNITYMECH.curie("notes"),
    model_uri=COMMUNITYMECH.genomeRecord__notes,
    domain=None,
    range=Optional[str],
)

slots.geneAnnotation__gene_id = Slot(
    uri=COMMUNITYMECH.gene_id,
    name="geneAnnotation__gene_id",
    curie=COMMUNITYMECH.curie("gene_id"),
    model_uri=COMMUNITYMECH.geneAnnotation__gene_id,
    domain=None,
    range=str,
)

slots.geneAnnotation__gene_symbol = Slot(
    uri=COMMUNITYMECH.gene_symbol,
    name="geneAnnotation__gene_symbol",
    curie=COMMUNITYMECH.curie("gene_symbol"),
    model_uri=COMMUNITYMECH.geneAnnotation__gene_symbol,
    domain=None,
    range=Optional[str],
)

slots.geneAnnotation__locus_tag = Slot(
    uri=COMMUNITYMECH.locus_tag,
    name="geneAnnotation__locus_tag",
    curie=COMMUNITYMECH.curie("locus_tag"),
    model_uri=COMMUNITYMECH.geneAnnotation__locus_tag,
    domain=None,
    range=Optional[str],
)

slots.geneAnnotation__product = Slot(
    uri=COMMUNITYMECH.product,
    name="geneAnnotation__product",
    curie=COMMUNITYMECH.curie("product"),
    model_uri=COMMUNITYMECH.geneAnnotation__product,
    domain=None,
    range=Optional[str],
)

slots.geneAnnotation__genome = Slot(
    uri=COMMUNITYMECH.genome,
    name="geneAnnotation__genome",
    curie=COMMUNITYMECH.curie("genome"),
    model_uri=COMMUNITYMECH.geneAnnotation__genome,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^GC[AF]_[0-9]{9}\.[0-9]+$"),
)

slots.geneAnnotation__kegg_ortholog = Slot(
    uri=COMMUNITYMECH.kegg_ortholog,
    name="geneAnnotation__kegg_ortholog",
    curie=COMMUNITYMECH.curie("kegg_ortholog"),
    model_uri=COMMUNITYMECH.geneAnnotation__kegg_ortholog,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^K[0-9]{5}$"),
)

slots.geneAnnotation__go_terms = Slot(
    uri=COMMUNITYMECH.go_terms,
    name="geneAnnotation__go_terms",
    curie=COMMUNITYMECH.curie("go_terms"),
    model_uri=COMMUNITYMECH.geneAnnotation__go_terms,
    domain=None,
    range=Optional[Union[Union[dict, Term], list[Union[dict, Term]]]],
)

slots.geneAnnotation__supports_roles = Slot(
    uri=COMMUNITYMECH.supports_roles,
    name="geneAnnotation__supports_roles",
    curie=COMMUNITYMECH.curie("supports_roles"),
    model_uri=COMMUNITYMECH.geneAnnotation__supports_roles,
    domain=None,
    range=Optional[Union[Union[str, "FunctionalRoleEnum"], list[Union[str, "FunctionalRoleEnum"]]]],
)

slots.geneAnnotation__supports_interaction = Slot(
    uri=COMMUNITYMECH.supports_interaction,
    name="geneAnnotation__supports_interaction",
    curie=COMMUNITYMECH.curie("supports_interaction"),
    model_uri=COMMUNITYMECH.geneAnnotation__supports_interaction,
    domain=None,
    range=Optional[str],
)

slots.geneAnnotation__evidence = Slot(
    uri=COMMUNITYMECH.evidence,
    name="geneAnnotation__evidence",
    curie=COMMUNITYMECH.curie("evidence"),
    model_uri=COMMUNITYMECH.geneAnnotation__evidence,
    domain=None,
    range=Optional[Union[Union[dict, EvidenceItem], list[Union[dict, EvidenceItem]]]],
)

slots.supportingReference__reference = Slot(
    uri=MECH_SHARED.reference,
    name="supportingReference__reference",
    curie=MECH_SHARED.curie("reference"),
    model_uri=COMMUNITYMECH.supportingReference__reference,
    domain=None,
    range=str,
)

slots.supportingReference__reference_title = Slot(
    uri=MECH_SHARED.reference_title,
    name="supportingReference__reference_title",
    curie=MECH_SHARED.curie("reference_title"),
    model_uri=COMMUNITYMECH.supportingReference__reference_title,
    domain=None,
    range=Optional[str],
)

slots.supportingReference__supports = Slot(
    uri=MECH_SHARED.supports,
    name="supportingReference__supports",
    curie=MECH_SHARED.curie("supports"),
    model_uri=COMMUNITYMECH.supportingReference__supports,
    domain=None,
    range=Optional[Union[str, "SupportLevelEnum"]],
)

slots.supportingReference__evidence_source = Slot(
    uri=MECH_SHARED.evidence_source,
    name="supportingReference__evidence_source",
    curie=MECH_SHARED.curie("evidence_source"),
    model_uri=COMMUNITYMECH.supportingReference__evidence_source,
    domain=None,
    range=Optional[str],
)

slots.supportingReference__snippet = Slot(
    uri=MECH_SHARED.snippet,
    name="supportingReference__snippet",
    curie=MECH_SHARED.curie("snippet"),
    model_uri=COMMUNITYMECH.supportingReference__snippet,
    domain=None,
    range=Optional[str],
)

slots.supportingReference__explanation = Slot(
    uri=MECH_SHARED.explanation,
    name="supportingReference__explanation",
    curie=MECH_SHARED.curie("explanation"),
    model_uri=COMMUNITYMECH.supportingReference__explanation,
    domain=None,
    range=Optional[str],
)

slots.supportingReference__notes = Slot(
    uri=MECH_SHARED.notes,
    name="supportingReference__notes",
    curie=MECH_SHARED.curie("notes"),
    model_uri=COMMUNITYMECH.supportingReference__notes,
    domain=None,
    range=Optional[str],
)

slots.discussion__discussion_id = Slot(
    uri=MECH_SHARED.discussion_id,
    name="discussion__discussion_id",
    curie=MECH_SHARED.curie("discussion_id"),
    model_uri=COMMUNITYMECH.discussion__discussion_id,
    domain=None,
    range=str,
)

slots.discussion__prompt = Slot(
    uri=MECH_SHARED.prompt,
    name="discussion__prompt",
    curie=MECH_SHARED.curie("prompt"),
    model_uri=COMMUNITYMECH.discussion__prompt,
    domain=None,
    range=str,
)

slots.discussion__kind = Slot(
    uri=MECH_SHARED.kind,
    name="discussion__kind",
    curie=MECH_SHARED.curie("kind"),
    model_uri=COMMUNITYMECH.discussion__kind,
    domain=None,
    range=Optional[Union[str, "DiscussionKindEnum"]],
)

slots.discussion__status = Slot(
    uri=MECH_SHARED.status,
    name="discussion__status",
    curie=MECH_SHARED.curie("status"),
    model_uri=COMMUNITYMECH.discussion__status,
    domain=None,
    range=Optional[Union[str, "DiscussionStatusEnum"]],
)

slots.discussion__attaches_to = Slot(
    uri=MECH_SHARED.attaches_to,
    name="discussion__attaches_to",
    curie=MECH_SHARED.curie("attaches_to"),
    model_uri=COMMUNITYMECH.discussion__attaches_to,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.discussion__rationale = Slot(
    uri=MECH_SHARED.rationale,
    name="discussion__rationale",
    curie=MECH_SHARED.curie("rationale"),
    model_uri=COMMUNITYMECH.discussion__rationale,
    domain=None,
    range=Optional[str],
)

slots.discussion__proposed_experiments = Slot(
    uri=MECH_SHARED.proposed_experiments,
    name="discussion__proposed_experiments",
    curie=MECH_SHARED.curie("proposed_experiments"),
    model_uri=COMMUNITYMECH.discussion__proposed_experiments,
    domain=None,
    range=Optional[Union[Union[dict, ProposedExperiment], list[Union[dict, ProposedExperiment]]]],
)

slots.discussion__evidence = Slot(
    uri=MECH_SHARED.evidence,
    name="discussion__evidence",
    curie=MECH_SHARED.curie("evidence"),
    model_uri=COMMUNITYMECH.discussion__evidence,
    domain=None,
    range=Optional[Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]],
)

slots.discussion__posed_by = Slot(
    uri=MECH_SHARED.posed_by,
    name="discussion__posed_by",
    curie=MECH_SHARED.curie("posed_by"),
    model_uri=COMMUNITYMECH.discussion__posed_by,
    domain=None,
    range=Optional[str],
)

slots.discussion__posed_date = Slot(
    uri=MECH_SHARED.posed_date,
    name="discussion__posed_date",
    curie=MECH_SHARED.curie("posed_date"),
    model_uri=COMMUNITYMECH.discussion__posed_date,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.discussion__resolved_date = Slot(
    uri=MECH_SHARED.resolved_date,
    name="discussion__resolved_date",
    curie=MECH_SHARED.curie("resolved_date"),
    model_uri=COMMUNITYMECH.discussion__resolved_date,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.discussion__resolution_note = Slot(
    uri=MECH_SHARED.resolution_note,
    name="discussion__resolution_note",
    curie=MECH_SHARED.curie("resolution_note"),
    model_uri=COMMUNITYMECH.discussion__resolution_note,
    domain=None,
    range=Optional[str],
)

slots.discussion__notes = Slot(
    uri=MECH_SHARED.notes,
    name="discussion__notes",
    curie=MECH_SHARED.curie("notes"),
    model_uri=COMMUNITYMECH.discussion__notes,
    domain=None,
    range=Optional[str],
)

slots.proposedExperiment__experiment_id = Slot(
    uri=MECH_SHARED.experiment_id,
    name="proposedExperiment__experiment_id",
    curie=MECH_SHARED.curie("experiment_id"),
    model_uri=COMMUNITYMECH.proposedExperiment__experiment_id,
    domain=None,
    range=Optional[str],
)

slots.proposedExperiment__name = Slot(
    uri=MECH_SHARED.name,
    name="proposedExperiment__name",
    curie=MECH_SHARED.curie("name"),
    model_uri=COMMUNITYMECH.proposedExperiment__name,
    domain=None,
    range=Optional[str],
)

slots.proposedExperiment__description = Slot(
    uri=MECH_SHARED.description,
    name="proposedExperiment__description",
    curie=MECH_SHARED.curie("description"),
    model_uri=COMMUNITYMECH.proposedExperiment__description,
    domain=None,
    range=Optional[str],
)

slots.proposedExperiment__approach = Slot(
    uri=MECH_SHARED.approach,
    name="proposedExperiment__approach",
    curie=MECH_SHARED.curie("approach"),
    model_uri=COMMUNITYMECH.proposedExperiment__approach,
    domain=None,
    range=Optional[str],
)

slots.proposedExperiment__model_systems = Slot(
    uri=MECH_SHARED.model_systems,
    name="proposedExperiment__model_systems",
    curie=MECH_SHARED.curie("model_systems"),
    model_uri=COMMUNITYMECH.proposedExperiment__model_systems,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.proposedExperiment__perturbations = Slot(
    uri=MECH_SHARED.perturbations,
    name="proposedExperiment__perturbations",
    curie=MECH_SHARED.curie("perturbations"),
    model_uri=COMMUNITYMECH.proposedExperiment__perturbations,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.proposedExperiment__readouts = Slot(
    uri=MECH_SHARED.readouts,
    name="proposedExperiment__readouts",
    curie=MECH_SHARED.curie("readouts"),
    model_uri=COMMUNITYMECH.proposedExperiment__readouts,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.proposedExperiment__decision_criterion = Slot(
    uri=MECH_SHARED.decision_criterion,
    name="proposedExperiment__decision_criterion",
    curie=MECH_SHARED.curie("decision_criterion"),
    model_uri=COMMUNITYMECH.proposedExperiment__decision_criterion,
    domain=None,
    range=Optional[str],
)

slots.proposedExperiment__would_support = Slot(
    uri=MECH_SHARED.would_support,
    name="proposedExperiment__would_support",
    curie=MECH_SHARED.curie("would_support"),
    model_uri=COMMUNITYMECH.proposedExperiment__would_support,
    domain=None,
    range=Optional[str],
)

slots.proposedExperiment__would_refute = Slot(
    uri=MECH_SHARED.would_refute,
    name="proposedExperiment__would_refute",
    curie=MECH_SHARED.curie("would_refute"),
    model_uri=COMMUNITYMECH.proposedExperiment__would_refute,
    domain=None,
    range=Optional[str],
)

slots.dataset__accession = Slot(
    uri=MECH_SHARED.accession,
    name="dataset__accession",
    curie=MECH_SHARED.curie("accession"),
    model_uri=COMMUNITYMECH.dataset__accession,
    domain=None,
    range=Optional[str],
)

slots.dataset__title = Slot(
    uri=MECH_SHARED.title,
    name="dataset__title",
    curie=MECH_SHARED.curie("title"),
    model_uri=COMMUNITYMECH.dataset__title,
    domain=None,
    range=Optional[str],
)

slots.dataset__description = Slot(
    uri=MECH_SHARED.description,
    name="dataset__description",
    curie=MECH_SHARED.curie("description"),
    model_uri=COMMUNITYMECH.dataset__description,
    domain=None,
    range=Optional[str],
)

slots.dataset__organism = Slot(
    uri=MECH_SHARED.organism,
    name="dataset__organism",
    curie=MECH_SHARED.curie("organism"),
    model_uri=COMMUNITYMECH.dataset__organism,
    domain=None,
    range=Optional[str],
)

slots.dataset__dataset_type = Slot(
    uri=MECH_SHARED.dataset_type,
    name="dataset__dataset_type",
    curie=MECH_SHARED.curie("dataset_type"),
    model_uri=COMMUNITYMECH.dataset__dataset_type,
    domain=None,
    range=Optional[Union[str, "DatasetTypeEnum"]],
)

slots.dataset__repository = Slot(
    uri=MECH_SHARED.repository,
    name="dataset__repository",
    curie=MECH_SHARED.curie("repository"),
    model_uri=COMMUNITYMECH.dataset__repository,
    domain=None,
    range=Optional[Union[str, "DatasetRepositoryEnum"]],
)

slots.dataset__sample_types = Slot(
    uri=MECH_SHARED.sample_types,
    name="dataset__sample_types",
    curie=MECH_SHARED.curie("sample_types"),
    model_uri=COMMUNITYMECH.dataset__sample_types,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.dataset__sample_count = Slot(
    uri=MECH_SHARED.sample_count,
    name="dataset__sample_count",
    curie=MECH_SHARED.curie("sample_count"),
    model_uri=COMMUNITYMECH.dataset__sample_count,
    domain=None,
    range=Optional[int],
)

slots.dataset__conditions = Slot(
    uri=MECH_SHARED.conditions,
    name="dataset__conditions",
    curie=MECH_SHARED.curie("conditions"),
    model_uri=COMMUNITYMECH.dataset__conditions,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.dataset__platform = Slot(
    uri=MECH_SHARED.platform,
    name="dataset__platform",
    curie=MECH_SHARED.curie("platform"),
    model_uri=COMMUNITYMECH.dataset__platform,
    domain=None,
    range=Optional[str],
)

slots.dataset__url = Slot(
    uri=MECH_SHARED.url,
    name="dataset__url",
    curie=MECH_SHARED.curie("url"),
    model_uri=COMMUNITYMECH.dataset__url,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.dataset__publication = Slot(
    uri=MECH_SHARED.publication,
    name="dataset__publication",
    curie=MECH_SHARED.curie("publication"),
    model_uri=COMMUNITYMECH.dataset__publication,
    domain=None,
    range=Optional[str],
)

slots.dataset__findings = Slot(
    uri=MECH_SHARED.findings,
    name="dataset__findings",
    curie=MECH_SHARED.curie("findings"),
    model_uri=COMMUNITYMECH.dataset__findings,
    domain=None,
    range=Optional[str],
)

slots.dataset__evidence = Slot(
    uri=MECH_SHARED.evidence,
    name="dataset__evidence",
    curie=MECH_SHARED.curie("evidence"),
    model_uri=COMMUNITYMECH.dataset__evidence,
    domain=None,
    range=Optional[Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]],
)

slots.dataset__notes = Slot(
    uri=MECH_SHARED.notes,
    name="dataset__notes",
    curie=MECH_SHARED.curie("notes"),
    model_uri=COMMUNITYMECH.dataset__notes,
    domain=None,
    range=Optional[str],
)
