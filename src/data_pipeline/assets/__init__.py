import dagster as dg


@dg.asset
def example_asset() -> str:
    """Placeholder asset — replace with real pipeline logic."""
    return "hello from data-pipeline"


all_assets = [example_asset]
