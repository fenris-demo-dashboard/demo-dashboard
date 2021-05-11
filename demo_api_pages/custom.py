"""Pre-Fill API page for Auto Pre-Fill Demo."""
from demo_supplements.aesthetics.aesthetics import initialize_logo_and_title
from demo_supplements.dashboard_components.personal_request_form import (
    personal_request_form,
)


def app():
    """Allow custom request to Fenris APIs."""
    initialize_logo_and_title("Custom API Request")
    personal_request_form()
