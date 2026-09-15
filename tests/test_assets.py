import dagster as dg

from data_pipeline.assets import example_asset


def test_example_asset_materializes() -> None:
    result = dg.materialize([example_asset])
    assert result.success
