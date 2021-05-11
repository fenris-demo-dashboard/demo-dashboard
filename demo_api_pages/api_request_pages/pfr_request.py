"""PFR request page."""
from demo_supplements.aesthetics.aesthetics import clean_raw_json, format_pfr_response
from demo_supplements.demo_text.api_field_descriptions import pfr_field_info
from demo_supplements.io.request_handlers.live_requests import live_query
from demo_supplements.io.request_handlers.mock_requests import mock_personal_query

from heimdal.entities.person import Person

import streamlit as st


def app(person: Person, should_use_mocks: bool):
    """Mock request to teh PFR API."""
    try:
        if should_use_mocks:
            response = mock_personal_query(person=person, service_name="PFR")
        elif not should_use_mocks:
            response = live_query(input_object=person, service_name="PFR")
        else:
            response = {"error": "no response found"}
    except Exception:
        response = {"error": Exception}

    st.subheader(f"Scoring API Response for " f"{person.first_name} {person.last_name}")

    if st.sidebar.checkbox(label="Raw JSON Data"):
        components_to_remove_from_response = [
            "message",
            "requestId",
            "submissionId",
            "status",
            "modelVersion",
        ]
        cleaned_response = clean_raw_json(response, components_to_remove_from_response)
        st.write(cleaned_response)
    else:
        format_pfr_response(
            response=response,
            targets=[
                "trend",
                "creditLevel",
                "insuranceTier",
                "financeTier",
                "decile",
            ],
            field_info=pfr_field_info,
        )
