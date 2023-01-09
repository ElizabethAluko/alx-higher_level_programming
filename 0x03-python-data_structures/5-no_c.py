#!/usr/bin/python3

def no_c(my_string):
    """Remove c and C from a string"""
    str = ''
    for i in my_string:
        if ((i != 'c') and (i != 'C')):
            str += i
    return (str)
