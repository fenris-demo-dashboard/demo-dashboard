from demo_supplements.dashboard_components.dashboard_helper_functions import (
    match_name_to_row,
)
from demo_supplements.io.fake_request_data import (
    FAKE_PEOPLE_DF,
    FAKE_PERSON_ADDRESS_INPUT_MAP,
)

from heimdal.io.deserializers.person import load_person_from_df_row
from heimdal.io.mappers.personal_input_maps import PersonAddressInputMap


import pandas as pd


def load_person_from_first_and_last_name(
    first_name: str,
    last_name: str,
    df: pd.DataFrame = FAKE_PEOPLE_DF,
    input_map: PersonAddressInputMap = FAKE_PERSON_ADDRESS_INPUT_MAP,
):
    """Create a Person object and Address object given a selected persona."""
    matched_row = match_name_to_row(
        name=" ".join([first_name, last_name]), sample_personas_df=df
    )
    person = load_person_from_df_row(matched_row, input_map)

    return person
