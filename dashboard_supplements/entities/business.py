"""Dataclasses for the business domain entities."""

from dataclasses import dataclass, field
from typing import List, Optional

from dashboard_supplements.entities.address import Address
from dashboard_supplements.entities.shared_schemas import CamelCaseSchema

import marshmallow_dataclass


@dataclass
class Business:
    """Dataclass to hold Business field inputs for business APIs."""

    names: List[str] = field(default_factory=list)
    address: Address = None
    other_addresses: Optional[List[Address]] = None


BusinessSchema = marshmallow_dataclass.class_schema(Business)
BusinessRequestSchema = marshmallow_dataclass.class_schema(
    Business, base_schema=CamelCaseSchema
)
