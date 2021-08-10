"""Importing fake request data and constructing input maps."""
from dashboard_supplements.entities.mappers import (
    AddressInputMap,
    BusinessAddressInputMap,
    PersonAddressInputMap,
)

import pandas as pd


def fake_person_address_input_map() -> PersonAddressInputMap:
    """Establish a person address input map for the fake people dataframe."""
    person_address_input_map = PersonAddressInputMap(
        first_name="person.firstName",
        middle_name="person.middleName",
        last_name="person.lastName",
        address_line1="address.addressLine1",
        city="address.city",
        state="address.state",
        zip_code="address.zipCode",
        date_of_birth="person.dateOfBirth",
    )
    return person_address_input_map


def fake_business_address_input_map() -> BusinessAddressInputMap:
    """Fake business address input map generator func."""
    business_address_input_map = BusinessAddressInputMap(
        names="names",
        address_line1="address.addressLine1",
        city="address.city",
        state="address.state",
        zip_code="address.zipCode",
    )
    return business_address_input_map


def fake_address_input_map() -> AddressInputMap:
    """Fake address input map generator func."""
    address_input_map = AddressInputMap(
        address_line1="address.addressLine1",
        city="address.city",
        state="address.state",
        zip_code="address.zipCode",
    )
    return address_input_map


def fake_df(sample_csv_path: str) -> pd.DataFrame:
    """Read and return a dataframe from a csv path."""
    output_df = pd.read_csv(sample_csv_path)
    return output_df


FAKE_BUSINESS_DF = fake_df(
    sample_csv_path="./dashboard_supplements/assets/smb_requests_data_file.csv"
)
FAKE_PEOPLE_DF = fake_df(
    sample_csv_path="./dashboard_supplements/assets/personal_requests_data_file.csv"
)
FAKE_ADDRESS_DF = fake_df(
    sample_csv_path="./dashboard_supplements/assets/property_requests_data_file.csv"
)

FAKE_PERSON_ADDRESS_INPUT_MAP = fake_person_address_input_map()
FAKE_BUSINESS_ADDRESS_INPUT_MAP = fake_business_address_input_map()
FAKE_ADDRESS_INPUT_MAP = fake_address_input_map()
