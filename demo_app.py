"""Fenris API Demo App dashboard home page."""

from demo_api_pages import (
    life_events_monitor,
    personal_dashboard,
)

from demo_supplements.aesthetics.aesthetics import initialize_logo_and_title
from demo_supplements.demo_text.demo_dashboard_text import api_descriptions

import streamlit as st

icon_link = (
    "https://fenrisd.com/wp-content/uploads/2018/03/cropped-site-icon-32x32.png"
)
st.set_page_config(
    page_title="Fenris API Demo App", page_icon=icon_link, layout="wide"
)

def get_demo_pages(pages: dict) -> str:
    """Display demo pages in a sidebar streamlit select box.

    Returns selected API and list of available pages.
    """
    api_selection_options = list(pages.keys())
    api_selection_options.insert(0, "---")
    st.sidebar.title("Control Panel")
    api_selection = st.sidebar.selectbox("Select Capability", api_selection_options)
    return str(api_selection)


def sidebar_api_selection(api_selection: str, pages: dict) -> None:
    """Generate sidebar dropdown sidebar API selection."""
    endpoint_mapper = {
        "PFR API": "PFR",
        "Recent Life Events API": "LifeEvents",
        "Life Events Monitor": "LifeEvents",
        "Auto Insurance Prefill API": "AutoPrefill",
    }

    if api_selection != "---":
        selected_page = pages[api_selection]
        selected_page.app(
            title=api_selection,
            service_name=endpoint_mapper[api_selection],
        )
    elif api_selection == "---":
        initialize_logo_and_title("Dashboard")
        st.subheader("API Information")

        for selected_page in list(pages.keys()):
            expander = st.beta_expander(label=f"{selected_page}", expanded=True)
            expander.write(f"{api_descriptions.get(selected_page)}")


def main() -> None:
    """Execute the main Demo App."""

    available_pages = {
        "Life Events Monitor": life_events_monitor,
        "Recent Life Events API": personal_dashboard,
        "Auto Insurance Prefill API": personal_dashboard,
        "PFR API": personal_dashboard,
    }

    user_selected_page = get_demo_pages(pages=available_pages)
    sidebar_api_selection(api_selection=user_selected_page, pages=available_pages)


if __name__ == "__main__":
    main()
