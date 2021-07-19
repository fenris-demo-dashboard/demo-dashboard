"""Pytest configuration file with centralized fixtures."""
from copy import deepcopy
from typing import Callable

from dashboard_supplements.entities.address import Address
from dashboard_supplements.entities.business import Business
from dashboard_supplements.entities.mappers import AddressInputMap
from dashboard_supplements.entities.mappers import BusinessAddressInputMap
from dashboard_supplements.entities.mappers import PersonAddressInputMap
from dashboard_supplements.entities.person import Person
from dashboard_supplements.io.deserializers.address import load_address_from_df_row
from dashboard_supplements.io.deserializers.business import load_business_from_df_row
from dashboard_supplements.io.deserializers.person import load_person_from_df_row

import pandas as pd

import pytest


@pytest.fixture(scope="session")
def fake_people_df() -> Callable[..., pd.DataFrame]:
    df = pd.read_csv(
        "./dashboard_supplements/assets/personal_requests_data_file.csv", index_col=0
    )

    def return_df_copy() -> pd.DataFrame:
        return df.copy()

    return return_df_copy


@pytest.fixture(scope="session")
def fake_people_person_address_input_map() -> Callable[..., PersonAddressInputMap]:
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

    def return_deepcopy() -> PersonAddressInputMap:
        return deepcopy(person_address_input_map)

    return return_deepcopy


@pytest.fixture(scope="function")
def generate_fake_person(
    fake_people_df: Callable,
    fake_people_person_address_input_map: Callable,
) -> Callable[..., Person]:
    fake_people_df_instance = fake_people_df()
    fake_people_person_address_input_map_instance = (
        fake_people_person_address_input_map()
    )
    fake_person = load_person_from_df_row(
        fake_people_df_instance.iloc[0], fake_people_person_address_input_map_instance
    )

    def return_deepcopy() -> Person:
        return deepcopy(fake_person)

    return return_deepcopy


@pytest.fixture(scope="function")
def fake_address_input_map() -> Callable[..., AddressInputMap]:
    address_map = AddressInputMap(
        address_line1="address.addressLine1",
        city="address.city",
        state="address.state",
        zip_code="address.zipCode",
    )

    def return_deepcopy() -> AddressInputMap:
        return deepcopy(address_map)

    return return_deepcopy


@pytest.fixture(scope="function")
def fake_address_df() -> Callable[..., pd.DataFrame]:
    df = pd.read_csv(
        "dashboard_supplements/assets/property_requests_data_file.csv", index_col=0
    )

    def return_df_copy() -> pd.DataFrame:
        return df.copy()

    return return_df_copy


@pytest.fixture(scope="function")
def generate_fake_address(
    fake_address_df: Callable, fake_address_input_map: Callable
) -> Callable[..., Address]:
    fake_address_df_instance = fake_address_df()
    fake_address_input_map_instance = fake_address_input_map()
    fake_address = load_address_from_df_row(
        fake_address_df_instance.iloc[0], fake_address_input_map_instance
    )

    def return_deepcopy() -> Address:
        return deepcopy(fake_address)

    return return_deepcopy


@pytest.fixture(scope="session")
def fake_business_df() -> Callable[..., pd.DataFrame]:
    df = pd.read_csv(
        "dashboard_supplements/assets/smb_requests_data_file.csv", index_col=0
    )
    # df["names"] = df["names"].apply(eval)

    def return_df_copy() -> pd.DataFrame:
        return df.copy()

    return return_df_copy


@pytest.fixture(scope="session")
def fake_business_address_input_map() -> Callable[..., BusinessAddressInputMap]:
    business_address_input_map = BusinessAddressInputMap(
        names="names",
        address_line1="address.addressLine1",
        city="address.city",
        state="address.state",
        zip_code="address.zipCode",
    )

    def return_deepcopy() -> BusinessAddressInputMap:
        return deepcopy(business_address_input_map)

    return return_deepcopy


@pytest.fixture(scope="function")
def generate_fake_business(
    fake_business_df: Callable, fake_business_address_input_map: Callable
) -> Callable[..., Business]:
    fake_business_df_instance = fake_business_df()
    fake_business_address_input_map_instance = fake_business_address_input_map()
    fake_business = load_business_from_df_row(
        fake_business_df_instance.iloc[1], fake_business_address_input_map_instance
    )

    def return_deepcopy() -> Business:
        return deepcopy(fake_business)

    return return_deepcopy
