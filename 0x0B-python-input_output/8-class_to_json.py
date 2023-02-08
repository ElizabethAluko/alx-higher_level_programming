#!/usr/bin/python3
"""Defines a function that returns a dictionary"""


def class_to_json(obj):
    """Returns the dictionary representation of object"""
    return (obj.__dict__)
