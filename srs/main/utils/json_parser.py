import json
from srs.main.utils.find_file import find


def get_config(name):
    json_file = find(name)
    with open(json_file, "r") as file:
        content = file.read()
    return json.loads(content)
