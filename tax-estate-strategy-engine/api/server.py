"""FastAPI app: wires together the scenario and strategy routers.

Routers call the engines (ingestion/reasoning/scoring/ranking/reporting);
the engines call the graph client; Pydantic models in `api.models`
define every response shape. This module only assembles the app — no
business logic lives here.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import scenario, strategies

app = FastAPI(
    title="Tax + Estate Strategy Engine API",
    description="Reasoning, scoring, ranking, and reporting over client tax/estate scenarios.",
)

# Allow all origins for now; tighten this once a frontend origin is known.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scenario.router)
app.include_router(strategies.router)


@app.get("/")
def root() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
