from typing import Callable

from dashboard_supplements.entities.services import personal_service_category
from dashboard_supplements.aesthetics.aesthetics import (
    camel_case_to_split_title,
    clean_and_capitalize_string_input,
    clean_raw_json,
    denest_dict,
    divide_name,
    formatted_address_string_from_df_row,
)
from dashboard_supplements.dashboard_components.dashboard_helper_functions import (
    generate_selection,
    match_name_to_row,
)
from dashboard_supplements.io.deserializers.person import (
    load_person_from_first_and_last_name,
)
from dashboard_supplements.io.mock_responses import load_fake_response_df
from dashboard_supplements.io.request_handlers.mock_requests import mock_personal_query


def test_load_person_from_first_and_last_name(
    fake_people_df: Callable, fake_people_person_address_input_map: Callable
) -> None:
    fake_people_df_instance = fake_people_df()
    fake_people_person_address_input_map_instance = (
        fake_people_person_address_input_map()
    )

    first_name = "Carissa"
    last_name = "Sharma"

    person = load_person_from_first_and_last_name(
        df=fake_people_df_instance,
        input_map=fake_people_person_address_input_map_instance,
        first_name=first_name,
        last_name=last_name,
    )
    assert person is not None


def test_mock_personal_query_for_pfr(generate_fake_person: Callable) -> None:
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="PFR")

    assert response.get("status") == "Success"
    assert response is not None


def test_mock_personal_query_for_life_events(generate_fake_person: Callable) -> None:
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="LifeEvents")

    assert response.get("status") == "SUCCESS"
    assert response is not None


def test_mock_personal_query_for_auto_prefill(generate_fake_person: Callable) -> None:
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="AutoPrefill")

    assert response.get("status") == "Success"
    assert response is not None


def test_match_name_to_row(fake_people_df: Callable) -> None:
    sample_df = fake_people_df()
    name_to_match = "Jenny Everywhere"
    expected_row = sample_df.iloc[0]

    target_row = match_name_to_row(name=name_to_match, sample_personas_df=sample_df)

    assert target_row.equals(expected_row)


def test_generate_persona_selection() -> None:
    persona_name_list = ["Jane Doe", "John Doe", "Jack Donovan", "Julie Dunham"]
    expected_response = "---"

    persona_selection = generate_selection(
        input_list=persona_name_list, service_category=personal_service_category
    )
    assert persona_selection == expected_response


def test_formatted_address_string_from_df_row(fake_people_df: Callable) -> None:
    df_row = fake_people_df().iloc[0]
    expected_output = "63724 Ramsey Way, Dallas, TX 75246"

    formatted_string = formatted_address_string_from_df_row(row=df_row)
    assert formatted_string == expected_output


def test_load_fake_response_df() -> None:

    path = "./dashboard_supplements/assets/sample_results/sample_pfr_results.csv"

    fake_response_df = load_fake_response_df(path=path)

    assert len(fake_response_df) > 5
    assert fake_response_df is not None


def test_camel_case_to_split_title() -> None:
    input_strings = ["dirtyInput", "messyString", "fixMePlease intoANewString"]

    expected_output = ["Dirty Input", "Messy String", "Fix Me Please Into A New String"]

    for input_string, result in zip(input_strings, expected_output):
        output_string = camel_case_to_split_title(string=input_string)
        assert output_string == result


def test_clean_and_capitalize_string_input() -> None:
    input_strings = [" jenny \n", "everywhere  ", "1011 somewhere way \n "]

    expected_output = ["Jenny", "Everywhere", "1011 Somewhere Way"]

    for input_string, result in zip(input_strings, expected_output):
        output_string = clean_and_capitalize_string_input(string=input_string)
        assert output_string == result


def test_divide_name() -> None:
    name = "Jenny Everywhere"
    expected_response = ("Jenny", "Everywhere")

    result = divide_name(name=name)
    assert expected_response == result


def test_denest_dict() -> None:
    nested_dict = {
        "dict": "value",
        "dictA_key1": "value_1",
        "dictB_key1": "value_2",
        "dictB_key2_key3": "value_3",
    }
    expected_result = {
        "dict": "value",
        "dictA": {"key1": "value_1"},
        "dictB": {"key1": "value_2", "key2": {"key3": "value_3"}},
    }

    result = denest_dict(nested_dict)
    assert expected_result == result


def test_clean_raw_json() -> None:
    pass
