from demo_supplements.aesthetics.aesthetics import spinner_decorator_factory
from demo_supplements.io.request_handlers.auth import initialize_demo_client

from heimdal.io.request_handlers.auto_prefill import get_auto_prefill_data
from heimdal.io.request_handlers.life_event import get_life_event_data
from heimdal.io.request_handlers.pfr import get_pfr_data
from heimdal.io.request_handlers.property import get_property_data

fetch_methods = {
    "PFR": get_pfr_data,
    "LifeEvents": get_life_event_data,
    "AutoPrefill": get_auto_prefill_data,
    "PropertyDetails": get_property_data,
}


@spinner_decorator_factory(spinner_text="Querying Fenris APIs...")
def live_query(input_object, service_name):
    """
    Query the inputted API with input_object given service name.
    Returns response_json.
    """

    client = initialize_demo_client(service_name=service_name)
    fetch_method = fetch_methods.get(service_name)
    service = client.service_constructor(client=client)

    response_json, headers, raw_response, idx = fetch_method(
        service.endpoint,
        client.bearer_token,
        input_object,
        job_id=f"fenris-demo-app-{service_name}-query",
        record_number=1,
    ).result()

    return response_json
