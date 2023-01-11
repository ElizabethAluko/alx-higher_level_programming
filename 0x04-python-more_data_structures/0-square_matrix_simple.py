#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_n = [[j ** 2 for j in row] for row in matrix]
    return (matrix_n)
