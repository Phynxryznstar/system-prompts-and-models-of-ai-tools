"""CLI command definitions for interacting with the strategy engine."""

from __future__ import annotations

import click

from graph.seed_example_data import seed_example_data
from ingestion.scenario_ingestion import ingest_client_scenario
from reasoning.engine import find_all_strategies
from reasoning.scenario_schema import load_client_scenario_from_file
from reporting.builder import build_full_report
from scoring.engine import score_scenario


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Tax + Estate Strategy Engine command-line interface."""
    if ctx.invoked_subcommand is None:
        click.echo("Tax + Estate Strategy Engine")


@cli.command("seed-example-data")
def seed_example_data_command() -> None:
    """Insert a small set of example nodes/relationships into Neo4j."""
    seed_example_data()


@cli.command("ingest-scenario")
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def ingest_scenario_command(path: str) -> None:
    """Load a ClientScenario JSON file and ingest it into Neo4j."""
    scenario = load_client_scenario_from_file(path)
    summary = ingest_client_scenario(scenario)
    click.echo(
        f"Summary for '{scenario.id}': "
        f"{summary['entities']} entities, "
        f"{summary['activities']} activities, "
        f"{summary['assets']} assets, "
        f"{summary['constraints']} constraints, "
        f"1 state tax rule ({scenario.state})"
    )


@cli.command("run-reasoning")
@click.argument("scenario_id")
def run_reasoning_command(scenario_id: str) -> None:
    """Run the reasoning engine against a ClientScenario already in Neo4j."""
    try:
        strategies = find_all_strategies(scenario_id)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc

    if not strategies:
        click.echo(f"No strategies found for scenario '{scenario_id}'.")
        return

    click.echo(f"Strategies for scenario '{scenario_id}':")
    for strategy in strategies:
        click.echo(f"  - {strategy.name} ({strategy.type.value})")


@cli.command("score-strategies")
@click.argument("scenario_id")
def score_strategies_command(scenario_id: str) -> None:
    """Run reasoning and scoring for a ClientScenario, then print the results."""
    try:
        scored = score_scenario(scenario_id)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc

    if not scored:
        click.echo(f"No strategies found for scenario '{scenario_id}'.")
        return

    click.echo(f"Scored strategies for scenario '{scenario_id}':")
    for strategy, score in sorted(scored, key=lambda pair: pair[1], reverse=True):
        click.echo(f"  - {strategy.name} ({strategy.type.value}): ${score:,.0f}")


@cli.command("generate-report")
@click.argument("scenario_id")
def generate_report_command(scenario_id: str) -> None:
    """Load a ClientScenario, run reasoning + scoring, and print a Markdown report."""
    try:
        report = build_full_report(scenario_id)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc

    click.echo(report)
