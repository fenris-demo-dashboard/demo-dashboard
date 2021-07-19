from typing import Callable

from dashboard_supplements.io.request_handlers.mock_requests import (
    mock_business_query,
    mock_personal_query,
)

import pytest


@pytest.mark.parametrize(
    "service_name", ["PFR", "LifeEvents", "LifePrefill", "AutoPrefill"]
)
def test_mock_personal_query(service_name: str, generate_fake_person: Callable) -> None:
    fake_person = generate_fake_person()

    response = mock_personal_query(person=fake_person, service_name=service_name)

    assert response.get("status").lower() == "success"
    assert response is not None


def test_mock_business_query(generate_fake_business: Callable) -> None:
    fake_business = generate_fake_business()
    response = mock_business_query(business=fake_business, service_name="SMB")
    assert response.get("status").lower() == "success"
