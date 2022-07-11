import asyncio
import logging

import rasa
import rasa.nlu
from rasa.model import get_latest_model
from rasa.shared import data
from rasa.core.agent import Agent

from RASA.intent import Entity, Intent

config = "config.yml"
training_files = "data/"
domain = "domain.yml"
endpoints = "endpoints.yml"
credentials = "credentials.yml"
output = "models/"
default_model_path = output + "nlu.tar.gz"


class Model:
    current_request: dict

    def __init__(self, m_path: str) -> None:
        self.agent = Agent.load(model_path=m_path)
        print("NLU model loaded successfully.")

    def message(self, message: str) -> dict:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        self.current_request = result
        # return json_to_string(result)
        return result


def train_model():
    rasa.train(domain, config, [training_files], output)
    m_path = get_latest_model()
    # process_training_data(train_result)
    # run_cmdline(model_path)
    print(m_path)
    return m_path


def test_model():
    nlu_data_directory = data.get_nlu_directory(training_files)
    stories_directory = data.get_core_directory(training_files)
    rasa.test(model_path, stories_directory, nlu_data_directory)
    logging.info("Done testing.")


def send_message(message: str):
    result = mdl.message(message)
    intent_name = result["intent"]["name"]
    intent_confidence = result["intent"]["confidence"]
    req_entities = result["entities"]
    entities: list[Entity] = []
    for entity in req_entities:
        entity_type = entity["entity"]
        position = (entity["start"], entity["end"])
        confidence = entity["confidence_entity"]
        value = entity["value"]
        entities.append(Entity(entity_type, position, confidence, value))
    intent = Intent(intent_name, intent_confidence, entities)
    logging.info(f"intent: {intent.name}, confidence: {intent.confidence}, entities: {intent.entities}")
    if intent.confidence < 0.7:
        logging.info(result["intent_ranking"])


"""https://rasa.com/docs/rasa/next/jupyter-notebooks/#train-a-model"""
if __name__ == '__main__':
    # model_path = train_model()
    # test_model()

    model_path = get_latest_model(output)
    mdl = Model(model_path)
    sentences = ["Mach die Lampe an.",
                 "Dimm die Lampe im Wohnzimmer etwas heller",
                 "Schalte die Lampe im Bad aus",
                 "Ich möchte die Leuchte im WC blau."]
    for sentence in sentences:
        send_message(message=sentence)
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