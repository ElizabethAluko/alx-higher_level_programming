#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2"""
    my_list1 = my_list[:]
    for i in range(0, len(my_list1)):
        if (my_list1[i] % 2 == 0):
            my_list1[i] = True
        else:
            my_list1[i] = False
    return (my_list1)
