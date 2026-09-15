# data-pipeline

A Dagster-based data pipeline, managed with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv sync
cp .env.example .env   # then fill in real values
```

## Local development

Run the Dagster UI (loads `.env` automatically):

```bash
uv run dagster dev
```

Open http://localhost:3000.

## Tests / lint / types

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```

## Docker Compose

Runs a shared Dagster instance (webserver + daemon) backed by Postgres, so
the whole team sees the same run history instead of separate local DBs.

```bash
cp .env.example .env   # if you haven't already
docker compose up --build
```

Open http://localhost:3000.

## Project layout

```
src/data_pipeline/
├── definitions.py   # Dagster Definitions entry point
├── assets/          # pipeline assets
├── resources/       # IO managers / API clients / external config
└── jobs/            # schedules, sensors, jobs
tests/               # pytest suite
deployment/
└── dagster_home/    # dagster.yaml + workspace.yaml used only by docker-compose
                      # (kept out of the repo root so local `dagster dev` doesn't
                      # pick up the Postgres storage config)
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for team workflow conventions.
