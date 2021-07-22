"""Life Events API page for Life Events Demo."""
from copy import deepcopy

from dasboard_pages.api_request_pages import mock_response_page

from dashboard_supplements.aesthetics.formatting import (
    initialize_logo_and_title,
    remove_index_from_df,
)
from dashboard_supplements.dashboard_helper_functions import (
    generate_df_from_life_event,
    generate_sidebar_selection,
)
from dashboard_supplements.demo_text.demo_dashboard_text import event_names
from dashboard_supplements.entities.services import service_category_mapper
from dashboard_supplements.io.deserializers.person import (
    load_person_from_name,
)
from dashboard_supplements.io.mock_responses import FAKE_LIFE_EVENT_RESPONSE_DF
from dashboard_supplements.io.serializers.shared import generate_list_of_names_from_df

import streamlit as st

import pandas as pd

def app(title: str, service_name: str) -> None:
    """Display sample personas for Life Events API Demo."""
    initialize_logo_and_title(title)

    event_names_list = deepcopy(event_names)
    event_names_list.insert(0, "---")
    life_event_df = FAKE_LIFE_EVENT_RESPONSE_DF
    cleaned_display_df = life_event_df.rename(
        columns={
            "requestBody.person.firstName": "First Name",
            "requestBody.person.lastName": "Last Name",
            "requestBody.person.dateOfBirth": "Date of Birth",
            "requestBody.address.zipCode": "Zip Code",
            "requestBody.address.state": "State",
        }
    )
    cleaned_display_df.drop_duplicates(subset=["First Name", "Last Name"], inplace=True)
    columns_to_display = [
        "First Name",
        "Last Name",
        "Date of Birth",
        "Zip Code",
        "State",
    ]

    life_event = st.sidebar.selectbox(
        "Select A Life Event",
        event_names_list,
    )

    if life_event == "---":
        st.write(
            "Every month, approximately 5% of your policy holders will "
            "experience a significant life event. We provide instant insight "
            "on nine key life events. Explore each one via the panel on the left."
        )
        st.subheader("Sample Book of Business")

        display_df_without_index = remove_index_from_df(cleaned_display_df[columns_to_display])
        display_df_without_index.rename(columns={"Last Name": "Name"}, inplace=True)
        st.table(display_df_without_index)

    elif life_event != "---":
        event_monitor_df = generate_df_from_life_event(
            df=cleaned_display_df,
            life_event_name=life_event,
            show_cols=columns_to_display,
        )

        life_event_persona_names = generate_list_of_names_from_df(
            df=event_monitor_df, fname_col="First Name", lname_col="Last Name"
        )

        service_category = service_category_mapper[service_name]

        name_selection = generate_sidebar_selection(
            input_list=life_event_persona_names,
            service_category=service_category,
        )

        if name_selection == "---":
            st.subheader("Select a persona on the sidebar to query life events")
            st.table(event_monitor_df)
        elif name_selection != "---":
            person = load_person_from_name(
                name=name_selection,
            )
            mock_response_page.app(
                query_entity=person,
                service_name=service_name,
                service_category=service_category,
            )
