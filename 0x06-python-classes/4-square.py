#!/usr/bin/python3


"""Define a Square class"""


class Square:
    """A square has four equal sides"""

    def __init__(self, size=0):
        """Create a new Square object.

        Args:
            size (int): The size of the new square object
        """
        self.set__size(size)

    def get__size(self):
        """It is use to get the __size"""
        return self.__size

    def set__size(self, size):
        """It is used to set the value of __size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Define the area of the square"""
        return (self.__size * self.__size)
