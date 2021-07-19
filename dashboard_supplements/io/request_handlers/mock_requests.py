import json
from typing import Any, Dict

from dashboard_supplements.entities.address import Address
from dashboard_supplements.entities.business import Business
from dashboard_supplements.entities.person import Person
from dashboard_supplements.io.mock_responses import api_to_fake_response_df_mapper


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

    name_match_condition = (
        fake_data_df["requestBody.person.firstName"].str.strip() == first_name
    ) & (fake_data_df["requestBody.person.lastName"].str.strip() == last_name)
    persona_row_match = fake_data_df.loc[name_match_condition].iloc[-1]
    response_json = json.loads(persona_row_match.to_json())
    return dict(response_json)


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
        fake_data_df["requestBody.address.addressLine1"].str.strip() == address_line1
    ) & (fake_data_df["requestBody.address.zipCode"].str.strip() == zip_code)
    address_row_match = fake_data_df.loc[address_match_condition].iloc[-1]
    response_json = json.loads(address_row_match.to_json())
    return dict(response_json)


def mock_business_query(
    business: Business,
    service_name: str,
):
    """Fetch data from mock responses based on business name."""
    fake_data_df = api_to_fake_response_df_mapper.get(service_name)
    business_name = business.names[0]
    business_row_match = fake_data_df.loc[
        business_name.strip() == fake_data_df["name"].str.strip()
    ].iloc[-1]
    response_json = json.loads(business_row_match.to_json())
    return dict(response_json)
