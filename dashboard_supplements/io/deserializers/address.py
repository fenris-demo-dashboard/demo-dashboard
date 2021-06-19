"""Address deserializer file."""
from dashboard_supplements.entities.address import Address, AddressSchema
from dashboard_supplements.entities.mappers import AddressInputMap

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
