#!/usr/bin/python3

def no_c(my_string):
    """Remove c and C from a string"""
    for i in my_string:
        if ((i == c) or (i == C)):
            del i
            continue
    return (my_string)
