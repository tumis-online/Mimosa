from dataclasses import dataclass


@dataclass
class Entity:
    entity_type: str
    position: tuple
    confidence: float
    value: str


@dataclass
class Intent:
    name: str
    confidence: float
    entities: list[Entity]
