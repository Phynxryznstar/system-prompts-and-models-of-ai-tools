"""Scoring formulas for evaluating tax efficiency of a strategy.

Each `score_*` function does pure math: it takes the `Strategy` object a
`reasoning.rules` rule produced (using `strategy.estimated_inputs` and
related_* lists) and returns a single numeric score — an illustrative
dollar-value estimate of the strategy's benefit. Formulas never touch
the graph or the reasoning engine; that orchestration lives in
`scoring.engine`.

The scenario/graph data model doesn't yet carry real dollar figures per
entity/activity (actual income, W-2 wages, UBIA, asset basis, etc.) —
that arrives with richer ingestion later. Until then, these formulas
combine the counts the reasoning engine captured in `estimated_inputs`
with illustrative per-unit dollar assumptions and simplified rates
(named `ASSUMED_*` below), so the scoring engine has real numbers to
rank strategies on today. Swap these constants for actual client/tax
data later without changing any calling code.
"""

from __future__ import annotations

from typing import Callable

from reasoning.rules import Strategy

# --- Shared rate assumptions -------------------------------------------------

TOP_MARGINAL_INDIVIDUAL_RATE = 0.37
FLAT_CORPORATE_RATE = 0.21
FEDERAL_ESTATE_TAX_RATE = 0.40
LONG_TERM_CAPITAL_GAINS_AND_NIIT_RATE = 0.238  # 20% LTCG + 3.8% NIIT
SELF_EMPLOYMENT_PAYROLL_TAX_RATE = 0.153
QBI_DEDUCTION_RATE = 0.20
CURRENT_BONUS_DEPRECIATION_RATE = 0.60  # phased-down §168(k) bonus rate

# --- Per-strategy placeholder assumptions ------------------------------------

ASSUMED_QBI_PER_ACTIVITY = 500_000.0
QBI_WAGE_UBIA_LIMITATION_DISCOUNT = 0.5  # haircut for the W-2 wage / UBIA limit

ASSUMED_INCOME_PER_GROUPABLE_ACTIVITY = 150_000.0

ASSUMED_INTEREST_EXPENSE_PER_FARM_ACTIVITY = 100_000.0

ASSUMED_BASIS_STEP_UP_PER_PARTNERSHIP = 750_000.0
BASIS_STEP_UP_ANNUAL_DEPRECIATION_RATE = 1 / 15

ASSUMED_QBI_GAIN_PER_SCORP = 100_000.0

ASSUMED_INCOME_SHIFTED_PER_CCORP = 300_000.0

COST_SEG_ACCELERATION_SHARE = 0.30  # share of asset value reclassified to shorter lives

IDGT_FROZEN_APPRECIATION_SHARE = 0.30

FLP_VALUATION_DISCOUNT_RATE = 0.30
ASSUMED_VALUE_PER_PARTNERSHIP = 750_000.0

ASSUMED_SLAT_GIFT_VALUE = 1_000_000.0  # SLAT rule doesn't yet capture an asset total

GRAT_REMAINDER_SHARE = 0.25

CRT_CHARITABLE_DEDUCTION_SHARE = 0.30

DYNASTY_TRUST_TRANSFERABLE_WEALTH_SHARE = 0.5
DYNASTY_TRUST_GENERATIONS_SHELTERED = 2

ASSUMED_INCOME_PER_STATE_ACTIVITY = 100_000.0
ASSUMED_STATE_TAX_RATE = 0.05
ASSUMED_VALUE_PER_DEPRECIABLE_ASSET = 400_000.0

STATE_ESTATE_TAX_EXEMPTION_GAP = 5_000_000.0  # federal exemption minus a typical state exemption
STATE_ESTATE_TAX_RATE = 0.16


# ---------------------------------------------------------------------------
# Tax strategies
# ---------------------------------------------------------------------------


def score_199a_qbi_optimization(strategy: Strategy) -> float:
    """§199A: QBI x 20%, discounted for the W-2 wage / UBIA limitation."""
    activity_count = strategy.estimated_inputs.get("qualifying_activity_count", 0)
    qbi = activity_count * ASSUMED_QBI_PER_ACTIVITY
    return qbi * QBI_DEDUCTION_RATE * QBI_WAGE_UBIA_LIMITATION_DISCOUNT


def score_469_passive_activity_grouping(strategy: Strategy) -> float:
    """§469: tax value of converting grouped activities from passive to active."""
    activity_count = strategy.estimated_inputs.get("groupable_activity_count", 0)
    convertible_income = activity_count * ASSUMED_INCOME_PER_GROUPABLE_ACTIVITY
    return convertible_income * TOP_MARGINAL_INDIVIDUAL_RATE


def score_163j_farming_election(strategy: Strategy) -> float:
    """§163(j): tax value of restoring the business interest deduction for farming."""
    activity_count = strategy.estimated_inputs.get("farming_activity_count", 0)
    restored_interest = activity_count * ASSUMED_INTEREST_EXPENSE_PER_FARM_ACTIVITY
    return restored_interest * TOP_MARGINAL_INDIVIDUAL_RATE


def score_754_basis_step_up(strategy: Strategy) -> float:
    """§754: tax value of the depreciation increase from a partnership basis step-up."""
    partnership_count = strategy.estimated_inputs.get("partnership_count", 0)
    step_up = partnership_count * ASSUMED_BASIS_STEP_UP_PER_PARTNERSHIP
    annual_depreciation_increase = step_up * BASIS_STEP_UP_ANNUAL_DEPRECIATION_RATE
    return annual_depreciation_increase * TOP_MARGINAL_INDIVIDUAL_RATE


def score_scorp_wage_optimization(strategy: Strategy) -> float:
    """S-corp: QBI increase from an optimized wage mix, net of the added payroll tax."""
    s_corp_count = strategy.estimated_inputs.get("s_corporation_count", 0)
    qbi_gain = s_corp_count * ASSUMED_QBI_GAIN_PER_SCORP
    qbi_tax_value = qbi_gain * QBI_DEDUCTION_RATE * TOP_MARGINAL_INDIVIDUAL_RATE
    payroll_tax_cost = qbi_gain * SELF_EMPLOYMENT_PAYROLL_TAX_RATE
    return qbi_tax_value - payroll_tax_cost


def score_ccorp_rate_arbitrage(strategy: Strategy) -> float:
    """C-corp: tax saved by shifting income from individual to flat corporate rates."""
    c_corp_count = strategy.estimated_inputs.get("c_corporation_count", 0)
    income_shifted = c_corp_count * ASSUMED_INCOME_SHIFTED_PER_CCORP
    return income_shifted * (TOP_MARGINAL_INDIVIDUAL_RATE - FLAT_CORPORATE_RATE)


def score_cost_segregation_bonus_depreciation(strategy: Strategy) -> float:
    """Cost segregation + bonus depreciation: tax value of accelerated depreciation."""
    total_asset_value = strategy.estimated_inputs.get("total_asset_value", 0)
    accelerated_value = total_asset_value * COST_SEG_ACCELERATION_SHARE * CURRENT_BONUS_DEPRECIATION_RATE
    return accelerated_value * TOP_MARGINAL_INDIVIDUAL_RATE


# ---------------------------------------------------------------------------
# Estate strategies
# ---------------------------------------------------------------------------


def score_idgt(strategy: Strategy) -> float:
    """IDGT: estate tax avoided on the appreciation frozen out of the estate."""
    total_asset_value = strategy.estimated_inputs.get("total_asset_value", 0)
    frozen_appreciation = total_asset_value * IDGT_FROZEN_APPRECIATION_SHARE
    return frozen_appreciation * FEDERAL_ESTATE_TAX_RATE


def score_flp_valuation_discounts(strategy: Strategy) -> float:
    """FLP: estate tax saved via minority/marketability valuation discounts."""
    partnership_count = strategy.estimated_inputs.get("partnership_count", 0)
    gross_value = partnership_count * ASSUMED_VALUE_PER_PARTNERSHIP
    discount = gross_value * FLP_VALUATION_DISCOUNT_RATE
    return discount * FEDERAL_ESTATE_TAX_RATE


def score_slat(strategy: Strategy) -> float:
    """SLAT: estate tax saved by removing a spouse-accessible gift from the estate."""
    return ASSUMED_SLAT_GIFT_VALUE * FEDERAL_ESTATE_TAX_RATE


def score_grat(strategy: Strategy) -> float:
    """GRAT: estate tax saved on the remainder interest passing to beneficiaries."""
    total_asset_value = strategy.estimated_inputs.get("total_asset_value", 0)
    remainder_value = total_asset_value * GRAT_REMAINDER_SHARE
    return remainder_value * FEDERAL_ESTATE_TAX_RATE


def score_crt(strategy: Strategy) -> float:
    """CRT: charitable deduction value plus capital-gains tax deferred on the gift."""
    total_asset_value = strategy.estimated_inputs.get("total_asset_value", 0)
    charitable_deduction_value = total_asset_value * CRT_CHARITABLE_DEDUCTION_SHARE * TOP_MARGINAL_INDIVIDUAL_RATE
    capital_gains_deferred = total_asset_value * LONG_TERM_CAPITAL_GAINS_AND_NIIT_RATE
    return charitable_deduction_value + capital_gains_deferred


def score_dynasty_trust(strategy: Strategy) -> float:
    """Dynasty trust: estate tax saved across generations by sheltering transferred wealth."""
    income_range_high = strategy.estimated_inputs.get("income_range_high", 0)
    transferable_wealth = income_range_high * DYNASTY_TRUST_TRANSFERABLE_WEALTH_SHARE
    return transferable_wealth * FEDERAL_ESTATE_TAX_RATE * DYNASTY_TRUST_GENERATIONS_SHELTERED


# ---------------------------------------------------------------------------
# State strategies
# ---------------------------------------------------------------------------


def score_state_conformity(strategy: Strategy) -> float:
    """State conformity: state tax impact of federal bonus depreciation add-back/decoupling."""
    activity_count = len(strategy.related_activities)
    state_taxable_income = activity_count * ASSUMED_INCOME_PER_STATE_ACTIVITY
    return state_taxable_income * CURRENT_BONUS_DEPRECIATION_RATE * ASSUMED_STATE_TAX_RATE


def score_state_estate_tax_exposure(strategy: Strategy) -> float:
    """State estate tax exposure: tax on the gap between state and federal exemptions."""
    return STATE_ESTATE_TAX_EXEMPTION_GAP * STATE_ESTATE_TAX_RATE


def score_state_depreciation_differences(strategy: Strategy) -> float:
    """State depreciation differences: timing benefit of state/federal decoupling."""
    asset_count = strategy.estimated_inputs.get("depreciable_asset_count", 0)
    asset_value = asset_count * ASSUMED_VALUE_PER_DEPRECIABLE_ASSET
    timing_benefit = asset_value * CURRENT_BONUS_DEPRECIATION_RATE
    return timing_benefit * ASSUMED_STATE_TAX_RATE


# ---------------------------------------------------------------------------
# Dispatch: map a Strategy back to the formula that scores it
# ---------------------------------------------------------------------------

# Most strategies have a fixed name and map directly; the three state rules
# prefix their name with the state code (e.g. "FL Federal Conformity
# Review"), so those are matched by a stable suffix instead.
_EXACT_NAME_FORMULAS: dict[str, Callable[[Strategy], float]] = {
    "§199A Qualified Business Income Optimization": score_199a_qbi_optimization,
    "§469 Passive Activity Grouping Election": score_469_passive_activity_grouping,
    "§163(j) Farming Business Election": score_163j_farming_election,
    "§754 Partnership Basis Step-Up Election": score_754_basis_step_up,
    "S-Corporation Wage Optimization": score_scorp_wage_optimization,
    "C-Corporation Rate Arbitrage": score_ccorp_rate_arbitrage,
    "Cost Segregation + Bonus Depreciation": score_cost_segregation_bonus_depreciation,
    "Intentionally Defective Grantor Trust (IDGT)": score_idgt,
    "FLP Valuation Discounts": score_flp_valuation_discounts,
    "Spousal Lifetime Access Trust (SLAT)": score_slat,
    "Grantor Retained Annuity Trust (GRAT)": score_grat,
    "Charitable Remainder Trust (CRT)": score_crt,
    "Dynasty Trust": score_dynasty_trust,
}

_NAME_SUFFIX_FORMULAS: list[tuple[str, Callable[[Strategy], float]]] = [
    ("Federal Conformity Review", score_state_conformity),
    ("State Estate/Inheritance Tax Exposure", score_state_estate_tax_exposure),
    ("Bonus Depreciation Decoupling", score_state_depreciation_differences),
]


def get_formula_for_strategy(strategy: Strategy) -> Callable[[Strategy], float] | None:
    """Return the formula that scores `strategy`, or None if none is registered."""
    formula = _EXACT_NAME_FORMULAS.get(strategy.name)
    if formula is not None:
        return formula

    for suffix, suffix_formula in _NAME_SUFFIX_FORMULAS:
        if strategy.name.endswith(suffix):
            return suffix_formula

    return None
