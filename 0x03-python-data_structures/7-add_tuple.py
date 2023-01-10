#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if not (tuple_a and tuple_b):
        tuple = (0, 0)
    if len(tuple_a) == 1:
        tuple = (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_a) == 0:
        tuple = (tuple_b[0], tuple_b[1])
    elif len(tuple_b) == 1:
        tuple = (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif len(tuple_b) == 0:
        tuple = (tuple_a[0], tuple_a[1])
    else:
        tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tuple)
