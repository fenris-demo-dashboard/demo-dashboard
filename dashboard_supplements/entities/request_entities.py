"""Dataclasses for the request body entities."""

from dataclasses import dataclass, field
from typing import List, Optional

from dashboard_supplements.entities.shared_schemas import CamelCaseSchema

import marshmallow_dataclass


@dataclass
class Address:
    """Dataclass to hold Address field inputs for Pfr."""

    address_line1: str = ""
    city: Optional[str] = None
    state: str = ""
    zip_code: Optional[str] = None


AddressSchema = marshmallow_dataclass.class_schema(Address)
AddressRequestSchema = marshmallow_dataclass.class_schema(
    Address, base_schema=CamelCaseSchema
)


@dataclass
class Business:
    """Dataclass to hold Business field inputs for business APIs."""

    address: Optional[Address]
    names: List[str] = field(default_factory=list)
    other_addresses: Optional[List[Address]] = None


BusinessSchema = marshmallow_dataclass.class_schema(Business)
BusinessRequestSchema = marshmallow_dataclass.class_schema(
    Business, base_schema=CamelCaseSchema
)


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
