"""Strategy endpoints: reasoning, scoring, ranking, and reporting for a scenario.

Each endpoint loads the scenario via the graph client (implicitly, by
calling into the matching engine — every engine here already loads the
scenario itself and raises `ValueError` if it's missing), runs exactly
one engine, and shapes the result with `api.models`. No reasoning,
scoring, ranking, or report-building logic lives in this module.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from api.models import RankingResponse, ReportResponse, StrategyResult
from graph import queries as graph_queries
from ranking.engine import rank_scenario
from reasoning.engine import find_all_strategies
from reporting.builder import build_full_report
from scoring.engine import score_scenario

router = APIRouter(prefix="/strategies", tags=["strategies"])


def _not_found(scenario_id: str) -> HTTPException:
    return HTTPException(status_code=404, detail=f"ClientScenario '{scenario_id}' not found.")


@router.get("/{scenario_id}/reasoning", response_model=list[StrategyResult])
def get_reasoning(scenario_id: str) -> list[StrategyResult]:
    """Return every strategy the reasoning engine finds for this scenario."""
    try:
        strategies = find_all_strategies(scenario_id, graph_queries)
    except ValueError as exc:
        raise _not_found(scenario_id) from exc
    return [StrategyResult.from_strategy(strategy) for strategy in strategies]


@router.get("/{scenario_id}/scoring", response_model=list[StrategyResult])
def get_scoring(scenario_id: str) -> list[StrategyResult]:
    """Return every strategy for this scenario along with its raw score."""
    try:
        scored = score_scenario(scenario_id, graph_queries)
    except ValueError as exc:
        raise _not_found(scenario_id) from exc
    return [StrategyResult.from_strategy(strategy, raw_score=score) for strategy, score in scored]


@router.get("/{scenario_id}/ranking", response_model=RankingResponse)
def get_ranking(scenario_id: str) -> RankingResponse:
    """Return every strategy for this scenario, weighted and sorted by rank."""
    try:
        ranked = rank_scenario(scenario_id, graph_queries)
    except ValueError as exc:
        raise _not_found(scenario_id) from exc
    strategies = [
        StrategyResult.from_strategy(strategy, raw_score=raw_score, weighted_score=weighted_score)
        for strategy, raw_score, weighted_score in ranked
    ]
    return RankingResponse(scenario_id=scenario_id, strategies=strategies)


@router.get("/{scenario_id}/report", response_model=ReportResponse)
def get_report(scenario_id: str) -> ReportResponse:
    """Return the full Markdown strategy report for this scenario."""
    try:
        markdown = build_full_report(scenario_id, graph_queries)
    except ValueError as exc:
        raise _not_found(scenario_id) from exc
    return ReportResponse(scenario_id=scenario_id, markdown=markdown)
