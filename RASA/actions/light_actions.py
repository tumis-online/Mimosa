from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from RASA import domain as nlu


class EnableItemAction(Action):

    def name(self) -> Text:
        return nlu.Action.ENABLE_ITEM

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        current_user_intent = tracker.get_intent_of_latest_message()
        slot_item = tracker.get_slot(nlu.Slot.ITEM)
        slot_location = tracker.get_slot(nlu.Slot.LOCATION)
        # item = next(tracker.get_latest_entity_values(Entity.ITEM), None)
        event: EventType
        pass


class DisableItemAction(Action):

    def name(self) -> Text:
        return nlu.Action.DISABLE_ITEM

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        current_user_intent = tracker.get_intent_of_latest_message()
        slot_item = tracker.get_slot(nlu.Slot.ITEM)
        slot_location = tracker.get_slot(nlu.Slot.LOCATION)
        # item = next(tracker.get_latest_entity_values(Entity.ITEM), None)
        if slot_item is None:
            return ""
        pass


class DimLightAction(Action):

    def name(self) -> Text:
        return nlu.Action.DIM

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        current_user_intent = tracker.get_intent_of_latest_message()
        scene_name = tracker.get_slot(nlu.Slot.SCENE_NAME)
        # TODO action should query graphql api
        q = "select * from restaurants where cuisine='{0}' limit 1".format(scene_name)
        result = db.query(q)

        return [SlotSet("matches", result if result is not None else [])]


class ChangeColorAction(Action):

    def name(self) -> Text:
        return nlu.Action.CHANGE_COLOR

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        current_user_intent = tracker.get_intent_of_latest_message()
        scene_name = tracker.get_slot(nlu.Slot.SCENE_NAME)
        # TODO action should query graphql api
        q = "select * from restaurants where cuisine='{0}' limit 1".format(scene_name)
        result = db.query(q)

        return [SlotSet("matches", result if result is not None else [])]
