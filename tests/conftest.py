"""Pytest configuration file with centralized fixtures."""
from copy import deepcopy

from heimdal.client import Client
from heimdal.client_functions import (
    load_credentials,
)
from heimdal.io.deserializers.address import load_address_from_df_row
from heimdal.io.deserializers.person import load_person_from_df_row
from heimdal.io.mappers.personal_input_maps import PersonAddressInputMap
from heimdal.io.mappers.property_input_maps import AddressInputMap

import pandas as pd

import pytest


@pytest.fixture(scope="session")
def fake_people_df():
    df = pd.read_csv("tests/assets/postman_requests_data_file.csv")

    def return_df_copy():
        return df.copy()

    return return_df_copy


@pytest.fixture(scope="session")
def fake_people_person_address_input_map():
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

    def return_deepcopy():
        return deepcopy(person_address_input_map)

    return return_deepcopy


@pytest.fixture(scope="session")
def authentication_credentials():
    credentials = load_credentials()
    return credentials


@pytest.fixture(scope="function")
def test_client(authentication_credentials):
    client_id = authentication_credentials.get("client_id")
    client_secret = authentication_credentials.get("client_secret")

    def generate_test_client(service_name: str):
        return Client(
            client_id=client_id, client_secret=client_secret, service_name=service_name
        )

    return generate_test_client


@pytest.fixture(scope="function")
def generate_fake_person(fake_people_df, fake_people_person_address_input_map):
    fake_people_df = fake_people_df()
    fake_people_person_address_input_map = fake_people_person_address_input_map()
    fake_person = load_person_from_df_row(
        fake_people_df.iloc[0], fake_people_person_address_input_map
    )

    def return_deepcopy():
        return deepcopy(fake_person)

    return return_deepcopy


@pytest.fixture(scope="function")
def fake_address_input_map():
    address_map = AddressInputMap(
        address_line1="addressLine1",
        city="city",
        state="state",
        zip_code="zipCode",
    )

    def return_deepcopy():
        return deepcopy(address_map)

    return return_deepcopy


@pytest.fixture(scope="function")
def fake_address_df():
    df = pd.read_csv("tests/assets/address_sample.csv")

    def return_df_copy():
        return df.copy()

    return return_df_copy


@pytest.fixture(scope="function")
def generate_fake_address_for_property(fake_address_df, fake_address_input_map):
    fake_address_df = fake_address_df()
    fake_address_input_map = fake_address_input_map()
    fake_address = load_address_from_df_row(
        fake_address_df.iloc[0], fake_address_input_map
    )

    def return_deepcopy():
        return deepcopy(fake_address)

    return return_deepcopy
