#!/usr/bin/python3
"""Defines a geometry base class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """Instantiate Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the areaof the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return string representation of a Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
