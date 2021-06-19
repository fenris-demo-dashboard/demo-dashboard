"""Business deserializer file."""
from dashboard_supplements.io.input_to_row_matchers import match_business_to_row
from dashboard_supplements.entities.address import AddressSchema
from dashboard_supplements.entities.business import Business, BusinessSchema
from dashboard_supplements.entities.mappers import BusinessAddressInputMap
from dashboard_supplements.io.request_handlers.fake_request_data import (
    FAKE_BUSINESS_DF,
    FAKE_BUSINESS_ADDRESS_INPUT_MAP,
)

import pandas as pd

def load_business_from_df_row(
    row: pd.Series, input_map: BusinessAddressInputMap
) -> Business:
    """Use a mapper to deserialize a row from a dataframe into a business entity."""
    business_keys = BusinessSchema().load_fields.keys()
    address_keys = AddressSchema().load_fields.keys()

    input_dict = row.to_dict()
    output_dict = dict()
    for k, v in vars(input_map).items():
        try:
            output_dict[k] = input_dict[v]
        except KeyError:
            output_dict[k] = ""

    business_dict = {k: v for (k, v) in output_dict.items() if k in business_keys}
    business_dict['names'] = eval(business_dict['names'])
    address_dict = {k: v for (k, v) in output_dict.items() if k in address_keys}
    try:
        address_dict["zip_code"] = str(int(address_dict["zip_code"]))
    except ValueError:
        address_dict["zip_code"] = str(address_dict["zip_code"])

    address = AddressSchema().load(address_dict)
    business = BusinessSchema().load(business_dict)

    business.address = address
    return business


def load_business_from_name(
        name: str,
        df: pd.DataFrame = FAKE_BUSINESS_DF,
        input_map: BusinessAddressInputMap = FAKE_BUSINESS_ADDRESS_INPUT_MAP,
) -> Business:
    """Create a Person object and Address object given a selected persona."""
    matched_row = match_business_to_row(
        business=name, sample_business_df=df
    )
    matched_row['address.zipCode'] = int(matched_row['address.zipCode'])
    business = load_business_from_df_row(matched_row, input_map)

    return business