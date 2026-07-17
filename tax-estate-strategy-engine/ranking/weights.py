"""Default weighting values used to rank strategies by domain.

`get_weight(strategy_type)` is the single place that maps a
`StrategyType` to its weight, so `ranking.engine` (and anything else
that needs a weight) never hardcodes the mapping itself.
"""

from __future__ import annotations

from reasoning.rules import StrategyType

TAX_WEIGHT = 1.0
ESTATE_WEIGHT = 1.3
STATE_WEIGHT = 0.8
COMBINED_WEIGHT = 1.5

_WEIGHTS_BY_TYPE: dict[StrategyType, float] = {
    StrategyType.TAX: TAX_WEIGHT,
    StrategyType.ESTATE: ESTATE_WEIGHT,
    StrategyType.STATE: STATE_WEIGHT,
    StrategyType.COMBINED: COMBINED_WEIGHT,
}


def get_weight(strategy_type: StrategyType) -> float:
    """Return the ranking weight for a given strategy type."""
    return _WEIGHTS_BY_TYPE[strategy_type]
