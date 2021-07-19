"""Life events request page."""
from dashboard_supplements.aesthetics.formatting import (
    camel_case_to_split_title,
    clean_raw_json,
    format_response_by_service,
)
from dashboard_supplements.entities.services import ServiceCategory

import streamlit as st


def app(
    query_entity: object, service_name: str, service_category: ServiceCategory
) -> None:
    """Display response for a mock personal query."""
    try:
        response = service_category.mock_query_func(query_entity, service_name)
    except Exception:
        response = {"error": Exception}

    st.subheader(f"{camel_case_to_split_title(service_name)} API Response")

    if st.sidebar.checkbox(label="Raw JSON Data"):
        cleaned_response = clean_raw_json(response)
        st.write(cleaned_response)
    else:
        format_response_by_service(service_name=service_name, response=response)
