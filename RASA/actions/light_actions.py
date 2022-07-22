"""
Custom Actions run by rasa action server.
* Responsible for handling light actions and pass to Smart Home Control API.
"""

import logging
from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from RASA.domain.constants.responses import Responses
from RASA.domain.constants.actions import Action as NLU_Actions
from RASA.domain.constants.intents import Intent as NLU_Intents
from RASA.domain.constants import forms as nlu


class EnableItemAction(Action):
    """NLU Action to process enable item request and pass to Smart Home Control API."""
    _action: str = NLU_Actions.ENABLE_ITEM
    _intent: str = NLU_Intents.ENABLE_ITEM

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        current_user_intent = tracker.get_intent_of_latest_message()
        if not check_intent(current_user_intent, self._intent):
            return []
        slot_item = tracker.get_slot(nlu.Slot.ITEM)
        slot_location = tracker.get_slot(nlu.Slot.LOCATION)

        # item = next(tracker.get_latest_entity_values(Entity.ITEM), None)
        event = SlotSet(slot_item, slot_location)
        return [event]


class DisableItemAction(Action):
    """NLU Action to process disable item request and pass to Smart Home Control API."""
    _action: str = NLU_Actions.DISABLE_ITEM
    _intent: str = NLU_Intents.DISABLE_ITEM

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        current_user_intent = tracker.get_intent_of_latest_message()
        if not check_intent(current_user_intent, self._intent):
            return []
        slot_item = tracker.get_slot(nlu.Slot.ITEM)
        slot_location = tracker.get_slot(nlu.Slot.LOCATION)
        # item = next(tracker.get_latest_entity_values(Entity.ITEM), None)
        if slot_item is None:
            return ""
        pass


class DimLightAction(Action):
    """NLU Action to process dim light request and pass to Smart Home Control API."""
    _action: str = NLU_Actions.DIM
    _intent: str = NLU_Intents.DIM

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        current_user_intent = tracker.get_intent_of_latest_message()
        if not check_intent(current_user_intent, self._intent):
            return []
        scene_name = tracker.get_slot(nlu.Slot.SCENE_NAME)
        # TODO action should query graphql api
        result = "" # db.query(q)

        return [SlotSet("matches", result if result is not None else [])]


def check_intent(current_user_intent, class_intent: str) -> bool:
    """
    Checks, whether current user intent is equal to class intent.
    :param current_user_intent: intent predicted by nlu
    :param class_intent: intent which should cause action
    :return: True, if intents match
    """
    if current_user_intent is not class_intent:
        logging.error("Intent %s is leading to a wrong action.", current_user_intent)
        return False
    return True


class ChangeColorAction(Action):
    """NLU Action to process change color request and pass to Smart Home Control API."""
    _action: str = NLU_Actions.CHANGE_COLOR
    _intent: str = NLU_Intents.CHANGE_COLOR

    def name(self) -> Text:
        return self._action

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        logging.info("Run '%s' action.", self._action)
        current_user_intent = tracker.get_intent_of_latest_message()
        if not check_intent(current_user_intent, self._intent):
            dispatcher.utter_message(template=Responses.OUT_OF_SCOPE.value)
            return []
        item_slot = tracker.get_slot(nlu.Slot.ITEM)
        location_slot = tracker.get_slot(nlu.Slot.LOCATION)
        color_slot = tracker.get_slot(nlu.Slot.COLOR)
        logging.debug("Slots used for action: %s, %s, %s.", item_slot, location_slot, color_slot)
        # TODO action should query graphql api

        result = [item_slot, location_slot, color_slot]

        return [SlotSet("matches", result if result is not None else [])]
