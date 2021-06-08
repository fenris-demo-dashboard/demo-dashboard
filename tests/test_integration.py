from demo_supplements.io.request_handlers.auth import initialize_demo_client
from demo_supplements.io.request_handlers.live_requests import (
    live_query,
)

from heimdal.constants import service_names

import pytest


@pytest.mark.parametrize(
    "client_service_string",
    [
        service_names.pfr,
        service_names.life_events,
        service_names.auto_prefill,
        service_names.life_prefill,
        service_names.property_details,
        service_names.property_risks,
        service_names.property_replacement,
        service_names.smb,
    ],
)
def test_st_client(client_service_string):

    client = initialize_demo_client(client_service_string)
    assert client is not None


@pytest.mark.parametrize(
    "service_name",
    [
        service_names.pfr,
        service_names.life_events,
        service_names.auto_prefill,
        service_names.life_prefill,
    ],
)
def test_live_personal_query(service_name, generate_fake_person):
    fake_person = generate_fake_person()

    response = live_query(input_object=fake_person, service_name=service_name)

    assert response is not None
    assert response.get("status").lower() == "success"


@pytest.mark.parametrize(
    "service_name",
    [
        service_names.property_details,
        service_names.property_risks,
        service_names.property_replacement,
    ],
)
def test_live_property_query(service_name, generate_fake_address):
    fake_address = generate_fake_address()

    response = live_query(input_object=fake_address, service_name=service_name)

    assert response is not None
    assert response.get("status").lower() == "success"


def test_live_business_query(generate_fake_business):
    fake_address = generate_fake_business()

    response = live_query(input_object=fake_address, service_name="SMB")

    assert response is not None
    assert response.get("status").lower() == "success"
