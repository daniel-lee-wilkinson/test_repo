import dagster as dg


class ExampleAPIResource(dg.ConfigurableResource):
    """Placeholder resource showing how to pull secrets from the environment.

    Real secrets live in `.env` locally (gitignored) or in the deploy
    target's environment/secret store in production — never hardcoded here.
    """

    api_key: str = dg.EnvVar("EXAMPLE_API_KEY")


all_resources = {
    "example_api": ExampleAPIResource(),
}
