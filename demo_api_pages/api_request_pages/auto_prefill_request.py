"""Pre-Fill request page."""

from demo_supplements.aesthetics.aesthetics import (
    clean_raw_json,
    format_auto_prefill_response,
)
from demo_supplements.io.request_handlers.mock_requests import mock_personal_query

from heimdal.entities.person import Person

import streamlit as st


def app(person: Person):
    """Mock a request to the Auto Insurance Prefill API."""
    try:
        response = mock_personal_query(person=person, service_name="AutoPrefill")
    except Exception:
        response = {"error": Exception}

    st.subheader(
        f"Auto Prefill API Response for " f"{person.first_name} {person.last_name}"
    )

    if st.sidebar.checkbox("Raw JSON Data"):
        components_to_remove_from_response = [
            "requestId",
            "submissionId",
            "status",
            "modelVersion",
        ]
        cleaned_response = clean_raw_json(response, components_to_remove_from_response)
        st.write(cleaned_response)
    else:
        format_auto_prefill_response(response)
