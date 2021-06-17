"""Pytest configuration file with centralized fixtures."""
from copy import deepcopy
from typing import Callable, Dict

from heimdal.client import Client
from heimdal.client_functions import (
    load_credentials,
)
from heimdal.entities.address import Address
from heimdal.entities.business import Business
from heimdal.entities.person import Person
from heimdal.io.deserializers.address import load_address_from_df_row
from heimdal.io.deserializers.business import load_business_from_df_row
from heimdal.io.deserializers.person import load_person_from_df_row
from heimdal.io.mappers.business_input_maps import BusinessAddressInputMap
from heimdal.io.mappers.personal_input_maps import PersonAddressInputMap
from heimdal.io.mappers.property_input_maps import AddressInputMap

import pandas as pd

import pytest


@pytest.fixture(scope="session")
def fake_people_df() -> Callable[..., pd.DataFrame]:
    df = pd.read_csv("tests/assets/postman_requests_data_file.csv")

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


@pytest.fixture(scope="session")
def authentication_credentials() -> Dict[str, str]:
    try:
        credentials = load_credentials()
        return dict(credentials)
    except RuntimeError as error:
        raise error


@pytest.fixture(scope="function")
def test_client(authentication_credentials: dict) -> Callable[[str], Client]:
    client_id = authentication_credentials.get("client_id")
    client_secret = authentication_credentials.get("client_secret")

    def generate_test_client(service_name: str) -> Client:
        return Client(
            client_id=client_id, client_secret=client_secret, service_name=service_name
        )

    return generate_test_client


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
    df = pd.read_csv("tests/assets/postman_requests_data_file.csv", index_col=0)

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
    df = pd.read_csv("tests/assets/smb_data.csv")
    df["names"] = df["names"].apply(eval)

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
