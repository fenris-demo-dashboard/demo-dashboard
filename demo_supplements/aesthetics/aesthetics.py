import ast
import json
from copy import deepcopy
from pathlib import Path

from PIL import Image

from demo_supplements.visualizations.visualizations import (
    generate_highlight_barplot,
    indicator_distributions,
)

import pandas as pd

import streamlit as st


def initialize_logo_and_title(title: str):
    """Load demo page headers/logo."""
    logo_image_path = Path("./demo_supplements/assets/logos/fenris_logo.png")
    logo_image = Image.open(logo_image_path)

    col1, col2 = st.beta_columns([1, 2])
    col1.image(logo_image, use_column_width="always")
    col2.title(title)


def formatted_address_string_from_df_row(row: pd.Series):
    """Return a formatted address string from a df row."""
    address = (
        f"{row['address.addressLine1']}, "
        f"{row['address.city']},"
        f"{row['address.state']} "
        f"{row['address.zipCode']}"
    )

    return address


def clean_and_capitalize_string_input(string: str) -> str:
    """Capitalize string and strip of whitespace/extraneous characters."""
    input_string = string
    input_string = input_string.strip().capitalize()
    return input_string


def spinner_decorator_factory(spinner_text: str) -> callable:
    """Decorate time-consuming functions with a descriptive spinner."""

    def spinner_decorator(func: callable):
        def spinner_wrapper(*args, **kwargs):
            with st.spinner(text=spinner_text):
                result = func(*args, **kwargs)
            return result

        return spinner_wrapper

    return spinner_decorator


def divide_name(name: str):
    """Divide a name by first and last, splitting on a space."""
    first_name, last_name = name.split(" ")[0], name.split(" ")[1]
    return first_name, last_name


def format_life_events_response(response: dict):
    """Format life event json objects from mocked response."""
    life_events = response.get("events")
    life_event_json = json.loads(life_events)
    st.table(pd.DataFrame(life_event_json, index=range(len(life_event_json))))


def clean_raw_json(response: dict, components_to_remove_from_response: list):
    """Remove extraneous key value pairs from raw json before display."""
    response_copy = deepcopy(response)
    for item in components_to_remove_from_response:
        if response_copy.get(item):
            response_copy.pop(item)
    response_copy_with_parsed_dicts = {}
    for k, v in response_copy.items():
        try:
            parsed_literal = ast.literal_eval(v)
            response_copy_with_parsed_dicts[k] = parsed_literal
        except (SyntaxError, ValueError):
            response_copy_with_parsed_dicts[k] = v

    return response_copy_with_parsed_dicts


def camel_case_to_split_title(string: str):

    start_idx = [i for i, e in enumerate(string) if e.isupper()] + [len(string)]

    start_idx = [0] + start_idx
    split_string = [string[x:y] for x, y in zip(start_idx, start_idx[1:])]
    return " ".join(x.title() for x in split_string)


def format_pfr_response(response: dict, targets: list, field_info: dict):
    """Format PFR JSON API response according to target list"""
    client_information_dict = {k: response.get(k, "Not Found") for k in targets}

    for target in targets:
        title = camel_case_to_split_title(target)
        expander = st.beta_expander(
            f"{title}: {client_information_dict.get(target)}", expanded=True
        )

        explanation = field_info.get(target).explanation

        if explanation:
            expander.write(explanation)

            if indicator_distributions.get(target):
                target_indicator = client_information_dict.get(target)

                generate_highlight_barplot(
                    indicator_value=target_indicator,
                    indicator_distribution=indicator_distributions.get(target),
                    expander=expander,
                    x_label=title,
                )

        caption = field_info.get(target).caption
        if caption:
            expander.markdown(caption)


def format_auto_prefill_response(response: dict):
    """Format JSON API response according to target list"""
    targets = ["primary", "drivers", "vehicles", "vehiclesEnhanced"]

    client_information_dict = {
        k: ast.literal_eval(response.get(k, "Not Found")) for k in targets
    }

    for idx, target in enumerate(targets):

        expander_title = camel_case_to_split_title(target)

        expander = st.beta_expander(f"{expander_title}")

        if isinstance(client_information_dict.get(target), dict):
            info_df = pd.json_normalize(client_information_dict.get(target))
            info_dataframe = pd.DataFrame(info_df)
        else:
            info_dataframe = pd.DataFrame(client_information_dict.get(target))

        if info_dataframe.shape[0] == 1:
            info_dataframe = info_dataframe.transpose()
            info_dataframe.index = info_dataframe.index.map(camel_case_to_split_title)
        else:
            info_dataframe.columns = info_dataframe.columns.map(
                camel_case_to_split_title
            )

        expander.dataframe(info_dataframe)
