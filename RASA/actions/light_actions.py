from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class EnableItemAction(Action):

    def name(self) -> Text:
        return "action_enable_item"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: "DomainDict") -> List[
        Dict[Text, Any]]:
        pass


class DisableItemAction(Action):

    def name(self) -> Text:
        return "action_disable_item"

    async def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[
        Dict[Text, Any]]:
        pass


class DimLightAction(Action):

    def name(self) -> Text:
        return "dim"

    async def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        scene_name = tracker.get_slot('scene_name')
        # TODO action should query graphql api
        q = "select * from restaurants where cuisine='{0}' limit 1".format(scene_name)
        result = db.query(q)

        return [SlotSet("matches", result if result is not None else [])]


class ChangeColorAction(Action):

    def name(self) -> Text:
        return "change_color"

    async def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        scene_name = tracker.get_slot("scene_name")
        # TODO action should query graphql api
        q = "select * from restaurants where cuisine='{0}' limit 1".format(scene_name)
        result = db.query(q)

        return [SlotSet("matches", result if result is not None else [])]
