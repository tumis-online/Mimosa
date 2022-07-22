"""Train, Test Model and parsing Model messages."""
import asyncio
import json
import logging
from os import path

import rasa
from rasa.core.agent import Agent
from rasa.model import get_latest_model
from rasa.shared import data

from RASA.domain.constants import actions as nlu

CONFIDENCE_THRESHOLD = 0.7

CONFIG_FILE = "config.yml"
TRAINING_FILES_DIR = "data"
DOMAIN_DIR = "domain"
DOMAIN_FILE = path.join(DOMAIN_DIR, "domain.yml")
ENDPOINTS_FILE = "endpoints.yml"
CREDENTIALS_FILE = "credentials.yml"
OUTPUT_DIR = "models"
DEFAULT_MODEL_PATH = path.join(OUTPUT_DIR, "nlu.tar.gz")


class ModelHandler:
    """Handles model agent message processing."""
    current_request: dict

    def __init__(self, m_path: str) -> None:
        self.agent = Agent.load(model_path=m_path)
        logging.info("NLU model loaded successfully.")

    def message(self, message: str) -> dict:
        """
        Sends message to RASA agent.
        :param message: text provided by user
        :return: result from nlu with detected intent, entities and according actions
        """
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        self.current_request = result
        # return json_to_string(result)
        return result


def train_model():
    """Train model via rasa sdk."""
    rasa.train(DOMAIN_FILE, CONFIG_FILE, [TRAINING_FILES_DIR], OUTPUT_DIR)
    m_path = get_latest_model()
    # process_training_data(train_result)
    # run_cmdline(model_path)
    logging.info("NLU model %s trained successfully.", m_path)
    return m_path


def test_model():
    """Test model via rasa sdk."""
    nlu_data_directory = data.get_nlu_directory(TRAINING_FILES_DIR)
    stories_directory = data.get_core_directory(TRAINING_FILES_DIR)
    rasa.test(model_path, stories_directory, nlu_data_directory)
    logging.info("Done testing.")


async def parse_result(result: json) -> nlu.Intent:
    """
    Parses model JSON response.
    :param result: JSON result of model message
    :return: Intent with the highest confidence score with provided entities
    """
    intent_name = result["intent"]["name"]
    intent_confidence = result["intent"]["confidence"]
    req_entities = result["entities"]
    entities: list[nlu.Entity] = []
    for entity in req_entities:
        entity_type = entity["entity"]
        position = (entity["start"], entity["end"])
        confidence = entity["confidence_entity"]
        value = entity["value"]
        entities.append(nlu.Entity(entity_type, position, confidence, value))
    intent = nlu.Intent(intent_name, intent_confidence, entities)
    return intent


async def send_message(message: str) -> None:
    """
    Sends and parses model message.
    :param message: text input to model
    """
    result = mdl.message(message)
    intent = await parse_result(result)
    logging.info(
        "intent: %s, confidence: %f, entities: %s",
        intent.name, intent.confidence, intent.entities
    )
    if intent.confidence < CONFIDENCE_THRESHOLD:
        logging.info(result["intent_ranking"])


if __name__ == '__main__':
    # According to https://rasa.com/docs/rasa/next/jupyter-notebooks/#train-a-model.
    # model_path = train_model()
    # test_model()

    model_path = get_latest_model(OUTPUT_DIR)
    mdl = ModelHandler(model_path)
    sentences = [
        "Mach die Lampe an.",
        "Dimm die Lampe im Wohnzimmer etwas heller",
        "Schalte die Lampe im Bad aus",
        "Ich möchte die Leuchte im WC blau."
    ]
    for sentence in sentences:
        asyncio.run(send_message(message=sentence))
    """
    if os.path.isfile("errors.json"):
        print("NLU Errors:")
        print(open("errors.json").read())
    else:
        print("No NLU errors.")

    if os.path.isdir("results"):
        print("\n")
        print("Core Errors:")
        print(open("results/failed_test_stories.yml").read())
    """