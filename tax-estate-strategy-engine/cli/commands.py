"""CLI command definitions for interacting with the strategy engine."""

from __future__ import annotations

import shutil
import subprocess
import time
import webbrowser
from pathlib import Path

import click
import uvicorn

from api.server import app as fastapi_app
from graph.seed_example_data import seed_example_data
from ingestion.scenario_ingestion import ingest_client_scenario
from ranking.engine import rank_scenario
from reasoning.engine import find_all_strategies
from reasoning.scenario_schema import load_client_scenario_from_file
from reporting.builder import build_full_report
from scoring.engine import score_scenario

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
FRONTEND_URL = "http://localhost:5173"
DEPLOYMENT_DIR = Path(__file__).resolve().parent.parent / "deployment"
BACKEND_URL = "http://localhost:8000"
NEO4J_BROWSER_URL = "http://localhost:7474"


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


@cli.command("rank-strategies")
@click.argument("scenario_id")
def rank_strategies_command(scenario_id: str) -> None:
    """Run reasoning, scoring, and ranking for a ClientScenario, then print the results."""
    try:
        ranked = rank_scenario(scenario_id)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc

    if not ranked:
        click.echo(f"No strategies found for scenario '{scenario_id}'.")
        return

    click.echo(f"Ranked strategies for scenario '{scenario_id}':")
    for strategy, raw_score, weighted_score in ranked:
        click.echo(
            f"  - {strategy.name} ({strategy.type.value}): "
            f"raw=${raw_score:,.0f} weighted=${weighted_score:,.0f}"
        )


@cli.command("serve-api")
def serve_api_command() -> None:
    """Run the FastAPI app with Uvicorn on http://localhost:8000."""
    uvicorn.run(fastapi_app, host="localhost", port=8000)


@cli.command("serve-frontend")
def serve_frontend_command() -> None:
    """Install frontend dependencies if needed, then run the Vite dev server."""
    if not (FRONTEND_DIR / "node_modules").exists():
        click.echo("Installing frontend dependencies (npm install)...")
        subprocess.run(["npm", "install"], cwd=FRONTEND_DIR, check=True)

    click.echo(f"Starting the frontend dev server at {FRONTEND_URL} ...")
    process = subprocess.Popen(["npm", "run", "dev"], cwd=FRONTEND_DIR)
    try:
        time.sleep(2)
        webbrowser.open(FRONTEND_URL)
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


def _compose_command() -> list[str]:
    """Return the available Compose invocation: standalone `docker-compose`
    if installed, otherwise the `docker compose` plugin."""
    if shutil.which("docker-compose"):
        return ["docker-compose"]
    return ["docker", "compose"]


@cli.command("deploy-local")
def deploy_local_command() -> None:
    """Check for deployment/.env, then run the full stack with docker-compose."""
    env_path = DEPLOYMENT_DIR / ".env"
    if not env_path.exists():
        raise click.ClickException(
            f"Missing {env_path}. Run:\n"
            f"  cd {DEPLOYMENT_DIR} && cp env.example .env\n"
            "then edit .env (set a real NEO4J_PASSWORD) before retrying."
        )

    click.echo("Starting local deployment (Neo4j + backend + frontend)...")
    click.echo(f"  Backend:       {BACKEND_URL}")
    click.echo(f"  Frontend:      {FRONTEND_URL}")
    click.echo(f"  Neo4j Browser: {NEO4J_BROWSER_URL}")
    click.echo()

    subprocess.run([*_compose_command(), "up", "--build"], cwd=DEPLOYMENT_DIR, check=True)
