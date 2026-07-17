"""Ingestion of a validated `ClientScenario` into Neo4j.

Takes a `ClientScenario` (see `reasoning.scenario_schema`) and writes it
into the graph using the generic helpers in `graph.queries`: a
`ClientScenario` node, one node per entity/activity/asset, a node per
constraint tag, and a `StateTaxRule` node for the scenario's state — each
connected back to the scenario. Everything goes through `MERGE`, so
re-running ingestion for the same scenario file updates it in place
instead of creating duplicates.
"""

from __future__ import annotations

from typing import Any

from graph.connection import verify_connectivity
from graph.queries import merge_node, merge_relationship
from graph.schema import NodeLabel, RelationshipType
from reasoning.scenario_schema import ClientScenario


def _create_node(label: NodeLabel, key_value: str, properties: dict[str, Any]) -> dict[str, Any]:
    node = merge_node(label, key_value, properties)
    print(f"  Node created: ({label.value} {{id: {key_value!r}}})")
    return node


def _create_relationship(
    start_label: NodeLabel,
    start_key_value: str,
    relationship: RelationshipType,
    end_label: NodeLabel,
    end_key_value: str,
) -> None:
    merge_relationship(start_label, start_key_value, relationship, end_label, end_key_value)
    print(
        f"  Relationship created: ({start_label.value} {start_key_value!r})"
        f"-[:{relationship.value}]->({end_label.value} {end_key_value!r})"
    )


def _state_tax_rule_id(state: str) -> str:
    return f"state_{state.lower()}"


def ingest_client_scenario(client_scenario: ClientScenario) -> dict[str, int]:
    """Insert a `ClientScenario` and all of its related nodes into Neo4j.

    Returns a summary dict with a count of each kind of node created,
    for the caller to report back to the user.
    """
    verify_connectivity()

    print(f"Ingesting ClientScenario '{client_scenario.id}'...")

    scenario_properties = client_scenario.model_dump(
        exclude={"id", "entities", "activities", "assets", "constraints"}
    )
    _create_node(NodeLabel.CLIENT_SCENARIO, client_scenario.id, scenario_properties)

    for entity in client_scenario.entities:
        properties = entity.model_dump(exclude={"id"}, exclude_none=True)
        _create_node(NodeLabel.ENTITY, entity.id, properties)
        _create_relationship(
            NodeLabel.CLIENT_SCENARIO,
            client_scenario.id,
            RelationshipType.HAS_ENTITY,
            NodeLabel.ENTITY,
            entity.id,
        )

    for activity in client_scenario.activities:
        properties = activity.model_dump(exclude={"id"}, exclude_none=True)
        _create_node(NodeLabel.ACTIVITY, activity.id, properties)
        _create_relationship(
            NodeLabel.CLIENT_SCENARIO,
            client_scenario.id,
            RelationshipType.HAS_ACTIVITY,
            NodeLabel.ACTIVITY,
            activity.id,
        )

    for asset in client_scenario.assets:
        properties = asset.model_dump(exclude={"id"}, exclude_none=True)
        _create_node(NodeLabel.ASSET, asset.id, properties)
        _create_relationship(
            NodeLabel.CLIENT_SCENARIO,
            client_scenario.id,
            RelationshipType.HAS_ASSET,
            NodeLabel.ASSET,
            asset.id,
        )

    for constraint in client_scenario.constraints:
        _create_node(NodeLabel.CONSTRAINT, constraint, {"name": constraint})
        _create_relationship(
            NodeLabel.CLIENT_SCENARIO,
            client_scenario.id,
            RelationshipType.SUBJECT_TO_CONSTRAINT,
            NodeLabel.CONSTRAINT,
            constraint,
        )

    state_tax_rule_id = _state_tax_rule_id(client_scenario.state)
    _create_node(NodeLabel.STATE_TAX_RULE, state_tax_rule_id, {"state": client_scenario.state})
    _create_relationship(
        NodeLabel.CLIENT_SCENARIO,
        client_scenario.id,
        RelationshipType.APPLIES_IN_STATE,
        NodeLabel.STATE_TAX_RULE,
        state_tax_rule_id,
    )

    print(f"Scenario ingestion complete: {client_scenario.id}")

    return {
        "entities": len(client_scenario.entities),
        "activities": len(client_scenario.activities),
        "assets": len(client_scenario.assets),
        "constraints": len(client_scenario.constraints),
        "state_tax_rules": 1,
    }
