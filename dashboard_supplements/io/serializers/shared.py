"""Shared serializers."""
from dashboard_supplements.aesthetics.formatting import (
    clean_and_capitalize_string_input,
)

import pandas as pd


def generate_list_of_names_from_df(
    df: pd.DataFrame, fname_col: str, lname_col: str
) -> list:
    """Generate a list of names from a dataframe and fname/lname cols."""
    list_of_names = list(
        df[fname_col].apply(clean_and_capitalize_string_input)
        + " "
        + df[lname_col].apply(clean_and_capitalize_string_input)
    )
    return list_of_names
