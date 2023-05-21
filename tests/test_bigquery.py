import pandas as pd

import marshall


GCP_PROJECT = "xando-1-main"


settings = dict(
    project=GCP_PROJECT,
    dataset={"Chicago Crimes": "bigquery-public-data.chicago_crime.crime"}
)


def test_min_max_data_range():

    df = marshall.bigquery(
        "What is the data range for the chicago_crimes datasets?",
        **settings,
    )

    assert df is not None


def test_day_with_higher_number_of_crimes():

    df = marshall.bigquery(
        "Find day with highest number of crimes committed",
        **settings,
    )

    assert all(pd.to_datetime(df['crime_date']) == "2003-01-01")
