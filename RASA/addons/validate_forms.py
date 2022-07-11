from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateItemConfigForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_item_config_form"

    @staticmethod
    def item_db() -> List[Text]:
        """Database of supported items"""
        return ["light", "power_socket"]

    def validate_item(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate item value."""
        print(domain)
        if slot_value in self.item_db():
            # validation succeeded, set the value of the "item" slot to value
            return {"item": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again (Trigger)
            dispatcher.utter_message(text=f"Leider kann ich ein Gerät '{slot_value}' nicht finden.")
            return {"item": None}