"""Dataclasses for the address domain entities."""

from dataclasses import dataclass
from typing import Optional

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
