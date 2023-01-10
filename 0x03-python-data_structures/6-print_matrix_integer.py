#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """A matrix of integers"""
    for items in matrix for j in items:
        if items[-1] == j:
            print("{:d}".format(j))
        else:
            print("{:d}".format(j), end=" "))
