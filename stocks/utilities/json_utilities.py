import json


def read_json_file(filepath):
    with open(filepath, "r") as json_file:
        data = json.load(json_file)
    return data
