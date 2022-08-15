"""
Custom Actions run by rasa action server.
* Responsible for handling light actions and pass to Smart Home Control API.

For RASA SDK v3 Events Doc visit: https://rasa.com/docs/action-server/sdk-events
"""

import logging
from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from RASA.domain.constants.actions import Action as NLU_Action
from RASA.domain.constants.intents import Intent as NLU_Intent
from RASA.domain.constants.forms import Slot as NLU_Slot
from RASA.domain.constants.response import Response as NLU_Response


class EnableItemAction(Action):
    """NLU Action to process enable item request and pass to Smart Home Control API."""
    _action: str = NLU_Action.ENABLE_ITEM.value
    _intent: str = NLU_Intent.ENABLE_ITEM

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        slot_item = tracker.get_slot(NLU_Slot.ITEM)
        slot_location = tracker.get_slot(NLU_Slot.LOCATION)

        # item = next(tracker.get_latest_entity_values(Entity.ITEM), None)
        event = SlotSet(slot_item, slot_location)
        response = FollowupAction(name=NLU_Response.ACTION_PERFORMED)
        return [event, response]


class DisableItemAction(Action):
    """NLU Action to process disable item request and pass to Smart Home Control API."""
    _action: str = NLU_Action.DISABLE_ITEM
    _intent: str = NLU_Intent.DISABLE_ITEM

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        slot_item = tracker.get_slot(NLU_Slot.ITEM)
        slot_location = tracker.get_slot(NLU_Slot.LOCATION)
        # item = next(tracker.get_latest_entity_values(Entity.ITEM), None)
        if slot_item is None:
            return ""
        event = FollowupAction(
            name="",
            timestamp=None
        )


class DimLightAction(Action):
    """NLU Action to process dim light request and pass to Smart Home Control API."""
    _action: str = NLU_Action.DIM
    _intent: str = NLU_Intent.DIM

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        scene_name = tracker.get_slot(NLU_Slot.SCENE_NAME)
        # TODO action should query graphql api
        result = ""  # db.query(q)

        return [SlotSet("matches", result if result is not None else [])]


class ChangeColorAction(Action):
    """NLU Action to process change color request and pass to Smart Home Control API."""
    _action: str = NLU_Action.CHANGE_COLOR
    _intent: str = NLU_Intent.CHANGE_COLOR

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        item_slot = tracker.get_slot(NLU_Slot.ITEM)
        location_slot = tracker.get_slot(NLU_Slot.LOCATION)
        color_slot = tracker.get_slot(NLU_Slot.COLOR)
        logging.debug("Slots used for action: %s, %s, %s.", item_slot, location_slot, color_slot)
        # TODO action should query graphql api

        result = [item_slot, location_slot, color_slot]

        return [SlotSet("matches", result if result is not None else [])]
