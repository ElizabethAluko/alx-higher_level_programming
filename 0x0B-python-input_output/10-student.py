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
        if (type(attrs) == list):
            for i in attrs:
                if all(type(i) == str):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
