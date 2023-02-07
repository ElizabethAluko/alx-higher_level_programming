#!/usr/bin/python3
"""Defines a writes a string text file function"""


def write_file(filename="", text=""):
    """Write text to file and returns number of string written"""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
