from demo_supplements.aesthetics.aesthetics import spinner_decorator_factory
from demo_supplements.io.request_handlers.auth import initialize_demo_client

from heimdal.client import Client
from heimdal.entities.address import Address
from heimdal.entities.person import Person
from heimdal.io.request_handlers.auto import get_auto_prefill_data
from heimdal.io.request_handlers.life_event import get_life_event_data
from heimdal.io.request_handlers.pfr import get_pfr_data
from heimdal.io.request_handlers.property_details import get_property_details_data


@spinner_decorator_factory(spinner_text="Querying Scoring API...")
def query_pfr_with_custom_person(
    person: Person,
    client: Client = initialize_demo_client(service_name="PFR"),
):
    """
    Query the PFR API given the inputted person.
    Returns response_json.
    """

    response_json, headers, raw_response, idx = get_pfr_data(
        pfr_url=client.pfr_url,
        bearer_token=client.bearer_token,
        person=person,
        job_id="fenris-demo-app",
        record_number=1,
    ).result()

    return response_json


@spinner_decorator_factory(spinner_text="Querying Life Events API...")
def query_life_events_with_custom_person(
    person: Person,
    client: Client = initialize_demo_client(service_name="LifeEvents"),
):
    """
    Query the Life Events API given the inputted person.
    Returns response_json.
    """

    response_json, headers, raw_response, idx = get_life_event_data(
        life_event_url=client.life_events_url,
        bearer_token=client.bearer_token,
        person=person,
        job_id="fenris-demo-app",
        record_number=1,
    ).result()

    return response_json


@spinner_decorator_factory(spinner_text="Querying Property Details API...")
def query_property_with_custom_address(
    address: Address,
    client: Client = initialize_demo_client(service_name="PropertyDetails"),
):
    """
    Query the Property Details API given the inputted address object.
    Returns response_json.
    """

    response_json, headers, raw_response, idx = get_property_details_data(
        property_url=client.property_details_url,
        bearer_token=client.bearer_token,
        address=address,
        job_id="fenris-demo-app",
        record_number=1,
    ).result()

    return response_json


@spinner_decorator_factory(spinner_text="Querying Auto Prefill API...")
def query_auto_prefill_with_custom_person(
    person: Person,
    client: Client = initialize_demo_client(service_name="AutoPrefill"),
):
    """
    Query the Auto Prefill API given the inputted person.
    Returns response_json.
    """

    response_json, headers, raw_response, idx = get_auto_prefill_data(
        auto_prefill_url=client.auto_prefill_url,
        bearer_token=client.bearer_token,
        person=person,
        job_id="fenris-demo-app",
        record_number=1,
    ).result()

    return response_json
