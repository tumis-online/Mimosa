from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Unit(BaseModel):
    id: Optional[str]
    label: str
    type: str
    location: str


class State(Enum):
    ON = "ON"
    OFF = "OFF"

