"""Stores NLU domain specific form and slot constants to be accessible."""
from enum import Enum


class Slot(Enum):
    """NLU Slot names."""
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    ITEM = "item"
    ITEM_STATUS = "item_status"
    COLOR = "color"
    BRIGHTNESS = "brightness"
    LOCATION = "location"
    VALUE = "value"
    SCENE_NAME = "scene_name"


class Form(Enum):
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
