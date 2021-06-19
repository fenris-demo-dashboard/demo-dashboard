from pathlib import Path

from dashboard_supplements.entities.mappers import (
    BusinessAddressInputMap,
    PersonAddressInputMap,
)

import pandas as pd


def fake_people_df() -> pd.DataFrame:
    """Load the dataframe with fake persona information."""
    sample_csv_path = Path(
        "./dashboard_supplements/assets/postman_requests_data_file.csv"
    )
    df = pd.read_csv(sample_csv_path)
    return df


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


def fake_business_df() -> pd.DataFrame:
    """Load the dataframe with fake business information."""
    sample_csv_path = Path(
        "./dashboard_supplements/assets/smb_requests_data_file.csv"
    )
    df = pd.read_csv(sample_csv_path)
    return df


def fake_business_address_input_map():
    business_address_input_map = BusinessAddressInputMap(
        names="names",
        address_line1="address.addressLine1",
        city="address.city",
        state="address.state",
        zip_code="address.zipCode",
    )
    return business_address_input_map


FAKE_PEOPLE_DF = fake_people_df()
FAKE_PERSON_ADDRESS_INPUT_MAP = fake_person_address_input_map()
FAKE_BUSINESS_DF = fake_business_df()
FAKE_BUSINESS_ADDRESS_INPUT_MAP = fake_business_address_input_map()

