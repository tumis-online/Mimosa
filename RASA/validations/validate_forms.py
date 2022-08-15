import logging
from typing import Text, List, Any, Dict, Set

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from RASA.domain.constants.response import Response
from RASA.domain.constants.actions import Action as NLU_Actions
from bco.api.graphql import smart_env


def check_intent(current_user_intent: str, class_intent: str) -> bool:
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


class ValidateItemConfigForm(FormValidationAction):
    """
    Validate form input by requesting item database from Smart Home API.
    """
    def name(self) -> Text:
        return NLU_Actions.Validate.Form.ITEM_CONFIG

    @staticmethod
    def item_db() -> Set[Text]:
        """Database of supported items"""
        return smart_env.item_db

    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        current_user_intent = tracker.get_intent_of_latest_message()
        if not check_intent(current_user_intent, self._intent):
            out_of_scope_utterance: str = Response.OUT_OF_SCOPE
            dispatcher.utter_message(template=out_of_scope_utterance)
            return []
        additional_slots = ["outdoor_seating"]
        if tracker.slots.get("outdoor_seating") is True:
            # If the user wants to sit outside, ask
            # if they want to sit in the shade or in the sun.
            additional_slots.append("shade_or_sun")

        return additional_slots + domain_slots

    def validate_item(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validates, if item value can be found in database."""
        print(domain)
        if slot_value in self.item_db():
            # validation succeeded, set the value of the "item" slot to value
            return {"item": slot_value}

        # validation failed, set this slot to None so that the
        # user will be asked for the slot again (Trigger)
        dispatcher.utter_message(text=f"Leider kann ich ein Gerät '{slot_value}' nicht finden.")
        return {"item": None}
