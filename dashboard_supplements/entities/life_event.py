"""Dataclasses for the life event domain entities."""

from dataclasses import dataclass
from typing import Optional

from dashboard_supplements.entities.address import Address

import marshmallow_dataclass


@dataclass
class NewMoverInfo:
    """Dataclass to represent new mover info entity."""

    previous_address: Address
    current_address: Address


@dataclass
class LifeEvent:
    """Dataclass to represent life event entity."""

    event_type: str
    event_date: str
    process_date: str
    other_data: Optional[NewMoverInfo] = None


LifeEventSchema = marshmallow_dataclass.class_schema(LifeEvent)
