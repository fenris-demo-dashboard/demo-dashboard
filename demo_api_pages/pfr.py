"""Scoring API page for PFR Demo."""
from pathlib import Path

from demo_api_pages.api_request_pages import pfr_request

from demo_supplements.aesthetics.aesthetics import (
    divide_name,
    initialize_logo_and_title,
)
from demo_supplements.dashboard_components.dashboard_helper_functions import (
    generate_image_dashboard,
    generate_persona_selection,
)
from demo_supplements.demo_text.demo_dashboard_text import sample_persona_names
from demo_supplements.io.deserializers.person import (
    load_person_from_first_and_last_name,
)
from demo_supplements.io.request_handlers.auth import use_mock_or_api_pull

import streamlit as st


def app():
    """Display sample personas for PFR API Demo."""
    initialize_logo_and_title("PFR")

    name_selection = generate_persona_selection(sample_persona_names)
    use_mocks = use_mock_or_api_pull()

    if name_selection == "---":
        st.subheader("Select a persona whom you would like to score:")
        image_base_path = Path("./demo_supplements/assets/demo_persona_photos/")

        generate_image_dashboard(
            rows=2,
            columns=3,
            persona_names=sample_persona_names,
            img_path=image_base_path,
            caption="address",
        )

    elif name_selection != "---":
        first_name, last_name = divide_name(name_selection)
        person = load_person_from_first_and_last_name(
            first_name=first_name,
            last_name=last_name,
        )
        pfr_request.app(person=person, should_use_mocks=use_mocks)
