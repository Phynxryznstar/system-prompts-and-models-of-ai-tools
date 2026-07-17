"""CLI command definitions for interacting with the strategy engine."""

from __future__ import annotations

import click

from graph.seed_example_data import seed_example_data


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
