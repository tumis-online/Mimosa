# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from RASA.domain import domain as nlu
from user import User


class GreetAction(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user: str = "Benutzer"
        # TODO receive from database
        dispatcher.utter_message(text=f"Hallo {user}!")
        return []


class CreateUserAction(Action):

    def name(self) -> Text:
        return "action_create_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        first_name = tracker.get_slot(nlu.Slot.FIRST_NAME)
        last_name = tracker.get_slot(nlu.Slot.LAST_NAME)
        user: User = User(first_name=first_name, last_name=last_name)
        # TODO send to database
        dispatcher.utter_message(text=f"Hallo {user.first_name} {user.last_name}!")
        return []
