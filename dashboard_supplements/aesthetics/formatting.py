import ast
import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict

from PIL import Image

from dashboard_supplements.demo_text.api_field_descriptions import pfr_field_info
from dashboard_supplements.demo_text.demo_dashboard_text import event_names
from dashboard_supplements.entities.services import service_names
from dashboard_supplements.visualizations.pfr_visualizations import (
    generate_highlight_barplot,
    indicator_distributions,
)

import pandas as pd

import streamlit as st


def initialize_logo_and_title(title: str) -> None:
    """Load demo page headers/logo."""
    logo_image_path = Path("./dashboard_supplements/assets/logos/fenris_logo.png")
    logo_image = Image.open(logo_image_path)

    col1, col2 = st.beta_columns([1, 2])
    col1.image(logo_image, use_column_width="always")
    col2.title(title)


def formatted_address_string_from_df_row(row: pd.Series) -> str:
    """Return a formatted address string from a df row."""
    address = (
        f"{row['address.addressLine1'].strip()}, "
        f"{row['address.city'].strip()}, "
        f"{row['address.state'].strip()} "
        f"{str(int(row['address.zipCode'])).strip()}"
    )

    return address


def clean_and_capitalize_string_input(string: str) -> str:
    """Capitalize string and strip of whitespace/extraneous characters."""
    input_string = string
    input_string = input_string.strip().title()
    return input_string


def format_life_events_response(response: dict) -> None:
    """Format life event json objects from mocked response."""
    life_events = str(response.get("events"))
    try:
        life_event_json = json.loads(life_events)
        st.table(pd.DataFrame(life_event_json, index=range(len(life_event_json))))
    except TypeError:
        st.table(pd.DataFrame(life_events, index=range(len(life_events))))


def clean_raw_json(response: dict) -> dict:
    """Remove extraneous key value pairs from raw dict before display."""
    # remove dicts and lists from string nesting (for mock data)
    st.write(response)
    response_copy_with_parsed_dicts = {}
    response_copy = deepcopy(response)
    for k, v in response_copy.items():
        try:
            parsed_literal = ast.literal_eval(v)
            response_copy_with_parsed_dicts[k] = parsed_literal
        except (SyntaxError, ValueError):
            response_copy_with_parsed_dicts[k] = v

    denested_response = denest_dict(dict1=response_copy_with_parsed_dicts, key=".")
    components_to_remove_from_response = [
        "requestId",
        "submissionId",
        "modelVersion",
        "sequenceId",
        "message",
        "score",
        "requestBody",
        "Unnamed: 0",
        "fenrisId",
        "event_names",
        *event_names,
    ]
    denested_response_copy = deepcopy(denested_response)
    for item in components_to_remove_from_response:
        if item in denested_response_copy.keys():
            denested_response_copy.pop(item)

    st.write(denested_response_copy)
    return denested_response_copy


def camel_case_to_split_title(string: str) -> str:
    """Split a camel case string to one with title case."""
    if string.isupper():
        return string
    else:
        start_idx = [i for i, e in enumerate(string) if e.isupper()] + [len(string)]

        start_idx = [0] + start_idx
        split_string = [string[x:y] for x, y in zip(start_idx, start_idx[1:])]
        return " ".join(x.title() for x in split_string)


def format_pfr_response(response: dict) -> None:
    """Format PFR JSON API response according to target list"""
    targets = [
        "trend",
        "creditLevel",
        "insuranceTier",
        "financeTier",
        "decile",
    ]
    client_information_dict = {k: response.get(k, "Not Found") for k in targets}

    for target_title in targets:
        title = camel_case_to_split_title(string=target_title)
        expander = st.beta_expander(
            f"{title}: {client_information_dict.get(target_title)}", expanded=True
        )

        target = pfr_field_info.get(target_title)

        if target:
            expander.write(target.explanation)

            if target_title in indicator_distributions.keys():
                target_indicator = client_information_dict.get(target_title)

                generate_highlight_barplot(
                    indicator_value=target_indicator,
                    indicator_distribution=indicator_distributions.get(target_title),
                    expander=expander,
                    x_label=title,
                )

            expander.markdown(target.caption)


def format_auto_prefill_response(response: dict) -> None:
    """Format JSON API response according to target list"""
    targets = ["primary", "drivers", "vehicles", "vehiclesEnhanced"]
    response = clean_raw_json(response)

    try:
        client_information_dict = {
            k: ast.literal_eval(response.get(k, "Not Found")) for k in targets
        }
    except (SyntaxError, ValueError):
        client_information_dict = {k: response.get(k, "Not Found") for k in targets}

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
            info_dataframe.rename(columns={0: "Values"}, inplace=True)
        else:
            info_dataframe.columns = info_dataframe.columns.map(
                camel_case_to_split_title
            )

        expander.dataframe(info_dataframe)


def generic_json_format(response: dict) -> None:
    clean_json = clean_raw_json(response)
    st.write(clean_json)


def format_property_response(response: dict) -> None:
    nested_response = denest_dict(response)
    st.json(nested_response)
    # response_table = pd.DataFrame.from_dict(nested_response, orient='index')
    # response_table.rename(columns={0: "Data Values"}, inplace=True)
    # st.table(response_table)


def format_response_by_service(service_name: str, response: dict) -> None:
    format_response_dispatch_mapper = {
        service_names.pfr: format_pfr_response,
        service_names.life_events: format_life_events_response,
        service_names.life_prefill: generic_json_format,
        service_names.auto_prefill: format_auto_prefill_response,
        service_names.property_details: format_property_response,
        service_names.property_risks: format_property_response,
        service_names.property_replacement: format_property_response,
        service_names.smb: generic_json_format,
    }
    """Format response object according to service categorization."""
    response_format_func = format_response_dispatch_mapper.get(service_name)
    if response_format_func:
        response_format_func(response)
    else:
        st.write(response)


def denest_dict(dict1: dict, key: str = "_") -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for k, v in dict1.items():

        # for each key call method split_rec which
        # will split keys to form recursively nested dictionary
        split_rec(k, v, result, key)
    return result


def split_rec(k: str, v: Any, out: dict, key: str = "_") -> None:

    # splitting keys in dict
    # calling_recursively to break items on '_'
    k, *rest = k.split(key, 1)
    if rest:
        split_rec(rest[0], v, out.setdefault(k, {}), key)
    else:
        out[k] = v
