"""Personal API page for Streamlit Demo App."""
from pathlib import Path

from dasboard_pages.api_request_pages import mock_response_page

from dashboard_supplements.aesthetics.aesthetics import (
    divide_name,
    initialize_logo_and_title,
)
from dashboard_supplements.dashboard_components.dashboard_helper_functions import (
    generate_image_dashboard,
    generate_selection,
)
from dashboard_supplements.entities.services import (
    service_category_mapper
)
from dashboard_supplements.io.deserializers.person import (
    load_person_from_first_and_last_name,
)

import streamlit as st


def app(title: str, service_name: str) -> None:
    """Display sample personas for PFR API Demo."""
    initialize_logo_and_title(title)

    service_category = service_category_mapper.get(service_name)
    sample_information = service_category.sample_information

    query_selection = generate_selection(
        input_list=sample_information,
        service_category=service_category,
    )

    if query_selection == "---":
        st.subheader(f"Select a {service_category.prompt}: ")
        image_base_path = Path("./dashboard_supplements/assets/")

        generate_image_dashboard(
            rows=2,
            columns=3,
            persona_names=sample_information,
            img_path=image_base_path / service_category.image_path,
            caption="address",
        )

    elif query_selection != "---":
        first_name, last_name = divide_name(query_selection)
        person = load_person_from_first_and_last_name(
            first_name=first_name,
            last_name=last_name,
        )
        mock_response_page.app(person=person, service_name=service_name)
