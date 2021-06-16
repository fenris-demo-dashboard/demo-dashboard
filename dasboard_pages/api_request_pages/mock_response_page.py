"""Life events request page."""
from dashboard_supplements.aesthetics.aesthetics import (
    camel_case_to_split_title,
    clean_raw_json,
    format_response_by_service,
)
from dashboard_supplements.entities.person import Person
from dashboard_supplements.io.request_handlers.mock_requests import mock_personal_query

import streamlit as st


def app(person: Person, service_name: str) -> None:
    """Display response for a mock personal query."""
    try:
        response = mock_personal_query(person=person, service_name=service_name)
    except Exception:
        response = {"error": Exception}

    page_title = camel_case_to_split_title(service_name)
    st.subheader(
        f"{page_title} API Response for " f"{person.first_name} {person.last_name}"
    )

    if st.sidebar.checkbox(label="Raw JSON Data"):
        components_to_remove_from_response = [
            "requestId",
            "submissionId",
            "message",
            "score",
            "status",
            "modelVersion",
            "sequenceId",
        ]
        cleaned_response = clean_raw_json(response, components_to_remove_from_response)
        st.write(cleaned_response)
    else:
        format_response_by_service(service_name=service_name, response=response)
