"""Test functions used by the demo dashboard."""


from demo_supplements.io.deserializers.person import (
    load_person_from_first_and_last_name,
)
from demo_supplements.io.request_handlers.auth import initialize_demo_client
from demo_supplements.io.request_handlers.custom_requests import (
    query_auto_prefill_with_custom_person,
)
from demo_supplements.io.request_handlers.live_requests import (
    live_query,
)
from demo_supplements.io.request_handlers.mock_requests import mock_personal_query

# TODO: Add testing for - load_credentials, deserializers, serializers
# test formatted address string, match image to row


def test_st_client():

    client = initialize_demo_client("PFR")

    assert client is not None


def test_load_person_from_first_and_last_name(
    fake_people_df, fake_people_person_address_input_map
):
    fake_people_df = fake_people_df()
    fake_people_person_address_input_map = fake_people_person_address_input_map()

    first_name = "Carissa"
    last_name = "Sharma"

    person = load_person_from_first_and_last_name(
        df=fake_people_df,
        input_map=fake_people_person_address_input_map,
        first_name=first_name,
        last_name=last_name,
    )
    assert person is not None


def test_mock_personal_query_for_pfr(generate_fake_person):
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="PFR")

    assert response.get("status") == "Success"
    assert response is not None


def test_live_query_for_pfr(generate_fake_person):
    fake_person = generate_fake_person()

    response = live_query(input_object=fake_person, service_name="PFR")

    assert response is not None
    assert response.get("status") == "Success"


def test_mock_personal_query_for_life_events(generate_fake_person):
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="LifeEvents")

    assert response.get("status") == "SUCCESS"
    assert response is not None


def test_live_query_for_life_events(generate_fake_person):
    fake_person = generate_fake_person()

    response = live_query(input_object=fake_person, service_name="LifeEvents")

    assert response is not None
    assert response.get("status") == "SUCCESS"


def test_mock_personal_query_for_auto_prefill(generate_fake_person):
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="AutoPrefill")

    assert response.get("status") == "Success"
    assert response is not None


def test_live_query_for_auto_prefill(generate_fake_person):
    fake_person = generate_fake_person()

    response = live_query(input_object=fake_person, service_name="AutoPrefill")

    assert response is not None
    assert response.get("status") == "Success"
