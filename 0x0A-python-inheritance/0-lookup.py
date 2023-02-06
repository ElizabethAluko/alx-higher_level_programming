#!/usr/bin/python3
"""Defines object attribute lookup function"""


def lookup(obj):
    """returns the list of available attributes of obj"""

    return(list(dir(obj)))
