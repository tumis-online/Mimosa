"""
Custom Actions run by rasa action server.
* Responsible for handling scene actions and pass to Smart Home Control API.
"""

from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet


class EditSceneAction(Action):
    """NLU Action to process add scene request and pass to Smart Home Control API."""
    def name(self) -> Text:
        return "action_edit_scene"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # tracker.slots_to_validate()
        scene_name = tracker.get_slot('scene_name')
        current_user_intent = tracker.get_intent_of_latest_message()
        # TODO action should query graphql api
        result = []

        return [SlotSet("matches", result if result is not None else [])]


