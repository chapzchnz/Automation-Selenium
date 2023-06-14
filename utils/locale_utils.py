import json
import os

from resources.application_settings import APPLICATION_LOCALE


def load_json_value(file_path, key):
    with open(file_path, "r") as file:
        json_data = json.load(file)
    return json_data.get(key)


def get(key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if APPLICATION_LOCALE == "en_EN":
        file_path = os.path.join(current_dir, "..", "resources", "en", "en_EN.json")
    else:
        file_path = os.path.join(current_dir, "..", "resources", "german", "ger_GER.json")

    return load_json_value(file_path, key)
