#!/usr/bin/python3
"""Defines a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialize a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Defines the area"""
        return (self.__size * self.__size)

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
