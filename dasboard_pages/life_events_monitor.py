"""Life Events API page for Life Events Demo."""
from copy import deepcopy

from dasboard_pages.api_request_pages import mock_response_page

from dashboard_supplements.aesthetics.aesthetics import (
    divide_name,
    initialize_logo_and_title,
)
from dashboard_supplements.dashboard_components.dashboard_helper_functions import (
    generate_df_from_life_event,
    generate_selection,
)
from dashboard_supplements.demo_text.demo_dashboard_text import event_names
from dashboard_supplements.entities.services import service_category_mapper
from dashboard_supplements.io.deserializers.person import (
    load_person_from_first_and_last_name,
)
from dashboard_supplements.io.mock_responses import FAKE_LIFE_EVENT_RESPONSE_DF
from dashboard_supplements.io.serializers.shared import generate_list_of_names_from_df

import streamlit as st


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
        st.dataframe(cleaned_display_df[columns_to_display])

    elif life_event != "---":
        event_monitor_df = generate_df_from_life_event(
            df=cleaned_display_df,
            life_event_name=life_event,
            show_cols=columns_to_display,
        )

        life_event_persona_names = generate_list_of_names_from_df(
            df=event_monitor_df, fname_col="First Name", lname_col="Last Name"
        )

        name_selection = generate_selection(
            input_list=life_event_persona_names,
            service_category=service_category_mapper.get(service_name),
        )

        if name_selection == "---":
            st.subheader("Select a persona on the sidebar to query life events")
            st.table(event_monitor_df)
        elif name_selection != "---":
            first_name, last_name = divide_name(name_selection)
            person = load_person_from_first_and_last_name(
                first_name=first_name,
                last_name=last_name,
            )
            mock_response_page.app(person=person, service_name=service_name)
