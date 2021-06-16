from dashboard_supplements.dashboard_components.dashboard_helper_functions import (
    match_name_to_row,
)
from dashboard_supplements.entities.address import AddressSchema
from dashboard_supplements.entities.person import Person, PersonSchema
from dashboard_supplements.io.fake_request_data import (
    FAKE_PEOPLE_DF,
    FAKE_PERSON_ADDRESS_INPUT_MAP,
)
from dashboard_supplements.io.mappers.personal import PersonAddressInputMap

import pandas as pd


def load_person_from_df_row(row: pd.Series, input_map: PersonAddressInputMap) -> Person:
    """Use a mapper to deserialize a row from a dataframe into a person entity."""
    person_keys = PersonSchema().load_fields.keys()
    address_keys = AddressSchema().load_fields.keys()

    input_dict = row.to_dict()
    output_dict = dict()
    for k, v in vars(input_map).items():
        try:
            output_dict[k] = input_dict[v]
        except KeyError:
            output_dict[k] = ""

    person_dict = {k: v for (k, v) in output_dict.items() if k in person_keys}
    address_dict = {k: v for (k, v) in output_dict.items() if k in address_keys}
    try:
        address_dict["zip_code"] = str(int(address_dict["zip_code"]))
    except ValueError:
        address_dict["zip_code"] = str(address_dict["zip_code"])

    address = AddressSchema().load(address_dict)
    person = PersonSchema().load(person_dict)

    person.address = address
    return person


def load_person_from_first_and_last_name(
    first_name: str,
    last_name: str,
    df: pd.DataFrame = FAKE_PEOPLE_DF,
    input_map: PersonAddressInputMap = FAKE_PERSON_ADDRESS_INPUT_MAP,
) -> Person:
    """Create a Person object and Address object given a selected persona."""
    matched_row = match_name_to_row(
        name=" ".join([first_name, last_name]), sample_personas_df=df
    )
    person = load_person_from_df_row(matched_row, input_map)

    return person
