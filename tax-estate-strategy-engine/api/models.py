"""Pydantic response models for the API.

Every model here mirrors the shape already produced by an existing
engine — nothing is invented: `ScenarioSummary` mirrors the
`ClientScenario` node dict returned by the graph client,
`StrategyResult` mirrors `reasoning.rules.Strategy` (plus the optional
raw/weighted scores `scoring.engine` and `ranking.engine` attach to it),
`ReportResponse` wraps the Markdown string `reporting.builder` returns,
and `RankingResponse` wraps the list `ranking.engine.rank_scenario`
returns. The `from_*` classmethods are the only place that translate
engine output into these shapes, so routers stay thin.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from reasoning.rules import Strategy, StrategyType


class ScenarioSummary(BaseModel):
    """Summary of a `ClientScenario` as stored in the graph."""

    id: str
    tax_year: int | None = None
    filing_status: str | None = None
    income_range: str | None = None
    state: str | None = None
    existing_elections: list[str] = Field(default_factory=list)

    @classmethod
    def from_node(cls, scenario_node: dict[str, Any]) -> "ScenarioSummary":
        return cls(
            id=scenario_node["id"],
            tax_year=scenario_node.get("tax_year"),
            filing_status=scenario_node.get("filing_status"),
            income_range=scenario_node.get("income_range"),
            state=scenario_node.get("state"),
            existing_elections=list(scenario_node.get("existing_elections") or []),
        )


class IngestionResult(BaseModel):
    """Summary returned after ingesting a `ClientScenario` into the graph."""

    scenario_id: str
    entities: int
    activities: int
    assets: int
    constraints: int
    state_tax_rules: int


class StrategyResult(BaseModel):
    """A strategy from the reasoning engine, with its optional raw/weighted scores.

    `raw_score` is set once `scoring.engine` has scored the strategy;
    `weighted_score` is set once `ranking.engine` has weighted it. Both
    are `None` for a strategy that has only been through reasoning.
    """

    name: str
    type: StrategyType
    related_entities: list[str] = Field(default_factory=list)
    related_activities: list[str] = Field(default_factory=list)
    related_assets: list[str] = Field(default_factory=list)
    related_constraints: list[str] = Field(default_factory=list)
    related_sections: list[str] = Field(default_factory=list)
    estimated_inputs: dict[str, Any] = Field(default_factory=dict)
    raw_score: float | None = None
    weighted_score: float | None = None

    @classmethod
    def from_strategy(
        cls,
        strategy: Strategy,
        raw_score: float | None = None,
        weighted_score: float | None = None,
    ) -> "StrategyResult":
        return cls(
            name=strategy.name,
            type=strategy.type,
            related_entities=strategy.related_entities,
            related_activities=strategy.related_activities,
            related_assets=strategy.related_assets,
            related_constraints=strategy.related_constraints,
            related_sections=strategy.related_sections,
            estimated_inputs=strategy.estimated_inputs,
            raw_score=raw_score,
            weighted_score=weighted_score,
        )


class RankingResponse(BaseModel):
    """The ranked (weighted, sorted) strategies for a scenario."""

    scenario_id: str
    strategies: list[StrategyResult] = Field(default_factory=list)


class ReportResponse(BaseModel):
    """The full Markdown strategy report for a scenario."""

    scenario_id: str
    markdown: str
