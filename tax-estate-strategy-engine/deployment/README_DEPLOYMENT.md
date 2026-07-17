# Deployment Guide

This folder packages the Tax + Estate Strategy Engine (Neo4j + FastAPI
backend + React frontend) as three independent Docker containers,
orchestrated locally with Docker Compose, and deployable individually to
Render, Railway, Vercel, or any Docker-Hub-based host.

```
deployment/
├── Dockerfile.backend      # FastAPI + Uvicorn production image
├── Dockerfile.frontend     # React + Vite production image
├── docker-compose.yml      # neo4j + backend + frontend, wired together
├── env.example             # Template for deployment/.env
└── README_DEPLOYMENT.md    # This file
```

## 1. Run it locally with Docker Compose

**Prerequisites:** Docker and Docker Compose installed.

1. Copy the environment template and fill in a real password:

   ```bash
   cd deployment
   cp env.example .env
   # edit .env and set NEO4J_PASSWORD to something real
   ```

2. Build and start everything:

   ```bash
   docker-compose up --build
   ```

   If your Docker install only has the newer Compose plugin (no
   standalone `docker-compose` binary — common on recent Docker Desktop
   and Engine installs), use `docker compose` (two words) instead; both
   read the same `docker-compose.yml`. `python main.py deploy-local`
   (see below) detects which one you have automatically.

   The first run builds the backend and frontend images and pulls the
   `neo4j:5` image, which takes a few minutes. Subsequent runs are much
   faster (Docker caches layers). Add `-d` to run in the background.

3. Once the containers are up (the backend waits for Neo4j's healthcheck
   to pass before starting), open:

   | Service            | URL                          |
   | ------------------ | ----------------------------- |
   | Backend (FastAPI)  | http://localhost:8000         |
   | Backend docs       | http://localhost:8000/docs    |
   | Frontend           | http://localhost:5173         |
   | Neo4j Browser      | http://localhost:7474         |

   Log into Neo4j Browser with the username/password from your `.env`
   (default username `neo4j`).

4. Seed the graph and try the CLI against the containerized Neo4j from
   your host (it reads the same `.env` conventions — see the main
   project README for the full command list):

   ```bash
   cd ..
   NEO4J_URI=bolt://localhost:7687 NEO4J_USERNAME=neo4j NEO4J_PASSWORD=<your_password> \
     python main.py seed-example-data
   ```

5. Stop everything with `docker-compose down` (add `-v` to also delete
   the Neo4j data volume).

### Shortcut: `python main.py deploy-local`

From the project root (`tax-estate-strategy-engine/`), `python main.py
deploy-local` wraps steps 2–3 above: it checks that `deployment/.env`
exists (and tells you exactly how to create it if not), prints the three
URLs, and runs `docker-compose up --build` (or `docker compose`,
whichever is installed) for you.

### Why `NEO4J_USER` becomes `NEO4J_USERNAME`

`env.example` uses `NEO4J_USER` because that's the common convention for
a `.env` file. Internally, `docker-compose.yml` maps it to whatever each
piece actually expects: `NEO4J_AUTH=<user>/<password>` for the official
Neo4j image, and `NEO4J_USERNAME=<user>` for the backend (which reads
`NEO4J_USERNAME` via `config/settings.py`). You don't need to do anything
for this — it's just worth knowing if you go looking for `NEO4J_USER` in
the Python code and don't find it.

## 2. Deploying to the cloud

The three services are independent — you don't have to deploy them
together or even to the same provider.

### Backend → Render

1. Push this repository to GitHub (or connect Render to your existing
   remote).
2. In Render, create a **New Web Service**, point it at the repo, and
   set:
   - **Root directory:** `tax-estate-strategy-engine`
   - **Dockerfile path:** `deployment/Dockerfile.backend`
   - **Docker build context:** `.` (the root directory above)
3. Add environment variables (Render → your service → **Environment**):
   `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE`
   (point these at Neo4j Aura — see below — or another reachable Neo4j
   instance; Render can't reach a `neo4j` container defined in your local
   `docker-compose.yml`).
4. Render detects `EXPOSE 8000` and the `CMD`; no extra start command is
   needed. Your API is live at the `.onrender.com` URL Render assigns.

### Backend + Neo4j → Railway

1. In Railway, create a new project and **Deploy from GitHub repo**.
2. Add a service for the backend using `deployment/Dockerfile.backend`
   (root directory `tax-estate-strategy-engine`, same as Render above).
3. For the database, either:
   - Add Neo4j Aura Free (see below) and just set env vars on the
     backend service, or
   - Deploy Neo4j as its own Railway service from the `neo4j:5` Docker
     image, then set `NEO4J_URI=bolt://<railway-neo4j-service>:7687`
     using Railway's internal networking/service DNS.
4. Set `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE`
   as Railway environment variables on the backend service.
5. Railway assigns a public URL and handles the port mapping from
   `EXPOSE 8000` automatically.

### Frontend → Vercel

Vercel builds static Vite output directly — you don't need
`Dockerfile.frontend` there.

1. In Vercel, **Import Project** from your repo.
2. Set:
   - **Root directory:** `tax-estate-strategy-engine/frontend`
   - **Build command:** `npm run build`
   - **Output directory:** `dist`
3. Add an environment variable **`VITE_API_BASE_URL`** set to your
   deployed backend's URL (e.g. the Render/Railway URL from above).
   Vite inlines this at build time, so set it *before* triggering a
   build/deploy, and redeploy whenever the backend URL changes.
4. Vercel builds and serves the frontend on its own domain; no server
   process (and no `vite preview`) is needed in this path.

### Docker Hub (any provider)

To run the same images anywhere Docker is supported (a VM, Kubernetes,
Fly.io, etc.), build and push them yourself:

```bash
# from tax-estate-strategy-engine/
docker build -t <your-dockerhub-username>/tax-estate-backend:latest \
  -f deployment/Dockerfile.backend .
docker push <your-dockerhub-username>/tax-estate-backend:latest

docker build -t <your-dockerhub-username>/tax-estate-frontend:latest \
  -f deployment/Dockerfile.frontend \
  --build-arg VITE_API_BASE_URL=https://your-backend-domain.example \
  .
docker push <your-dockerhub-username>/tax-estate-frontend:latest
```

Then on your target host/orchestrator, pull both images and run them
with the same environment variables described above (`NEO4J_URI`,
`NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE` for the backend;
`VITE_API_BASE_URL` as a *build* arg, already baked into the frontend
image by the time you pull it).

## 3. Configuring environment variables in production

- **Never commit `.env`** — it's git-ignored; `env.example` is the
  template that ships in version control.
- Set real secrets (`NEO4J_PASSWORD` especially) through your host's
  secret/environment variable manager (Render/Railway's Environment tab,
  Vercel's Environment Variables page, Kubernetes Secrets, etc.), not in
  the Dockerfile or docker-compose.yml.
- The backend fails fast with a clear error (`config/settings.py`) if
  `NEO4J_URI`, `NEO4J_USERNAME`, or `NEO4J_PASSWORD` are missing at
  startup — check your platform's logs first if the container won't
  come up.
- Remember `VITE_API_BASE_URL` is a **build-time** value for the
  frontend, not a runtime one. Changing it means rebuilding the frontend
  image (or re-triggering a Vercel build), not just restarting a
  container.
- If you expose the frontend on a real domain, tighten CORS in
  `api/server.py` (currently `allow_origins=["*"]` for local development)
  to that domain specifically.

## 4. Scaling the backend

The backend is stateless (all state lives in Neo4j), so it scales
horizontally without any code changes:

- **Docker Compose:** `docker-compose up --build --scale backend=3`
  starts 3 backend containers. You'll need a load balancer (e.g. nginx,
  Traefik) in front of them, since plain Compose doesn't add one — this
  mode is mainly useful for local load testing.
- **Render:** raise the **Instance Count** on the service, or enable
  autoscaling on a paid plan.
- **Railway:** increase **Replicas** in the service settings.
- **Kubernetes/other orchestrators:** run the backend image as a
  Deployment with `replicas: N` behind a Service/Ingress.

Neo4j itself is not horizontally scaled by this setup — a single Neo4j
instance (local container or Aura) backs every backend replica. For
serious concurrent load, upgrade to a larger Aura tier or a clustered
Neo4j Enterprise deployment rather than adding more Neo4j containers.

## 5. Using Neo4j Aura instead of local Neo4j

Neo4j Aura (Neo4j's managed cloud offering, including a free tier) can
replace the `neo4j` container entirely — useful for cloud deployments
(Render/Railway can't reach a container from your local
`docker-compose.yml`) or if you'd rather not operate Neo4j yourself.

1. Create a free/paid instance at [Neo4j Aura](https://neo4j.com/cloud/aura/)
   and note the connection URI it gives you — it looks like
   `neo4j+s://<id>.databases.neo4j.io`.
2. Set these wherever the backend runs (`.env` for local Compose runs,
   or your host's environment variable settings in production):
   ```bash
   NEO4J_URI=neo4j+s://<id>.databases.neo4j.io
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=<the password Aura generated for you>
   ```
3. **Local Docker Compose with Aura:** the `backend` service still lists
   `depends_on: neo4j`, so a plain `docker-compose up` starts the local
   `neo4j` container too, even though the backend won't use it. To skip
   it entirely, start the other two services with `--no-deps`:
   ```bash
   docker-compose up --build --no-deps backend frontend
   ```
   As long as `NEO4J_URI` in your `.env` points at Aura instead of
   `bolt://neo4j:7687`, the backend connects there directly regardless
   of whether the local `neo4j` container is running.
4. Aura uses TLS (`neo4j+s://`), which the `neo4j` Python driver already
   handles automatically based on the URI scheme — no code changes
   needed.
