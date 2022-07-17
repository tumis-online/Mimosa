from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet


class AddSceneAction(Action):

    def name(self) -> Text:
        return "action_add_scene"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # tracker.slots_to_validate()
        scene_name = tracker.get_slot('scene_name')
        current_user_intent = tracker.get_intent_of_latest_message()
        # TODO action should query graphql api
        q = "select * from restaurants where cuisine='{0}' limit 1".format(scene_name)
        result = db.query(q)

        return [SlotSet("matches", result if result is not None else [])]


