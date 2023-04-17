import json


class Like(object):
    def __init__(self, json_str: str):
        self.__dict__ = json.loads(json_str)
        self.__id = self.__dict__.get("id")

    @property
    def id(self):
        return self.__id
