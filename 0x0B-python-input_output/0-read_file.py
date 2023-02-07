#!/usr/bin/python3
"""Defines a function that reads a text and print it out"""


def read_file(filename=""):
    """Read a file and print it to stdout"""
    with open(filename, encoding = "utf-8") as f:
        print(f.read(), end="")
