import warnings
import pathlib

from google.cloud import bigquery
from tabulate import tabulate

from .core import _generate_prompt, _call_openai, _ipytohn_nice_string

warnings.filterwarnings("ignore", "Your application has authenticated using end user credentials")


TEMPLATE = pathlib.Path(__file__).parent / "prompts" / "bigquery.jinja"


def _get_table_schema(client, table_location):
    table = client.get_table(table_location)

    schema = {"name": [], "type": [], "mode": []}
    for field in table.schema:
        schema['name'].append(field.name)
        schema['type'].append(field.field_type)
        schema['mode'].append(field.mode)

    return tabulate(schema, headers='keys', tablefmt='simple_grid')


def generate(query, project, dataset):
    client = bigquery.Client(project=project)
    tables = [
        {
            "name": table_name,
            "schema": _get_table_schema(client, table_location),
            "location": table_location,
        }
        for table_name, table_location in dataset.items()
    ]

    prompt = _generate_prompt(
        template=TEMPLATE,
        user_query=query,
        tables=tables
    )

    query = _call_openai(prompt)

    df = client.query(query).to_dataframe()

    df.prompt = _ipytohn_nice_string(prompt)
    df.query = _ipytohn_nice_string(query)

    return df
