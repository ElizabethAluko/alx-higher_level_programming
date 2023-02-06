#!/usr/bin/python3

"""Contains a function that returns the list of available attributes of an object."""           


def lookup(obj):
    """returns the list of available attributes of obj"""

    return(list(dir(obj)))
