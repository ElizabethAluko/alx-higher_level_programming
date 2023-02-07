#!/usr/bin/python3
"""Define an object representation of JSON string"""
import json


def from_json_string(my_str):
    """Returns an object of a JSON string"""
    return (json.loads(my_str))
