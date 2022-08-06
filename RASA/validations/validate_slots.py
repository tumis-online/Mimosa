from typing import Text, Any, Dict

from rasa_sdk import Tracker, ValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from bco.api.graphql.client import gql_client_handler


class ValidatePredefinedSlots(ValidationAction):
    def validate_item(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate item value."""
        request = ""
        client_handler = gql_client_handler.GraphQLClientHandler()
        client_handler.send_graphql_request(request)
        if isinstance(slot_value, str):
            # validation succeeded, capitalize the value of the "location" slot
            return {"": slot_value.capitalize()}
        # validation failed, set this slot to None
        return {"location": None}