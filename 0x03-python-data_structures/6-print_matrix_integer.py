#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """A matrix of integers"""
    if not matrix:
        return (0)
    for items in matrix:
        for j in items:
            if items[-1] == j:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
        print()
