#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints items of a list in reverse order"""
    if not my_list:
        return(0)
    for i in range(-1, -(len(my_list) + 1), -1):
        print("{:d}".format(my_list[i]))
    return (my_list)
