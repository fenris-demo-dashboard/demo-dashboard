"""Life events request page."""
from demo_supplements.aesthetics.aesthetics import (
    camel_case_to_split_title,
    clean_raw_json,
    format_auto_prefill_response,
    format_life_events_response,
    format_pfr_response,
)
from demo_supplements.demo_text.api_field_descriptions import pfr_field_info
from demo_supplements.io.request_handlers.mock_requests import mock_personal_query

from heimdal.entities.person import Person

import streamlit as st


def app(person: Person, service_name: str):

    try:
        response = mock_personal_query(person=person, service_name=service_name)
    except Exception:
        response = {"error": Exception}

    page_title = camel_case_to_split_title(service_name)
    st.subheader(
        f"{page_title} API Response for " 
        f"{person.first_name} {person.last_name}"
    )

    if st.sidebar.checkbox(label="Raw JSON Data"):
        components_to_remove_from_response = [
            "requestId",
            "submissionId",
            "message"
            "status",
            "modelVersion",
        ]
        cleaned_response = clean_raw_json(response, components_to_remove_from_response)
        st.write(cleaned_response)
    else:
        if service_name == "LifeEvents":
            format_life_events_response(response=response)
        elif service_name == "PFR":
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
        elif service_name == "AutoPrefill":
            format_auto_prefill_response(response=response)
