"""Helper functions for the Fenris Demo App."""
from copy import deepcopy
from pathlib import Path

from PIL import Image

from dashboard_supplements.aesthetics.aesthetics import (
    formatted_address_string_from_df_row,
)
from dashboard_supplements.entities.services import ServiceCategory

import pandas as pd

import streamlit as st


def generate_sidebar_selection(
    input_list: list, service_category: ServiceCategory
) -> st.selectbox:
    """Load st.selectbox for an input list."""

    selections = deepcopy(input_list)
    selections.insert(0, "---")
    streamlit_selections = st.sidebar.selectbox(
        f"Which {service_category.prompt} would you like to explore?", selections
    )
    return streamlit_selections


def generate_image_dashboard(
    rows: int,
    info_for_display: list,
    img_path: Path,
    display_name_mapper: dict,
    service_category: ServiceCategory,
) -> None:
    """Generate dashboard of images from list of identifying characteristics."""

    for row_num in range(rows):
        streamlit_cols = st.beta_columns(3)

        for col_num in range(3):

            image_index = (row_num * 3) + col_num
            query_information = info_for_display[image_index]
            label_text = display_name_mapper[query_information]
            streamlit_cols[col_num].markdown(
                f"<h4 style='text-align: center; color: #0C2E4F; "
                f"family:Roboto;'>{label_text}</h4>",
                unsafe_allow_html=True,
            )

            row_match = match_title_to_row(
                input_obj=query_information,
                service_category=service_category
            )

            load_image_from_title(
                img_path=img_path,
                title=query_information,
                caption=formatted_address_string_from_df_row(row=row_match),
                cols_object=streamlit_cols,
                col=col_num,
            )


def match_title_to_row(input_obj: str, service_category: ServiceCategory):
    row_selection_func = service_category.select_row_from_user_query_func
    row_match = row_selection_func(input_obj, service_category.sample_information_df)
    return row_match


def load_image_from_title(
    img_path: Path, title: str, caption: str, cols_object: st.beta_columns, col: int
) -> None:
    """Load image from base path with name and address label."""
    image = Image.open(img_path / f"{'_'.join(title.split(' '))}.png")
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
