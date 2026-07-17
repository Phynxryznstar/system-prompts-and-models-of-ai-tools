# Tax + Estate Strategy Engine

A backend engine (plus a React frontend) for modeling tax, estate, and
multi-state tax strategy using a Neo4j graph database: ingest a client
scenario, run it through a rule-based reasoning engine, score and rank
the resulting strategies, and generate a Markdown report — via the CLI,
a FastAPI backend, or the browser.

## Project structure

```
.
├── graph/        # Graph schema, Neo4j connection/query helpers, example-data seed script
├── ingestion/    # Loads a validated ClientScenario into the graph
├── reasoning/    # ClientScenario JSON schema/loader + the rule-based reasoning engine
├── scoring/      # Dollar-value scoring formulas for every strategy the reasoning engine finds
├── ranking/      # Domain weights + weighted sorting on top of scoring
├── reporting/    # Assembles a Markdown strategy report from scenario + strategy data
├── api/          # FastAPI app exposing all of the above over HTTP
├── frontend/     # React + TypeScript (Vite) app that talks to the API
├── deployment/   # Dockerfiles + docker-compose for running/deploying the whole stack
├── cli/          # Command-line interface tying every layer together
├── config/       # Configuration (Neo4j connection, API keys)
├── data/         # Sample data (e.g. example client scenarios)
├── main.py       # CLI entry point
└── requirements.txt
```

## Requirements

- Python 3.11+
- Node.js 20+ (for the frontend)
- A Neo4j database (Neo4j Aura, a self-hosted instance, or Neo4j Desktop)

## Running in Replit

1. **Create a new Repl**
   - Go to [replit.com](https://replit.com) and create a new Repl.
   - Choose the **Python** template (Python 3.11+).
   - Import this project (upload the files, or import from GitHub if the
     code is hosted in a repository).

2. **Install dependencies**
   - Replit usually detects `requirements.txt` and installs Python
     dependencies automatically. If it doesn't, open the Replit
     **Shell** tab and run:
     ```bash
     pip install -r requirements.txt
     ```
   - For the frontend, run once:
     ```bash
     cd frontend && npm install
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
   - Run from the Shell:
     ```bash
     python main.py --help
     ```
   - Typical workflow:
     ```bash
     python main.py seed-example-data
     python main.py ingest-scenario data/scenarios/scenario_001.json
     python main.py run-reasoning scenario_001
     python main.py score-strategies scenario_001
     python main.py rank-strategies scenario_001
     python main.py generate-report scenario_001
     ```
   - To serve the API: `python main.py serve-api` (http://localhost:8000).
   - To serve the frontend: `python main.py serve-frontend` (http://localhost:5173,
     opens automatically; requires the API running separately).
   - To run the whole stack (Neo4j + backend + frontend) in Docker:
     `python main.py deploy-local` — see `deployment/README_DEPLOYMENT.md`.

## Running locally

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then fill in your Neo4j credentials
python main.py --help
```

For the frontend:

```bash
cd frontend
npm install
cp .env.example .env  # points VITE_API_BASE_URL at the API, defaults to http://localhost:8000
npm run dev
```

## Status

- `graph/` — schema (node labels, relationship types, constraints/indexes),
  Neo4j connection helpers, generic query helpers, and a seed script for
  example data.
- `reasoning/` — `ClientScenario` JSON schema/loader, and a reasoning
  engine with 16 rules across tax, estate, and state strategies.
- `ingestion/` — loads a validated `ClientScenario` into the graph.
- `scoring/` — dollar-value formulas for every strategy rule, plus
  orchestration to score a whole scenario.
- `ranking/` — domain weights (tax/estate/state/combined) and a weighted
  sort on top of scoring.
- `reporting/` — Markdown templates + a builder that assembles a full
  strategy report.
- `api/` — FastAPI app (scenario + strategies routers) exposing
  ingestion, reasoning, scoring, ranking, and reporting over HTTP.
- `frontend/` — React + TypeScript + Vite + Tailwind app: ingest a
  scenario, view its ranked strategies, and read/download its report.
- `cli/` — commands for every step above, including `serve-api`,
  `serve-frontend`, and `deploy-local`.
- `config/` — Neo4j settings from environment variables; not yet
  expanded with other API keys.
- `deployment/` — Dockerfiles for the backend and frontend, a
  docker-compose stack (Neo4j + backend + frontend), and a deployment
  guide covering Render/Railway/Vercel/Docker Hub and Neo4j Aura.
