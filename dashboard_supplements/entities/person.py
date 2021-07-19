"""Dataclasses for the person domain entities."""

from dataclasses import dataclass
from typing import List, Optional

from dashboard_supplements.entities.address import Address
from dashboard_supplements.entities.shared_schemas import CamelCaseSchema

import marshmallow_dataclass


@dataclass
class Person:
    """Dataclass to hold Person field inputs for personal APIs."""

    first_name: str = ""
    middle_name: Optional[str] = None
    last_name: str = ""
    date_of_birth: Optional[str] = None
    address: Optional[Address] = None
    other_addresses: Optional[List[Address]] = None


PersonSchema = marshmallow_dataclass.class_schema(Person)
PersonalRequestSchema = marshmallow_dataclass.class_schema(
    Person, base_schema=CamelCaseSchema
)
