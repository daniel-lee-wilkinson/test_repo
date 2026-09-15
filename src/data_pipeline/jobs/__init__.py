import dagster as dg

# Schedules, sensors, and jobs beyond plain asset definitions go here.

all_jobs: list[dg.JobDefinition] = []
all_schedules: list[dg.ScheduleDefinition] = []
all_sensors: list[dg.SensorDefinition] = []
