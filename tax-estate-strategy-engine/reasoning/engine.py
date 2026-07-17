"""Core reasoning engine for evaluating tax and estate strategies.

Ties a `ClientScenario` already stored in Neo4j to the rule functions in
`reasoning.rules`: each `find_*_strategies` function loads the scenario
node (so a missing scenario fails fast with a clear error), runs the
relevant rules against it, and returns whichever `Strategy` objects those
rules decided apply. This module has no scoring logic of its own — it
only collects what the rules found; the `scoring` package is responsible
for turning that into an estimated benefit.
"""

from __future__ import annotations

from graph import queries as graph_queries
from graph.schema import NodeLabel
from reasoning.rules import ESTATE_RULES, STATE_RULES, TAX_RULES, GraphClient, Strategy


def _load_scenario(client_scenario_id: str, graph_client: GraphClient) -> dict:
    scenario = graph_client.get_node(NodeLabel.CLIENT_SCENARIO, client_scenario_id)
    if scenario is None:
        raise ValueError(f"ClientScenario '{client_scenario_id}' not found in the graph.")
    return scenario


def _run_rules(client_scenario_id: str, graph_client: GraphClient, rules: list) -> list[Strategy]:
    return [
        strategy
        for rule in rules
        if (strategy := rule(client_scenario_id, graph_client)) is not None
    ]


def find_tax_strategies(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> list[Strategy]:
    """Return the tax strategies that apply to the given client scenario."""
    _load_scenario(client_scenario_id, graph_client)
    return _run_rules(client_scenario_id, graph_client, TAX_RULES)


def find_estate_strategies(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> list[Strategy]:
    """Return the estate strategies that apply to the given client scenario."""
    _load_scenario(client_scenario_id, graph_client)
    return _run_rules(client_scenario_id, graph_client, ESTATE_RULES)


def find_state_strategies(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> list[Strategy]:
    """Return the state-level strategies that apply to the given client scenario."""
    _load_scenario(client_scenario_id, graph_client)
    return _run_rules(client_scenario_id, graph_client, STATE_RULES)


def find_all_strategies(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> list[Strategy]:
    """Return every tax, estate, and state strategy that applies."""
    return (
        find_tax_strategies(client_scenario_id, graph_client)
        + find_estate_strategies(client_scenario_id, graph_client)
        + find_state_strategies(client_scenario_id, graph_client)
    )
