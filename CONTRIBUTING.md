# Contributing

## First-time setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
2. `uv sync` — creates `.venv` with exact versions from `uv.lock`.
3. `cp .env.example .env` and fill in your own values. `.env` is gitignored
   and never committed — each collaborator keeps their own copy.
4. `uv run dagster dev` to confirm the local UI comes up at
   http://localhost:3000.

## Adding dependencies

Use `uv add <package>` (or `uv add --dev <package>` for tooling only). This
updates `pyproject.toml` and `uv.lock` together — commit both so everyone's
environment stays identical.

## Branches and PRs

- Branch off `main`: `feature/<short-description>` or `fix/<short-description>`.
- Open a PR into `main`; CI (ruff, mypy, pytest) must pass before merging.
- Keep PRs scoped to one asset/resource/change where possible — with 2-3
  people touching `src/data_pipeline/assets/` concurrently, smaller PRs
  avoid merge conflicts.

## Secrets

- Never commit real values to `.env.example` — placeholders/blank only.
- Read secrets in code via Dagster's `EnvVar("NAME")` (see
  `src/data_pipeline/resources/__init__.py`), not `os.environ` directly.
- Shared staging/production secrets are injected as real environment
  variables at deploy time, not stored in the repo.
