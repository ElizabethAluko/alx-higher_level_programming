#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer"""
    biggest = 0
    if not my_list:
        return (None)
    for i in my_list:
        if i > biggest:
            biggest = i
        else:
            continue
    return (biggest)
