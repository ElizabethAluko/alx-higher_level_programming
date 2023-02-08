#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Defines student names and age"""

    def __init__(self, first_name, last_name, age):
        """Instantiate names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of student
        If attrs is a list of strings, represents 
        only those attributes included in the list.

        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = dict()
            old_dict = self.__dict__
            for (key, value) in old_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
