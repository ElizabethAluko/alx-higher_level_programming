#!/usr/bin/python3
"""Defines a function that writes JSON representation of an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dump(my_obj))
