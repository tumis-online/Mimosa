import asyncio
import os

import rasa
import rasa.nlu
from rasa.model import get_latest_model
from rasa.shared import data
from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string

config = "config.yml"
training_files = "data/"
domain = "domain.yml"
endpoints = "endpoints.yml"
credentials = "credentials.yml"
output = "models/"
model_path = output + "nlu.tar.gz"


class Model:

    def __init__(self, m_path: str) -> None:
        self.agent = Agent.load(model_path=m_path)
        print("NLU model loaded")

    def message(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(self.agent.parse_message(message))
        return json_to_string(result)


def train_model():
    rasa.train(domain, config, [training_files], output)
    m_path = get_latest_model()
    # process_training_data(train_result)
    # run_cmdline(model_path)
    print(m_path)
    return m_path


"""https://rasa.com/docs/rasa/next/jupyter-notebooks/#train-a-model"""
if __name__ == '__main__':
    model_path = train_model()
    nlu_data_directory = data.get_nlu_directory(training_files)
    stories_directory = data.get_core_directory(training_files)
    print(stories_directory, nlu_data_directory)

    rasa.test(model_path, stories_directory, nlu_data_directory)
    print("Done testing.")

    mdl = Model(model_path)
    sentence = "Mach die Lampe an."
    print(mdl.message(sentence))

    if os.path.isfile("errors.json"):
        print("NLU Errors:")
        print(open("errors.json").read())
    else:
        print("No NLU errors.")

    if os.path.isdir("results"):
        print("\n")
        print("Core Errors:")
        print(open("results/failed_test_stories.yml").read())
