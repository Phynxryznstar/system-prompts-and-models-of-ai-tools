"""Seed script for inserting example graph data for manual testing.

Populates a small, self-consistent set of `TaxSection`, `Trust`,
`EstatePlanningConcept`, `RiskExposure`, and `ClientScenario` nodes (and
the relationships between them) so the graph schema can be exercised
end to end before real ingestion scripts are built out.

Run directly with `python -m graph.seed_example_data`, or via the CLI:
`python main.py seed-example-data`.
"""

from __future__ import annotations

from graph.connection import verify_connectivity
from graph.queries import merge_node, merge_relationship
from graph.schema import NodeLabel, RelationshipType

TAX_SECTION_199A = "irc_199a"
TAX_SECTION_469 = "irc_469"
TAX_SECTION_163J = "irc_163j"
TRUST_IDGT = "trust_idgt"
CONCEPT_ESTATE_TAX_REDUCTION = "concept_estate_tax_reduction"
RISK_ESTATE_TAX = "risk_estate_tax"
CLIENT_SCENARIO_EXAMPLE = "example_scenario"


def _seed_nodes() -> None:
    merge_node(
        NodeLabel.TAX_SECTION,
        TAX_SECTION_199A,
        {"name": "IRC §199A", "section_number": "199A"},
    )
    merge_node(
        NodeLabel.TAX_SECTION,
        TAX_SECTION_469,
        {"name": "IRC §469", "section_number": "469"},
    )
    merge_node(
        NodeLabel.TAX_SECTION,
        TAX_SECTION_163J,
        {"name": "IRC §163(j)", "section_number": "163(j)"},
    )
    merge_node(
        NodeLabel.TRUST,
        TRUST_IDGT,
        {"name": "IDGT", "trust_type": "Intentionally Defective Grantor Trust"},
    )
    merge_node(
        NodeLabel.ESTATE_PLANNING_CONCEPT,
        CONCEPT_ESTATE_TAX_REDUCTION,
        {"name": "EstateTaxReduction"},
    )
    merge_node(
        NodeLabel.RISK_EXPOSURE,
        RISK_ESTATE_TAX,
        {"name": "EstateTaxRisk"},
    )
    merge_node(
        NodeLabel.CLIENT_SCENARIO,
        CLIENT_SCENARIO_EXAMPLE,
        {
            "filing_status": "MFJ",
            "income_range": "7000000-10000000",
        },
    )


def _seed_relationships() -> None:
    merge_relationship(
        NodeLabel.TAX_SECTION,
        TAX_SECTION_199A,
        RelationshipType.REFERENCES,
        NodeLabel.TAX_SECTION,
        TAX_SECTION_469,
    )
    merge_relationship(
        NodeLabel.TAX_SECTION,
        TAX_SECTION_199A,
        RelationshipType.REFERENCES,
        NodeLabel.TAX_SECTION,
        TAX_SECTION_163J,
    )
    merge_relationship(
        NodeLabel.TRUST,
        TRUST_IDGT,
        RelationshipType.PROVIDES_PROTECTION,
        NodeLabel.RISK_EXPOSURE,
        RISK_ESTATE_TAX,
    )
    merge_relationship(
        NodeLabel.TRUST,
        TRUST_IDGT,
        RelationshipType.OPTIMIZES_ESTATE_TAX,
        NodeLabel.ESTATE_PLANNING_CONCEPT,
        CONCEPT_ESTATE_TAX_REDUCTION,
    )
    merge_relationship(
        NodeLabel.CLIENT_SCENARIO,
        CLIENT_SCENARIO_EXAMPLE,
        RelationshipType.SUBJECT_TO_CONSTRAINT,
        NodeLabel.RISK_EXPOSURE,
        RISK_ESTATE_TAX,
    )


def seed_example_data() -> None:
    """Connect to Neo4j and insert the example nodes and relationships.

    Uses `MERGE` throughout (via `graph.queries`), so it is safe to run
    more than once without creating duplicate data.
    """
    verify_connectivity()

    _seed_nodes()
    _seed_relationships()

    print("Seeded example data into Neo4j:")
    print("  Nodes:")
    for node_id in (
        TAX_SECTION_199A,
        TAX_SECTION_469,
        TAX_SECTION_163J,
        TRUST_IDGT,
        CONCEPT_ESTATE_TAX_REDUCTION,
        RISK_ESTATE_TAX,
        CLIENT_SCENARIO_EXAMPLE,
    ):
        print(f"    - {node_id}")
    print("  Relationships:")
    print(f"    ({TAX_SECTION_199A})-[:REFERENCES]->({TAX_SECTION_469})")
    print(f"    ({TAX_SECTION_199A})-[:REFERENCES]->({TAX_SECTION_163J})")
    print(f"    ({TRUST_IDGT})-[:PROVIDES_PROTECTION]->({RISK_ESTATE_TAX})")
    print(f"    ({TRUST_IDGT})-[:OPTIMIZES_ESTATE_TAX]->({CONCEPT_ESTATE_TAX_REDUCTION})")
    print(f"    ({CLIENT_SCENARIO_EXAMPLE})-[:SUBJECT_TO_CONSTRAINT]->({RISK_ESTATE_TAX})")


if __name__ == "__main__":
    seed_example_data()
