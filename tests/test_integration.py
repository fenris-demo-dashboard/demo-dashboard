from demo_supplements.io.request_handlers.auth import initialize_demo_client
from demo_supplements.io.request_handlers.live_requests import (
    live_query,
)


def test_st_pfr_client():

    client = initialize_demo_client("PFR")
    assert client is not None


def test_st_life_events_client():

    client = initialize_demo_client("LifeEvents")
    assert client is not None


def test_st_auto_prefill_client():

    client = initialize_demo_client("AutoPrefill")
    assert client is not None


def test_st_property_details_client():

    client = initialize_demo_client("PropertyDetails")
    assert client is not None


def test_st_property_risks_client():

    client = initialize_demo_client("PropertyRisks")
    assert client is not None


def test_live_query_for_pfr(generate_fake_person):
    fake_person = generate_fake_person()

    response = live_query(input_object=fake_person, service_name="PFR")

    assert response is not None
    assert response.get("status") == "Success"


def test_live_query_for_life_events(generate_fake_person):
    fake_person = generate_fake_person()

    response = live_query(input_object=fake_person, service_name="LifeEvents")

    assert response is not None
    assert response.get("status") == "SUCCESS"


def test_live_query_for_auto_prefill(generate_fake_person):
    fake_person = generate_fake_person()

    response = live_query(input_object=fake_person, service_name="AutoPrefill")

    assert response is not None
    assert response.get("status") == "Success"


def test_life_query_for_property_details(generate_fake_address_for_property):
    fake_address = generate_fake_address_for_property()

    response = live_query(input_object=fake_address, service_name="PropertyDetails")

    assert response is not None
    assert response.get("status").lower() == "success"
