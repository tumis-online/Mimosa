from dataclasses import dataclass


@dataclass
class Entity:
    """NLU Entity names"""
    ITEM = "ITEM"
    LOC = "LOC"
    VALUE = "VALUE"
    COLOR = "COLOR"
    STATE = "STATE"
    BRIGHTNESS = "BRIGHTNESS"
    NAME = "NAME"

    """dataclass describing extracted entity in text."""
    entity_type: str
    position: tuple
    confidence: float
    value: str


@dataclass
class Intent:
    """NLU Intent names"""
    GREET = "greet"
    GOODBYE = "goodbye"
    MOOD_GREAT = "mood_great"
    MOOD_UNHAPPY = "mood_unhappy"
    AFFIRM = "affirm"
    DENY = "deny"
    ENABLE_ITEM = "enable_item"
    DISABLE_ITEM = "disable_item"
    DIM = "dim"
    CHANGE_COLOR = "change_color"
    ADD_SCENE = "add_scene"
    BOT_REQUEST = "bot_request"
    FALLBACK = "nlu_fallback"

    """dataclass describing extracted intent in given text."""
    name: str
    confidence: float
    entities: list[Entity]
