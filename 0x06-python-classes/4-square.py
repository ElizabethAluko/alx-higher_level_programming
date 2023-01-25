#!/usr/bin/python3


"""Define a Square class"""


class Square:
    """A square has four equal sides"""

    def __init__(self, size=0):
        """Create a new Square object.

        Args:
            size (int): The size of the new square object
        """
    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Define the area of the square"""
        return (self.__size * self.__size)
