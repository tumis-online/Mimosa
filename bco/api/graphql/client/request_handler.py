"""Formatting User Input into Request Representation."""
import json
from typing import List, Dict
from fastapi import FastAPI
from RASA.domain.constants import Intent
from bco.api.graphql.client import gql_client_handler
from bco.api.graphql.client.requests.files import RequestFile

app = FastAPI()


@app.get("/")
async def request(intent: str, entities: List[str]) -> bool:
    """
    Transforms action with intentions and entities (with decent accuracy percentage)
    extracted from User input into request and performs according action.
    :param intent: estimated intent extracted from user input
    :param entities: estimated entities extracted from user input
    :return: True, if request successful, False otherwise
    """
    if intent == Intent.ENABLE_ITEM:
        # TODO Send request to client docker container
        # Session needed
        await gql_client_handler.execute_query(Request.Type.GET_LIGHTS)
        return True
    return False

# NLU Entities (Item) ?


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