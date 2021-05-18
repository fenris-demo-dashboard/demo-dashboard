"""Custom API request page."""
from demo_supplements.aesthetics.aesthetics import format_response_by_service
from demo_supplements.io.request_handlers.live_requests import live_query


def app(api: str, body: object):
    """Make a request to the customer's specified API."""
    try:
        response = live_query(input_object=body, service_name=api)
    except Exception:
        response = {"error": Exception}

    format_response_by_service(response=response, service_name=api)
