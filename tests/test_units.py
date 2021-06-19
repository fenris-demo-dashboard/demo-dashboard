from typing import Callable

from dashboard_supplements.io.request_handlers.mock_requests import mock_personal_query


def test_mock_personal_query_for_pfr(generate_fake_person: Callable) -> None:
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="PFR")

    assert response.get("status") == "Success"
    assert response is not None


def test_mock_personal_query_for_life_events(generate_fake_person: Callable) -> None:
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="LifeEvents")

    assert response.get("status") == "SUCCESS"
    assert response is not None


def test_mock_personal_query_for_auto_prefill(generate_fake_person: Callable) -> None:
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name="AutoPrefill")

    assert response.get("status") == "Success"
    assert response is not None

