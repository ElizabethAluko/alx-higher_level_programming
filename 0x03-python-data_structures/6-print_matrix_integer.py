#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """A matrix of integers"""
    for items in matrix for j in items:
        if not (j + 1):
            print("{:d}".format(j, end=" "))
            print()
        else:
            print("{:d}".format(j, end=" "))
    print()
