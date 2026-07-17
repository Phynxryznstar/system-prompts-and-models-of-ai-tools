# Tax + Estate Strategy Engine

A backend engine for modeling tax, estate, and multi-state tax strategy
using a Neo4j graph database. This is currently a CLI-only project — no
web UI yet.

## Project structure

```
tax-estate-strategy-engine/
├── graph/        # Graph schema definitions and Neo4j connection/query utilities
├── ingestion/     # Scripts for loading client, tax, and estate data into the graph
├── reasoning/     # Reasoning engine logic for evaluating strategies
├── scoring/       # Tax, estate, and state tax scoring logic
├── cli/           # Command-line interface
├── config/        # Configuration (Neo4j connection, API keys)
├── main.py        # Entry point
└── requirements.txt
```

## Requirements

- Python 3.11+
- A Neo4j database (Neo4j Aura, a self-hosted instance, or Neo4j Desktop)

## Running in Replit

1. **Create a new Repl**
   - Go to [replit.com](https://replit.com) and create a new Repl.
   - Choose the **Python** template (Python 3.11+).
   - Import this project (upload the files, or import from GitHub if the
     code is hosted in a repository).

2. **Install dependencies**
   - Replit usually detects `requirements.txt` and installs dependencies
     automatically. If it doesn't, open the Replit **Shell** tab and run:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure environment variables (Secrets)**
   - In the Repl, open the **Secrets** tool (lock icon in the left sidebar).
   - Add the following secrets:
     - `NEO4J_URI` — e.g. `neo4j+s://<your-db-id>.databases.neo4j.io`
     - `NEO4J_USERNAME` — e.g. `neo4j`
     - `NEO4J_PASSWORD` — your database password
     - Any additional API keys required by future integrations
   - These are loaded as environment variables at runtime, so no secrets
     need to be committed to the code.

4. **Run the project**
   - Click the **Run** button, or run from the Shell:
     ```bash
     python main.py
     ```
   - This currently prints `Tax + Estate Strategy Engine` as a placeholder
     while the graph, ingestion, reasoning, scoring, and CLI modules are
     built out.

## Running locally

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # if present, then fill in your Neo4j credentials
python main.py
```

## Status

This is an early scaffold. Modules under `graph/`, `ingestion/`,
`reasoning/`, `scoring/`, `cli/`, and `config/` are stubbed out with
docstrings describing their intended responsibility, ready to be filled
in as the engine is built out.
