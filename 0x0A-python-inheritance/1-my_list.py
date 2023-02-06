#!/usr/bin/python3
"""Defines a class that inherits a class"""


class MyList(list):
    """Inherit list class to list"""

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
