"""Graph schema definitions.

Defines node labels, relationship types, and the constraints/indexes used
to model tax entities, estate structures, and jurisdictional rules in
Neo4j. Call `initialize_schema()` once (e.g. from a setup script) to
create all constraints and indexes; every statement uses
`IF NOT EXISTS`, so it is safe to run repeatedly.
"""

from __future__ import annotations

from enum import Enum

from graph.connection import get_session


class NodeLabel(str, Enum):
    """Node labels used throughout the graph."""

    TAX_SECTION = "TaxSection"
    REG_SECTION = "RegSection"
    PUBLICATION_CHUNK = "PublicationChunk"
    CONCEPT = "Concept"
    ENTITY = "Entity"
    ACTIVITY = "Activity"
    ELECTION = "Election"
    CREDIT_DEDUCTION = "CreditDeduction"
    CONSTRAINT = "Constraint"
    TRUST = "Trust"
    ESTATE_PLANNING_CONCEPT = "EstatePlanningConcept"
    RISK_EXPOSURE = "RiskExposure"
    OWNERSHIP_STRUCTURE = "OwnershipStructure"
    BENEFICIARY = "Beneficiary"
    CLIENT_SCENARIO = "ClientScenario"
    STATE_TAX_RULE = "StateTaxRule"


class RelationshipType(str, Enum):
    """Relationship types used throughout the graph."""

    REFERENCES = "REFERENCES"
    EXCEPTS = "EXCEPTS"
    MODIFIES = "MODIFIES"
    LIMITED_BY = "LIMITED_BY"
    DEFINES = "DEFINES"
    APPLIES_TO_ENTITY = "APPLIES_TO_ENTITY"
    RELATES_TO_CONCEPT = "RELATES_TO_CONCEPT"
    RELATES_TO_ACTIVITY = "RELATES_TO_ACTIVITY"
    TRIGGERS_CREDIT = "TRIGGERS_CREDIT"
    AVAILABLE_ELECTION = "AVAILABLE_ELECTION"
    SUBJECT_TO_CONSTRAINT = "SUBJECT_TO_CONSTRAINT"
    HOLDS_ASSET = "HOLDS_ASSET"
    OWNED_BY = "OWNED_BY"
    PROVIDES_PROTECTION = "PROVIDES_PROTECTION"
    OPTIMIZES_ESTATE_TAX = "OPTIMIZES_ESTATE_TAX"
    INTERACTS_WITH_TAX_SECTION = "INTERACTS_WITH_TAX_SECTION"
    ENHANCES_STRATEGY = "ENHANCES_STRATEGY"
    USES_OWNERSHIP_STRUCTURE = "USES_OWNERSHIP_STRUCTURE"
    APPLIES_IN_STATE = "APPLIES_IN_STATE"


# Every node carries a unique `id` property (enforced below). This maps
# each label to the additional properties that should be indexed to keep
# ingestion/lookup queries fast.
NODE_INDEXED_PROPERTIES: dict[NodeLabel, tuple[str, ...]] = {
    NodeLabel.TAX_SECTION: ("section_number",),
    NodeLabel.REG_SECTION: ("reg_number",),
    NodeLabel.PUBLICATION_CHUNK: ("source",),
    NodeLabel.CONCEPT: ("name",),
    NodeLabel.ENTITY: ("name", "entity_type"),
    NodeLabel.ACTIVITY: ("name",),
    NodeLabel.ELECTION: ("name",),
    NodeLabel.CREDIT_DEDUCTION: ("name",),
    NodeLabel.CONSTRAINT: ("name",),
    NodeLabel.TRUST: ("name", "trust_type"),
    NodeLabel.ESTATE_PLANNING_CONCEPT: ("name",),
    NodeLabel.RISK_EXPOSURE: ("name",),
    NodeLabel.OWNERSHIP_STRUCTURE: ("name", "structure_type"),
    NodeLabel.BENEFICIARY: ("name",),
    NodeLabel.CLIENT_SCENARIO: ("client_id",),
    NodeLabel.STATE_TAX_RULE: ("state",),
}


def _constraint_name(label: NodeLabel) -> str:
    return f"{label.value.lower()}_id_unique"


def _index_name(label: NodeLabel, property_name: str) -> str:
    return f"{label.value.lower()}_{property_name}_idx"


def build_constraint_statements() -> list[str]:
    """Return `CREATE CONSTRAINT` statements enforcing a unique `id` per label."""
    return [
        f"CREATE CONSTRAINT {_constraint_name(label)} IF NOT EXISTS "
        f"FOR (n:{label.value}) REQUIRE n.id IS UNIQUE"
        for label in NodeLabel
    ]


def build_index_statements() -> list[str]:
    """Return `CREATE INDEX` statements for each label's indexed properties."""
    statements = []
    for label, properties in NODE_INDEXED_PROPERTIES.items():
        for property_name in properties:
            statements.append(
                f"CREATE INDEX {_index_name(label, property_name)} IF NOT EXISTS "
                f"FOR (n:{label.value}) ON (n.{property_name})"
            )
    return statements


def create_constraints() -> None:
    """Create the unique `id` constraint for every node label."""
    with get_session() as session:
        for statement in build_constraint_statements():
            session.run(statement)


def create_indexes() -> None:
    """Create secondary indexes for every node label's indexed properties."""
    with get_session() as session:
        for statement in build_index_statements():
            session.run(statement)


def initialize_schema() -> None:
    """Create all node constraints and indexes in Neo4j.

    Safe to run repeatedly; every underlying statement uses
    `IF NOT EXISTS`. Intended to be run once during setup, before any
    ingestion scripts populate the graph.
    """
    create_constraints()
    create_indexes()
