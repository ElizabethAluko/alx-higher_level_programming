#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number"""
    if number < 0:
        number = number * -1
    n = number % 10
    print("{:d}".format(n), end="")
    return (n)
