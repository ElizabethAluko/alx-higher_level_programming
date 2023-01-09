#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif len(tuple_a) == 0:
        tuple = (0 + tuple_b[0], 0 + tuple_b[1])
    elif len(tuple_b) == 1:
        tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif len(tuple_b) == 0:
        tuple = (tuple_a[0] + 0, tuple_a[1] + 0)
    else:
        tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tuple)
