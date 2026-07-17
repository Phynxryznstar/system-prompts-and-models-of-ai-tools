"""Scenario endpoints: read a ClientScenario's summary, or ingest a new one.

Routers only translate HTTP <-> engine calls: this module loads data via
the graph client and the ingestion engine, and shapes the result with
`api.models`. No reasoning/scoring/ranking logic lives here.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from api.models import IngestionResult, ScenarioSummary
from graph import queries as graph_queries
from graph.schema import NodeLabel
from ingestion.scenario_ingestion import ingest_client_scenario
from reasoning.scenario_schema import ClientScenario

router = APIRouter(prefix="/scenario", tags=["scenario"])


@router.get("/{scenario_id}", response_model=ScenarioSummary)
def get_scenario(scenario_id: str) -> ScenarioSummary:
    """Return a `ClientScenario`'s summary as stored in the graph."""
    scenario_node = graph_queries.get_node(NodeLabel.CLIENT_SCENARIO, scenario_id)
    if scenario_node is None:
        raise HTTPException(status_code=404, detail=f"ClientScenario '{scenario_id}' not found.")
    return ScenarioSummary.from_node(scenario_node)


@router.post("/ingest", response_model=IngestionResult, status_code=201)
def ingest_scenario(scenario: ClientScenario) -> IngestionResult:
    """Ingest a `ClientScenario` JSON payload into the graph."""
    summary = ingest_client_scenario(scenario)
    return IngestionResult(scenario_id=scenario.id, **summary)
