#!/usr/bin/python3
"""Contains an add function that adds 2 integers"""


def add_integer(a, b=98):
    """A function that adds 2 integers

    args: a and b must be an integers or floats"""
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError('a must be an integer')
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
