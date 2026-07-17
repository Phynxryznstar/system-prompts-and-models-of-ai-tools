"""Markdown templates for the strategy report.

Every `*_TEMPLATE` here is a plain Python string with `{placeholder}`
slots, filled in with `str.format(**kwargs)` by `reporting.builder`.
Templates hold formatting/layout only — they never compute or fetch
anything themselves. They render clean, heading-and-table Markdown with
no custom syntax, so the same strings can be converted straight to
HTML/PDF later without changes.
"""

REPORT_HEADER_TEMPLATE = """\
# Tax + Estate Strategy Report

**Scenario:** {scenario_id}
**Generated:** {generated_at}
"""

SCENARIO_SUMMARY_TEMPLATE = """\
## Scenario Summary

| Field | Value |
| --- | --- |
| Scenario ID | {scenario_id} |
| Tax Year | {tax_year} |
| Filing Status | {filing_status} |
| Income Range | {income_range} |
| State | {state} |
| Existing Elections | {existing_elections} |
"""

STRATEGY_SECTION_TEMPLATE = """\
### {strategy_name} ({strategy_type})

**Estimated benefit:** ${score:,.0f}

{narrative}

| Related to | Value |
| --- | --- |
| Entities | {related_entities} |
| Activities | {related_activities} |
| Assets | {related_assets} |
| Constraints | {related_constraints} |
| IRC Sections | {related_sections} |
"""

FOOTER_TEMPLATE = """\
---

**Total strategies identified:** {strategy_count}
**Total estimated benefit:** ${total_score:,.0f}

_This report was generated automatically by the Tax + Estate Strategy \
Engine and is for planning-discussion purposes only — it is not tax, \
legal, or financial advice. Estimated benefits use illustrative \
assumptions and should be verified by a qualified professional before \
acting on them._

_Generated {generated_at}._
"""
