from enum import Enum
from typing import Optional, Set
from pydantic import BaseModel


# Set of items that are currently supported.
item_db: Set[str] = {""}


class Unit(BaseModel):
    """"""
    id: Optional[str]
    label: str
    type: str
    location: str


class State(Enum):
    """States that an Item can be in."""
    ON = "ON"
    OFF = "OFF"

