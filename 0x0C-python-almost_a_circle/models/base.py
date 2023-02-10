#!/usr/bin/python3
"""Define the base class"""


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
