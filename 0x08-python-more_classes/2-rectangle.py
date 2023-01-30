#!/usr/bin/python3

"""Define a Rectangle class"""


class Rectangle:
    """Empty rectangle class"""

    def __init__(self, width=0, height=0):
        """Create s new rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the object"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the object"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get or set the height of the object"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the object"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the object"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the object.
        returns 0 if either width or height is 0
        """

        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        else:
            return (2 * (self.__width + self.__height))
