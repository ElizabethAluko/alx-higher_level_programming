#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    a_dictionary2 = {}
    for key in a_dictionary:
        a_dictionary2[key] = 2 * a_dictionary[key]
    return (a_dictionary2)
