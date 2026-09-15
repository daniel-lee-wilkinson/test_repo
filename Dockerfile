FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Install dependencies first so this layer is cached across code changes.
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project --no-dev

COPY src/ src/
RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 4000

# Serves the Dagster code location as a gRPC server for the webserver/daemon
# to load — point Dagster's workspace.yaml at host "<container>", port 4000.
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-m", "data_pipeline.definitions"]
