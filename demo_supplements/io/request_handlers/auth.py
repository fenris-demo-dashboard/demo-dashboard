from heimdal.client import Client

import streamlit as st


def initialize_demo_client(service_name) -> Client:
    """Load credentials and return a Client for Heimdal API access."""
    client_id = st.secrets["STREAMLIT_FENRIS_CLIENT_ID"]
    client_secret = st.secrets["STREAMLIT_FENRIS_CLIENT_SECRET"]
    client = Client(
        client_id=client_id, client_secret=client_secret, service_name=service_name
    )
    return client


def use_mock_or_api_pull() -> bool:
    """Determine whether to use API mocks or real calls."""
    return False
