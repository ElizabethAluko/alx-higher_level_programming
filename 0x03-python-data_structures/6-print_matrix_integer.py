#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """A matrix of integers"""
    for items in matrix for j in items:
        print("{}".format(j, end=" "))
    print()
