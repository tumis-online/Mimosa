"""
Custom Actions run by rasa action server.
* Responsible for handling actions depending on slot and pass to user database.
"""
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from RASA.domain.constants import Slot as NLU_Slots
from user import User


class GreetAction(Action):
    """NLU Action to greet user with slot name."""
    def name(self) -> Text:
        return "action_greet"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user: str = "Benutzer"
        # TODO receive from database
        dispatcher.utter_message(text=f"Hallo {user}!")
        return []


class CreateUserAction(Action):
    """NLU Action to process create user request and pass to database."""
    def name(self) -> Text:
        return "action_create_user"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        first_name = tracker.get_slot(NLU_Slots.FIRST_NAME)
        last_name = tracker.get_slot(NLU_Slots.LAST_NAME)
        user: User = User(first_name=first_name, last_name=last_name)
        # TODO send to database
        dispatcher.utter_message(text=f"Hallo {user.first_name} {user.last_name}!")
        return []
