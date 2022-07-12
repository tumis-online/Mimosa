from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet


class AddSceneAction(Action):

    def name(self) -> Text:
        return "add_scene"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        scene_name = tracker.get_slot('scene_name')
        # TODO action should query graphql api
        q = "select * from restaurants where cuisine='{0}' limit 1".format(scene_name)
        result = db.query(q)

        return [SlotSet("matches", result if result is not None else [])]

