#!/usr/bin/python3

def number_keys(a_dictionary):
    """ function that returns the number of keys in a dictionary."""
    k = 0
    for i, j in a_dictionary.items():
        k += 1
    return (k)

# step2
# def number_keys(a_dictionary):
#     for i, j in enumerate(a_dictionary):
#         continue
#     return (i + 1)

# step3
# def number_keys(a_dictionary):
#     return len(a_dictionary.keys())
