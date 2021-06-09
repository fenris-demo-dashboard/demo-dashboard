import json
from typing import Any, Dict

from demo_supplements.aesthetics.aesthetics import spinner_decorator_factory
from demo_supplements.io.mock_responses import api_to_fake_response_df_mapper

from heimdal.entities.address import Address
from heimdal.entities.person import Person


@spinner_decorator_factory(spinner_text="Fetching API Response...")
def mock_personal_query(
    person: Person,
    service_name: str,
) -> Dict[str, Any]:
    """
    Fetch data from mock response based on first, last, and service name.
    """
    fake_data_df = api_to_fake_response_df_mapper.get(service_name)

    first_name = person.first_name.strip()
    last_name = person.last_name.strip()

    name_match_condition = (fake_data_df["first_name"].str.strip() == first_name) & (
        fake_data_df["last_name"].str.strip() == last_name
    )
    persona_row_match = fake_data_df.loc[name_match_condition].iloc[0]
    response_json = json.loads(persona_row_match.to_json())
    return response_json


def mock_property_query(
    address: Address,
    service_name: str,
) -> Dict[str, Any]:
    """
    Fetch data from mock response based on first, last, and service name.
    """
    fake_data_df = api_to_fake_response_df_mapper.get(service_name)

    address_line1 = address.address_line1.strip()
    zip_code = address.zip_code.strip()

    address_match_condition = (
        fake_data_df["addressLine1"].str.strip() == address_line1
    ) & (fake_data_df["zipCode"].str.strip() == zip_code)
    address_row_match = fake_data_df.loc[address_match_condition].iloc[0]
    response_json = json.loads(address_row_match.to_json())
    return response_json
