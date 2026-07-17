"""Scoring engine: orchestrates reasoning + formulas into (strategy, score) pairs.

`score_strategy` and `score_strategies` apply `scoring.formulas` to
`Strategy` objects that already exist. `score_scenario` is the
convenience entry point that runs the reasoning engine and scoring
together for a given scenario id. This module contains no math of its
own — that lives entirely in `scoring.formulas`; it only wires the
reasoning engine's output to the formula registry.
"""

from __future__ import annotations

from graph import queries as graph_queries
from reasoning.engine import find_all_strategies
from reasoning.rules import GraphClient, Strategy
from scoring.formulas import get_formula_for_strategy


def score_strategy(strategy: Strategy, graph_client: GraphClient = graph_queries) -> float:
    """Score a single strategy using its matching formula.

    `graph_client` isn't used by any formula today (they work entirely
    off `Strategy.estimated_inputs`), but is accepted here for symmetry
    with the other scoring entry points and in case a future formula
    needs to look up additional graph data.
    """
    formula = get_formula_for_strategy(strategy)
    if formula is None:
        raise ValueError(f"No scoring formula registered for strategy '{strategy.name}'.")
    return formula(strategy)


def score_strategies(
    strategies: list[Strategy], graph_client: GraphClient = graph_queries
) -> list[tuple[Strategy, float]]:
    """Score a list of strategies, returning (strategy, score) pairs."""
    return [(strategy, score_strategy(strategy, graph_client)) for strategy in strategies]


def score_scenario(
    scenario_id: str, graph_client: GraphClient = graph_queries
) -> list[tuple[Strategy, float]]:
    """Run the reasoning engine for a scenario, then score every strategy it finds."""
    strategies = find_all_strategies(scenario_id, graph_client)
    return score_strategies(strategies, graph_client)
