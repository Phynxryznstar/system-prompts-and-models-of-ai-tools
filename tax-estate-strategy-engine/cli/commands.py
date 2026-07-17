"""CLI command definitions for interacting with the strategy engine."""

from __future__ import annotations

import click

from graph.seed_example_data import seed_example_data
from ingestion.scenario_ingestion import ingest_client_scenario
from reasoning.scenario_schema import load_client_scenario_from_file


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
