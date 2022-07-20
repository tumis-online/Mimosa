from typing import Dict, List
from dataclasses import dataclass


class Action:
    """NLU action names"""
    ENABLE_ITEM = "action_enable_item"
    DISABLE_ITEM = "action_disable_item"
    DIM = "action_dim"
    CHANGE_COLOR = "action_change_color"
    ADD_SCENE = "action_add_scene"

    class Validate:
        """Validation Actions"""
        SLOT_MAPPINGS = "validate_slot_mappings"

        class Form:
            """Validate Form Actions"""
            ITEM_CONFIG = "validate_item_config_form"
            LIGHT = "validate_light_form"
            POWER_SOCKET = "validate_power_socket_form"
            FALLBACK_ITEM = "validate_fallback_item_form"
            SCENE = "validate_scene_form"


@dataclass
class Slot:
    """NLU Slot names"""
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    ITEM = "item"
    ITEM_STATUS = "item_status"
    COLOR = "color"
    BRIGHTNESS = "brightness"
    LOCATION = "location"
    VALUE = "value"
    SCENE_NAME = "scene_name"


@dataclass
class Form:
    """NLU Slots required for forms."""
    # General forms
    NAME = [Slot.FIRST_NAME, Slot.LAST_NAME]
    ITEM_CONFIG = [Slot.ITEM, Slot.LOCATION]
    FALLBACK_ITEM = [Slot.ITEM_STATUS, Slot.VALUE]

    # Item forms
    LIGHT = [Slot.ITEM_STATUS, Slot.COLOR, Slot.VALUE]
    POWER_SOCKET = [Slot.ITEM_STATUS]

    # Scene forms
    SCENE = [Slot.SCENE_NAME]


@dataclass
class Entity:
    """NLU Entity names"""
    ITEM = "ITEM"
    LOC = "LOC"
    LOCAL_GEO = {
        "THIS": ["diese", "das", "dieses", "hier", "da"],
        "ALL": ["alle", "überall"]
    }
    VALUE = "VALUE"
    COLOR = "COLOR"
    STATE = "STATE"
    BRIGHTNESS = "BRIGHTNESS"
    SCENE_NAME = "SCENE_NAME"
    FIRST_NAME = "FIRST_NAME"
    LAST_NAME = "LAST_NAME"

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
