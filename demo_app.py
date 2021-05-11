"""Fenris API Demo App dashboard home page."""

from demo_api_pages import auto_prefill, custom, life_events, pfr

from demo_supplements.aesthetics.aesthetics import initialize_logo_and_title
from demo_supplements.demo_text.demo_dashboard_text import api_descriptions

import streamlit as st


def get_demo_pages(pages):
    """Display demo pages in a sidebar streamlit select box.

    Returns selected API and list of available pages.
    """
    api_selection_options = list(pages.keys())
    api_selection_options.insert(0, "---")
    st.sidebar.title("Control Panel")
    api_selection = st.sidebar.selectbox("Select Capability", api_selection_options)
    return api_selection


def sidebar_api_selection(api_selection, pages):
    """Generate sidebar dropdown sidebar API selection."""
    if api_selection != "---":
        selected_page = pages[api_selection]
        selected_page.app()
    elif api_selection == "---":
        initialize_logo_and_title("Dashboard")
        st.subheader("API Information")

        for selected_page in list(pages.keys()):
            expander = st.beta_expander(label=f"{selected_page}", expanded=True)
            expander.write(f"{api_descriptions.get(selected_page)}")


def main():
    """Execute the main Demo App."""
    available_pages = {
        "Life Events API": life_events,
        "Auto Insurance Prefill API": auto_prefill,
        "PFR API": pfr,
        "Custom Request": custom,
    }

    user_selected_page = get_demo_pages(pages=available_pages)
    sidebar_api_selection(api_selection=user_selected_page, pages=available_pages)


if __name__ == "__main__":
    main()
