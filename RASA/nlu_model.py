import os

import rasa
from rasa.shared import data

config = "config.yml"
training_files = "data/"
domain = "domain.yml"
output = "models/"


"""https://rasa.com/docs/rasa/next/jupyter-notebooks/#train-a-model"""
if __name__ == '__main__':
    train_result = rasa.train(domain, config, [training_files], output)
    model_path = train_result.model
    print(model_path)

    nlu_data_directory = data.get_nlu_directory(training_files)
    stories_directory = data.get_core_directory(training_files)
    print(stories_directory, nlu_data_directory)

    rasa.test(model_path, stories_directory, nlu_data_directory)
    print("Done testing.")

    if os.path.isfile("errors.json"):
        print("NLU Errors:")
        print(open("errors.json").read())
    else:
        print("No NLU errors.")

    if os.path.isdir("results"):
        print("\n")
        print("Core Errors:")
        print(open("results/failed_test_stories.yml").read())
