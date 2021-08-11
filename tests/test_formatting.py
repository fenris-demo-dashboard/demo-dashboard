from typing import Callable

from dashboard_supplements.aesthetics.formatting import (
    camel_case_to_split_title,
    clean_and_capitalize_string_input,
    clean_raw_json,
    nest_dict,
    formatted_address_string_from_df_row,
)
from dashboard_supplements.dashboard_helper_functions import generate_sidebar_selection
from dashboard_supplements.entities.services import personal_service_category


def test_generate_sidebar_selection() -> None:
    persona_name_list = ["Jane Doe", "John Doe", "Jack Donovan", "Julie Dunham"]
    expected_response = "---"

    persona_selection = generate_sidebar_selection(
        default_selection="---",
        input_list=persona_name_list,
        service_category=personal_service_category,
    )
    assert persona_selection == expected_response


def test_formatted_address_string_from_df_row(fake_people_df: Callable) -> None:
    df_row = fake_people_df().iloc[0]
    expected_output = "63724 Ramsey Way, Dallas, TX 75246"

    formatted_string = formatted_address_string_from_df_row(row=df_row)
    assert formatted_string == expected_output


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

    result = nest_dict(nested_dict)
    assert expected_result == result


def test_clean_raw_json() -> None:
    unclean_json = {
        "requestId": "to be removed",
        "item1": "shall remain unnested",
        "nest1.layer1": "shall be nested",
        "nest1.layer2.part1": "shall be nested deeper",
        "nest1.layer2.part2": "part 2",
    }
    expected_clean_json = {
        "item1": "shall remain unnested",
        "nest1": {
            "layer1": "shall be nested",
            "layer2": {"part1": "shall be nested deeper", "part2": "part 2"},
        },
    }
    real_clean_json = clean_raw_json(unclean_json)

    assert expected_clean_json == real_clean_json
