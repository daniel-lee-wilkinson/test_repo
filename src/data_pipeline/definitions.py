import dagster as dg

from data_pipeline.assets import all_assets
from data_pipeline.jobs import all_jobs, all_schedules, all_sensors
from data_pipeline.resources import all_resources

defs = dg.Definitions(
    assets=all_assets,
    resources=all_resources,
    jobs=all_jobs,
    schedules=all_schedules,
    sensors=all_sensors,
)
