#!/usr/bin/python3
"""Define the base class"""
import json


class Base:
    """Manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a new Base"""

        if id != None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json representation of the dictiinary"""
        if (list_dictionaries is None or
                list_dictionaries == []):
            return ("[]")

        return (json.dumps(list_dictionaries))
