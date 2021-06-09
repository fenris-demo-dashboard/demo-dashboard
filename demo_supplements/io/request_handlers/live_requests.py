from typing import Any, Dict

from demo_supplements.aesthetics.aesthetics import spinner_decorator_factory
from demo_supplements.io.request_handlers.auth import initialize_demo_client

from heimdal.io.request_handlers.business import get_business_data
from heimdal.io.request_handlers.personal import get_personal_data
from heimdal.io.request_handlers.property import get_property_data

fetch_methods = {
    "PFR": get_personal_data,
    "LifeEvents": get_personal_data,
    "LifePrefill": get_personal_data,
    "AutoPrefill": get_personal_data,
    "PropertyDetails": get_property_data,
    "PropertyRisks": get_property_data,
    "PropertyReplacement": get_property_data,
    "SMB": get_business_data,
}


@spinner_decorator_factory(spinner_text="Querying Fenris APIs...")
def live_query(input_object: object, service_name: str) -> Dict[str, Any]:
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
