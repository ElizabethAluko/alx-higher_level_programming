#!/usr/bin/python3
"""Defines a append-a-string text file function"""


def append_write(filename="", text=""):
    """Append text to file and returns number of string append"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
