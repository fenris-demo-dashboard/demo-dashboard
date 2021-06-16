from demo_supplements.exceptions import InvalidClientCredentialsException

from heimdal.client import Client

import streamlit as st


def initialize_demo_client(service_name: str) -> Client:
    """Load credentials and return a Client for Heimdal API access."""
    try:
        client_id = st.secrets["STREAMLIT_FENRIS_CLIENT_ID"]
        client_secret = st.secrets["STREAMLIT_FENRIS_CLIENT_SECRET"]
        client = Client(
            client_id=client_id,
            client_secret=client_secret,
            service_name=service_name,
            production_environment="uat",
        )
        return client
    except Exception:
        raise InvalidClientCredentialsException(
            "Invalid client credentials. "
            "Specify authorized credentials in a central config file"
        )
