#!/usr/bin/python3
"""Define the base class"""
import json


class Base:
    """Manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a new Base"""

        if id is not None:
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

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string representation
        of the object"""
        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                d_string = [s.to_dictionary() for s in list_objs]
                f.write(Base.to_json_string(d_string))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation"""
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all
        attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
        new.update(**dictionary)
        return (new)
