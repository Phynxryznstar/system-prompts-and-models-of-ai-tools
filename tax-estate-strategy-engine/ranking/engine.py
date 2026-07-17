"""Ranking engine: turns scored strategies into a weighted, sorted ranking.

`rank_strategy` applies a domain weight (see `ranking.weights`) to a raw
score. `rank_strategies` weights and sorts strategies that are already
`(strategy, score)` pairs — the exact shape `scoring.engine.score_scenario`
and `scoring.engine.score_strategies` return, so ranking drops straight
into the scoring pipeline. `rank_scenario` is the full pipeline: load
the scenario, run reasoning + scoring, weight every result, and return
it sorted. No math beyond the weight multiplication happens here — raw
dollar scores come entirely from `scoring.formulas`.
"""

from __future__ import annotations

from graph import queries as graph_queries
from ranking.weights import get_weight
from reasoning.rules import GraphClient, Strategy
from scoring.engine import score_scenario


def rank_strategy(strategy: Strategy, score: float) -> float:
    """Return `score` weighted by the strategy's domain (tax/estate/state/combined)."""
    return score * get_weight(strategy.type)


def rank_strategies(
    strategies_with_scores: list[tuple[Strategy, float]],
) -> list[tuple[Strategy, float, float]]:
    """Weight scored strategies and sort them descending by weighted score."""
    ranked = [
        (strategy, score, rank_strategy(strategy, score)) for strategy, score in strategies_with_scores
    ]
    return sorted(ranked, key=lambda item: item[2], reverse=True)


def rank_scenario(
    scenario_id: str, graph_client: GraphClient = graph_queries
) -> list[tuple[Strategy, float, float]]:
    """Run reasoning + scoring for a scenario, then weight and sort the results."""
    scored_strategies = score_scenario(scenario_id, graph_client)
    return rank_strategies(scored_strategies)
