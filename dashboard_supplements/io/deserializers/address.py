"""Address deserializer file."""
from dashboard_supplements.entities.address import Address, AddressSchema
from dashboard_supplements.entities.mappers import AddressInputMap
from dashboard_supplements.io.request_handlers.fake_request_data import (
    FAKE_ADDRESS_DF,
    FAKE_ADDRESS_INPUT_MAP,
)
from dashboard_supplements.io.input_to_row_matchers import match_property_to_row

import pandas as pd


def load_address_from_df_row(row: pd.Series, input_map: AddressInputMap) -> Address:
    """Generate address from a dataframe row given an address input map."""
    address_keys = AddressSchema().load_fields.keys()

    input_dict = row.to_dict()
    output_dict = dict()
    for k, v in vars(input_map).items():
        try:
            output_dict[k] = input_dict[v]
        except KeyError:
            output_dict[k] = ""

    address_dict = {k: v for (k, v) in output_dict.items() if k in address_keys}
    address_dict["zip_code"] = str(address_dict["zip_code"])

    address = AddressSchema().load(address_dict)

    return address


def load_address_from_string(
        address: str,
        df: pd.DataFrame = FAKE_ADDRESS_DF,
        input_map: AddressInputMap = FAKE_ADDRESS_INPUT_MAP,
) -> Address:
    """Create a Person object and Address object given a selected persona."""
    matched_row = match_property_to_row(
        address=address, sample_address_df=df
    )
    address = load_address_from_df_row(matched_row, input_map)

    return address