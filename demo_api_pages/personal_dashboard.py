"""Personal API page for Streamlit Demo App."""
from pathlib import Path

from demo_api_pages.api_request_pages import mock_response_page

from demo_supplements.aesthetics.aesthetics import (
    divide_name,
    initialize_logo_and_title,
)
from demo_supplements.dashboard_components.dashboard_helper_functions import (
    generate_image_dashboard,
    generate_selection,
)
from demo_supplements.demo_text.demo_dashboard_text import (
    sample_persona_names,
    sample_business_names,
    sample_property_names,
)
from demo_supplements.io.deserializers.person import (
    load_person_from_first_and_last_name,
)

import streamlit as st

service_category_mapper = {
    'PFR': "personal",
    'LifeEvents': 'personal',
    'AutoPrefill': 'personal',
    'LifePrefill': 'personal',
    'SMB': 'small business',
    'PropertyRisks': 'property',
    'PropertyDetails': 'property',
    'PropertyReplacementCost': 'property',
}

service_sample_information = {
    'property': sample_property_names,
    'small business': sample_business_names,
    'personal': sample_persona_names
}

service_prompt_mapper = {
    'property': 'Select a property:',
    'personal': 'Select a policy holder:',
    'small business': 'Select a business:'
}

service_image_paths = {
    'property': 'demo_property_photos',
    'personal': 'demo_persona_photos',
    'small business': 'demo_business_photos'
}


def app(title: str, service_name: str) -> None:
    """Display sample personas for PFR API Demo."""

    initialize_logo_and_title(title)

    service_category = service_category_mapper.get(service_name)
    sample_information = service_sample_information.get(service_category)

    query_selection = generate_selection(
        input_list=sample_information,
        service_category=service_category,
    )

    if query_selection == "---":
        st.subheader(service_prompt_mapper.get(service_category))
        image_base_path = Path("./demo_supplements/assets/")

        generate_image_dashboard(
            rows=2,
            columns=3,
            persona_names=sample_information,
            img_path=image_base_path / service_image_paths.get(service_category),
            caption="address",
        )

    elif query_selection != "---":
        first_name, last_name = divide_name(query_selection)
        person = load_person_from_first_and_last_name(
            first_name=first_name,
            last_name=last_name,
        )
        mock_response_page.app(person=person, service_name=service_name)
