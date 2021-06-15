from dataclasses import dataclass
from typing import Optional


@dataclass
class PersonAddressInputMap:
    """Dataclass to hold inputs for Personal APIs."""

    first_name: str
    last_name: str
    address_line1: str
    city: str
    state: str
    zip_code: str
    middle_name: Optional[str] = None
    date_of_birth: Optional[str] = None