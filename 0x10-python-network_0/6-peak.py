#!/usr/bin/python3
"""Returns a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find the maximum of a list"""
    if len(list_of_integers) == 0:
        return
    return (max(list_of_integers))
