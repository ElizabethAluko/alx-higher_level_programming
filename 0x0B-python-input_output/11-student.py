#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Defines student names and age"""

    def __init__(self, first_name, last_name, age):
        """Instantiate names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of student"""
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all student attributes"""
        for k, v in json.items():
            setattr(self, k, v)
