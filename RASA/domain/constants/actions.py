"""Stores NLU domain specific action constants to be accessible."""
from enum import Enum


class Action(Enum):
    """NLU action names."""
    ENABLE_ITEM = "action_enable_item"
    DISABLE_ITEM = "action_disable_item"
    DIM = "action_dim"
    CHANGE_COLOR = "action_change_color"
    ADD_SCENE = "action_add_scene"

    class Validate(Enum):
        """Validation Actions."""
        SLOT_MAPPINGS = "validate_slot_mappings"

        class Form(Enum):
            """Validate Form Actions."""
            ITEM_CONFIG = "validate_item_config_form"
            LIGHT = "validate_light_form"
            POWER_SOCKET = "validate_power_socket_form"
            FALLBACK_ITEM = "validate_fallback_item_form"
            SCENE = "validate_scene_form"
