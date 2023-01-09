#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple = ()
    for i in range(2):
        if ((not tuple_a[i]) or (not tuple_b[i])):
            tuple_a[i], tuple_b[i] = 0
    tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tuple)
