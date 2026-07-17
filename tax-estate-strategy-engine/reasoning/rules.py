"""Rule definitions used by the reasoning engine to evaluate strategies.

Each `rule_*` function looks at a single `ClientScenario` already stored
in the graph, decides whether one specific tax/estate/state strategy is
worth surfacing for that client, and — if so — returns a `Strategy`
object describing what it touches (entities, activities, assets,
constraints, tax sections) and the raw numbers a future scoring engine
will need (`estimated_inputs`). A rule returns `None` when the strategy
doesn't apply.

Rules never score anything — no dollar benefit, no ranking, no
probability of audit. That is the scoring engine's job (see the
`scoring` package); rules only detect applicability and shape the
strategy for it.

Every rule takes an optional `graph_client`, defaulting to the real
`graph.queries` module, so tests can pass in a fake with the same
`get_node` / `get_related_nodes` interface instead of hitting Neo4j.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Protocol

from graph import queries as graph_queries
from graph.schema import NodeLabel, RelationshipType

# Thresholds below are illustrative placeholders for demo purposes; a
# real deployment would source these (and the state lists) from ingested
# StateTaxRule / RegSection data rather than hardcoding them here.
HIGH_VALUE_ASSET_THRESHOLD = 250_000
DYNASTY_TRUST_INCOME_THRESHOLD = 5_000_000

STATES_WITH_ESTATE_OR_INHERITANCE_TAX = {
    "CT", "HI", "IL", "IA", "KY", "ME", "MD", "MA", "MN",
    "NE", "NJ", "NY", "OR", "PA", "RI", "VT", "WA", "DC",
}

STATES_DECOUPLED_FROM_BONUS_DEPRECIATION = {
    "AR", "CA", "MS", "NJ", "NY", "PA",
}


class StrategyType(str, Enum):
    """The domain a strategy primarily belongs to."""

    TAX = "tax"
    ESTATE = "estate"
    STATE = "state"
    COMBINED = "combined"


@dataclass
class Strategy:
    """A candidate strategy detected for a client scenario.

    `estimated_inputs` carries whatever raw numbers/flags the rule could
    pull from the graph (counts, asset values, income range, etc.) — the
    scoring engine turns these into an actual estimated benefit later.
    """

    name: str
    type: StrategyType
    related_entities: list[str] = field(default_factory=list)
    related_activities: list[str] = field(default_factory=list)
    related_assets: list[str] = field(default_factory=list)
    related_constraints: list[str] = field(default_factory=list)
    related_sections: list[str] = field(default_factory=list)
    estimated_inputs: dict[str, Any] = field(default_factory=dict)


class GraphClient(Protocol):
    """The subset of `graph.queries` that rules rely on."""

    def get_node(
        self, label: NodeLabel, key_value: Any, key: str = "id"
    ) -> dict[str, Any] | None: ...

    def get_related_nodes(
        self,
        label: NodeLabel,
        key_value: Any,
        relationship: RelationshipType,
        related_label: NodeLabel,
        key: str = "id",
        direction: str = "out",
    ) -> list[dict[str, Any]]: ...


def _get_scenario(client_scenario_id: str, graph_client: GraphClient) -> dict[str, Any] | None:
    return graph_client.get_node(NodeLabel.CLIENT_SCENARIO, client_scenario_id)


def _get_scenario_entities(client_scenario_id: str, graph_client: GraphClient) -> list[dict[str, Any]]:
    return graph_client.get_related_nodes(
        NodeLabel.CLIENT_SCENARIO, client_scenario_id, RelationshipType.HAS_ENTITY, NodeLabel.ENTITY
    )


def _get_scenario_activities(client_scenario_id: str, graph_client: GraphClient) -> list[dict[str, Any]]:
    return graph_client.get_related_nodes(
        NodeLabel.CLIENT_SCENARIO, client_scenario_id, RelationshipType.HAS_ACTIVITY, NodeLabel.ACTIVITY
    )


def _get_scenario_assets(client_scenario_id: str, graph_client: GraphClient) -> list[dict[str, Any]]:
    return graph_client.get_related_nodes(
        NodeLabel.CLIENT_SCENARIO, client_scenario_id, RelationshipType.HAS_ASSET, NodeLabel.ASSET
    )


def _get_scenario_constraint_ids(client_scenario_id: str, graph_client: GraphClient) -> set[str]:
    constraints = graph_client.get_related_nodes(
        NodeLabel.CLIENT_SCENARIO, client_scenario_id, RelationshipType.SUBJECT_TO_CONSTRAINT, NodeLabel.CONSTRAINT
    )
    return {c["id"] for c in constraints}


def _parse_income_range(income_range: str | None) -> tuple[float, float] | None:
    """Parse a "low-high" income range string, e.g. "7000000-10000000"."""
    if not income_range:
        return None
    try:
        low, high = income_range.split("-")
        return float(low), float(high)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Tax strategies
# ---------------------------------------------------------------------------


def rule_199a_qbi_optimization(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """§199A: qualified business income deduction (QBI, W-2 wages, UBIA, grouping)."""
    entities = _get_scenario_entities(client_scenario_id, graph_client)
    activities = _get_scenario_activities(client_scenario_id, graph_client)

    pass_through_entity_ids = {e["id"] for e in entities if e.get("type") in ("s_corporation", "partnership")}
    qualifying_activities = [
        a for a in activities if a.get("type") == "trade_or_business" and a.get("entity") in pass_through_entity_ids
    ]
    if not qualifying_activities:
        return None

    return Strategy(
        name="§199A Qualified Business Income Optimization",
        type=StrategyType.TAX,
        related_entities=sorted(pass_through_entity_ids),
        related_activities=[a["id"] for a in qualifying_activities],
        related_sections=["irc_199a"],
        estimated_inputs={"qualifying_activity_count": len(qualifying_activities)},
    )


def rule_469_passive_activity_grouping(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """§469: grouping trade-or-business activities to manage active vs. passive treatment."""
    activities = _get_scenario_activities(client_scenario_id, graph_client)
    trade_or_business = [a for a in activities if a.get("type") == "trade_or_business"]
    distinct_entities = {a["entity"] for a in trade_or_business if a.get("entity")}

    if len(trade_or_business) < 2 or len(distinct_entities) < 2:
        return None

    return Strategy(
        name="§469 Passive Activity Grouping Election",
        type=StrategyType.TAX,
        related_entities=sorted(distinct_entities),
        related_activities=[a["id"] for a in trade_or_business],
        related_sections=["irc_469"],
        estimated_inputs={"groupable_activity_count": len(trade_or_business)},
    )


def rule_163j_farming_election(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """§163(j): electing out of the business interest limitation for a farming business."""
    activities = _get_scenario_activities(client_scenario_id, graph_client)
    farming_activities = [a for a in activities if a.get("type") == "farming"]
    if not farming_activities:
        return None

    return Strategy(
        name="§163(j) Farming Business Election",
        type=StrategyType.TAX,
        related_activities=[a["id"] for a in farming_activities],
        related_entities=sorted({a["entity"] for a in farming_activities if a.get("entity")}),
        related_sections=["irc_163j"],
        estimated_inputs={"farming_activity_count": len(farming_activities)},
    )


def rule_754_basis_step_up(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """§754: electing to step up a partnership's inside basis on a transfer of interest."""
    entities = _get_scenario_entities(client_scenario_id, graph_client)
    partnerships = [e for e in entities if e.get("type") == "partnership"]
    if not partnerships:
        return None

    return Strategy(
        name="§754 Partnership Basis Step-Up Election",
        type=StrategyType.TAX,
        related_entities=[e["id"] for e in partnerships],
        related_sections=["irc_754"],
        estimated_inputs={"partnership_count": len(partnerships)},
    )


def rule_scorp_wage_optimization(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """S-corp reasonable-compensation vs. distribution mix optimization."""
    entities = _get_scenario_entities(client_scenario_id, graph_client)
    s_corporations = [e for e in entities if e.get("type") == "s_corporation"]
    if not s_corporations:
        return None

    return Strategy(
        name="S-Corporation Wage Optimization",
        type=StrategyType.TAX,
        related_entities=[e["id"] for e in s_corporations],
        estimated_inputs={"s_corporation_count": len(s_corporations)},
    )


def rule_ccorp_rate_arbitrage(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """C-corp flat rate vs. high individual marginal rate arbitrage."""
    entities = _get_scenario_entities(client_scenario_id, graph_client)
    c_corporations = [e for e in entities if e.get("type") == "c_corporation"]
    if not c_corporations:
        return None

    return Strategy(
        name="C-Corporation Rate Arbitrage",
        type=StrategyType.TAX,
        related_entities=[e["id"] for e in c_corporations],
        estimated_inputs={"c_corporation_count": len(c_corporations)},
    )


def rule_cost_segregation_bonus_depreciation(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """Cost segregation + bonus depreciation on qualifying real property assets."""
    assets = _get_scenario_assets(client_scenario_id, graph_client)
    depreciable_assets = [
        a for a in assets if a.get("type") in ("commercial_real_estate", "commercial_farm") or a.get("buildings")
    ]
    if not depreciable_assets:
        return None

    return Strategy(
        name="Cost Segregation + Bonus Depreciation",
        type=StrategyType.TAX,
        related_assets=[a["id"] for a in depreciable_assets],
        related_activities=sorted({a["activity"] for a in depreciable_assets if a.get("activity")}),
        estimated_inputs={
            "depreciable_asset_count": len(depreciable_assets),
            "total_asset_value": sum(a.get("value") or 0 for a in depreciable_assets),
        },
    )


# ---------------------------------------------------------------------------
# Estate strategies
# ---------------------------------------------------------------------------


def rule_idgt(client_scenario_id: str, graph_client: GraphClient = graph_queries) -> Strategy | None:
    """Intentionally Defective Grantor Trust (IDGT) to freeze estate value."""
    constraint_ids = _get_scenario_constraint_ids(client_scenario_id, graph_client)
    if "estate_tax_risk" not in constraint_ids:
        return None

    assets = _get_scenario_assets(client_scenario_id, graph_client)

    return Strategy(
        name="Intentionally Defective Grantor Trust (IDGT)",
        type=StrategyType.ESTATE,
        related_assets=[a["id"] for a in assets],
        related_constraints=["estate_tax_risk"],
        estimated_inputs={"total_asset_value": sum(a.get("value") or 0 for a in assets)},
    )


def rule_flp_valuation_discounts(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """Family Limited Partnership (FLP) minority/marketability valuation discounts."""
    constraint_ids = _get_scenario_constraint_ids(client_scenario_id, graph_client)
    entities = _get_scenario_entities(client_scenario_id, graph_client)
    partnerships = [e for e in entities if e.get("type") == "partnership"]

    if "estate_tax_risk" not in constraint_ids or not partnerships:
        return None

    return Strategy(
        name="FLP Valuation Discounts",
        type=StrategyType.ESTATE,
        related_entities=[e["id"] for e in partnerships],
        related_constraints=["estate_tax_risk"],
        estimated_inputs={"partnership_count": len(partnerships)},
    )


def rule_slat(client_scenario_id: str, graph_client: GraphClient = graph_queries) -> Strategy | None:
    """Spousal Lifetime Access Trust (SLAT) for married clients with estate tax risk."""
    scenario = _get_scenario(client_scenario_id, graph_client)
    constraint_ids = _get_scenario_constraint_ids(client_scenario_id, graph_client)

    if not scenario or scenario.get("filing_status") != "MFJ" or "estate_tax_risk" not in constraint_ids:
        return None

    return Strategy(
        name="Spousal Lifetime Access Trust (SLAT)",
        type=StrategyType.ESTATE,
        related_constraints=["estate_tax_risk"],
        estimated_inputs={"filing_status": scenario["filing_status"]},
    )


def rule_grat(client_scenario_id: str, graph_client: GraphClient = graph_queries) -> Strategy | None:
    """Grantor Retained Annuity Trust (GRAT) for transferring future asset appreciation."""
    constraint_ids = _get_scenario_constraint_ids(client_scenario_id, graph_client)
    assets = _get_scenario_assets(client_scenario_id, graph_client)
    high_value_assets = [a for a in assets if (a.get("value") or 0) >= HIGH_VALUE_ASSET_THRESHOLD]

    if "estate_tax_risk" not in constraint_ids or not high_value_assets:
        return None

    return Strategy(
        name="Grantor Retained Annuity Trust (GRAT)",
        type=StrategyType.ESTATE,
        related_assets=[a["id"] for a in high_value_assets],
        related_constraints=["estate_tax_risk"],
        estimated_inputs={"total_asset_value": sum(a.get("value") or 0 for a in high_value_assets)},
    )


def rule_crt(client_scenario_id: str, graph_client: GraphClient = graph_queries) -> Strategy | None:
    """Charitable Remainder Trust (CRT) to defer/avoid gain and shrink the taxable estate."""
    constraint_ids = _get_scenario_constraint_ids(client_scenario_id, graph_client)
    relevant_constraints = constraint_ids & {"estate_tax_risk", "NIIT_risk"}

    assets = _get_scenario_assets(client_scenario_id, graph_client)
    total_value = sum(a.get("value") or 0 for a in assets)

    if not relevant_constraints or total_value < HIGH_VALUE_ASSET_THRESHOLD:
        return None

    return Strategy(
        name="Charitable Remainder Trust (CRT)",
        type=StrategyType.ESTATE,
        related_assets=[a["id"] for a in assets],
        related_constraints=sorted(relevant_constraints),
        estimated_inputs={"total_asset_value": total_value},
    )


def rule_dynasty_trust(client_scenario_id: str, graph_client: GraphClient = graph_queries) -> Strategy | None:
    """Dynasty trust for multi-generational estate/GST tax planning."""
    scenario = _get_scenario(client_scenario_id, graph_client)
    constraint_ids = _get_scenario_constraint_ids(client_scenario_id, graph_client)

    income_range = _parse_income_range(scenario.get("income_range")) if scenario else None
    high_income = income_range is not None and income_range[1] >= DYNASTY_TRUST_INCOME_THRESHOLD

    if "estate_tax_risk" not in constraint_ids or not high_income:
        return None

    return Strategy(
        name="Dynasty Trust",
        type=StrategyType.ESTATE,
        related_constraints=["estate_tax_risk"],
        estimated_inputs={"income_range_high": income_range[1]},
    )


# ---------------------------------------------------------------------------
# State strategies
# ---------------------------------------------------------------------------


def rule_state_conformity(client_scenario_id: str, graph_client: GraphClient = graph_queries) -> Strategy | None:
    """Federal-to-state conformity review for pass-through and depreciation items."""
    scenario = _get_scenario(client_scenario_id, graph_client)
    if not scenario or not scenario.get("state"):
        return None

    activities = _get_scenario_activities(client_scenario_id, graph_client)
    if not activities:
        return None

    state = scenario["state"]
    state_tax_rule = graph_client.get_node(NodeLabel.STATE_TAX_RULE, f"state_{state.lower()}")

    return Strategy(
        name=f"{state} Federal Conformity Review",
        type=StrategyType.STATE,
        related_activities=[a["id"] for a in activities],
        estimated_inputs={"state": state, "state_tax_rule_known": state_tax_rule is not None},
    )


def rule_state_estate_tax_exposure(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """Exposure to a separate state-level estate or inheritance tax."""
    scenario = _get_scenario(client_scenario_id, graph_client)
    state = scenario.get("state") if scenario else None
    constraint_ids = _get_scenario_constraint_ids(client_scenario_id, graph_client)

    if not state or state not in STATES_WITH_ESTATE_OR_INHERITANCE_TAX or "estate_tax_risk" not in constraint_ids:
        return None

    return Strategy(
        name=f"{state} State Estate/Inheritance Tax Exposure",
        type=StrategyType.STATE,
        related_constraints=["estate_tax_risk"],
        estimated_inputs={"state": state},
    )


def rule_state_depreciation_differences(
    client_scenario_id: str, graph_client: GraphClient = graph_queries
) -> Strategy | None:
    """State decoupling from federal bonus depreciation (IRC §168(k))."""
    scenario = _get_scenario(client_scenario_id, graph_client)
    state = scenario.get("state") if scenario else None
    if not state or state not in STATES_DECOUPLED_FROM_BONUS_DEPRECIATION:
        return None

    assets = _get_scenario_assets(client_scenario_id, graph_client)
    depreciable_assets = [
        a for a in assets if a.get("type") in ("commercial_real_estate", "commercial_farm") or a.get("buildings")
    ]
    if not depreciable_assets:
        return None

    return Strategy(
        name=f"{state} Bonus Depreciation Decoupling",
        type=StrategyType.STATE,
        related_assets=[a["id"] for a in depreciable_assets],
        estimated_inputs={"state": state, "depreciable_asset_count": len(depreciable_assets)},
    )


# ---------------------------------------------------------------------------
# Rule registries, grouped by domain for `reasoning.engine`
# ---------------------------------------------------------------------------

TAX_RULES = [
    rule_199a_qbi_optimization,
    rule_469_passive_activity_grouping,
    rule_163j_farming_election,
    rule_754_basis_step_up,
    rule_scorp_wage_optimization,
    rule_ccorp_rate_arbitrage,
    rule_cost_segregation_bonus_depreciation,
]

ESTATE_RULES = [
    rule_idgt,
    rule_flp_valuation_discounts,
    rule_slat,
    rule_grat,
    rule_crt,
    rule_dynasty_trust,
]

STATE_RULES = [
    rule_state_conformity,
    rule_state_estate_tax_exposure,
    rule_state_depreciation_differences,
]
