"""Reusable Cypher queries and graph utility functions.

Generic helpers for creating/merging nodes and relationships and for
running arbitrary Cypher, built on top of `graph.connection.get_session`.
Ingestion, reasoning, and scoring code should go through these helpers
rather than issuing ad-hoc driver calls, so query patterns stay
consistent across the codebase.
"""

from __future__ import annotations

from typing import Any

from neo4j import Record

from graph.connection import get_session
from graph.schema import NodeLabel, RelationshipType


def run_query(cypher: str, parameters: dict[str, Any] | None = None) -> list[Record]:
    """Run a read Cypher statement and return all result records."""
    with get_session() as session:
        result = session.run(cypher, parameters or {})
        return list(result)


def run_write(cypher: str, parameters: dict[str, Any] | None = None) -> None:
    """Run a write Cypher statement inside a managed write transaction."""

    def _work(tx, cypher: str = cypher, parameters: dict[str, Any] | None = parameters) -> None:
        tx.run(cypher, parameters or {})

    with get_session() as session:
        session.execute_write(_work)


def merge_node(
    label: NodeLabel,
    key_value: Any,
    properties: dict[str, Any] | None = None,
    key: str = "id",
) -> dict[str, Any]:
    """Create or update a node identified by `key`/`key_value`.

    Any `properties` are merged onto the node, so re-ingesting the same
    `key_value` updates existing fields rather than duplicating the node.
    Returns the resulting node's properties.
    """
    props = dict(properties or {})
    props[key] = key_value

    cypher = (
        f"MERGE (n:{label.value} {{{key}: $key_value}}) "
        "SET n += $properties "
        "RETURN n"
    )
    with get_session() as session:
        result = session.run(cypher, key_value=key_value, properties=props)
        record = result.single()
        return dict(record["n"]) if record else {}


def merge_relationship(
    start_label: NodeLabel,
    start_key_value: Any,
    relationship: RelationshipType,
    end_label: NodeLabel,
    end_key_value: Any,
    start_key: str = "id",
    end_key: str = "id",
    properties: dict[str, Any] | None = None,
) -> None:
    """Create or update a relationship between two existing nodes."""
    cypher = (
        f"MATCH (a:{start_label.value} {{{start_key}: $start_key_value}}) "
        f"MATCH (b:{end_label.value} {{{end_key}: $end_key_value}}) "
        f"MERGE (a)-[r:{relationship.value}]->(b) "
        "SET r += $properties"
    )
    run_write(
        cypher,
        {
            "start_key_value": start_key_value,
            "end_key_value": end_key_value,
            "properties": properties or {},
        },
    )


def get_node(label: NodeLabel, key_value: Any, key: str = "id") -> dict[str, Any] | None:
    """Fetch a single node by its key property, or None if it doesn't exist."""
    cypher = f"MATCH (n:{label.value} {{{key}: $key_value}}) RETURN n LIMIT 1"
    records = run_query(cypher, {"key_value": key_value})
    return dict(records[0]["n"]) if records else None


def get_related_nodes(
    label: NodeLabel,
    key_value: Any,
    relationship: RelationshipType,
    related_label: NodeLabel,
    key: str = "id",
    direction: str = "out",
) -> list[dict[str, Any]]:
    """Return nodes connected to a given node via a specific relationship.

    `direction` is "out" for `(n)-[r]->(related)` or "in" for
    `(n)<-[r]-(related)`.
    """
    if direction not in ("out", "in"):
        raise ValueError("direction must be 'out' or 'in'")

    node_pattern = f"(n:{label.value} {{{key}: $key_value}})"
    related_pattern = f"(related:{related_label.value})"
    rel_pattern = f"[:{relationship.value}]"
    pattern = (
        f"{node_pattern}-{rel_pattern}->{related_pattern}"
        if direction == "out"
        else f"{node_pattern}<-{rel_pattern}-{related_pattern}"
    )

    cypher = f"MATCH {pattern} RETURN related"
    records = run_query(cypher, {"key_value": key_value})
    return [dict(record["related"]) for record in records]


def delete_node(label: NodeLabel, key_value: Any, key: str = "id") -> None:
    """Delete a node and any relationships attached to it."""
    cypher = f"MATCH (n:{label.value} {{{key}: $key_value}}) DETACH DELETE n"
    run_write(cypher, {"key_value": key_value})
