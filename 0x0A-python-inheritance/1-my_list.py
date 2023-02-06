#!/usr/bin/python3
"""Defines a class that inherits a class"""


class MyList(list):
    """Inherit list class to list the list in sorted ascending order"""

    def print_sorted(self):
        """Prints the sorted list in ascending order"""
        print(sorted(self))
