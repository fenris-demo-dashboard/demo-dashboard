from typing import Callable

from dashboard_supplements.entities.address import Address
from dashboard_supplements.entities.business import Business
from dashboard_supplements.entities.person import Person
from dashboard_supplements.io.deserializers.address import (
    load_address_from_df_row,
    load_address_from_string,
)
from dashboard_supplements.io.deserializers.business import (
    load_business_from_df_row,
    load_business_from_name,
)
from dashboard_supplements.io.deserializers.person import (
    load_person_from_df_row,
    load_person_from_name,
)
from dashboard_supplements.io.input_to_row_matchers import (
    match_business_to_row,
    match_person_to_row,
    match_property_to_row,
)
from dashboard_supplements.io.mock_responses import load_fake_response_df


def test_load_person_from_name(
    fake_people_df: Callable, fake_people_person_address_input_map: Callable
) -> None:
    fake_people_df_instance = fake_people_df()
    fake_people_person_address_input_map_instance = (
        fake_people_person_address_input_map()
    )

    person = load_person_from_name(
        df=fake_people_df_instance,
        input_map=fake_people_person_address_input_map_instance,
        name="Carissa Sharma",
    )
    assert person is not None
    assert isinstance(person, Person)


def test_deserialize_person_with_address_from_df_row(
    fake_people_df: Callable, fake_people_person_address_input_map: Callable
) -> None:
    fake_people_df_instance = fake_people_df()
    fake_people_person_address_input_map_instance = (
        fake_people_person_address_input_map()
    )
    row = fake_people_df_instance.iloc[0]

    person = load_person_from_df_row(row, fake_people_person_address_input_map_instance)

    assert isinstance(person, Person)


def test_match_person_to_row(fake_people_df: Callable) -> None:
    sample_df = fake_people_df()
    name_to_match = "Jenny Everywhere"
    expected_row = sample_df.iloc[0]

    target_row = match_person_to_row(name=name_to_match, sample_personas_df=sample_df)

    assert target_row.equals(expected_row)


def test_load_address_from_string(
    fake_address_df: Callable, fake_address_input_map: Callable
) -> None:
    fake_address_df_instance = fake_address_df()
    fake_address_input_map_instance = fake_address_input_map()

    fake_address = "16854 Westport Blvd, Randor, DE 19968"
    address = load_address_from_string(
        df=fake_address_df_instance,
        input_map=fake_address_input_map_instance,
        address=fake_address,
    )

    assert address is not None
    assert isinstance(address, Address)


def test_deserialize_address_from_df_row(
    fake_address_df: Callable, fake_address_input_map: Callable
) -> None:
    fake_address_df_instance = fake_address_df()
    fake_address_input_map_instance = fake_address_input_map()

    row = fake_address_df_instance.iloc[0]

    address = load_address_from_df_row(row, fake_address_input_map_instance)

    assert isinstance(address, Address)


def test_match_property_to_row(fake_address_df: Callable) -> None:
    sample_df = fake_address_df()
    address_to_match = "63724 Ramsey Way"
    expected_row = sample_df.iloc[0]

    target_row = match_property_to_row(
        address=address_to_match, sample_address_df=sample_df
    )

    assert target_row.equals(expected_row)


def test_load_business_from_name(
    fake_business_df: Callable, fake_business_address_input_map: Callable
) -> None:
    fake_business_df_instance = fake_business_df()
    fake_business_input_map_instance = fake_business_address_input_map()

    fake_business_name = "Super Smart Software"

    business = load_business_from_name(
        df=fake_business_df_instance,
        input_map=fake_business_input_map_instance,
        name=fake_business_name,
    )

    assert business is not None
    assert isinstance(business, Business)


def test_deserialize_business_from_df_row(
    fake_business_df: Callable, fake_business_address_input_map: Callable
) -> None:
    fake_business_df_instance = fake_business_df()
    fake_business_input_map_instance = fake_business_address_input_map()

    row = fake_business_df_instance.iloc[0]

    business = load_business_from_df_row(row, fake_business_input_map_instance)

    assert isinstance(business, Business)


def test_match_business_to_row(fake_business_df: Callable) -> None:
    sample_df = fake_business_df()
    business_to_match = "Super Smart Software"
    expected_row = sample_df.iloc[0]

    target_row = match_business_to_row(
        business=business_to_match, sample_business_df=sample_df
    )

    assert target_row.equals(expected_row)


def test_load_fake_response_df() -> None:
    path = "./dashboard_supplements/assets/sample_results/sample_pfr_results.csv"

    fake_response_df = load_fake_response_df(path=path)

    assert len(fake_response_df) > 5
    assert fake_response_df is not None
