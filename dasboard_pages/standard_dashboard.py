"""Standard API Dashboard page for Streamlit Demo App."""
from pathlib import Path

from dasboard_pages.api_request_pages import mock_response_page

from dashboard_supplements.aesthetics.formatting import (
    initialize_logo_and_title,
)
from dashboard_supplements.dashboard_helper_functions import (
    generate_image_dashboard,
    generate_sidebar_selection,
)
from dashboard_supplements.entities.services import service_category_mapper

import streamlit as st


def app(title: str, service_name: str) -> None:
    """Display sample personas for PFR API Demo."""
    initialize_logo_and_title(title)

    service_category = service_category_mapper[service_name]
    sample_information_list = service_category.sample_information
    label_information = service_category.display_label_mapper

    query_selection = generate_sidebar_selection(
        input_list=sample_information_list,
        service_category=service_category,
    )

    if query_selection == "---":
        st.subheader(f"Select a {service_category.prompt}: ")
        image_base_path = Path("./dashboard_supplements/assets/")

        generate_image_dashboard(
            rows=int(len(sample_information_list)/3),
            info_for_display=sample_information_list,
            img_path=image_base_path / service_category.image_path,
            display_name_mapper=label_information,
            service_category=service_category,
        )

    elif query_selection != "---":
        query_input = service_category.deserialization_process_func(query_selection)
        mock_response_page.app(
            query_entity=query_input,
            service_name=service_name,
            service_category=service_category
        )
