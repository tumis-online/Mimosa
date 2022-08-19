"""Formatting User Input into Request Representation."""
import json
from typing import List, Dict

from RASA.domain.constants import Intent
from bco.api.graphql.client.requests.files import RequestFile


class Request:
    """Representation of intentions and entities extracted from User input as GraphQL requests."""

    request_file: str
    variables: Dict[str: str]

    class Type:
        """Type of Request providing file."""
        # Queries
        GET_DEVICES = RequestFile.Query.GET_DEVICES
        GET_LIGHTS = RequestFile.Query.GET_LIGHTS
        GET_LOCATIONS = RequestFile.Query.GET_LOCATIONS

        # Mutations
        ADD_ITEM = RequestFile.Mutation.ADD_ITEM
        REMOVE_ITEM = RequestFile.Mutation.REMOVE_ITEM
        ENABLE_ITEM = RequestFile.Mutation.SWITCH_LIGHT
        CHANGE_COLOR = RequestFile.Mutation.CHANGE_COLOR
        DIM_LIGHT = RequestFile.Mutation.DIM_LIGHT
        ADD_SCENE = RequestFile.Mutation.ADD_SCENE
        REMOVE_SCENE = RequestFile.Mutation.REMOVE_SCENE


class RequestHandler:
    """Takes intentions and entities (with decent accuracy percentage)
    extracted from User input and performs according action."""

    current_intent: str
    current_entities: List[str]

    async def request(self, intent: str, entities: List[str]) -> bool:
        """
        Transforms action with intent and entities provided into request.
        :param intent: estimated intent extracted from user input
        :param entities: estimated entities extracted from user input
        :return: True, if request successful, False otherwise
        """
        self.current_intent = intent
        self.current_entities = entities

        if intent == Intent.ENABLE_ITEM:
            # TODO Send request to client docker container
            return True
        return False

    async def _perform_request(self, request: Request) -> json:
        pass

    # NLU Entities (Item) ?
