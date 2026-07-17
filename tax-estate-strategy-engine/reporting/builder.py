"""Assembles a Markdown strategy report from scenario + strategy data.

Templates in `reporting.templates` hold formatting only; this module
pulls together the actual content — scenario facts, each strategy's
detected context, and its score — and fills the templates in. It never
introduces its own Markdown/HTML syntax beyond what the templates
already define, so the report stays clean and ready for a future
Markdown-to-PDF export step.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from graph import queries as graph_queries
from graph.schema import NodeLabel
from reasoning.rules import GraphClient, Strategy
from reporting.templates import (
    FOOTER_TEMPLATE,
    REPORT_HEADER_TEMPLATE,
    SCENARIO_SUMMARY_TEMPLATE,
    STRATEGY_SECTION_TEMPLATE,
)
from scoring.engine import score_scenario

# Short, plain-English explanations of why each strategy tends to apply.
# Keyed the same way as `scoring.formulas`'s dispatch table: an exact
# name for most strategies, and a stable suffix for the three state
# rules whose names are prefixed with a state code.
_STRATEGY_NARRATIVES: dict[str, str] = {
    "§199A Qualified Business Income Optimization": (
        "The client has qualifying pass-through trade-or-business activity, so structuring "
        "wages, UBIA, and entity grouping to maximize the §199A deduction is worth pursuing."
    ),
    "§469 Passive Activity Grouping Election": (
        "Multiple trade-or-business activities across different entities create an "
        "opportunity to group them under §469, changing which losses and income are "
        "treated as active vs. passive."
    ),
    "§163(j) Farming Business Election": (
        "The client operates a farming activity, which can elect out of the §163(j) "
        "business interest limitation in exchange for slower depreciation on farm assets."
    ),
    "§754 Partnership Basis Step-Up Election": (
        "The client holds partnership interests; a §754 election lets a future transfer "
        "step up the partnership's inside basis, increasing depreciation going forward."
    ),
    "S-Corporation Wage Optimization": (
        "The client owns an S-corporation, so the split between W-2 wages and "
        "distributions can be tuned to balance the QBI deduction against payroll tax."
    ),
    "C-Corporation Rate Arbitrage": (
        "The client owns a C-corporation; shifting income to it can arbitrage the flat "
        "corporate rate against a much higher individual marginal rate."
    ),
    "Cost Segregation + Bonus Depreciation": (
        "The client holds real property assets suited to a cost segregation study, "
        "accelerating depreciation through remaining bonus depreciation."
    ),
    "Intentionally Defective Grantor Trust (IDGT)": (
        "The client faces estate tax risk; an IDGT can freeze the value of transferred "
        "assets for estate tax purposes while the grantor keeps paying the income tax on them."
    ),
    "FLP Valuation Discounts": (
        "The client's partnership interests, combined with estate tax risk, make them a "
        "candidate for minority/marketability discounts via a family limited partnership."
    ),
    "Spousal Lifetime Access Trust (SLAT)": (
        "The client is married and faces estate tax risk; a SLAT can remove assets from "
        "the estate while preserving indirect access to them through a spouse."
    ),
    "Grantor Retained Annuity Trust (GRAT)": (
        "The client holds high-value assets and faces estate tax risk, making a GRAT "
        "useful for transferring future appreciation at minimal gift tax cost."
    ),
    "Charitable Remainder Trust (CRT)": (
        "The client's asset base and NIIT/estate tax exposure support a CRT, which can "
        "defer capital gains tax and generate a current charitable deduction."
    ),
    "Dynasty Trust": (
        "The client's income level and estate tax risk support multi-generational "
        "planning through a dynasty trust to shelter transferred wealth from repeated "
        "estate/GST tax."
    ),
}

_NARRATIVE_SUFFIXES: list[tuple[str, str]] = [
    (
        "Federal Conformity Review",
        "The client's state may not fully conform to recent federal tax changes, so "
        "federal elections should be reviewed for their state-level treatment.",
    ),
    (
        "State Estate/Inheritance Tax Exposure",
        "The client's state imposes its own estate or inheritance tax with a lower "
        "exemption than the federal one, creating exposure beyond the federal estate tax.",
    ),
    (
        "Bonus Depreciation Decoupling",
        "The client's state decouples from federal bonus depreciation, so state and "
        "federal depreciation schedules will diverge for qualifying assets.",
    ),
]

_DEFAULT_NARRATIVE = (
    "This strategy was flagged by the reasoning engine as potentially applicable based "
    "on the client's entities, activities, and constraints."
)


def _narrative_for_strategy(strategy: Strategy) -> str:
    narrative = _STRATEGY_NARRATIVES.get(strategy.name)
    if narrative is not None:
        return narrative

    for suffix, suffix_narrative in _NARRATIVE_SUFFIXES:
        if strategy.name.endswith(suffix):
            return suffix_narrative

    return _DEFAULT_NARRATIVE


def _join_or_none(values: list[str]) -> str:
    return ", ".join(values) if values else "None"


def build_strategy_section(strategy: Strategy, score: float) -> str:
    """Render one strategy's Markdown section, given its score."""
    return STRATEGY_SECTION_TEMPLATE.format(
        strategy_name=strategy.name,
        strategy_type=strategy.type.value,
        score=score,
        narrative=_narrative_for_strategy(strategy),
        related_entities=_join_or_none(strategy.related_entities),
        related_activities=_join_or_none(strategy.related_activities),
        related_assets=_join_or_none(strategy.related_assets),
        related_constraints=_join_or_none(strategy.related_constraints),
        related_sections=_join_or_none(strategy.related_sections),
    )


def build_scenario_summary(scenario_node: dict[str, Any]) -> str:
    """Render the Markdown scenario-summary section from a ClientScenario node."""
    existing_elections = scenario_node.get("existing_elections") or []
    return SCENARIO_SUMMARY_TEMPLATE.format(
        scenario_id=scenario_node.get("id", "Unknown"),
        tax_year=scenario_node.get("tax_year", "Unknown"),
        filing_status=scenario_node.get("filing_status", "Unknown"),
        income_range=scenario_node.get("income_range", "Unknown"),
        state=scenario_node.get("state", "Unknown"),
        existing_elections=_join_or_none(list(existing_elections)),
    )


def build_full_report(scenario_id: str, graph_client: GraphClient = graph_queries) -> str:
    """Load a scenario, run reasoning + scoring, and render the full Markdown report."""
    scenario_node = graph_client.get_node(NodeLabel.CLIENT_SCENARIO, scenario_id)
    if scenario_node is None:
        raise ValueError(f"ClientScenario '{scenario_id}' not found in the graph.")

    scored_strategies = sorted(
        score_scenario(scenario_id, graph_client), key=lambda pair: pair[1], reverse=True
    )
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    header = REPORT_HEADER_TEMPLATE.format(scenario_id=scenario_id, generated_at=generated_at)
    summary = build_scenario_summary(scenario_node)

    if scored_strategies:
        sections = "\n".join(
            build_strategy_section(strategy, score) for strategy, score in scored_strategies
        )
    else:
        sections = "_No strategies were identified for this scenario._\n"

    footer = FOOTER_TEMPLATE.format(
        strategy_count=len(scored_strategies),
        total_score=sum(score for _, score in scored_strategies),
        generated_at=generated_at,
    )

    return "\n".join([header, summary, "## Identified Strategies\n", sections, footer])
