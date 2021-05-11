"""Helper functions for the Fenris Demo App."""
from copy import deepcopy
from pathlib import Path

from PIL import Image

from demo_supplements.aesthetics.aesthetics import (
    divide_name,
    formatted_address_string_from_df_row,
)
from demo_supplements.demo_text.demo_dashboard_text import (
    life_event_descriptions,
)
from demo_supplements.io.fake_request_data import FAKE_PEOPLE_DF

import pandas as pd

import streamlit as st


def generate_persona_selection(persona_name_list):
    """Load st.selectbox for list of personas."""
    persona_selections = deepcopy(persona_name_list)
    persona_selections.insert(0, "---")
    persona_selections = st.sidebar.selectbox(
        "Which personality would you like to explore?", persona_selections
    )
    return persona_selections


def generate_image_dashboard(
    rows: int, columns: int, persona_names: list, img_path: Path, caption: str
):
    """Generate dashboard of persona images from list of persona names + dimensions."""
    postman_sample_df = FAKE_PEOPLE_DF

    for row_num in range(rows):
        streamlit_cols = st.beta_columns(columns)

        for col_num in range(columns):

            persona_index = (row_num * 3) + col_num
            name = persona_names[persona_index]
            # streamlit_cols[col_num].subheader(f"{name}")
            streamlit_cols[col_num].markdown(
                f"<h4 style='text-align: center; color: #0C2E4F; "
                f"family:Roboto;'>{name}</h4>",
                unsafe_allow_html=True,
            )

            persona_row_match = match_name_to_row(
                name=name, sample_personas_df=postman_sample_df
            )

            if caption == "address":
                caption_text = formatted_address_string_from_df_row(
                    row=persona_row_match
                )
            else:
                caption_text = ""

            load_image_from_name(
                img_path=img_path,
                name=name,
                caption=caption_text,
                cols_object=streamlit_cols,
                col=col_num,
            )


def match_name_to_row(name: str, sample_personas_df: pd.DataFrame):
    """Return a series (dataframe row) with address and demographic info."""
    first_name, last_name = divide_name(name)
    name_match_condition = (
        sample_personas_df["person.firstName"].str.strip() == first_name
    ) & (sample_personas_df["person.lastName"].str.strip() == last_name)
    persona_row_match = sample_personas_df.loc[name_match_condition].iloc[0]
    return persona_row_match


def load_image_from_name(
    img_path: Path, name: str, caption: str, cols_object: st.beta_columns, col: int
):
    """Load image from base path with name and address label."""
    image = Image.open(img_path / f"{'_'.join(name.split(' '))}.png")
    cols_object[col].image(image, caption=f"{caption}")


def generate_df_from_life_event(
    df: pd.DataFrame, life_event_name: str, show_cols: list
) -> pd.DataFrame:
    """Return filtered dataframe of personas with a certain life event."""
    df_copy = df.copy()
    df_return = df_copy[df_copy[life_event_name]]
    df_return = df_return[show_cols]
    df_return.reset_index(inplace=True, drop=True)
    return df_return


def load_life_event_descriptions():

    col1, col2 = st.beta_columns(2)
    move_trigger_expander = col1.beta_expander("Move Triggers", expanded=True)
    life_trigger_expander = col2.beta_expander("Life Triggers", expanded=True)

    for event, trigger_category in life_event_descriptions.items():
        expander = (
            move_trigger_expander
            if trigger_category == "move"
            else life_trigger_expander
        )
        expander.markdown(f"* {event}")
