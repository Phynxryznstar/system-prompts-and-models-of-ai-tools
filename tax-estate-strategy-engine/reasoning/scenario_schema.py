"""JSON schema and loader for a `ClientScenario`.

A `ClientScenario` describes one client's facts for a given tax year —
their entities (individuals, S-corps, partnerships, etc.), the activities
those entities engage in, the assets involved, any elections already in
place, and the risk/constraint tags that should steer the reasoning
engine (e.g. NIIT exposure, passive loss limitation risk).

Ingestion scripts and the reasoning engine both consume this shape, so it
lives here as the single source of truth for what a valid scenario file
looks like.

Example JSON file:

    {
      "id": "scenario_001",
      "tax_year": 2026,
      "filing_status": "MFJ",
      "income_range": "7000000-10000000",
      "state": "FL",
      "entities": [
        { "id": "entity_client", "type": "individual", "owner": "client" },
        { "id": "entity_spouse", "type": "individual", "owner": "spouse" },
        { "id": "entity_scorp", "type": "s_corporation", "owner": "client" },
        { "id": "entity_ccorp", "type": "c_corporation", "owner": "spouse" },
        {
          "id": "partnership_1",
          "type": "partnership",
          "ownership_percent": 50,
          "active_participation": true
        }
      ],
      "activities": [
        {
          "id": "activity_trade_business_1",
          "type": "trade_or_business",
          "entity": "partnership_1",
          "active": true
        },
        {
          "id": "activity_rental_1",
          "type": "rental_real_estate",
          "entity": "entity_client",
          "active": true
        }
      ],
      "assets": [
        {
          "id": "asset_farm_property",
          "type": "commercial_farm",
          "value": 2500000,
          "acreage": 20,
          "buildings": 6,
          "activity": "activity_farm"
        }
      ],
      "existing_elections": [],
      "constraints": [
        "high_income",
        "NIIT_risk",
        "estate_tax_risk",
        "passive_loss_risk",
        "interest_limitation_risk"
      ]
    }
"""

from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, Field


class Entity(BaseModel):
    """A party or legal entity involved in the client's structure.

    `owner`, `ownership_percent`, and `active_participation` are optional
    because they only apply to some entity types (e.g. an `individual`
    has an `owner`, while a `partnership` has an `ownership_percent`).
    """

    id: str
    type: str
    owner: str | None = None
    ownership_percent: float | None = None
    active_participation: bool | None = None


class Activity(BaseModel):
    """A trade, business, or other activity carried on by an entity."""

    id: str
    type: str
    entity: str
    active: bool | None = None


class Asset(BaseModel):
    """An asset held by the client, optionally tied to an activity.

    `acreage` and `buildings` are optional because they only apply to
    certain asset types (e.g. farm or real estate holdings).
    """

    id: str
    type: str
    value: float | None = None
    acreage: float | None = None
    buildings: int | None = None
    activity: str | None = None


class ClientScenario(BaseModel):
    """A single client's facts for a given tax year.

    See the module docstring for a complete example JSON document.
    """

    id: str
    tax_year: int
    filing_status: str
    income_range: str
    state: str
    entities: list[Entity] = Field(default_factory=list)
    activities: list[Activity] = Field(default_factory=list)
    assets: list[Asset] = Field(default_factory=list)
    existing_elections: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)


def load_client_scenario_from_file(path: str) -> ClientScenario:
    """Load and validate a `ClientScenario` from a JSON file on disk.

    Raises:
        FileNotFoundError: If `path` does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        pydantic.ValidationError: If the JSON does not match the
            `ClientScenario` schema.
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return ClientScenario.model_validate(data)
